# Feature Specification: AI-Native AWS Setup — Update

**Feature Branch**: `002-ai-native-aws-setup`  
**Created**: 2025-11-06  
**Status**: Draft  
**Input**: User description: "specs/001-ai-native-aws-setup update"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Align setup with governance and MCP (Priority: P1)

As a maintainer, I update the AI-native AWS setup assets (spec, quickstart, governance references) so contributors and AI agents follow the documented constitution, use official AWS MCP servers, and default to the correct region with safe, read-only validation.

**Why this priority**: Governance alignment and safe AWS connectivity are foundational to every contribution.

**Independent Test**: Perform a documentation-driven review using the quality checklist; confirm links from README to AGENTS.md and Constitution exist; confirm `.github/mcp/aws-mcp-config.json` is referenced; run the documented MCP smoke test end-to-end.

**Acceptance Scenarios**:

1. Given the repository governance model, When a contributor opens README, Then README.md contains direct links to `AGENTS.md` and `.specify/memory/constitution.md` within the first 30 lines under a "Governance" or "Getting Started" section (link texts: "AGENTS.md" and "Constitution").
2. Given configured AWS MCP servers, When the smoke test is run, Then it succeeds using the default region `us-east-1` or a region defined in `.env`.

---

### User Story 2 - Bootstrap with updated quickstart (Priority: P2)

As a new contributor, I can follow the updated quickstart to install prerequisites, set `.env` from `.env.example`, sign in with AWS SSO, and verify read-only AWS connectivity without creating or changing resources.

**Why this priority**: A frictionless first-run experience accelerates onboarding and reduces support load.

**Independent Test**: Follow the quickstart steps from a fresh environment; complete within the target time and verify all required files and checks.

**Acceptance Scenarios**:

1. Given a fresh clone, When I follow the quickstart, Then I complete bootstrap in ≤ 10 minutes with prerequisites verified or install guidance provided.
2. Given `.env.example`, When I copy it to `.env` and set values, Then `.env` is ignored by Git and the smoke test runs successfully.

---

### User Story 3 - Numbering and short-name conventions (Priority: P3)

As an AI agent or developer, I can read clear rules for generating `NNN-<short-name>` branches and spec folders, ensuring the next number is determined across local/remote branches and existing `specs/` directories for the exact short-name.

**Why this priority**: Consistent numbering and naming ensure predictable automation and history.

**Independent Test**: Run the documented specify flow with a sample description; verify the correct next number is chosen and the spec is created under the proper path.

**Acceptance Scenarios**:

1. Given a feature description and existing `001-<short-name>`, When I run the specify flow, Then branch `002-<short-name>` and `specs/002-<short-name>/spec.md` are created.
2. Given multiple short-names, When numbering is computed, Then it only considers branches and directories that match the exact short-name.

---

### Edge Cases

- Prerequisites cannot be installed automatically (network restrictions); guidance must be provided to complete manually.
- AWS credentials absent or expired; smoke test should fail fast with actionable guidance.
- `.env` missing required variables; quickstart must indicate how to populate from `.env.example`.
- Inconsistent numbering due to stale local branches; documentation must include a fetch/prune step.
- Duplicate numeric prefixes across different features; enforce a single owner per numeric prefix. The lowest-numbered active branch retains its number; new or conflicting features must be renumbered to the next available number and documented in the affected feature’s spec/plan.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Documentation MUST link from `README.md` to `AGENTS.md` and `.specify/memory/constitution.md`, and describe the serverless-first, least-privilege posture.
- **FR-002**: Quickstart MUST guide copying `.env.example` to `.env`, setting values, and confirm `.env` is git-ignored; no secrets are committed.
- **FR-003**: AWS MCP smoke test MUST be documented to perform a read-only operation and complete in ≤ 5 seconds under normal conditions.
- **FR-004**: Default region MUST be `us-east-1` and MAY be overridden via `.env` (`AWS_REGION`). If `AWS_DEFAULT_REGION` is set by the environment, it MUST equal `AWS_REGION` to avoid ambiguity; the docs MUST make this explicit.
- **FR-005**: Specify flow MUST document how to determine the next number by checking (1) remote branches, (2) local branches, and (3) `specs/` directories for the exact short-name.
- **FR-006**: Naming conventions MUST be documented: `NNN-<short-name>` with short-names of 2–4 words, hyphen-separated, action-noun when applicable.
- **FR-007**: Failure states MUST emit actionable guidance (e.g., missing MCP config, missing SSO session, or missing env vars) without exposing secrets.
- **FR-008**: Governance references MUST specify the use of official AWS MCP servers and default region behavior, consistent with `AGENTS.md`.

### Key Entities *(include if feature involves data)*

- **Governance References**: Links and descriptions that anchor contributor behavior (Constitution, AGENTS guidance).
- **Environment Configuration**: `.env.example` variables and local `.env` file used by tooling and MCP.
- **Feature Artifacts**: Numbered branches and spec folders following conventions.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: New contributors complete bootstrap using the updated quickstart in ≤ 10 minutes and report no blockers during smoke tests.
- **SC-002**: The MCP smoke test succeeds in ≤ 5 seconds using read-only permissions, with default region `us-east-1` unless overridden via `.env`.
- **SC-003**: README contains working links to `AGENTS.md` and the Constitution; a documentation check confirms both links are present and reachable.
- **SC-004**: The specify flow, when triggered with a sample description, produces a new `NNN-<short-name>` branch and `specs/NNN-<short-name>/spec.md` in ≤ 60 seconds.
- **SC-005**: A secrets scan or review confirms `.env` is ignored and no secrets are committed; `.env.example` is present and complete.

## Assumptions & Dependencies

### Assumptions

- Contributors have access to GitHub and network connectivity to install prerequisites or can follow manual steps.
- Default AWS region is `us-east-1` unless overridden by `.env`.
- Contributors authenticate to AWS via AWS SSO / Identity Center following documented steps.

### Dependencies

- Governance documents at `AGENTS.md` and `.specify/memory/constitution.md`.
- AWS MCP configuration at `.github/mcp/aws-mcp-config.json`.
- Spec Kit CLI prerequisites and Git for branch operations.
