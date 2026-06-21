---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 634eab8c10e0d9498a332cac3205fe4550cfa9b38c84c59c22e8561189d52e6c
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-quality-monitoring-incidents-management
    - DQMIM
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Data Quality Monitoring Incidents Management
description: Workflow for reviewing, assigning, and dismissing data quality anomalies from the UI, including auto-resolved incidents that self-heal without manual intervention.
tags:
  - data-quality
  - workflow
  - incident-management
timestamp: "2026-06-19T22:06:10.705Z"
---

# Data Quality Monitoring Incidents Management

**Data Quality Monitoring Incidents Management** refers to the tools and workflows within [Unity Catalog](/concepts/unity-catalog.md) on Databricks that allow users to track, investigate, and resolve data quality anomalies detected across tables in a schema. When [Anomaly Detection](/concepts/anomaly-detection.md) identifies a table that violates freshness or completeness expectations, it creates an incident that appears in the **Data Quality Monitoring** results page in [Catalog Explorer](/concepts/catalog-explorer.md). ^[anomaly-detection-databricks-on-aws.md]

## Incident Visibility and Access

Users with **MANAGE** or **SELECT** privileges on a catalog can view all incidents across schemas in that catalog by selecting **All Schemas** from the schema drop-down. To see incidents for a specific schema, the user must also have the necessary privileges on that schema. The results page displays a summary section at the top showing the percentage of healthy tables and the percentage of schemas or tables currently monitored, followed by a table listing the incidents. ^[anomaly-detection-databricks-on-aws.md]

The incidents table can be filtered using buttons for **Unhealthy**, **Healthy**, or **Error** tables. Columns differ slightly depending on which tab is selected. ^[anomaly-detection-databricks-on-aws.md]

## Managing Unhealthy Table Incidents

From the **Unhealthy** tab, clicking **Review** in the **Results** column opens the incident details for the affected table. Two actions are available:

- **Assign to me**: Claims ownership of the incident to indicate active investigation. The table remains in an **Unhealthy** status. The assignment persists for 7 days. ^[anomaly-detection-databricks-on-aws.md]
- **Not an issue**: Marks the incident as a false positive and dismisses it. The table's status changes from **Unhealthy** to **Healthy**, and the **Resolution** column in the [Recently Resolved Incidents](#view-recently-resolved-incidents) section displays **Not an issue**. The dismissal persists for 7 days. ^[anomaly-detection-databricks-on-aws.md]

## View Recently Resolved Incidents

The **Recently Resolved Incidents** section of the data quality monitoring dashboard shows tables that were previously unhealthy but have since recovered automatically without manual intervention. A table appears in this section when its status changes from **Unhealthy** to **Healthy** on its own. ^[anomaly-detection-databricks-on-aws.md]

Monitoring recently auto-resolved incidents helps identify self-healing data quality issues, which are typically transient problems such as upstream delays or staleness windows that resolve after fresh data arrives. Reviewing these incidents helps distinguish flaky issues from persistent problems and ensures that tables remain healthy over time. ^[anomaly-detection-databricks-on-aws.md]

The section includes columns such as table name, schema, and resolution reason, providing a template that can be imported into the workspace.^[anomaly-detection-databricks-on-aws.md]

## Table Quality Details

Clicking a review link in the incidents list opens the **Table Quality Details** view for the selected table. This view shows summaries from each quality check, with graphs of predicted and observed values at each evaluation timestamp, plotted for the last 1 week of data. If the table failed quality checks, the UI also displays any upstream jobs identified as the root cause. ^[anomaly-detection-databricks-on-aws.md]

This view can also be accessed from the **Monitoring Dashboard** (legacy Lakeview dashboard) or from the **Quality** tab on the table page in Catalog Explorer. ^[anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) – The underlying mechanism that detects freshness and completeness issues.
- [Health Indicators](/concepts/health-indicators-databricks.md) – Visual status badges shown in Catalog Explorer for each table.
- Alerts for Anomaly Detection – SQL-based alerts on output results tables.
- system.data_quality_monitoring.table_results|System Tables for Data Quality Monitoring – `system.data_quality_monitoring.table_results` table for logged results.
- [Data Quality Monitoring UI](/concepts/data-quality-monitoring-ui.md) – The overall interface for viewing monitoring results.

## Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
