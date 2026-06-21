---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f2201a107910df37c47772bf4deaa37d2c8ab810f5b7df82f43dcca9926571a2
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - manage-privilege-for-data-quality-monitoring-alerts
    - MPFDQMA
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: MANAGE Privilege for Data Quality Monitoring Alerts
description: The MANAGE privilege on a schema or catalog is required to create or manage alert rules for data quality monitoring in Unity Catalog.
tags:
  - privileges
  - unity-catalog
  - data-quality
  - security
timestamp: "2026-06-18T10:45:05.326Z"
---

# MANAGE Privilege for Data Quality Monitoring Alerts

The **`MANAGE` privilege** is the required permission for creating and managing data quality monitoring alert rules in [Unity Catalog](/concepts/unity-catalog.md). Alert rules notify workspace users by email when anomaly detection identifies an unhealthy table within a catalog or schema. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Required Permissions by Scope

The privileges required to create or manage an alert rule depend on the rule's scope: ^[alerts-for-anomaly-detection-databricks-on-aws.md]

- To create a schema-level alert, you must have the **`MANAGE` privilege on the schema**.
- To create a catalog-level alert, you must have the **`MANAGE` privilege on the catalog**.

## Creating and Managing Alerts

### Using the Data Quality Monitoring UI (Beta)

The Data Quality Monitoring UI provides a graphical interface for creating and managing alert rules without leaving the page. This feature is in Beta and is visible to all users by default — workspace admins do not need to enable it from the **Previews** page. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

To view your alert rules:

1. Navigate to a schema in Catalog Explorer. Data quality monitoring must be enabled for this schema.
2. Click the **Details** tab. Next to **Data Quality Monitoring**, click **View results**.
3. In the upper-right corner, click **Manage alerts**.

From the **Manage alerts** popover, you can create a new alert rule, edit an existing rule's scope and recipients, or delete an alert. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

To create an alert:

1. Click **Manage alerts** to open the alerts popover.
2. Click **Create alert**.
3. Configure the alert rule:
   - **Catalog**: Select the catalog to monitor.
   - **Schema**: Select a specific schema, or select **All Schemas** to create a catalog-level alert that covers every schema in the catalog.
   - **Notify**: Search for and select one or more workspace users to notify by email.
4. Click **Save**. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Using Databricks SQL

You can also create alerts by querying the anomaly detection output system table. This approach supports advanced filtering and custom notification templates. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

By default, only account admins can access the system table `system.data_quality_monitoring.table_results`. If other users need to configure alerts, make sure to grant appropriate access. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## How Alerts Work

Each alert rule is scoped to a catalog or a specific schema. When a monitored table within the rule's scope becomes unhealthy, each recipient receives one email per important unhealthy table. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for managing data assets and permissions
- [Anomaly Detection](/concepts/anomaly-detection.md) — The system that identifies data quality issues triggering alerts
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The broader framework for monitoring data health
- [Account Admin](/concepts/account-admin-unity-catalog.md) — The role that can access the system table by default
- System Tables — The system tables that store anomaly detection results

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
