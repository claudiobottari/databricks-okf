---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1f5eea4da2a5a2bbae1c8056c6903e44b24ae1e78c8bb9bd63bc10e495f20127
  pageDirectory: concepts
  sources:
    - create-a-profile-using-the-databricks-ui-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-profiling-in-databricks-unity-catalog
    - DPIDUC
  citations:
    - file: create-a-profile-using-the-databricks-ui-databricks-on-aws.md
title: Data Profiling in Databricks Unity Catalog
description: The process of analyzing table statistics and data quality metrics using the Databricks UI within Unity Catalog, supporting profile types for general analysis, time series, and ML inference monitoring.
tags:
  - data-quality
  - unity-catalog
  - databricks
  - monitoring
timestamp: "2026-06-18T14:47:44.257Z"
---

# Data Profiling in Databricks Unity Catalog

**Data Profiling** in Unity Catalog is a feature that automatically computes statistics and quality metrics for tables, enabling you to monitor data health, detect anomalies, and track changes over time. Profiles can be created through the Databricks UI or the API, and are stored as Unity Catalog managed tables for querying and visualization. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Creating a Profile via the UI

Profiles are created from the **Quality** tab of a table in [Catalog Explorer](/concepts/catalog-explorer.md). The process requires that [Anomaly Detection](/concepts/anomaly-detection.md) is enabled for the schema (or already configured). ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

1. Open Catalog Explorer from the workspace sidebar.
2. Navigate to the target table.
3. Click the **Quality** tab.
4. If anomaly detection is not enabled for the schema, click **Enable**. If already enabled, click **Configure**.
5. In the **Data Quality Monitoring** dialog, click **Configure** under **Data profiling**.
6. Select the **Profile type** and fill in required parameters.

^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Profile Types

The **Profile type** drop‑down offers three options:

| Profile Type | Description | Additional Required Parameters |
|--------------|-------------|--------------------------------|
| **Profiling** | Basic column‑level statistics and quality metrics. | None |
| **TimeSeries** | Profiles data partitioned into time‑based windows. | **Metric granularities** (how to split data by time) and **Timestamp column** (must be `TIMESTAMP` or convertible via `to_timestamp`). |
| **Inference** | Monitors model inference quality (classification or regression). | All TimeSeries parameters plus: **Problem type**, **Prediction column**, optional **Label column**, and **Model ID column**. |

^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

> **Note:**  
> - When a TimeSeries or Inference profile is first created, it analyzes only the 30 days of data prior to creation. All new data is processed thereafter.  
> - Materialized views do **not** support incremental processing.  
> - Best practice: enable **change data feed (CDF)** so that only newly appended data is processed on each refresh, improving efficiency and reducing cost. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Advanced Options

### Schedule

- **Refresh on schedule** – set frequency and time for automatic profile runs.  
- **Refresh manually** – the profile only runs when triggered from the Quality tab.

### Notifications

Up to 5 email addresses can be added per notification event type.

### Metrics

- **Metrics tables schema name** – the Unity Catalog schema where metric tables are stored. Defaults to the profiled table’s schema.  
- **Assets directory** – path for storing profiling assets. Default: `/Users/{user_name}/databricks_lakehouse_monitoring/{table_name}`. Must not be blank.  
- **Unity Catalog baseline table name** – name of a table or view containing baseline data for comparison.  
- **Metric slicing expressions** – define subsets of the table to profile independently. Example: `"col_2 > 10"` creates two slices (one for the condition, one for its complement).  
- **Custom metrics** – add user‑defined metrics (types: `Aggregate`, `Derived`, or `Drift`) using SQL definitions.

^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Editing an Existing Profile

After creation, you can modify a profile’s settings by:

1. Opening the table’s **Quality** tab.
2. Clicking **Configure**.
3. In the **Data profiling** section, clicking **Configure** to open the **Update profile** dialog.

^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Refreshing and Viewing Results

To manually trigger a profile run, click **View refresh history** on the Quality tab, then **Refresh metrics**.

Profile outputs are stored in Unity Catalog **metric tables**, which can be queried in notebooks, SQL query editors, or browsed in Catalog Explorer. Refresh history is only visible from the workspace where data profiling was enabled. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Controlling Access to Profile Outputs

- Metric tables and dashboards are owned by the profile creator.  
- Access to metric tables is managed via standard [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md).  
- Dashboards can be shared within a workspace using the **Share** button.

^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Deleting a Profile

1. Open the **Update profile** dialog (see [Editing an existing profile](#editing-an-existing-profile)).
2. From the **Update** dropdown, select **Delete**.

^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Related Concepts

- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Anomaly Detection](/concepts/anomaly-detection.md)
- Monitor Metric Tables
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md)
- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md)
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)

## Sources

- create-a-profile-using-the-databricks-ui-databricks-on-aws.md

# Citations

1. [create-a-profile-using-the-databricks-ui-databricks-on-aws.md](/references/create-a-profile-using-the-databricks-ui-databricks-on-aws-d97351d2.md)
