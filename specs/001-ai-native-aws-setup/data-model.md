# Data Model: Bootstrap AI-Native AWS Setup

Created: 2025-11-06
Branch: 001-ai-native-aws-setup

## Entities

### Feature Specification
- Attributes: title, branch, created date, user scenarios, functional requirements, success criteria, assumptions
- Relationships: references Governance, AWS MCP Configuration, Environment Configuration

### Governance (Constitution)
- Attributes: principles, constraints, gates, version, ratified date
- Relationships: informs all features; referenced by AI Agent Instructions

### AI Agent
- Attributes: name, default status, instructions file path, context files
- Relationships: follows Governance; uses MCP config and environment

### AWS MCP Configuration
- Attributes: default region, allowed services, credentials strategy (SSO)
- Relationships: consumes Environment Configuration variables

### Environment Configuration
- Attributes: non-secret variables (.env.example), secret variables (.env untracked)
- Relationships: used by MCP config and Makefile targets

## Validation Rules
- Secrets must not be committed; `.env` ignored by Git
- `.env.example` must include all required variable keys with placeholder values
- Default region must be defined and overridable by `.env`

## State Transitions
- Draft → Ready: when spec, plan, and checklist pass quality gates and quickstart is verified locally
