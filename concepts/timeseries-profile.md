---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 408fce329f174af02b8afc2b8f9340383616a92a38c91b63fc691d676d8a8240
  pageDirectory: concepts
  sources:
    - create-a-data-profile-using-the-api-databricks-on-aws.md
    - create-a-profile-using-the-databricks-ui-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - timeseries-profile
    - TimeSeries profiles
  citations:
    - file: create-a-data-profile-using-the-api-databricks-on-aws.md
    - file: create-a-profile-using-the-databricks-ui-databricks-on-aws.md
title: TimeSeries Profile
description: A data profile type that compares data distributions across time windows using a timestamp column and granularities
tags:
  - databricks
  - time-series
  - data-profiling
timestamp: "2026-06-19T17:55:02.061Z"
---

# TimeSeries Profile

**TimeSeries Profile** is a [Data Profiling](/concepts/data-profiling.md) type in Databricks that compares data distributions across configurable time windows. It uses a timestamp column to partition data into successive windows and computes statistics for each window, enabling trend analysis and anomaly detection over time. ^[create-a-data-profile-using-the-api-databricks-on-aws.md, create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Requirements

Before creating a TimeSeries profile, the following conditions must be met:

1. The table must be a managed or external Delta table registered in [Unity Catalog](/concepts/unity-catalog.md). Only one profile per table per [Metastore](/concepts/metastore.md) is allowed. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]
2. A timestamp column is required. The data type must be `TIMESTAMP` or convertible using the `to_timestamp` [PySpark function](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.to_timestamp.html). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]
3. At least one granularity must be selected (see below). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Granularities

The following aggregation granularities are available: ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

- `AGGREGATION_GRANULARITY_5_MINUTES`
- `AGGREGATION_GRANULARITY_30_MINUTES`
- `AGGREGATION_GRANULARITY_1_HOUR`
- `AGGREGATION_GRANULARITY_1_DAY`
- `AGGREGATION_GRANULARITY_1_WEEK`
- `AGGREGATION_GRANULARITY_2_WEEKS`
- `AGGREGATION_GRANULARITY_3_WEEKS`
- `AGGREGATION_GRANULARITY_4_WEEKS`
- `AGGREGATION_GRANULARITY_1_MONTH`
- `AGGREGATION_GRANULARITY_1_YEAR`

Multiple granularities can be specified simultaneously; metrics are computed independently for each window size. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

## Initial Behavior

