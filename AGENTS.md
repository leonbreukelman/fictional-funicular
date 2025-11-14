# AI Agent Instructions

This file provides guidance for AI agents (including GitHub Copilot, Claude, and others) working within this repository.

## Core Directives

- **Use Official AWS MCP Servers**: All AWS queries and operations must use the official AWS MCP servers configured in `.github/mcp/aws-mcp-config.json`.
- **Default Region**: AWS operations default to `us-east-1` unless explicitly overridden in `.env`.
- **Serverless-First Architecture**: Prefer serverless solutions (Lambda, API Gateway, DynamoDB, S3) over traditional compute (EC2, RDS).
- **Constitution Compliance**: Reference `.specify/memory/constitution.md` for all architectural and implementation decisions.

## Workflow

Follow the Spec-Driven Development workflow:

1. `/speckit.constitution` - Establish project principles
2. `/speckit.specify` - Create baseline specification
3. `/speckit.clarify` (optional) - Ask structured questions
4. `/speckit.plan` - Create implementation plan
5. `/speckit.tasks` - Generate actionable tasks
6. `/speckit.checklist` (optional) - Validate quality
7. `/speckit.implement` - Execute implementation
8. `/speckit.analyze` (optional) - Verify consistency

## Code Standards

- Use least-privilege IAM policies
- Enable encryption at rest and in transit
- Implement proper error handling and logging
- Write tests with >90% coverage target
- Document all public APIs and interfaces

## Resource References

- AWS MCP Configuration: `.github/mcp/aws-mcp-config.json`
- Environment Variables: `.env`
- Constitution: `.specify/memory/constitution.md`
- Scripts: `.specify/scripts/bash/`
