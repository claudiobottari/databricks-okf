---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8d41dde011696a01e2a8bed2f03fbd5160a7c0b91a4d517a8cf4b110e7981289
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-completeness-anomaly-detection
    - DC(D
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Data Completeness (Anomaly Detection)
description: A quality metric that measures expected row counts over 24 hours using historical analysis, flagging tables with unusually low row additions
tags:
  - data-quality
  - monitoring
  - completeness
timestamp: "2026-06-19T14:00:25.594Z"
---

# Data Completeness (Anomaly Detection)

**Data Completeness (Anomaly Detection)** refers to a quality monitoring capability in Databricks that automatically evaluates whether tables in a schema have received the expected number of rows within a 24-hour period. By analyzing historical row count patterns, the system predicts a range of expected rows and flags tables as incomplete when actual row counts fall below the lower bound of that range. ^[anomaly-detection-databricks-on-aws.md]

## Overview

Data completeness is one of two primary quality dimensions monitored by Databricks anomaly detection, alongside [Data Freshness (Anomaly Detection)](/concepts/data-freshness-anomaly-detection.md). Completeness monitoring helps data consumers and pipeline operators identify when data ingestion pipelines fail to deliver the expected volume of records, enabling rapid detection of upstream data quality issues. ^[anomaly-detection-databricks-on-aws.md]

## How Completeness Is Measured

Completeness is determined by analyzing the historical row count of a table and building a predictive model. The system examines the number of rows committed to the table over the last 24 hours and compares this observed value against a predicted range derived from historical patterns. If the observed row count is less than the lower bound of the predicted range, the table is marked as **incomplete**. ^[anomaly-detection-databricks-on-aws.md]

The completeness check does not take into account metrics such as the fraction of nulls, zero values, or NaN. ^[anomaly-detection-databricks-on-aws.md]

## Percent Null for Completeness

**Percent null** adds additional quality details to completeness monitoring. Percent null is the percentage of rows written to the table in the last 24 hours expected to have null values for a given column. Data quality monitoring analyzes the historical trend for each column and, based on this data, predicts a range. If the percent null for a column over the last 24 hours is higher than the upper bound of this range, the table is also marked as incomplete. ^[anomaly-detection-databricks-on-aws.md]

## Enabling Completeness Monitoring

Completeness monitoring is automatically enabled when you enable anomaly detection on a schema. To enable anomaly detection:

1. Navigate to the schema in Unity Catalog.
2. Click the **Details** tab.
3. Click **Enable**.
4. In the **Data Quality Monitoring** dialog, ensure that **Anomaly detection** is toggled on, then click **Save**.

After enabling, Databricks automatically scans each table at the same frequency it is updated. ^[anomaly-detection-databricks-on-aws.md]

## Viewing Completeness Results

Completeness results are available through several interfaces:

- **Health indicators** appear in Catalog Explorer for each table within a schema, showing a summary of table health including completeness status. ^[anomaly-detection-databricks-on-aws.md]
- **Data Quality Monitoring UI** provides detailed incident information, including which tables are marked as incomplete. ^[anomaly-detection-databricks-on-aws.md]
- **Table Quality Details** view allows deeper analysis of trends, showing graphs of predicted and observed row counts at each evaluation timestamp over the last week. ^[anomaly-detection-databricks-on-aws.md]

## Managing Completeness Incidents

When a table is flagged as incomplete, users can take the following actions from the **Unhealthy** tab in the Data Quality Monitoring UI:

- **Assign to me**: Claims ownership of the incident to indicate active investigation. The table remains in an **Unhealthy** status. The assignment persists for 7 days.
- **Not an issue**: Marks the incident as a false positive and dismisses it. The table's status changes from **Unhealthy** to **Healthy**. The dismissal persists for 7 days.

Tables that recover automatically appear in the **Recently Resolved Incidents** section, helping distinguish transient issues from persistent problems. ^[anomaly-detection-databricks-on-aws.md]

## Limitations

- Anomaly detection does not support views or foreign tables. ^[anomaly-detection-databricks-on-aws.md]
- The determination of completeness does not take into account metrics such as the fraction of nulls, zero values, or NaN (beyond the percent null check). ^[anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Data Freshness (Anomaly Detection)](/concepts/data-freshness-anomaly-detection.md) — The companion quality dimension that monitors how recently a table has been updated.
- [Anomaly Detection on Databricks](/concepts/anomaly-detection-databricks.md) — The overall framework for automated data quality monitoring.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that enables anomaly detection on schemas.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The broader practice of monitoring data quality in Databricks.
- [Catalog Explorer](/concepts/catalog-explorer.md) — The UI for viewing health indicators and quality results.

## Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
