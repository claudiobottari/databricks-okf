---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fdbc84f851f9780750d96d584c2acd379547ae495b32b01b04948a6edaabc8a7
  pageDirectory: concepts
  sources:
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - anomaly-detection-for-table-completeness
    - ADFTC
  citations:
    - file: data-quality-monitoring-databricks-on-aws.md
title: Anomaly Detection for Table Completeness
description: A monitoring feature that analyzes historical row counts to predict an expected range of rows over 24 hours and marks a table as incomplete if the actual count falls below the lower bound.
tags:
  - anomaly-detection
  - completeness
  - data-monitoring
timestamp: "2026-06-18T15:02:52.893Z"
---

# Anomaly Detection for Table Completeness

**Anomaly Detection for Table Completeness** is a capability within [Data Quality Monitoring on Databricks](/concepts/data-quality-monitoring-databricks.md) that automatically monitors whether tables in [Unity Catalog](/concepts/unity-catalog.md) receive the expected number of rows within a 24-hour window. It is part of the broader anomaly detection framework in Databricks that helps ensure data quality without manual threshold configuration.

## Overview

Anomaly detection enables scalable data quality monitoring with one click. It monitors all tables in a schema using intelligent scanning that prioritizes important tables and skips low-impact ones. Databricks automatically assesses data quality by analyzing historical data patterns to evaluate each table's freshness and completeness. ^[data-quality-monitoring-databricks-on-aws.md]

The feature monitors enabled tables for two dimensions: **freshness** and **completeness**. Completeness specifically focuses on row-level expectations within a 24-hour period. ^[data-quality-monitoring-databricks-on-aws.md]

## How Completeness Detection Works

Completeness refers to the number of rows expected to be written to a table in the last 24 hours. Anomaly detection analyzes the historical row count of a table and, based on this historical data, predicts a range of expected rows. If the number of rows committed over the last 24 hours falls below the lower bound of this predicted range, the table is marked as incomplete. ^[data-quality-monitoring-databricks-on-aws.md]

This approach is fully automated and adaptive. Rather than requiring users to set static thresholds, the system builds per-table models based on each table's unique behavior and patterns over time. ^[data-quality-monitoring-databricks-on-aws.md]

## Why Completeness Matters

To draw useful insights from your data, you must have confidence in its quality. Completeness monitoring helps ensure that data pipelines are functioning correctly and that downstream consumers are not making decisions based on partial or missing data. ^[data-quality-monitoring-databricks-on-aws.md]

## Relation to Freshness

Completeness and freshness are the two dimensions of anomaly detection:

- **Freshness** analyzes the history of commits to a table and builds a per-table model to predict the time of the next commit. If a commit is unusually late, the table is marked as stale.
- **Completeness** checks whether the row count over the last 24 hours falls within the expected range based on historical patterns.

Both dimensions operate automatically without manual configuration. ^[data-quality-monitoring-databricks-on-aws.md]

## Comparison with Data Profiling

Data profiling (formerly known as Lakehouse Monitoring) is a complementary capability that provides summary statistics of table data. While anomaly detection focuses on freshness and completeness with automated thresholding, data profiling captures historical metrics on data distribution, enables custom metrics, and tracks drift over time. Anomaly detection and data profiling serve different use cases and can be used together for comprehensive data quality monitoring. ^[data-quality-monitoring-databricks-on-aws.md]

## Key Characteristics

- **Non-invasive**: Data quality monitoring does not modify any tables it monitors, nor does it add overhead to jobs that populate those tables. ^[data-quality-monitoring-databricks-on-aws.md]
- **Automated**: No manual threshold configuration is required; the system learns from historical patterns.
- **Scalable**: Intelligent scanning prioritizes important tables and skips low-impact ones across a schema.
- **Per-table modeling**: Each table receives an individualized model based on its own historical commit and row count patterns.

## Related Concepts

- [Anomaly Detection for Table Freshness](/concepts/anomaly-detection-for-table-freshness.md)
- [Data Profiling](/concepts/data-profiling.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Data Quality Monitoring on Databricks](/concepts/data-quality-monitoring-databricks.md)
- [Lakehouse Monitoring](/concepts/lakehouse-monitoring.md)

## Sources

- data-quality-monitoring-databricks-on-aws.md

# Citations

1. [data-quality-monitoring-databricks-on-aws.md](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
