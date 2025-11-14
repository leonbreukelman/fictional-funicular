<!--
Sync Impact Report
Version Change: INITIAL → 1.0.0
Modified Principles: N/A (initial constitution)
Added Sections:
  - Core Principles (7 principles: Specificity, Reusability, Adaptability, Role Assignment,
    Chain-of-Thought, Few-Shot Examples, Self-Verification)
  - Technology Stack Requirements (Python 3.12+, Node.js 20+, MCP, mem0, Copilot)
  - Development Workflow (Initialization, Artifact Generation, Code Hardening, Memory Management)
  - Governance (Amendment Process, Compliance, Living Document)
Removed Sections: N/A

Templates Requiring Updates:
  ✅ plan-template.md - ALIGNED
     - Constitution Check section present and references constitution file
     - Technical Context includes Python/dependencies/testing framework placeholders
     - No updates required
  
  ✅ spec-template.md - ALIGNED
     - User Scenarios & Testing section aligns with Few-Shot Examples principle
     - Requirements section supports Specificity principle
     - Includes edge cases for Self-Verification
     - No updates required
  
  ✅ tasks-template.md - ALIGNED
     - Phase structure supports Chain-of-Thought reasoning
     - Test-first approach aligns with Self-Verification principle (NON-NEGOTIABLE)
     - User story organization supports Modularity/Reusability
     - No updates required
  
  ✅ checklist-template.md - ALIGNED
     - Supports Self-Verification principle through systematic checks
     - No updates required
  
  ✅ agent-file-template.md - NOT REVIEWED (out of scope for core templates)

Follow-up TODOs:
- Address phase gate criteria for workflows
- Add error handling and recovery flows to specs
- Define security requirements (auth, data protection)
- Specify performance degradation under load
- Add concurrency conflict resolution
- Define assumption validation mechanisms

Rationale for v1.0.0: Initial constitution establishing foundational principles for AI-native
repository. This is the first formally ratified version.
-->

# Fictional Funicular AI-Native Repository Constitution

## Core Principles

### I. Specificity in Constraints
**MUST** provide detailed, unambiguous constraints for every task, specification, and implementation.
Each artifact MUST include explicit requirements covering scope, acceptance criteria, and boundaries.
Avoid vague language; replace "should" with explicit MUST/MAY statements with clear rationale.

**Rationale**: Specificity enables AI agents to execute autonomously without clarification cycles,
reducing ambiguity and ensuring consistent interpretation across the development lifecycle.

### II. Reusability Through Modularity
**MUST** design all components as modular, reusable templates and libraries. Code, prompts, and
specifications MUST be structured for reuse across different contexts. Leverage template-based
generation for specifications, plans, tasks, and agent definitions.

**Rationale**: Modular design accelerates development by eliminating redundant work and ensures
consistency through shared, proven patterns.

### III. Adaptability via Extension Points
**MUST** provide explicit extension mechanisms for future stack additions and workflow modifications.
Configuration files, plugin architectures, and hook systems MUST be designed into core components.
Avoid hard-coded dependencies; use dependency injection and configuration-driven behavior.

**Rationale**: Adaptability ensures the repository evolves with changing requirements and technologies
without requiring fundamental restructuring.

### IV. Role Assignment for AI Agents
**MUST** explicitly define roles, responsibilities, and constraints for AI agents in AGENTS.md.
Each agent MUST have a clear purpose (e.g., orchestrator using MCP, memory agent via mem0).
Prompts MUST begin with role assignment statements (e.g., "You are a Python engineer...").

**Rationale**: Role clarity enables AI agents to operate within defined boundaries, ensuring predictable
behavior and preventing scope creep.

### V. Chain-of-Thought Reasoning (NON-NEGOTIABLE)
**MUST** structure all complex reasoning processes as explicit step-by-step chains. Planning documents,
specifications, and implementation guides MUST break down logic into numbered, sequential steps.
Each step MUST state inputs, transformations, and outputs explicitly.

**Rationale**: Chain-of-thought reasoning makes AI decision-making transparent, debuggable, and
verifiable, ensuring correctness and enabling human oversight.

### VI. Few-Shot Examples for Guidance
**MUST** include 1-3 concrete examples for each specification, template, or prompt pattern.
Examples MUST cover typical use cases, edge cases, and anti-patterns. Use inline examples in
documentation and prompts to demonstrate expected behavior.

**Rationale**: Examples reduce interpretation variance, accelerate agent learning, and serve as
executable documentation for both humans and AI.

### VII. Self-Verification Through Checkpoints
**MUST** embed validation and testing checkpoints at every phase of development. All code MUST be
tested before merging. Specifications MUST include acceptance criteria. Plans MUST define
verification steps. NO untested code shall be committed.

