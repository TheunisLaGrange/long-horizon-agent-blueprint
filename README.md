# Autonomous Long-Horizon Agent Blueprint

A durable, state-driven autonomous agent framework designed to maintain state coherence across long-running trajectories.

## Project Directory Structure

```text
long-horizon-agent-blueprint/
│
├── .gitignore               # Excludes python cache, environments, and secrets
├── .git/                    # Git tracking history binary workspace
├── README.md                # Main map and architecture blueprint
├── CHANGELOG.md             # Historical record of design modifications
├── git_commit_guide.md      # Conventional commit standardization guidelines
│
├── config/                  
│   └── agent_config.yaml    # Centralized behavior, model, and safety configurations
│
└── src/
    ├── __init__.py          # Marks src as an imported python package
    │
    ├── diagnostics/         # 🌟 Isolated Observability Subsystem
    │   ├── __init__.py
    │   ├── telemetry.py     # StepTrace and state diagnostic structures
    │   └── analyzer.py      # Post-mortem rendering and logs compilation
    │
    └── core/                # 🚀 Core Execution & Business Logic
        ├── __init__.py
        ├── state.py         # Persistent state checkpoint management
        ├── llm_service.py   # Planner/Worker logic and step tool routing
        └── engine.py        # Central state machine loop and execution harness
```

## Design Philosophy

1. **Durable Orchestration:** The agent logs persistent state snapshots (`AgentState`) after every discrete turn. The execution path can crash, reboot, and resume directly from a checkpoint without duplicating prior work.
2. **Decoupled Diagnostics:** The core engine acts as a clean state transition layer. It remains free of reporting bloat by leveraging external telemetry packages to log data payloads.
3. **Configuration Driven Levers:** Fine-tuning model boundaries, sleep constraints, and retry loops requires editing standard configurations rather than altering production engine code.

## Getting Started

1. Ensure requirements are met: `pip install pyyaml`
2. Review commit rules: Read `git_commit_guide.md`
3. Execute the primary pipeline: `python main.py`
