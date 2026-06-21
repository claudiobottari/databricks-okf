---
title: DELTA_VIOLATE_TABLE_PROPERTY_VALIDATION_FAILED error condition | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-violate-table-property-validation-failed-error-class
ingestedAt: "2026-06-18T08:07:49.049Z"
---

[SQLSTATE: 0A000](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-0a-feature-not-supported)

The validation of the properties of table `<table>` has been violated:

## EXISTING\_DELETION\_VECTORS\_WITH\_INCREMENTAL\_MANIFEST\_GENERATION[​](#existing_deletion_vectors_with_incremental_manifest_generation "Direct link to EXISTING_DELETION_VECTORS_WITH_INCREMENTAL_MANIFEST_GENERATION")

Symlink manifest generation is unsupported while deletion vectors are present in the table.

In order to produce a version of the table without deletion vectors, run '`REORG TABLE <table> APPLY (PURGE)`'.

## PERSISTENT\_DELETION\_VECTORS\_IN\_NON\_PARQUET\_TABLE[​](#persistent_deletion_vectors_in_non_parquet_table "Direct link to PERSISTENT_DELETION_VECTORS_IN_NON_PARQUET_TABLE")

Persistent deletion vectors are only supported on Parquet-based Delta tables.

## PERSISTENT\_DELETION\_VECTORS\_WITH\_INCREMENTAL\_MANIFEST\_GENERATION[​](#persistent_deletion_vectors_with_incremental_manifest_generation "Direct link to PERSISTENT_DELETION_VECTORS_WITH_INCREMENTAL_MANIFEST_GENERATION")

Persistent deletion vectors and incremental symlink manifest generation are mutually exclusive.
