---
title: DELTA_ICEBERG_WRITER_COMPAT_VIOLATION error condition | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-iceberg-writer-compat-violation-error-class
ingestedAt: "2026-06-18T08:07:26.254Z"
---

[SQLSTATE: KD00E](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-kd-datasource-specific-errors)

The validation of IcebergWriterCompatV`<version>` has failed.

## CANNOT\_CHANGE\_MAP\_STRUCT\_KEY[​](#cannot_change_map_struct_key "Direct link to CANNOT_CHANGE_MAP_STRUCT_KEY")

IcebergWriterCompatV`<version>` disallows changing map keys that are structs. This transaction changes the key for maps: `<map_names>`.

## CONFIG\_NOT\_ENABLED[​](#config_not_enabled "Direct link to CONFIG_NOT_ENABLED")

IcebergWriterCompatV`<version>` requires the config `<config>` to be enabled.

## DISABLING\_REQUIRED\_TABLE\_FEATURE[​](#disabling_required_table_feature "Direct link to DISABLING_REQUIRED_TABLE_FEATURE")

IcebergWriterCompatV`<version>` requires feature `<feature>` to be supported and enabled. You cannot drop it from the table.

## FIELD\_ID\_DOES\_NOT\_MATCH\_PHYSICAL\_NAME[​](#field_id_does_not_match_physical_name "Direct link to FIELD_ID_DOES_NOT_MATCH_PHYSICAL_NAME")

IcebergWriterCompatV`<version>` requires column mapping field physical names be equal to 'col-\[fieldId\]', but this is not true for fields: `<field_names>`, physical names: `<physical_names>`.

## INCOMPATIBLE\_TABLE\_FEATURE[​](#incompatible_table_feature "Direct link to INCOMPATIBLE_TABLE_FEATURE")

IcebergWriterCompatV`<version>` is incompatible with feature `<feature>`.

## MISSING\_REQUIRED\_TABLE\_FEATURE[​](#missing_required_table_feature "Direct link to MISSING_REQUIRED_TABLE_FEATURE")

IcebergWriterCompatV`<version>` requires feature `<feature>` to be supported and enabled.

## UNSUPPORTED\_DATA\_TYPE[​](#unsupported_data_type "Direct link to UNSUPPORTED_DATA_TYPE")

IcebergWriterCompatV`<version>` does not support the data type `<dataType>` in your schema. Your schema:

`<schema>`

## UNSUPPORTED\_ICEBERG\_TABLE\_PROPERTY[​](#unsupported_iceberg_table_property "Direct link to UNSUPPORTED_ICEBERG_TABLE_PROPERTY")

IcebergWriterCompatV`<version>` does not support Apache Iceberg table property '`<key>`'.

## WRONG\_REQUIRED\_TABLE\_PROPERTY[​](#wrong_required_table_property "Direct link to WRONG_REQUIRED_TABLE_PROPERTY")

IcebergWriterCompatV`<version>` requires table property '`<key>`' to be set to '`<requiredValue>`'. Current value: '`<actualValue>`'.
