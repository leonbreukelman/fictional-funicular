<!--
Sync Impact Report
- Version change: n/a → 1.0.0
- Modified principles: Added initial set (I–IX)
- Added sections: Additional Constraints & Security Requirements; Development Workflow & Quality Gates
- Removed sections: None (template placeholders replaced)
- Templates requiring updates:
	- ⚠ .specify/templates/plan-template.md (ensure Constitution Check mirrors Principles I–IX)
	- ⚠ .specify/templates/spec-template.md (ensure mandatory sections align with Spec-Driven Development principle)
	- ⚠ .specify/templates/tasks-template.md (ensure task phases and checklist mapping reflect governance gates)
	- ✅ .github/copilot-instructions.md (created/updated by agent context script)
- Follow-up TODOs:
	- TODO(RATIFICATION_HISTORY): Backfill historical ratification notes if prior governance existed
-->

# Fictional Funicular AI-Native AWS Constitution

## Core Principles

### I. Serverless-First on AWS
- All solutions MUST prefer managed, serverless services on AWS (e.g., Lambda, API Gateway,
	DynamoDB, S3, EventBridge, Step Functions) over self-managed compute (EC2, containers) unless
	a justified exception is recorded in the feature plan’s Complexity Tracking.
- Data and workflows SHOULD minimize operational burden; infrastructure complexity requires explicit
	justification and rollback plan.

### II. Least-Privilege IAM and Encryption
- Access MUST follow least-privilege IAM: scoped roles, resource-level permissions, and separation
	of duties across environments (dev/stage/prod).
- Encryption MUST be enabled in transit (TLS 1.2+) and at rest (KMS-managed or service-managed keys).
- Wildcard principals or resources ("*") MUST NOT be used without a documented, time-bounded exception
	in the plan’s Complexity Tracking.

### III. Spec-Driven Development
- Every feature MUST begin with a specification (`specs/NNN-short-name/spec.md`) that defines
	user scenarios, testable requirements, and measurable success criteria.
- The standard command workflow is: `/speckit.constitution` → `/speckit.specify` → `/speckit.plan`
	→ `/speckit.tasks` → `/speckit.implement` → `/speckit.analyze` (optional).
- Branches MUST follow `NNN-short-name` format with a unique numeric prefix across the repository.
- Specifications MUST be user-value focused and technology-agnostic; implementation details live in plans/tasks.

### IV. AI-Native Collaboration
- GitHub Copilot is the default AI assistant. Agents MUST follow `AGENTS.md` and this constitution.
- AWS MCP servers MUST be the official configuration for all AWS queries. Default region is `us-east-1`,
	overridable via `.env`.
- AI-generated changes MUST respect security and privacy; human review is required for merges affecting
	production or security posture.

### V. Secrets and Configuration
- Secrets MUST NOT be committed. `.env` MUST be ignored by Git; `.env.example` MUST list required variables
	with non-sensitive placeholders.
- AWS SSO / Identity Center is the primary local authentication method; prefer short-lived credentials.
- Configuration changes MUST document impacts on security and operations in the plan.

### VI. Quality Gates and Testing Discipline
- Code features target ≥90% test coverage; adopt red–green–refactor where applicable.
- For documentation/scripts-only features, checklist-based validation and smoke tests are REQUIRED.
- Contract changes MUST include updated contracts and tests (or documented manual verification steps).

### VII. Observability and Logging
- Execution paths MUST produce human-readable logs with clear failure modes; CLI tasks SHOULD emit
	machine-parseable cues where feasible (e.g., JSON blocks or stable markers).
- Error messages MUST be actionable, citing the failing precondition and next steps.

### VIII. Versioning and Breaking Changes
- This constitution follows Semantic Versioning. MAJOR: redefinitions/removals; MINOR: new principles
	or expanded guidance; PATCH: clarifications/typos.
- Public contracts, governance documents, and workflows SHOULD follow SemVer where practical.
- Breaking changes REQUIRE migration notes and reviewer sign-off in the plan’s Constitution Check.

