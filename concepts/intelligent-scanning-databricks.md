---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eb92c13804fa652d5d6ce6a7e0eeda6265e1aaf443119178ecf4448d38d80921
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - intelligent-scanning-databricks
    - IS(
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Intelligent Scanning (Databricks)
description: An automated scan frequency system that prioritizes high-impact tables based on popularity and downstream usage, while reducing scan frequency for less critical tables
tags:
  - data-quality
  - scanning
  - optimization
timestamp: "2026-06-19T14:00:34.672Z"
---

# Intelligent Scanning (Databricks)

**Intelligent Scanning** is a Databricks feature that automates table scan frequencies for data quality monitoring, prioritizing high-impact tables based on popularity and downstream usage while reducing scan frequency for less critical tables. It is part of the [Anomaly Detection](/concepts/anomaly-detection.md) system in [Unity Catalog](/concepts/unity-catalog.md).^[anomaly-detection-databricks-on-aws.md]

## How Intelligent Scanning Works

Intelligent scanning analyzes historical patterns of table usage to determine which tables to prioritize for scanning. It evaluates tables based on:

- **Popularity** — How frequently a table is accessed by users and queries.
- **Downstream usage** — How many other tables or workloads depend on the table as a source.

Based on this analysis, intelligent scanning increases the scan frequency for high-impact tables and reduces the frequency for less critical tables. This ensures that the most important tables receive timely monitoring while minimizing unnecessary resource consumption.^[anomaly-detection-databricks-on-aws.md]

## Purpose and Benefits

Intelligent scanning serves two primary purposes:

1. **Efficiency** — It limits resource consumption by reducing scan frequency for tables that are less critical or rarely accessed.
2. **Reliability** — It prioritizes tables that are most important to the business, ensuring their quality is monitored closely.

This automated approach eliminates the need for manual configuration of scan frequencies for each table in a schema.^[anomaly-detection-databricks-on-aws.md]

## Impact on Anomaly Detection

Anomaly detection monitors tables for [freshness](/concepts/freshness-data-quality.md) (timeliness of updates) and [completeness](/concepts/data-completeness.md) (expected row count) and percent null values. Intelligent scanning determines the frequency at which each table is evaluated for these metrics based on its usage profile. When anomaly detection is enabled on a schema, Databricks uses intelligent scanning to schedule scans for all tables within that schema.^[anomaly-detection-databricks-on-aws.md]

## Health Indicator Delays

Due to intelligent scanning, health indicators for some tables may be delayed by up to two weeks after initial schema enablement if the table was skipped during the initial scan. The health indicator is populated on the next scheduled rescan.^[anomaly-detection-databricks-on-aws.md]

## Manual Exclusion

To exclude specific tables from intelligent scanning, use the Create a Monitor or Update a Monitor API and specify the excluded tables in the `excluded_table_full_names` parameter. For more information, see the API documentation.^[anomaly-detection-databricks-on-aws.md]

## Non-Disruptive Operation

Intelligent scanning **does not** modify any tables it monitors, nor does it add overhead to any jobs that populate these tables. It operates as a read-only background process.^[anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) — The overall data quality monitoring system that uses intelligent scanning
- [Freshness](/concepts/freshness-data-quality.md) — A metric monitored by anomaly detection, indicating how recently a table has been updated
- [Completeness](/concepts/data-completeness.md) — A metric indicating whether the expected number of rows have been written to a table
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform that hosts anomaly detection
- [Health Indicators](/concepts/health-indicators-databricks.md) — Visual status indicators for table quality in Catalog Explorer
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The broader framework for monitoring table quality

## Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
