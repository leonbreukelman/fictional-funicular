# AI-Native Spec-Driven Development Repository Template for AWS

## Governance

- AGENTS: See [AGENTS.md](AGENTS.md)
- Constitution: See [.specify/memory/constitution.md](.specify/memory/constitution.md)
- AWS MCP configuration: [.github/mcp/aws-mcp-config.json](.github/mcp/aws-mcp-config.json)
- Region: Default comes from `.env` (`AWS_REGION`, default `us-east-1`). If `AWS_DEFAULT_REGION` exists in your environment, it MUST equal `AWS_REGION`.
- Smoke test: `aws sts get-caller-identity` is read-only and should complete in ≤ 5 seconds under normal conditions.

This README serves as a comprehensive guide to establishing an AI-native, spec-driven development repository optimized for AWS environments. It enables developers, AI agents, or agentic tools like GitHub Copilot CLI to configure and utilize the repository from scratch. The framework emphasizes structured workflows using GitHub's Spec Kit, real-time integration with AWS services via official Model Context Protocol (MCP) servers, and governance mechanisms to ensure compliance, security, and scalability. While focused on AWS, the design is modular, allowing substitution of AWS-specific components with equivalents from other cloud providers (e.g., Azure or GCP) through configuration adjustments.

The repository supports semi-autonomous development: begin with human-guided AI assistance for planning and coding, then evolve toward fully AI-managed infrastructure using Amazon Bedrock Agents and Lambda functions. Defaults are configurable in centralized locations to accommodate variations without extensive rework.

This document is crafted for accessibility by junior developers, enthusiasts, or basic AI agents. It uses clear steps, code examples, and explanations, assuming basic familiarity with command-line interfaces and GitHub.

## Overview

This template repository facilitates:
- **Spec-Driven Development (SDD)**: Define requirements first, then generate plans, tasks, and code using AI agents.
- **AI Integration**: Leverage Copilot CLI (default) for natural language interactions, with options for alternatives like Claude.
- **Cloud Connectivity**: Use official AWS MCP servers for querying AWS resources, documentation, and serverless operations in real time.
- **Governance**: Embed non-negotiable principles (e.g., least-privilege IAM, serverless-first architecture) via constitution files and checklists.
- **Modularity**: AWS components (e.g., Lambda, Bedrock) can be replaced by equivalents (e.g., Azure Functions, Azure AI) by updating configurations.
- **Evolution Path**: Start with foundational setups and progress to autonomous deployments, where AI agents handle infrastructure provisioning via Bedrock.

Key benefits include reduced manual effort, enforced best practices, and a reproducible environment achievable in approximately 10 minutes.

## Prerequisites

