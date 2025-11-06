# Research — AI-Native AWS Setup — Update

Date: 2025-11-06
Branch: 002-ai-native-aws-setup
Spec: specs/002-ai-native-aws-setup/spec.md

## Topics and Decisions

### 1) Read-only AWS connectivity for smoke test
- Decision: Use `sts:GetCallerIdentity` as the canonical read-only check.
- Rationale: Zero side effects; widely permitted; verifies credentials, region, and connectivity.
- Alternatives considered:
  - `iam:GetUser` — Not always permitted and may fail with role-based auth.
  - `s3:ListAllMyBuckets` — Broader permissions, slower, and not always allowed.

### 2) Default region handling
- Decision: Default to `us-east-1`; allow override via `.env` (e.g., `AWS_REGION`, `AWS_DEFAULT_REGION`).
- Rationale: Matches governance; consistent developer experience.
- Alternatives considered:
  - Prompting users each run — Adds friction; not necessary.
  - Global config file only — `.env` override improves repo-local clarity.

### 3) AWS SSO for local development
- Decision: Prefer AWS SSO / Identity Center sign-in (`aws sso login`) with short-lived credentials.
- Rationale: Strong security defaults, least-privilege alignment, and better auditability.
- Alternatives considered:
  - Long-lived access keys — Higher risk; contrary to governance.
  - Assume-role via profiles without SSO — Requires separate bootstrap; acceptable as a fallback but not primary.

### 4) Minimal AWS MCP service scope
- Decision: Document STS as the required minimal service for smoke testing; broader read-only services MAY be enabled as needed.
- Rationale: Keep initial footprint minimal; reduce permission surface.
- Alternatives considered:
  - Include IAM, S3, Lambda read-only by default — Expands scope without immediate need; can be added per feature.

### 5) Numbering and short-name conventions
- Decision: Keep `NNN-<short-name>`, compute next number from remote branches, local branches, and `specs/` directories matching exact short-name.
- Rationale: Avoid collisions; deterministic automation.
- Alternatives considered:
  - Timestamped branches — Harder to order and audit in specs.
  - Single global sequence ignoring short-name — Loses grouping by feature line.

## Outcomes
- No open NEEDS CLARIFICATION items remain.
- Proceed with Phase 1 artifacts: data model, contracts, quickstart.
