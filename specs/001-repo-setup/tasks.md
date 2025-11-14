---
description: "Task list for AI-Native Repository Setup implementation (updated 2025-11-13)"
---

# Tasks: AI-Native Repository Setup

**Input**: Design documents from `/specs/001-repo-setup/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/

**Tests**: Tests are included per constitution principle VII (NON-NEGOTIABLE: 100% test coverage enforced via pre-commit hook)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

**Updated**: 2025-11-13 to align with current plan.md (Python 3.12+ primary, Node.js 20+ utilities, mem0ai, Spec-kit CLI, structured logging, constitution governance, agent definitions)

## Technical Context

**Language/Version**: Python 3.12+ (primary), Node.js 20+ (utilities)  
**Primary Dependencies**: mem0ai (agent memory), Spec-kit CLI, structlog (logging), black (formatter), pytest (testing)  
**Storage**: File system for constitution/specs/templates; mem0 backend for agent memory (default: Qdrant vector store)  
**Testing**: pytest for Python, Jest for Node.js utilities  
**Performance Goals**: <10 min full initialization, <30 min feature workflow, <500ms agent memory retrieval  
**Constraints**: Minimal external dependencies, no print statements (structured logging only), 100% test coverage enforced  
**Scale/Scope**: 5+ concurrent features, 100+ specifications, single-repo architecture

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

Single project structure at repository root per plan.md:
- `src/` - Source code (agents/, workflows/, utils/)
- `tests/` - Three-tier structure (unit/, integration/, contract/)
- `.specify/` - Templates, memory (constitution.md), scripts (bash/, python/)
- `.git/hooks/` - Pre-commit hooks for coverage enforcement
- Configuration files at root (pyproject.toml, package.json, .vscode/, AGENTS.md, copilot-instructions.md)

---

## Phase 0: Prerequisites Validation (New - FR-016)

**Purpose**: Proactive validation to prevent mid-workflow failures

- [ ] T000a [P] Create .specify/scripts/bash/prereq-checker.sh to validate Python 3.12+, Node 20+, npm, uv, git, mem0ai, disk space per FR-016
- [ ] T000b Run prereq-checker.sh with --json flag to verify all prerequisites before setup

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T000 [P] Verify uv installed via `uv --version`, install if missing using `curl -LsSf https://astral.sh/uv/install.sh | sh`
- [X] T001 Create Python virtual environment using uv venv in project root
- [X] T002 [P] Create project directory structure: src/, tests/, .specify/ per plan.md
- [X] T003 [P] Create pyproject.toml with Python 3.12+ config, dependencies (mem0ai, structlog, pytest, pytest-cov, black, mypy), and pytest-cov config (fail_under=100)
- [X] T004 [P] Create package.json for Node.js utilities with ESLint and Prettier
- [X] T005 [P] Create .gitignore for Python (.venv/, __pycache__/, .pytest_cache/, .coverage, .mem0/)
- [ ] T006 [P] Create .vscode/settings.json with Python interpreter path, formatters, and Copilot config
- [X] T007 [P] Create .vscode/extensions.json recommending GitHub Copilot and Python extensions
- [X] T008 Install Python dependencies using uv pip install in activated virtual environment
- [X] T008a [P] Create .pre-commit-config.yaml for pytest-cov hook per FR-011

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T009 Create src/utils/logging.py with structlog JSON formatter and correlation ID processor
- [X] T010 [P] Create src/utils/validation.py with input validation utilities (string patterns, file paths) per FR-017
- [X] T011 [P] Create src/utils/config.py for environment variable and configuration management
- [X] T012 [P] Create tests/unit/test_utils.py for logging, validation, and config utilities
- [X] T013 [P] Create README.md with project overview, prerequisites (including mem0ai per spec), and quick start reference
- [X] T014 Run pytest to verify foundational utilities pass tests with 100% coverage

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Initialize Core Repository Structure (Priority: P1) 🎯 MVP

**Goal**: Establish .specify/ directory with templates, constitution, AGENTS.md, and copilot-instructions.md

