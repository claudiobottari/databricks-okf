---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f8db717a035ef943d1c3bce49bd5b3497c3fc553b23c0dadf12446ce5d789f94
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - freshness-monitoring-databricks-anomaly-detection
    - FM(AD
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Freshness Monitoring (Databricks Anomaly Detection)
description: A quality dimension that monitors how recently a table has been updated, using historical commit patterns to predict when the next commit should occur and flagging tables as stale if commits are unusually late.
tags:
  - data-quality
  - anomaly-detection
  - monitoring
timestamp: "2026-06-19T08:58:55.317Z"
---

# Freshness Monitoring (Databricks Anomaly Detection)

**Freshness Monitoring** is a feature of [Databricks Anomaly Detection](/concepts/databricks-anomaly-detection.md) that automatically tracks how recently tables have been updated and flags any table whose commits are unusually late compared to historical patterns. It is one of two primary quality dimensions monitored by Databricks, alongside [completeness monitoring](/concepts/data-completeness.md). ^[anomaly-detection-databricks-on-aws.md]

## Overview

Freshness refers to how recently a table has been updated. Databricks anomaly detection analyzes the history of commits to a table and builds a per-table model to predict the time of the next commit. If a commit is unusually late, the table is marked as **stale**. ^[anomaly-detection-databricks-on-aws.md]

This monitoring runs as a background job that does not modify any tables it monitors nor add overhead to jobs that populate those tables. ^[anomaly-detection-databricks-on-aws.md]

## How It Works

The freshness check works by:

1. **Analyzing commit history** – The system examines the historical pattern of commits for each table.
2. **Building a predictive model** – A per-table model is created to predict when the next commit should occur.
3. **Comparing actual vs. predicted** – If a commit arrives significantly later than predicted, the table is flagged as stale. ^[anomaly-detection-databricks-on-aws.md]

The system uses [Intelligent Scanning](/concepts/intelligent-scanning.md) to automate table scan frequencies, prioritizing high-impact tables based on popularity and downstream usage, and reducing scan frequency for less critical tables. ^[anomaly-detection-databricks-on-aws.md]

## Viewing Freshness Results

Freshness results appear in several locations:

- **Health indicators** – Shown in Catalog Explorer for each table within a monitored schema. ^[anomaly-detection-databricks-on-aws.md]
- **Data Quality Monitoring UI** – Accessible from the schema's **Details** tab by clicking **View results**. ^[anomaly-detection-databricks-on-aws.md]
- **Table Quality Details** – Provides graphs of predicted and observed commit times for the last week, along with root cause analysis identifying upstream jobs that caused failures. ^[anomaly-detection-databricks-on-aws.md]

## Requirements

- [Unity Catalog](/concepts/unity-catalog.md) enabled workspace.
- [Serverless compute](/concepts/serverless-gpu-compute.md) must be available (enabled by default in workspaces with Unity Catalog).
- To enable anomaly detection on a schema: `MANAGE SCHEMA` or `MANAGE CATALOG` privilege.
- To view health indicators: `SELECT` or `BROWSE` privilege. ^[anomaly-detection-databricks-on-aws.md]

## Enabling Freshness Monitoring

Freshness monitoring is automatically enabled when you enable anomaly detection on a schema:

1. Navigate to the schema in Unity Catalog.
2. Click the **Details** tab.
3. Click **Enable**.
4. In the **Data Quality Monitoring** dialog, ensure **Anomaly detection** is toggled on.
5. Click **Save**.

A scan is initiated. For schemas enabled prior to September 24, 2025, Databricks runs historical backtesting for the first scan. ^[anomaly-detection-databricks-on-aws.md]

## Excluding Tables

To manually exclude tables from freshness monitoring, use the Create a Monitor API or Update a Monitor API and specify excluded tables in the `excluded_table_full_names` parameter. ^[anomaly-detection-databricks-on-aws.md]

## Legacy Configuration (Pre-July 2025)

Prior to July 21, 2025, users could customize freshness evaluation parameters by editing job task parameters. The `metric_type` for freshness is `FreshnessConfig`. Available legacy parameters include:

- `disable_check` – Disables the freshness check.
- `tables_to_skip` – Lists tables to skip.
- `tables_to_scan` – Lists tables to scan.
- `table_threshold_overrides` – Overrides freshness thresholds.
- `table_latency_threshold_overrides` – Overrides latency thresholds.
- `static_table_threshold_override` – Configures behavior for static tables.
- `event_timestamp_col_names` – Specifies event timestamp columns (not supported in the current version).

These configuration options are not supported for new customers after July 21, 2025. ^[anomaly-detection-databricks-on-aws.md]

## Limitations

- Event freshness based on event time columns and ingestion latency is not supported in the current version. It was available only to beta users. ^[anomaly-detection-databricks-on-aws.md]
- Anomaly detection does not support views or foreign tables. ^[anomaly-detection-databricks-on-aws.md]

## Managing Stale Table Incidents

When a table is marked stale from the **Unhealthy** tab:

- **Assign to me** – Claims ownership of the incident. The table remains **Unhealthy**. The assignment persists for 7 days.
- **Not an issue** – Marks the incident as a false positive. The table status changes to **Healthy**. The dismissal persists for 7 days. ^[anomaly-detection-databricks-on-aws.md]

The **Recently Resolved Incidents** section shows tables that returned to **Healthy** status automatically, helping distinguish transient upstream delays from persistent problems. ^[anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Completeness Monitoring (Databricks Anomaly Detection)](/concepts/completeness-monitoring-databricks-anomaly-detection.md) – Monitors row counts and null percentages.
- [Data Quality Monitoring UI](/concepts/data-quality-monitoring-ui.md) – Central interface for viewing all quality incidents.
- [Intelligent Scanning](/concepts/intelligent-scanning.md) – Automates scan frequency based on table importance.
- [Root Cause Analysis](/concepts/inference-tables-for-root-cause-analysis.md) – Identifies upstream jobs causing quality failures.
- [Health Indicators](/concepts/health-indicators-databricks.md) – Visual status badges in Catalog Explorer.

## Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
