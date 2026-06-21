---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9e4240ad4ad2500ca5cdb799e167ef123e6be3572b40e09f133cf74eeaed83b8
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - column-masks-in-delta-lake
    - CMIDL
    - Column Masks (Databricks)
    - Column masking in Delta
    - Column masks in Databricks
  citations:
    - file: delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
title: Column Masks in Delta Lake
description: A Delta Lake table feature for dynamically masking column values at read time, which is incompatible with REFRESH SYNC UNIFORM.
tags:
  - delta-lake
  - security
  - column-level
timestamp: "2026-06-19T10:09:45.611Z"
---

Here is the wiki page for "Column Masks in Delta Lake", written based solely on the provided source material.

---

## Column masks in Delta Lake

**Column masks** are a Delta Lake security feature that controls which values a query can see in a specific column by rewriting the column's data at read time. This allows sensitive data—such as personally identifiable information (PII)—to be dynamically obscured for certain users without altering the underlying data in storage. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Overview

Column masks are typically implemented using a user-defined function (UDF) that returns either the original column value or a masked version. The masking logic is evaluated at query time, and the same column can display different values to different users depending on their access privileges. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Interaction with Delta Uniform

The `REFRESH` identifier `SYNC UNIFORM`, which synchronizes a Delta table's metadata to the [Delta Uniform](/concepts/delta-uniform.md) format, **does not support** column masks. Attempting to run `REFRESH SYNC UNIFORM` on a table that has column masks defined produces the error condition `DELTA_UNIFORM_REFRESH_NOT_SUPPORTED` with the reason `COLUMN_MASK`. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

The error message is:

```
COLUMN_MASK: Column mask is not supported by REFRESH identifier SYNC UNIFORM.
```

This limitation exists because the Delta Uniform format cannot represent column‑mask semantics. To use `REFRESH SYNC UNIFORM`, you must first drop or disable all column masks on the table. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Unity Catalog Implementation

In Unity Catalog, column masks can be implemented as [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md)—an [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) mechanism that applies a UDF to mask column contents based on governed tags and user attributes. These policies can be defined at catalog, schema, or table scope and automatically apply to all matching columns, making them reusable across many tables without per‑table configuration. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Related Concepts

- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) – attribute‑based policies that implement column masking in Unity Catalog
- [Column Mask Policies](/concepts/column-mask-policies.md) – the broader category of Unity Catalog security policies for column‑level masking
- [Delta Lake](/concepts/delta-lake.md) – the open‑source storage layer that supports column masks
- [Delta Uniform](/concepts/delta-uniform.md) – the format interoperability layer that does not support column masks
- DELTA_UNIFORM_REFRESH_NOT_SUPPORTED error class|DELTA_UNIFORM_REFRESH_NOT_SUPPORTED error condition – the error class that includes the `COLUMN_MASK` reason
- [Row Filters and Column Masks (table-level)](/concepts/row-filters-and-column-masks.md) – the alternative per‑object approach for column masking

## Sources

- delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md

# Citations

1. [delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_not_supported-error-condition-databricks-on-aws-9dd3f333.md)
2. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
