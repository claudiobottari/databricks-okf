---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 67b72b6b2d0739b2e4be949246620ea9106cd067b67114fea46f7305c7004f54
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - health-indicators-databricks
    - HI(
    - Health Indicators
    - Health Indicators (Data Quality)
    - health indicators
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Health Indicators (Databricks)
description: Visual status indicators shown in Catalog Explorer that summarize table health for data consumers, requiring SELECT or BROWSE permissions to view.
tags:
  - data-quality
  - ui
  - monitoring
timestamp: "2026-06-19T17:33:45.874Z"
---

Here is the wiki page for "Health Indicators (Databricks)".

---

# Health Indicators (Databricks)

**Health Indicators** are visual status badges in [Catalog Explorer](/concepts/catalog-explorer.md) that summarize the data quality of tables within a schema where [Anomaly Detection](/concepts/anomaly-detection.md) has been enabled. They provide a quick, at-a-glance assessment of table health for data consumers and business users without requiring navigation to the full [Data Quality Monitoring](/concepts/data-quality-monitoring.md) UI. ^[anomaly-detection-databricks-on-aws.md]

## Overview

After you enable anomaly detection on a schema, health indicators appear on the schema and table overview pages in Catalog Explorer. These indicators show whether a table is healthy, unhealthy, or in an error state based on automated scans of freshness and completeness. ^[anomaly-detection-databricks-on-aws.md]

Users need the `SELECT` or `BROWSE` privilege to view the health indicator status of tables. ^[anomaly-detection-databricks-on-aws.md]

## Health Indicator Statuses

The following table describes each health indicator status:

| Status | Description |
|--------|-------------|
| **Healthy** | The table passed all quality checks for freshness and completeness. |
| **Unhealthy** | The table failed one or more quality checks. The table may be stale (not updated recently) or incomplete (fewer rows than expected). |
| **Error** | The monitoring system encountered an error while evaluating the table. |

^[anomaly-detection-databricks-on-aws.md]

## How Health Indicators Are Determined

Health indicators are based on two primary quality dimensions evaluated by the anomaly detection background job: ^[anomaly-detection-databricks-on-aws.md]

- **Freshness**: How recently a table has been updated. The system analyzes the history of commits to a table and builds a per-table model to predict the time of the next commit. If a commit is unusually late, the table is marked as stale. ^[anomaly-detection-databricks-on-aws.md]
- **Completeness**: The number of rows expected to be written to the table in the last 24 hours. The system analyzes historical row counts and predicts a range of expected rows. If the number of rows committed over the last 24 hours is less than the lower bound of this range, the table is marked as incomplete. ^[anomaly-detection-databricks-on-aws.md]

Additionally, **percent null** adds quality details to completeness by analyzing the percentage of rows written in the last 24 hours that have null values for a given column. If the percent null exceeds the predicted upper bound, the table is marked as incomplete. ^[anomaly-detection-databricks-on-aws.md]

## Smart Scanning and Health Indicator Population

Databricks uses intelligent scanning to automate table scan frequencies. Smart scanning prioritizes high-impact tables as determined by popularity and downstream usage, and reduces frequency for less critical tables. ^[anomaly-detection-databricks-on-aws.md]

Smart scanning might delay the population of health indicators for some tables by up to two weeks if the table was skipped during the initial scan. The health indicator is populated on the next scheduled rescan. ^[anomaly-detection-databricks-on-aws.md]

## Viewing Health Indicators

Health indicators appear in two locations within Catalog Explorer: ^[anomaly-detection-databricks-on-aws.md]

1. **Schema overview page**: Shows health indicators for all tables within the schema.
2. **Table overview page**: Shows the health indicator for the specific table.

![Health indicators for tables in a schema.](https://docs.databricks.com/aws/en/assets/images/anomaly-detection-health-indicators-d8e978de4283df5a4c8fc0c5815eaa92.png)

## Managing Unhealthy Tables

When a table is marked as unhealthy, users can navigate to the [Data Quality Monitoring UI](/concepts/data-quality-monitoring-ui.md) to review incident details. From the incident details view, two actions are available: ^[anomaly-detection-databricks-on-aws.md]

- **Assign to me**: Claims ownership of the incident to indicate active investigation. The table remains in an **Unhealthy** status. The assignment persists for 7 days.
- **Not an issue**: Marks the incident as a false positive and dismisses it. The table's status changes from **Unhealthy** to **Healthy**. The dismissal persists for 7 days.

## Recently Resolved Incidents

The **Recently Resolved Incidents** section shows tables that were previously unhealthy but have since recovered on their own. A table appears in this section when its status changes from **Unhealthy** to **Healthy** automatically, without manual intervention. ^[anomaly-detection-databricks-on-aws.md]

Monitoring recently auto-resolved incidents helps identify self-healing data quality issues, such as transient problems like upstream delays or staleness windows that resolve after fresh data arrives. ^[anomaly-detection-databricks-on-aws.md]

## Table Quality Details

The **Table Quality Details** UI provides deeper insights into trends and explains why anomalies were detected for specific tables. This view can be accessed from: ^[anomaly-detection-databricks-on-aws.md]

- The **Results UI** by clicking the review link in the incidents list.
- The **Monitoring Dashboard** (legacy) by clicking the table name in the Quality Overview tab.
- The **UC Table viewer** by visiting the **Quality** tab on the table page.

The UI shows summaries from each quality check with graphs of predicted and observed values at each evaluation timestamp, plotting results from the last 1 week of data. If the table failed quality checks, the UI also displays any upstream jobs identified as the root cause. ^[anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) — The underlying monitoring system that generates health indicators.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The broader framework for tracking data quality.
- [Catalog Explorer](/concepts/catalog-explorer.md) — The UI where health indicators are displayed.
- [Freshness](/concepts/freshness-data-quality.md) — A quality dimension measuring how recently a table was updated.
- [Completeness](/concepts/data-completeness.md) — A quality dimension measuring expected row counts.
- [Percent Null](/concepts/percent-null.md) — A completeness sub-metric for null value analysis.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that enables anomaly detection.

## Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
