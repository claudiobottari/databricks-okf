---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e409b0d1cb9913941480d680440da365509e75e4be04c62bd576f1cb057dd3cf
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grant-policy-effective-privilege-union-model
    - GPEPUM
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: GRANT Policy Effective Privilege Union Model
description: The effective privileges on a securable object are the union of direct grants and any applicable GRANT policies, meaning a more selective policy does not override existing direct grants.
tags:
  - access-control
  - unity-catalog
  - authorization
  - security
timestamp: "2026-06-19T08:47:19.805Z"
---

# GRANT Policy Effective Privilege Union Model

The **GRANT Policy Effective Privilege Union Model** describes how [Unity Catalog](/concepts/unity-catalog.md) determines a principal's effective privileges on a securable object when both [ABAC GRANT Policies](/concepts/abac-grant-policies.md) and traditional Direct GRANT statements are in place. Effective privileges are computed as the **union** of all applicable GRANT policies and direct grants — a principal gains access if either source grants the privilege. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Overview

ABAC GRANT policies dynamically grant privileges on securable objects based on governed tags, while direct grants assign privileges by explicitly naming objects in the three-level namespace (`catalog.schema.object`). Because Unity Catalog combines both mechanisms, a principal may hold a privilege through a direct grant even when a GRANT policy would not have granted it, and vice versa. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## How the Union Works

A principal holds the `EXECUTE` privilege on a model when **any** of the following is true: ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

- A GRANT policy attached to the model’s catalog or schema lists the principal in its `TO` clause (and not in `EXCEPT`), and the policy’s tag-based `WHEN` condition matches the model’s tags.
- A direct `GRANT EXECUTE ON MODEL` statement (or an inherited grant from the parent schema or catalog) is in effect for that principal — whether granted directly, through group membership, or through administrative privileges.

The union is evaluated at query time: the system checks all sources of privilege and returns `EXECUTE` if at least one source grants it. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Interaction with Direct Grants

Because access is the union of these sources, a more selective GRANT policy does **not** mean that an excluded principal automatically lacks `EXECUTE`. The principal can still hold the privilege through a direct grant on the model, its schema, or its catalog. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

To understand who truly has access on an object, administrators must inspect both mechanisms: ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

- Use `SHOW EFFECTIVE POLICIES ON SCHEMA <schema>` (or `ON CATALOG <catalog>`) to list every GRANT policy covering models in that scope.
- Use `SHOW GRANTS ON MODEL <model>` and on its ancestors to enumerate direct grants.

## Implications

- **No automatic revocation**: A GRANT policy that excludes a group does not remove a direct grant that already exists. Administrators must ensure consistency between the two systems.
- **Audit complexity**: `SHOW GRANTS` does **not** return privileges awarded by a GRANT policy, so combining outputs from both `SHOW GRANTS` and `SHOW EFFECTIVE POLICIES` is necessary for a complete picture.
- **Best practice**: Databricks recommends not mixing GRANT policies and direct grants for the same privilege on the same securable type. Choosing one mechanism makes it easier to reason about who has access and simplifies auditing. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Example Scenario

Consider a GRANT policy that grants `EXECUTE` only on models tagged `lifecycle = 'production'` to `analysts`. If the `analysts` group also has a direct `GRANT EXECUTE` on the `staging` schema, members of `analysts` will have `EXECUTE` on all models in `staging` — even those not tagged `production` — because the direct grant overrides the policy’s restriction. The policy and the direct grant are unioned, not intersected. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [ABAC GRANT Policies](/concepts/abac-grant-policies.md)
- Direct GRANT statements
- [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md)
- [Governed Tags](/concepts/governed-tags.md)
- [SHOW EFFECTIVE POLICIES](/concepts/show-effective-policies.md)
- SHOW GRANTS
- [Policy Evaluation Order in ABAC](/concepts/abac-policy-evaluation-and-enforcement.md)

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
