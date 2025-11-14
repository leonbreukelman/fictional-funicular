# Requirements Quality Checklist: AI-Native AWS Setup — Update (aws-setup)

**Purpose**: Unit tests for the requirements (English) — validate completeness, clarity, consistency, measurability, and coverage for this feature’s spec/plan/tasks
**Created**: 2025-11-06
**Feature**: [Spec](../spec.md) | [Plan](../plan.md) | [Tasks](../tasks.md) | [Quickstart](../quickstart.md)
**Depth**: Standard (author drafting aid)
**Audience/Timing**: Author during drafting and refinement
**Focus Areas**: Governance links & consistency; Region & environment semantics
**Exclusions**: Performance tuning beyond timing criteria already in the spec

## Requirement Completeness

- [ ] CHK001 Are governance linkage requirements (README → AGENTS.md → Constitution) explicitly documented with locations and link text? [Completeness, Spec §FR-001]
- [ ] CHK002 Are onboarding steps for env setup, SSO login, and smoke test fully enumerated in quickstart (no implied steps)? [Completeness, Spec §US2, Quickstart]
- [ ] CHK003 Does the spec define numbering/short-name rules and the sources for next-number computation (remote, local, specs)? [Completeness, Spec §FR-005, §US3]
- [ ] CHK004 Is the read-only MCP smoke test requirement included with the operation, purpose, and success threshold? [Completeness, Spec §FR-003, Contracts/mcp-smoke-test]
- [ ] CHK005 Are edge cases listed in the spec reflected by acceptance criteria or guidance somewhere (not just enumerated)? [Completeness, Spec §Edge Cases, Tasks]

## Requirement Clarity

- [ ] CHK006 Is the term “default region” precisely bound to variable names (e.g., AWS_REGION) and override behavior via .env? [Clarity, Spec §FR-004, Quickstart]
- [ ] CHK007 Is “read-only” unambiguously defined (no create/update/delete) for the smoke test? [Clarity, Spec §US1, §FR-003]
- [ ] CHK008 Are naming conventions for short-name (2–4 words, hyphen-separated, action-noun) specified without ambiguity? [Clarity, Spec §FR-006]
- [ ] CHK009 Do acceptance scenarios avoid vague terms like “discoverable” by specifying where links must appear? [Clarity, Spec §US1 Acceptance]
- [ ] CHK010 Are failure messages required to be actionable with next steps (not generic errors)? [Clarity, Spec §FR-007]

## Governance Links & Consistency (Focus)

- [ ] CHK010a Are the exact README anchor locations for links to AGENTS.md and Constitution specified (section headings or paths)? [Clarity, Spec §US1 Acceptance]
- [ ] CHK010b Do README, AGENTS.md, and Constitution consistently describe serverless-first and least-privilege posture without contradictions? [Consistency, Spec §FR-001, Plan §Constitution Check]

## Requirement Consistency

- [ ] CHK011 Do region defaults and overrides align across Spec, Plan, Quickstart, and AGENTS.md? [Consistency, Spec §FR-004, Plan §Technical Context, Quickstart]
- [ ] CHK012 Do tasks reflect the spec’s acceptance criteria for each user story without introducing new requirements? [Consistency, Tasks vs Spec §US1–US3]
- [ ] CHK013 Is the smoke test described consistently (operation, timing threshold) across Spec, Contracts, and Quickstart? [Consistency, Spec §FR-003, Contracts, Quickstart]
- [ ] CHK014 Are governance principles referenced consistently (serverless-first, least-privilege, SSO) across Spec and Plan checks? [Consistency, Plan §Constitution Check, Spec §FR-001, §FR-007]

## Acceptance Criteria Quality (Measurability)

- [ ] CHK015 Are time-based criteria quantified (≤ 10 minutes bootstrap, ≤ 5 seconds smoke test, ≤ 60 seconds specify flow)? [Measurability, Spec §SC-001–SC-004]
- [ ] CHK016 Can the governance linkage success be verified objectively (presence of working README links)? [Measurability, Spec §SC-003, Tasks T005/T016]
- [ ] CHK017 Do acceptance criteria avoid technology-specific internal metrics (keep user-facing)? [Measurability, Spec §Success Criteria]

## Scenario Coverage

- [ ] CHK018 Are primary flows covered: governance discovery, bootstrap, and numbering? [Coverage, Spec §US1–US3]
- [ ] CHK019 Are alternate flows covered for multiple profiles and region overrides? [Coverage, Quickstart, Spec §Assumptions]
- [ ] CHK020 Are exception flows covered for missing credentials, expired SSO session, or missing `.env` values with guidance? [Coverage, Spec §Edge Cases, §FR-007]

## Edge Case Coverage

- [ ] CHK021 Are connectivity/installation constraints (no internet, restricted installs) addressed with manual guidance? [Edge Case, Spec §Edge Cases, Quickstart]
- [ ] CHK022 Is numbering conflict (duplicate numeric prefixes) addressed with a documented rule or mitigation? [Edge Case, [Gap], Setup script observation]
- [ ] CHK023 Are stale local branches handled via a documented fetch/prune prerequisite? [Edge Case, Spec §Edge Cases, US3]

## Non-Functional Requirements

- [ ] CHK024 Are security posture requirements (least-privilege IAM, no secrets in repo, SSO) explicitly specified? [NFR, Spec §FR-007, Plan §Constitution Check]
- [ ] CHK025 Are observability/logging requirements for scripts/docs (actionable errors) specified? [NFR, Spec §FR-008, Plan §Technical Context]
- [ ] CHK026 Are performance expectations specified only as user-facing timings (not internal TPS)? [NFR, Spec §Success Criteria]

## Dependencies & Assumptions

- [ ] CHK027 Are assumptions (default region, access to SSO, network availability) explicitly documented and internally consistent? [Dependencies, Spec §Assumptions]
- [ ] CHK028 Are external dependencies (AWS CLI, MCP servers, Spec Kit tooling) enumerated with locations and versions if relevant? [Dependencies, Plan §Technical Context, README]

## Ambiguities & Conflicts

- [ ] CHK029 Is there any ambiguity between `.env` keys (AWS_REGION vs AWS_DEFAULT_REGION) and how conflicts are resolved? [Ambiguity, Data-Model, [Gap]]
- [ ] CHK030 Do any tasks introduce requirements not present in the spec (scope creep)? [Conflict, Tasks vs Spec]

## Traceability & IDs

- [ ] CHK031 Are FR/SC IDs consistently used and cross-referenced in tasks and plan? [Traceability, Spec §FR/SC, Plan, Tasks]
- [ ] CHK032 Is there a clear mapping from user stories (US1–US3) to tasks (T005–T015) enabling independent verification? [Traceability, Spec §US1–US3, Tasks]

## Region & Environment Semantics (Focus)

- [ ] CHK033 Does `.env.example` explicitly include `AWS_REGION` with default `us-east-1` and a comment about overrides? [Completeness, Tasks T001/T011]
- [ ] CHK034 Is the relationship between `AWS_REGION` and `AWS_DEFAULT_REGION` documented to avoid ambiguity or conflicts? [Clarity, Data-Model, Spec §FR-004]
- [ ] CHK035 Do Quickstart and README use consistent region variable names and avoid mixing unrelated env keys? [Consistency, Quickstart, README]

---

Notes:
- Checklist tests the quality of requirements, not implementation behavior.
- Mark items with [Gap]/[Ambiguity]/[Conflict] when documentation needs updates.
