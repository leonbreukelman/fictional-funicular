# Tasks: Bootstrap AI-Native AWS Setup

Feature: specs/001-ai-native-aws-setup/spec.md
Plan: specs/001-ai-native-aws-setup/plan.md
Branch: 001-ai-native-aws-setup
Created: 2025-11-06

## Phase 1: Setup (project initialization)

- [ ] T001 Create .env.example with placeholders at ./.env.example
- [ ] T002 Update .gitignore to ignore .env and local artifacts at ./.gitignore
- [ ] T003 Create or verify AWS MCP config file at ./.github/mcp/aws-mcp-config.json
- [ ] T004 Create or verify Copilot context file with usage norms at ./.github/copilot-instructions.md
- [ ] T005 Add Quickstart and Governance links to README at ./README.md
- [ ] T006 [P] Add Makefile skeleton with phony targets at ./Makefile

## Phase 2: Foundational (blocking prerequisites)

- [ ] T007 Implement bootstrap target: check uv, specify-cli, aws cli; print guidance at ./Makefile
- [ ] T008 [P] Implement specify target: wrap .specify/scripts/bash/create-new-feature.sh at ./Makefile
- [ ] T009 Implement plan target: wrap .specify/scripts/bash/setup-plan.sh at ./Makefile
- [ ] T010 [P] Implement tasks target: wrap .specify/scripts/bash/check-prerequisites.sh at ./Makefile
- [ ] T011 Implement implement and analyze targets (pass-through stubs) at ./Makefile
- [ ] T012 [P] Implement mcp-smoke target (delegates to script) at ./Makefile

## Phase 3: User Story 1 — Bootstrap a fresh clone (P1)

Goal: New contributor completes bootstrap; core files present; governance discoverable; smoke checks pass without cloud changes.
Independent Test: Follow Quickstart; verify files, docs presence, and non-impact checks run without errors.

- [ ] T013 [US1] Finalize Quickstart steps and troubleshooting at ./specs/001-ai-native-aws-setup/quickstart.md
- [ ] T014 [P] [US1] Declare Copilot as default AI and norms at ./AGENTS.md
- [ ] T015 [US1] Ensure Constitution baseline principles and gates are present at ./.specify/memory/constitution.md
- [ ] T016 [P] [US1] Add optional verify-bootstrap target to check presence of required files at ./Makefile

## Phase 4: User Story 2 — Create a new feature spec (P2)

Goal: Trigger spec workflow to create NNN-<short-name> branch and spec stub quickly.
Independent Test: Run specify target with description; new branch + specs directory created and populated.

- [ ] T017 [US2] Document specify flow, naming, and numbering in README at ./README.md
- [ ] T018 [P] [US2] Add guard/docs for unique numeric prefixes and recovery steps at ./README.md
- [ ] T019 [US2] Link relevant prompt file for reference at ./.github/prompts/speckit.specify.prompt.md

## Phase 5: User Story 3 — Verify AWS MCP connectivity safely (P3)

Goal: Validate read-only AWS connectivity using SSO with no mutations.
Independent Test: Run mcp-smoke target; command finishes ≤5s; prints identity/region; no mutations.

- [ ] T020 [US3] Create mcp-smoke script using `aws sts get-caller-identity` at ./.specify/scripts/bash/mcp-smoke.sh
- [ ] T021 [P] [US3] Add SSO login + smoke test docs to Quickstart at ./specs/001-ai-native-aws-setup/quickstart.md
- [ ] T022 [US3] Extend .env.example with region/profile placeholders at ./.env.example
- [ ] T023 [P] [US3] Add least-privilege dev role guidance to agents doc at ./AGENTS.md

## Final Phase: Polish & Cross-Cutting

- [ ] T024 Link Quickstart prominently in README’s top section at ./README.md
- [ ] T025 [P] Add “no secrets in repo” checklist to README or CONTRIBUTING at ./README.md

## Dependencies (story completion order)

1. Phase 1: Setup → 2. Phase 2: Foundational → 3. US1 (P1) → 4. US2 (P2) → 5. US3 (P3) → 6. Polish

## Parallel execution examples

- T006 (Makefile skeleton) can run in parallel with T003 (MCP config) and T004 (Copilot context)
- T008 (specify target) can run in parallel with T010 (tasks target) and T012 (mcp-smoke target)
- In US1, T014 (AGENTS.md) can run in parallel with T016 (verify-bootstrap target)
- In US3, T021 (Quickstart docs) can run in parallel with T023 (AGENTS least-privilege guidance)

## Implementation strategy (MVP first)

- MVP: Complete Phases 1–2 and US1 (P1) — this yields a working bootstrap with governance and docs
- Next: US2 (spec creation) for planning flow, then US3 (AWS connectivity) for environment validation
- Finally: Polish tasks to streamline onboarding and guardrails

## Format validation

All tasks follow format: `- [ ] T### [P] [US#] Description with file path` (Story label only for US phases). Checked for unique IDs and explicit file paths.

## Summary

- Output: specs/001-ai-native-aws-setup/tasks.md
- Total tasks: 25
- Per story: US1=4, US2=3, US3=4 (remaining belong to Setup/Foundational/Polish)
- Parallel opportunities: 8 examples provided
- Independent tests: Defined per user story
