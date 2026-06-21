---
title: Use custom metrics with data profiling | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/custom-metrics
ingestedAt: "2026-06-18T08:04:17.520Z"
---

This page describes how to create a custom metric in data profiling. In addition to the analysis and drift statistics that are automatically calculated, you can create custom metrics. For example, you might want to track a weighted mean that captures some aspect of business logic or use a custom model quality score. You can also create custom drift metrics that track changes to the values in the primary table (compared to the baseline or the previous time window).

For more details on how to use the `MonitorMetric` API, see the [API reference](https://databricks-sdk-py.readthedocs.io/en/latest/dbdataclasses/catalog.html#databricks.sdk.service.catalog.MonitorMetric).

## Types of custom metrics[​](#types-of-custom-metrics "Direct link to types-of-custom-metrics")

Data profiling includes the following types of custom metrics:

*   Aggregate metrics, which are calculated based on columns in the primary table. Aggregate metrics are stored in the profile metrics table.
*   Derived metrics, which are calculated based on previously computed aggregate metrics and do not directly use data from the primary table. Derived metrics are stored in the profile metrics table.
*   Drift metrics, which compare previously computed aggregate or derived metrics from two different time windows, or between the primary table and the baseline table. Drift metrics are stored in the drift metrics table.

Using derived and drift metrics where possible minimizes recomputation over the full primary table. Only aggregate metrics access data from the primary table. Derived and drift metrics can then be computed directly from the aggregate metric values.

## Custom metrics parameters[​](#custom-metrics-parameters "Direct link to Custom metrics parameters")

To define a custom metric, you create a [Jinja template](https://jinja.palletsprojects.com/en/3.0.x/templates/#variables) for a SQL column expression. The tables in this section describe the parameters that define the metric, and the parameters that are used in the Jinja template.

### Create `definition`[​](#create-definition "Direct link to create-definition")

The `definition` parameter must be a single string expression in the form of a Jinja template. It cannot contain joins or subqueries.

The following table lists the parameters you can use to create a SQL Jinja Template to specify how to calculate the metric.

## Aggregate metric example[​](#aggregate-metric-example "Direct link to Aggregate metric example")

The following example computes the average of the square of the values in a column, and is applied to columns `f1` and `f2`. The output is saved as a new column in the profile metrics table and is shown in the analysis rows corresponding to the columns `f1` and `f2`. The applicable column names are substituted for the Jinja parameter `{{input_column}}`.

Python

    from databricks.sdk.service.catalog import MonitorMetric, MonitorMetricTypefrom pyspark.sql import types as TMonitorMetric(    type=MonitorMetricType.CUSTOM_METRIC_TYPE_AGGREGATE,    name="squared_avg",    input_columns=["f1", "f2"],    definition="avg(`{{input_column}}`*`{{input_column}}`)",    output_data_type=T.StructField("output", T.DoubleType()).json(),)

The following code defines a custom metric that computes the average of the difference between columns `f1` and `f2`. This example shows the use of `[":table"]` in the `input_columns` parameter to indicate that more than one column from the table is used in the calculation.

Python

    from databricks.sdk.service.catalog import MonitorMetric, MonitorMetricTypefrom pyspark.sql import types as TMonitorMetric(    type=MonitorMetricType.CUSTOM_METRIC_TYPE_AGGREGATE,    name="avg_diff_f1_f2",    input_columns=[":table"],    definition="avg(f1 - f2)",    output_data_type=T.StructField("output", T.DoubleType()).json(),)

This example computes a weighted model quality score. For observations where the `critical` column is `True`, a heavier penalty is assigned when the predicted value for that row does not match the ground truth. Because it's defined on the raw columns (`prediction` and `label`), it's defined as an aggregate metric. The `:table` column indicates that this metric is calculated from multiple columns. The Jinja parameters `{{prediction_col}}` and `{{label_col}}` are replaced with the name of the prediction and ground truth label columns for the profile.

Python

    from databricks.sdk.service.catalog import MonitorMetric, MonitorMetricTypefrom pyspark.sql import types as TMonitorMetric(    type=MonitorMetricType.CUSTOM_METRIC_TYPE_AGGREGATE,    name="weighted_error",    input_columns=[":table"],    definition="""avg(CASE      WHEN {{prediction_col}} = {{label_col}} THEN 0      WHEN {{prediction_col}} != {{label_col}} AND critical=TRUE THEN 2      ELSE 1 END)""",    output_data_type=T.StructField("output", T.DoubleType()).json(),)

## Derived metric example[​](#derived-metric-example "Direct link to Derived metric example")

The following code defines a custom metric that computes the square root of the `squared_avg` metric defined earlier in this section. Because this is a derived metric, it does not reference the primary table data and instead is defined in terms of the `squared_avg` aggregate metric. The output is saved as a new column in the profile metrics table.

Python

    from databricks.sdk.service.catalog import MonitorMetric, MonitorMetricTypefrom pyspark.sql import types as TMonitorMetric(    type=MonitorMetricType.CUSTOM_METRIC_TYPE_DERIVED,    name="root_mean_square",    input_columns=["f1", "f2"],    definition="sqrt(squared_avg)",    output_data_type=T.StructField("output", T.DoubleType()).json(),)

## Drift metrics example[​](#drift-metrics-example "Direct link to Drift metrics example")

The following code defines a drift metric that tracks the change in the `weighted_error` metric defined earlier in this section. The `{{current_df}}` and `{{base_df}}` parameters allow the metric to reference the `weighted_error` values from the current window and the comparison window. The comparison window can be either the baseline data or the data from the previous time window. Drift metrics are saved in the drift metrics table.

Python

    from databricks.sdk.service.catalog import MonitorMetric, MonitorMetricTypefrom pyspark.sql import types as TMonitorMetric(    type=MonitorMetricType.CUSTOM_METRIC_TYPE_DRIFT,    name="error_rate_delta",    input_columns=[":table"],    definition="{{current_df}}.weighted_error - {{base_df}}.weighted_error",    output_data_type=T.StructField("output", T.DoubleType()).json(),)