Before setup, ensure the following are installed and configured:
- **GitHub Account**: Required for repository creation and Copilot CLI authentication. Create a new repository on GitHub (e.g., via the web interface or `gh repo create <repo-name> --public`).
- **Node.js 20+**: For running MCP servers and Copilot CLI. Install from [nodejs.org](https://nodejs.org/).
- **Python 3.12+**: For backend services (e.g., FastAPI) and tools. Install from [python.org](https://www.python.org/).
- **uv Tool**: For Python package management. Install via `python -m pip install --upgrade uv`.
- **AWS CLI**: For AWS interactions. Install from [AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and configure with `aws configure` (use default profile unless specified).
- **Copilot CLI (copilot)**: Required for repository management. Install from [https://github.com/github/copilot-cli](https://github.com/github/copilot-cli).
- **Visual Studio Code (VS Code)**: Recommended IDE with extensions for GitHub Copilot and AWS Toolkit.
- **AWS Account**: With access to services like Bedrock, Lambda, and IAM. Default region: us-east-1 (configurable).

No Docker or dev containers are required; setups are native and script-based for simplicity.

## Repository Creation and Initial Setup

1. **Create the Repository**:
   - On GitHub, create a new repository (replace `<repo-name>` with your chosen name, e.g., `ai-aws-template`).
   - Clone it locally: `git clone https://github.com/<your-username>/<repo-name>.git`.
   - Navigate to the directory: `cd <repo-name>`.

2. **Install Spec Kit CLI**:
   - Run: `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git`.
   - This installs the `specify` command globally for project scaffolding.

3. **Initialize the Project**:
   - Run: `specify init . --here --ai copilot --script sh --ignore-agent-tools`.
     - `--here`: Uses the current directory.
     - `--ai copilot`: Configures for GitHub Copilot CLI (default; change to `claude` or others as needed).
     - `--script sh`: Generates Bash scripts (use `ps` for PowerShell).
     - `--ignore-agent-tools`: Skips checks for AI binaries.
   - This creates the `.specify/` directory with templates, scripts, and initial specs.

4. **One-Command Setup via Makefile**:
   - Create a `Makefile` at the root with the following content (or generate it via a script):
     ```
     .PHONY: setup-aws check-prerequisites create-feature

     setup-aws:
     	@./.specify/scripts/check-prerequisites.sh
     	@./.specify/scripts/setup-plan.sh
     	@echo "AWS setup complete. Default region: us-east-1."

     check-prerequisites:
     	@./.specify/scripts/check-prerequisites.sh

     create-feature:
     	@./.specify/scripts/create-new-feature.sh
     ```
   - Run: `make setup-aws`.
     - This verifies prerequisites, installs dependencies (e.g., via uv), configures AWS defaults, and sets up MCP.

5. **Configure Environment Variables**:
   - Create or edit `.env` at the root (gitignore it for security):
     ```
     AWS_REGION=us-east-1  # Default; override for other regions
     AWS_PROFILE=default    # Default profile
     GH_TOKEN=<your-github-token>  # For private repos
     ```
   - Source it: `source .env`.

## Configuration

Centralize configurations to minimize scattering and enable easy overrides.

### MCP Configuration (Official AWS Servers Only)
- Use official AWS MCP servers from [awslabs/mcp](https://github.com/awslabs/mcp). No global installs; run on-demand via `npx`.
- Create `.github/mcp/aws-mcp-config.json`:
  ```
  {
    "servers": {
      "aws-api": {
        "command": "npx",
        "args": ["-y", "@aws/mcp-servers-aws-api"],
        "env": {
          "AWS_REGION": "${env:AWS_REGION}",
          "AWS_PROFILE": "${env:AWS_PROFILE}"
        }
      },
      "aws-knowledge": {
        "type": "remote",
        "url": "https://mcp.us-east-1.amazonaws.com/knowledge"
      },
      "aws-serverless": {
        "command": "npx",
        "args": ["-y", "@aws/mcp-servers-serverless"]
      },
      "aws-bedrock-agentcore": {
        "command": "npx",
        "args": ["-y", "@aws/mcp-servers-bedrock-agentcore"]
      },
      "aws-bedrock-knowledgebases": {
        "command": "npx",
        "args": ["-y", "@aws/mcp-servers-bedrock-knowledgebases"]
      }
    }
  }
  ```
- Reference this in `.vscode/mcp.json` for VS Code integration.
- Test: Run `npx -y @aws/mcp-servers-aws-api` to verify.
  - Identity smoke test (read-only; ≤ 5s expected): `aws sts get-caller-identity --output json`

For other clouds (e.g., Azure), create a parallel config (e.g., `azure-mcp-config.json`) and switch via env vars.

### AI Agent Configuration
- **Default: GitHub Copilot CLI**:
  - Install: `npm install -g @github/copilot-cli`.
  - Authenticate: `copilot-cli login`.
- Create `AGENTS.md` at root for AI guidance:
  ```
  # AI Agent Instructions
  - Use official AWS MCP servers for all AWS queries.
  - Default region: us-east-1.
  - Enforce serverless-first architecture.
  - Reference .specify/memory/constitution.md for all decisions.
  ```
- For alternatives (e.g., Claude), add `CLAUDE.md` and update initialization (`--ai claude`).

### Governance Configuration
- **Constitution and Constraints**: Run `/speckit.constitution` in Copilot CLI to generate `.specify/memory/constitution.md`:
  ```
  Principle 1: Security-First – Use least-privilege IAM, encryption at rest/transit.
  Principle 2: Serverless-First – Prefer Lambda, API Gateway over EC2.
  Principle 3: Region Restriction – Default to us-east-1; allow eu-west-1 as secondary.
  ```
- **Checklists**: Use `/speckit.checklist` to create feature-specific validations (e.g., test coverage >90%).

## Workflow

Follow Spec-Driven Development using slash commands in Copilot CLI or VS Code.

1. **Define Principles**: `/speckit.constitution`.
2. **Specify Requirements**: `/speckit.specify "Build a serverless API for user data"`.
3. **Clarify Ambiguities**: `/speckit.clarify`.
4. **Generate Plan**: `/speckit.plan`.
5. **Break into Tasks**: `/speckit.tasks` (includes [P] for parallel tasks).
6. **Implement**: `/speckit.implement` (executes tasks, invokes MCP for AWS queries).
7. **Analyze and Validate**: `/speckit.analyze`.

Example for a serverless app:
- Spec: User stories in `spec.md`.
- Plan: Architecture with Lambda, DynamoDB.
- Tasks: Ordered steps like "Create IAM role" [P] "Define Lambda function".

## AI Integration and Agentic Workflows

- **Copilot CLI Usage**: In terminal or VS Code, use `@github` for repo context. Prompts reference `.github/copilot-instructions.md` automatically.
- **Chat Modes**: Define in `.github/chatmodes/` (e.g., `aws-architect.chatmode.md` for planning).
- **MCP in Workflows**: Agents query AWS via MCP (e.g., "List EC2 instances" routes to aws-api server).
- **Customization**: Switch agents by re-initializing with `--ai <agent>`.

## Evolution to Autonomy

Once foundational, integrate Amazon Bedrock:
- Deploy Bedrock Agents via CloudFormation (inspired by maei project).
- Action Groups: Use OpenAPI schemas and Lambda for actions (e.g., deploy infrastructure).
- MCP Bridge: AgentCore MCP Server connects VS Code to Bedrock for real-time processing.
- End State: Agents autonomously query, plan, and deploy (e.g., "Deploy static site" invokes Lambda).

Start with query-only; enable actions via IAM policies.

## Customization and Defaults

All defaults are options:
- **Central Override**: Edit `.env` or `constitution.md` for changes (e.g., set `AWS_REGION=eu-west-1`).
- **Multi-Cloud**: Replace AWS MCP entries with Azure equivalents in config; re-run setup.
- **Agent Switch**: Update `--ai` in init command.

## Troubleshooting

- **MCP Errors**: Verify `npx` works; check AWS credentials.
- **Command Not Found**: Ensure CLI installations (uv, npm).
- **AI Hallucinations**: Refine prompts; enforce constitution checks.
- **Setup Fails**: Run scripts manually (e.g., `./.specify/scripts/check-prerequisites.sh`).

For issues, consult [AWS MCP docs](https://awslabs.github.io/mcp/) or [Spec Kit repo](https://github.com/github/spec-kit). Commit changes and create PRs for validation.
