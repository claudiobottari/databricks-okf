---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c94c842e4907e17d0a9c249527e48525a64f6670c7752ed1c6dab2cfdc8112de
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dynamic-views-for-recipient-scoped-access-control
    - DVFRAC
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Dynamic Views for Recipient-Scoped Access Control
description: Using dynamic views with the CURRENT_RECIPIENT() function to configure fine-grained access control at row and column levels based on recipient properties. Enables data masking and security by restricting recipient access according to properties specified in the recipient definition. Requires Databricks Runtime 14.2+.
tags:
  - delta-sharing
  - access-control
  - dynamic-views
  - security
timestamp: "2026-06-19T18:02:18.232Z"
---

---
title: Dynamic Views for Recipient-Scoped Access Control
summary: Dynamic views in OpenSharing allow fine-grained row-level and column-level access control and data masking based on recipient properties using the CURRENT_RECIPIENT() function.
sources:
  - create-shares-for-opensharing-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T15:00:00.000Z"
updatedAt: "2026-06-19T15:00:00.000Z"
tags:
  - databricks
  - delta-sharing
  - opensharing
  - access-control
  - dynamic-views
aliases:
  - dynamic-views-for-recipient-scoped-access-control
  - DVRSA
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Dynamic Views for Recipient-Scoped Access Control

**Dynamic Views for Recipient-Scoped Access Control** is a feature of [OpenSharing](/concepts/opensharing.md) on Databricks that lets you control exactly which rows and columns a recipient can see when querying a shared view. Using the `CURRENT_RECIPIENT()` SQL function inside the view definition, you can enforce row-level security, column-level security, and data masking based on properties of the recipient. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Overview

When you share a Dynamic View that uses `CURRENT_RECIPIENT()`, the view evaluates the recipient's properties — both default properties (such as `databricks.accountId`, `databricks.metastoreId`, and `databricks.name`) and any custom properties you define — and filters or masks the data accordingly. This enables a single view to serve multiple recipients, each seeing only the data they are permitted to access. ^[create-shares-for-opensharing-databricks-on-aws.md]

The approach is an extension of [View Sharing](/concepts/delta-sharing.md) and is configured when you add a dynamic view to a share. Dynamic views can be used for:

- [Row-Level Security](/concepts/row-level-security-rls-policies.md) – restrict access to specific rows.
- Column-Level Security – hide or mask sensitive columns.
- [Data Masking](/concepts/conditional-column-masking.md) – obfuscate data values based on recipient attributes.

## How It Works

To create a recipient-scoped dynamic view, define a view in your Unity Catalog [Metastore](/concepts/metastore.md) that includes calls to `CURRENT_RECIPIENT()`. For example, a view on a sales table might filter rows so that each recipient only sees records for their own country:

```sql
CREATE VIEW shared_sales AS
SELECT *
FROM sales
WHERE country = CURRENT_RECIPIENT().country;
```

When the recipient queries the share, Databricks evaluates `CURRENT_RECIPIENT().country` using the recipient's stored properties. The recipient never sees the properties or the filtering logic — only the filtered result set. ^[create-shares-for-opensharing-databricks-on-aws.md]

You can also combine conditions for more granular control, such as restricting both rows and columns:

```sql
CREATE VIEW recipient_filtered AS
SELECT
  CASE
    WHEN CURRENT_RECIPIENT().role = 'manager' THEN employee_salary
    ELSE NULL
  END AS salary_masked,
  employee_id,
  department
FROM employees
WHERE department = CURRENT_RECIPIENT().department;
```

Recipient properties are set when you [Manage recipients](/concepts/data-recipient.md) in OpenSharing. Default properties include:

| Property | Description |
|---|---|
| `databricks.accountId` | Databricks account of the recipient (Databricks-to-Databricks only) |
| `databricks.metastoreId` | Unity Catalog [Metastore](/concepts/metastore.md) of the recipient (Databricks-to-Databricks only) |
| `databricks.name` | Recipient display name |

You can also add custom properties such as `country`, `department`, or `role` at recipient creation time. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Requirements

- The view must be added to a share using a SQL warehouse or compute running Databricks Runtime 13.3 LTS or above.
- The `CURRENT_RECIPIENT()` function requires Databricks Runtime 14.2 or above on the compute that evaluates the view definition.
- Standard [View Sharing](/concepts/delta-sharing.md) requirements apply, including that the view must be defined on Delta tables, other shareable views, or local materialized views and streaming tables (not on foreign tables). ^[create-shares-for-opensharing-databricks-on-aws.md]

## Limitations

- All View Sharing limitations apply to dynamic views. Specifically:
  - You cannot share views that reference shared tables or shared views.
  - You cannot share views that reference foreign tables, including foreign Iceberg tables.
- If the recipient does not have direct access to the underlying data (for example, when using Databricks-to-Open sharing), `LIMIT` clauses and predicate pushdown are not supported. The system fully materializes all query results before returning them to the recipient, regardless of any query filters. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The overall data-sharing protocol on Databricks.
- [View Sharing](/concepts/delta-sharing.md) – Sharing read-only views with recipients.
- CURRENT_RECIPIENT Function – SQL function that returns the current recipient's properties.
- Manage Recipients – How to create and configure recipients and their properties.
- [Row-Level Security](/concepts/row-level-security-rls-policies.md) – A broader security model for restricting data access.
- Column-Level Security – Techniques for hiding or masking columns.

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
