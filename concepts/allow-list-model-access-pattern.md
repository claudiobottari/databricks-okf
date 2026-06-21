---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 70a7034673f593d8db771281d28ac9192eaa020a50222e16a7059218b3990e3f
  pageDirectory: concepts
  sources:
    - foundation-model-unity-catalog-permissions-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - allow-list-model-access-pattern
    - AMAP
  citations:
    - file: foundation-model-unity-catalog-permissions-databricks-on-aws.md
title: Allow-list Model Access Pattern
description: A security pattern for foundation model governance where default EXECUTE permission is revoked from the system.ai schema and then selectively granted on approved individual models.
tags:
  - databricks
  - security
  - governance
timestamp: "2026-06-19T10:39:38.153Z"
---

## Allow-list Model Access Pattern

The **Allow-list Model Access Pattern** is a security governance approach for restricting access to [Databricks-hosted foundation models](/concepts/databricks-hosted-foundation-models.md). It uses [Unity Catalog](/concepts/unity-catalog.md) permissions on the `system.ai` schema to create an explicit allow-list of approved models. By default, all users have `EXECUTE` permission on the `system.ai` schema, which opens all Databricks-hosted foundation models to users. The allow-list pattern reverses this default: the `EXECUTE` permission is removed from the schema, and `EXECUTE` is then selectively granted only on approved individual models. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### When to Use

This pattern is intended for scenarios where legal or regulatory requirements mandate restricting which specific models are accessible. Examples include:

- Export-controlled model families.
- Vendor-restricted or region-restricted models.
- Corporate policies prohibiting specific foundation models. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

For day-to-day governance tasks such as cost tracking, rate limits, or network controls, Databricks recommends using alternative features like `system.billing`, [AI Gateway](/concepts/ai-gateway.md), Private Link, and egress controls rather than the allow-list pattern. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### How It Works

The system enforces the allow-list consistently across three types of workloads: 

- **Pay-per-token** endpoints – automatically enforced.
- **Batch inference (AI Functions)** – automatically enforced.
- **Provisioned throughput** endpoints – require manual deletion of disallowed endpoints after permissions are updated. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Step-by-Step Implementation

**Requirements:** Unity Catalog must be enabled, and the user must have account admin or Unity Catalog admin privileges. The feature must be enabled for the account by contacting the Databricks account team. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

#### Step 1: Remove `EXECUTE` permission from the `system.ai` schema

Removing `EXECUTE` from the schema clears all default access to models. After this step, no user can invoke any model until permissions are explicitly re-granted. In Catalog Explorer, navigate to the **system** catalog, then the **ai** schema, click the **Permissions** tab, and revoke `EXECUTE` from **All Users** (or from all groups). ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

> **Important:** Once `EXECUTE` is removed from the schema, pay-per-token and batch inference calls to all models stop immediately. Provisioned throughput endpoints continue serving until manually deleted. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

#### Step 2: Grant `EXECUTE` on approved models

For each model that the organization approves, selectively grant the `EXECUTE` privilege. In Catalog Explorer, under **system** > **ai** > **models**, select the target model, click the **Permissions** tab, and grant `EXECUTE` to **All Users** or to specific groups. Repeat for each approved model. This creates the allow-list of permitted models. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

#### Step 3: Remove disallowed provisioned throughput endpoints

Provisioned throughput endpoints that serve a disallowed model must be manually deleted. Active endpoints continue serving until removed. Pay-per-token and batch inference endpoints automatically enforce the new permissions, so no additional action is required for those types. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Limitations

The **Agent Bricks Knowledge Assistant** does not support foundation model Unity Catalog permissions. Organizations that actively use Knowledge Assistant should contact their Databricks account team before enabling this feature. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that enforces the permissions.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The service that serves Databricks-hosted models.
- [system.ai Schema](/concepts/systemai-schema.md) – The Unity Catalog schema containing model objects.
- EXECUTE privilege – The permission required to invoke a model.
- [AI Gateway](/concepts/ai-gateway.md) – Alternative mechanism for rate limits and request tracking.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) – Dedicated endpoints that require separate cleanup.
- Batch Inference – AI Functions workloads automatically governed by the allow-list.

### Sources

- foundation-model-unity-catalog-permissions-databricks-on-aws.md

# Citations

1. [foundation-model-unity-catalog-permissions-databricks-on-aws.md](/references/foundation-model-unity-catalog-permissions-databricks-on-aws-cd5ede3c.md)
