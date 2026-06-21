---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a8062488547db8eefef71fb224fb99abe79459393d1797c36623d3df339af770
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-freshness-anomaly-detection
    - DF(D
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Data Freshness (Anomaly Detection)
description: A quality metric that measures how recently a table has been updated, using historical commit patterns to predict expected next commit times
tags:
  - data-quality
  - monitoring
  - freshness
timestamp: "2026-06-19T14:00:26.220Z"
---

# Data Freshness (Anomaly Detection)

**Data Freshness (Anomaly Detection)** refers to the automated monitoring capability in Databricks that evaluates how recently a table has been updated. By analyzing historical commit patterns, Databricks builds a per-table model to predict the expected time of the next commit. If a commit is unusually late, the table is marked as stale. ^[anomaly-detection-databricks-on-aws.md]

## Overview

Data freshness is one of two primary quality dimensions monitored by Databricks' anomaly detection feature, alongside [Data Completeness (Anomaly Detection)](/concepts/data-completeness-anomaly-detection.md). When anomaly detection is enabled on a schema, a background job monitors all tables in that schema for freshness and completeness without requiring manual configuration for each table. ^[anomaly-detection-databricks-on-aws.md]

## How Freshness Detection Works

Databricks analyzes the history of commits to a table and builds a statistical model to predict when the next commit should occur. The model accounts for the table's historical update patterns, such as daily, hourly, or irregular schedules. If a commit does not occur within the expected timeframe, the table is flagged as stale. ^[anomaly-detection-databricks-on-aws.md]

The freshness check does not modify any tables it monitors, nor does it add overhead to any jobs that populate these tables. ^[anomaly-detection-databricks-on-aws.md]

## Requirements

To use anomaly detection for data freshness monitoring, the following requirements must be met:

- A [Unity Catalog](/concepts/unity-catalog.md) enabled workspace.
- [Serverless compute](/concepts/serverless-gpu-compute.md) must be available in the workspace (enabled by default in workspaces with Unity Catalog).
- To enable anomaly detection on a schema, the user must have `MANAGE SCHEMA` or `MANAGE CATALOG` privileges on the catalog schema.
- To view health indicator status of tables, the user needs `SELECT` or `BROWSE` privileges.

^[anomaly-detection-databricks-on-aws.md]

## Enabling Anomaly Detection

To enable anomaly detection on a schema:

1. Navigate to the schema in Unity Catalog.
2. Click the **Details** tab.
3. Click **Enable**.
4. In the **Data Quality Monitoring** dialog, ensure that **Anomaly detection** is toggled on, then click **Save**.

A scan is initiated automatically. Databricks scans each table at the same frequency it is updated, providing up-to-date insights without requiring manual configuration for each table. ^[anomaly-detection-databricks-on-aws.md]

## Health Indicators

After anomaly detection is enabled, health indicators appear on schema and table overview pages in Catalog Explorer. These indicators provide a summary of table health for data consumers and business users. ^[anomaly-detection-databricks-on-aws.md]

The health indicator statuses include:

| Status | Description |
|--------|-------------|
| Healthy | Table is up to date based on predicted freshness |
| Unhealthy | Table is stale — a commit is unusually late |
| Error | An error occurred during evaluation |

^[anomaly-detection-databricks-on-aws.md]

## Viewing Freshness Results

Results can be viewed in several ways:

- **Health indicators** appear in Catalog Explorer for each table within a schema.
- **Data Quality Monitoring UI** — On the **Details** tab of a schema with monitoring enabled, click **View results** to see incidents.
- **Table Quality Details** — Click the review link in the incidents list to see detailed trends, including graphs of predicted and observed values at each evaluation timestamp. Results from the last week of data are plotted.

If a table fails the freshness check, the UI also displays any upstream jobs identified as the root cause. ^[anomaly-detection-databricks-on-aws.md]

## Managing Stale Table Incidents

From the **Unhealthy** tab in the Data Quality Monitoring UI, two actions are available for stale table incidents:

- **Assign to me** — Claims ownership of the incident to indicate active investigation. The table remains in an **Unhealthy** status. The assignment persists for 7 days.
- **Not an issue** — Marks the incident as a false positive and dismisses it. The table's status changes from **Unhealthy** to **Healthy**. The dismissal persists for 7 days.

^[anomaly-detection-databricks-on-aws.md]

## Recently Resolved Incidents

The **Recently Resolved Incidents** section shows tables that were previously unhealthy but have since recovered on their own. A table appears here when its status changes from **Unhealthy** to **Healthy** automatically, without manual intervention. Monitoring these auto-resolved incidents helps identify self-healing data quality issues, such as transient upstream delays or staleness windows that resolve after fresh data arrives. ^[anomaly-detection-databricks-on-aws.md]

## Intelligent Scanning

Databricks uses intelligent scanning to automate table scan frequencies. Intelligent scanning prioritizes high-impact tables as determined by popularity and downstream usage, and reduces frequency for less critical tables. To manually exclude tables, use the Create a Monitor or Update a Monitor API and specify the excluded tables in the `excluded_table_full_names` parameter. ^[anomaly-detection-databricks-on-aws.md]

Smart scanning might delay the population of health indicators for some tables by up to two weeks if the table was skipped during the initial scan. The health indicator is populated on the next scheduled rescan. ^[anomaly-detection-databricks-on-aws.md]

## Limitations

- Anomaly detection does not support views or foreign tables.
- Event freshness, which was based on event time columns and ingestion latency, was available only to users of the data quality monitoring beta version. In the current version, event freshness is not supported.

^[anomaly-detection-databricks-on-aws.md]

## Setting Up Alerts

To configure a Databricks SQL alert on the output results table for freshness anomalies, see Alerts for Anomaly Detection. ^[anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Data Completeness (Anomaly Detection)](/concepts/data-completeness-anomaly-detection.md) — The other primary quality dimension, monitoring expected row counts
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer required for anomaly detection
- Serverless Compute — Required compute infrastructure for monitoring
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The broader framework for assessing table health
- [Catalog Explorer](/concepts/catalog-explorer.md) — UI for viewing health indicators and results

## Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
