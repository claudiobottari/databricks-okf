---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3ceb28fc219cd5252a41a21606caed2e666d0a87adad99b53085009cc8563b7f
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deletion-vectors-and-column-mapping-in-shared-tables
    - Column Mapping in Shared Tables and Deletion Vectors
    - DVACMIST
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Deletion Vectors and Column Mapping in Shared Tables
description: Storage optimization features (deletion vectors for efficient deletes/updates, column mapping for renaming/dropping columns) that can be enabled on shared Delta tables. Requires history sharing and recipients must use Databricks Runtime 14.1+ or open source delta-sharing-spark 3.1+ to query such tables.
tags:
  - delta-sharing
  - delta-lake
  - storage-optimization
timestamp: "2026-06-19T18:02:21.736Z"
---

# Deletion Vectors and Column Mapping in Shared Tables

**Deletion vectors** and **column mapping** are [Delta Lake Table](/concepts/delta-lake-table.md) features that can be enabled on source tables shared via [OpenSharing](/concepts/opensharing.md). Deletion vectors allow Delta tables to mark rows as deleted without rewriting data files, while column mapping enables renaming and dropping columns without rewriting underlying Parquet files. Both features improve storage efficiency and schema flexibility, but impose specific requirements on how tables are shared and queried.^[create-shares-for-opensharing-databricks-on-aws.md]

## Provider Requirements

To share a table that has deletion vectors or column mapping enabled, the provider **must share the table with history** (full history from the beginning). History sharing is configured when adding the table to a share via Catalog Explorer, SQL, or the CLI. Without history sharing, tables using these features cannot be added to a share. See Add tables to a share for instructions on enabling history sharing.^[create-shares-for-opensharing-databricks-on-aws.md]

## Recipient Requirements

When a shared table uses deletion vectors or column mapping, recipients must use one of the following compute types to query it:

- A SQL warehouse (Databricks SQL)
- A compute cluster running **Databricks Runtime 14.1 or above**
- A compute cluster running **open source `delta-sharing-spark` 3.1 or above**

These versions contain the necessary reader support for resolving deletion vectors and column mapping metadata. Recipients using older runtimes will encounter errors when attempting to query these tables.^[create-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [Deletion vectors in Databricks](/concepts/deletion-vectors-in-delta-lake.md) – Detailed documentation on enabling and using deletion vectors.
- Rename and drop columns with Delta Lake column mapping – Column mapping feature guide.
- [Delta Sharing](/concepts/delta-sharing.md) – The technology underlying OpenSharing.
- [Delta Lake](/concepts/delta-lake.md) – The open format that supports these features.
- [History sharing](/concepts/table-history-sharing.md) – The prerequisite for sharing tables with these features.
- [OpenSharing](/concepts/opensharing.md) – The sharing protocol used to distribute Delta tables.

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
