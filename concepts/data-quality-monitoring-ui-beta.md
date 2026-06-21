---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ca171a2ec33569ff2fa51ff92db3660560f61ca4b4866ab815455e74ac5e1110
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-quality-monitoring-ui-beta
    - DQMU(
    - Data Quality Monitoring Dashboard
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Data Quality Monitoring UI (Beta)
description: A Beta UI feature in Databricks Catalog Explorer that provides a visual interface for viewing data quality results and managing alert rules without leaving the page.
tags:
  - ui
  - beta
  - data-quality
  - unity-catalog
timestamp: "2026-06-18T10:45:12.385Z"
---

# Data Quality Monitoring UI (Beta)

The **Data Quality Monitoring UI** is a graphical interface within Catalog Explorer that lets you create and manage alerts for [Anomaly Detection](/concepts/anomaly-detection.md) without leaving the page. It is currently in Beta and is visible to all users by default — workspace admins do not need to enable it from the **Previews** page. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Capabilities

From the Data Quality Monitoring UI you can:

- View the health status of monitored tables in a schema.
- Create alert rules that notify selected workspace users by email when a monitored table becomes unhealthy.
- Edit the scope and recipients of existing alert rules.
- Delete alert rules.

Each alert rule is scoped to a catalog or a specific schema. When a monitored table within that scope becomes unhealthy, each recipient receives one email per important unhealthy table. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Required permissions

The privileges required to create or manage an alert rule depend on the rule's scope:

- To create a schema‑level alert, you must have the `MANAGE` privilege on the schema.
- To create a catalog‑level alert, you must have the `MANAGE` privilege on the catalog.

^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Accessing the UI

1. In Catalog Explorer, navigate to a schema where [Data Quality Monitoring](/concepts/data-quality-monitoring.md) is enabled.
2. Click the **Details** tab.
3. Next to **Data Quality Monitoring**, click **View results**.

This opens the Data Quality Monitoring UI. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Managing alerts

### Viewing alert rules

In the upper‑right corner of the Data Quality Monitoring UI, click **Manage alerts**. A popover opens showing your existing alert rules, including the catalog, schema, and number of recipients for each rule. From this popover you can create a new alert, edit an existing rule, or delete a rule. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Creating an alert

1. Click **Manage alerts** to open the alerts popover.
2. Click **Create alert**.
3. Configure the alert rule:
   - **Catalog**: Select the catalog to monitor.
   - **Schema**: Select a specific schema, or select **All Schemas** to create a catalog‑level alert covering every schema in the catalog.
   - **Notify**: Search for and select one or more workspace users to notify by email.
4. Click **Save**.

The alert rule is now active. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Related concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) — The underlying mechanism that identifies data quality issues
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — Overall framework for monitoring data quality in Unity Catalog
- [Catalog Explorer](/concepts/catalog-explorer.md) — The workspace UI where the Data Quality Monitoring UI is accessed
- Alerts for Anomaly Detection — Alternative approach using Databricks SQL alerts

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