**Independent Test**: Run `specify --version` and verify .specify/ directory exists with all templates and constitution.md populated

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T015 [P] [US1] Create tests/integration/test_specify_init.py for Spec-kit initialization validation
- [ ] T016 [P] [US1] Create tests/unit/test_constitution.py for constitution entity validation
- [ ] T017 [P] [US1] Create tests/integration/test_templates.py for template structure validation

### Implementation for User Story 1

- [ ] T018 [US1] Verify Spec-kit CLI installed via `specify --version`, install if missing using uv tool install
- [ ] T019 [US1] Run `specify init --ai copilot --here` to create .specify/ directory structure
- [ ] T020 [US1] Verify .specify/templates/ contains spec-template.md, plan-template.md, tasks-template.md, checklist-template.md
- [ ] T021 [US1] Create or verify .specify/memory/constitution.md exists with 7 principles from plan
- [ ] T022 [US1] Create AGENTS.md at repository root with orchestrator and memory_agent definitions per quickstart.md
- [ ] T023 [US1] Create copilot-instructions.md at repository root with role assignment, chain-of-thought, and few-shot examples per quickstart.md
- [ ] T024 [US1] Create .specify/scripts/python/ directory for Python automation scripts
- [ ] T025 [US1] Verify all templates are accessible and follow constitution principles
- [ ] T026 [US1] Run integration tests to verify Spec-kit initialization and template structure

**Checkpoint**: User Story 1 complete - Repository has foundational AI-native structure and can generate specifications

---

## Phase 4: User Story 2 - Configure AI Agent Memory and Context (Priority: P2)

**Goal**: Integrate mem0ai for agent memory persistence with hierarchical key structure

**Independent Test**: Store test context via mem0, retrieve in new Python session, verify persistence and search functionality

### Tests for User Story 2 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T027 [P] [US2] Create tests/integration/test_mem0_integration.py for memory storage and retrieval
- [ ] T028 [P] [US2] Create tests/unit/test_memory_agent.py for memory agent logic validation
- [ ] T029 [P] [US2] Create tests/contract/test_agent_api.py for memory API endpoints per contracts/agent-api.yaml

### Implementation for User Story 2

- [ ] T030 [P] [US2] Create src/agents/memory_agent.py with MemoryAgent class implementing storage/search/delete
- [ ] T031 [US2] Implement hierarchical key validation in memory_agent.py (pattern: namespace:branch:feature:context_type per FR-020)
- [ ] T032 [US2] Create .specify/scripts/python/mem0_setup.py to initialize mem0 with file-based backend
- [ ] T032a [US2] Add mem0 backend fallback logic per FR-018: Qdrant primary, file-based on failure with warning
- [ ] T033 [US2] Implement memory context expiration logic in memory_agent.py
- [ ] T034 [US2] Add memory backup/restore functionality to .specify/scripts/python/mem0_setup.py
- [ ] T035 [P] [US2] Create src/agents/__init__.py to export MemoryAgent
- [ ] T036 [US2] Test mem0 integration: store test context, verify retrieval and search
- [ ] T037 [US2] Run contract tests to validate memory API endpoints
- [ ] T038 [US2] Document memory key conventions in AGENTS.md including branch namespacing
- [ ] T038a [US2] Add branch-based namespacing to memory keys per FR-020 for concurrent development (format: namespace:branch:feature:context_type)
- [ ] T038b [US2] Test memory isolation per SC-006: create contexts on different branches and verify no cross-contamination

**Checkpoint**: User Story 2 complete - Agents can store and retrieve context across sessions

---

## Phase 5: User Story 4 - Enable Spec-Kit Workflow Commands (Priority: P2)

**Goal**: Implement workflows for /speckit.specify, /speckit.plan, /speckit.tasks, /speckit.implement

**Independent Test**: Run each command in sequence on test feature, verify generated artifacts follow templates and pass constitution checks

### Tests for User Story 4 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T039 [P] [US4] Create tests/integration/test_speckit_commands.py for workflow command validation
- [ ] T040 [P] [US4] Create tests/unit/test_workflows.py for workflow logic unit tests
- [ ] T041 [P] [US4] Create tests/integration/test_constitution_check.py for compliance validation

