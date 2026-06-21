---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 48007f1070c2e85599088911e3772a34ffd566f7f0e364c69ee3bf020e97ab37
  pageDirectory: concepts
  sources:
    - read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - asynchronous-iceberg-metadata-generation
    - AIMG
    - Asynchronous Task Execution
  citations:
    - file: read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
      start: 11
      end: 24
    - file: read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
      start: 30
      end: 42
    - file: read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
      start: 45
      end: 48
    - file: read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
      start: 66
      end: 74
    - file: read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
      start: 72
      end: 74
    - file: read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
      start: 82
      end: 90
    - file: read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
      start: 96
      end: 102
    - file: read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
      start: 108
      end: 115
    - file: read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
      start: 109
      end: 115
    - file: read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
      start: 120
      end: 125
    - file: read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
      start: 19
      end: 24
    - file: read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
      start: 130
      end: 132
title: Asynchronous Iceberg Metadata Generation
description: The process by which Databricks automatically generates Iceberg metadata (commit metadata JSON files) in the background after each Delta Lake write transaction, using the same compute resource without blocking writes.
tags:
  - delta-lake
  - iceberg
  - metadata
  - performance
timestamp: "2026-06-19T20:11:28.262Z"
---

# Asynchronous Iceberg Metadata Generation

**Asynchronous Iceberg Metadata Generation** is the mechanism by which Databricks automatically creates Apache Iceberg metadata for Delta Lake tables that have Iceberg reads (UniForm) enabled, without blocking write transactions. This allows Iceberg clients to read Delta Lake tables using the same underlying Parquet data files.

## How it works

When Iceberg reads are enabled on a [Delta Lake Table](/concepts/delta-lake-table.md), Databricks generates Iceberg metadata asynchronously after each Delta Lake write transaction completes. The metadata is produced on the same compute resource that executed the Delta Lake transaction, without rewriting any data files. A single copy of the Parquet data files then serves both Delta and Iceberg readers. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md#L11-L24]

## Requirements

Asynchronous metadata generation is automatically triggered when the following conditions are met:

- The [Delta Lake Table](/concepts/delta-lake-table.md) is registered to [Unity Catalog](/concepts/unity-catalog.md) (managed or external).
- Column mapping is enabled on the table.
- The table has `minReaderVersion >= 2` and `minWriterVersion >= 7`.
- All writes to the table use Databricks Runtime 14.3 LTS or above.
- The table is accessed by **name** (not by path) to trigger automatic metadata generation. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md#L30-L42]

Deletion vectors must not be enabled on the table. If they are, use `REORG` to disable and purge them before enabling Iceberg reads. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md#L45-L48]

## Metadata generation process

The asynchronous generation process runs after a Delta Lake write transaction finishes. To avoid introducing latency into write operations, Databricks groups multiple Delta Lake commits into a single Iceberg metadata commit when table commits occur frequently (seconds to minutes apart). ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md#L66-L74]

Only one metadata generation process can be active on a given compute resource at any time. If a commit occurs while another metadata generation is already in progress, the commit succeeds in Delta Lake but does **not** trigger an additional asynchronous Iceberg metadata generation. This prevents cascading latency for high-frequency write workloads. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md#L72-L74]

## Tracking status

The metadata generation status is recorded in both Unity Catalog and Iceberg table properties. On Databricks, you can review it using `DESCRIBE EXTENDED` (look for the *Delta Uniform Iceberg* section) or in [Catalog Explorer](/concepts/catalog-explorer.md). The following metadata fields are available:

- `delta.uniform.deltaVersions`: The range of Delta Lake versions that have been converted to Iceberg.
- `delta.uniform.lastUpdatedTimestamp`: The timestamp of the last Iceberg metadata generation.

^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md#L82-L90]

## Manual trigger

If automatic generation fails (e.g., due to cluster termination, job failure, or a write from a client that does not support UniForm), you can manually trigger a synchronous metadata conversion using the `MSCK REPAIR TABLE` command:

```sql
MSCK REPAIR TABLE <table_name> SYNC METADATA
```

^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md#L96-L102]

## Metadata JSON files

Each time Databricks converts a new version of the [Delta Lake Table](/concepts/delta-lake-table.md) to Iceberg, a new metadata JSON file is created under the table directory:

```
<table-path>/metadata/<version-number>-<uuid>.metadata.json
```

Some Iceberg clients (such as BigQuery) require the path to the latest metadata JSON file to register an external Iceberg table. You can find the current metadata location in the *Delta Uniform Iceberg* section of `DESCRIBE EXTENDED` or in Catalog Explorer. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md#L108-L115]

Clients that use path-based registration must manually update the metadata JSON path when table versions advance. Querying stale metadata can cause errors if corresponding Parquet data files have been removed by `VACUUM`. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md#L109-L115]

## Limitations

- Asynchronous metadata generation works only when the table is accessed by **name**; path-based access does not trigger it. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md#L120-L125]
- Metadata generation uses driver resources on the compute that wrote the data, which can increase driver memory and CPU usage. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md#L19-L24]
- Iceberg metadata generation is not supported for [materialized views](/concepts/materialized-views-in-databricks.md) or streaming tables. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md#L120-L125]
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) works for Delta clients but is **not** exposed in Iceberg metadata. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md#L130-L132]

## Related concepts

- [Delta Lake Universal Format (UniForm)](/concepts/delta-lake-universal-format-uniform.md) – The original name for this feature.
- [IcebergCompatV2](/concepts/icebergcompatv2.md) – The write protocol feature required for Iceberg reads.
- [Column mapping](/concepts/column-mapping-in-delta-lake.md) – A prerequisite for Iceberg reads.
- [Deletion Vectors](/concepts/deletion-vectors.md) – Not compatible with Iceberg v2 reads.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The open table format used for reading.
- [MSCK REPAIR TABLE](/concepts/fsck-repair-table.md) – SQL command to manually trigger metadata generation.

## Sources

- read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md

# Citations

1. [read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md:11-24](/references/read-delta-lake-tables-with-iceberg-clients-databricks-on-aws-ae1b1933.md)
2. [read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md:30-42](/references/read-delta-lake-tables-with-iceberg-clients-databricks-on-aws-ae1b1933.md)
3. [read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md:45-48](/references/read-delta-lake-tables-with-iceberg-clients-databricks-on-aws-ae1b1933.md)
4. [read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md:66-74](/references/read-delta-lake-tables-with-iceberg-clients-databricks-on-aws-ae1b1933.md)
5. [read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md:72-74](/references/read-delta-lake-tables-with-iceberg-clients-databricks-on-aws-ae1b1933.md)
6. [read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md:82-90](/references/read-delta-lake-tables-with-iceberg-clients-databricks-on-aws-ae1b1933.md)
7. [read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md:96-102](/references/read-delta-lake-tables-with-iceberg-clients-databricks-on-aws-ae1b1933.md)
8. [read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md:108-115](/references/read-delta-lake-tables-with-iceberg-clients-databricks-on-aws-ae1b1933.md)
9. [read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md:109-115](/references/read-delta-lake-tables-with-iceberg-clients-databricks-on-aws-ae1b1933.md)
10. [read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md:120-125](/references/read-delta-lake-tables-with-iceberg-clients-databricks-on-aws-ae1b1933.md)
11. [read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md:19-24](/references/read-delta-lake-tables-with-iceberg-clients-databricks-on-aws-ae1b1933.md)
12. [read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md:130-132](/references/read-delta-lake-tables-with-iceberg-clients-databricks-on-aws-ae1b1933.md)
