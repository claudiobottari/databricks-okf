---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f8eb861a51daa90337e43ff3ba91f7dd0b2fbb7da5bf46a1f03aeed1aa58cb5c
  pageDirectory: concepts
  sources:
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - intelligent-schema-scanning
    - ISS
  citations:
    - file: data-quality-monitoring-databricks-on-aws.md
title: Intelligent Schema Scanning
description: An approach used by Databricks anomaly detection that prioritizes important tables and skips low-impact ones when monitoring all tables in a schema.
tags:
  - scanning
  - optimization
  - data-monitoring
timestamp: "2026-06-18T15:01:53.653Z"
---

# Intelligent Schema Scanning

**Intelligent Schema Scanning** is a feature of [Anomaly Detection](/concepts/anomaly-detection.md) within [Data Quality Monitoring](/concepts/data-quality-monitoring.md) on Databricks. It enables scalable, one-click monitoring of all tables in a schema by automatically prioritizing important tables and skipping low-impact ones. ^[data-quality-monitoring-databricks-on-aws.md]

## Overview

Intelligent Schema Scanning evaluates a schema’s tables and selects which ones to monitor based on their historical data patterns and likely importance. Tables that are determined to be low-impact are skipped, reducing overhead while still covering the most critical assets. This makes anomaly detection practical at scale without requiring manual configuration per table. ^[data-quality-monitoring-databricks-on-aws.md]

## How It Works

When anomaly detection is enabled for a schema, Intelligent Schema Scanning analyzes the commit history and other metadata for every table. It builds per-table models to assess each table’s freshness and completeness. Tables that are unlikely to yield actionable insights are automatically excluded from monitoring. The result is a monitoring profile that focuses resources on the tables that matter most. ^[data-quality-monitoring-databricks-on-aws.md]

## Relationship to Other Monitoring Capabilities

- **[Anomaly Detection](/concepts/anomaly-detection.md)** – The parent capability that uses Intelligent Schema Scanning to determine which tables to monitor.
- **[Data Profiling](/concepts/data-profiling.md)** – A separate but complementary capability that provides summary statistics and historical metrics for a table, allowing you to track distribution, drift, and performance over time.

## Related Concepts

- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Data governance

## Sources

- data-quality-monitoring-databricks-on-aws.md

# Citations

1. [data-quality-monitoring-databricks-on-aws.md](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
