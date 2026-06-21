---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 95f526cf2584edbccb78989d86bb2054e570e9d86b2fa454eaf5265db0a449b7
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-quality-monitoring-ui-databricks
    - DQMU(
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Data Quality Monitoring UI (Databricks)
description: A user interface for viewing anomaly detection results, incidents per schema or catalog, with tabs for unhealthy, healthy, or error tables and features for assigning and dismissing incidents.
tags:
  - data-quality
  - ui
  - incidents
timestamp: "2026-06-19T17:33:30.867Z"
---

# Data Quality Monitoring UI (Databricks)

The **Data Quality Monitoring UI** is a visual interface in Databricks Catalog Explorer that displays the results of [Anomaly Detection](/concepts/anomaly-detection.md) scans on tables within schemas that have data quality monitoring enabled. It provides an at-a-glance view of table health, including freshness and completeness, and allows users to review, manage, and resolve data quality incidents. ^[anomaly-detection-databricks-on-aws.md]

## Accessing the UI

After enabling data quality monitoring on a schema, click **View results** on the schema's **Details** tab to open the Data Quality Monitoring UI. You can also access results from all schemas that have monitoring enabled in Catalog Explorer. ^[anomaly-detection-databricks-on-aws.md]

The results UI contains [Catalog and Schema](/concepts/catalog-and-schema.md) dropdowns. When you select a catalog, the schema dropdown is populated with schemas in that catalog that have data quality monitoring enabled. ^[anomaly-detection-databricks-on-aws.md]

- If you have **MANAGE** or **SELECT** privileges on the catalog, you can view incidents at the catalog level by selecting **All Schemas** from the **Schema** drop-down menu. ^[anomaly-detection-databricks-on-aws.md]
- To view incidents for a specific schema, you must also have **MANAGE** or **SELECT** privileges on that schema. ^[anomaly-detection-databricks-on-aws.md]

## UI Layout

The results page shows a summary section at the top, which displays overall data quality for the selected scope, including the percentage of healthy tables and the percentage of schemas or tables currently monitored. Below this section is a table listing incidents across all monitored tables in the selected scope. Use the buttons to display **Unhealthy**, **Healthy**, or **Error** tables. ^[anomaly-detection-databricks-on-aws.md]

The columns in the incidents table differ slightly depending on whether you select **Unhealthy**, **Healthy**, or **Error**. ^[anomaly-detection-databricks-on-aws.md]

## Managing Unhealthy Table Incidents

From the **Unhealthy** tab, click **Review** in the **Results** column to open the incident details for the table. From this view, two actions are available: ^[anomaly-detection-databricks-on-aws.md]

- **Assign to me**: Claims ownership of the incident to indicate that it is actively being investigated. The table remains in an **Unhealthy** status. The assignment persists for 7 days. ^[anomaly-detection-databricks-on-aws.md]
- **Not an issue**: Marks the incident as a false positive and dismisses it. The table's status changes from **Unhealthy** to **Healthy**, and the **Resolution** column in the Recently Resolved Incidents section displays **Not an issue**. The dismissal persists for 7 days. ^[anomaly-detection-databricks-on-aws.md]

## Recently Resolved Incidents

The **Recently Resolved Incidents** section of the Data Quality Monitoring dashboard shows tables that were previously unhealthy but have since recovered on their own. A table appears in this section when its status changes from **Unhealthy** to **Healthy** automatically, without manual intervention. ^[anomaly-detection-databricks-on-aws.md]

Monitoring recently auto-resolved incidents helps you identify self-healing data quality issues. Typically, these issues are transient problems such as upstream delays or staleness windows that resolve after fresh data arrives. Reviewing auto-resolved incidents helps you distinguish flaky issues from persistent problems and ensures that your tables remain healthy over time. ^[anomaly-detection-databricks-on-aws.md]

## Health Indicators

After you enable anomaly detection on a schema, health indicators appear on the schema and table overview pages in Catalog Explorer. The health indicator shows a summary of table health for data consumers and business users without requiring them to navigate to the Data Quality Monitoring UI. Users need the SELECT or BROWSE permission to view the health indicator status. ^[anomaly-detection-databricks-on-aws.md]

Smart scanning might delay the population of health indicators for some tables by up to two weeks if the table was skipped during the initial scan. The health indicator is populated on the next scheduled rescan. ^[anomaly-detection-databricks-on-aws.md]

## Table Quality Details

The **Table Quality Details** UI allows you to dive deeper into trends and understand why anomalies were detected for specific tables. You can access this view in several ways: ^[anomaly-detection-databricks-on-aws.md]

- From the **Results UI** (new experience), by clicking on the review link in the incidents list. ^[anomaly-detection-databricks-on-aws.md]
- From the **Monitoring Dashboard** (legacy Lakeview dashboard), by clicking on the table name in the Quality Overview tab. ^[anomaly-detection-databricks-on-aws.md]
- From the **UC Table viewer**, by visiting the **Quality** tab on the table page. ^[anomaly-detection-databricks-on-aws.md]

All options take you to the same **Table Quality Details** view for the selected table. ^[anomaly-detection-databricks-on-aws.md]

When viewing a table, the UI shows summaries from each quality check for the table, with graphs of predicted and observed values at each evaluation timestamp. The graphs plot results from the last 1 week of data. If the table failed the quality checks, the UI also displays any upstream jobs that were identified as the root cause. ^[anomaly-detection-databricks-on-aws.md]

## Prerequisites for Viewing Results

To view the health indicator status of tables, you need SELECT or BROWSE privileges. To view incidents at the catalog level, you must have **MANAGE** or **SELECT** privileges on the catalog. To view incidents for a specific schema, you must also have **MANAGE** or **SELECT** privileges on that schema. ^[anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) — The underlying monitoring system that evaluates table freshness and completeness
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The broader capability that includes both anomaly detection and the monitoring UI
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer that provides the access control for viewing monitoring results
- System Tables — The storage backend for monitoring results
- Lakeview Dashboards — The legacy monitoring dashboard that preceded the new UI

## Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
