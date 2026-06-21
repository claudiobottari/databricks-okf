---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 490afc277f9363298b4706026fa9aa90300d93ada872acb226f969e87e87333d
  pageDirectory: concepts
  sources:
    - create-table-clone-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - clone-table-limitations
    - CTL
  citations:
    - file: create-table-clone-databricks-on-aws.md
title: CLONE Table Limitations
description: Streaming tables and materialized views cannot be used as source or target tables for CLONE operations in Databricks.
tags:
  - limitations
  - streaming
  - materialized-views
timestamp: "2026-06-18T14:56:13.386Z"
---

# CLONE Table Limitations

**CLONE Table Limitations** describes the constraints that apply when using the `CREATE TABLE CLONE` statement (deep or shallow) on Databricks. These limitations affect the supported source and target table types, runtime versions, Unity Catalog integration, and naming conventions.

## Overview

The `CLONE` operation creates a copy of a source Delta, managed [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md), or Apache Parquet table. While the command supports both deep and shallow cloning, several restrictions exist depending on the table format, the Databricks Runtime version, and whether the table is managed by [Unity Catalog](/concepts/unity-catalog.md).^[create-table-clone-databricks-on-aws.md]

## Supported Source and Target Table Types

- **Managed Iceberg tables** support only **deep cloning**; shallow cloning is not permitted. Additionally, the table format cannot be changed during the clone operation.^[create-table-clone-databricks-on-aws.md]
- **Delta, Parquet, and foreign Iceberg tables** support both deep and shallow cloning.^[create-table-clone-databricks-on-aws.md]

## Unity Catalog and Shallow Clones

Shallow clone support for Unity Catalog managed tables depends on the Databricks Runtime version:

- **Databricks SQL and Databricks Runtime 13.3 LTS and above** — Shallow clones are supported for Unity Catalog managed tables.^[create-table-clone-databricks-on-aws.md]
- **Databricks Runtime 12.2 LTS and below** — Shallow clones are **not** supported in Unity Catalog.^[create-table-clone-databricks-on-aws.md]

## Streaming Tables and Materialized Views

Streaming Tables and [Materialized Views](/concepts/materialized-views-in-databricks.md) are **not supported** as source or target tables for any `CLONE` operation.^[create-table-clone-databricks-on-aws.md]

## Table Name Restrictions

- The target `table_name` must **not** include a temporal specification or options specification.^[create-table-clone-databricks-on-aws.md]
- If `table_name` is provided as a path instead of a table identifier, the operation **fails**. This applies when the `LOCATION path` clause is used to create an external table.^[create-table-clone-databricks-on-aws.md]

## Related Concepts

- [Deep Clone](/concepts/deep-clone.md) — Creates a fully independent copy of the source table.
- [Shallow Clone](/concepts/shallow-clone.md) — Creates a metadata-only copy that references the source data files.
- [CREATE TABLE CLONE](/concepts/create-table-clone-syntax.md) — Full syntax and parameter documentation.
- Clone a Table on Databricks — Best practices and use cases for cloning.
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer that affects shallow clone support.
- Streaming Tables and [Materialized Views](/concepts/materialized-views-in-databricks.md) — Table types not eligible for cloning.

## Sources

- create-table-clone-databricks-on-aws.md

# Citations

1. [create-table-clone-databricks-on-aws.md](/references/create-table-clone-databricks-on-aws-49def2a6.md)
