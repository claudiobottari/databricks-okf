---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8d79cfaa9a8b13d4990d4587d7ab2a40b8787be39f63329d390ae61e137a3ef6
  pageDirectory: concepts
  sources:
    - unity-catalog-requirements-and-limitations-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-securable-object-naming-constraints
    - UCSONC
  citations:
    - file: unity-catalog-requirements-and-limitations-databricks-on-aws.md
title: Unity Catalog Securable Object Naming Constraints
description: Object names in Unity Catalog are limited to 255 characters, stored as lowercase, and cannot contain periods, spaces, forward slashes, or ASCII control characters.
tags:
  - unity-catalog
  - naming
  - limitations
timestamp: "2026-06-19T23:15:14.211Z"
---

# [Unity Catalog](/concepts/unity-catalog.md) Securable Object Naming Constraints

**Unity Catalog Securable Object Naming Constraints** define the rules and limitations for naming securable objects — such as catalogs, schemas, tables, views, and functions — within [Unity Catalog](/concepts/unity-catalog.md) on Databricks. These constraints ensure consistent naming across the [Metastore](/concepts/metastore.md) and prevent conflicts.

## Character and Length Restrictions

All object names in [Unity Catalog](/concepts/unity-catalog.md) are subject to the following limitations:

- **Maximum length**: Object names cannot exceed 255 characters. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]
- **Prohibited characters**:
  - Period (`.`)
  - Space ( )
  - Forward slash (`/`)
  - All ASCII control characters (00-1F hex)
  - The DELETE character (7F hex)

^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

## Case Handling

[Unity Catalog](/concepts/unity-catalog.md) stores all object names as lowercase, regardless of how they are specified during creation. When referencing [Unity Catalog](/concepts/unity-catalog.md) names in SQL statements that contain special characters such as hyphens (`-`), you must escape the name with backticks. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

## Column Name Handling

Column names have slightly different rules than other securable objects:

- Column names can include special characters, but the name must be escaped with backticks in all SQL statements when special characters are used. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]
- [Unity Catalog](/concepts/unity-catalog.md) preserves the original casing of column names. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]
- Queries against [Unity Catalog](/concepts/unity-catalog.md) tables are case-insensitive for column references. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that enforces these naming constraints.
- [Unity Catalog Securable Objects](/concepts/unity-catalog-securable-objects.md) — The objects (catalogs, schemas, tables, etc.) subject to these naming rules.
- Databricks SQL — The query language used to interact with [Unity Catalog](/concepts/unity-catalog.md) objects.
- Unity Catalog Requirements and Limitations — Broader requirements for compute, file formats, and known limitations.

## Sources

- unity-catalog-requirements-and-limitations-databricks-on-aws.md

# Citations

1. [unity-catalog-requirements-and-limitations-databricks-on-aws.md](/references/unity-catalog-requirements-and-limitations-databricks-on-aws-0188dbe0.md)
