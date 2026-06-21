---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cb35b39ae0d5369777cd74b4762145234c9228a8282efe5fe4e537530fa45952
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-quality-monitoring-ui
    - DQMU
    - Data Quality Monitoring Results UI
    - Data quality monitoring results UI
    - data quality monitoring results UI
    - Create a monitor UI
    - data-quality-monitoring-ui-alert-management
    - DQMUAM
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Data Quality Monitoring UI
description: A Databricks interface (Beta) for creating and managing anomaly detection alert rules directly within the Data Quality Monitoring page, including scope and recipient configuration.
tags:
  - data-quality
  - monitoring
  - user-interface
  - databricks
timestamp: "2026-06-19T17:31:54.636Z"
---

## Data Quality Monitoring UI

The **Data Quality Monitoring UI** is a Beta feature in Databricks that allows users to create and manage anomaly detection alerts directly from the user interface, without leaving the page. It provides a visual way to configure alert rules that notify selected workspace users by email when a monitored table within a specified catalog or schema is detected as unhealthy. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

The UI is visible to all users by default; workspace administrators do not need to enable it from the **Previews** page. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Required Permissions

The privileges required to create or manage an alert rule depend on the rule's scope:

- To create a **schema-level alert**, the user must have the `MANAGE` privilege on the schema.
- To create a **catalog-level alert**, the user must have the `MANAGE` privilege on the catalog.

^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Viewing and Managing Alerts

To access the Data Quality Monitoring UI and manage alert rules:

1. Navigate to a schema in [Catalog Explorer](/concepts/catalog-explorer.md). Data quality monitoring must be enabled for that schema.
2. Click the **Details** tab. Next to **Data Quality Monitoring**, click **View results**. This opens the Data Quality Monitoring UI.
3. In the upper-right corner of the page, click **Manage alerts**. A popover opens showing existing alert rules, including the catalog, schema, and number of recipients for each rule.

From this popover, users can create a new alert rule, select an existing alert to edit its scope and recipients, or delete the alert. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Creating an Alert

To create an alert from the Data Quality Monitoring UI:

1. Open the **Manage alerts** popover as described above.
2. Click **Create alert**.
3. Configure the alert rule:
   - **Catalog**: Select the catalog to monitor.
   - **Schema**: Select a specific schema, or select **All Schemas** to create a catalog-level alert that covers every schema in the catalog.
   - **Notify**: Search for and select one or more workspace users to notify by email.
4. Click **Save**.

After creation, the rule will send an email notification for each important unhealthy table detected within its scope. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) – The underlying system that flags unhealthy tables.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – Broader framework for monitoring table health.
- Alert Rules – Configurable triggers for notifications.
- [Catalog Explorer](/concepts/catalog-explorer.md) – UI tool for navigating Unity Catalog objects.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) hosting schemas and tables.
- Email Notifications – Delivery mechanism for alert messages.
- Beta – Release stage of this feature.

### Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
