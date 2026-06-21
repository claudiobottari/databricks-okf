---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2d37f259e087ad68c33114c26aa9550b07ab83e01440022809c55bd0adebcad5
  pageDirectory: concepts
  sources:
    - attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grant-policies-beta
    - GP(
    - ABAC GRANT Policies (Beta)
    - GRANT Policies
    - GRANT policies
    - Grant Policies
    - GRANT Policies for Models (Beta)
    - GRANT Policy
    - GRANT Policy for Models (Beta)
    - GRANT policy
  citations:
    - file: attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
title: GRANT Policies (Beta)
description: ABAC policy type for dynamic privilege grants, currently scoped to EXECUTE permission on models in Unity Catalog
tags:
  - access-control
  - dynamic-privileges
  - unity-catalog
timestamp: "2026-06-19T22:08:52.533Z"
---

# GRANT Policies (Beta)

**GRANT Policies** are an attribute-based access control (ABAC) policy type in [Unity Catalog](/concepts/unity-catalog.md) that dynamically grant Unity Catalog privileges when their tag-based condition matches a securable object's tags. Unlike traditional `GRANT` statements that must be issued for each object individually, GRANT policies evaluate a condition against the attributes of securable objects within their scope every time access is checked, granting the specified privilege on every matching object. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## How GRANT Policies Work

Each time a user attempts to access a securable object, Unity Catalog identifies all GRANT policies whose scope covers the object, checks whether the user is in the `TO` list and not in the `EXCEPT` list, and evaluates the policy's `WHEN` condition against the tags on the securable, including inherited tags. If the policy applies, Unity Catalog grants the privilege. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

The effective privileges on an object are the union of direct grants and any applicable GRANT policies. A principal has the privilege if a GRANT policy in scope applies to that principal or a direct `GRANT` of the same privilege applies. GRANT policies only add access—they cannot revoke access that was granted directly. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Current Scope (Beta)

GRANT policies are currently in Beta. In this release, they support one privilege on one securable type: `EXECUTE` on models. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Differences from Row Filter and Column Mask Policies

ABAC also supports [row and column-level security](/concepts/row-level-security-rls-policies.md) through row filter policies and column mask policies on tables, materialized views, and streaming tables. GRANT policies differ from these in two key ways: ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

- **No UDFs required:** Row filter and column mask policies require user-defined functions (UDFs) to implement filtering or masking logic. GRANT policies do not use UDFs—the condition is expressed inline in the policy definition. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]
- **Privilege grants vs. data filtering:** GRANT policies dynamically grant privileges (e.g., `EXECUTE`), whereas row filter and column mask policies restrict which data a user can see or how column values are presented. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Policy Definition

GRANT policies use the same evaluation model as row filter and column mask policies, with the exception that they do not use UDFs. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

Each GRANT policy specifies: ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

- **Scope:** The securable object where the policy is attached, specified by the `ON` clause. Supported policy scopes are `CATALOG` and `SCHEMA`. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]
- **Securable type:** Models only, specified using `GRANT EXECUTE FOR MODELS`. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]
- **Principals:** Who the policy applies to (`TO` clause) and who is exempt (`EXCEPT` clause). ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]
- **Conditions:** Tag-based expressions in the `WHEN` clause that determine which securable objects the policy targets. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that provides ABAC capabilities
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — The broader access control model
- [Governed Tags](/concepts/governed-tags.md) — Attributes used in policy conditions to identify which data a policy should protect
- [Row Filter Policies](/concepts/row-filter-policies.md) — ABAC policies that restrict data content
- [Column Mask Policies](/concepts/column-mask-policies.md) — ABAC policies that mask sensitive columns
- User-Defined Functions (UDFs) — Required for row filter and column mask policies, but not for GRANT policies

## Sources

- attribute-based-access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [attribute-based-access-control-in-unity-catalog-databricks-on-aws.md](/references/attribute-based-access-control-in-unity-catalog-databricks-on-aws-23c11bc2.md)
