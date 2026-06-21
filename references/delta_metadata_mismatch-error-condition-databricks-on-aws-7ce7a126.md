---
title: DELTA_METADATA_MISMATCH error condition | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-metadata-mismatch-error-class
ingestedAt: "2026-06-18T08:07:27.979Z"
---

[SQLSTATE: 42KDG](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-42-syntax-error-or-access-rule-violation)

A metadata mismatch was detected when writing to the Delta table.

## ACL\_ENABLED[​](#acl_enabled "Direct link to ACL_ENABLED")

Table ACLs are enabled in this cluster, so automatic schema migration is not allowed. Please use the `ALTER TABLE` command for changing the schema.

## ENABLE\_LIQUID[​](#enable_liquid "Direct link to ENABLE_LIQUID")

To enable clustering on the existing table, please use "overwrite" mode and set: '.option("overwriteSchema", "true")'.

## OVERWRITE\_REQUIRED[​](#overwrite_required "Direct link to OVERWRITE_REQUIRED")

To overwrite your schema or change partitioning, please set: '.option("overwriteSchema", "true")'.

Note that the schema can't be overwritten when using 'replaceWhere'.

## PARTITIONING\_MISMATCH[​](#partitioning_mismatch "Direct link to PARTITIONING_MISMATCH")

Partition columns do not match the partition columns of the table.

Given: `<provided>`

Table: `<original>`

## SCHEMA\_MISMATCH[​](#schema_mismatch "Direct link to SCHEMA_MISMATCH")

A schema mismatch detected when writing to the Delta table (Table ID: `<id>`).

To enable schema migration using DataFrameWriter or DataStreamWriter, please set: '.option("mergeSchema", "true")'.

For other operations, set the session configuration spark.databricks.delta.schema.autoMerge.enabled to "true". See the documentation specific to the operation for details.

Table schema:

`<tableSchema>`

Data schema:

`<dataSchema>`
