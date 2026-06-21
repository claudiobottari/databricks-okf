---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f5922ea8d285191062437817f2d87b117804212c297347b9ae71225132b4e89e
  pageDirectory: concepts
  sources:
    - describe-history-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - temporal-specification-restriction-on-describe-history
    - TSRODH
    - Temporal Specification|temporal specification
    - temporal specification or options specification
  citations:
    - file: describe-history-databricks-on-aws.md
title: Temporal Specification Restriction on DESCRIBE HISTORY
description: The DESCRIBE HISTORY command does not accept temporal or options specifications in the table name parameter.
tags:
  - delta-lake
  - sql
  - syntax
timestamp: "2026-06-19T10:12:27.749Z"
---

# Temporal Specification Restriction on DESCRIBE HISTORY

The **`DESCRIBE HISTORY`** command in Databricks SQL returns provenance information about writes to a [Delta table](/concepts/delta-lake-table.md), including the operation, user, and timestamp for each write. Table history is retained for 30 days. ^[describe-history-databricks-on-aws.md]

## Syntax

```sql
DESCRIBE HISTORY table_name
```

^[describe-history-databricks-on-aws.md]

## Restriction

When using `DESCRIBE HISTORY`, the `table_name` must not include a temporal specification or options specification. ^[describe-history-databricks-on-aws.md]

This means you cannot use time-travel syntax such as `TIMESTAMP AS OF` or `VERSION AS OF` when describing a table's history. The table name must be a plain identifier without any temporal or options qualifiers.

## Invalid Examples

The following queries are not valid and will produce an error:

```sql
-- Invalid: temporal specification not allowed
DESCRIBE HISTORY my_table TIMESTAMP AS OF '2025-01-01';

-- Invalid: temporal specification not allowed
DESCRIBE HISTORY my_table VERSION AS OF 5;
```

## Reason for the Restriction

`DESCRIBE HISTORY` returns information about all writes to a table over the retention period, not the state of the table at a specific point in time. Since the command covers the full write history rather than querying table contents at a past moment, a temporal specification would be logically inconsistent with the command's purpose. ^[describe-history-databricks-on-aws.md]

## Related Concepts

- Delta table history — How table history works, including the 30-day retention period
- Temporal specification — Time-travel syntax for querying table snapshots
- DESCRIBE DETAIL — Another DESCRIBE command for Delta tables
- table_changes function — An alternative way to retrieve change data over time
- Time travel in Delta Lake — General concepts around querying historical table states

## Sources

- describe-history-databricks-on-aws.md

# Citations

1. [describe-history-databricks-on-aws.md](/references/describe-history-databricks-on-aws-c4aeec74.md)
