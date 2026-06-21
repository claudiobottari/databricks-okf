---
title: Row filter and column mask policy evaluation and runtime behavior | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/policy-evaluation
ingestedAt: "2026-06-18T08:03:32.897Z"
---

note

This page describes evaluation and runtime behavior for row filter and column mask policies, which use UDFs and are enforced by the Databricks Runtime during query execution. For GRANT policies (Beta), see [ABAC GRANT policies for models (Beta)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/grant-policies).

This page explains how ABAC policies are evaluated at query time, including:

*   How conflicts between multiple policies are handled
*   How column mask type casting works
*   What safeguards prevent data exposure when tags or functions that a policy depends on are deleted

## Policy evaluation and enforcement[​](#policy-evaluation-and-enforcement "Direct link to policy-evaluation-and-enforcement")

When a user queries a table, ABAC evaluation proceeds in two stages: policy evaluation in Unity Catalog and policy enforcement in the Databricks Runtime.

Different users may see different results from the same query because policy evaluation depends on the user's identity, group memberships, and the tags on the data they access. Changes to group membership or tag assignments dynamically alter the effective policies at query time.

### Policy evaluation (Unity Catalog)[​](#policy-evaluation-unity-catalog "Direct link to policy-evaluation-unity-catalog")

Unity Catalog performs the following steps using the securable object's metadata (e.g., governed tag assignments) and the querying user's identity and group memberships:

1.  Identifies all policies whose scope covers the queried table.
2.  For each of these policies, checks whether the querying user is in the `TO` list and not in the `EXCEPT` list.
3.  For each policy, evaluates table and column conditions against the tags on the queried object, including inherited tags. Column conditions must match at least one column.
4.  If the policy applies, determines the effective row filter or column mask and sends it to the Databricks Runtime as part of the table metadata.

### Policy enforcement (Databricks Runtime)[​](#policy-enforcement-databricks-runtime "Direct link to policy-enforcement-databricks-runtime")

The Databricks Runtime query planner translates the effective row filter or column mask into secure view on top of the table scans that enforce filtering and masking during query execution. This is the same enforcement mechanism used for [table-level row filters and column masks](https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/).

## Fail-closed design[​](#fail-closed-design "Direct link to fail-closed-design")

ABAC follows a fail-closed model, where Databricks defaults to denying access if it cannot verify security. Databricks only allows access to ABAC-secured tables when it can safely enforce all applicable policies. This applies to unsupported compute versions, specific operations on the underlying table data, and situations where a policy's dependencies (tags or functions) have been removed.

### Unsupported compute versions[​](#unsupported-compute-versions "Direct link to Unsupported compute versions")

ABAC policies require Databricks Runtime 16.4 or above, or serverless compute. If a user attempts to access an ABAC-secured table from an unsupported version, the query fails closed (access is denied) to prevent unprotected data exposure.

