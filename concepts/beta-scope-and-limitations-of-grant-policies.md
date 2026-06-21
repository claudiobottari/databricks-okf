---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bf2df6747213da9b2bb81152fbca51be4b74a9418c39b953b440ff0af93605cc
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - beta-scope-and-limitations-of-grant-policies
    - Limitations of GRANT Policies and Beta Scope
    - BSALOGP
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: Beta Scope and Limitations of GRANT Policies
description: In Beta, GRANT policies only support EXECUTE privilege on models (MLflow and foundation models), cannot grant USE CATALOG/SCHEMA, and policies can only be attached at catalog or schema level, not model level.
tags:
  - unity-catalog
  - abac
  - limitations
  - beta
timestamp: "2026-06-18T10:35:53.159Z"
---

# Beta Scope and Limitations of GRANT Policies

**GRANT policies** are an [ABAC|attribute-based access control (ABAC)](/concepts/attribute-based-access-control-abac.md) mechanism in Unity Catalog that dynamically grant privileges to securable objects based on their governed tags. As of this writing, GRANT policies are in **Beta**, which means the feature is available for evaluation and testing but carries a narrower scope than the full ABAC vision. This page documents exactly what is supported in Beta and what is not, covering privilege types, securable object types, attachment levels, interaction with direct grants, and known limitations. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

---

## Supported Scope in Beta

### Privileges and Securable Types

During Beta, GRANT policies can grant only the **`EXECUTE`** privilege on only one securable type: **models**. This includes both customer-registered MLflow models stored in Unity Catalog and Databricks-hosted foundation models (e.g., those in the `system.ai` schema). No other privileges — such as `CREATE MODEL`, `CREATE MODEL VERSION`, or `APPLY TAG` — are supported, nor are other securable types like tables, volumes, schemas, or catalogs. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Attachment Level

A GRANT policy must be attached to a **catalog** or a **schema**. It cannot be attached directly to a model. The policy’s `WHEN` condition is evaluated against the governed tags on every model within the chosen catalog or schema. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Principals

Policies specify which principals (users, groups, or service principals) receive the privilege via the `TO` clause, and optionally exclude specific principals via `EXCEPT`. Using groups rather than individual users is a best practice because membership changes automatically propagate to the policy. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

---

## How GRANT Policies Interact with Direct Grants

The effective `EXECUTE` privilege on a model is the **union** of all direct grants and any applicable GRANT policies. A principal can access a model if any of the following hold:

- A GRANT policy attached to the model’s catalog or schema includes the principal in `TO` (and not in `EXCEPT`), and the policy’s condition matches the model’s tags.
- A direct `GRANT EXECUTE` on the model, its parent schema, or its parent catalog is in effect for that principal (granted directly, via group membership, or through administrative privileges).

Because access is additive, a more restrictive GRANT policy does **not** override a broader direct grant. If you rely on GRANT policies as the primary control for `EXECUTE`, you should audit existing direct grants using `SHOW GRANTS` and the effective permissions APIs. `SHOW GRANTS` does **not** reflect privileges granted by a GRANT policy, so the two sources must be inspected separately. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Prerequisite Permissions

GRANT policies do **not** grant the `USE CATALOG` and `USE SCHEMA` permissions that are required to reach a model. These must be granted directly using the standard `GRANT` statement. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

---

## Known Limitations

The following limitations apply during Beta:

| Limitation | Details |
|---|---|
| **Only `EXECUTE` on models** | No other privileges (`CREATE MODEL`, `CREATE MODEL VERSION`, `APPLY TAG`) or securable types (tables, volumes, etc.) are supported. |
| **Attachment limited to catalog/schema** | Policies cannot be attached to a model directly. |
| **`SHOW GRANTS` does not include policy grants** | You must combine `SHOW GRANTS` output with `SHOW EFFECTIVE POLICIES` to see all `EXECUTE` access. |
| **`INFORMATION_SCHEMA` excludes policies** | GRANT policies are not surfaced in Information Schema views. |
| **No direct coverage for deletions** | Deleting a model or a model version is not covered by GRANT policies; use the normal model lifecycle management interfaces. |
| **Delta Sharing incompatibility** | Models that have GRANT policies defined cannot be shared via [Delta Sharing](/concepts/delta-sharing.md). |
| **Quotas apply** | Separate quotas exist for GRANT policies, distinct from quotas for row filter and column mask policies. |
| **Compute requirement** | Creating, modifying, or dropping GRANT policies via SQL requires a classic compute cluster running **Databricks Runtime 18.3 or above**. |

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

---

## Audit Logging and Policy Queries

- **Audit logs**: Create, alter, and drop operations on GRANT policies are logged under the same `createPolicy`, `deletePolicy`, `getPolicy`, and `listPolicies` actions as row filter and column mask policies.
- **Listing policies**: Use `SHOW POLICIES` or `SHOW EFFECTIVE POLICIES` on a catalog or schema to see which GRANT policies apply. The `table` column for these policies is `NULL` because they are not table-scoped.
- **Describing a policy**: Use `DESCRIBE POLICY <policy_name> ON {CATALOG | SCHEMA} <name>` to view properties including name, securable type, principals, privileges, and the `WHEN` condition.
- **Required permission**: To view or manage a GRANT policy, you need `MANAGE` on the target catalog or schema, or ownership of that object. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

---

## Best Practices

- **Use groups in `TO`/`EXCEPT`** instead of individual users to simplify maintenance.
- **Attach at the smallest scope** possible (prefer schema over catalog) to avoid unintended tag matches.
- **Use tag inheritance** to set default values at the catalog or schema level, overridden only on specific models.
- **Avoid mixing GRANT policies and direct grants** for the same privilege on the same objects — the union behavior makes auditing difficult.
- **Grant `USE CATALOG` and `USE SCHEMA` directly**; reserve GRANT policies for `EXECUTE` only.
- **Audit existing direct grants** before introducing GRANT policies to ensure the policies provide the intended access. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

---

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Governed Tags](/concepts/governed-tags.md)
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- [MLflow Model Registry in Unity Catalog](/concepts/mlflow-model-registry-in-unity-catalog.md)
- [Databricks-hosted foundation models](/concepts/databricks-hosted-foundation-models.md)

## Sources

- [abac-grant-policies-for-models-beta-databricks-on-aws.md] (Databricks on AWS documentation)

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
