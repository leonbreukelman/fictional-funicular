# Quickstart: AI-Native Repository Setup

**Feature**: 001-repo-setup | **Last Updated**: 2025-11-13  
**Purpose**: Get started with AI-native repository development in under 15 minutes

## Prerequisites Checklist

Before starting, ensure you have:

- [ ] **Python 3.12+** installed (`python3 --version`)
- [ ] **Node.js 20+** installed (`node --version`)
- [ ] **NPM** installed (`npm --version`)
- [ ] **uv** installed (`uv --version` or install via `curl -LsSf https://astral.sh/uv/install.sh | sh`)
- [ ] **Git 2.x** installed (`git --version`)
- [ ] **VSCode** installed with GitHub Copilot extension
- [ ] **GitHub Copilot** subscription active
- [ ] **GitHub Copilot CLI** configured (`gh copilot --version`)
- [ ] **WSL/Linux/macOS** environment (bash scripts require Unix shell)
- [ ] **500MB+ free disk space** for dependencies and memory storage

## Quick Setup (10 minutes)

### Step 1: Install Spec-kit CLI (1 minute)

```bash
# Install Spec-kit using uv
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# Verify installation
specify --version
```

### Step 2: Initialize Repository (2 minutes)

```bash
# Navigate to your repository root
cd /path/to/your/repo

# Initialize Spec-kit (creates .specify/ directory)
specify init --ai copilot --here

# This creates:
# - .specify/templates/
# - .specify/memory/
# - .specify/scripts/
```

### Step 3: Create Virtual Environment (1 minute)

**Important: Always activate the virtual environment before installing packages to avoid global installation issues that can cause path conflicts.**

```bash
# Create Python virtual environment using uv
uv venv

# Activate virtual environment
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows

# Install core dependencies
uv pip install mem0ai structlog pytest pytest-cov black mypy
```

### Step 4: Generate Constitution (2 minutes)

```bash
# In VSCode, open GitHub Copilot chat
# Type: /speckit.constitution

# Follow the prompt to generate constitution.md
# The file will be created at .specify/memory/constitution.md
```

Expected output: Constitution with 7 principles, technology stack, workflow, and governance.

### Step 5: Create Agent Definitions (2 minutes)

Create `AGENTS.md` in repository root:

```bash
cat > AGENTS.md << 'EOF'
# AI Agents

## Orchestrator Agent

**Agent ID**: `orchestrator`  
**Type**: ORCHESTRATOR  
**Role**: You are an MCP-based orchestration agent coordinating multiple AI agents to complete complex development tasks.

**Responsibilities**:
- Route tasks to appropriate specialized agents
- Aggregate results from multiple agents
- Manage task dependencies and sequencing
- Monitor agent health and availability

**Constraints**:
- MUST use MCP protocol for all agent communication
- MUST NOT execute tasks directly (delegate to specialized agents)
- MUST maintain task execution logs in mem0

**Integration Points**:
- MCP Server (coordination)
- mem0 (task history)
- GitHub Copilot (user interface)

**Memory Keys**:
- `orchestration:global:task_queue`
- `orchestration:global:agent_registry`

## Memory Agent

**Agent ID**: `memory_agent`  
**Type**: MEMORY  
**Role**: You are a memory management agent responsible for storing and retrieving agent context using mem0.

**Responsibilities**:
- Store prompt patterns and templates
- Maintain critique history from code hardening
- Track specification decisions across features
- Implement memory lifecycle policies

**Constraints**:
- MUST use hierarchical key structure (namespace:feature:context_type)
- MUST validate memory keys before storage
- MUST respect expiration policies
- MUST NOT store sensitive data (PII, secrets)

**Integration Points**:
- mem0 (primary storage)
- File system (backup snapshots)

**Memory Keys**:
- `prompt_dna:*:*`
- `critique_history:*:*`
- `specification_context:*:*`
EOF
```

### Step 6: Create Copilot Instructions (2 minutes)

Create `copilot-instructions.md` in repository root:

```bash
cat > copilot-instructions.md << 'EOF'
# GitHub Copilot Instructions

## Role Assignment Template

You are a [ROLE] agent working in an AI-native repository following constitutional principles:
- Principle I: Specificity in Constraints
- Principle V: Chain-of-Thought Reasoning (NON-NEGOTIABLE)
- Principle VII: Self-Verification Through Checkpoints (NON-NEGOTIABLE)

## Chain-of-Thought Template

When performing complex tasks:

**Step 1**: [Action]
- Input: [What you receive]
- Transformation: [What you do]
- Output: [What you produce]

**Step 2**: [Action]
- Input: [Output from Step 1]
- Transformation: [What you do]
- Output: [What you produce]

[Continue numbering...]

## Few-Shot Examples

### Example 1: Storing Memory Context

Input: "Store prompt pattern for hardening workflow"

```python
from mem0 import Memory

memory = Memory()
memory.add(
    "prompt_dna:global:hardening_phase1",
    metadata={
        "principle": "Chain-of-Thought",
        "phase": 1,
        "example": "Step 1: Analyze code..."
    }
)
```

### Example 2: Constitution Check

Input: "Validate specification against principles"

```python
# Check Principle V: Chain-of-Thought
steps = spec.find_all("Step ")
assert len(steps) >= 3, "Insufficient chain-of-thought steps"

# Check Principle VII: Self-Verification
tests = spec.find_all("test_")
assert len(tests) > 0, "No tests defined (NON-NEGOTIABLE)"
```

## Self-Verification Checklist

Before completing any task:

- [ ] All requirements explicitly stated (Principle I)
- [ ] Components are reusable (Principle II)
- [ ] Extension points provided (Principle III)
- [ ] Agent roles clearly defined (Principle IV)
- [ ] Chain-of-thought steps numbered (Principle V)
- [ ] 1-3 examples provided (Principle VI)
- [ ] Tests written and passing (Principle VII)
EOF
```