### Implementation for User Story 4

- [ ] T042 [P] [US4] Create src/workflows/constitution.py with ConstitutionWorkflow class for principle validation
- [ ] T043 [P] [US4] Create src/workflows/specify.py with SpecifyWorkflow class for spec generation
- [ ] T044 [P] [US4] Create src/workflows/plan.py with PlanWorkflow class for plan generation
- [ ] T045 [US4] Implement constitution check logic in constitution.py (validate against 7 principles)
- [ ] T046 [US4] Implement specification generation in specify.py (parse user input, fill template)
- [ ] T047 [US4] Implement plan generation in plan.py (extract tech context, generate research)
- [ ] T048 [P] [US4] Create src/workflows/__init__.py to export workflow classes
- [ ] T049 [US4] Integrate workflows with memory agent for context storage
- [ ] T050 [US4] Test workflow sequence: specify → plan → tasks with test feature
- [ ] T051 [US4] Verify generated artifacts pass constitution checks
- [ ] T051a [US4] Implement constitution validation failure handling per FR-013 with specific error reporting (failing principles, line refs, example fixes)
- [ ] T052 [US4] Run integration tests for all workflow commands

**Checkpoint**: User Story 4 complete - Full Spec-kit workflow operational from specification to tasks

---

## Phase 6: User Story 3 - Establish Code Hardening Workflow (Priority: P3)

**Goal**: Implement four-phase code hardening process with security, performance, architecture reviews

**Independent Test**: Submit Python code snippet, execute all 4 phases, verify threat model, hardened code, critique, and test cases generated

### Tests for User Story 3 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T053 [P] [US3] Create tests/unit/test_hardening.py for hardening workflow phase logic
- [ ] T054 [P] [US3] Create tests/integration/test_hardening_workflow.py for full workflow execution
- [ ] T055 [P] [US3] Create tests/contract/test_hardening_api.py for workflow API endpoints

### Implementation for User Story 3

- [ ] T056 [P] [US3] Create src/workflows/hardening.py with HardeningWorkflow class
- [ ] T056a [US3] Add language validation to hardening.py per FR-019 (Python/Node.js only, error on unsupported with supported languages list)
- [ ] T057 [P] [US3] Implement Phase 1 (Intake & Strategy) with threat modeling in hardening.py
- [ ] T058 [US3] Implement Phase 2 (Implementation) with code generation and validation in hardening.py
- [ ] T059 [US3] Implement Phase 3 (RCI - Recursive Critique) with multi-perspective review in hardening.py
- [ ] T060 [US3] Implement Phase 4 (Verification & Delivery) with test generation in hardening.py
- [ ] T061 [US3] Add phase gate approval mechanism to hardening.py
- [ ] T062 [US3] Create .specify/scripts/python/hardening_workflow.py CLI wrapper for hardening workflow
- [ ] T063 [US3] Integrate hardening workflow with memory agent for critique history storage
- [ ] T064 [US3] Test hardening workflow with sample Python code containing security vulnerabilities
- [ ] T065 [US3] Verify threat model includes CWE IDs and severity ratings per SC-004
- [ ] T066 [US3] Verify Phase 4 generates pytest test cases
- [ ] T067 [US3] Run integration tests for complete hardening workflow

**Checkpoint**: User Story 3 complete - Production-ready code hardening available for security and quality assurance

---

## Phase 7: MCP Coordination (Cross-Cutting)

**Purpose**: Enable multi-agent coordination via Model Context Protocol

- [ ] T068 [P] Create src/agents/orchestrator.py with MCPCoordinator class for agent coordination
- [ ] T069 [P] Create tests/unit/test_orchestrator.py for orchestrator logic validation
- [ ] T070 [P] Create tests/integration/test_mcp_integration.py for MCP coordination testing
- [ ] T071 Create .specify/scripts/python/mcp_coordinator.py with asyncio message routing
- [ ] T072 Implement agent registration in orchestrator.py (register_agent method)
- [ ] T073 Implement task coordination in orchestrator.py (coordinate method with asyncio.Queue)
- [ ] T074 Implement agent health checks in orchestrator.py
- [ ] T075 Integrate orchestrator with memory agent and workflow agents
- [ ] T076 Test MCP coordination: route task to multiple agents, aggregate results
- [ ] T077 Run integration tests for MCP coordination functionality

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Documentation, configuration, and final integration

