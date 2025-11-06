---

description: "Tasks for AI-Native AWS Setup — Update"
---

# Tasks: AI-Native AWS Setup — Update

**Input**: Design documents from `/specs/002-ai-native-aws-setup/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/

**Tests**: This feature is documentation- and workflow-focused. Formal tests are optional; rely on checklist validation and the read-only AWS smoke test.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish baseline files and configs required by all stories

- [ ] T001 Create environment template at .env.example with placeholders for AWS_REGION (default us-east-1) and AWS_PROFILE
- [ ] T002 [P] Verify .gitignore includes `.env` and `.env.*` entries in .gitignore (add if missing)
- [ ] T003 [P] Verify MCP config exists at .github/mcp/aws-mcp-config.json (create or align with README references if missing)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Ensure governance references and anchors exist across docs

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 Ensure AGENTS.md mentions official AWS MCP servers and default region behavior (update AGENTS.md)

**Checkpoint**: Foundation ready — user story implementation can now begin in parallel

---

## Phase 3: User Story 1 — Align setup with governance and MCP (Priority: P1) 🎯 MVP

**Goal**: Update assets so contributors and agents follow the constitution, use official AWS MCP servers, and default to the correct region with safe, read-only validation.

**Independent Test**: Documentation review confirms README links to AGENTS.md and Constitution, `.github/mcp/aws-mcp-config.json` is referenced, and the MCP smoke test can be executed end-to-end.

### Implementation for User Story 1

- [ ] T005 [US1] Add/confirm README links to AGENTS.md and .specify/memory/constitution.md in README.md
- [ ] T006 [P] [US1] Reference .github/mcp/aws-mcp-config.json in README.md with note on default region override via .env
- [ ] T007 [P] [US1] Create/verify smoke test contract at specs/002-ai-native-aws-setup/contracts/mcp-smoke-test.contract.md for sts:GetCallerIdentity
- [ ] T008 [US1] Add troubleshooting section for MCP/read-only identity check in README.md

**Checkpoint**: User Story 1 complete — governance alignment and MCP references verifiable independently

---

## Phase 4: User Story 2 — Bootstrap with updated quickstart (Priority: P2)

**Goal**: Provide an easy, ≤10-minute bootstrap with `.env` setup, AWS SSO sign-in, and read-only connectivity validation.

**Independent Test**: Follow quickstart from a fresh environment; complete within the target time and verify `aws sts get-caller-identity` succeeds.

### Implementation for User Story 2

- [ ] T009 [US2] Ensure quickstart at specs/002-ai-native-aws-setup/quickstart.md includes: fetch/prune, copy .env.example, set AWS_REGION, aws sso login, and sts get-caller-identity
- [ ] T010 [P] [US2] Add link from README.md to specs/002-ai-native-aws-setup/quickstart.md (e.g., in Getting Started/Quickstart section)
- [ ] T011 [P] [US2] Finalize .env.example placeholders (AWS_REGION=us-east-1 comment, AWS_PROFILE example) at repository root
- [ ] T012 [US2] Add AGENTS.md note on using AWS SSO and `.env` region override to match quickstart

**Checkpoint**: User Story 2 complete — a new contributor can bootstrap and verify read-only AWS access in ≤10 minutes

---

## Phase 5: User Story 3 — Numbering and short-name conventions (Priority: P3)

**Goal**: Clarify `NNN-<short-name>` rules and the compute-next-number process across remote branches, local branches, and specs directories.

**Independent Test**: Using the documented steps, create a new feature with the next number correctly computed for an exact short-name match.

### Implementation for User Story 3

- [ ] T013 [US3] Document numbering and short-name rules in README.md (Workflow section), including `git fetch --all --prune` pre-step
- [ ] T014 [P] [US3] Add explicit steps to AGENTS.md for computing next number (remote branches, local branches, specs directories) with exact short-name matching
- [ ] T015 [US3] Cross-check specs/002-ai-native-aws-setup/spec.md acceptance criteria are reflected in README and AGENTS.md wording

**Checkpoint**: User Story 3 complete — numbering docs enable deterministic, independent feature creation

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Consistency and quality across documentation and configs

- [ ] T016 [P] Validate README.md links to AGENTS.md, Constitution, and Quickstart resolve correctly
- [ ] T017 [P] Ensure default region wording and `.env` override are consistent across README.md, AGENTS.md, specs/002-ai-native-aws-setup/quickstart.md, and contracts/mcp-smoke-test.contract.md
- [ ] T018 Run a final checklist review against specs/002-ai-native-aws-setup/checklists/requirements.md and update docs as needed

---

## Dependencies & Execution Order

### Phase Dependencies

- Setup (Phase 1): No dependencies — can start immediately
- Foundational (Phase 2): Depends on Setup completion — BLOCKS all user stories
- User Stories (Phase 3+): Depend on Foundational completion
  - Stories can proceed in parallel if staffed
  - Or sequentially in priority order (P1 → P2 → P3)
- Polish (Final Phase): Depends on completing desired user stories

### User Story Dependencies

- User Story 1 (P1): Can start after Foundational — no dependencies on other stories
- User Story 2 (P2): Can start after Foundational — independent of US1, but references quickstart link from README
- User Story 3 (P3): Can start after Foundational — independent of US1/US2, but cross-references docs

### Within Each User Story

- For this documentation feature: edit files atomically; prefer small commits
- Keep stories independently verifiable to allow partial merges if needed

### Parallel Opportunities

- Setup: T002 and T003 can run in parallel
- US1: T006 and T007 can run in parallel
- US2: T010 and T011 can run in parallel
- US3: T014 can run in parallel with T013/T015 (different files)
- Polish: T016 and T017 can run in parallel

---

## Parallel Example: User Story 1

```bash
# Parallelizable tasks for US1 (different files)
Task: "Reference .github/mcp/aws-mcp-config.json in README.md with default region note" (T006)
Task: "Create/verify smoke test contract at specs/002-ai-native-aws-setup/contracts/mcp-smoke-test.contract.md" (T007)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. STOP and VALIDATE: Verify governance links and run read-only smoke test
5. Merge or demo if ready

### Incremental Delivery

1. Setup + Foundational → baseline
2. Add US1 → validate independently (MVP)
3. Add US2 → validate quickstart flow
4. Add US3 → validate numbering flow

### Parallel Team Strategy

- After Foundational: assign US1, US2, US3 to different contributors
- Use small PRs; verify each story independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] labels used only in user story phases
- Each user story is independently deliverable and testable
- Avoid cross-story coupling; prefer explicit references and links
