---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c5058a8b2d36bc562f4c07d3b30ac5175dc998e6c1f8cf6f6aa6ab960560efe6
  pageDirectory: concepts
  sources:
    - row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policy-evaluation-and-enforcement
    - Enforcement and ABAC Policy Evaluation
    - APEAE
    - Policy Evaluation and Enforcement
    - Policy Evaluation Order in ABAC
  citations:
    - file: row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md
title: ABAC Policy Evaluation and Enforcement
description: Two-stage process where Unity Catalog evaluates which policies apply based on user identity and tags, then Databricks Runtime enforces row filters and column masks during query execution.
tags:
  - unity-catalog
  - abac
  - policy-evaluation
  - databricks-runtime
timestamp: "2026-06-19T20:15:59.022Z"
---

## ABAC Policy Evaluation and Enforcement

**ABAC Policy Evaluation and Enforcement** describes how Databricks attribute-based access control (ABAC) policies for row filters and column masks are assessed and applied at query time. The process involves two distinct stages: evaluation within Unity Catalog and enforcement by the Databricks Runtime. Because policy outcomes depend on the user’s identity, group membership, and the governed tags attached to the data, different users may see different results from the same query. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

### Policy Evaluation (Unity Catalog)

When a user queries a table, Unity Catalog performs the following steps using the securable object’s metadata (including governed tag assignments) and the querying user’s identity and group memberships:  

1. Identifies all policies whose scope covers the queried table.  
2. For each policy, checks whether the user is in the `TO` list and not in the `EXCEPT` list.  
3. Evaluates table and column conditions against the tags on the queried object (including inherited tags); column conditions must match at least one column.  
4. If a policy applies, determines the effective row filter or column mask and sends it to the Databricks Runtime as part of the table metadata. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

### Policy Enforcement (Databricks Runtime)

The Databricks Runtime query planner translates the effective row filter or column mask into a secure view on top of table scans. This view enforces filtering and masking during query execution using the same mechanism used for table-level [Row Filter](/concepts/row-filter-policies.md)s and Column Masks. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

### Fail-Closed Design

ABAC follows a fail‑closed model: Databricks denies access if it cannot verify that all applicable policies can be enforced. The system only allows access when safe enforcement is possible. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

#### Unsupported Compute Versions

ABAC policies require Databricks Runtime 16.4 or above, or serverless compute. Queries against an ABAC‑secured table from an unsupported version fail closed (access denied) to prevent unprotected data exposure. On dedicated access mode, Databricks delegates enforcement to serverless compute to guarantee fine‑grained controls. Users on older runtimes must be explicitly exempted from all applicable policies to access such tables. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

#### Unsupported Operations on Protected Data

Certain operations are incompatible with row filters or column masks and fail rather than bypass enforcement. To run these operations, the principal must be listed in the `EXCEPT` clause of every ABAC policy that applies to the table. Exempt principals are not subject to the policy, so Databricks can safely allow the operation without enforcing it. Affected operations include: accessing ABAC‑secured tables from unsupported Databricks Runtime versions, time travel queries, deep and shallow cloning, OpenSharing (the share owner must be exempt and have required OpenSharing permissions), and AI Search index creation and syncing. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

#### Removed Policy Dependencies

ABAC policies depend on governed tags and user‑defined functions (UDFs). If any dependency is removed while a policy still references it, queries against tables in the policy’s scope fail.

* **Governed tag deletion:** Deleting a governed tag that an ABAC policy references causes all queries against the object and its children to fail with an `INVALID_PARAMETER_VALUE.UC_ABAC_UNKNOWN_TAG_POLICY` error, even if the tag was not applied to the queried tables. The UI and API do not prevent such deletion; users must ensure no policy references a tag before deleting it. To resolve, restore the deleted tag or update/delete the policy.  
* **Deleting a tagged column:** Databricks prevents dropping a column that has a governed tag applied. A user with `ASSIGN` on the tag and `APPLY TAG` on the object must first remove the tag before the column can be dropped. Automated pipelines that attempt to drop such a column fail until the tag is removed.  
* **Policy-referenced function deletion:** If a UDF referenced by a policy is deleted, queries against tables in that scope fail with `UC_DEPENDENCY_DOES_NOT_EXIST`. To resolve, restore the function or update the policy to use a different UDF. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

### Rules for Multiple Filters and Masks

Only one distinct row filter can apply at query time for a given table and user; similarly, only one distinct column mask per column can resolve at runtime. If multiple distinct filters or masks would apply, Databricks blocks access and returns an error. Conflicts arise, for example, when a table‑level filter or mask overlaps with an ABAC policy, when a `USING COLUMNS` clause references a `MATCH COLUMNS` alias that matches multiple columns, or when a masked column appears in another policy’s `USING COLUMNS` clause.

Multiple ABAC policies can coexist for the same table or column if they produce the same effective filter or mask (e.g., two policies referencing the same UDF with identical arguments). When conflicts are detected, Databricks throws an `INVALID_PARAMETER_VALUE.UC_ABAC_MULTIPLE_ROW_FILTERS` or `COLUMN_MASKS_FEATURE_NOT_SUPPORTED.MULTIPLE_MASKS` error and blocks access until the conflict is resolved. To diagnose, use `SHOW EFFECTIVE POLICIES` and check `INFORMATION_SCHEMA.ROW_FILTERS` and `INFORMATION_SCHEMA.COLUMN_MASKS`. Resolutions include refining policy conditions, adjusting governed tags, modifying `TO`/`EXCEPT` clauses, or restructuring overlapping policies. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

### Automatic Type Casting for Column Masks

Databricks automatically casts both the input and output of column mask functions resolved from ABAC policies. The input column value is cast to match the mask function’s parameter type, and the function’s output is cast to match the target column’s data type. This ensures type consistency and reliable query behavior. If the types are not compatible, the cast fails and a runtime error is returned. Casting follows ANSI SQL standards for `CAST` operations, with one addition: on Databricks Runtime 18.1 and above, ABAC column mask policies can cast structs to `VARIANT`, which is not supported in general SQL. Mask functions must return types compatible with target columns. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

### Related Concepts

- [Row Filter](/concepts/row-filter-policies.md) – Table‑level filtering applied by the Databricks Runtime.
- Column Mask – Column‑level masking applied during query execution.
- [Unity Catalog](/concepts/unity-catalog.md) – The catalog that evaluates ABAC policies.
- Databricks Runtime – The execution engine that enforces policies.
- [ABAC GRANT Policies](/concepts/abac-grant-policies.md) – A separate (Beta) ABAC mechanism for model access.
- [Governed Tags](/concepts/governed-tags.md) – Tags that are used in policy conditions and must not be removed while referenced.
- UDF – User‑defined functions that implement the filter or mask logic.
- [OpenSharing](/concepts/opensharing.md) – Delta Sharing integration with ABAC.
- [SHOW EFFECTIVE POLICIES](/concepts/show-effective-policies.md) – SQL command to diagnose applied policies.

### Sources

- row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md

# Citations

1. [row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md](/references/row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws-2d8da254.md)