On [dedicated access mode](https://docs.databricks.com/aws/en/compute/dedicated-overview), Databricks delegates enforcement to serverless compute to guarantee that fine-grained access controls are applied. To allow users on older runtimes to access these tables, you must explicitly exempt them from the policies.

### Unsupported operations on protected data[​](#unsupported-operations-on-protected-data "Direct link to Unsupported operations on protected data")

Certain operations are incompatible with row filters or column masks. These operations fail rather than bypass enforcement. To run them, the principal must be listed in the `EXCEPT` clause of every ABAC policy that applies to the table. Exempt principals are not subject to the policy, so Databricks does not need to enforce it and can safely allow the operation.

Operations that require the executing principal to be exempt include pipeline refreshes, backup processes, and administrative workflows such as the following:

*   Accessing ABAC-secured tables from compute running Databricks Runtime versions below 16.4
*   Time travel queries
*   Deep and shallow cloning
*   OpenSharing, where the share owner must be exempt from the policy and have the required [OpenSharing permissions](https://docs.databricks.com/aws/en/delta-sharing/). Note that the policy does not govern the recipient's access.
*   AI Search index creation and syncing

For more details on these and other limitations, see [Requirements, quotas, and limitations for row filter and column mask policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/requirements).

### Removed policy dependencies[​](#removed-policy-dependencies "Direct link to Removed policy dependencies")

ABAC policies depend on governed tags and UDFs. If any of these dependencies are removed while a policy still references them, queries against tables in the policy's scope fail.

#### Governed tag deletion[​](#governed-tag-deletion "Direct link to Governed tag deletion")

If you delete a governed tag that an ABAC policy references, all queries against the object where the policy is attached and its child objects fail with an [`INVALID_PARAMETER_VALUE.UC_ABAC_UNKNOWN_TAG_POLICY`](https://docs.databricks.com/aws/en/error-messages/invalid-parameter-value-error-class) error. This occurs even if the tag was not applied to the queried tables.

When a governed tag is deleted, it becomes an ungoverned tag. The allowed value restrictions are removed, and anyone with `APPLY TAG` can modify values without the `ASSIGN` privilege.

warning

The UI and API do not prevent deleting a governed tag that is referenced in an ABAC policy. Before deleting a governed tag, ensure that no ABAC policy references it.

To resolve the error, either restore the deleted tag, or update or delete the policy that references it. See [Create and manage governed tags](https://docs.databricks.com/aws/en/admin/governed-tags/manage-governed-tags).

#### Deleting a column that is tagged[​](#deleting-a-column-that-is-tagged "Direct link to Deleting a column that is tagged")

Databricks prevents deleting a column that has a governed tag applied. To drop the column, a user with `ASSIGN` on the tag and `APPLY TAG` on the object must first remove the tag, then the column can be deleted.

This is relevant for declarative pipelines and other automated workflows that modify table schemas. If a pipeline attempts to drop a tagged column, the operation fails. To unblock the pipeline, a user with the required tag permissions must remove the tag, run the pipeline so the schema change succeeds, and then reapply the tag to the relevant columns. If the tag is not reapplied, queries against the data will fail because the policy is still in scope but the expected tag is no longer on the object.

#### Policy-referenced function deletion[​](#policy-referenced-function-deletion "Direct link to Policy-referenced function deletion")

If a UDF referenced by a policy is deleted while the policy is still in scope, queries against tables in that scope fail with [`UC_DEPENDENCY_DOES_NOT_EXIST`](https://kb.databricks.com/delta/query-failing-with-uc_dependency_does_not_exist-in-unity-catalog). To resolve, either restore the function or update the policy to reference a different UDF.

## Rules for multiple filters and masks[​](#rules-for-multiple-filters-and-masks "Direct link to rules-for-multiple-filters-and-masks")

Only one distinct row filter can be applied at query time for a given table and user. Similarly, only one distinct column mask per column can resolve at runtime for a given column and user. This prevents ambiguous results.

If multiple distinct filters or masks apply to the same user and table (or column), Databricks blocks access and returns an error. For example:

*   **A table-level filter or mask conflicts with an ABAC policy.** A table or column that already has a [manually applied row filter or column mask](https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/manually-apply) conflicts with any ABAC-defined filter or mask on the same target.
*   **A row filter's `USING COLUMNS` clause references a `MATCH COLUMNS` alias that matches multiple columns.** The `USING COLUMNS` clause passes column values to the UDF. If a `MATCH COLUMNS` alias in the `USING COLUMNS` clause matches more than one column, the engine cannot determine which column to pass to the UDF, and the query fails with an error.
*   **A masked column is referenced in the `USING COLUMNS` clause of another policy.** If a column is masked by one policy, it cannot be used as an input argument in the `USING COLUMNS` clause of another policy.

Multiple ABAC policies can coexist for the same table or column if they result in the same effective filter or mask. For example, two policies that reference the same UDF with the same arguments resolve to the same filter or mask, and don't conflict.

### Troubleshooting policy conflicts[​](#troubleshooting-policy-conflicts "Direct link to Troubleshooting policy conflicts")

When Databricks detects multiple distinct filters or masks during policy evaluation for a given user, it throws an [`INVALID_PARAMETER_VALUE.UC_ABAC_MULTIPLE_ROW_FILTERS`](https://docs.databricks.com/aws/en/error-messages/invalid-parameter-value-error-class) or [`COLUMN_MASKS_FEATURE_NOT_SUPPORTED.MULTIPLE_MASKS`](https://docs.databricks.com/aws/en/error-messages/error-classes) error and blocks access to the table until the conflict is resolved.

To diagnose and resolve:

1.  Use [`SHOW EFFECTIVE POLICIES`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-aux-show-policies) to see all policies that apply to the table.
2.  Check [`INFORMATION_SCHEMA.ROW_FILTERS`](https://docs.databricks.com/aws/en/sql/language-manual/information-schema/row_filters) and [`INFORMATION_SCHEMA.COLUMN_MASKS`](https://docs.databricks.com/aws/en/sql/language-manual/information-schema/column_masks) to identify any table-level row filters or column masks that may conflict.
3.  Check which policies overlap in their `TO`/`EXCEPT` principals and `WHEN`/`MATCH COLUMNS` conditions.
4.  Resolve by:
    *   **Refining policy conditions.** Update `WHEN` or `MATCH COLUMNS` clauses to be more specific so distinct policies target different tables or columns.
    *   **Adjusting governed tags.** Review tag assignments on columns or tables that trigger unintended policy matches and remove or update them.
    *   **Adjusting principals.** Update `TO`/`EXCEPT` clauses so each user is covered by at most one policy per table (for row filters) or per column (for column masks).
    *   **Restructuring policies.** Consolidate overlapping policies into a single policy, or split broad policies into separate, explicitly targeted ones.

## Automatic type casting for column masks[​](#automatic-type-casting-for-column-masks "Direct link to automatic-type-casting-for-column-masks")

Databricks automatically casts both the input and output of column mask functions resolved from ABAC policies. The input column value is cast to match the mask function's parameter type, and the function output is cast to match the target column's data type. This ensures type consistency and reliable query behavior when masking columns. Automatic casting works as follows:

1.  **Masking function execution**: When policy evaluation determines that masking applies, the masking function executes on the matching column values.
2.  **Automatic type casting**: Databricks casts the input column value to match the function's parameter type, and casts the function output to match the target column's data type.
3.  **Result return**: The properly typed result is returned to the query.

If the input or output types aren't compatible, the cast fails and the query returns a runtime error. Casting follows ANSI SQL standards for `CAST` operations ([full compatibility details](https://docs.databricks.com/aws/en/sql/language-manual/functions/cast#returns)), with one addition: on Databricks Runtime 18.1 and above, ABAC column mask policies can cast structs to `VARIANT`, which isn't supported in general SQL.

You must ensure mask functions return types compatible with target columns. See [Cast-compatible masking functions](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/common-patterns#cast-compatible) for examples and the VARIANT approach for flexible masking across column types.
