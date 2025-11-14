# CLI Contracts: Bootstrap AI-Native AWS Setup

Created: 2025-11-06
Branch: 001-ai-native-aws-setup

## Targets

### bootstrap
- Purpose: Install/validate Spec Kit CLI prerequisites; ensure core files exist
- Input: none
- Output: human-readable logs; non-zero exit on failure
- Error Modes: missing tools, no network, permission errors

### specify
- Purpose: Create a new feature branch and spec from a description
- Input: description string (quoted)
- Output: JSON with BRANCH_NAME and SPEC_FILE paths
- Error Modes: conflicting numeric prefix; invalid short-name

### plan
- Purpose: Initialize planning workflow for current feature
- Input: short description (optional)
- Output: JSON with FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH
- Error Modes: duplicate numeric prefixes; missing spec directory

### tasks
- Purpose: Generate actionable tasks after planning
- Input: none
- Output: tasks.md populated in feature dir

### implement
- Purpose: Execute implementation phase actions
- Input: none
- Output: implementation artifacts per spec

### analyze
- Purpose: Verify consistency with constitution and spec
- Input: none
- Output: analysis results (logs/report)

### mcp-smoke
- Purpose: Validate AWS MCP read-only access
- Input: none (depends on .env and SSO session)
- Output: human-readable success + timing; non-zero exit on failure
- Error Modes: no AWS CLI, not logged into SSO, missing permissions