### IX. Simplicity and Complexity Justification
- Prefer the simplest design that satisfies requirements (YAGNI). Complexity MUST be justified in the
	plan’s Complexity Tracking table with rejected alternatives.

## Additional Constraints and Security Requirements
- Default AWS region is `us-east-1`; contributors MAY override via `.env`.
- Data residency/compliance constraints MUST be documented when applicable before implementation.
- Least-privilege and encryption principles apply to all environments and data flows.

## Development Workflow, Review Process, Quality Gates
- Every feature MUST include spec → plan → tasks before implementation.
- PRs MUST demonstrate alignment with this constitution. Reviewers SHALL block merges when principles
	are violated or exceptions lack justification.
- No secrets in repository: CI/CD and pre-commit hooks SHOULD enforce basic checks where available.
- `tasks.md` MUST map work to user stories and requirements using the standardized checklist format.

## Governance
- This constitution supersedes other practices for architecture, security, and workflow.
- Amendments require a PR that updates this file, includes a Sync Impact Report, and increments
	the version per SemVer with Ratified/Last Amended dates.
- Compliance is verified during planning (Constitution Check) and at review time. Exceptions MUST be
	documented in Complexity Tracking with a clear remediation plan and time bounds.

**Version**: 1.0.0 | **Ratified**: 2025-11-06 | **Last Amended**: 2025-11-06
# [PROJECT_NAME] Constitution
<!-- Example: Spec Constitution, TaskFlow Constitution, etc. -->

## Core Principles

### [PRINCIPLE_1_NAME]
<!-- Example: I. Library-First -->
[PRINCIPLE_1_DESCRIPTION]
<!-- Example: Every feature starts as a standalone library; Libraries must be self-contained, independently testable, documented; Clear purpose required - no organizational-only libraries -->

### [PRINCIPLE_2_NAME]
<!-- Example: II. CLI Interface -->
[PRINCIPLE_2_DESCRIPTION]
<!-- Example: Every library exposes functionality via CLI; Text in/out protocol: stdin/args → stdout, errors → stderr; Support JSON + human-readable formats -->

### [PRINCIPLE_3_NAME]
<!-- Example: III. Test-First (NON-NEGOTIABLE) -->
[PRINCIPLE_3_DESCRIPTION]
<!-- Example: TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced -->

### [PRINCIPLE_4_NAME]
<!-- Example: IV. Integration Testing -->
[PRINCIPLE_4_DESCRIPTION]
<!-- Example: Focus areas requiring integration tests: New library contract tests, Contract changes, Inter-service communication, Shared schemas -->

### [PRINCIPLE_5_NAME]
<!-- Example: V. Observability, VI. Versioning & Breaking Changes, VII. Simplicity -->
[PRINCIPLE_5_DESCRIPTION]
<!-- Example: Text I/O ensures debuggability; Structured logging required; Or: MAJOR.MINOR.BUILD format; Or: Start simple, YAGNI principles -->

## [SECTION_2_NAME]
<!-- Example: Additional Constraints, Security Requirements, Performance Standards, etc. -->

[SECTION_2_CONTENT]
<!-- Example: Technology stack requirements, compliance standards, deployment policies, etc. -->

## [SECTION_3_NAME]
<!-- Example: Development Workflow, Review Process, Quality Gates, etc. -->

[SECTION_3_CONTENT]
<!-- Example: Code review requirements, testing gates, deployment approval process, etc. -->

## Governance
<!-- Example: Constitution supersedes all other practices; Amendments require documentation, approval, migration plan -->

[GOVERNANCE_RULES]
<!-- Example: All PRs/reviews must verify compliance; Complexity must be justified; Use [GUIDANCE_FILE] for runtime development guidance -->

**Version**: [CONSTITUTION_VERSION] | **Ratified**: [RATIFICATION_DATE] | **Last Amended**: [LAST_AMENDED_DATE]
<!-- Example: Version: 2.1.1 | Ratified: 2025-06-13 | Last Amended: 2025-07-16 -->
