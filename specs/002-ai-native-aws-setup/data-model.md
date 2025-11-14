# Data Model — AI-Native AWS Setup — Update

This feature updates documentation and workflow assets. While no runtime data is stored, we model key configuration entities for clarity and validation.

## Entities

### Governance References
- Description: Repository-level guidance documents that define principles and workflow.
- Artifacts:
  - `AGENTS.md`
  - `.specify/memory/constitution.md`
- Fields:
  - `links`: list of relative paths
  - `principles`: list of high-level constraints to reference in plans

### Environment Configuration
- Description: Local configuration controlling region and auth behavior.
- Files:
  - `.env.example` (tracked template)
  - `.env` (untracked private file)
- Fields (suggested):
  - `AWS_REGION` (string, default `us-east-1`)
  - `AWS_DEFAULT_REGION` (string, optional; if set, MUST equal `AWS_REGION` to avoid ambiguity)
  - `AWS_PROFILE` (string, optional; SSO profile name)

### MCP Configuration
- Description: Project-level settings for AWS MCP servers.
- File:
  - `.github/mcp/aws-mcp-config.json`
- Fields (illustrative):
  - `services`: array of strings (e.g., ["sts"] initial minimum)
  - `region`: string (default `us-east-1`)

### Feature Artifacts
- Description: Numbered branches and spec folders that represent features.
- Fields:
  - `number` (int, 1..n)
  - `shortName` (kebab-case string)
  - `paths` (spec directory, spec.md, plan.md, quickstart.md)
