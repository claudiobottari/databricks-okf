---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 81fd20522901e23e1abef11f4b2acd4157431d9eb2d8ea222dba734552217ed3
  pageDirectory: concepts
  sources:
    - foundation-model-unity-catalog-permissions-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-allow-list-via-unity-catalog-permissions
    - MAVUCP
  citations:
    - file: foundation-model-unity-catalog-permissions-databricks-on-aws.md
title: Model Allow-List via Unity Catalog Permissions
description: A security pattern where admins remove default EXECUTE from system.ai schema and selectively grant EXECUTE only on approved models, creating an explicit allow-list of accessible models.
tags:
  - security-pattern
  - unity-catalog
  - access-control
timestamp: "2026-06-18T12:26:02.744Z"
---

Here is the wiki page based on the provided source material.

---

---
title: Model Allow-List via Unity Catalog Permissions
summary: A method to restrict access to specific Databricks-hosted foundation models by using Unity Catalog permissions on the system.ai schema and individual model objects, creating an allow-list of permitted models.
sources:
  - foundation-model-unity-catalog-permissions-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:32:47.595Z"
updatedAt: "2026-06-18T11:32:47.595Z"
tags:
  - unity-catalog
  - access-control
  - foundation-models
  - ai
  - security
aliases:
  - model-allow-list-via-unity-catalog-permissions
  - MALUCP
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Model Allow-List via Unity Catalog Permissions

**Model Allow-List via Unity Catalog Permissions** is a governance method that lets account admins restrict which [Databricks-hosted foundation models](/concepts/databricks-hosted-foundation-models.md) their organization can access. By manipulating Unity Catalog `EXECUTE` permissions on the `system.ai` schema and individual model objects, an admin creates an allow-list of approved model families while blocking all others. This enforcement is consistent across pay-per-token, provisioned throughput, and batch inference (AI Functions) workloads. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## When to use this feature[^fn:1]

Use this feature only when legally or organizationally required to restrict which specific models are open — for example, for export-controlled model families, vendor-restricted or region-restricted models, or corporate policies prohibiting specific foundation models. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

For day-to-day governance, use:
- `system.billing` for cost tracking and attribution
- [AI Gateway](/concepts/ai-gateway.md) for rate limits and request-level usage tracking
- Private Link or private networking for secure connectivity
- Egress and network controls for restricting outbound traffic

## How it works[^fn:2]

By default, all users have `EXECUTE` permission on the `system.ai` schema, which opens all Databricks-hosted foundation models. To create an allow-list, the admin removes this default permission and then selectively grants `EXECUTE` on approved individual models. The system enforces permissions consistently across all model access patterns. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Enforcement behavior

| Workload | Enforcement |
|----------|-------------|
| Pay-per-token endpoints | Automatically enforced |
| Batch inference (AI Functions) | Automatically enforced |
| Provisioned throughput endpoints | Require manual deletion of disallowed endpoints |

## Requirements[^fn:3]

- Unity Catalog must be enabled for your account.
- You must have account admin or Unity Catalog admin privileges.
- The feature must be enabled for your account (contact your Databricks account team).

## Step-by-step instructions[^fn:4]

### Step 1: Remove EXECUTE permission from the schema

Removing `EXECUTE` from the `system.ai` schema clears all default access. No user can invoke any model until permissions are explicitly re-granted.

1. Go to **Catalog**.
2. Select the **system** catalog, then the **ai** schema.
3. Click the **Permissions** tab.
4. Revoke `EXECUTE` from **All Users** (or from all groups).

After this step, pay-per-token and batch inference calls to all models stop immediately. Provisioned throughput endpoints continue serving until manually deleted. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Step 2: Grant `EXECUTE` on approved models

For each approved model:
1. In Catalog Explorer, navigate to **system** > **ai** > **models** > your target model.
2. Click the **Permissions** tab.
3. Grant `EXECUTE` to **All Users**, or to specific groups.

Repeat for each approved model. This creates an allow-list of permitted models. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Step 3: Remove disallowed provisioned throughput endpoints

Delete all provisioned throughput endpoints that serve a disallowed model. Active endpoints continue serving until removed — they do not automatically enforce the new permissions. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Limitations[^fn:5]

- **Knowledge Assistant**: Agent Bricks Knowledge Assistant does not support foundation model Unity Catalog permissions. Contact your Databricks account team before enabling this feature if you actively use Knowledge Assistant.

## Related concepts

- [Unity Catalog permissions](/concepts/unity-catalog-permissions-model.md) – The permission model that underpins this access control
- [AI Gateway](/concepts/ai-gateway.md) – Rate limits and request-level tracking for model APIs
- system.billing – Cost tracking for model usage Attribution
- [Databricks-hosted foundation models](/concepts/databricks-hosted-foundation-models.md) – The models governed by this policy

## Sources

- foundation-model-unity-catalog-permissions-databricks-on-aws.md

# Citations

1. [foundation-model-unity-catalog-permissions-databricks-on-aws.md](/references/foundation-model-unity-catalog-permissions-databricks-on-aws-cd5ede3c.md)
