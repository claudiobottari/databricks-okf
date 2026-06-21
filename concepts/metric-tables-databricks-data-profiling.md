---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2f2a6886be93bfcb350e263735a3fbf609bcd8b8453ad764a23d552b4ce573c3
  pageDirectory: concepts
  sources:
    - create-a-data-profile-using-the-api-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metric-tables-databricks-data-profiling
    - MT(DP
  citations:
    - file: create-a-data-profile-using-the-api-databricks-on-aws.md
title: Metric Tables (Databricks Data Profiling)
description: Unity Catalog tables created by data profiles that store computed statistics; can be queried via notebooks, SQL query explorer, or Catalog Explorer.
tags:
  - data-quality
  - unity-catalog
  - tables
timestamp: "2026-06-19T14:29:15.684Z"
---

# Metric Tables (Databricks Data Profiling)

**Metric Tables** are [Unity Catalog](/concepts/unity-catalog.md) tables created by Databricks Data Profiling to store computed statistics about a profiled table. They are generated automatically when a profile is created and are refreshed on demand or on a schedule. Metric tables allow users to query historical data quality metrics directly using SQL or Python, and they can be viewed in Catalog Explorer. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Overview

When you create a data profile on a managed or external Delta table registered in Unity Catalog, Databricks generates a set of metric tables that capture the statistics specified by the profile type—TimeSeries, InferenceLog, or Snapshot. These tables are written to an output schema you designate at profile creation time. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

Each time you call `create_refresh` to update the profile, the metric tables are recomputed. The refresh runs on serverless compute, independent of the notebook's attached cluster. The results are stored in the same output schema, and you can continue working in the notebook while the refresh completes. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Access and Permissions

Metric tables are owned by the user who created the profile. Because they are Unity Catalog tables, you control access using standard Unity Catalog privileges (e.g., `SELECT`, `MODIFY`). The associated dashboard is also owned by the profile creator; it can be shared within the workspace using the **Share** button at the upper-right of the dashboard. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Querying Metric Tables

You can query metric tables with the Databricks SQL query explorer or from notebooks using Spark SQL. The exact schemas and metric names depend on the profile type. For detailed documentation of the statistics stored, see the official [Monitor metric tables](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-output) page. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Related Concepts

- [Databricks Data Profiling](/concepts/databricks-data-profiling.md)
- Profile Types
- [Unity Catalog](/concepts/unity-catalog.md)
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)

## Sources

- create-a-data-profile-using-the-api-databricks-on-aws.md

# Citations

1. [create-a-data-profile-using-the-api-databricks-on-aws.md](/references/create-a-data-profile-using-the-api-databricks-on-aws-e282ec7f.md)
