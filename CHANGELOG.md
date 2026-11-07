# Changelog

All notable changes to this agent system will be documented here.

## - 2026-11-07
### Added
- Created `config/agent_config.yaml` to decouple runtime parameters from application code.
- Added a global `max_trajectory_steps` safety guardrail in `main.py` to prevent infinite execution loops and API runaway costs.

## - 2026-11-07
### Changed
- Refactored repository into a modular directory structure (`src/core` and `src/diagnostics`) to satisfy the Single Responsibility Principle.
- Replaced basic print tracking with a structural `StepTrace` system to preserve step payloads and capture exception stacks.

## - 2026-11-07
### Added
- Initial proof-of-concept state machine loop with durable checkpoint structures.
