---
title: DELTA_DUPLICATE_COLUMNS_FOUND error condition | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-duplicate-columns-found-error-class
ingestedAt: "2026-06-18T08:07:19.109Z"
---

[SQLSTATE: 42711](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-42-syntax-error-or-access-rule-violation)

Found duplicate column(s): `<duplicateCols>`.

## ADDING\_COLUMNS[​](#adding_columns "Direct link to ADDING_COLUMNS")

The duplicate was found while adding columns.

## CLUSTER\_BY[​](#cluster_by "Direct link to CLUSTER_BY")

The duplicate was found in `CLUSTER BY`.

## CONVERT\_TO\_DELTA[​](#convert_to_delta "Direct link to CONVERT_TO_DELTA")

The duplicate was found during conversion to Delta.

## DATA[​](#data "Direct link to DATA")

The duplicate was found in the data being saved.

## EXISTING\_SCHEMA[​](#existing_schema "Direct link to EXISTING_SCHEMA")

The duplicate was found in the existing table schema.

The duplicate was found in the metadata update.

## PARTITION\_COLUMNS[​](#partition_columns "Direct link to PARTITION_COLUMNS")

The duplicate was found in the partition columns.

## PARTITION\_SCHEMA[​](#partition_schema "Direct link to PARTITION_SCHEMA")

The duplicate was found in the partition schema.

## READ\_SCHEMA[​](#read_schema "Direct link to READ_SCHEMA")

The duplicate was found in the schema of the data being read.

## REPLACING\_COLUMNS[​](#replacing_columns "Direct link to REPLACING_COLUMNS")

The duplicate was found while replacing columns.

## SPECIFIED\_COLUMNS[​](#specified_columns "Direct link to SPECIFIED_COLUMNS")

The duplicate was found in the specified columns.

## TABLE\_SCHEMA[​](#table_schema "Direct link to TABLE_SCHEMA")

The duplicate was found in the table schema.
