---
title: DELTA_UNSUPPORTED_CLUSTERING_COLUMN_PREDICATES error condition | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-unsupported-clustering-column-predicates-error-class
ingestedAt: "2026-06-18T08:07:45.569Z"
---

[SQLSTATE: 0A000](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-0a-feature-not-supported)

`<command>` command for Liquid tables does not support the provided predicates:

## NON\_CLUSTERING\_COLUMN[​](#non_clustering_column "Direct link to NON_CLUSTERING_COLUMN")

`<command>` predicate references non-clustering column '`<columnName>`'. Only the clustering columns may be referenced when `<command>` is run on a Liquid table: \[`<columnList>`\].

## NO\_CLUSTERING\_COLUMNS[​](#no_clustering_columns "Direct link to NO_CLUSTERING_COLUMNS")

`<command>` command is not supported on Liquid tables without clustering columns.

## UNRESOLVED\_COLUMN[​](#unresolved_column "Direct link to UNRESOLVED_COLUMN")

Fail to resolve column '`<columnName>`' in `<command>` predicate. Available clustering columns: \[`<columnList>`\].

## UNSUPPORTED\_EXPRESSION[​](#unsupported_expression "Direct link to UNSUPPORTED_EXPRESSION")

Unsupported expression: `<expression>`.
