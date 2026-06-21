---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0761e95622c953d8ca2eee83760e9fea3525ade503eff31ce1b611dfd83576e4
  pageDirectory: concepts
  sources:
    - row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multiple-row-filter-and-column-mask-conflict-resolution
    - Column Mask Conflict Resolution and Multiple Row Filter
    - MRFACMCR
  citations:
    - file: row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md
title: Multiple Row Filter and Column Mask Conflict Resolution
description: Rules ensuring only one distinct row filter per table and one distinct column mask per column can apply at runtime; conflicts block access and require diagnosis via SHOW EFFECTIVE POLICIES and INFORMATION_SCHEMA views.
tags:
  - abac
  - row-filters
  - column-masks
  - conflict-resolution
timestamp: "2026-06-19T20:16:02.594Z"
---

# Multiple Row Filter and Column Mask Conflict Resolution

**Multiple Row Filter and Column Mask Conflict Resolution** refers to the mechanisms and rules that Databricks uses to handle situations where multiple access control policies could apply to the same table, row filter, or column mask for a given user. Databricks enforces a strict one-policy-per-target rule to prevent ambiguous or conflicting data access outcomes.

## Conflict Rules

Only one distinct row filter can be applied at query time for a given table and user. Similarly, only one distinct column mask per column can resolve at runtime for a given column and user. If multiple distinct filters or masks apply to the same user and table (or column), Databricks blocks access and returns an error. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

### Conflict Scenarios

Conflicts arise in several specific situations:

- **A table-level filter or mask conflicts with an ABAC policy.** A table or column that already has a [manually applied row filter or column mask](https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/manually-apply) conflicts with any ABAC-defined filter or mask on the same target. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

- **A row filter's `USING COLUMNS` clause references a `MATCH COLUMNS` alias that matches multiple columns.** The `USING COLUMNS` clause passes column values to the UDF. If a `MATCH COLUMNS` alias matches more than one column, the engine cannot determine which column to pass to the UDF, and the query fails with an error. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

- **A masked column is referenced in the `USING COLUMNS` clause of another policy.** If a column is masked by one policy, it cannot be used as an input argument in the `USING COLUMNS` clause of another policy. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

### Permitted Coexistence

Multiple ABAC policies can coexist for the same table or column if they result in the same effective filter or mask. For example, two policies that reference the same UDF with the same arguments resolve to the same filter or mask and do not conflict. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Error Handling

When Databricks detects multiple distinct filters or masks during policy evaluation for a given user, it throws an [`INVALID_PARAMETER_VALUE.UC_ABAC_MULTIPLE_ROW_FILTERS`](https://docs.databricks.com/aws/en/error-messages/invalid-parameter-value-error-class) or [`COLUMN_MASKS_FEATURE_NOT_SUPPORTED.MULTIPLE_MASKS`](https://docs.databricks.com/aws/en/error-messages/error-classes) error and blocks access to the table until the conflict is resolved. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Troubleshooting Policy Conflicts

To diagnose and resolve policy conflicts:

1. **Use [`SHOW EFFECTIVE POLICIES`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-aux-show-policies)** to see all policies that apply to the table. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

2. **Check [`INFORMATION_SCHEMA.ROW_FILTERS`](https://docs.databricks.com/aws/en/sql/language-manual/information-schema/row_filters) and [`INFORMATION_SCHEMA.COLUMN_MASKS`](https://docs.databricks.com/aws/en/sql/language-manual/information-schema/column_masks)** to identify any table-level row filters or column masks that may conflict. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

3. **Check which policies overlap** in their `TO`/`EXCEPT` principals and `WHEN`/`MATCH COLUMNS` conditions. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

### Resolution Strategies

Resolve conflicts using one or more of the following approaches:

- **Refining policy conditions.** Update `WHEN` or `MATCH COLUMNS` clauses to be more specific so distinct policies target different tables or columns. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

- **Adjusting governed tags.** Review tag assignments on columns or tables that trigger unintended policy matches and remove or update them. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

- **Adjusting principals.** Update `TO`/`EXCEPT` clauses so each user is covered by at most one policy per table (for row filters) or per column (for column masks). ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

- **Restructuring policies.** Consolidate overlapping policies into a single policy, or split broad policies into separate, explicitly targeted ones. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Policy Evaluation Process

Understanding the conflict resolution rules requires familiarity with the underlying policy evaluation process. When a user queries a table, Unity Catalog identifies all policies whose scope covers the queried table, checks whether the querying user is in the `TO` list and not in the `EXCEPT` list, evaluates table and column conditions against tags, and determines the effective row filter or column mask. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

Different users may see different results from the same query because policy evaluation depends on the user's identity, group memberships, and the tags on the data they access. Changes to group membership or tag assignments dynamically alter the effective policies at query time. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Related Concepts

- [Row Filter Policy](/concepts/abac-row-filter-policy.md) — An ABAC policy that filters rows based on user identity and tags.
- [Column Mask Policy](/concepts/column-mask-policies.md) — An ABAC policy that masks column values based on user identity and tags.
- [ABAC Policy Evaluation](/concepts/dynamic-abac-policy-evaluation.md) — The process by which Unity Catalog determines effective policies for a query.
- [Governed Tags](/concepts/governed-tags.md) — Tags used by ABAC policies to determine access conditions.
- Fail-Closed Design — The security model where access is denied unless enforcement is confirmed.

## Sources

- row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md

# Citations

1. [row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md](/references/row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws-2d8da254.md)
