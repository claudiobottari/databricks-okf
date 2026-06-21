---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e941ed028e18541476f3353fac9d0ce26f4c80ff6bd1a2d9cdd2cc733ae0c1f5
  pageDirectory: concepts
  sources:
    - create-a-profile-using-the-databricks-ui-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-metrics-and-slicing-expressions
    - Slicing Expressions and Custom Metrics
    - CMASE
  citations:
    - file: create-a-profile-using-the-databricks-ui-databricks-on-aws.md
title: Custom Metrics and Slicing Expressions
description: Advanced profiling options allowing users to define custom SQL-based metrics and slice data into subsets for granular analysis alongside default metrics.
tags:
  - data-profiling
  - custom-metrics
  - slicing
timestamp: "2026-06-19T17:56:46.791Z"
---

# Custom Metrics and Slicing Expressions

**Custom Metrics and Slicing Expressions** are advanced configuration options in Databricks data profiling that allow users to extend the built-in monitoring capabilities with user-defined calculations and population subsets. These features are configured during the creation or editing of a data profile through the Databricks UI.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Overview

When creating a [Data Profiling on Databricks|data profile](/concepts/data-profiling-in-databricks.md), you can enhance the standard analysis by adding custom computations and defining subsets of your data for separate analysis. Both custom metrics and slicing expressions are configured in the **Metrics** section under **Advanced options** in the data profiling setup dialog.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Custom Metrics

Custom metrics let you define user‑defined quantitative measures that appear in the metric tables alongside the built-in metrics. Each custom metric requires specifying a name, type, input columns, output data type, and a SQL definition that implements the metric logic.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### Configuration Fields

- **Name**: A descriptive label for the metric.
- **Type**: One of `Aggregate`, `Derived`, or `Drift`. The type determines how the metric is computed and interpreted.
- **Input columns**: The columns from the table that the metric operates on.
- **Output type**: The Spark data type of the metric’s result (e.g., `DOUBLE`, `BIGINT`).
- **Definition**: SQL code that implements the metric logic, written in valid Spark SQL.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

Custom metrics are useful for tracking domain‑specific quantities such as custom business KPIs, derived ratios, or calculations not covered by the default profiling statistics.

## Slicing Expressions

Slicing expressions define subsets—or *slices*—of the profiled table. The profiling engine computes metrics independently for each slice as well as for the entire table, enabling segment‑level comparisons and analysis.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### How Slicing Works

- A simple predicate expression like `"col_2 > 10"` automatically generates two complementary slices: one where the condition is true (`col_2 > 10`) and one where it is false (`col_2 <= 10`).^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- An expression that names a column (e.g., `"col_1"`) generates one slice for each unique value in that column.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- Multiple slicing expressions can be added; each is evaluated independently, producing its own set of slices.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### Use Cases

- **Segment‑level monitoring**: Profile data quality separately for high‑value vs. low‑value transaction records.
- **Categorical breakdown**: Automatically generate slices for every category in a column (e.g., product region, customer tier).
- **Anomaly detection**: Combine slicing with Anomaly Detection for Data Quality|anomaly detection to identify deviations in specific data segments.

## Configuration in the UI

To configure custom metrics and slicing expressions:

1. Open Catalog Explorer and navigate to the target table.
2. Click the **Quality** tab.
3. If data profiling is not enabled, click **Enable**; otherwise click **Configure**.
4. In the **Data Quality Monitoring** dialog, click **Configure** next to **Data profiling**.
5. In the expanded **Advanced options** section, under **Metrics**:
   - For **Custom metrics**: Click **Add custom metric** and fill in the fields (name, type, input columns, output type, definition).
   - For **Metric slicing expressions**: Click **Add expression** and enter the expression definition.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Storage and Querying

Custom metrics and slicing results are stored in the [Monitor Metric Tables|profile metric tables](/concepts/profile-metric-tables.md) created by the data profile. These are Unity Catalog tables that can be queried in notebooks, the SQL query explorer, or viewed in Catalog Explorer.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Editing and Managing

After a profile is created, you can edit custom metrics and slicing expressions by clicking **Configure** on the **Quality** tab and selecting **Configure** in the **Data profiling** section of the dialog. The update dialog allows modifying existing settings.^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Related Concepts

- [Data Profiling on Databricks](/concepts/data-profiling-in-databricks.md)
- [Profile Metrics Table](/concepts/profile-metrics-table.md)
- [Drift Metrics Table](/concepts/drift-metrics-table.md)
- Anomaly Detection for Data Quality
- [Catalog Explorer](/concepts/catalog-explorer.md)
- Monitor Metric Tables
- [30-Day Lookback Window](/concepts/30-day-lookback-window.md)

## Sources

- create-a-profile-using-the-databricks-ui-databricks-on-aws.md

# Citations

1. [create-a-profile-using-the-databricks-ui-databricks-on-aws.md](/references/create-a-profile-using-the-databricks-ui-databricks-on-aws-d97351d2.md)
