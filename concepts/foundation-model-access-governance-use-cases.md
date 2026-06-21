---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 34ac9bdc8946113c80f9ad2b0e10209eb7997edf9fb1d83905831a7fe8bc5564
  pageDirectory: concepts
  sources:
    - foundation-model-unity-catalog-permissions-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foundation-model-access-governance-use-cases
    - FMAGUC
  citations:
    - file: foundation-model-unity-catalog-permissions-databricks-on-aws.md
title: Foundation Model Access Governance Use Cases
description: The distinction between when to use foundation model Unity Catalog permissions (export controls, vendor restrictions, corporate policies) versus other governance tools like billing, AI Gateway, and network controls.
tags:
  - governance
  - best-practice
  - compliance
timestamp: "2026-06-18T12:26:17.384Z"
---

---
title: Foundation Model Access Governance Use Cases
summary: Scenarios and procedures for using Unity Catalog permissions to restrict access to Databricks-hosted foundation models, such as enforcing export control, vendor restrictions, or corporate policies.
sources:
  - foundation-model-unity-catalog-permissions-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - access-control
  - foundation-models
  - unity-catalog
  - governance
aliases:
  - foundation-model-governance-use-cases
  - FMAGUC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Foundation Model Access Governance Use Cases

**Foundation Model Access Governance Use Cases** describes the situations in which an organization applies [Unity Catalog](/concepts/unity-catalog.md) permissions on the `system.ai` schema and individual model objects to restrict which Databricks-hosted foundation models users can invoke. This governance model is intended for legally mandated restrictions, not for everyday cost or rate management. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## When to Use This Feature

This feature is designed for scenarios where an organization must block specific foundation models for legal or contractual reasons, such as:

- **Export-controlled model families** — Models subject to international trade regulations.
- **Vendor-restricted or region-restricted models** — Models that the provider limits to specific geographies or contractual agreements.
- **Corporate policies prohibiting specific foundation models** — Internal security or ethics policies that ban certain model providers or model types.

For day-to-day governance tasks (cost tracking, rate limits, network security), Databricks recommends using separate features: `system.billing` for cost attribution, [AI Gateway](/concepts/ai-gateway.md) for rate limits and request-level usage tracking, Private Link or private networking for secure connectivity, and egress/network controls for outbound traffic restrictions. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## How It Works

Foundation model access governance uses Unity Catalog permissions on the `system.ai` schema and individual model objects within that schema. By default, all users have `EXECUTE` permission on the `system.ai` schema, which opens all Databricks-hosted foundation models. To restrict access, an admin removes the default `EXECUTE` on the schema and then selectively grants `EXECUTE` on approved individual models. The enforcement applies consistently across pay-per-token endpoints, batch inference ([AI Functions](/concepts/ai-functions.md)), and provisioned throughput endpoints (with a manual step for the latter). ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Step-by-Step Procedure

### Step 1: Remove `EXECUTE` Permission from the Schema

Revoke `EXECUTE` from all users (or relevant groups) on the `system.ai` schema. In Catalog Explorer, navigate to **Catalog** → **system** → **ai** → **Permissions** tab, then revoke `EXECUTE` from **All Users**. After this step, pay-per-token and batch inference calls to all models stop immediately. Provisioned throughput endpoints continue serving until manually deleted. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Step 2: Grant `EXECUTE` on Approved Models

For each model your organization approves, grant `EXECUTE` privilege on that model object. In Catalog Explorer, go to **system** → **ai** → **models**, select the target model, click the **Permissions** tab, and grant `EXECUTE` to **All Users** or specific groups. Repeat for every approved model to create an allow-list. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Step 3: Remove Disallowed Provisioned Throughput Endpoints

Delete any [Provisioned Throughput](/concepts/provisioned-throughput.md) endpoints that serve a disallowed model. Pay-per-token and batch inference endpoints automatically enforce the new permissions, but provisioned throughput endpoints do not. Active endpoints will continue serving until you delete them manually. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Limitations

- **Agent Bricks Knowledge Assistant**: The [Knowledge Assistant](/concepts/agent-bricks-knowledge-assistant-incompatibility.md) does not support foundation model Unity Catalog permissions. Contact your Databricks account team before enabling this feature if you actively use Knowledge Assistant.
- Provisioned throughput endpoints require manual deletion after permission changes; they do not automatically respect the new access controls.

## Requirements

- Unity Catalog must be enabled for your account.
- You need account admin or Unity Catalog admin privileges.
- The feature must be enabled for your account by reaching out to your Databricks account team.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance platform that provides the permission model.
- [system.ai Schema](/concepts/systemai-schema.md) — The schema containing Databricks-hosted foundation model objects.
- EXECUTE permission — The privilege required to invoke a model.
- [Pay-per-Token Endpoints](/concepts/pay-per-token-endpoints.md) — Endpoints that automatically enforce model permissions.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Reserved capacity endpoints that require manual cleanup after permission changes.
- [Batch inference (AI Functions)](/concepts/ai-functions.md) — Serverless inference that automatically enforces permissions.
- [AI Gateway](/concepts/ai-gateway.md) — Alternative governance tool for rate limits and usage tracking.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Overview of Databricks hosted model serving.

## Sources

- foundation-model-unity-catalog-permissions-databricks-on-aws.md

# Citations

1. [foundation-model-unity-catalog-permissions-databricks-on-aws.md](/references/foundation-model-unity-catalog-permissions-databricks-on-aws-cd5ede3c.md)
