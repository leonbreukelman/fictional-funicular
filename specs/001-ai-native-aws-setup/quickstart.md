# Quickstart: Bootstrap AI-Native AWS Setup

Created: 2025-11-06
Branch: 001-ai-native-aws-setup

## 1) Prereqs
- Git, Bash
- Spec Kit CLI prerequisites: uv, specify-cli (documented in repo)
- AWS CLI v2 (for SSO)

## 2) Install AWS CLI v2 (Linux)
- Follow official AWS instructions for your distro. On Ubuntu:
  - https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

## 3) Configure AWS SSO
- Start an SSO session (opens browser unless you pass --no-browser):
  - `aws configure sso`
- If running headless, use device authorization flow and paste the code from terminal into a browser.

## 4) Environment
- Copy `.env.example` to `.env` and set variables:
  - `AWS_DEFAULT_REGION=us-east-1` (override as needed)
  - Any MCP-related environment variables required by `.github/mcp/aws-mcp-config.json`
- Ensure `.env` is ignored by Git (already configured).

## 5) Bootstrap
- Run the bootstrap target to validate tools and configs:
  - `make bootstrap`

## 6) MCP Smoke Test
- Validate connectivity (read-only, no-impact):
  - `make mcp-smoke`

## 7) Create a Spec (example)
- Create a new feature spec from a description:
  - `make specify DESC="Bootstrap AI-native AWS setup"`

Notes:
- If `aws` command is not found (exit code 127), install AWS CLI v2 and retry.
- For SSO in headless environments, use device code login shown in the terminal instructions.
