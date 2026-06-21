---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ff69e4a6e93a92e7f196efe289e2e40e3938896368c3ed874fc39baa49bb691b
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - alert-rule-permissions-model
    - ARPM
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Alert Rule Permissions Model
description: "Privilege requirements for creating and managing anomaly detection alert rules: MANAGE privilege on the schema for schema-level alerts, MANAGE privilege on the catalog for catalog-level alerts."
tags:
  - databricks
  - permissions
  - unity-catalog
  - rbac
timestamp: "2026-06-19T22:04:39.378Z"
---

# Alert Rule Permissions Model

The **Alert Rule Permissions Model** defines the [Unity Catalog](/concepts/unity-catalog.md) privileges required to create and manage alert rules for anomaly detection in the Data Quality Monitoring UI. These alert rules notify workspace users by email when a monitored table becomes unhealthy within a catalog or schema. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Required Privileges

The privileges required to create or manage an alert rule depend entirely on the rule's scope. There are two levels: catalog-level and schema-level. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Schema-Level Scope

To create a schema-level alert, you must have the `MANAGE` privilege on the specific schema. This scope restricts the alert to monitor tables only within that single schema. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Catalog-Level Scope

To create a catalog-level alert, you must have the `MANAGE` privilege on the entire catalog. This scope covers every schema within the catalog. When creating an alert through the UI, selecting "All Schemas" creates a catalog-level alert. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Creating and Managing Alerts

Users configure alert rules directly from the Data Quality Monitoring UI. To create an alert:

1. Navigate to a schema in [Catalog Explorer](/concepts/catalog-explorer.md) where data quality monitoring is enabled.
2. Click the **Details** tab, then **View results** next to **Data Quality Monitoring**.
3. In the upper-right corner, click **Manage alerts**.
4. Click **Create alert** and configure the rule.
5. Select the **Catalog** and **Schema** (or "All Schemas" for a catalog-level alert).
6. Select one or more workspace users to notify by email.
7. Click **Save**. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

The UI enforces that only users with the appropriate `MANAGE` privilege can create or modify alert rules at the corresponding scope. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Notification Behavior

When a monitored table within the rule's scope becomes unhealthy, each recipient receives one email per important unhealthy table. This ensures that users are notified promptly without receiving excessive duplicate alerts for the same incident. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) — The monitoring system that generates the health status triggering alerts.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The broader framework for monitoring table health.
- [Unity Catalog](/concepts/unity-catalog.md) — The catalog and schema objects where [MANAGE Privilege](/concepts/manage-privilege.md) is required.
- [Catalog Explorer](/concepts/catalog-explorer.md) — The UI tool for navigating to alert configuration.

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
