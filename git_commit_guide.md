# Git Commit Message Guide

To maintain a clean, readable project history, this repository follows the Conventional Commits specification. This structural transparency allows the team (and automated CI pipelines) to track changes across prompts, configurations, and core python logic.

## Commit Message Format

Each commit message consists of a **header**, a **body**, and a **footer**. The header has a special format that includes a **type** and a **subject**:

```text
<type>: <subject>

[optional body]

[optional footer(s)]
```

### 1. Allowed Types

*   `feat`: A new feature implemented in the agent engine, core state, or tool ecosystem.
*   `fix`: A bug fix (e.g., resolving string casing mismatches or parsing discrepancies).
*   `prompt`: Modifications made to LLM text generation, behavioral context, or persona configurations.
*   `config`: Non-code parameter fine-tuning (modifying `agent_config.yaml`, sleep delays, or timeouts).
*   `refactor`: Structural optimization of production code that does not alter external functionality (e.g., isolating subsystems).
*   `docs`: Documentation adjustments (updating `README.md`, diagrams, or this guide).
*   `test`: Introducing, refining, or replacing runtime evaluators or mocking scripts.

### 2. Concrete Examples

#### Engineering a New Step Execution Loop
```text
feat: integrate structured step telemetry into the runtime orchestrator

Introduced the StepTrace primitive inside src/diagnostics to systematically 
capture execution snapshots. Updated engine.py to generate post-mortem analysis logs.
```

#### Correcting a Critical Discrepancy
```text
fix: resolve string case mismatch inside LLM tool matching criteria

Converted worker string matching paths to use lowercase comparisons. This eliminates
the SCHEMA_MATCH_DISCREPANCY failure encountered during report generation tasks.
```

#### Tuning Trajectory Constraints
```text
config: adjust agent sleep windows and maximum trajectory limit

Increased self_scheduling_delay to 2 seconds to proactively mitigate API throttling.
Reduced max_trajectory_steps to 20 to prevent runaway computation costs.
```

---

## Branching Guidelines

*   `main`: The clean, production-ready core. Direct commits are restricted.
*   `feature/*`: Branching strategy for implementing fresh capabilities or tools.
*   `fix/*`: Branching strategy for tracking and engineering bug resolutions.
