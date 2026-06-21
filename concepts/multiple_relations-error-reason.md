---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 466ae2a6d935fac7049c33a7824b402b085d272a68d0038b538c70f04892bb8a
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multiple_relations-error-reason
    - MER
    - MULTIPLE_RELATIONS restriction
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: MULTIPLE_RELATIONS error reason
description: A sub-reason of DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED indicating the view references more than one relation.
tags:
  - databricks
  - error-messages
  - views
timestamp: "2026-06-18T15:26:09.719Z"
---

---
title: MULTIPLE_RELATIONS error reason
summary: An error that occurs when using `table_changes` on a view that references more than one relation, preventing change tracking.
sources:
  - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - delta-lake
  - error
  - troubleshooting
aliases:
  - multiple-relations-error-reason
  - MULTIPLE_RELATIONS
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 2
---

# MULTIPLE_RELATIONS error reason

The **MULTIPLE_RELATIONS** error reason is part of the DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error class. It occurs when you attempt to use the `table_changes` function on a view that references more than one base relation (for example, a view built from a join or union of multiple tables).

## Error message

When the error is raised, the condition message reads:

```
MULTIPLE_RELATIONS: The view references more than one relation.
```

^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Cause

The `table_changes` function in [Delta Lake](/concepts/delta-lake.md) can only track changes on a single Delta table. If the view you pass as an argument is defined by a query that joins, unions, or otherwise combines multiple tables, the function cannot resolve change tracking because it does not know which underlying table's change feed to follow. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

The view must reference **exactly one** relation (a specific Delta table) to be eligible for change data capture via `table_changes`. Views that perform aggregations, joins, or references to more than one table will trigger this error.

## How to resolve

To use `table_changes`, ensure that the input is either:

- The name of a single Delta table, or
- A view that directly selects from exactly one Delta table without combining other relations.

If you need to consume changes from multiple tables, consider calling `table_changes` separately for each table and then combining the results in a downstream process.

## Related concepts

- DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error class
- table_changes function
- [Delta Lake change data feed](/concepts/delta-lake-change-data-feed-cdf.md)
- View structural constraints for table_changes|View limitations for table_changes
- ERROR_CLASS error handling

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)
