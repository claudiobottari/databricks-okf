---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 35f00560493d451d0f3e2ef97ca9a450124583432b156657cc7694bc5ac406fb
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grant-policy-quotas-and-limitations-beta
    - Limitations (Beta) and GRANT Policy Quotas
    - GPQAL(
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: GRANT Policy Quotas and Limitations (Beta)
description: The current Beta restrictions on GRANT policies including only EXECUTE on models, no direct model attachment, no SHOW GRANTS visibility, and separate quotas.
tags:
  - data-governance
  - access-control
  - beta
  - limitations
timestamp: "2026-06-19T17:23:29.984Z"
---

# GRANT Policy Quotas and Limitations (Beta)

**GRANT Policy Quotas and Limitations (Beta)** describes the current capacity constraints and unsupported scenarios for attribute-based access control (ABAC) GRANT policies on Unity Catalog, as of the Beta release. GRANT policies dynamically grant privileges to securable objects whose governed tags match a condition, but during Beta only one privilege (`EXECUTE` on models) is available, and several restrictions apply. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Overview

GRANT policies are a type of ABAC policy that evaluates a `WHEN` condition against [Governed Tags](/concepts/governed-tags.md) on securable objects every time access is checked. In Beta, they can be attached only at the catalog or schema level and can grant only the `EXECUTE` privilege on [Unity Catalog Models](/concepts/unity-catalog-for-ml-models.md) — both customer-registered MLflow models and Databricks‑hosted foundation models in `system.ai`. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Compute Requirements

Creating, modifying, or dropping GRANT policies using SQL requires a classic compute cluster running Databricks Runtime 18.3 or above. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Quotas

The quota limits for GRANT policies are separate from the [Quotas for Row Filter and Column Mask Policies](/concepts/row-filter-and-column-mask-policies.md). The source document does not specify numerical limits; it only notes that they are distinct and advises referring to the platform documentation for current values. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Limitations

The following limitations apply in the Beta release:

- **Privilege scope:** Only the `EXECUTE` privilege on models is supported. Privileges such as `CREATE MODEL`, `CREATE MODEL VERSION`, and `APPLY TAG` are not covered by GRANT policies and must be granted directly. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Prerequisite permissions:** The `USE SCHEMA` and `USE CATALOG` permissions (required to reach a model) are not supported by GRANT policies and must be granted directly. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Attachment level:** A policy can be attached only to a catalog or a schema, not directly to a model. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Visibility in `SHOW GRANTS`:** Privileges granted by a GRANT policy do not appear in the output of `SHOW GRANTS`. Administrators must use `SHOW EFFECTIVE POLICIES` or the REST API to see policy-based grants. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **`INFORMATION_SCHEMA`:** GRANT policies are not exposed in the `INFORMATION_SCHEMA` views. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Model deletion:** Deleting a model or a model version is not governed by GRANT policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Delta Sharing:** You cannot use [Delta Sharing](/concepts/delta-sharing.md) to share models that have GRANT policies defined on them. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Governed Tags](/concepts/governed-tags.md)
- [Row Filter and Column Mask Policies](/concepts/row-filter-and-column-mask-policies.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- [MLflow Model Registry](/concepts/mlflow-model-registry.md)
- System AI Foundation Models

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
