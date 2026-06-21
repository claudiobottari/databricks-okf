---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 58482b8fb3c84f56b3f2ca5d0ea348960b3a66c4fd472f4df36e5b6e1fa5a911
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - union-of-direct-grants-and-grant-policies
    - GRANT Policies and Union of Direct Grants
    - UODGAGP
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: Union of Direct Grants and GRANT Policies
description: Effective privileges on an object are the union of direct grants and any applicable GRANT policies, meaning a more selective GRANT policy does not override a broader direct grant.
tags:
  - access-control
  - permissions
  - unity-catalog
timestamp: "2026-06-18T14:15:48.473Z"
---

# Union of Direct Grants and GRANT Policies

**Union of Direct Grants and GRANT Policies** refers to the combined effect of both traditional direct `GRANT` statements and attribute-based [GRANT policies](/concepts/abac-grant-policy.md) in [Unity Catalog](/concepts/unity-catalog.md), where the effective privileges on a securable object are determined by the union of both access control mechanisms. This concept is fundamental to understanding how access is actually computed when both methods are in use.

## How the Union Works

The effective privileges on any securable object in Unity Catalog are the **union** of:

- Privileges granted through direct `GRANT` statements (assigned explicitly to specific securable objects, their parent schemas, or their catalogs)
- Privileges granted through ABAC GRANT policies that dynamically match based on governed tags and conditions

A principal holds `EXECUTE` on a model when **any** of the following is true:

1. A GRANT policy attached to the model's catalog or schema lists the principal in its `TO` clause (and not in `EXCEPT`), and the policy's `WHEN` condition matches the tags on the model.
2. A direct `GRANT EXECUTE` on the model, its schema, or its catalog is in effect for that principal — whether granted directly, through group membership, or through other administrative privileges.

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

Because access is the union of these sources, a more selective GRANT policy does **not** mean that an excluded principal lacks `EXECUTE`. The principal can still hold the privilege through a direct grant on the model, or its parent schema or catalog. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Implications for Access Control

### GRANT Policies Do Not Override Direct Grants

GRANT policies are not exclusive — they add access but do not remove access granted through other means. If you intend to use GRANT policies as the primary way to control `EXECUTE` on models, first determine whether any direct grants already in place might override the policy. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Auditing Effective Access

To determine the **actual** effective access for a principal, you must check both sources:

1. **List GRANT policies** whose scope covers the models in that schema or catalog:
   - SQL: `SHOW EFFECTIVE POLICIES ON SCHEMA <parent_schema>` (or `ON CATALOG <parent_catalog>`)
   - REST API: `GET /api/2.1/unity-catalog/policies/{on_securable_type}/{on_securable_fullname}?include_inherited=true`
   - Python SDK: `w.policies.list_policies(..., include_inherited=True)`

2. **Enumerate direct grants** on the model and its ancestors:
   - SQL: `SHOW GRANTS` on the model and its ancestors
   - For direct grants: `GET /api/2.1/unity-catalog/permissions/{securable_type}/{full_name}`
   - For union of direct and inherited grants: `GET /api/2.1/unity-catalog/effective-permissions/{securable_type}/{full_name}` (Python SDK: `w.grants.get_effective(...)`)

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Important Distinction

`SHOW GRANTS` does **not** return privileges granted by a GRANT policy. GRANT policies are not visible through standard `SHOW GRANTS` output. To see all `EXECUTE` access on a model, combine `SHOW GRANTS` output for the model with the GRANT policies returned by `SHOW EFFECTIVE POLICIES` on its parent schema or catalog. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Best Practices for Managing the Union

To avoid confusion and audit complexity when both mechanisms are in use:

- **Don't mix GRANT policies and direct grants for the same privilege.** For a given privilege on a securable, choose either GRANT policies or direct grants, not both. GRANT policies union with direct grants, so mixing them on the same securable makes it harder to reason about who has access and to audit changes. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Use direct grants for `USE CATALOG` and `USE SCHEMA`**, and GRANT policies for `EXECUTE`. GRANT policies do not grant the prerequisite permissions required to access a model. Grant those directly, and use a GRANT policy to scope `EXECUTE` on individual models by tag. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Current Scope (Beta)

In the current Beta release, the union applies specifically to:
- One privilege type: `EXECUTE`
- One securable type: Models (both customer-registered MLflow Models and Databricks-hosted foundation models in `system.ai`)

Additional privileges and securable types will be supported in future releases. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — The attribute-based policy mechanism that forms one part of the union
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer where both mechanisms coexist
- [Direct Grants](/concepts/grant-policy-vs-direct-grant.md) — Traditional privilege assignment via `GRANT` statements
- [Effective Permissions](/concepts/feature-store-wide-permissions.md) — The computed result of the union for a given principal
- [SHOW EFFECTIVE POLICIES](/concepts/show-effective-policies.md) — SQL command for listing inherited policies

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
