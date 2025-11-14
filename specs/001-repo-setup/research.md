# Research: AI-Native Repository Setup

**Feature**: 001-repo-setup | **Date**: 2025-11-13  
**Purpose**: Research technical decisions and best practices for AI-native repository infrastructure

**Updated**: 2025-11-13 - Added decisions for enforcement mechanisms, error handling, and measurement methodologies

## Research Tasks

### 1. mem0 Storage Backend Selection

**Decision**: Use Qdrant (default) for vector storage with file-based fallback

**Rationale**:
- Qdrant is mem0's default backend and well-supported
- Provides vector similarity search for context retrieval
- Local deployment suitable for single-developer repository
- File-based fallback available if Qdrant unavailable

**Alternatives Considered**:
- **Chroma**: Good alternative but requires separate installation
- **File-based only**: Simpler but lacks vector search capabilities
- **External service (Pinecone, Weaviate)**: Adds external dependency and cost

**Implementation Notes**:
- Start with file-based backend for simplicity (`mem0ai` includes it)
- Document Qdrant setup for advanced use cases
- Configuration via environment variables

### 2. MCP Server Implementation Pattern

**Decision**: Use Python-based MCP server with asyncio for coordination

**Rationale**:
- Python 3.12+ with async/await provides clean coordination model
- Aligns with primary language choice
- MCP protocol is message-based, fits asyncio event loop
- Can coordinate multiple AI agents (Copilot, custom agents)

**Alternatives Considered**:
- **Node.js MCP server**: Would split stack unnecessarily
- **Direct API calls**: Bypasses standardized coordination protocol
- **Third-party MCP services**: Adds external dependency

**Implementation Notes**:
- Create `mcp_coordinator.py` with message routing
- Use Python's `asyncio.Queue` for message passing
- Document MCP protocol integration points

### 3. Structured Logging Implementation

**Decision**: Use structlog with JSON formatter for all logging

**Rationale**:
- structlog provides structured, context-aware logging
- JSON output enables easy parsing and analysis
- Built-in context processors for correlation IDs
- Compatible with Python standard library logging

**Alternatives Considered**:
- **Standard logging**: Less structured, harder to parse
- **loguru**: Good but adds dependency; structlog more standard
- **Custom solution**: Reinventing wheel

**Implementation Notes**:
- Configure structlog in `src/utils/logging.py`
- Add correlation/trace ID processor
- Redact sensitive data (PII, secrets)

### 4. Agent Memory Storage Keys

**Decision**: Use hierarchical key structure with namespaces

**Rationale**:
- Prevents key collisions across features
- Enables selective memory retrieval
- Supports memory lifecycle management

**Key Structure**:
```
<namespace>:<feature>:<context_type>
Examples:
- prompt_dna:global:patterns
- critique_history:001-repo-setup:phase1
- specification_context:001-repo-setup:requirements
```

**Alternatives Considered**:
- **Flat keys**: Simpler but collision-prone
- **UUID-based**: No semantic meaning
- **Timestamp-based**: Hard to query

**Implementation Notes**:
- Document key conventions in AGENTS.md
- Provide helper functions for key generation
- Implement memory cleanup policies

### 5. Code Hardening Workflow Integration

**Decision**: Implement as standalone Python module with phase gates

**Rationale**:
- Each phase (Intake, Implementation, RCI, Verification) is independent
- Phase gates enforce constitution principle V (Chain-of-Thought)
- Modular design enables phase-specific testing
- Can be invoked via CLI or integrated into CI/CD

**Alternatives Considered**:
- **Inline in copilot-instructions**: Less testable
- **External service**: Adds dependency
- **Manual process**: Defeats automation goal

**Implementation Notes**:
- Create `src/workflows/hardening.py` with phase classes
- Each phase returns structured output
- Gate approval tracked in phase metadata

### 6. VSCode Workspace Configuration

**Decision**: Use `.vscode/settings.json` for repository-specific config

**Rationale**:
- Standard VSCode approach for workspace settings
- Version-controlled configuration
- Enables Copilot integration settings
- Supports Python/Node.js tooling configuration

**Key Settings**:
```json
{
  "python.defaultInterpreterPath": "./.venv/bin/python",
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.testing.pytestEnabled": true,
  "github.copilot.enable": {
    "*": true,
    "markdown": true,
    "python": true
  }
}
```

**Alternatives Considered**:
- **User settings**: Not repository-specific
- **Configuration files**: Less IDE-integrated
- **Extension recommendations**: Supplementary, not replacement

**Implementation Notes**:
- Create `.vscode/settings.json`
- Add `.vscode/extensions.json` for recommended extensions
- Document manual Copilot setup steps

