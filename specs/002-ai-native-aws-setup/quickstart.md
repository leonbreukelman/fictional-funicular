# Quickstart — AI-Native AWS Setup (Update)

This guide helps you bootstrap the AI-native AWS setup, verify read-only AWS connectivity, and understand naming/numbering.

## Prerequisites

- Git
- Bash (Linux/macOS) — this repo uses a Linux dev container by default
- AWS CLI v2 (for SSO sign-in and identity check)
- Access to an AWS account with SSO configured

## 1) Fetch latest and ensure numbering context

```bash
git fetch --all --prune
```

## 2) Configure environment

- Copy the example env file and set values:

```bash
cp .env.example .env
```

- Ensure `.env` is ignored by Git and contains a region:
  - `AWS_REGION=us-east-1` (default) or your preferred region
  - If `AWS_DEFAULT_REGION` is set in your environment, it MUST equal `AWS_REGION`; prefer setting only `AWS_REGION`.

### Required Environment Variables

- `AWS_REGION` (required): Default `us-east-1`; override as needed.
- `AWS_PROFILE` (optional): Your AWS SSO profile name.

## 3) Sign in with AWS SSO

```bash
aws sso login
```

If you have multiple profiles, set `AWS_PROFILE` in your `.env` or shell session.

## 4) Verify read-only AWS connectivity (smoke test)

Using the AWS CLI directly:

```bash
aws sts get-caller-identity --output json
```

Expected output contains `Account`, `Arn`, and `UserId`. This is a zero-impact read-only operation and should complete in ≤ 5 seconds under normal conditions.

## 5) Create a new feature spec (reference)

- Use the `/speckit.specify` flow. The system will:
  - Determine the next number by checking remote branches, local branches, and `specs/` directories for the exact short-name
  - Create branch `NNN-<short-name>` and populate `specs/NNN-<short-name>/spec.md`

## 6) Links and governance

- AI agent guidance: `AGENTS.md`
- Constitution: `.specify/memory/constitution.md`
- AWS MCP configuration: `.github/mcp/aws-mcp-config.json`

## Troubleshooting

- Missing credentials: Run `aws sso login` again or set `AWS_PROFILE` to your SSO profile.
- Region errors: Set `AWS_REGION` in your `.env` (default is `us-east-1`).
- Numbering conflicts: Run `git fetch --all --prune` and retry.
