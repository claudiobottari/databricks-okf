---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2b90e0e72a94fe5546796971df313f1ad66d61d95f91c5f68202bf156e891fe8
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multiple_relations-constraint-for-table_changes
    - MCFT
    - MULTIPLE_RELATIONS constraint for table_changes
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: MULTIPLE_RELATIONS constraint for table_changes
description: A validation rule requiring that views used with table_changes reference exactly one relation (table or view), not multiple
tags:
  - databricks
  - validation
  - view-constraints
timestamp: "2026-06-19T15:07:33.790Z"
---

# MULTIPLE_RELATIONS Constraint for `table_changes`

The **MULTIPLE_RELATIONS** constraint is a sub‑condition of the DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error class|DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED|DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error class (SQLSTATE 0AKDC). It is raised when the table_changes function is called on a view that references more than one base relation. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Cause

The `table_changes` function expects the input to be a single Delta table. If the view passed to the function is defined by a query that joins or unions multiple tables — i.e., references more than one relation — the system cannot determine which table’s changes to track, and the `MULTIPLE_RELATIONS` constraint is triggered. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Context

The `MULTIPLE_RELATIONS` constraint is one of several possible reasons for the DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error|DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error condition. Other related sub‑conditions include:

- NON_DETERMINISTIC_EXPRESSIONS constraint for table_changes|NON_DETERMINISTIC_EXPRESSIONS constraint for table_changes|NON_DETERMINISTIC_EXPRESSIONS — the view contains non‑deterministic expressions.
- NOT_DELTA_TABLE constraint for table_changes|NOT_DELTA_TABLE constraint for table_changes|NOT_DELTA_TABLE — the view does not reference a Delta table at all.
- NOT_SHARED_VIEW constraint for table_changes|NOT_SHARED_VIEW — the view is not an [OpenSharing view](/concepts/opensharing-views.md).
- SUBQUERY constraint for table_changes|SUBQUERY constraint for table_changes|SUBQUERY — the view contains a sub‑query.
- UNSUPPORTED_OPERATOR constraint for table_changes|UNSUPPORTED_OPERATOR constraint for table_changes|UNSUPPORTED_OPERATOR — the view uses an operator that is not allowed.

^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Resolution

To use `table_changes`, ensure that the view references exactly one Delta table. If the view is defined with a multi‑table query, rewrite it to refer to a single table, or call `table_changes` directly on the Delta table instead of on the view. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

## Related Concepts

- table_changes function — the function that tracks row-level changes on Delta tables.
- [Delta table](/concepts/delta-lake-table.md) — the underlying storage format that supports change tracking.
- View — a logical table defined by a saved query.
- [OpenSharing view](/concepts/opensharing-views.md) — a view shared through Delta Sharing that is subject to specific constraints.
- DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED error class — the parent error class with multiple sub‑conditions.

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)