## Verify Installation

Run the following to ensure everything is set up correctly:

```bash
# Check Python environment
python --version  # Should be 3.12+

# Check Python packages
python -c "import mem0; print('✅ mem0')"
python -c "import structlog; print('✅ structlog')"
python -c "import pytest; print('✅ pytest')"

# Check Node environment
node --version    # Should be 20+
npm --version

# Check Spec-kit
specify --version

# Check Git
git status        # Should show clean working tree or modified files

# Check constitution
test -f .specify/memory/constitution.md && echo "✅ Constitution exists" || echo "❌ Run /speckit.constitution"

# Check agents
test -f AGENTS.md && echo "✅ Agents defined" || echo "❌ Create AGENTS.md"

# Check copilot instructions
test -f copilot-instructions.md && echo "✅ Copilot instructions exist" || echo "❌ Create copilot-instructions.md"
```

## First Feature Workflow

Now create your first feature to test the setup:

```bash
# 1. Create feature specification
# In VSCode Copilot chat:
# /speckit.specify "Create a simple hello world Python script"

# This will:
# - Create branch: 001-hello-world
# - Generate: specs/001-hello-world/spec.md

# 2. Generate implementation plan
# /speckit.plan

# This will create:
# - specs/001-hello-world/plan.md
# - specs/001-hello-world/research.md
# - specs/001-hello-world/data-model.md
# - specs/001-hello-world/contracts/
# - specs/001-hello-world/quickstart.md

# 3. Generate task list
# /speckit.tasks

# This will create:
# - specs/001-hello-world/tasks.md

# 4. Implement feature
# /speckit.implement

# This will create source files following the plan

# 5. Validate against constitution
# /speckit.checklist
```

## Common Issues and Solutions

- **mem0ai install fails**: Ensure venv is activated and use `uv pip install mem0ai`. If using pip, switch to uv for faster installs.
- **uv vs pip confusion**: Always prefer uv for speed and consistency (10-100x faster than pip). Install uv if missing.
- **Venv not activated**: Global installations can cause path issues. Always activate with `source .venv/bin/activate` before pip commands.
- **Python version too old**: Upgrade to 3.12+ if `python3 --version` shows <3.12.
- **mem0ai import error**: Run `python -c "import mem0ai"` to test; reinstall if fails.

## Next Steps

Once setup is complete:

1. **Read the Constitution**: Review `.specify/memory/constitution.md` to understand principles
2. **Explore Templates**: Check `.specify/templates/` for spec, plan, and task templates
3. **Review Agents**: Read `AGENTS.md` to understand agent roles
4. **Practice Workflow**: Create a test feature to familiarize with commands
5. **Customize Scripts**: Add custom automation to `.specify/scripts/`

## Configuration Files

### VSCode Settings (`.vscode/settings.json`)

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.mypyEnabled": true,
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": [
    "tests",
    "--cov=src",
    "--cov-report=term-missing"
  ],
  "github.copilot.enable": {
    "*": true,
    "markdown": true,
    "python": true,
    "yaml": true
  },
  "editor.formatOnSave": true
}
```

### Python Project Config (`pyproject.toml`)

```toml
[project]
name = "fictional-funicular"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "mem0ai>=1.0.0",
    "structlog>=24.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-cov>=4.1.0",
    "black>=24.0.0",
    "mypy>=1.8.0",
]

[tool.pytest.ini_options]
addopts = "--cov=src --cov-report=term-missing --cov-fail-under=100"
testpaths = ["tests"]

[tool.black]
line-length = 100
target-version = ['py312']

[tool.mypy]
python_version = "3.12"
strict = true
```

### Git Ignore (`.gitignore`)

```
# Python
.venv/
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
.pytest_cache/
.coverage
htmlcov/

# mem0
.mem0/
*.qdrant/

# VSCode
.vscode/*
!.vscode/settings.json
!.vscode/extensions.json

# OS
.DS_Store
Thumbs.db

# Logs
*.log
```

## Performance Tips

1. **Use uv for all Python operations** - 10-100x faster than pip
2. **Enable mem0 file-based backend** - No external dependencies
3. **Limit memory search results** - Default to 5 items
4. **Batch agent operations** - Reduce MCP coordination overhead
5. **Cache constitution and templates** - Read once per session

## Support and Resources

- **Constitution**: `.specify/memory/constitution.md`
- **Spec-kit Docs**: https://github.com/github/spec-kit
- **mem0 Docs**: https://docs.mem0.ai
- **GitHub Copilot**: https://docs.github.com/copilot
- **Repository Issues**: Open an issue for problems

## Estimated Times

| Task | Time |
|------|------|
| Prerequisites check | 2 min |
| Install Spec-kit | 1 min |
| Initialize repository | 2 min |
| Setup Python environment | 1 min |
| Generate constitution | 2 min |
| Create agent definitions | 2 min |
| Create Copilot instructions | 2 min |
| Verify installation | 2 min |
| **Total** | **~15 min** |

## Success Criteria

✅ You're ready to proceed when:

- All prerequisites installed and verified
- Constitution exists with 7 principles
- AGENTS.md defines orchestrator and memory agents
- copilot-instructions.md has prompt templates
- Virtual environment active with mem0, structlog, pytest
- First test feature can be created via `/speckit.specify`
- Constitution checks pass for generated specs

**Next Command**: `/speckit.specify "Your feature description here"`
