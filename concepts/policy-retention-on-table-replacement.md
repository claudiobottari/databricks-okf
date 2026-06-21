---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f9c27a18880273f9d429ff1a16315d9bda75080e6a6839aeac496bc542a1f534
  pageDirectory: concepts
  sources:
    - manually-apply-row-filters-and-column-masks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - policy-retention-on-table-replacement
    - PROTR
  citations:
    - file: manually-apply-row-filters-and-column-masks-databricks-on-aws.md
title: Policy Retention on Table Replacement
description: The behavior where row filters and column masks are automatically retained when running REPLACE TABLE, preventing accidental loss of data access policies unless explicitly dropped or updated.
tags:
  - unity-catalog
  - table-management
  - data-governance
timestamp: "2026-06-19T19:30:51.852Z"
---

# Policy Retention on Table Replacement

When a table is replaced using `REPLACE TABLE` in Databricks, pre-existing row filters and column masks are automatically preserved. This retention behavior prevents accidental loss of data access policies that could otherwise occur when the table schema is redefined. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Row Filter Retention

If a row filter was applied to the original table, it is **retained regardless of schema changes**. Even if the new table definition omits the filter, the policy remains in effect. This applies whether the schema changes fundamentally or stays the same. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Column Mask Retention

A column mask is retained if the new table includes **columns with the same names** as those that had masks in the original table. If a masked column name is dropped or renamed during the replacement, the mask is not carried over. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

## Important Considerations

- **Policy preservation is automatic**: Both row filters and column masks are kept even if they are not explicitly redefined in the `REPLACE TABLE` statement. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]
- **Schema conflicts can cause failures**: If a retained policy references a column that was removed, renamed, or changed in type, subsequent queries against the replaced table may fail. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]
- **Resolution**: To resolve a policy that references a missing or altered column, update or drop the policy using `ALTER TABLE`. ^[manually-apply-row-filters-and-column-masks-databricks-on-aws.md]

This retention mechanism is designed to support data governance by ensuring that access policies are not inadvertently removed during table replacement operations.

## Related Concepts

- [Row filter](/concepts/row-filter-policies.md) – A policy that restricts which rows a user can see in a table.
- [Column mask](/concepts/column-mask-policies.md) – A policy that redacts or transforms values in a specific column.
- REPLACE TABLE – The SQL command that triggers policy retention.
- ALTER TABLE – The command used to modify or remove retained policies.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that manages row filters and column masks.
- Access control – The broader concept of data security policies.

## Sources

- manually-apply-row-filters-and-column-masks-databricks-on-aws.md

# Citations

1. [manually-apply-row-filters-and-column-masks-databricks-on-aws.md](/references/manually-apply-row-filters-and-column-masks-databricks-on-aws-b311d10e.md)
