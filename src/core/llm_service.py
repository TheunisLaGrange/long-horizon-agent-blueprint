import sys
from typing import Dict, List, Any
from src.diagnostics.telemetry import StepTrace  # Import explicit tracing primitives

class LLMService:
    """Handles core cognitive duties (Planning and Execution Tool Routing)."""
    
    @staticmethod
    def generate_plan(objective: str) -> List[str]:
        print(f"[Planner LLM] Breaking down objective: '{objective}'")
        return [
            "Fetch data from source API",
            "Process payload and look for anomalies",
            "Generate structured summary report"
        ]

    @staticmethod
    def execute_step(step: str, trace: StepTrace) -> Dict[str, Any]:
        """Executes worker actions while populating generic telemetry fields."""
        print(f"[Worker LLM] Executing task: '{step}'")
        
        # Simulating the case-sensitivity schema discrepancy edge-case
        if "Fetch" in step:
            trace.status = "SUCCESS"
            return {"records": 105, "status": "fetched"}
        elif "Process" in step:
            trace.status = "SUCCESS"
            return {"anomalies_found": 3}
        elif "Report" in step:
            trace.status = "SUCCESS"
            return {"artifact_path": "/outputs/report.md"}
        
        # Populate explicit error context in the trace structure on failure
        trace.status = "CRITICAL_ERROR"
        trace.error_code = "SCHEMA_MATCH_DISCREPANCY"
        trace.diagnostic_msg = (
            f"The task description string '{step}' failed to match any registered tool routing keys. "
            f"Check casing conventions or model routing configuration alignment."
        )
        return {}
