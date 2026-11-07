import time
import sys
import traceback
from src.core.state import AgentState
from src.core.llm_service import LLMService
from src.diagnostics.telemetry import StepTrace

class AutonomousAgentRuntime:
    """The core state machine that controls the agent transition loop."""
    
    def __init__(self, state: AgentState):
        self.state = state
        self.llm = LLMService()

    def step_engine(self) -> bool:
        """Executes one state cycle. Returns False to pause/terminate."""
        # 1. Guard against active sleep schedules
        if self.state.status == "SLEEPING":
            if time.time() < self.state.wake_time:
                return False 
            self.state.status = "RUNNING"

        # 2. Lazy Planning Phase Initialization
        if not self.state.plan:
            self.state.status = "RUNNING"
            self.state.plan = self.llm.generate_plan(self.state.objective)
            self.state.save_checkpoint()
            return True

        # 3. Successful Goal Target Check
        if self.state.current_step_index >= len(self.state.plan):
            self.state.status = "COMPLETED"
            print("🎉 Objective achieved successfully.")
            self.state.save_checkpoint()
            return False

        current_step = self.state.plan[self.state.current_step_index]
        
        # 4. Instantiate isolated telemetry tracer node
        trace_node = StepTrace(step_name=current_step, step_index=self.state.current_step_index)
        
        try:
            # Route execution out to the tool provider
            result = self.llm.execute_step(current_step, trace_node)
            trace_node.payload = result
            
            # Trap non-exception failures immediately based on telemetry markers
            if trace_node.status == "CRITICAL_ERROR":
                raise ValueError(trace_node.diagnostic_msg)
                
            # Advance pointers and handle rate throttling configurations
            self.state.current_step_index += 1
            if self.state.current_step_index < len(self.state.plan):
                self.state.status = "SLEEPING"
                self.state.wake_time = time.time() + 1
            
            # Serialize trace metrics and dump state snapshots
            self.state.trace_history.append(trace_node.to_dict())
            self.state.save_checkpoint()
            return True

        except Exception as e:
            # Trap system failures, environment faults, and custom logic exceptions safely
            self.state.status = "FAILED"
            
            # Fallback wrapper if exceptions crash the execution layer unexpectedly
            if trace_node.status != "CRITICAL_ERROR":
                trace_node.status = "CRITICAL_ERROR"
                trace_node.error_code = type(e).__name__
                trace_node.diagnostic_msg = "".join(traceback.format_exception(*sys.exc_info()))
            
            self.state.trace_history.append(trace_node.to_dict())
            print(f"❌ Trajectory broken at step {self.state.current_step_index}. Initiating recovery protocols.")
            self.state.save_checkpoint()
            return False
