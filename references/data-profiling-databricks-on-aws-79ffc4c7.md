---
title: Data profiling | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/
ingestedAt: "2026-06-18T08:04:12.940Z"
---

This article describes data profiling. It gives an overview of the components and usage of data profiling.

Data profiling provides summary statistics for a table, computing profiling metrics over time so you can easily view historical trends. It is useful for in-depth monitoring of all key metrics for select tables. You can also use it to track the performance of machine learning models and model-serving endpoints by profiling inference tables that contain model inputs and predictions. The diagram shows the flow of data through data and ML pipelines in Databricks, and how you can use profiling to continuously track data quality and model performance.

![Data profiling overview](https://docs.databricks.com/aws/en/assets/images/lakehouse-monitoring-overview-2b9bad8d4d90e166a1844c9830486921.png)

## Why use data profiling?[​](#why-use-data-profiling "Direct link to Why use data profiling?")

Quantitative metrics help you track and confirm the quality and consistency of your data over time. When you detect changes in your table's data distribution or corresponding model's performance, the tables created by data profiling can capture and alert you to the change and can help you identify the cause.

Data profiling helps you answer questions like the following:

*   What does data integrity look like, and how does it change over time? For example, what is the fraction of null or zero values in the current data, and has it increased?
*   What does the statistical distribution of the data look like, and how does it change over time? For example, what is the 90th percentile of a numerical column? Or, what is the distribution of values in a categorical column, and how does it differ from yesterday?
*   Is there drift between the current data and a known baseline, or between successive time windows of the data?
*   What does the statistical distribution or drift of a subset or slice of the data look like?
*   How are ML model inputs and predictions shifting over time?
*   How is model performance trending over time? Is model version A performing better than version B?

In addition, data profiling lets you control the time granularity of observations and set up custom metrics.

## Requirements[​](#requirements "Direct link to requirements")

*   Your workspace must be enabled for Unity Catalog and you must have access to Databricks SQL.
*   To enable data profiling, you must have the following privileges:
    *   `USE CATALOG` on the catalog and `USE SCHEMA` on the schema containing the table.
    *   `SELECT` on the table.
    *   `MANAGE` on the catalog, schema, or table.

note

Data profiling uses serverless compute for jobs but does not require that your account be enabled for serverless compute. For information about tracking expenses, see [View data quality monitoring expenses](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/expense).

## How data profiling works[​](#how-data-profiling-works "Direct link to How data profiling works")

To profile a table, you create a profile attached to the table. To profile the performance of a machine learning model, you attach the profile to an inference table that holds the model's inputs and corresponding predictions.

Data profiling provides the following types of analysis: time series, inference, and snapshot.

This section briefly describes the input tables used by data profiling and the metric tables it produces. The diagram shows the relationship between the input tables, the metric tables, the profile, and the dashboard.

![Data profiling diagram](https://docs.databricks.com/aws/en/assets/images/lakehouse-monitoring-1795712375f648c67cef310c2e287ff5.png)

### Primary table and baseline table[​](#primary-table-and-baseline-table "Direct link to primary-table-and-baseline-table")

In addition to the table to be profiled, called the “primary table”, you can optionally specify a baseline table to use as a reference for measuring drift, or the change in values over time. A baseline table is useful when you have a sample of what you expect your data to look like. The idea is that drift is then computed relative to expected data values and distributions.

The baseline table should contain a dataset that reflects the expected quality of the input data, in terms of statistical distributions, individual column distributions, missing values, and other characteristics. It should match the schema of the profiled table. The exception is the timestamp column for tables used with time series or inference profiles. If columns are missing in either the primary table or the baseline table, profiling uses best-effort heuristics to compute the output metrics.

For profiles that use a snapshot profile, the baseline table should contain a snapshot of the data where the distribution represents an acceptable quality standard. For example, on grade distribution data, one might set the baseline to a previous class where grades were distributed evenly.

For profiles that use a time series profile, the baseline table should contain data that represents time windows where data distributions represent an acceptable quality standard. For example, on weather data, you might set the baseline to a week, month, or year where the temperature was close to expected normal temperatures.

For profiles that use an inference profile, a good choice for a baseline is the data that was used to train or validate the model being profiled. In this way, users can be alerted when the data has drifted relative to what the model was trained and validated on. This table should contain the same feature columns as the primary table, and additionally should have the same `model_id_col` that was specified for the primary table's InferenceLog so that the data is aggregated consistently. Ideally, the test or validation set used to evaluate the model should be used to ensure comparable model quality metrics.

### Metric tables and dashboard[​](#metric-tables-and-dashboard "Direct link to Metric tables and dashboard")

Profiling creates two metric tables and a dashboard. Metric values are computed for the entire table, and for the time windows and data subsets (or “slices”) that you specify when you create the profile. In addition, for inference analysis, metrics are computed for each model ID. For more details about the metric tables, see [Data profiling metric tables](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-output).

*   The profile metric table contains summary statistics. See the [profile metrics table schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-output#profile-metrics-table).
*   The drift metrics table contains statistics related to the data's drift over time. If a baseline table is provided, drift is also profiled relative to the baseline values. See the [drift metrics table schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-output#drift-metrics-table).

The metric tables are Delta tables and are stored in a Unity Catalog schema that you specify. You can view these tables using the Databricks UI, query them using Databricks SQL, and create dashboards and alerts based on them.

For each profile, Databricks automatically creates a dashboard to help you visualize and present the profile results. The dashboard is fully customizable. See [Dashboards](https://docs.databricks.com/aws/en/dashboards/).

## Limitations[​](#limitations "Direct link to Limitations")

*   Only Delta tables are supported for profiling, and the table must be one of the following table types: managed tables, external tables, views, materialized views, or streaming tables.
*   Profiles created over materialized views do not support incremental processing.
*   Not all regions are supported. For regional support, see the column **Data profiling** in the table [AI and machine learning features availability](https://docs.databricks.com/aws/en/resources/feature-region-support#ai-aws).
*   Profiles created using the time series or inference analysis modes only compute metrics over the last 30 days. If you need to adjust this, contact your Databricks account team.
*   The maximum table size for a snapshot profile is 4TB. For larger tables, use time series profiles instead.

## Start using data profiling[​](#start-using-data-profiling "Direct link to Start using data profiling")

See the following articles to get started:

*   [Create a profile using the Databricks UI](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-ui).
*   [Create a data profile using the API](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-api).
*   [Data profiling metric tables](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-output).
*   [Data profiling dashboard](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-dashboard).
*   [Profile alerts](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-alerts).
*   [Use custom metrics with data profiling](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/custom-metrics).
*   [Monitor served models using Unity AI Gateway\-enabled inference tables](https://docs.databricks.com/aws/en/ai-gateway/inference-tables).
*   [Monitor fairness and bias for classification models](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/fairness-bias).
*   See the reference material for the [data profiling API](https://api-docs.databricks.com/python/lakehouse-monitoring/latest/index.html).
*   [Example notebooks](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-api#example-notebooks).
