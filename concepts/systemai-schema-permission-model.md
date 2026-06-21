---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c56cf3e46c114e88cab5104f55e71060b9dcbfaadf9bd3920f8988e431aac690
  pageDirectory: concepts
  sources:
    - foundation-model-unity-catalog-permissions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - systemai-schema-permission-model
    - SSPM
  citations:
    - file: foundation-model-unity-catalog-permissions-databricks-on-aws.md
title: system.ai Schema Permission Model
description: The Unity Catalog schema (system.ai) that governs access to all Databricks-hosted foundation models through EXECUTE permissions, applied consistently across pay-per-token, provisioned throughput, and batch inference workloads.
tags:
  - unity-catalog
  - permissions
  - schema
timestamp: "2026-06-19T18:55:18.810Z"
---

## system.ai Schema Permission Model

The **system.ai Schema Permission Model** is a granular access control mechanism for Databricks-hosted foundation models. By using [Unity Catalog](/concepts/unity-catalog.md) permissions on the `system.ai` schema and individual model objects, account administrators can restrict which models users can invoke, consistently across pay-per-token, provisioned throughput, and batch inference (AI Functions) workloads. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### When to Use

This feature is designed for legally required restrictions, such as export-controlled model families, vendor-restricted or region-restricted models, or corporate policies prohibiting specific foundation models. For day-to-day governance, Databricks recommends using `system.billing` for cost tracking, [AI Gateway](/concepts/ai-gateway.md) for rate limits and usage tracking, and networking controls like Private Link for secure connectivity. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Default Behavior

By default, all users have `EXECUTE` permission on the `system.ai` schema, which opens all Databricks-hosted foundation models. Removing this default permission and selectively granting `EXECUTE` on approved models creates an allow‑list approach. Enforcement is automatic for pay-per-token and batch inference endpoints; provisioned throughput endpoints require manual deletion of disallowed endpoints. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Requirements

- Unity Catalog must be enabled for the account.
- Account admin or [Unity Catalog admin](/concepts/unity-catalog-admin-roles.md) privileges.
- The feature must be enabled by the Databricks account team. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Step-by-Step Configuration

1. **Remove `EXECUTE` from the `system.ai` schema** – Revoke `EXECUTE` from **All Users** (or all groups) via the Catalog Explorer's Permissions tab. After removal, pay-per-token and batch inference calls to all models stop immediately. Provisioned throughput endpoints continue serving until manually deleted. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

2. **Grant `EXECUTE` on approved models** – In Catalog Explorer, navigate to `system.ai.models`, select the target model, open the Permissions tab, and grant `EXECUTE` to **All Users** or to specific groups. Repeat for each approved model. This builds an explicit allow‑list. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

3. **Remove disallowed provisioned throughput endpoints** – Manually delete all provisioned throughput endpoints that serve a disallowed model. Active endpoints continue serving until removed. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Limitations

- **Agent Bricks Knowledge Assistant** does not support foundation model Unity Catalog permissions. Customers using Knowledge Assistant should contact their Databricks account team before enabling this feature. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Unity Catalog Permissions](/concepts/unity-catalog-permissions-model.md)
- [AI Gateway](/concepts/ai-gateway.md)
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md)
- [Batch Inference (AI Functions)](/concepts/ai-functions-and-batch-inference.md)

### Sources

- foundation-model-unity-catalog-permissions-databricks-on-aws.md

# Citations

1. [foundation-model-unity-catalog-permissions-databricks-on-aws.md](/references/foundation-model-unity-catalog-permissions-databricks-on-aws-cd5ede3c.md)
