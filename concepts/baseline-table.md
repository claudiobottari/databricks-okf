---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 130531c5ac01f928d4fc9ca2359a74eceb4f68c4d7bcfca6044f415084c9bd75
  pageDirectory: concepts
  sources:
    - data-profiling-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - baseline-table
  citations:
    - file: data-profiling-databricks-on-aws.md
title: Baseline Table
description: An optional reference table in Databricks data profiling used to compute drift metrics relative to expected data distributions and quality standards.
tags:
  - data-quality
  - drift-detection
  - databricks
timestamp: "2026-06-19T18:06:51.316Z"
---

# Baseline Table

A **Baseline Table** is an optional reference table used in [Data Profiling](/concepts/data-profiling.md) to measure drift in a profiled primary table. It represents a “ground truth” dataset showing the expected distribution, quality, and statistical characteristics of your data. When provided, drift metrics are computed relative to the baseline values, enabling detection of unexpected changes in data quality or distribution over time. ^[data-profiling-databricks-on-aws.md]

## General Requirements

A baseline table should contain a dataset that reflects the expected quality of the input data — including statistical distributions, individual column distributions, missing values, and other characteristics. It must match the schema of the profiled table, with the exception of the timestamp column for tables used with time series or inference profiles. If columns are missing in either the primary table or the baseline table, profiling uses best-effort heuristics to compute output metrics. ^[data-profiling-databricks-on-aws.md]

## Choosing a Baseline Table by Profile Type

### Snapshot Profiles

For snapshot profiles, the baseline should be a snapshot of data where the distribution represents an acceptable quality standard. For example, on grade distribution data, you might set the baseline to a previous class where grades were distributed evenly. ^[data-profiling-databricks-on-aws.md]

### Time Series Profiles

For time series profiles, the baseline should contain data representing time windows where data distributions represent an acceptable quality standard. For example, on weather data, you might set the baseline to a week, month, or year where the temperature was close to expected normal temperatures. ^[data-profiling-databricks-on-aws.md]

### Inference Profiles

For inference profiles, a good choice for a baseline is the data used to train or validate the model being profiled. This allows alerting when the data has drifted relative to what the model was trained and validated on. The baseline table should contain the same feature columns as the primary table and should have the same `model_id_col` specified for the primary table's InferenceLog, so data is aggregated consistently. Ideally, the test or validation set used to evaluate the model should be used to ensure comparable model quality metrics. ^[data-profiling-databricks-on-aws.md]

## Relationship to Other Profiling Components

The baseline table is one of the input tables in data profiling. Profiling produces two metric tables: a profile metrics table containing summary statistics, and a drift metrics table containing statistics related to the data's drift over time. If a baseline table is provided, drift is also profiled relative to the baseline values, providing meaningful context for detecting when data deviates from expected norms. ^[data-profiling-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md)
- Primary Table
- [Drift Metrics Table](/concepts/drift-metrics-table.md)
- [Profile Metrics Table](/concepts/profile-metrics-table.md)
- [Snapshot Profile](/concepts/snapshot-profile.md)
- [Time Series Profile](/concepts/time-series-profile.md)
- [Inference Profile](/concepts/inference-profile.md)

## Sources

- data-profiling-databricks-on-aws.md

# Citations

1. [data-profiling-databricks-on-aws.md](/references/data-profiling-databricks-on-aws-79ffc4c7.md)
