---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ed9766650556412af6f6c3f4e692cc607bcd98f68f743ecbe99052127112a62d
  pageDirectory: concepts
  sources:
    - foundation-model-unity-catalog-permissions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-allow-listing-via-execute-grants
    - MAVEG
  citations:
    - file: foundation-model-unity-catalog-permissions-databricks-on-aws.md
title: Model Allow-Listing via EXECUTE Grants
description: The pattern of removing default EXECUTE on the system.ai schema and then selectively granting EXECUTE on approved individual model objects to create an allow-list of permitted foundation models.
tags:
  - databricks
  - security
  - model-governance
timestamp: "2026-06-19T18:55:23.112Z"
---

# Model Allow-Listing via EXECUTE Grants

**Model Allow-Listing via EXECUTE Grants** is a Unity Catalog–based mechanism that account administrators can use to restrict access to Databricks-hosted foundation models by explicitly granting the `EXECUTE` privilege only on approved models. By default, all users have `EXECUTE` on the `system.ai` schema, which opens all models; removing that default and selectively granting `EXECUTE` on individual models creates an allow-list. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## When to Use This Feature

This feature is intended only for cases where legal or regulatory requirements mandate restricting specific model families, such as:

- Export-controlled models
- Vendor-restricted or region-restricted models
- Corporate policies that prohibit certain foundation models

For day-to-day governance tasks like cost tracking, rate limiting, or network security, Databricks recommends using separate tools such as `system.billing`, [AI Gateway](/concepts/ai-gateway.md), Private Link, and egress controls. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## How It Works

Foundation model Unity Catalog permissions apply to objects in the `system.ai` schema of Unity Catalog. Initially, the system grants `EXECUTE` on the schema to all users, giving everyone access to all Databricks-hosted foundation models. To restrict access, an administrator removes that default permission and then re‑grants `EXECUTE` on only the approved model objects. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

Enforcement is automatic for:

- **Pay-per-token** endpoints
- **Batch inference (AI Functions)**

For **provisioned throughput** endpoints, enforcement is not automatic; an administrator must manually delete any endpoints that serve a disallowed model. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Step-by-Step Procedure

### 1. Remove `EXECUTE` from the `system.ai` schema

Navigate to the **system** catalog → **ai** schema → **Permissions** tab, and revoke `EXECUTE` from **All Users** (or from all groups). After this step, all pay-per-token and batch inference calls to any model stop immediately. Provisioned throughput endpoints continue serving until deleted. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### 2. Grant `EXECUTE` on approved models

For each approved model, open the model object under `system.ai.models` in Catalog Explorer, go to the **Permissions** tab, and grant `EXECUTE` to **All Users** or to specific groups. Repeat for every model that should remain accessible. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

### 3. Remove disallowed provisioned throughput endpoints

Manually delete any provisioned throughput endpoints that serve a model not in the allow‑list. Active endpoints will not stop serving until deleted. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Requirements

- Unity Catalog must be enabled for the account.
- The user performing the steps must have account admin or Unity Catalog admin privileges.
- The feature itself must be enabled for the account (contact your Databricks account team). ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Limitations

- **Knowledge Assistant**: The Agent Bricks Knowledge Assistant does **not** support foundation model Unity Catalog permissions. Contact your account team before enabling the feature if you actively use Knowledge Assistant. ^[foundation-model-unity-catalog-permissions-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that hosts the `system.ai` schema and permission model.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The set of endpoints affected by EXECUTE grants.
- [AI Gateway](/concepts/ai-gateway.md) – Recommended for rate limiting and request‑level usage tracking.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) – Endpoint type that requires manual cleanup after allow‑listing.

## Sources

- foundation-model-unity-catalog-permissions-databricks-on-aws.md

# Citations

1. [foundation-model-unity-catalog-permissions-databricks-on-aws.md](/references/foundation-model-unity-catalog-permissions-databricks-on-aws-cd5ede3c.md)
