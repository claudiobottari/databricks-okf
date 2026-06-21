---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60b9e136b5ee5049920c1c3ea83d509b89ce4dda46354754be2406f9d156b41c
  pageDirectory: concepts
  sources:
    - delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - delta-uniform-delta_log-location-errors
    - DUDLE
  citations:
    - file: delta_uniform_ingress_violation-error-condition-databricks-on-aws.md
title: Delta Uniform delta_log location errors
description: Errors related to missing, unexpected, or incorrect delta_log location metadata when working with Delta Uniform ingress tables
tags:
  - error-messages
  - delta-lake
  - databricks
timestamp: "2026-06-18T11:57:14.400Z"
---

# Delta Uniform delta_log location errors

**Delta Uniform delta_log location errors** are a category of error conditions that occur when [Delta Uniform](/concepts/delta-uniform.md) fails to read or convert metadata from another table format (such as [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)) to [Delta Lake](/concepts/delta-lake.md) format. These errors indicate problems with the delta_log location, which is the metadata directory that Delta Uniform uses to expose non-Delta tables as Delta tables. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Overview

Delta Uniform enables tables stored in other formats (like Apache Iceberg or Apache Hive) to be read as if they were Delta Lake tables. This requires a valid delta_log location — the directory where Delta's transaction log is stored. When Delta Uniform cannot locate or access this directory, or when the directory contains unexpected metadata, it raises a `DELTA_UNIFORM_INGRESS_VIOLATION` error. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Error Sub-types

### DELTA_LOG_LOCATION_NOT_FOUND

**Error message:**

```
The delta_log location is missing for table <tableName>.
Cannot find metadata path for table <tableName>.
```

^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

This error occurs when Delta Uniform cannot locate the metadata path for a table. The `_delta_log` directory — which contains the Delta transaction log — is either missing, inaccessible, or the table was not properly configured as a Delta Uniform ingress table. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### NOT_UNIFORM_INGRESS_TABLE

**Error message:**

```
Table <tableName> is not a uniform ingress table.
```

^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

This error occurs when an operation attempts to read a table through Delta Uniform, but the table was not created or configured as a [Delta Uniform Ingress Table](/concepts/delta-uniform-ingress-table.md). The table might exist in another format (such as Iceberg or Hive) but lacks the Delta Uniform metadata layer needed for Delta-native reads. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### UNEXPECTED_DELTA_LOG_LOCATION

**Error message:**

```
Unexpected delta_log location <tablePath> for table <tableName>.
```

^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

This error occurs when Delta Uniform finds a delta_log location at a path that does not match expectations for the given table. This can happen when:

- A table's metadata points to a delta_log location that belongs to a different table.
- The delta_log path has been modified or corrupted.
- The table was moved or renamed without updating the Delta Uniform metadata.

### UNITY_CATALOG_NOT_ENABLED

**Error message:**

```
Unity Catalog is required for Read Apache Iceberg with Delta Uniform.
```

^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

This error occurs when a read operation attempts to use Delta Uniform with [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) tables but [Unity Catalog](/concepts/unity-catalog.md) is not enabled on the workspace. Delta Uniform's Iceberg integration requires Unity Catalog to be active. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

### OPERATION_NOT_SUPPORTED

**Error message:**

```
Operation is not supported. Only `CREATE` and `REFRESH` are supported on Uniform Apache Iceberg Ingress Table.
```

^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

This error occurs when an operation other than `CREATE` or `REFRESH` is attempted on a Delta Uniform ingress table backed by Apache Iceberg. These tables only support the creation of the Delta Uniform metadata layer and refreshing of the Delta log from the source format. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Common Causes

| Cause | Related Error |
|-------|---------------|
| The `_delta_log` directory was not created for the table | `DELTA_LOG_LOCATION_NOT_FOUND` |
| The table is not registered as a Delta Uniform ingress table | `NOT_UNIFORM_INGRESS_TABLE` |
| The delta_log path points to a different table's metadata | `UNEXPECTED_DELTA_LOG_LOCATION` |
| Unity Catalog is not enabled on the workspace | `UNITY_CATALOG_NOT_ENABLED` |
| An unsupported operation was attempted on an Iceberg-backed Delta Uniform table | `OPERATION_NOT_SUPPORTED` |

## Troubleshooting Steps

1. **Verify the table is a Delta Uniform table.** Check that the table was created using `CREATE TABLE` with `UNIFORM` or `INGRESS` configuration. If the table was created in a different format and you want to read it via Delta Uniform, you may need to create a Delta Uniform layer over the existing table. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

2. **Check that the delta_log directory exists.** The `_delta_log` directory must exist at the expected table path. If the directory is missing, you may need to run a `REFRESH` operation to regenerate the Delta metadata from the source format. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

3. **Confirm Unity Catalog is enabled.** Delta Uniform's Iceberg integration requires Unity Catalog. Verify that your workspace has Unity Catalog enabled and that the table is registered in a Unity Catalog [Metastore](/concepts/metastore.md). ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

4. **Ensure the operation is supported.** Only `CREATE` and `REFRESH` operations are supported on Delta Uniform Iceberg ingress tables. Attempting other DDL or DML operations will result in an `OPERATION_NOT_SUPPORTED` error. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

5. **Validate the delta_log location path.** If you encounter an `UNEXPECTED_DELTA_LOG_LOCATION` error, examine the table's metadata to verify that the delta_log location points to the correct directory for this table. ^[delta_uniform_ingress_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) — The feature that enables reading non-Delta tables as Delta tables
- [Delta Uniform Ingress Table](/concepts/delta-uniform-ingress-table.md) — A table configured for inbound conversion to Delta format
- [Delta Lake](/concepts/delta-lake.md) — The open-source storage format that Delta Uniform targets
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — A table format that can be served through Delta Uniform
- [Unity Catalog](/concepts/unity-catalog.md) — Required for Delta Uniform Iceberg integration
- Delta Log — The transaction log directory that Delta Uniform reads
- [CREAT TABLE ... UNIFORM](/concepts/delta-uniform.md) — SQL syntax for creating Delta Uniform tables
- REFRESH — Operation to regenerate Delta metadata from the source format

## Sources

- delta_uniform_ingress_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_ingress_violation-error-condition-databricks-on-aws.md](/references/delta_uniform_ingress_violation-error-condition-databricks-on-aws-1bfee206.md)
