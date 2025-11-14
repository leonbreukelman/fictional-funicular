# fictional-funicular

AI-Native Repository Setup - A specification-driven development environment.

## Overview

This repository implements an AI-native development workflow using the Spec-kit CLI framework. It provides:

- Structured specification management with constitutional governance
- Agent memory persistence using mem0ai
- Multi-language support (Python 3.12+, Node.js 20+)
- Test-first development with 100% coverage enforcement
- Structured logging and validation utilities

## Prerequisites

- Python 3.12 or higher
- Node.js 20 or higher
- uv (Python package installer)
- Git
- **mem0ai** - Required for agent memory persistence

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fictional-funicular
```

2. Create and activate virtual environment:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install Python dependencies:
```bash
uv pip install -r requirements.txt
```

4. Install Node.js dependencies:
```bash
npm install
```

5. Install pre-commit hooks:
```bash
pre-commit install
```

## Quick Start

### Initialize Spec-kit

```bash
# Install Spec-kit CLI
uv tool install speckit

# Initialize repository structure
specify init --ai copilot --here
```

### Run Tests

```bash
# Run all tests with coverage
pytest

# Run specific test file
pytest tests/unit/test_utils.py

# Generate coverage report
pytest --cov-report=html
```

### Development Workflow

1. **Write specifications** in `specs/<feature>/spec.md`
2. **Generate tasks** using `/speckit.tasks.prompt`
3. **Implement features** following test-first approach
4. **Verify coverage** - all tests must achieve 100% coverage
5. **Run pre-commit hooks** - automatic on commit

## Project Structure

```
.
├── .specify/               # Constitutional governance
│   ├── constitution.md     # Project principles
│   ├── prompts/           # Workflow templates
│   └── scripts/           # Automation scripts
├── src/                   # Source code
│   ├── cli/              # Command-line interface
│   ├── memory/           # Agent memory management
│   ├── specs/            # Specification handling
│   └── utils/            # Shared utilities
├── tests/                # Test suite
│   ├── unit/            # Unit tests
│   ├── integration/     # Integration tests
│   └── e2e/             # End-to-end tests
└── specs/               # Feature specifications
```

## Configuration

Environment variables can be configured in `.env` file:

```env
# mem0 configuration
MEM0_BACKEND=filesystem
MEM0_STORAGE_PATH=.mem0/

# Logging configuration
LOG_LEVEL=INFO
LOG_FORMAT=json
```

## Contributing

1. Follow specification-driven development
2. Maintain 100% test coverage (NON-NEGOTIABLE)
3. Use structured logging (no print statements)
4. Run pre-commit hooks before committing
5. Update documentation for new features

## License

See [LICENSE](LICENSE) file for details.

## Resources

- [Spec-kit CLI Documentation](https://github.com/spec-kit/spec-kit)
- [mem0ai Documentation](https://docs.mem0.ai/)
- [Project Constitution](.specify/constitution.md)
