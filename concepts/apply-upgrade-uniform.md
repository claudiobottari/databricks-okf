---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3b4e20f4117e90e40636a11e8b28811855f76bfc58df4d6b83b9ae07db78eafc
  pageDirectory: concepts
  sources:
    - reorg-table-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - apply-upgrade-uniform
    - A(U
  citations:
    - file: reorg-table-databricks-on-aws.md
title: APPLY (UPGRADE UNIFORM)
description: A REORG TABLE subcommand that upgrades a Delta table to a specified Apache Iceberg version (1 or 2) for Iceberg compatibility.
tags:
  - iceberg
  - delta-lake
  - table-upgrade
  - uniform
timestamp: "2026-06-19T20:13:18.062Z"
---

# APPLY (UPGRADE UNIFORM)

**APPLY (UPGRADE UNIFORM)** is a clause within the `REORG TABLE` SQL statement on Databricks that rewrites a Delta table’s files to upgrade its underlying Apache Iceberg compatibility format. It is used to enable or update the table’s Uniform (Iceberg) format so that the table can be read by Iceberg-compatible engines.

## Syntax

```sql
REORG TABLE table_name APPLY ( UPGRADE UNIFORM ( ICEBERG_COMPAT_VERSION = version ) )
```

The `version` parameter must be either `1` or `2`. ^[reorg-table-databricks-on-aws.md]

## Overview

`APPLY (UPGRADE UNIFORM)` is part of the `REORG TABLE` command, which reorganizes Delta Lake tables. When a table has been configured for [Delta Lake Uniform](/concepts/delta-uniform.md) (Iceberg compatibility), this clause forces a rewrite of all table files to conform to the specified Iceberg compatibility version. Metadata-only deletes are not sufficient for upgrading the Uniform format; the files themselves must be rewritten to include the Iceberg metadata required by the target version. ^[reorg-table-databricks-on-aws.md]

## Behavior

- **File rewriting:** Unlike `APPLY (PURGE)`, which only rewrites files containing soft‑deleted data, `APPLY (UPGRADE UNIFORM)` **may rewrite all files** in the table to ensure every file carries the correct Iceberg compatibility markers. ^[reorg-table-databricks-on-aws.md]
- **Idempotence:** `REORG TABLE` is idempotent—running the command twice on the same dataset has no effect. If the table is already at the requested Iceberg version, the second run does nothing. ^[reorg-table-databricks-on-aws.md]
- **Applicability:** This clause applies to **Databricks SQL** and **Databricks Runtime 14.3 and above**. ^[reorg-table-databricks-on-aws.md]

## Version Selection

The `ICEBERG_COMPAT_VERSION` parameter accepts:

- `1` – Upgrade to Iceberg format v1.
- `2` – Upgrade to Iceberg format v2 (adds support for row‑level deletes, etc.).

The table must already be enabled for Uniform before running this command. If a table has never been configured for Uniform, use `ALTER TABLE` to enable the feature first.

## Related Concepts

- [REORG TABLE](/concepts/reorg-table.md) – The parent command that contains the `APPLY (UPGRADE UNIFORM)` clause.
- [Delta Lake Uniform](/concepts/delta-uniform.md) – The feature that allows Delta tables to be read as Iceberg tables.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The open table format that Uniform targets.
- VACUUM – Used after `REORG` to physically remove old files that are no longer needed.

## Sources

- reorg-table-databricks-on-aws.md

# Citations

1. [reorg-table-databricks-on-aws.md](/references/reorg-table-databricks-on-aws-58d61683.md)
