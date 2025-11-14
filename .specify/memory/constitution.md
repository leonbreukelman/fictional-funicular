<!--
Sync Impact Report
==================
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
