---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3b5986be344e689cddb884aa4b3a4cd40bf2fc24d6380d5d8b7c842c60c20e1e
  pageDirectory: concepts
  sources:
    - create-a-profile-using-the-databricks-ui-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-metrics-for-data-profiling
    - CMFDP
  citations:
    - file: create-a-profile-using-the-databricks-ui-databricks-on-aws.md
title: Custom Metrics for Data Profiling
description: User-defined SQL-based metrics that augment built-in profiling metrics, with configurable types (Aggregate, Derived, Drift), input columns, output types, and SQL definitions.
tags:
  - data-profiling
  - data-quality
  - sql
  - customization
timestamp: "2026-06-19T14:30:12.455Z"
---

# Custom Metrics for Data Profiling

**Custom metrics** are user-defined calculations that extend the built-in metrics available in [Data Profiling](/concepts/data-profiling.md). They allow you to define additional summary statistics, drift measures, or other aggregations beyond the system-provided set.

## Overview

Data profiling provides summary statistics for a table and computes profiling metrics over time. In addition to the built-in metrics, you can set up custom metrics to track data quality measures that are specific to your use case. Custom metrics appear in the metric tables like any built-in metric, and they can be configured when creating or editing a profile. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Configuration

Custom metrics are configured in the **Advanced options** section of the data profiling dialog. To add a custom metric, click **Add custom metric** and provide the following fields: ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

- **Name** – A human-readable identifier for the custom metric.
- **Type** – The category of metric. Choose from `Aggregate`, `Derived`, or `Drift`.
- **Input columns** – The columns to apply the metric to, selected from a drop-down list.
- **Output type** – The Spark data type of the metric’s result.
- **Definition** – SQL code that defines how the custom metric is computed.

After creation, custom metrics are computed alongside the system-generated metrics in every profile run. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Usage

Custom metrics are stored in the profile’s [Metric Tables](/concepts/profile-metric-tables.md) and can be queried using Databricks SQL or viewed in Catalog Explorer. They can also be included in the [Profile Dashboard](/concepts/profile-dashboard-databricks.md) visualizations and used to create alert rules ([Profile Alerts](/concepts/profile-alerts.md)) that trigger when metric values cross defined thresholds. Because custom metrics behave like built-in metrics, all profiling time windows and data slicing configurations apply equally to them.

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – The overall feature for monitoring table statistics
- [Metric Tables](/concepts/profile-metric-tables.md) – The system tables that store profiling output, including custom metrics
- [Profile Dashboard](/concepts/profile-dashboard-databricks.md) – The automatically generated visualization for profile results
- [Profile Alerts](/concepts/profile-alerts.md) – Alert rules that can reference custom metrics
- [Metric Slicing Expressions](/concepts/metric-slicing-expressions.md) – Define subsets of data to profile alongside custom metrics

## Sources

- create-a-profile-using-the-databricks-ui-databricks-on-aws.md

# Citations

1. [create-a-profile-using-the-databricks-ui-databricks-on-aws.md](/references/create-a-profile-using-the-databricks-ui-databricks-on-aws-d97351d2.md)
