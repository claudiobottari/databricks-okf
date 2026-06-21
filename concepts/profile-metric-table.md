---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8a476bb4c6c6cac4425971150802670a125826955eda3028e4a81bd04a5e48ee
  pageDirectory: concepts
  sources:
    - data-profiling-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - profile-metric-table
    - PMT
  citations:
    - file: data-profiling-databricks-on-aws.md
title: Profile Metric Table
description: An output table created by data profiling containing summary statistics for a table, stored as a Delta table in Unity Catalog, with metrics computed for time windows and data slices.
tags:
  - data-quality
  - monitoring
  - databricks
  - delta-lake
timestamp: "2026-06-19T14:42:49.325Z"
---

```markdown
---
title: Profile Metric Table
summary: A Delta table produced by data profiling containing summary statistics (e.g., null fractions, percentiles, value distributions) for the profiled table, stored in Unity Catalog.
sources:
  - data-profiling-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:44:34.457Z"
updatedAt: "2026-06-19T09:44:34.457Z"
tags:
  - data-quality
  - monitoring
  - delta-table
  - unity-catalog
aliases:
  - profile-metric-table
  - PMT
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Profile Metric Table

A **Profile Metric Table** is one of the two metric tables automatically created by [[Data Profiling]] in Databricks Unity Catalog. It contains summary statistics that describe the distribution and quality of data in a profiled table, computed over specified time windows, data slices, and (for inference profiles) model IDs. ^[data-profiling-databricks-on-aws.md]

## Contents

The profile metric table stores summary statistics for each column of the primary table. Examples of the metrics captured include the fraction of null or zero values, percentiles (e.g., the 90th percentile of a numerical column), and the distribution of values in categorical columns. These statistics are computed for the entire table, for the time granularity and data subsets (slices) specified when the profile was created, and for each model ID when profiling an inference table. ^[data-profiling-databricks-on-aws.md]

The full schema is documented in Databricks’ [profile metrics table schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-output#profile-metrics-table). ^[data-profiling-databricks-on-aws.md]

## Storage and Access

Profile metric tables are [[Delta Lake Table|Delta Tables]] stored in a Unity Catalog schema that you specify during profile creation. They can be queried with Databricks SQL, viewed in the Databricks UI, and used as the basis for custom dashboards and alerts. ^[data-profiling-databricks-on-aws.md]

For each profile, Databricks automatically generates a dashboard that visualizes the metric table data. The dashboard is fully customizable. ^[data-profiling-databricks-on-aws.md]

## Relationship to Drift Metrics Table

Data profiling creates two metric tables per profile: the profile metric table and the [[Drift Metrics Table]]. While the profile metric table focuses on summary statistics, the drift metrics table captures change in data distributions over time or relative to a baseline. Both tables are Delta tables stored in Unity Catalog and are used together to monitor data quality and consistency. ^[data-profiling-databricks-on-aws.md]

## Use Cases

- **Data integrity monitoring**: Track null ratios, zero values, and other quality indicators over time.
- **Distributional changes**: Observe shifts in percentiles, categorical distributions, or other statistical properties.
- **Model performance monitoring**: When profiling an inference table, the metric table can help track model inputs and predictions over time, enabling comparison between model versions. ^[data-profiling-databricks-on-aws.md]

## Related Concepts

- [[Data Profiling]] – The overall system that creates the metric tables.
- [[Drift Metrics Table]] – The companion table for change detection.
- [[Unity Catalog]] – The governance layer where metric tables are stored.
- Databricks SQL – Used to query metric tables.
- [[Delta Lake Table|Delta Tables]] – The storage format for metric tables.
- Dashboards (Databricks) – Visualizations built from metric tables.
- [[Data Quality Monitoring]] – The broader practice of tracking data health.
- [[Inference Tables]] – Tables that hold model inputs and predictions for profiling.

## Sources

- data-profiling-databricks-on-aws.md
```

# Citations

1. [data-profiling-databricks-on-aws.md](/references/data-profiling-databricks-on-aws-79ffc4c7.md)
