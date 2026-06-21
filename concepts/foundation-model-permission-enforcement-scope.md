---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1f25c6e289f284083aa3fd778dbfe54abbb025d018e4df8689e8750fdb8b3d47
  pageDirectory: concepts
  sources:
    - foundation-model-unity-catalog-permissions-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - foundation-model-permission-enforcement-scope
    - FMPES
  citations:
    - file: foundation-model-unity-catalog-permissions-databricks-on-aws.md
title: Foundation Model Permission Enforcement Scope
description: The principle that foundation model Unity Catalog permissions are automatically enforced for pay-per-token and batch inference (AI Functions) but not for provisioned throughput endpoints.
tags:
  - permissions
  - databricks
  - foundation-models
timestamp: "2026-06-18T12:26:26.882Z"
---

# Foundation Model Permission Enforcement Scope

**Foundation Model Permission Enforcement Scope** refers to the scope of enforcement for [Unity Catalog](/concepts/unity-catalog.md) permissions on foundation models hosted by Databricks in the `system.ai` schema. This feature allows account admins to restrict which Databricks-hosted foundation models users can access by controlling `EXECUTE` permissions on individual model objects within Unity Catalog. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Overview

Foundation Model Permission Enforcement Scope defines which workloads and endpoints are subject to Unity Catalog permission controls when an admin removes the default `EXECUTE` permission from the `system.ai` schema and re-grants it selectively on approved models. The enforcement scope varies by inference type: pay-per-token and batch inference endpoints automatically enforce changes, while provisioned throughput endpoints require manual intervention. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Supported Inference Types and Enforcement Behavior

### Pay-per-Token Endpoints

Pay-per-token endpoints automatically enforce Unity Catalog permissions. When an admin removes `EXECUTE` from the `system.ai` schema, calls to pay-per-token endpoints stop immediately for all models not explicitly granted. When `EXECUTE` is re-granted on a specific model, access is restored automatically. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Batch Inference (AI Functions)

Batch inference workloads — also called AI Functions — automatically enforce Unity Catalog permissions. The same rule applies: removing `EXECUTE` from the schema blocks all batch inference calls, and granting `EXECUTE` on individual models allows them. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Provisioned Throughput Endpoints

Provisioned throughput endpoints do **not** automatically enforce Unity Catalog permissions after schema-level changes. If an admin removes `EXECUTE` from the `system.ai` schema, any existing provisioned throughput endpoints serving disallowed models continue to function until manually deleted. Admins must explicitly delete the disallowed provisioned throughput endpoints as part of the enforcement workflow. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Requirements

- Unity Catalog must be enabled for the account.
- The user configuring permissions must have [account admin](/concepts/account-admin-unity-catalog.md) or [Unity Catalog admin](/concepts/unity-catalog-admin-roles.md) privileges.
- The foundation model Unity Catalog permissions feature must be enabled for the account through the Databricks account team. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Enforcement Workflow

### Step 1: Remove EXECUTE from the Schema

Remove the default `EXECUTE` permission on the `system.ai` schema from **All Users** (or from all groups). This clears default access to all models. After this step, pay-per-token and batch inference calls stop immediately for all models. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Step 2: Grant EXECUTE on Approved Models

Selectively grant `EXECUTE` permission on each approved model in `system.ai.models`. This creates an allow-list: only models with explicit grants are accessible. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### Step 3: Delete Disallowed Provisioned Throughput Endpoints

Manually delete any provisioned throughput endpoints that serve models not in the allow-list. Active endpoints continue serving until removed, so this step is essential to fully enforce restrictions. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## When to Use Foundation Model Unity Catalog Permissions

This feature is intended for scenarios where legal or regulatory requirements mandate blocking specific models. Use cases include: ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

- Export-controlled model families
- Vendor-restricted or region-restricted models
- Corporate policies prohibiting specific foundation models

For day-to-day governance, Databricks recommends using alternative controls rather than model-level permissions: ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

- `system.billing` for cost tracking and attribution
- [AI Gateway](/concepts/ai-gateway.md) for rate limits and request-level usage tracking
- Private Link or private networking for secure connectivity
- Egress and network controls for restricting outbound traffic

## Limitations

- **Knowledge Assistant**: The Agent Bricks Knowledge Assistant does not support foundation model Unity Catalog permissions. Contact the Databricks account team before enabling this feature if Knowledge Assistant is actively used. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]
- **Provisioned throughput endpoints** require manual deletion — they do not automatically enforce schema-level permission changes. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer providing permission enforcement
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The API surface for Databricks-hosted models
- [AI Gateway](/concepts/ai-gateway.md) — Rate limiting and usage tracking alternative to model permissions
- [system.ai Schema](/concepts/systemai-schema.md) — The Unity Catalog schema containing foundation model objects
- EXECUTE permission — The privilege controlling model invocation
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Dedicated compute endpoints for model serving

## Sources

- foundation-model-unity-catalog-permissions-databricks-on-aws.md

# Citations

1. [foundation-model-unity-catalog-permissions-databricks-on-aws.md](/references/foundation-model-unity-catalog-permissions-databricks-on-aws-cd5ede3c.md)