### 7. Test Coverage Enforcement

**Decision**: Use pytest-cov with 100% coverage requirement

**Rationale**:
- pytest-cov integrates with pytest (chosen test framework)
- Coverage reports in multiple formats (terminal, HTML, XML)
- Can fail builds on coverage threshold
- Constitution principle VII mandates 100% coverage

**Configuration**:
```ini
[tool.pytest.ini_options]
addopts = "--cov=src --cov-report=term-missing --cov-fail-under=100"
testpaths = ["tests"]
```

**Alternatives Considered**:
- **coverage.py**: Requires separate configuration
- **Manual tracking**: Not enforceable
- **Lower threshold**: Violates constitution

**Implementation Notes**:
- Add pytest-cov to dependencies
- Configure in pyproject.toml
- Integrate with pre-commit hooks

### 8. Virtual Environment Management with uv

**Decision**: Use uv for all Python package management and virtual environments

**Rationale**:
- uv is significantly faster than pip (10-100x)
- Modern tool with better dependency resolution
- Integrated virtual environment management (`uv venv`)
- Compatible with pip workflows

**Commands**:
```bash
# Create venv
uv venv

# Install dependencies
uv pip install <package>

# Sync from requirements
uv pip sync requirements.txt
```

**Alternatives Considered**:
- **pip + venv**: Traditional but slower
- **poetry**: Adds complexity, opinionated structure
- **pipenv**: Slower than uv

**Implementation Notes**:
- Document uv installation in README
- Create pyproject.toml for dependencies
- Add `.venv/` to .gitignore

## Best Practices Research

### Spec-kit Integration

**Best Practices**:
1. Always run `specify init --ai copilot --here` in repository root
2. Use feature branch naming: `###-short-name` pattern
3. Generate specs before plans, plans before tasks
4. Run constitution checks at each phase gate

**Sources**:
- Spec-kit GitHub repository documentation
- core-repo-setup.md guide

### GitHub Copilot Workflow

**Best Practices**:
1. Use `/speckit.*` commands in Copilot chat
2. Provide context via `@workspace` mentions
3. Reference constitution principles in prompts
4. Use inline comments for prompt guidance

**Sources**:
- GitHub Copilot documentation
- VSCode extension best practices

### Agent Memory Management

**Best Practices**:
1. Store only essential context (avoid data duplication)
2. Use expiration policies for temporary context
3. Implement memory cleanup on feature completion
4. Version memory schemas for compatibility

**Sources**:
- mem0ai documentation
- Vector database best practices

## Technology Stack Validation

### Python 3.12+ Features Used

- **Type hints with generics**: For type-safe APIs
- **asyncio**: For MCP coordination and concurrent operations
- **dataclasses**: For structured data models
- **pathlib**: For file system operations
- **contextlib**: For resource management

### Node.js 20+ Features Used

- **ESM modules**: For modern JavaScript
- **Top-level await**: For async utilities
- **TypeScript/JSDoc**: For type safety
- **npm scripts**: For development automation

### Dependency Minimization

**Runtime Python Dependencies**:
- mem0ai (required for agent memory)
- structlog (required for structured logging)
- (All others from standard library)

**Development Python Dependencies**:
- pytest (testing)
- pytest-cov (coverage)
- black (formatting)
- mypy (type checking)

**Node.js Dependencies** (development only):
- eslint (linting)
- prettier (formatting)
- jest (testing utilities if needed)

## Integration Patterns

### mem0 Integration

```python
from mem0 import Memory

# Initialize memory
memory = Memory()

# Store context
memory.add("prompt_dna:global:patterns", metadata={
    "principle": "Chain-of-Thought",
    "example": "Step 1: ..., Step 2: ..."
})

# Retrieve context
results = memory.search("chain-of-thought patterns", limit=5)
```

### MCP Coordination

```python
import asyncio
from typing import Dict, Any

class MCPCoordinator:
    def __init__(self):
        self.agents = {}
        self.message_queue = asyncio.Queue()
    
    async def register_agent(self, agent_id: str, agent):
        self.agents[agent_id] = agent
    
    async def coordinate(self, task: Dict[str, Any]):
        # Route task to appropriate agent
        # Aggregate results
        # Return coordinated response
        pass
```

### Spec-kit Command Workflow

```bash
# 1. Create feature specification
/speckit.specify "Feature description"

# 2. Clarify ambiguities (optional)
/speckit.clarify

# 3. Generate implementation plan
/speckit.plan

# 4. Generate task list
/speckit.tasks

# 5. Implement features
/speckit.implement

# 6. Validate against constitution
/speckit.checklist
```

