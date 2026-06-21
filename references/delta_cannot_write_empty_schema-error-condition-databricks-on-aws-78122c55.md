---
title: DELTA_CANNOT_WRITE_EMPTY_SCHEMA error condition | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-cannot-write-empty-schema-error-class
ingestedAt: "2026-06-18T08:07:04.807Z"
---

*   [](https://docs.databricks.com/aws/en/)
*   [Error messages](https://docs.databricks.com/aws/en/error-messages/)
*   [Error classes in Databricks](https://docs.databricks.com/aws/en/error-messages/error-classes)
*   DELTA\_CANNOT\_WRITE\_EMPTY\_SCHEMA error condition

Last updated on **Apr 13, 2026**

[SQLSTATE: 428GU](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-42-syntax-error-or-access-rule-violation)

The Delta table is not writable because parts of the schema are not supported. Reason:

## STRUCT\_ALL\_VOID\_FIELDS[​](#struct_all_void_fields "Direct link to STRUCT_ALL_VOID_FIELDS")

The column `<columnPath>` is a struct where all fields have VOID type.

## STRUCT\_NO\_FIELDS[​](#struct_no_fields "Direct link to STRUCT_NO_FIELDS")

The column `<columnPath>` is a struct with no fields.

## TABLE\_ALL\_VOID\_COLUMNS[​](#table_all_void_columns "Direct link to TABLE_ALL_VOID_COLUMNS")

All columns in the table schema have VOID type.

## TABLE\_NO\_COLUMNS[​](#table_no_columns "Direct link to TABLE_NO_COLUMNS")

The table schema has no columns defined.
