---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4d2e6707d2c83b20f94207977f6cc92ad1c8fe7caf1225bc210cdb4a0144a8a3
  pageDirectory: concepts
  sources:
    - foundation-model-unity-catalog-permissions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foundation-model-unity-catalog-permissions
    - FMUCP
    - Foundation Model Access in Unity Catalog
  citations:
    - file: foundation-model-unity-catalog-permissions-databricks-on-aws.md
title: Foundation Model Unity Catalog Permissions
description: A Databricks feature that allows account admins to restrict which Databricks-hosted foundation models users and groups can access using Unity Catalog permissions on the system.ai schema.
tags:
  - databricks
  - permissions
  - foundation-models
  - unity-catalog
timestamp: "2026-06-19T18:55:21.893Z"
---

```markdown
---
title: Foundation Model Unity Catalog Permissions
summary: A Databricks feature that uses Unity Catalog permissions on the system.ai schema to restrict which Databricks-hosted foundation models users and groups can access.
sources:
  - foundation-model-unity-catalog-permissions-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:25:52.419Z"
updatedAt: "2026-06-19T10:39:51.545Z"
tags:
  - databricks
  - permissions
  - foundation-models
aliases:
  - foundation-model-unity-catalog-permissions
  - FMUCP
confidence: 0.99
provenanceState: extracted
inferredParagraphs: 0
---

# Foundation Model Unity Catalog Permissions

**Foundation Model Unity Catalog Permissions** is an access control feature that allows account administrators to restrict which Databricks-hosted foundation models users and groups can invoke. It uses Unity Catalog permissions on the `system.ai` schema and individual model objects to enforce model‑level restrictions consistently across pay‑per‑token, provisioned throughput, and batch inference (AI Functions) workloads.^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## When to Use

Use this feature only when legally or organizationally required to restrict access to specific models, such as:

- Export-controlled model families
- Vendor-restricted or region-restricted models
- Corporate policies prohibiting specific foundation models

For day-to-day governance of foundation model usage, Databricks recommends using:
- `system.billing` for cost tracking and attribution
- [[AI Gateway]] for rate limits and request-level usage tracking
- Private Link or private networking for secure connectivity
- Egress and network controls for restricting outbound traffic

^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## How It Works

By default, all users have `EXECUTE` permission on the `system.ai` schema, which grants access to all Databricks-hosted foundation models. To restrict access, an admin removes the default `EXECUTE` permission from the schema and then selectively grants `EXECUTE` on approved individual models.^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

The system enforces permissions consistently across:
- **Pay-per-token** endpoints — automatically enforced
- **Batch inference (AI Functions)** — automatically enforced
- **Provisioned throughput** endpoints — require manual deletion of disallowed endpoints

After you remove `EXECUTE` from the schema, pay-per-token and batch inference calls to all models stop immediately. Provisioned throughput endpoints continue serving until manually deleted.^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Requirements

- Unity Catalog must be enabled for your account.
- Account admin or [[Unity Catalog]] admin privileges.
- The feature must be enabled for your account. Contact your Databricks account team to request enablement.^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Configuration Steps

### Step 1: Remove `EXECUTE` Permission from the Schema

Removing `EXECUTE` from the `system.ai` schema clears all default access to models. No user can invoke any model until explicit permissions are re‑granted.^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

1. Go to **Catalog**. Select the **system** catalog, then the **ai** schema. Click the **Permissions** tab.
2. Revoke `EXECUTE` from **All Users** (or from all groups).

After this step, pay-per-token and batch inference (AI Functions) calls to all models stop immediately. Provisioned throughput endpoints continue serving until manually deleted.^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Step 2: Grant `EXECUTE` on Approved Models

For each model your organization approves, selectively grant `EXECUTE` privilege.^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

1. In Catalog Explorer, under the **system** catalog, select **ai** > **models**, then your target model.
2. Click the **Permissions** tab.
3. Grant `EXECUTE` to **All Users**, or to specific groups.

Repeat for each approved model. This creates an allow‑list of permitted models.^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Step 3: Remove Disallowed Provisioned Throughput Endpoints

Delete all provisioned throughput endpoints that serve a disallowed model. Active endpoints continue serving until removed. Pay‑per‑token and batch inference (AI Functions) endpoints automatically enforce the new permissions; provisioned throughput endpoints do not, so manual deletion is required for those.^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Limitations

**Agent Bricks Knowledge Assistant** does not support foundation model Unity Catalog permissions. If your organization actively uses Knowledge Assistant, contact your Databricks account team before enabling this feature.^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Related Concepts

- [[AI Gateway]]
- [[Unity Catalog]]
- [[Foundation Model APIs]]
- [[system.ai schema]]
- [[Provisioned Throughput Endpoints]]
- [[AI Functions and Batch Inference|Batch Inference (AI Functions)]]

## Sources

- foundation-model-unity-catalog-permissions-databricks-on-aws.md
```

# Citations

1. [foundation-model-unity-catalog-permissions-databricks-on-aws.md](/references/foundation-model-unity-catalog-permissions-databricks-on-aws-cd5ede3c.md)
