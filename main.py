import time
from src.core.state import AgentState
from src.core.engine import AutonomousAgentRuntime # (Preserved engine logic)
from src.diagnostics.analyzer import TraceAnalyzer

if __name__ == "__main__":
    # 1. Initialize clean state
    state = AgentState(objective="Audit nightly compliance records")
    runtime = AutonomousAgentRuntime(state=state)

    print("=== STARTING AGENT TRAJECTORY ===")
    while state.status not in ["COMPLETED", "FAILED"]:
        runtime.step_engine()
        time.sleep(0.5)

    print(f"=== TRAJECTORY CONCLUDED WITH STATUS: {state.status} ===")
    
    # 2. Hand data over to the diagnostic module ONLY when needed
    TraceAnalyzer.print_post_mortem(state.session_id, state.trace_history)
