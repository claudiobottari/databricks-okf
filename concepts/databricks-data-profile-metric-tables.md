---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 570662262bdd38d75912a6e2a1f201f0e19dc411997eccb5f428be5cd8490f51
  pageDirectory: concepts
  sources:
    - create-a-data-profile-using-the-api-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-data-profile-metric-tables
    - DDPMT
  citations:
    - file: create-a-data-profile-using-the-api-databricks-on-aws.md
title: Databricks Data Profile Metric Tables
description: Unity Catalog tables created by data profiling that store computed statistics and can be queried via SQL or Catalog Explorer
tags:
  - databricks
  - metric-tables
  - unity-catalog
timestamp: "2026-06-19T17:55:28.168Z"
---

# Databricks Data Profile Metric Tables

**Databricks Data Profile Metric Tables** are Unity Catalog tables automatically created when a data profile is set up on a table. They store computed statistics that can be queried to monitor data quality, drift, and inference performance over time. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Overview

When you create a data profile on a table, the profiling system generates a set of metric tables in the output schema you specify. These tables hold the actual statistics computed by the profile, such as column-level metrics (count, mean, null count, distinct count, histograms) and drift metrics when a baseline is configured. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

The metric tables are Unity Catalog tables, so you can query them using notebooks, the SQL query explorer, or view them in Catalog Explorer. This allows you to integrate profile output into your existing data pipelines and dashboards. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Creation and Location

Metric tables are created in the schema specified by `output_schema_id` during profile creation. The profile configuration also requires an `assets_dir` parameter for storing dashboard artifacts. Once the profile is refreshed (either manually via `create_refresh` or on a schedule), the metric tables are populated. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

The refresh computation runs on serverless compute, not on the notebook cluster, so notebook execution can continue while statistics are updated. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Access Control

Metric tables are owned by the user who created the profile. Access can be controlled using standard Unity Catalog privileges. Dashboards generated from the profile can be shared within the workspace using the **Share** button. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Profile Types and Corresponding Metric Tables

The three profile types — `TimeSeries`, `InferenceLog`, and `Snapshot` — each produce metric tables that reflect their specific logic:

- **TimeSeries profile**: Computes distribution comparisons across time windows defined by `granularities`. Metric tables contain statistics grouped by each time window and optional slicing expressions.
- **InferenceLog profile**: Similar to TimeSeries but includes model quality metrics (e.g., accuracy, precision for classification; RMSE for regression). Slices are automatically created per distinct value of `model_id_column`.
- **Snapshot profile**: Computes metrics over the entire table contents at each refresh, representing the full table state at that point in time. The maximum table size for a snapshot profile is 4 TB. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Refreshing and Viewing Metrics

To view or update metric tables, use the data quality API:

- `create_refresh` triggers a new computation of metrics, which creates or updates the metric tables.
- `list_refreshes` returns the history of all refresh runs.
- `get_refresh` provides the status of a specific refresh run (pending, running, finished). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Deletion

Deleting a profile via `delete_monitor` does **not** automatically delete the metric tables and dashboard. You must remove those assets separately, or configure them to be stored in a location you manage independently. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – Overview of statistical analysis on Databricks tables.
- [Profile Metrics Table](/concepts/profile-metrics-table.md) – The structured output table storing per-column statistics.
- [Drift Metrics Table](/concepts/drift-metrics-table.md) – Stores distribution change metrics when a baseline is set.
- [Inference Log Analysis](/concepts/inferencelog-analysis.md) – Profile type for tracking model predictions and quality.
- Time Series Analysis – Profile type for monitoring over continuous time windows.
- Snapshot Profiling – Profile type that captures the full table state at each refresh.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer hosting metric tables.

## Sources

- create-a-data-profile-using-the-api-databricks-on-aws.md

# Citations

1. [create-a-data-profile-using-the-api-databricks-on-aws.md](/references/create-a-data-profile-using-the-api-databricks-on-aws-e282ec7f.md)
