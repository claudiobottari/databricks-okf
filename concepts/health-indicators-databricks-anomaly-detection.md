---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e8c2e180f21f9759d604ec0e80159e856a8ee07778e5fad9b4ca15943396306b
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - health-indicators-databricks-anomaly-detection
    - HI(AD
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Health Indicators (Databricks Anomaly Detection)
description: Visual status indicators shown in Catalog Explorer for each table within a monitored schema, summarizing table health for data consumers
tags:
  - data-quality
  - ui
  - catalog
timestamp: "2026-06-19T14:00:44.635Z"
---

# Health Indicators (Databricks Anomaly Detection)

**Health Indicators** are visual summaries of table health shown in [Catalog Explorer](/concepts/catalog-explorer.md) after [anomaly detection](/concepts/anomaly-detection-databricks.md) is enabled on a schema. They provide an at-a-glance signal about data quality for data consumers and business users, without requiring navigation to the full Data Quality Monitoring UI. ^[anomaly-detection-databricks-on-aws.md]

## Requirements

Users must have the `SELECT` or `BROWSE` privilege on a table to view its health indicator status. Health indicators only appear for tables in schemas that have anomaly detection enabled. ^[anomaly-detection-databricks-on-aws.md]

## How Health Indicators Work

Health indicators are derived from the two core checks of anomaly detection: **freshness** (how recently a table was updated) and **completeness** (whether the number of rows written in the last 24 hours falls within an expected range). ^[anomaly-detection-databricks-on-aws.md]

After you enable anomaly detection on a schema, Databricks runs a background job that monitors these metrics for each table. The results are summarized as health indicators on the schema and table overview pages in Catalog Explorer. ^[anomaly-detection-databricks-on-aws.md]

Because Databricks uses intelligent scanning to prioritize high-impact tables, the health indicator for some tables may be delayed by up to two weeks if the table was skipped during the initial scan. The indicator is populated on the next scheduled rescan. ^[anomaly-detection-databricks-on-aws.md]

## Health Indicator Statuses

Each table receives a health indicator status that reflects the outcome of the most recent freshness and completeness evaluation. (The specific status values are documented in a table in the Databricks UI; the source document does not reproduce the table content.) ^[anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection (Databricks)](/concepts/anomaly-detection-databricks.md) – The feature that enables health indicators.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – The broader framework for tracking table quality.
- [Unity Catalog](/concepts/unity-catalog.md) – Required for anomaly detection and health indicators.
- [Catalog Explorer](/concepts/catalog-explorer.md) – The interface where health indicators are displayed.
- [Freshness and Completeness Checks](/concepts/freshness-and-completeness-quality-metrics.md) – The metrics underlying health indicators.
- [Intelligent Scanning](/concepts/intelligent-scanning.md) – The scheduling mechanism that may delay health indicator population.
- Data Quality Monitoring Results UI – The detailed incident view for unhealthy tables.

## Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
