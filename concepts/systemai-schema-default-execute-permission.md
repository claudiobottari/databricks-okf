---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0cbab165a675f90b8d48b2ff1e78b59899f8a5369c64ccfffd9029ea6dc288eb
  pageDirectory: concepts
  sources:
    - foundation-model-unity-catalog-permissions-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - systemai-schema-default-execute-permission
    - SSDEP
  citations:
    - file: foundation-model-unity-catalog-permissions-databricks-on-aws.md
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: System.ai Schema Default EXECUTE Permission
description: The default permission model where all users have EXECUTE on the system.ai schema, granting access to all Databricks-hosted foundation models until an admin revokes it.
tags:
  - unity-catalog
  - permissions
  - databricks
timestamp: "2026-06-18T12:26:29.885Z"
---

# System.ai Schema Default EXECUTE Permission

The `system.ai` schema in Unity Catalog contains all Databricks-hosted foundation models. By default, all users receive `EXECUTE` permission on this schema, which grants access to every foundation model in the catalog.^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

This default permission simplifies model access for most teams, but can be removed and replaced with selective grants when regulatory, vendor, or corporate policy requirements demand restricting access to specific models.^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## How It Works

Foundation model Unity Catalog permissions use standard Unity Catalog permissions on the `system.ai` schema and individual model objects. The system enforces these permissions consistently across all model access patterns:^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

- **Pay-per-token endpoints** — automatically enforced
- **Batch inference (AI Functions)** — automatically enforced
- **Provisioned throughput endpoints** — require manual deletion of disallowed endpoints

By default, `EXECUTE` is granted to all users on the `system.ai` schema, opening every hosted foundation model. To restrict access, account admins remove this default schema-level grant and selectively grant `EXECUTE` only on approved individual models.^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## When to Modify the Default

Consider restricting the default `EXECUTE` permission only when legally required to control which specific models are accessible. Common scenarios include:^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

- **Export-controlled model families** — Models subject to international trade regulations
- **Vendor-restricted or region-restricted models** — Models limited by licensing agreements or geographic availability
- **Corporate policies** — Internal policies prohibiting use of specific foundation models

For day-to-day governance needs such as cost tracking or usage monitoring, Databricks recommends using other tools instead of model-level permissions:^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

| Governance Need | Recommended Tool |
|----------------|-----------------|
| Cost tracking and attribution | `system.billing` |
| Rate limits and request tracking | [AI Gateway](/concepts/ai-gateway.md) |
| Secure connectivity | Private Link or private networking |
| Outbound traffic control | Egress and network controls |

## Modifying the Default Permission

### Step 1: Remove EXECUTE from the Schema

1. In Catalog Explorer, navigate to **system** > **ai**.
2. Open the **Permissions** tab.
3. Revoke `EXECUTE` from **All Users** (or from all applicable groups).

After removing `EXECUTE` from the schema, pay-per-token and batch inference calls to all models stop immediately. Provisioned throughput endpoints continue serving until manually deleted.^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Step 2: Grant EXECUTE on Approved Models

For each approved model, selectively restore access:^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

1. In Catalog Explorer, go to **system** > **ai** > **models**, then select the target model.
2. Open the **Permissions** tab.
3. Grant `EXECUTE` to **All Users**, or to specific groups.

Repeat for each approved model. This creates an allow-list of permitted models.^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Step 3: Remove Disallowed Provisioned Throughput Endpoints

Provisioned throughput endpoints do not automatically enforce permissions changes. You must manually delete any endpoints serving disallowed models.^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Requirements

- Unity Catalog must be enabled for your account.
- Account admin or Unity Catalog admin privileges.
- The feature must be enabled for your account by your Databricks account team.^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Alternative: Using GRANT Policies for Foundation Model Access

Instead of individually granting `EXECUTE` on each approved model, you can use [ABAC GRANT Policy](/concepts/abac-grant-policy.md) to dynamically grant access to foundation models based on system tags. For example, a single policy can grant `EXECUTE` on all models tagged with a specific `ai.model_creator` value, automatically covering any new models from that creator.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Limitations

- **Knowledge Assistant**: The Agent Bricks Knowledge Assistant does not support foundation model Unity Catalog permissions. Contact your Databricks account team before enabling this feature if using Knowledge Assistant.^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The APIs for accessing Databricks-hosted models
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer managing the `system.ai` schema permissions
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Attribute-based policies for granting model access dynamically
- [System Tags](/concepts/system-tags.md) — Tags like `ai.model_creator` used in ABAC policies for model access
- [AI Gateway](/concepts/ai-gateway.md) — Tool for rate limits and request-level tracking

## Sources

- foundation-model-unity-catalog-permissions-databricks-on-aws.md
- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [foundation-model-unity-catalog-permissions-databricks-on-aws.md](/references/foundation-model-unity-catalog-permissions-databricks-on-aws-cd5ede3c.md)
2. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
