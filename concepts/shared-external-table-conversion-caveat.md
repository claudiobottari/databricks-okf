---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5f58c3938a73e6b165487847b65f533fb4b323d2b4e07d73629479b5cded2568
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - shared-external-table-conversion-caveat
    - SETCC
  citations:
    - file: convert-to-delta-databricks-on-aws.md
title: Shared External Table Conversion Caveat
description: The issue that multiple external tables sharing the same underlying Parquet directory require all such tables to be converted to Delta Lake, or they become inaccessible after the first conversion.
tags:
  - delta-lake
  - caveat
  - external-tables
timestamp: "2026-06-19T14:26:03.675Z"
---

# Shared External Table Conversion Caveat

The **Shared External Table Conversion Caveat** describes a situation where multiple External Tables in the [Hive Metastore](/concepts/built-in-hive-metastore.md) point to the same underlying Parquet directory. When the `CONVERT TO DELTA` command is run on one of those external tables, the directory is converted from Parquet to [Delta Lake](/concepts/delta-lake.md), making the other external tables that still expect Parquet metadata inaccessible until they are also converted. ^[convert-to-delta-databricks-on-aws.md]

## Cause

It is possible for several external tables (either in the same or different databases) to share the same location on disk — for example, a directory of Parquet files. If a user runs `CONVERT TO DELTA` on one of those tables, the command changes the directory’s underlying format by creating a Delta Lake transaction log. The other external tables are not automatically updated, and because they still reference the directory as a Parquet source, they become unreadable. ^[convert-to-delta-databricks-on-aws.md]

## Consequences

After conversion:

- Queries or writes against the unconverted external tables fail because the directory is no longer pure Parquet.
- The table metadata in the [Metastore](/concepts/metastore.md) still reflects the old Parquet format, which is now incompatible with the Delta Lake transaction log present in the directory.

## Solution

To restore access to the other external tables, you must also run `CONVERT TO DELTA` on each of them. This updates their metadata and allows them to work with the now-Delta directory. ^[convert-to-delta-databricks-on-aws.md]

## Prevention

Before converting a shared directory, identify all external tables that reference the same underlying path. Either convert them all at once or consolidate into a single table definition to avoid confusion.

## Related Concepts

- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — The SQL command that triggers this caveat.
- External Table — A table whose data resides outside the metastore’s managed location.
- [Parquet-to-Delta Conversion](/concepts/parquet-to-delta-conversion.md) — The general process of migrating Parquet data to Delta Lake.
- Delta Lake Compatibility — Issues that arise when mixing Delta and non-Delta readers on the same directory.
- [Hive Metastore](/concepts/built-in-hive-metastore.md) — The catalog that stores table metadata and location.

## Sources

- convert-to-delta-databricks-on-aws.md

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
