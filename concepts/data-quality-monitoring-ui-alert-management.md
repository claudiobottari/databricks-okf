---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d420d5d3267a65eed70388abb29c279df70aa079c3e5efd0c0de2a5ef1abda59
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-quality-monitoring-ui-alert-management
    - DQMUAM
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Data Quality Monitoring UI Alert Management
description: Beta feature for creating and managing anomaly detection alert rules directly from the Data Quality Monitoring UI in Catalog Explorer, scoped to catalogs or schemas.
tags:
  - databricks
  - ui
  - alerting
  - beta
timestamp: "2026-06-19T22:04:19.393Z"
---

```markdown
---
title: Data Quality Monitoring UI Alert Management
summary: A Beta feature in Databricks that allows users to create, view, and manage anomaly detection alert rules directly from the Data Quality Monitoring UI without leaving the page.
sources:
  - alerts-for-anomaly-detection-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:23:56.985Z"
updatedAt: "2026-06-19T08:57:31.122Z"
tags:
  - databricks
  - ui
  - beta
  - alert-management
aliases:
  - data-quality-monitoring-ui-alert-management
  - DQMUAM
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Data Quality Monitoring UI Alert Management

**Data Quality Monitoring UI Alert Management** refers to the process of creating, viewing, and managing alert rules directly within the Data Quality Monitoring UI (Beta) in Databricks. These alerts notify workspace users when anomaly detection identifies a data quality issue — such as a stale table or an unexpected drop in row count — allowing teams to respond quickly to problems without leaving the monitoring interface. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Overview

Alert rules are scoped to a catalog or a specific schema. When a monitored table within the rule's scope becomes unhealthy, each configured recipient receives one email per important unhealthy table. You can work with alerts from the Data Quality Monitoring UI, or alternatively create more advanced alerts by querying the anomaly detection output system table using Databricks SQL. This page focuses on the UI-based approach. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Required Permissions

The privileges required to create or manage an alert rule depend on the rule's scope:

- To create a **schema-level** alert, you must have the `MANAGE` privilege on that schema.
- To create a **catalog-level** alert, you must have the `MANAGE` privilege on that catalog.

^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Viewing and Managing Alerts in the UI

To view and manage existing alert rules:

1. Navigate to a schema in [[Catalog Explorer]]. Data quality monitoring must be enabled for that schema.
2. Click the **Details** tab. Next to **Data Quality Monitoring**, click **View results** to open the Data Quality Monitoring UI.
3. In the upper-right corner of the page, click **Manage alerts**. A popover opens listing existing alert rules, including the catalog, schema, and number of recipients for each rule.

From this popover you can:

- **Create** a new alert rule.
- **Edit** an existing alert to change its scope and recipients.
- **Delete** an alert.

^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Creating an Alert in the UI

To create a new alert rule:

1. In the upper-right corner of the Data Quality Monitoring UI, click **Manage alerts** to open the alerts popover.
2. Click **Create alert**.
3. Configure the alert rule:
   - **Catalog**: Select the catalog to monitor.
   - **Schema**: Select a specific schema, or select **All Schemas** to create a catalog-level alert that covers every schema in that catalog.
   - **Notify**: Search for and select one or more workspace users to notify by email.
4. Click **Save**.

The alert will begin monitoring the defined scope. When a table becomes unhealthy, each recipient receives a notification email. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Alternative: Alerts with Databricks SQL

For advanced filtering, custom notification templates, or queries against the system table `system.data_quality_monitoring.table_results`, you can create alerts using Databricks SQL. This approach requires appropriate access to the system table (by default only account admins can access it). See the full documentation for an example query and custom email template. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [[Anomaly detection]]
- [[Unity Catalog]]
- [[Data Quality Monitoring]]
- [[Catalog Explorer]]
- [[Databricks SQL Alerts]]
- System Tables

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md
```

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
