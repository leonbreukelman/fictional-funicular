# Contract: MCP Smoke Test (Read-Only)

## Purpose
Validate AWS connectivity and identity in a read-only manner using the official AWS MCP configuration.

## Action
- Name: sts:GetCallerIdentity
- Effect: Read-only
- Preconditions:
  - Valid AWS credentials (prefer SSO)
  - Region set via environment (default `us-east-1`)
  - AWS MCP server configured per `.github/mcp/aws-mcp-config.json`

## Request Shape (conceptual)
- No parameters required beyond credentials and region.

## Response Shape (conceptual)
```
{
  "Account": "123456789012",
  "Arn": "arn:aws:sts::123456789012:assumed-role/role-name/session-name",
  "UserId": "AROAXXXXX:session-name"
}
```

## Success Criteria
- Command completes in ≤ 5 seconds under normal conditions.
- No create/update/delete permissions required.
- Non-zero exit code and actionable message if credentials or region are missing.
