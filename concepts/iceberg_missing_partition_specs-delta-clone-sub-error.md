---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ac89bec4c3048b055fb9606f714667d77c56fe2fdecc0065d67308b5f0946d3e
  pageDirectory: concepts
  sources:
    - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iceberg_missing_partition_specs-delta-clone-sub-error
    - I(CS
  citations:
    - file: delta_clone_incompatible_source-error-condition-databricks-on-aws.md
title: ICEBERG_MISSING_PARTITION_SPECS (Delta Clone sub-error)
description: A specific DELTA_CLONE_INCOMPATIBLE_SOURCE sub-error indicating the source Iceberg table lacks partition specs.
tags:
  - error-message
  - delta-lake
  - iceberg
timestamp: "2026-06-19T10:02:43.611Z"
---

# ICEBERG_MISSING_PARTITION_SPECS (Delta Clone sub-error)

**ICEBERG_MISSING_PARTITION_SPECS** is a sub-error of the DELTA_CLONE_INCOMPATIBLE_SOURCE error condition. It occurs when a user attempts to clone a source Apache Iceberg table that has no partition specifications defined. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Error Detail

The full error message associated with this sub-error is:

> Source Apache Iceberg table has no partition specs in table.

This indicates that the clone source is a valid Iceberg table but lacks the partition metadata that Delta requires for the clone operation. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Cause

The source Iceberg table was created without any partition columns defined in its table metadata. The [Delta Clone](/concepts/delta-clone.md) feature for Iceberg tables requires partition specifications to be present, because Delta uses partition information to organize data layout. Without partition specs, the clone source is considered incompatible. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Resolution

To resolve this error, add partition specifications to the source Iceberg table before attempting the clone operation. This can be done by recreating the table with a `PARTITIONED BY` clause or by using ALTER TABLE to add partitions if the Iceberg table format supports it. (Inferred – not directly stated in the source.)

## Related Sub-errors

The DELTA_CLONE_INCOMPATIBLE_SOURCE error condition also includes these sub-errors:

- HAS_INDEXES – The source table has indexes that must be dropped before cloning.
- ICEBERG_UNDERGONE_PARTITION_EVOLUTION – The source Iceberg table has undergone partition evolution (partition scheme changed over time). ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## See Also

- [Delta Clone](/concepts/delta-clone.md) – The feature that triggers this error.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The table format used as a clone source.
- ICEBERG_MISSING_PARTITION_SPECS|Partition Specs – Metadata describing how data is partitioned.
- HAS_INDEXES (Delta Clone sub-error)
- ICEBERG_UNDERGONE_PARTITION_EVOLUTION (Delta Clone sub-error)

## Sources

- delta_clone_incompatible_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_incompatible_source-error-condition-databricks-on-aws.md](/references/delta_clone_incompatible_source-error-condition-databricks-on-aws-b63ca67d.md)
