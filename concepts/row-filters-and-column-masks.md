---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9ae01cb7c1708b27eba28ce7b7cbdda62c31b7f1d9e759d81a5262e545a8f48e
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - row-filters-and-column-masks
    - Column Masks and Row Filters
    - RFACM
    - ABAC Row Filters and Column Masks
    - ABAC vs. Row Filters and Column Masks
    - ABAC for row filtering and column masking
    - Manually apply row filters and column masks
    - Row Filters and Column Masks (table-level)
    - Row Filters and Column Masks in Unity Catalog
    - Rules for multiple filters and masks
    - table-level-row-filters-and-column-masks
    - Column Masks and Table-Level Row Filters
    - TRFACM
    - ABAC vs Table-Level Row Filters and Column Masks
  citations:
    - file: access-control-in-unity-catalog-databricks-on-aws.md
title: Row Filters and Column Masks
description: Per-table UDF-based row and column level filters that control what data users see at query time in Unity Catalog.
tags:
  - access-control
  - unity-catalog
  - data-masking
  - row-filtering
timestamp: "2026-06-19T17:23:43.055Z"
---

```markdown
---
title: Row Filters and Column Masks
summary: Per-table row and column filters applied via UDFs to control what data users see at query time, recommended when ABAC is not adopted or per-table logic is needed.
sources:
  - access-control-in-unity-catalog-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:36:53.475Z"
updatedAt: "2026-06-19T13:50:37.385Z"
tags:
  - unity-catalog
  - filtering
  - masking
aliases:
  - row-filters-and-column-masks
  - Column Masks and Row Filters
  - RFACM
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Row Filters and Column Masks

**Row filters** and **column masks** are table-level access control mechanisms in [[Unity Catalog]] that restrict what data users can see within tables at query time. Row filters hide entire rows based on a condition; column masks obfuscate specific column values before returning results. These mechanisms are part of Unity Catalog’s **table-level filtering and masking** access control model, which uses table-specific filters and views to control data visibility within tables. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Comparison with ABAC

[[Attribute-based access control (ABAC)]] uses governed tags and centralized policies to control data access dynamically across many objects. Row filters and column masks, by contrast, are applied per table and require explicit configuration on each table. ^[access-control-in-unity-catalog-databricks-on-aws.md]

| Aspect | Row Filters / Column Masks | ABAC |
|---|---|---|
| **Granularity** | Per-table | Tag-driven, can span many tables |
| **Automation** | Manual per-table setup | Automatic when new tables are tagged |
| **Centralization** | Logic scattered across tables | Policies defined once at catalog/schema scope |

## When to Use Row Filters and Column Masks

Databricks recommends using [[attribute-based access control (ABAC)]] as the primary mechanism for fine-grained access control. Row filters and column masks should be used only when:

- Per-table logic is required that cannot be expressed through tag-based ABAC conditions.
- Your organization has not yet adopted ABAC. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [[Attribute-Based Access Control (ABAC)]] — The recommended, tag-driven approach for fine-grained access control.
- [[Unity Catalog]] — The data governance platform that provides both ABAC and table-level filtering/masking.
- [[Governed Tags]] — The mechanism used by ABAC policies to dynamically assign privileges based on tag values.
- Privileges in Unity Catalog — The base model for granting access to securable objects.
- [[Workspace-Catalog Binding]] — Restricts which workspaces can access specific catalogs, external locations, and storage credentials.

## Sources

- access-control-in-unity-catalog-databricks-on-aws.md
```

# Citations

1. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)
