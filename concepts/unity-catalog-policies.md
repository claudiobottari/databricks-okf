---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9f5b5867319b26348272f82d223e7fb6cc46b24c20320c04a9f685e67792d6f0
  pageDirectory: concepts
  sources:
    - attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-policies
    - UCP
    - Unity Catalog ABAC policies
  citations:
    - file: attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: Unity Catalog Policies
description: Policies attached at hierarchy levels (catalog, schema, table) that are evaluated dynamically to enforce access rules based on attributes.
tags:
  - policies
  - access-control
  - unity-catalog
timestamp: "2026-06-18T14:28:18.126Z"
---

# Unity Catalog Policies

**Unity Catalog Policies** are a core access control mechanism in [Unity Catalog](/concepts/unity-catalog.md) that enable dynamic, attribute-based authorization for securable objects. Rather than requiring static grants on individual objects, policies evaluate conditions against attributes at access time, allowing a single policy to govern access across an entire catalog or schema. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Overview

Unity Catalog implements [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) through several types of policies. Each policy type is defined at a specific level in the Unity Catalog hierarchy — such as a catalog, schema, or table — and is evaluated dynamically when a user attempts to access a securable object. When a securable object has the attributes targeted by a policy, that policy takes effect automatically, ensuring consistent access rules without requiring per-object grants. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Policy Types

Unity Catalog supports three primary types of policies:

### Row Filter Policies

Row filter policies restrict the rows that a user can see when querying a table, materialized view, or streaming table. These policies use a user-defined function (UDF) to implement the filter logic, returning only the rows the user is authorized to view. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

### Column Mask Policies

Column mask policies obscure the values in specific columns for unauthorized users. Like row filters, they use a UDF to implement the masking logic, such as showing a partial credit card number or redacting personally identifiable information. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

### GRANT Policies (Beta)

[ABAC GRANT Policies](/concepts/abac-grant-policy.md) dynamically grant privileges to securable objects whose governed tags match a specified condition. Currently in Beta, GRANT policies support `EXECUTE` on models, including both customer-registered MLflow Models and Databricks-hosted foundation models. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## How Policies Work

Policies are attached at a level in the Unity Catalog hierarchy and are evaluated dynamically at access time. When a securable object has the attributes (represented through [Governed Tags](/concepts/governed-tags.md)) targeted by a policy, that policy takes effect automatically. This design means a single policy can enforce consistent access rules across an entire catalog or schema without requiring individual grants on each object. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

For GRANT policies specifically, Unity Catalog evaluates the policy's `WHEN` condition against the governed tags on each securable object in the policy's scope every time access is checked, granting the privilege on every securable object that matches. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Key Differences Between Policy Types

Row filter and column mask policies restrict the *content* of data a user can already access, while GRANT policies determine whether the user can access the object at all. Additionally, row filter and column mask policies require a user-defined function (UDF) to implement the filter or mask, whereas GRANT policies do not use UDFs — the condition is expressed inline in the policy definition. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Viewing Policies

You can view policies using SQL commands. `SHOW POLICIES` lists the policies defined on a securable object, while `SHOW EFFECTIVE POLICIES` also includes policies inherited from parent scopes, such as catalog-level policies that affect a schema. The `DESCRIBE POLICY` command shows the details of a specific policy, including its name, securable object, principals, privileges, and conditions. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [ABAC GRANT Policies](/concepts/abac-grant-policy.md) — Dynamic privilege grants based on governed tags
- [Governed Tags](/concepts/governed-tags.md) — Attributes used in policy conditions to determine access
- [System Tags](/concepts/system-tags.md) — Predefined attributes provided by Databricks
- [Row Filter Policies](/concepts/row-filter-policies.md) — Policies that restrict data content
- [Column Mask Policies](/concepts/column-mask-policies.md) — Policies that mask sensitive columns
- [Unity Catalog Securable Objects](/concepts/unity-catalog-securable-objects.md) — Objects that can be governed by policies
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — The broader access control model

## Sources

- attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [attribute-based-access-control-in-unity-catalog-databricks-on-aws.md](/references/attribute-based-access-control-in-unity-catalog-databricks-on-aws-23c11bc2.md)
2. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
