---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a43a508fcc127dc1da0f8d6d8f68dec48c1d3e8ce4a1ad70bd5908cb0d2f2476
  pageDirectory: concepts
  sources:
    - generate-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - generate-command-delta-lake
    - GC(L
    - GENERATE Command
    - GENERATE command
  citations:
    - file: generate-databricks-on-aws.md
title: GENERATE Command (Delta Lake)
description: A SQL statement used to generate manifest files for Delta Lake tables, primarily for compatibility with external query engines.
tags:
  - delta-lake
  - sql
  - databricks
timestamp: "2026-06-19T18:57:22.325Z"
---

# GENERATE Command (Delta Lake)

The **GENERATE command** is a Delta Lake SQL statement that produces a specified output mode — currently a manifest file — for an existing Delta table. It is used to make Delta table data accessible to query engines that do not natively read the Delta format. ^[generate-databricks-on-aws.md]

## Syntax

```sql
GENERATE mode FOR TABLE table_name
```

^[generate-databricks-on-aws.md]

## Parameters

- **mode** — A string literal specifying the type of output to generate. The only supported mode is `symlink_format_manifest`. This mode creates [manifest files](/concepts/delta-lake-manifest-files.md) that can be used to read the Delta table from Presto and Athena. ^[generate-databricks-on-aws.md]

- **table_name** — Identifies an existing [Delta Lake](/concepts/delta-lake.md) table. The name must not include a temporal specification or an options specification. ^[generate-databricks-on-aws.md]

## Usage

The `GENERATE` command operates on the latest table snapshot; it does not accept time-travel or option-based table references. ^[generate-databricks-on-aws.md]

For detailed instructions on generating and using manifest files, refer to the [Delta Lake documentation on generating a manifest file](https://docs.delta.io/latest/delta-utility.html#generate-a-manifest-file). ^[generate-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- [Symlink format manifest](/concepts/symlink-format-manifest.md)
- Presto
- Athena
- [Manifest file](/concepts/delta-lake-manifest-files.md)
- Delta Lake SQL commands

## Sources

- generate-databricks-on-aws.md

# Citations

1. [generate-databricks-on-aws.md](/references/generate-databricks-on-aws-7753d696.md)