- [ ] T078 [P] Update README.md with complete setup instructions, architecture diagram, and examples
- [ ] T079 [P] Create CONTRIBUTING.md with development workflow and constitution compliance guidelines
- [ ] T080 [P] Create docs/ directory with architecture.md documenting system design
- [ ] T081 [P] Add inline documentation (docstrings) to all public functions and classes per PEP 257
- [ ] T082 Run black formatter on all Python files to ensure PEP 8 compliance
- [ ] T083 Run mypy type checker on all Python files to validate type hints
- [ ] T084 Run pytest with coverage report to verify 100% test coverage requirement per FR-011 and SC-007
- [ ] T084a [P] Create pre-commit hook script in .git/hooks/pre-commit to enforce 100% coverage per FR-011
- [ ] T084b Configure pytest-cov in pyproject.toml with fail_under = 100 per FR-011
- [ ] T085 Create .github/workflows/ci.yml for automated testing and linting (optional CI/CD)
- [ ] T086 Perform final constitution check across all generated artifacts per FR-013
- [ ] T087 Create quickstart tutorial demonstrating full workflow (specify → implement)
- [ ] T088 Review and update .gitignore to exclude all generated and temporary files
- [ ] T088a Create example extension script in .specify/scripts/python/example_validator.py per FR-012 with documentation
- [ ] T089 Final integration test per SC-005: Create new feature using all workflows, verify end-to-end (under 30 min for 3-5 stories)
- [ ] T089a Integration test for concurrency per SC-006: Run 5 parallel feature workflows and verify no memory conflicts

---

## Dependencies & Execution Strategy

### User Story Dependencies

```
Setup (Phase 1) ──┐
                  │
                  ├──→ Foundational (Phase 2) ──┐
                  │                              │
                  │                              ├──→ US1 (P1) ──┐
                  │                              │                │
                  │                              ├──→ US2 (P2) ──┤
                  │                              │                ├──→ US4 (P2) ──┐
                  │                              ├──→ US3 (P3) ──┘                │
                  │                                                                │
                  └────────────────────────────────────────────────────────────→ MCP & Polish
```

**Completion Order**:
1. Setup → Foundational (sequential, blocking)
2. US1 (P1) MUST complete first (provides templates and constitution)
3. US2 (P2), US3 (P3), US4 (P2) can start after US1 (parallel where possible)
4. US4 depends on US2 (workflows need memory agent)
5. MCP coordination can integrate after US2 and US4
6. Polish after all user stories complete

### Parallel Execution Opportunities

**Within US1 (Phase 3)**:
- T015, T016, T017 (tests) can run in parallel
- T022, T023 (agent definitions) can run in parallel after T021

**Within US2 (Phase 4)**:
- T027, T028, T029 (tests) can run in parallel
- T030, T031, T032 (implementation) have dependencies, sequential

**Within US4 (Phase 5)**:
- T039, T040, T041 (tests) can run in parallel
- T042, T043, T044 (workflow classes) can run in parallel
- T045, T046, T047 (workflow logic) have dependencies, sequential

**Within US3 (Phase 6)**:
- T053, T054, T055 (tests) can run in parallel
- T056, T057 (setup and Phase 1) can run in parallel

**MCP Phase (Phase 7)**:
- T068, T069, T070, T071 can run in parallel (different files)

**Polish Phase (Phase 8)**:
- T078, T079, T080, T081 (documentation) can run in parallel

### MVP Scope Recommendation

**Minimum Viable Product** = Phase 1 + Phase 2 + Phase 3 (US1 only)

This delivers:
- ✅ Repository structure with .specify/ directory
- ✅ Constitution with 7 principles
- ✅ Agent definitions (AGENTS.md)
- ✅ Copilot instructions
- ✅ Template system functional
- ✅ Foundation for adding features

**MVP Tasks**: T001-T026 (26 tasks, ~4-6 hours)

