---
title: Data profiling metric tables | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-output
ingestedAt: "2026-06-18T08:04:24.793Z"
---

This page describes the metric tables created by data profiling. For information about the dashboard created by a profile, see [Data profiling dashboard](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-dashboard).

When a profile runs on a Databricks table, it creates or updates two metric tables: a profile metrics table and a drift metrics table.

*   The profile metrics table contains summary statistics for each column and for each combination of time window, slice, and grouping columns. For `InferenceLog` analysis, the analysis table also contains model accuracy metrics.
*   The drift metrics table contains statistics that track changes in distribution for a metric. Drift tables can be used to visualize or alert on changes in the data instead of specific values. The following types of drift are computed:
    *   Consecutive drift compares a window to the previous time window. Consecutive drift is only calculated if a consecutive time window exists after aggregation according to the specified granularities.
    *   Baseline drift compares a window to the baseline distribution determined by the baseline table. Baseline drift is only calculated if a baseline table is provided.

## Where metric tables are located[​](#where-metric-tables-are-located "Direct link to Where metric tables are located")

Metric tables are saved to `{output_schema}.{table_name}_profile_metrics` and `{output_schema}.{table_name}_drift_metrics`, where:

*   `{output_schema}` is the catalog and schema specified by `output_schema_name`.
*   `{table_name}` is the name of the table being profiled.

## How profile statistics are computed[​](#how-profile-statistics-are-computed "Direct link to How profile statistics are computed")

Each statistic and metric in the metric tables is computed for a specified time interval (called a “window”). For `Snapshot` analysis, the time window is a single point in time corresponding to the time the metric was refreshed. For `TimeSeries` and `InferenceLog` analysis, the time window is based on the granularities specified in `create_monitor` and the values in the `timestamp_col` specified in the `profile_type` argument.

Metrics are always computed for the entire table. In addition, if you provide a slicing expression, metrics are computed for each data slice defined by a value of the expression.

For example:

`slicing_exprs=["col_1", "col_2 > 10"]`

generates the following slices: one for `col_2 > 10`, one for `col_2 <= 10`, and one for each unique value in `col1`.

Slices are identified in the metrics tables by the column names `slice_key` and `slice_value`. In this example, one slice key would be “col\_2 > 10” and the corresponding values would be “true” and “false”. The entire table is equivalent to `slice_key` = NULL and `slice_value` = NULL. Slices are defined by a single slice key.

Metrics are computed for all possible groups defined by the time windows and slice keys and values. In addition, for `InferenceLog` analysis, metrics are computed for each model id. For details, see [Column schemas for generated tables](#output_schema).

### Additional statistics for model accuracy (`InferenceLog` analysis only)[​](#additional-statistics-for-model-accuracy-inferencelog-analysis-only "Direct link to additional-statistics-for-model-accuracy-inferencelog-analysis-only")

Additional statistics are calculated for `InferenceLog` analysis.

*   Model quality is calculated if both `label_col` and `prediction_col` are provided.
*   Slices are automatically created based on the distinct values of `model_id_col`.
*   For classification models, [fairness and bias statistics](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/fairness-bias) are calculated for slices that have a Boolean value.

## Query analysis and drift metrics tables[​](#query-analysis-and-drift-metrics-tables "Direct link to Query analysis and drift metrics tables")

You can query the metrics tables directly. The following example is based on `InferenceLog` analysis:

SQL

    SELECT  window.start, column_name, count, num_nulls, distinct_count, frequent_itemsFROM census_monitor_db.adult_census_profile_metricsWHERE model_id = 1    — Constrain to version 1  AND slice_key IS NULL    — look at aggregate metrics over the whole data  AND column_name = "income_predicted"ORDER BY window.start

## Column schemas for generated tables[​](#column-schemas-for-generated-tables "Direct link to column-schemas-for-generated-tables")

For each column in the primary table, the metrics tables contain one row for each combination of grouping columns. The column associated with each row is shown in the column `column_name`.

For metrics based on more than one column such as model accuracy metrics, `column_name` is set to `:table`.

For profile metrics, the following grouping columns are used:

*   time window
*   granularity (`TimeSeries` and `InferenceLog` analysis only)
*   log type - input table or baseline table
*   slice key and value
*   model id (`InferenceLog` analysis only)

For drift metrics, the following additional grouping columns are used:

*   comparison time window
*   drift type (comparison to previous window or comparison to baseline table)

The schemas of the metric tables are shown below, and are also shown in the [data profiling API reference documentation](https://api-docs.databricks.com/python/data-governance/unity-catalog/data-quality-monitoring/data-profiling/latest/index.html).

### Profile metrics table schema[​](#profile-metrics-table-schema "Direct link to profile-metrics-table-schema")

The following table shows the schema of the profile metrics table. Where a metric is not applicable to a row, the corresponding cell is null.

\[1\] Format of struct for `confusion_matrix`, `precision`, `recall`, `f1_score`, and `roc_auc_score`:

\[2\] For time series or inference profiles, the profile looks back 30 days from the time the profile is created. Due to this cutoff, the first analysis might include a partial window. For example, the 30 day limit might fall in the middle of a week or month, in which case the full week or month is not included in the calculation. This issue affects only the first window.

\[3\] The version shown in this column is the version that was used to calculate the statistics in the row and might not be the current version of the profile. Each time you refresh the metrics, the profile attempts to recompute previously calculated metrics using the current profile configuration. The current profile version appears in the profile information returned by the API and Python Client.

\[4\] Sample code to retrieve the 50th percentile: `SELECT element_at(quantiles, int((size(quantiles)+1)/2)) AS p50 ...` or `SELECT quantiles[500] ...` .

\[5\] Only shown if the profile has `InferenceLog` analysis type and both `label_col` and `prediction_col` are provided.

\[6\] Only shown if the profile has `InferenceLog` analysis type and `problem_type` is `classification`.

### Drift metrics table schema[​](#drift-metrics-table-schema "Direct link to drift-metrics-table-schema")

The following table shows the schema of the drift metrics table. The drift table is only generated if a baseline table is provided, or if a consecutive time window exists after aggregation according to the specified granularities. Where a metric is not applicable to a row, the corresponding cell is null.

\[7\] For time series or inference profiles, the profile looks back 30 days from the time the profile is created. Due to this cutoff, the first analysis might include a partial window. For example, the 30 day limit might fall in the middle of a week or month, in which case the full week or month is not included in the calculation. This issue affects only the first window.

\[8\] The version shown in this column is the version that was used to calculate the statistics in the row and might not be the current version of the profile. Each time you refresh the metrics, the profile attempts to recompute previously calculated metrics using the current profile configuration. The current profile version appears in the profile information returned by the API and Python Client.

\[9\] The output of the population stability index is a numeric value that represents how different two distributions are. The range is \[0, inf). PSI < 0.1 means no significant population change. PSI < 0.2 indicates moderate population change. PSI >= 0.2 indicates significant population change.
