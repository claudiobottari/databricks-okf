---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5b7d3aa035e93e7958a4d2c523221ccf214fd72f230dc7bbbef68e41c31adc8c
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - incident-management-for-data-quality
    - IMFDQ
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Incident Management for Data Quality
description: Workflow for reviewing and managing unhealthy table incidents, including assigning ownership to indicate active investigation and marking incidents as false positives (not an issue), with assignments and dismissals persisting for 7 days.
tags:
  - data-quality
  - workflow
  - incident-management
timestamp: "2026-06-19T08:59:51.320Z"
---

# Incident Management for Data Quality

**Incident Management for Data Quality** refers to the structured process of identifying, investigating, resolving, and monitoring data quality issues (incidents) that are detected in Unity Catalog tables through [Anomaly Detection](/concepts/anomaly-detection.md) and other [Data Quality Monitoring](/concepts/data-quality-monitoring.md) capabilities. The framework provides tools for classifying incidents, managing their lifecycle, and tracking resolutions.

## Incident Lifecycle

### Detection and Classification

When [Anomaly Detection](/concepts/anomaly-detection.md) is enabled on a schema in Unity Catalog, a background job monitors tables for **freshness** (how recently a table has been updated) and **completeness** (expected row count over the last 24 hours). If a table fails either check, it is classified as an "unhealthy" incident and appears in the **Unhealthy** tab of the [Data Quality Monitoring UI](/concepts/data-quality-monitoring-ui.md). ^[anomaly-detection-databricks-on-aws.md]

Incidents can also include **percent null** violations – when the percentage of null values in a column over the last 24 hours exceeds the predicted upper bound, indicating a completeness issue. ^[anomaly-detection-databricks-on-aws.md]

### Incident Review and Triage

From the **Unhealthy** tab in the Data Quality Monitoring UI, users can perform two key actions on each incident:

- **Assign to me**: Claims ownership of the incident, indicating it is actively being investigated. The table remains in an **Unhealthy** status. The assignment persists for 7 days. ^[anomaly-detection-databricks-on-aws.md]
- **Not an issue**: Marks the incident as a false positive and dismisses it. The table's status changes from **Unhealthy** to **Healthy**, and the **Resolution** column in the [Recently Resolved Incidents](/concepts/recently-resolved-incidents.md) section displays **Not an issue**. The dismissal persists for 7 days. ^[anomaly-detection-databricks-on-aws.md]

### Auto-Resolution and Self-Healing

Some incidents resolve automatically without manual intervention. When a table's status changes from **Unhealthy** to **Healthy** on its own, it appears in the **Recently Resolved Incidents** section of the data quality monitoring dashboard. This typically occurs for transient issues such as upstream delays or staleness windows that resolve after fresh data arrives. ^[anomaly-detection-databricks-on-aws.md]

## Monitoring and Visualization

### Health Indicators

After anomaly detection is enabled on a schema, health indicators appear on schema and table overview pages in Catalog Explorer. These provide a summary of table health for data consumers and business users without requiring navigation to the full incident UI. Users need the **SELECT** or **BROWSE** permission to view the health indicator status. ^[anomaly-detection-databricks-on-aws.md]

### Incident Results UI

The results page in the [Data Quality Monitoring UI](/concepts/data-quality-monitoring-ui.md) provides:

- A **summary section** at the top showing overall data quality for the selected scope (catalog or schema), including the percentage of healthy tables and the percentage of schemas/tables currently monitored.
- A **table of incidents** across all monitored tables in the selected scope, with buttons to display **Unhealthy**, **Healthy**, or **Error** tables. ^[anomaly-detection-databricks-on-aws.md]

### Table Quality Details

For specific tables, the **Table Quality Details** UI provides deeper trend analysis. It shows:

- **Summaries** from each quality check for the table, with graphs of predicted and observed values at each evaluation timestamp (plotting results from the last 1 week of data).
- **Root cause analysis** – if the table failed quality checks, any upstream jobs identified as the root cause are displayed. ^[anomaly-detection-databricks-on-aws.md]

## Logging and System Tables

All detected quality issues are logged in the `system.data_quality_monitoring.table_results` system table. This table stores scan results and is accessible by account admins, who can grant access to others as needed. A dashboard template (`metastore-quality-dashboard.lvdash.json`) can be imported

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
