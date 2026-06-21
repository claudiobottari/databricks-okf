---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 522e0632decd0cc1e43d316c83b3293dde010a70681e5a2c96d0fa3d02e266ee
  pageDirectory: concepts
  sources:
    - foundation-model-unity-catalog-permissions-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - systemai-schema
    - System.ai
  citations:
    - file: foundation-model-unity-catalog-permissions-databricks-on-aws.md
title: system.ai Schema
description: The Unity Catalog schema under the system catalog where foundation model objects reside and EXECUTE permissions are managed to control model access.
tags:
  - databricks
  - unity-catalog
  - schema
timestamp: "2026-06-19T10:39:20.092Z"
---

Here is the wiki page for "system.ai Schema".

---

## system.ai Schema

The **`system.ai` schema** is a Unity Catalog schema within the `system` catalog that contains Databricks-hosted foundation models as securable objects. By default, the schema grants `EXECUTE` permission to all users, which opens every model in the schema for invocation. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Governance Model

The `system.ai` schema uses Unity Catalog permissions to control which models users can invoke. Model permission enforcement applies consistently across pay-per-token endpoints, batch inference (AI Functions) workloads, and — through manual deletion — provisioned throughput endpoints. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Use Cases

The `system.ai` schema's permission model is intended for legally required restrictions — such as export-controlled model families, vendor-restricted or region-restricted models, and corporate policies prohibiting specific foundation models. For day-to-day governance, Databricks recommends using alternative mechanisms: `system.billing` for cost tracking and attribution, [AI Gateway](/concepts/ai-gateway.md) for rate limits and request-level usage tracking, and Private Link or private networking for secure connectivity. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Default Access

When the `system.ai` schema is first enabled, all users have `EXECUTE` permission on the schema itself, which grants access to every model within it. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Restricting Model Access

To restrict which models are available, account admins or Unity Catalog admins must perform the following steps:

1. **Remove the default `EXECUTE` permission** from the `system.ai` schema for all users. This immediately stops pay-per-token and batch inference (AI Functions) calls to all models, though provisioned throughput endpoints continue serving until manually deleted. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

2. **Selectively grant `EXECUTE` on approved individual models** by navigating to `system.ai.models.<model_name>` and assigning the permission to `All Users` or to specific groups. This creates an allow-list of permitted models. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

3. **Manually delete disallowed provisioned throughput endpoints** that serve unapproved models, as these endpoints are not automatically affected by permission changes. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Limitations

The [Agent Bricks Knowledge Assistant](/concepts/agent-bricks-knowledge-assistant-incompatibility.md) does not support foundation model Unity Catalog permissions. Databricks recommends contacting your account team before enabling the permissions feature if Knowledge Assistant is actively in use. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Requirements

Using `system.ai` schema permissions requires Unity Catalog to be enabled for the account, account admin or Unity Catalog admin privileges, and explicit enablement of the feature by the Databricks account team. Account admins can then manage access through the account-level preview settings. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that manages the `system.ai` schema
- [AI Gateway](/concepts/ai-gateway.md) — Rate limits and request-level usage tracking
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The models served from the `system.ai` schema
- [Foundation Model APIs compliance and security](/concepts/foundation-model-apis-compliance-standards.md) — Security posture for hosted models

### Sources

- foundation-model-unity-catalog-permissions-databricks-on-aws.md

# Citations

1. [foundation-model-unity-catalog-permissions-databricks-on-aws.md](/references/foundation-model-unity-catalog-permissions-databricks-on-aws-cd5ede3c.md)
