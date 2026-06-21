---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c82d1016d9233ef8242e69c9e1c096815055611d0354c53018ec5a643db7a44c
  pageDirectory: concepts
  sources:
    - row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policy-dependency-lifecycle-management
    - APDLM
  citations:
    - file: row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md
title: ABAC Policy Dependency Lifecycle Management
description: Handling of removed policy dependencies (governed tags, UDFs, tagged columns) including error codes, fail-closed behavior, and resolution steps required when dependencies are deleted while policies still reference them.
tags:
  - abac
  - dependency-management
  - governed-tags
  - udf
timestamp: "2026-06-19T20:16:10.665Z"
---

```yaml
---
title: ABAC Policy Dependency Lifecycle Management
summary: How ABAC policies depend on governed tags and UDFs, and what happens when those dependencies are removed, including the fail‑closed behavior and resolution steps.
sources:
  - row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T18:30:00.000Z"
updatedAt: "2026-06-19T18:30:00.000Z"
tags:
  - ABAC
  - Dependency
  - Lifecycle
  - Fail-Closed
  - Governed Tags
  - UDF
  - Row Filter
  - Column Mask
aliases:
  - ABAC dependency removal
  - ABAC policy dependency deletion
  - ABAC fail-closed dependency
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# ABAC Policy Dependency Lifecycle Management

**ABAC Policy Dependency Lifecycle Management** describes how [[Attribute-Based Access Control (ABAC)|Attribute‑Based Access Control (ABAC)]] policies in Unity Catalog depend on external objects — governed tags and user‑defined functions (UDFs) — and what occurs when those dependencies are deleted or become unavailable. Databricks uses a fail‑closed model: if any dependency is missing, access to tables in the policy’s scope is denied until the dependency is restored or the policy is updated. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Dependencies of an ABAC Policy

ABAC policies rely on two types of resources:

- **Governed tags** – The `WHEN` and `MATCH COLUMNS` clauses of a policy reference governed tags. Tag assignments on tables or columns determine whether a policy applies.
- **User‑defined functions (UDFs)** – Row filter and column mask policies use UDFs to define the filtering or masking logic. The policy references a specific UDF stored in Unity Catalog.

^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Behavior When a Dependency Is Removed

The system does not prevent deletion of a governed tag even if an ABAC policy references it. Similarly, a UDF can be dropped while a policy still refers to it. In both cases, queries against tables in the policy’s scope fail closed – access is denied – and an error is returned. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

### Governed Tag Deletion

If a governed tag that an ABAC policy references is deleted, all queries against the object where the policy is attached (and its child objects) fail with an `INVALID_PARAMETER_VALUE.UC_ABAC_UNKNOWN_TAG_POLICY` error. This occurs even if the tag was not applied to the queried table. After deletion, the tag becomes an ungoverned tag: allowed value restrictions are removed, and any user with `APPLY TAG` can modify values without the `ASSIGN` privilege. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

> **Warning:** The UI and API do not block deleting a governed tag that is referenced in an ABAC policy. Before deletion, ensure no ABAC policy references the tag.

To resolve the error, either restore the deleted tag, or update or delete the policy that references it. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

### Deleting a Column That Is Tagged

Databricks prevents dropping a column that has a governed tag applied. To remove the column, a user with `ASSIGN` on the tag and `APPLY TAG` on the object must first remove the tag, then drop the column. This is especially relevant for declarative pipelines or automated workflows that modify schemas: if a pipeline attempts to drop a tagged column, the operation fails. The workaround is to temporarily remove the tag, run the pipeline to apply the schema change, and reapply the tag to the relevant columns. If the tag is not reapplied, queries will fail because the policy still expects the tag on the object. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

### UDF Deletion

If a UDF referenced by a policy is deleted while the policy is still in scope, queries against tables in that scope fail with a `UC_DEPENDENCY_DOES_NOT_EXIST` error. To resolve, either restore the function or update the policy to reference a different UDF. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Fail‑Closed Behavior Across the Lifecycle

The fail‑closed design extends beyond dependency deletions. Databricks also denies access when:

- The compute version is below Databricks Runtime 16.4 (or is not serverless compute).
- An unsupported operation (e.g., time travel, deep clone, Delta Sharing, AI Search index sync) is attempted on an ABAC‑secured table.

In all cases, access is blocked until the condition is resolved or the principal is listed in the `EXCEPT` clause of every applicable policy. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Policy Evaluation and Enforcement

ABAC policy evaluation occurs in two stages:

1. **Unity Catalog** evaluates the policy against the user’s identity, group memberships, and tag assignments, and resolves the effective row filter or column mask.
2. **Databricks Runtime** enforces the filter or mask by rewriting queries with a secure view over the table scans.

Changes to group membership, tag assignments, or the existence of dependencies dynamically alter the effective policy at query time. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Related Concepts

- [[Governed Tags]] – The tag type that ABAC policies depend on; deletion triggers fail‑closed errors.
- [[Row Filter Policies|Row Filter]] – A table‑level UDF that filters rows based on policy conditions.
- Column Mask – A column‑level UDF that masks cell values.
- [[Row Filter and Column Mask Policies|Row Filter and Column Mask Policy Evaluation and Runtime Behavior]] – Full details on evaluation stages and conflict rules.
- [[SHOW EFFECTIVE POLICIES]] – Command to inspect which policies apply to a table.
- INFORMATION_SCHEMA.ROW_FILTERS and INFORMATION_SCHEMA.COLUMN_MASKS – System views for identifying manually applied filters or masks that may conflict with ABAC policies.
- Fail-Closed Design – The security principle used by ABAC.

## Sources

- row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md
```

# Citations

1. [row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md](/references/row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws-2d8da254.md)
