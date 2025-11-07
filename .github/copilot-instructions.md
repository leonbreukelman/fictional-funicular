# fictional-funicular Development Guidelines

Auto-generated from all feature plans. Last updated: 2025-11-06

## Active Technologies
- N/A (documentation and shell scripts) + Git, Bash shell; AWS CLI (for SSO sign-in and identity check) (002-ai-native-aws-setup)
- Bash shell scripting (WSL Ubuntu), Markdown documentation + Git, AWS CLI v2.x, Node.js 22+, npm (for MCP servers and Copilot CLI) (003-local-env-setup)
- File-based (.env configuration, documentation files) (003-local-env-setup)

- (001-ai-native-aws-setup)

## Project Structure

```text
backend/
frontend/
tests/
```

## Commands

# Local environment verification
.specify/scripts/bash/verify-local-setup.sh [--json]

# Feature creation workflow
.specify/scripts/bash/create-new-feature.sh --help

# GitHub Copilot CLI (if installed)
?? <your question>        # Ask for shell commands
git? <your question>      # Ask for git commands
# Note: Use Copilot CLI for AI-assisted queries; avoid GH CLI unless explicitly needed.

## Code Style

: Follow standard conventions

## Recent Changes
- 003-local-env-setup: Added [if applicable, e.g., PostgreSQL, CoreData, files or N/A]
- 003-local-env-setup: Added [if applicable, e.g., PostgreSQL, CoreData, files or N/A]
- 003-local-env-setup: Added Bash shell scripting (WSL Ubuntu), Markdown documentation + Git, AWS CLI v2.x, Node.js 22+, npm (for MCP servers and Copilot CLI)


<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
