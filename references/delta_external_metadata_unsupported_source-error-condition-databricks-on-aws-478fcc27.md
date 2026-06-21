---
title: DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE error condition | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-external-metadata-unsupported-source-error-class
ingestedAt: "2026-06-18T08:07:20.885Z"
---

[SQLSTATE: 0AKDC](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-0a-feature-not-supported)

External Metadata doesn't support source:

## COLUMN\_MASK[​](#column_mask "Direct link to COLUMN_MASK")

`<tableType>` with Column Mask (CM) policies.

## COLUMN\_RENAME\_WITHOUT\_COLUMN\_MAPPING[​](#column_rename_without_column_mapping "Direct link to COLUMN_RENAME_WITHOUT_COLUMN_MAPPING")

Column mapping must be enabled to use an alias in the reconciliation query.

## PROJECTION\_NOT\_SUPPORTED[​](#projection_not_supported "Direct link to PROJECTION_NOT_SUPPORTED")

The projection '`<projectionSql>`' of reconciliation query is not supported.

## ROW\_FILTER[​](#row_filter "Direct link to ROW_FILTER")

`<tableType>` with Row-level Security (RLS) policies.

## TABLE\_TYPE[​](#table_type "Direct link to TABLE_TYPE")

`<tableType>` table, only streaming table and materialized view are supported.
