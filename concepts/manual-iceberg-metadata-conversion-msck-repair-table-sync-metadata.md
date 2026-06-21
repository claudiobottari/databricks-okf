---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 95367b21b171dfd1ba0f96b4e632a23e59253ea66d8e24288a1304dc3f526a53
  pageDirectory: concepts
  sources:
    - read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - manual-iceberg-metadata-conversion-msck-repair-table-sync-metadata
    - MIMC(RTSM
  citations:
    - file: read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md
title: Manual Iceberg Metadata Conversion (MSCK REPAIR TABLE SYNC METADATA)
description: A synchronous operation that manually triggers Iceberg metadata generation for the latest Delta Lake table version, used when automatic generation fails due to cluster termination, errors, or writes from non-UniForm clients.
tags:
  - delta-lake
  - iceberg
  - operations
timestamp: "2026-06-19T20:11:24.286Z"
---

# Manual Iceberg Metadata Conversion (MSCK REPAIR TABLE SYNC METADATA)

**Manual Iceberg Metadata Conversion** is a synchronous operation that triggers immediate Iceberg metadata generation for the latest version of a [Delta Lake Table](/concepts/delta-lake-table.md) that has Iceberg reads (UniForm) enabled. This operation is performed using the `MSCK REPAIR TABLE <table-name> SYNC METADATA` SQL command. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Overview

When Iceberg reads are enabled on a [Delta Lake Table](/concepts/delta-lake-table.md), metadata generation typically runs asynchronously after each Delta Lake write transaction completes. The `MSCK REPAIR TABLE SYNC METADATA` command provides a way to manually trigger this conversion synchronously, meaning that when the command completes, the table contents available in Iceberg reflect the latest version of the [Delta Lake Table](/concepts/delta-lake-table.md) available when the conversion process started. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## When to Use Manual Conversion

Under normal conditions, manual metadata conversion should not be necessary because Databricks automatically generates Iceberg metadata asynchronously after write transactions. However, manual conversion can help in the following scenarios: ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

- A cluster terminates before automatic metadata generation succeeds.
- An error or job failure interrupts metadata generation.
- A client that does not support UniForm Iceberg metadata generation writes to the [Delta Lake Table](/concepts/delta-lake-table.md).

## Syntax

The command uses the following syntax:

```sql
MSCK REPAIR TABLE <table-name> SYNC METADATA
```

^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## How It Works

When executed, the command performs a synchronous conversion of the current [Delta Lake Table](/concepts/delta-lake-table.md) version to Iceberg metadata. This means the operation blocks until the metadata generation is complete, and upon successful completion, external Iceberg clients can immediately query the latest table version. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

Each time Databricks converts a new version of the [Delta Lake Table](/concepts/delta-lake-table.md) to Iceberg, it creates a new metadata JSON file stored under the table directory using the following pattern: ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

```
<table-path>/metadata/<version-number>-<uuid>.metadata.json
```

## Relationship to Automatic Metadata Generation

Delta Lake tables with Iceberg reads enabled automatically trigger metadata generation asynchronously after a Delta Lake write transaction completes. This metadata generation process uses the same compute that completed the Delta Lake transaction. To avoid write latencies, Delta Lake tables with frequent commits might group multiple Delta Lake commits into a single commit to Iceberg metadata. ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

Delta Lake ensures that only one metadata generation process is in progress on a given compute resource. Commits that would trigger a second concurrent metadata generation process successfully commit to Delta Lake but don't trigger asynchronous Iceberg metadata generation, preventing cascading latency for workloads with frequent commits (seconds to minutes between commits). ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

## Checking Metadata Generation Status

You can review Iceberg metadata generation status by doing one of the following: ^[read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md]

- Reviewing the `Delta Uniform Iceberg` section returned by `DESCRIBE EXTENDED table_name`.
- Reviewing table metadata with Catalog Explorer.

## Related Concepts

- [Iceberg Reads (UniForm)](/concepts/delta-uniform.md) — The feature that enables Iceberg clients to read Delta Lake tables.
- [Delta Lake to Iceberg Metadata Conversion](/concepts/delta-uniform-metadata-conversion.md) — The asynchronous process that generates Iceberg metadata automatically.
- Delta Lake Table Properties — Configuration properties for enabling Iceberg reads.
- Iceberg Metadata File Location — Where versioned metadata JSON files are stored.
- [REPAIR TABLE](/concepts/fsck-repair-table.md) — The SQL command used for manual metadata conversion.

## Sources

- read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md

# Citations

1. [read-delta-lake-tables-with-iceberg-clients-databricks-on-aws.md](/references/read-delta-lake-tables-with-iceberg-clients-databricks-on-aws-ae1b1933.md)
