---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3c7986f68d2f1222ffe9b180bd723d39b357d603cf2d380f0d5df7ddec78d89a
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grant-policy-limitations-and-beta-scope
    - Beta Scope and GRANT Policy Limitations
    - GPLABS
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: GRANT Policy Limitations and Beta Scope
description: "Current Beta limitations: only EXECUTE privilege on models is supported, policies can only be attached at catalog/schema level (not model), SHOW GRANTS doesn't reflect policy-granted privileges, and Delta Sharing is not compatible."
tags:
  - limitations
  - beta
  - unity-catalog
timestamp: "2026-06-18T14:16:12.405Z"
---

# GRANT Policy Limitations and Beta Scope

**GRANT Policy Limitations and Beta Scope** documents the current restrictions and supported functionality for [ABAC GRANT Policies](/concepts/abac-grant-policies.md) in Unity Catalog during their Beta phase. GRANT policies are attribute-based access control policies that dynamically grant privileges to securable objects based on governed tag conditions, but they are not yet fully featured.

## Beta Status

GRANT policies are currently in Beta. During this phase, they support only one privilege on one securable type: `EXECUTE` on models. This covers both customer-registered MLflow Models and Databricks-hosted foundation models in `system.ai`. Additional privileges and securable types will be supported in future releases. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Supported and Unsupported Privileges

### Supported Privilege

- **`EXECUTE` on models** — The only privilege currently available through GRANT policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Unsupported Privileges (Must Use Direct Grants)

The following operations are **not** supported by GRANT policies and must be granted directly using `GRANT` statements: ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

- `CREATE MODEL`
- `CREATE MODEL VERSION`
- `APPLY TAG`
- `USE SCHEMA` (prerequisite permission)
- `USE CATALOG` (prerequisite permission)

## Attachment Scope Limitations

A GRANT policy can only be attached to a catalog or a schema. It **cannot** be attached directly to a model. This means policies are evaluated at the catalog or schema level and apply to all models within that scope whose tags match the policy's condition. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Visibility Limitations

### `SHOW GRANTS` Does Not Reflect GRANT Policies

The `SHOW GRANTS` command does not return privileges granted by a GRANT policy. To see all `EXECUTE` access on a model, you must combine the output of `SHOW GRANTS` for the model with the GRANT policies returned by `SHOW EFFECTIVE POLICIES` on its parent schema or catalog. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### `INFORMATION_SCHEMA` Exclusion

GRANT policies are not included in `INFORMATION_SCHEMA`. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Model Deletion Limitations

Deleting a model or a model version is **not** covered by GRANT policies. These operations must be managed separately through the standard model lifecycle management procedures. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Delta Sharing Restriction

You cannot use [Delta Sharing](/concepts/delta-sharing.md) to share models that have GRANT policies defined on them. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Compute Requirements

Creating, modifying, or dropping GRANT policies with SQL requires a classic compute cluster running Databricks Runtime 18.3 or above. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Interaction with Direct Grants

The effective privileges on an object are the union of direct grants and any applicable GRANT policies. Because access is the union of these sources, a more selective GRANT policy does not mean that an excluded principal lacks `EXECUTE`. The principal can still hold the privilege through a direct grant on the model, or its parent schema or catalog. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Best Practices for Working Within Beta Limitations

- **Use direct grants for `USE CATALOG` and `USE SCHEMA`, GRANT policies for `EXECUTE`.** GRANT policies do not grant the prerequisite permissions required to access a model. Grant those directly, and use a GRANT policy to scope `EXECUTE` on individual models by tag. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Don't mix GRANT policies and direct grants for the same privilege.** For a given privilege on a securable, choose either GRANT policies or direct grants, not both. GRANT policies union with direct grants, so mixing them makes it harder to reason about who has access. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Future Scope

Additional privileges and securable types will be supported in future releases following the Beta period. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [ABAC GRANT Policies](/concepts/abac-grant-policies.md) — The full concept page for GRANT policies
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform providing ABAC capabilities
- [Governed Tags](/concepts/governed-tags.md) — Tags used in GRANT policy conditions
- [System Tags](/concepts/system-tags.md) — Predefined tags provided by Databricks
- MLflow Models — Models securable through GRANT policies
- [Row Filter Policies](/concepts/row-filter-policies.md) — Similar ABAC policies for data content restriction
- [Column Mask Policies](/concepts/column-mask-policies.md) — Similar ABAC policies for data masking
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — The broader access control model
- [Delta Sharing](/concepts/delta-sharing.md) — Sharing mechanism incompatible with GRANT policies on models

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
