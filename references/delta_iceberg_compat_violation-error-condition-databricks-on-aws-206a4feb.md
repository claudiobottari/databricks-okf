---
title: DELTA_ICEBERG_COMPAT_VIOLATION error condition | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-iceberg-compat-violation-error-class
ingestedAt: "2026-06-18T08:07:24.485Z"
---

[SQLSTATE: KD00E](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-kd-datasource-specific-errors)

The validation of IcebergCompatV`<version>` has failed.

## CHANGE\_VERSION\_NEED\_REWRITE[​](#change_version_need_rewrite "Direct link to CHANGE_VERSION_NEED_REWRITE")

Changing to IcebergCompatV`<newVersion>` requires rewriting the table. Please run `REORG TABLE APPLY (UPGRADE UNIFORM` ('`ICEBERG_COMPAT_VERSION = <newVersion>`'));

Note that `REORG` enables table feature IcebergCompatV`<newVersion>` and other Databricks runtime versions without that table feature support may not be able to write to the table.

## COMPAT\_VERSION\_NOT\_SUPPORTED[​](#compat_version_not_supported "Direct link to COMPAT_VERSION_NOT_SUPPORTED")

IcebergCompatVersion = `<version>` is not supported. Supported versions are between 1 and `<maxVersion>`.

## CONFIG\_NOT\_ENABLED[​](#config_not_enabled "Direct link to CONFIG_NOT_ENABLED")

IcebergCompatV`<version>` is not enabled in this environment.

## DELETION\_VECTORS\_NOT\_PURGED[​](#deletion_vectors_not_purged "Direct link to DELETION_VECTORS_NOT_PURGED")

IcebergCompatV`<version>` requires Deletion Vectors to be completely purged from the table. Please run the `REORG TABLE APPLY (PURGE)` command.

## DELETION\_VECTORS\_SHOULD\_BE\_DISABLED[​](#deletion_vectors_should_be_disabled "Direct link to DELETION_VECTORS_SHOULD_BE_DISABLED")

IcebergCompatV`<version>` requires Deletion Vectors to be disabled on the table first. Then run `REORG PURGE` command to purge the Deletion Vectors on the table.

## DISABLING\_REQUIRED\_TABLE\_FEATURE[​](#disabling_required_table_feature "Direct link to DISABLING_REQUIRED_TABLE_FEATURE")

IcebergCompatV`<version>` requires feature `<feature>` to be supported and enabled. You cannot drop it from the table. Instead, please disable IcebergCompatV`<version>` first.

## FILES\_NOT\_ICEBERG\_COMPAT[​](#files_not_iceberg_compat "Direct link to FILES_NOT_ICEBERG_COMPAT")

Enabling Uniform Apache Iceberg with IcebergCompatV`<version>` requires all files to be Apache Iceberg compatible.

There are `<addFilesCount>` files in table version `<tableVersion>` and `<addFilesWithoutTag>` files are not Apache Iceberg compatible, which is usually a result of concurrent write.

Please run the `REORG TABLE` table `APPLY (UPGRADE UNIFORM (ICEBERG_COMPAT_VERSION=<version>)` command again.

## INCOMPATIBLE\_TABLE\_FEATURE[​](#incompatible_table_feature "Direct link to INCOMPATIBLE_TABLE_FEATURE")

IcebergCompatV`<version>` is incompatible with feature `<feature>`.

## MISSING\_REQUIRED\_TABLE\_FEATURE[​](#missing_required_table_feature "Direct link to MISSING_REQUIRED_TABLE_FEATURE")

IcebergCompatV`<version>` requires feature `<feature>` to be supported and enabled.

## REPLACE\_TABLE\_CHANGE\_PARTITION\_NAMES[​](#replace_table_change_partition_names "Direct link to REPLACE_TABLE_CHANGE_PARTITION_NAMES")

IcebergCompatV`<version>` doesn't support replacing partitioned tables with a differently-named partition spec, because Iceberg-Spark 1.1.0 doesn't.

Prev Partition Spec: `<prevPartitionSpec>`

New Partition Spec: `<newPartitionSpec>`

## REQUIRE\_MANAGED\_TABLE[​](#require_managed_table "Direct link to REQUIRE_MANAGED_TABLE")

The feature can be enabled only on Managed Tables.

## REWRITE\_DATA\_FAILED[​](#rewrite_data_failed "Direct link to REWRITE_DATA_FAILED")

Rewriting data to IcebergCompatV`<version>` failed.

Please run the `REORG TABLE` table `APPLY (UPGRADE UNIFORM (ICEBERG_COMPAT_VERSION=<version>)` command again.

## SCHEMA\_COMPATIBILITY\_CHECK\_FAILED[​](#schema_compatibility_check_failed "Direct link to SCHEMA_COMPATIBILITY_CHECK_FAILED")

Apache Iceberg schema compatibility check failed during table creation or conversion: `<reason>`.

## UNSUPPORTED\_DATA\_TYPE[​](#unsupported_data_type "Direct link to UNSUPPORTED_DATA_TYPE")

IcebergCompatV`<version>` does not support the data type `<dataType>` in your schema. Your schema:

`<schema>`

## UNSUPPORTED\_PARTITION\_DATA\_TYPE[​](#unsupported_partition_data_type "Direct link to UNSUPPORTED_PARTITION_DATA_TYPE")

IcebergCompatV`<version>` does not support the data type `<dataType>` for partition columns in your schema. Your partition schema:

`<schema>`

## UNSUPPORTED\_TYPE\_WIDENING[​](#unsupported_type_widening "Direct link to UNSUPPORTED_TYPE_WIDENING")

IcebergCompatV`<version>` is incompatible with a type change applied to this table:

Field `<fieldPath>` was changed from `<prevType>` to `<newType>`.

## VERSION\_MUTUAL\_EXCLUSIVE[​](#version_mutual_exclusive "Direct link to VERSION_MUTUAL_EXCLUSIVE")

Only one IcebergCompat version can be enabled, please explicitly disable all other IcebergCompat versions that are not needed.

## WRONG\_REQUIRED\_TABLE\_PROPERTY[​](#wrong_required_table_property "Direct link to WRONG_REQUIRED_TABLE_PROPERTY")

IcebergCompatV`<version>` requires table property '`<key>`' to be set to '`<requiredValue>`'. Current value: '`<actualValue>`'.