## Risks and Mitigations

### Risk 1: mem0 Storage Corruption

**Mitigation**:
- Implement backup/restore functionality (FR-018)
- Use file-based fallback with automatic detection
- Document recovery procedures in quickstart.md
- Add validation checks before memory operations

### Risk 2: MCP Server Failures

**Mitigation**:
- Implement graceful degradation
- Add health checks and monitoring
- Provide direct agent invocation fallback

### Risk 3: Constitution Drift

**Mitigation**:
- Mandatory `/speckit.checklist` before merge
- Automated constitution validation
- Regular constitution reviews (quarterly)

### Risk 4: Test Coverage Gaps

**Mitigation**:
- pytest-cov enforces 100% coverage (FR-011)
- Pre-commit hooks run tests and block commits <100%
- CI/CD pipeline blocks on test failures

---

## New Decisions (Added 2025-11-13)

### 9. Coverage Enforcement Mechanism

**Decision**: Use pre-commit hooks with pytest-cov to enforce 100% test coverage locally

**Rationale**:
- Prevents low-coverage commits from entering history (fails fast)
- Aligns with Principle VII (Self-Verification NON-NEGOTIABLE)
- Provides immediate feedback during development
- More efficient than CI-only enforcement (saves time)

**Alternatives Considered**:
- **CI-only enforcement**: Slower feedback loop, allows local commits without coverage
- **IDE plugins only**: Not universally enforced, requires manual setup
- **Manual review**: Human error-prone, not scalable

**Implementation Notes**:
- `.pre-commit-config.yaml` with pytest-cov hook configured to --cov-fail-under=100
- `.coveragerc` with exclusion patterns for __init__.py, test files
- Document in quickstart.md "Expect pre-commit to fail if coverage <100%"
- Requirement FR-011

### 10. Prerequisite Validation Strategy

**Decision**: Create standalone prerequisite checker script executed before any workflow commands

**Rationale**:
- Proactive validation prevents mid-workflow failures (FR-016)
- Single source of truth for prerequisites
- Machine-readable JSON output for automation
- Provides actionable error messages

**Alternatives Considered**:
- **Inline checks in each script**: Duplicates validation logic
- **Manual verification only**: Error-prone, inconsistent
- **No validation**: High onboarding friction (proven in testing)

**Implementation Notes**:
- `.specify/scripts/bash/prereq-checker.sh` checks Python 3.12+, Node 20+, npm, uv, git, mem0ai, disk space
- JSON output mode for parsing: `--json`
- Text output mode for humans (default)
- Exit code 1 if any check fails
- Requirement FR-016

### 11. Prompt Template Validation Approach

**Decision**: Implement two-phase validation for hardening prompts: language detection + schema validation

**Rationale**:
- Prevents invalid prompts from entering workflow (FR-017, FR-019)
- Language validation ensures prompts match codebase (Python, JavaScript, etc.)
- Schema validation checks required sections (Context, Tasks, Success Criteria)
- Combines static analysis with structural checks

**Alternatives Considered**:
- **Schema validation only**: Misses language mismatches
- **Manual review only**: Error-prone, slow
- **No validation**: Allows broken prompts to fail during execution

**Implementation Notes**:
- `prompt_validator.py` with `detect_language()` and `validate_schema()` functions
- Language detection via keyword analysis (import, require, function, class, async)
- Schema validation checks for required markdown sections
- Provides actionable error messages (missing sections, language mismatch)
- Requirements FR-017, FR-019

### 12. Branch Namespacing for Memory Keys

**Decision**: Use hierarchical memory keys with branch name as second-level namespace: `namespace:branch:feature:context_type`

**Rationale**:
- Enables concurrent work on multiple features without memory pollution (FR-020)
- Simplifies cleanup (delete all keys for merged branch)
- Preserves memory isolation per branch
- Natural fit for git workflow

**Alternatives Considered**:
- **Flat keys without branch**: Risk of cross-contamination between concurrent features
- **Branch prefix only**: Less structured, harder to query
- **Separate mem0 instances per branch**: Overhead, complex setup

**Implementation Notes**:
- Memory key format: `ai-repo:001-repo-setup:spec:technical_context`
- Branch name extracted from `git branch --show-current`
- Cleanup via pattern: `ai-repo:001-repo-setup:*` when branch merged
- Update `MemoryContext` entity in data-model.md with `branch_name` field
- Requirement FR-020

## Conclusion

All technical decisions align with constitution principles and support the feature requirements. No NEEDS CLARIFICATION items remain. Proceed to Phase 1: Design & Contracts.
