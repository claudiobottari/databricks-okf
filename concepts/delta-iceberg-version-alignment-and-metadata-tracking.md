---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 697bb2be234bd1f9b2849b0b3ca4b9766578a6b8a44495516ce52eca3a11547e
  pageDirectory: concepts
  sources:
    - read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-iceberg-version-alignment-and-metadata-tracking
    - Metadata Tracking and Delta-Iceberg Version Alignment
    - DVAAMT
  citations:
    - file: read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
title: Delta-Iceberg Version Alignment and Metadata Tracking
description: Delta Lake and Iceberg table versions do not directly align by commit timestamp or version ID; metadata fields track the relationship, accessible via DESCRIBE EXTENDED or Catalog Explorer.
tags:
  - delta-lake
  - iceberg
  - versioning
  - metadata
timestamp: "2026-06-19T20:12:17.968Z"
---

# Delta-Iceberg Version Alignment and Metadata Tracking

**Delta-Iceberg Version Alignment and Metadata Tracking** refers to the mechanisms by which Delta Lake tables with Iceberg read support (UniForm) maintain version correspondence and metadata generation status between the two formats. When Iceberg reads are enabled on a [Delta Lake Table](/concepts/delta-lake-table.md), metadata is generated asynchronously, and the version IDs between Delta and Iceberg do not directly align. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Version Mismatch

In general, [Delta Lake Table](/concepts/delta-lake-table.md) versions **do not align** with Iceberg versions by either commit timestamp or version ID. This means that a given Iceberg snapshot may not correspond directly to a specific [Delta Lake Table](/concepts/delta-lake-table.md) version. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Metadata Generation Tracking

Enabling Iceberg reads on a [Delta Lake Table](/concepts/delta-lake-table.md) adds specific metadata fields to [Unity Catalog](/concepts/unity-catalog.md) and Iceberg table metadata to track metadata generation status. These fields allow users to verify which version of a [Delta Lake Table](/concepts/delta-lake-table.md) a given Iceberg table version corresponds to. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

### Checking Generation Status

On Databricks, users can review metadata generation status through:

- The **Delta Uniform Iceberg** section returned by `DESCRIBE EXTENDED table_name`
- Table metadata in **Catalog Explorer**
- Table properties via `SHOW TBLPROPERTIES` outside Databricks

^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Metadata Commit Batching

Delta Lake tables with frequent commits may **group multiple Delta Lake commits** into a single commit to Iceberg metadata. This batching helps avoid write latencies associated with metadata generation. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Concurrent Metadata Generation Prevention

Delta Lake ensures that **only one metadata generation process** is in progress on a given compute resource at a time. Commits that would trigger a second concurrent metadata generation process successfully commit to Delta Lake but do not trigger asynchronous Iceberg metadata generation. This prevents cascading latency for workloads with frequent commits (seconds to minutes between commits). ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Metadata File Storage

Delta Lake stores Iceberg metadata under the table directory using the following pattern:

```
<table-path>/metadata/<version-number>-<uuid>.metadata.json
```

^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Manual Metadata Trigger

The `MSCK REPAIR TABLE` command can be used to manually trigger Iceberg metadata generation for the latest version of the [Delta Lake Table](/concepts/delta-lake-table.md). This operation runs synchronously, meaning that when it completes, the table contents available in Iceberg reflect the latest version of the [Delta Lake Table](/concepts/delta-lake-table.md) available when the conversion process started. This should not be necessary under normal conditions, but can help if:

- A cluster terminates before automatic metadata generation succeeds
- An error or job failure interrupts metadata generation
- A client that does not support UniForm Iceberg metadata generation writes to the [Delta Lake Table](/concepts/delta-lake-table.md)

^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Universal Format (UniForm)](/concepts/delta-lake-universal-format-uniform.md) — The overarching framework for enabling multi-format reads on Delta tables
- [IcebergCompatV2](/concepts/icebergcompatv2.md) — The Delta write protocol feature required for Iceberg read support
- Delta Lake feature compatibility and protocols — Requirements for Delta reader and writer versions
- [Unity Catalog](/concepts/unity-catalog.md) — The metadata catalog that tracks Iceberg read-enabled tables
- [Column mapping](/concepts/column-mapping-in-delta-lake.md) — A required feature for Iceberg read support

## Sources

- read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md

# Citations

1. [read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md](/references/read-delta-lake-tables-with-iceberg-clients-databricks-on-aws-ae1b1933.md)
