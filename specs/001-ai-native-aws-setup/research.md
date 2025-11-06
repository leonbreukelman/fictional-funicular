# Research: Bootstrap AI-Native AWS Setup

Created: 2025-11-06
Branch: 001-ai-native-aws-setup
Spec: specs/001-ai-native-aws-setup/spec.md

## Decisions and Rationale

### 1) Local AWS authentication method
- Decision: Use AWS SSO / Identity Center for local MCP authentication
- Rationale: Short-lived credentials, enterprise alignment, avoids static secret distribution
- Alternatives considered:
  - AssumeRole via OIDC: Strong for CI; local developer setup more complex
  - Static access keys: Simpler but weaker security posture; rotation burden

### 2) Default region handling
- Decision: Default to `us-east-1` with `.env` override
- Rationale: Matches project guidance; predictable default; easy to change per environment
- Alternatives: No default (forces explicit set every time) — slower onboarding

### 3) Tooling
- Decision: Use Spec Kit CLI prerequisites (uv, specify-cli)
- Rationale: Standardized spec-driven workflow; reproducible scripts
- Alternatives: Ad-hoc shell scripts — less structured and harder to scale

### 4) AWS MCP smoke test
- Decision: No-impact smoke test using read-only operation (e.g., account identity)
- Rationale: Validates wiring and permissions without resource changes
- Alternatives: List resources (S3 buckets, etc.) — broader permissions needed

### 5) Makefile targets (CLI contracts)
- Decision: Provide action-oriented targets
  - bootstrap — install/verify prerequisites, set up configs
  - specify — create a new spec feature from description
  - plan — run plan workflow
  - tasks — generate tasks after planning
  - implement — execute implementation phase
  - analyze — consistency/verification
  - mcp-smoke — run read-only AWS MCP connectivity
- Rationale: Memorable verbs; aligns with workflow commands
- Alternatives: setup/init — acceptable; chose "bootstrap" for clarity and breadth

### 6) Secrets and env handling
- Decision: `.env` ignored by Git; provide `.env.example`
- Rationale: Prevent secret leakage while documenting required variables
- Alternatives: Commit `.env` with placeholders — risk of misuse

### 7) Spec numbering policy (conflict observed)
- Decision: Enforce unique numeric prefixes repo-wide (not per short-name)
- Rationale: Tooling expects a single directory per number; avoids plan/setup warnings
- Alternatives: Per-short-name numbering — conflicts with current scripts
- Follow-up: Renumber newer or older feature to next available number (e.g., 002-...)

## References
- AGENTS.md — governance and AWS MCP usage guidance
- .specify/memory/constitution.md — constitution (to be expanded)
- .github/mcp/aws-mcp-config.json — MCP server configuration
