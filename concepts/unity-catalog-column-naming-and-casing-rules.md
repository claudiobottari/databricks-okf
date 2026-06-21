---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5baa37c7e6d0761e130f54fad702ce5c55623e2885926d54d9355399ad7fb839
  pageDirectory: concepts
  sources:
    - unity-catalog-requirements-and-limitations-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-column-naming-and-casing-rules
    - Casing Rules and Unity Catalog Column Naming
    - UCCNACR
  citations:
    - file: unity-catalog-requirements-and-limitations-databricks-on-aws.md
title: Unity Catalog Column Naming and Casing Rules
description: Column names in Unity Catalog can use special characters if escaped with backticks; column casing is preserved but queries are case-insensitive.
tags:
  - unity-catalog
  - naming
  - sql
timestamp: "2026-06-19T23:15:23.569Z"
---

## [Unity Catalog](/concepts/unity-catalog.md) Column Naming and Casing Rules

**Unity Catalog Column Naming and Casing Rules** define how column names must be structured in [Unity Catalog](/concepts/unity-catalog.md) tables. These rules include a 255‑character limit, restricted characters for most securable objects, a special allowance for columns to use certain special characters when properly escaped, and the behavior of casing in queries. All rules apply to columns stored in Unity Catalog–managed and external tables.

### General Naming Constraints for Securable Objects

[Unity Catalog](/concepts/unity-catalog.md) imposes the following naming constraints on all securable objects, including columns:

- Object names **cannot exceed 255 characters**.
- The following characters are **not allowed**:
  - Period (`.`)
  - Space ( )
  - Forward slash (`/`)
  - All ASCII control characters (0x00–0x1F)
  - The DELETE character (0x7F)
- [Unity Catalog](/concepts/unity-catalog.md) stores **all object names as lowercase** internally. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

When referencing any [Unity Catalog](/concepts/unity-catalog.md) name in SQL statements that contains special characters — such as hyphens (`-`) — the name must be **escaped with backticks**. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

### Column‑Specific Rules

Columns have a special exception to the general special‑character restriction: **column names may contain special characters** (e.g., spaces, hyphens, or periods), provided they are **escaped with backticks in every SQL statement** that references them. This exception does not extend to other object types like schemas or tables. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

[Unity Catalog](/concepts/unity-catalog.md) **preserves the casing** of column names as originally defined. However, **queries against [Unity Catalog](/concepts/unity-catalog.md) tables are case‑insensitive** — both `SELECT colA` and `SELECT cola` reference the same column. This means column names are stored in the original case but cannot be relied upon for case‑sensitive matching in SQL. ^[unity-catalog-requirements-and-limitations-databricks-on-aws.md]

### Practical Implications

- When a column name contains a space, hyphen, or other disallowed character (from the general list), the column must always be wrapped in backticks: ``SELECT `my‑column` FROM table``.
- Because queries are case‑insensitive, you cannot create two columns in the same table that differ only by case (e.g., `ID` and `id`) — [Unity Catalog](/concepts/unity-catalog.md) will treat them as duplicates.
- The 255‑character maximum applies to column names as well.

### Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – Overview of the governance system.
- SQL escape rules – How backtick escaping works in Databricks SQL.
- Securable objects – Naming rules for schemas, tables, and other objects.
- Case sensitivity in Unity Catalog – Detailed behavior of case in identifiers.
- Unity Catalog limitations – Broader constraints and resource quotas.

### Sources

- unity-catalog-requirements-and-limitations-databricks-on-aws.md

# Citations

1. [unity-catalog-requirements-and-limitations-databricks-on-aws.md](/references/unity-catalog-requirements-and-limitations-databricks-on-aws-0188dbe0.md)
