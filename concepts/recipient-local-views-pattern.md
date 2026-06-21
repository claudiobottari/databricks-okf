---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 08186d839bc4707b4fb3399df624af7de9236dbdd0444e02c67f9fc2abadb3dc
  pageDirectory: concepts
  sources:
    - opensharing-and-abac-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-local-views-pattern
    - RVP
  citations:
    - file: opensharing-and-abac-databricks-on-aws.md
title: Recipient-Local Views Pattern
description: A pattern where providers share only base tables (not views) and recipients create local views over the shared tables in a separate schema, allowing ABAC policies on the shared tables to be respected when accessed through those views.
tags:
  - architecture
  - unity-catalog
  - delta-sharing
timestamp: "2026-06-19T19:50:27.147Z"
---

## Recipient-Local Views Pattern

The **Recipient-Local Views Pattern** is a data-sharing architecture for [OpenSharing](/concepts/opensharing.md) (Delta Sharing) that enables recipients to enforce [ABAC (Attribute-Based Access Control)](/concepts/abac-attribute-based-access-control.md) policies on shared data while preserving the ability to consume that data through views. Instead of the provider sharing views directly (which cannot have ABAC policies), the provider shares only the underlying base tables, and the recipient creates views locally over those shared tables. ^[opensharing-and-abac-databricks-on-aws.md]

### Motivation

ABAC policies — such as [Row Filters](/concepts/row-filter-policies.md) and Column Masks — can only be applied to tables, not to views. If a provider shares a view, the recipient cannot attach ABAC policies to it. The Recipient-Local Views Pattern solves this by having the recipient:

1. Receive the base tables via OpenSharing.
2. Apply ABAC policies on the shared tables (which are read-only but can have policies).
3. Create local views over the shared tables in a separate schema.

This ensures that when recipient users query the views, the ABAC policies on the underlying shared tables are respected. ^[opensharing-and-abac-databricks-on-aws.md]

### How It Works

1. **Provider shares only base tables**, not views. The shared tables appear in a read-only delta share schema on the recipient side. ^[opensharing-and-abac-databricks-on-aws.md]
2. **Recipient applies ABAC policies** to the shared tables (e.g., row filters, column masks) to control access for recipient-side users. ^[opensharing-and-abac-databricks-on-aws.md]
3. **Recipient creates views in a separate schema** (not the delta share schema, which is read-only). For example: ^[opensharing-and-abac-databricks-on-aws.md]

```sql
-- Recipient: apply ABAC policy to the shared table
CREATE POLICY hide_eu_customers
ON CATALOG recipient_catalog
ROW FILTER hide_eu
TO `account users`
EXCEPT 'recipient_admins'
FOR TABLES
MATCH COLUMNS has_tag('geo_region') AS region
USING COLUMNS (region);

-- Create a view in a separate schema (delta share schema is read-only)
CREATE VIEW recipient_catalog.analytics.employees_view AS
  SELECT * FROM recipient_catalog.delta_share_schema.employees;
```

After this setup, queries against `recipient_catalog.analytics.employees_view` automatically enforce the row filter defined on the underlying shared table. ^[opensharing-and-abac-databricks-on-aws.md]

### Prerequisites

- Databricks Runtime 16.4 or above (or Serverless Compute). ^[opensharing-and-abac-databricks-on-aws.md]
- OpenSharing must be configured between provider and recipient. ^[opensharing-and-abac-databricks-on-aws.md]
- The share owner must be **exempt from ABAC policies** on the provider side (via `EXCEPT` clause) so that the recipient receives unfiltered data. Without this exemption, the provider’s policies would filter data before it reaches the recipient. ^[opensharing-and-abac-databricks-on-aws.md]
- Recipient needs appropriate permissions to create policies and views (`MANAGE` on catalog/schema, `EXECUTE` on UDFs, etc.). ^[opensharing-and-abac-databricks-on-aws.md]

### Comparison to Direct View Sharing

| Aspect | Direct View Sharing | Recipient-Local Views Pattern |
|--------|---------------------|-------------------------------|
| ABAC policies | Cannot be applied on views | Policies applied on shared tables, respected through views |
| Share owner exemption | Required | Required |
| Recipient schema | Read-only delta share schema | Separate writable schema |
| Data control | Provider controls view logic | Recipient controls access policies |

The pattern is recommended when the recipient needs to enforce their own data access rules on top of shared data and still consume it through views. ^[opensharing-and-abac-databricks-on-aws.md]

### Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The Delta Sharing protocol used to share tables and views.
- [ABAC (Attribute-Based Access Control)](/concepts/abac-attribute-based-access-control.md) — Access control using row filters and column masks.
- [Unity Catalog](/concepts/unity-catalog.md) — The catalog system that governs ABAC policies.
- [Row Filters](/concepts/row-filter-policies.md) — A type of ABAC policy that filters rows based on conditions.
- Column Masks — A type of ABAC policy that masks sensitive column values.
- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for sharing data across platforms.

### Sources

- opensharing-and-abac-databricks-on-aws.md

# Citations

1. [opensharing-and-abac-databricks-on-aws.md](/references/opensharing-and-abac-databricks-on-aws-143be106.md)
