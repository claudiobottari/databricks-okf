---
title: DELTA_CLONE_INCOMPATIBLE_SOURCE error condition | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-clone-incompatible-source-error-class
ingestedAt: "2026-06-18T08:07:06.735Z"
---

[SQLSTATE: 0AKDC](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-0a-feature-not-supported)

The clone source has valid format, but has unsupported feature with Delta.

## HAS\_INDEXES[​](#has_indexes "Direct link to HAS_INDEXES")

Table `<tableName>` has indexes: `<indexNames>`. Drop the indexes before cloning.

## ICEBERG\_MISSING\_PARTITION\_SPECS[​](#iceberg_missing_partition_specs "Direct link to ICEBERG_MISSING_PARTITION_SPECS")

Source Apache Iceberg table has no partition specs in table.

## ICEBERG\_UNDERGONE\_PARTITION\_EVOLUTION[​](#iceberg_undergone_partition_evolution "Direct link to ICEBERG_UNDERGONE_PARTITION_EVOLUTION")

Source Apache Iceberg table has undergone partition evolution.