When a TimeSeries profile is created for the first time, only data from the 30 days prior to creation is analyzed. After creation, all newly appended data is processed incrementally on each refresh. ^[create-a-data-profile-using-the-api-databricks-on-aws.md, create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

Profiles defined on materialized views do **not** support incremental processing; they re-scan the full view on every refresh. ^[create-a-data-profile-using-the-api-databricks-on-aws.md, create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Best Practice: Enable Change Data Feed

It is a best practice to enable [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) (CDF) on the source table. When CDF is enabled, only newly appended data is processed, rather than re‑scanning the entire table each refresh. This makes execution more efficient and reduces costs as you scale profiling across many tables. ^[create-a-data-profile-using-the-api-databricks-on-aws.md, create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Creating a TimeSeries Profile

### Using the API (Python SDK)

The following example creates a TimeSeries profile on a table. The object type is always `"table"`. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.dataquality import Monitor, DataProfilingConfig, TimeSeriesConfig, AggregationGranularity

w = WorkspaceClient()
schema = w.schemas.get(full_name=f"{catalog}.{schema}")
table = w.tables.get(full_name=f"{catalog}.{schema}.{table_name}")

config = DataProfilingConfig(
    output_schema_id=schema.schema_id,
    assets_dir=f"/Workspace/Users/{username}/databricks_quality_monitoring/{TABLE_NAME}",
    time_series=TimeSeriesConfig(
        timestamp_column="ts",
        granularities=[AggregationGranularity.AGGREGATION_GRANULARITY_1_DAY]
    ),
    slicing_exprs=["type='Red'"]
)

info = w.data_quality.create_monitor(
    monitor=Monitor(
        object_type="table",
        object_id=table.table_id,
        data_profiling_config=config,
    ),
)
```

After creation, trigger an initial refresh with `create_refresh` (see Refresh and View Results). ^[create-a-data-profile-using-the-api-databricks-on-aws.md]

### Using the Databricks UI

1. In the workspace left sidebar, click the **Catalog** icon to open Catalog Explorer.
2. Navigate to the table you want to profile.
3. Click the **Quality** tab.
4. If anomaly detection is not yet enabled for the schema, click **Enable**; otherwise click **Configure**.
5. In the **Data Quality Monitoring** dialog, in the **Data profiling** field, click **Configure**.
6. From the **Profile type** drop-down, select **TimeSeries**.
7. Under **Metric granularities**, select the desired time windows.
8. Under **Timestamp column**, pick the column containing timestamps.
9. Optionally configure advanced options (see Advanced Options).
10. Click **Create profile**.

^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Refresh and View Results

- **API**: Call `create_refresh` to trigger an immediate refresh. The calculation runs on serverless compute, not on the notebook cluster. Use `list_refreshes` and `get_refresh` to monitor status. ^[create-a-data-profile-using-the-api-databricks-on-aws.md]
- **UI**: On the **Quality** tab, click **View refresh history**, then click **Refresh metrics**. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

Results are stored in Unity Catalog metric tables. You can query them in notebooks, the SQL query explorer, or view them in Catalog Explorer. ^[create-a-data-profile-using-the-api-databricks-on-aws.md, create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Schedule

To run the profile on a recurring schedule, provide a cron expression and timezone during creation. In the UI, enable **Refresh on schedule** and select the frequency and time. If not scheduled, select **Refresh manually** and trigger refreshes from the Quality tab. ^[create-a-data-profile-using-the-api-databricks-on-aws.md, create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Notifications

Email alerts can be configured for profile refresh failures or timeouts. Up to 5 email addresses are supported per event type. ^[create-a-data-profile-using-the-api-databricks-on-aws.md, create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Advanced Options

In the UI (or via API parameters), you can configure: ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

- **Metrics tables schema name**: The Unity Catalog schema where metric tables are stored (defaults to the same schema as the profiled table).
- **Assets directory**: Absolute path to store profiling assets.
- **Baseline table name**: Name of a table or view containing baseline data for comparison.
- **Metric slicing expressions**: Define subsets of the table to profile independently (e.g., `"col_2 > 10"` generates slices for `col_2 > 10` and `col_2 <= 10`; `"col_1"` generates one slice per unique value).
- **Custom metrics**: User‑defined SQL expressions (Aggregate, Derived, or Drift) that appear in metric tables alongside built‑in metrics.

## Editing and Deleting a Profile

- **Edit**: In the UI, revisit the **Quality** tab, click **Configure**, and modify settings. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Delete**: In the UI, open the **Update profile** dialog and select **Delete** from the dropdown. Using the API, call `delete_monitor`. This does **not** delete the metric tables or dashboard — these must be removed separately. ^[create-a-data-profile-using-the-api-databricks-on-aws.md, create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Access Control

The metric tables and dashboard created by a profile are owned by the user who created the profile. Standard Unity Catalog privileges control access to metric tables. Dashboards can be shared using the **Share** button. ^[create-a-data-profile-using-the-api-databricks-on-aws.md, create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – Overview of all profile types
- [InferenceLog Profile](/concepts/inferencelog-profile.md) – Profile type for model monitoring with prediction and label columns
- [Snapshot Profile](/concepts/snapshot-profile.md) – Profile type that captures full table state at each refresh
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that stores metric tables
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) – Feature that enables efficient incremental refreshes

## Sources

- create-a-data-profile-using-the-api-databricks-on-aws.md
- create-a-profile-using-the-databricks-ui-databricks-on-aws.md

# Citations

1. [create-a-data-profile-using-the-api-databricks-on-aws.md](/references/create-a-data-profile-using-the-api-databricks-on-aws-e282ec7f.md)
2. [create-a-profile-using-the-databricks-ui-databricks-on-aws.md](/references/create-a-profile-using-the-databricks-ui-databricks-on-aws-d97351d2.md)
