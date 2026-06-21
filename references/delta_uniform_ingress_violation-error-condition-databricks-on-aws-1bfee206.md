---
title: DELTA_UNIFORM_INGRESS_VIOLATION error condition | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-uniform-ingress-violation-error-class
ingestedAt: "2026-06-18T08:07:40.625Z"
---

[SQLSTATE: KD00E](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-kd-datasource-specific-errors)

Read Delta Uniform fails:

Metadata conversion from `<format>` to Delta failed, `<errorMessage>`.

## DELTA\_LOG\_LOCATION\_NOT\_FOUND[​](#delta_log_location_not_found "Direct link to DELTA_LOG_LOCATION_NOT_FOUND")

The delta\_log location is missing for table `<tableName>`.

Cannot find metadata path for table `<tableName>`.

## NOT\_UNIFORM\_INGRESS\_TABLE[​](#not_uniform_ingress_table "Direct link to NOT_UNIFORM_INGRESS_TABLE")

Table `<tableName>` is not a uniform ingress table.

## OPERATION\_NOT\_SUPPORTED[​](#operation_not_supported "Direct link to OPERATION_NOT_SUPPORTED")

Operation is not supported. Only `CREATE` and `REFRESH` are supported on Uniform Apache Iceberg Ingress Table.

## UNEXPECTED\_DELTA\_LOG\_LOCATION[​](#unexpected_delta_log_location "Direct link to UNEXPECTED_DELTA_LOG_LOCATION")

Unexpected delta\_log location `<tablePath>` for table `<tableName>`.

## UNITY\_CATALOG\_NOT\_ENABLED[​](#unity_catalog_not_enabled "Direct link to UNITY_CATALOG_NOT_ENABLED")

Unity Catalog is required for Read Apache Iceberg with Delta Uniform.
