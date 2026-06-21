---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b933d65db2ce81e634661d8f8b197a52ec8a63b43ddfcedc43bcd9d2eeb2fce2
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - alert-rule-scoping-catalog-vs-schema
    - ARS(VS
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Alert Rule Scoping (Catalog vs Schema)
description: Alert rules in Unity Catalog Data Quality Monitoring can be scoped to an entire catalog (all schemas) or a specific schema, controlling which monitored tables are covered.
tags:
  - unity-catalog
  - data-quality
  - authorization
timestamp: "2026-06-18T10:44:51.032Z"
---

# Alert Rule Scoping (Catalog vs Schema)

Alert rules for [Anomaly Detection](/concepts/anomaly-detection.md) in Unity Catalog’s Data Quality Monitoring are scoped to either a **catalog** or a **specific schema** within that catalog. The scope determines which monitored tables are evaluated for health status and which principals must hold the `MANAGE` privilege to create or manage the rule.^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Scope Options

When creating an alert rule from the Data Quality Monitoring UI, you first select a **Catalog** and then either:

- A specific **Schema** – the rule covers only tables in that schema (schema-level rule).
- **All Schemas** – the rule covers every schema in the selected catalog (catalog-level rule).^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Required Privileges

The `MANAGE` privilege is required on the securable object that matches the rule’s scope:

| Rule scope             | Required privilege           |
| ---------------------- | ---------------------------- |
| Schema-level alert     | `MANAGE` on the schema       |
| Catalog-level alert    | `MANAGE` on the catalog      |

If the scope is a schema, the creator needs `MANAGE` only on that schema, not on the parent catalog. If the scope is the entire catalog, `MANAGE` on the catalog is required.^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Creating a Scoped Alert (UI)

1. Open a schema in [Catalog Explorer](/concepts/catalog-explorer.md) where data quality monitoring is enabled.
2. Click the **Details** tab, then next to **Data Quality Monitoring**, click **View results** to open the Data Quality Monitoring UI.
3. Click **Manage alerts** (top right).
4. Click **Create alert**.
5. Configure the scope:
   - **Catalog**: choose the catalog that contains the tables of interest.
   - **Schema**: choose a specific schema or select **All Schemas** for a catalog-level rule.
6. Select one or more recipients under **Notify** (workspace users who will receive email notifications).
7. Click **Save**.^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Scoping via Databricks SQL Alerts

You can also create alerts by querying `system.data_quality_monitoring.table_results` using Databricks SQL. In this approach, the scope is implicit in the query’s `WHERE` clause—for example, by filtering on `catalog_name` and `schema_name`. The alert trigger condition is defined in the SQL alert editor. This method supports advanced filtering and custom notification templates, but does not enforce the same `MANAGE`-based scope boundaries as the UI; the query determines which results are evaluated.^[alerts-for-anomaly-detection-databricks-on-aws.md]

> Note: Access to `system.data_quality_monitoring.table_results` is restricted to [account admin](/concepts/account-admin-unity-catalog.md) by default; grant appropriate access if other users need to configure SQL alerts.

## Best Practices

- **Choose the smallest scope** that contains the tables you want to monitor. Schema-level rules limit the blast radius of privilege assignments and make it easier to delegate alert management to schema owners.
- **Use catalog-level rules** when you want a central governance team to monitor the entire catalog, and the team already holds `MANAGE` on the catalog.
- **Avoid overlapping scopes**. If you have both a catalog-level rule and a schema-level rule for the same schema, recipients may receive duplicate notifications for the same unhealthy table.

## See Also

- [Anomaly Detection](/concepts/anomaly-detection.md) – Overview of data quality anomaly detection in Unity Catalog
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – Enabling and viewing monitoring results
- [Unity Catalog](/concepts/unity-catalog.md) – Data governance layer for securable objects
- [MANAGE Privilege](/concepts/manage-privilege.md) – Required for alert rule CRUD operations
- [Catalog Explorer](/concepts/catalog-explorer.md) – UI for managing [Catalog and Schema](/concepts/catalog-and-schema.md) objects
- [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) – Creating alerts from SQL queries

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
