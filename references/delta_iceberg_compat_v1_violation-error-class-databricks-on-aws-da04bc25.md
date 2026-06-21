---
title: DELTA_ICEBERG_COMPAT_V1_VIOLATION error class | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-iceberg-compat-v1-violation-error-class
ingestedAt: "2026-06-18T08:07:22.617Z"
---

[SQLSTATE: KD00E](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-kd-datasource-specific-errors)

The validation of IcebergCompatV1 has failed.

## DISABLING\_REQUIRED\_TABLE\_FEATURE[​](#disabling_required_table_feature "Direct link to DISABLING_REQUIRED_TABLE_FEATURE")

IcebergCompatV1 requires feature `<feature>` to be supported and enabled. You cannot drop it from the table. Instead, please disable IcebergCompatV1 first.

## INCOMPATIBLE\_TABLE\_FEATURE[​](#incompatible_table_feature "Direct link to INCOMPATIBLE_TABLE_FEATURE")

IcebergCompatV1 is incompatible with feature `<feature>`.

## MISSING\_REQUIRED\_TABLE\_FEATURE[​](#missing_required_table_feature "Direct link to MISSING_REQUIRED_TABLE_FEATURE")

IcebergCompatV1 requires feature `<feature>` to be supported and enabled.

## REPLACE\_TABLE\_CHANGE\_PARTITION\_NAMES[​](#replace_table_change_partition_names "Direct link to REPLACE_TABLE_CHANGE_PARTITION_NAMES")

IcebergCompatV1 doesn't support replacing partitioned tables with a differently-named partition spec, because Iceberg-Spark 1.1.0 doesn't.

Prev Partition Spec: `<prevPartitionSpec>`

New Partition Spec: `<newPartitionSpec>`

## UNSUPPORTED\_DATA\_TYPE[​](#unsupported_data_type "Direct link to UNSUPPORTED_DATA_TYPE")

IcebergCompatV1 doesn't support schema with MapType or ArrayType or NullType. Your schema:

`<schema>`

## WRONG\_REQUIRED\_TABLE\_PROPERTY[​](#wrong_required_table_property "Direct link to WRONG_REQUIRED_TABLE_PROPERTY")

IcebergCompatV1 requires table property '`<key>`' to be set to '`<requiredValue>`'. Current value: '`<actualValue>`'.