**Rationale**: Self-verification ensures quality, catches errors early, and enables autonomous
iteration without human intervention for routine validation.

## Technology Stack Requirements

### Primary Language and Runtime
- **Python 3.12+**: Primary language for core logic, MCP servers, and automation scripts
- Type hints MUST be used for all public APIs and functions
- PEP 8 compliance enforced via black formatter
- Async I/O via asyncio for concurrent operations

### Supporting Technologies
- **Node.js 20+ / NPM**: For utility scripts, prompt linters, and build tooling
- TypeScript or JSDoc MUST be used for type safety in JavaScript code
- ESLint and Prettier for code quality and formatting

### AI and Agent Infrastructure
- **GitHub Copilot**: Primary AI coding assistant integrated with VSCode
- **Copilot CLI**: Command-line interface for prompt-based operations
- **Spec-kit**: Software Design Document (SDD) framework for specifications and planning
- **MCP Servers**: Model Context Protocol for coordinating multiple AI agents
- **mem0**: Agent memory persistence for episodic history and context retention

### Development Environment
- **VSCode**: Required IDE with GitHub Copilot extension
- **Git / GitHub**: Version control and collaboration platform
- Python dependencies: mem0, structlog (for logging), standard library preference
- Node dependencies: development tools only (linters, formatters)

### Constraints
- **MUST** minimize external runtime dependencies beyond stdlib + mem0 for Python
- **MUST** use structured logging (no print statements in libraries)
- **MUST** validate all inputs and avoid unsafe operations (eval, unsafe deserialization)
- **MUST** set explicit timeouts for network operations with bounded retries

## Development Workflow

### Initialization Sequence
1. Install Spec-kit CLI: `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git`
2. Initialize repository: `specify init --ai copilot --here`
3. Establish constitution: Use `/speckit.constitution` command with AI-native principles
4. Define specifications: Use `/speckit.specify` for feature requirements
5. Generate plans: Use `/speckit.plan` for technical implementation details
6. Break down tasks: Use `/speckit.tasks` for actionable work items
7. Implement: Use `/speckit.implement` to generate code and artifacts
8. Verify: Use `/speckit.checklist` to validate against constitution

### Artifact Generation Workflow
All specifications, plans, and tasks MUST follow the chain-of-thought structure:
- **Specifications** define "what and why" with user stories and few-shot examples
- **Plans** define "how" with data models, technical decisions, and contracts
- **Tasks** define atomic work items with dependencies, verification steps, and acceptance criteria

### Code Hardening Workflow
For production-ready code, MUST follow the four-phase hardening process:
1. **Phase 1: Intake and Strategy** - Analysis, threat modeling, and strategy recommendation
2. **Phase 2: Implementation** - Code generation with security, performance, and maintainability
3. **Phase 3: RCI** (Recursive Critique and Improvement) - Multi-perspective critique and refinement
4. **Phase 4: Verification and Delivery** - Test generation, benchmarks, and confidence reporting

### Memory Management
- Use mem0 for storing agent context, critique history, and prompt patterns
- Memory keys: 'prompt_dna', 'critique_history', 'specification_context'
- Agents MUST reference mem0 for adaptability and learning across sessions

### Quality Gates
- NO untested code: All implementations MUST have unit tests before merge
- Security validation: Input validation, no hardcoded secrets, safe file operations
- Performance targets: <500ms latency for API operations, Big-O analysis for hot paths
- Documentation: Public APIs MUST have type hints and docstrings

## Governance

This constitution supersedes all other development practices and policies. All decisions,
implementations, and modifications MUST align with the principles defined herein.

### Amendment Process
1. Amendments MUST be proposed via pull request to `.specify/memory/constitution.md`
2. Amendments MUST include rationale, impact analysis, and affected artifacts
3. Version MUST be incremented per semantic versioning:
   - MAJOR: Backward-incompatible principle changes or removals
   - MINOR: New principles or sections added
   - PATCH: Clarifications, typos, non-semantic refinements
4. Amendments MUST propagate to dependent templates and documentation
5. Deprecation window: one minor release or 90 days minimum

### Compliance and Verification
- All pull requests MUST verify compliance via `/speckit.checklist`
- Constitution checks are NON-NEGOTIABLE and gate all merges
- Complexity and deviations MUST be justified with explicit rationale
- Regular constitution reviews: quarterly or when major features are planned

### Living Document
This constitution is a living document that evolves with the repository. Agents MUST reference
this document for decision-making. The Sync Impact Report (HTML comment at top) tracks changes
and ensures dependent artifacts remain synchronized.

**Version**: 1.0.0 | **Ratified**: 2025-11-13 | **Last Amended**: 2025-11-13
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