### Incremental Delivery Strategy

1. **Sprint 1** (MVP): Setup + Foundational + US1 → Delivers working repository structure
2. **Sprint 2**: US2 + US4 → Delivers memory and workflow capabilities
3. **Sprint 3**: US3 + MCP → Delivers hardening and coordination
4. **Sprint 4**: Polish → Production-ready release

---

## Task Summary

**Total Tasks**: 100 (updated 2025-11-13 - aligned with current plan.md technical context and structure)

**Tasks by Phase**:
- Phase 0 (Prerequisites): 2 tasks (prereq validation per FR-016)
- Phase 1 (Setup): 10 tasks (Python 3.12+/Node.js 20+ environment, pre-commit config)
- Phase 2 (Foundational): 6 tasks (structured logging, validation, config per plan.md)
- Phase 3 (US1 - P1): 12 tasks (Spec-kit templates, constitution, agent definitions)
- Phase 4 (US2 - P2): 15 tasks (mem0ai integration, branch namespacing per plan.md)
- Phase 5 (US4 - P2): 15 tasks (workflow commands, constitution validation)
- Phase 6 (US3 - P3): 16 tasks (4-phase hardening workflow per plan.md)
- Phase 7 (MCP): 10 tasks (orchestrator agent coordination)
- Phase 8 (Polish): 14 tasks (documentation, coverage enforcement, final integration)

**Tasks by User Story**:
- US1 (Initialize Structure): 12 tasks
- US2 (Memory & Context): 15 tasks (added FR-018, FR-020 coverage)
- US3 (Code Hardening): 16 tasks (added FR-019 coverage)
- US4 (Workflow Commands): 15 tasks (added FR-013, FR-017 coverage)
- Infrastructure: 42 tasks (Phase 0, Setup, Foundational, MCP, Polish - added FR-011, FR-012, FR-016 coverage)

**Test Tasks**: 12 tasks (100% coverage enforced via pre-commit hook per FR-011)
**Parallel Opportunities**: 36 tasks marked [P] (36%)

**Estimated Effort**:
- Prerequisites: 0.5 hours
- MVP (US1): 4-6 hours
- US2 + US4: 7-9 hours
- US3: 5-7 hours
- MCP + Polish: 5-7 hours
- **Total**: 21.5-29.5 hours

**Edge Case Coverage**:
- FR-016 (prerequisite failures): T000a, T000b
- FR-017 (validation failures): T010, T051a
- FR-018 (mem0 fallback): T032a
- FR-019 (language validation): T056a
- FR-020 (branch namespacing): T031, T038a, T038b

---

## Validation Checklist

✅ **Format Compliance**:
- [x] All tasks use checkbox format `- [ ]`
- [x] All tasks have sequential IDs (T001-T089)
- [x] Parallel tasks marked with [P]
- [x] User story tasks marked with [US1], [US2], [US3], [US4]
- [x] All tasks include specific file paths
- [x] Test tasks precede implementation tasks per TDD

✅ **Organization**:
- [x] Tasks organized by user story priority (P1 → P2 → P3)
- [x] Each user story is independently testable
- [x] Dependencies clearly documented
- [x] Parallel execution opportunities identified

✅ **Completeness**:
- [x] All entities from data-model.md mapped to tasks
- [x] All functional requirements (FR-001 to FR-020) covered
- [x] All success criteria (SC-001 to SC-008) have validation tasks
- [x] All edge cases (FR-016 to FR-020) have implementation tasks
- [x] Enforcement mechanisms implemented (pre-commit hook, validation, fallback)
- [x] Measurement methodologies included (time command, pytest-cov, concurrency tests)
- [x] All endpoints from contracts/ mapped to tasks
- [x] All tech decisions from research.md addressed
- [x] Constitution principle VII satisfied (100% test coverage)

✅ **Executability**:
- [x] MVP scope defined (Phase 1-3)
- [x] Incremental delivery strategy provided
- [x] Each task has clear acceptance criteria
- [x] File paths enable immediate implementation

---

**Next Command**: `/speckit.implement` to begin executing tasks (or manually implement task by task)