---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 50d2bd8ab9d17130d75873b0be31ab9400f7fe10966473d05100cda22598ac00
  pageDirectory: concepts
  sources:
    - delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-uniform-required-table-properties
    - DURTP
  citations:
    - file: delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md
title: Delta Uniform Required Table Properties
description: The set of Delta table properties (tableId, snapshotId, metadataLocation) that must be present for Delta Uniform to function correctly when bridging between Delta Lake and Apache Iceberg.
tags:
  - databricks
  - delta-uniform
  - configuration
timestamp: "2026-06-18T15:23:13.485Z"
---

# Delta Uniform Required Table Properties

**Delta Uniform Required Table Properties** are the set of [Delta table](/concepts/delta-lake-table.md) properties that must be present for [Delta Uniform](/concepts/delta-uniform.md) (which exposes Delta tables as [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) tables) to function correctly. If any of these properties are missing, operations such as reading the table via the Iceberg protocol will fail with a `DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION` error. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Required Properties

The following three properties must be set in the Delta table’s metadata to enable Iceberg read compatibility:

- **`tableId`** – A unique identifier for the table.
- **`snapshotId`** – The identifier of the current snapshot.
- **`metadataLocation`** – The path to the Delta log metadata file.

If any of these properties are missing, Delta Uniform cannot determine the table’s identity or current state, and the engine raises the error sub‑condition `MISSING_UNIFORM_TBL_PROPERTIES`. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md] The error message explicitly lists which property is absent:

```
At least one of tableId <tableId>, snapshotId <snapshotId>, metadataLocation <location> is missing from Delta table properties; Is there manual change to the _delta_log?
```

^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Causes

The most common cause is a manual modification of the Delta transaction log (`_delta_log`), such as directly editing or deleting metadata files without using the Delta protocol. Databricks internally manages these properties; external changes that strip or omit them will break the Iceberg ingress pathway. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Related Error Conditions

The `DELTA_UNIFORM_ICEBERG_INGRESS_VIOLATION` error class also includes other sub‑conditions that cover additional validation failures:

- `MUST_REFRESH_SAME_TABLE` – Occurs when trying to refresh metadata with a different Iceberg table UUID. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]
- General parsing errors when version information in the metadata location is malformed. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Resolution

To resolve a `MISSING_UNIFORM_TBL_PROPERTIES` error:

1. Verify that the Delta table was created or altered correctly using [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) or the Delta Lake API, which automatically sets these properties.
2. Avoid any direct edits to the Delta transaction log. If manual changes have occurred, restore the required properties from a known good snapshot or re‑create the Delta table.
3. Use the `DESCRIBE DETAIL` command to inspect the current table properties and confirm that `tableId`, `snapshotId`, and `metadataLocation` are present. ^[delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) – The feature that allows Delta tables to be read as Iceberg tables.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The open table format supported by Delta Uniform.
- [Delta transaction log](/concepts/delta-transaction-log.md) – The `_delta_log` directory that stores metadata and must not be manually altered.
- Iceberg ingress – The process of reading a Delta table through the Iceberg protocol.
- Delta table properties – Metadata key‑value pairs that control table behavior.

## Sources

- delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_iceberg_ingress_violation-error-condition-databricks-on-aws-37d8ed72.md)
