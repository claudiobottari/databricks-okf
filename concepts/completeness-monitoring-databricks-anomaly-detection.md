---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4b64b57bd17872f4c87e07c910af9d04fd4e8a9eef0b0540e948d7c354831e84
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - completeness-monitoring-databricks-anomaly-detection
    - CM(AD
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Completeness Monitoring (Databricks Anomaly Detection)
description: A quality dimension that monitors the expected number of rows written to a table in the last 24 hours by analyzing historical row counts and flagging tables as incomplete if row counts fall below predicted bounds.
tags:
  - data-quality
  - anomaly-detection
  - monitoring
timestamp: "2026-06-19T08:59:06.834Z"
---

# Completeness Monitoring (Databricks Anomaly Detection)

**Completeness Monitoring** is a feature of [Databricks Anomaly Detection](/concepts/databricks-anomaly-detection.md) that automatically evaluates whether tables in a Unity Catalog schema have received the expected number of rows within the last 24 hours. It is part of the broader data quality monitoring system that helps data teams detect when tables are missing data without manual threshold configuration. ^[anomaly-detection-databricks-on-aws.md]

## How Completeness Is Determined

Completeness monitoring analyzes the historical row count of each table and builds a statistical model to predict an expected range of rows. If the number of rows committed over the last 24 hours falls below the lower bound of this predicted range, the table is marked as **incomplete**. ^[anomaly-detection-databricks-on-aws.md]

The system does not account for metrics such as the fraction of nulls, zero values, or NaN when determining completeness. ^[anomaly-detection-databricks-on-aws.md]

## Percent Null for Completeness

**Percent null** is an additional quality dimension within completeness monitoring. It tracks the percentage of rows written to a table in the last 24 hours that are expected to have null values for a given column. The system analyzes the historical trend for each column and predicts a range. If the actual percent null for a column over the last 24 hours exceeds the upper bound of this range, the table is also marked as incomplete. ^[anomaly-detection-databricks-on-aws.md]

## How It Works

Databricks creates a background job that monitors tables in schemas where anomaly detection has been enabled. The job:

- Analyzes historical row counts to establish baseline patterns.
- Predicts a range of expected row counts for each monitoring window.
- Compares actual row count against the predicted range.
- Marks tables as incomplete when counts fall below expectations.

The monitoring job does not modify any tables it monitors, nor does it add overhead to jobs that populate these tables. ^[anomaly-detection-databricks-on-aws.md]

## Prerequisites

Before completeness monitoring can be enabled, the workspace must meet the following requirements:

- [Unity Catalog](/concepts/unity-catalog.md) must be enabled.
- [Serverless compute](/concepts/serverless-gpu-compute.md) must be available in the workspace (enabled by default in workspaces with Unity Catalog).
- The user must have `MANAGE SCHEMA` or `MANAGE CATALOG` privileges on the target catalog or schema.
- To view health indicators, users need `SELECT` or `BROWSE` privileges. ^[anomaly-detection-databricks-on-aws.md]

## Enabling Completeness Monitoring

Completeness monitoring is automatically enabled when anomaly detection is turned on for a schema. To enable it:

1. Navigate to the schema in [Catalog Explorer](/concepts/catalog-explorer.md).
2. Click the **Details** tab.
3. Click **Enable**.
4. In the **Data Quality Monitoring** dialog, ensure **Anomaly detection** is toggled on.
5. Click **Save**.

A scan is initiated. After completion, results are visible through health indicators and the Data Quality Monitoring UI. ^[anomaly-detection-databricks-on-aws.md]

## Viewing Completeness Results

Completeness results are available through several interfaces:

- **Health indicators** appear in Catalog Explorer for each table within a monitored schema.
- **Data Quality Monitoring UI** provides a detailed incidents view showing which tables are incomplete.
- **System table** logs results in `system.data_quality_monitoring.table_results` for programmatic access.
- **Table Quality Details UI** shows historical trends with graphs of predicted versus observed row counts. ^[anomaly-detection-databricks-on-aws.md]

## Managing Incomplete Table Incidents

From the **Unhealthy** tab in the Data Quality Monitoring UI, users can:

- **Assign to me**: Indicate ownership of the incident investigation. The table remains unhealthy and the assignment persists for 7 days.
- **Not an issue**: Mark the incident as a false positive. The table status changes to **Healthy** and dismissal persists for 7 days. ^[anomaly-detection-databricks-on-aws.md]

Tables that automatically recover from incomplete status appear in the **Recently Resolved Incidents** section, allowing teams to distinguish transient issues from persistent problems. ^[anomaly-detection-databricks-on-aws.md]

## Limitations

- Completeness monitoring does not support views or foreign tables.
- The determination of completeness does not incorporate metrics such as the fraction of nulls, zero values, or NaN (though percent null is tracked separately). ^[anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Freshness Monitoring (Databricks Anomaly Detection)](/concepts/freshness-monitoring-databricks-anomaly-detection.md) — The companion check that evaluates how recently tables have been updated.
- [Data Quality Monitoring on Databricks](/concepts/data-quality-monitoring-databricks.md) — The broader framework for automated data quality assessment.
- [Anomaly Detection Overview](/concepts/anomaly-detection-databricks.md) — The system that combines freshness and completeness checks.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that enables schema-level monitoring.
- [Catalog Explorer](/concepts/catalog-explorer.md) — The UI for enabling and viewing monitoring results.

## Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
