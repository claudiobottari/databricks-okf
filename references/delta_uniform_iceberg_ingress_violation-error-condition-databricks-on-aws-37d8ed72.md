---
title: DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION error condition | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-uniform-iceberg-ingress-violation-error-class
ingestedAt: "2026-06-18T08:07:38.871Z"
---

[SQLSTATE: KD00E](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-kd-datasource-specific-errors)

Read Apache Iceberg with Delta Uniform has failed.

Failed to parse version from existing metadata location `<existingLocation>` or current metadata location `<currentLocation>`;

Check the file name convention on Apache Iceberg writer.

## MISSING\_UNIFORM\_TBL\_PROPERTIES[​](#missing_uniform_tbl_properties "Direct link to MISSING_UNIFORM_TBL_PROPERTIES")

At least one of tableId `<tableId>`, snapshotId `<snapshotId>`, metadataLocation `<location>` is missing from Delta table properties; Is there manual change to the \_delta\_log?

## MUST\_REFRESH\_SAME\_TABLE[​](#must_refresh_same_table "Direct link to MUST_REFRESH_SAME_TABLE")

Refresh existing Apache Iceberg table UUID `<existingId>`, with metadata from different Apache Iceberg table UUID `<currentId>` is not supported.

Metadata location to be refreshed must have a higher version than existing metadata location.

Existing metadata location `<existingLocation>`; current metadata location `<currentLocation>`.
