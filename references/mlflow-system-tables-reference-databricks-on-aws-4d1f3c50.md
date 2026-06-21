---
title: MLflow system tables reference | Databricks on AWS
source: https://docs.databricks.com/aws/en/admin/system-tables/mlflow
ingestedAt: "2026-06-18T08:02:46.107Z"
---

The `mlflow` system tables capture experiment metadata managed within the [MLflow tracking service](https://docs.databricks.com/aws/en/mlflow/tracking). These tables allow privileged users to take advantage of Databricks lakehouse tooling on their MLflow data across all workspaces within the region. You can use the tables to build custom AI/BI dashboards, set up SQL alerts, or perform large-scale analytical queries.

Through the `mlflow` system tables, users can answer questions like:

*   Which experiments have the lowest reliability?
*   What is the average GPU utilization across different experiments?

note

The `mlflow` system tables began recording MLflow data from all regions on September 2, 2025. Data from before that date may not be available.

## Available tables[​](#available-tables "Direct link to Available tables")

The `mlflow` schema includes the following tables:

*   `system.mlflow.experiments_latest`: Records experiment names and soft-deletion events. This data is similar to the [experiments page](https://docs.databricks.com/aws/en/mlflow/experiments) in the MLflow UI.
*   `system.mlflow.runs_latest`: Records run-lifecycle information, the params and tags associated with each run, and aggregated stats of min, max, and latest values of all metrics. This data is similar to the [runs search or runs detail page](https://docs.databricks.com/aws/en/mlflow/runs).
*   `system.mlflow.run_metrics_history`: Records the name, value, timestamp, and step of all metrics logged on runs, which can be used to plot detailed timeseries from runs. This data is similar to the metrics tab on the [runs detail page](https://docs.databricks.com/aws/en/mlflow/runs).

The following is an example of plotting run information using a dashboard:

![run details dashboard](https://docs.databricks.com/aws/en/assets/images/dashboard-run-details-7e80c6353e0efb82d838f0cf2ddbc1ad.png)

## Table schemas[​](#table-schemas "Direct link to Table schemas")

Below are the table schemas with descriptions and example data.

![ER diagram](https://docs.databricks.com/aws/en/assets/images/er-diagram-8687a2649617fa4db6f86ea4604bfbdc.svg)

### `system.mlflow.experiments_latest`[​](#systemmlflowexperiments_latest "Direct link to systemmlflowexperiments_latest")

### `system.mlflow.runs_latest`[​](#systemmlflowruns_latest "Direct link to systemmlflowruns_latest")

### `system.mlflow.run_metrics_history`[​](#systemmlflowrun_metrics_history "Direct link to systemmlflowrun_metrics_history")

## Sharing access with users[​](#sharing-access-with-users "Direct link to Sharing access with users")

By default, only account admins have access to system schemas. To give additional users access to the tables, an account admin must grant them the USE and SELECT permissions on the `system.mlflow.` schema. See [Unity Catalog privileges reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference).

**Any user who has access to these tables can view metadata across all MLflow experiments for all workspaces in the account**. To configure table access for a given group rather than individual users, see [Unity Catalog best practices](https://docs.databricks.com/aws/en/data-governance/unity-catalog/best-practices).

If you require finer-grained control than granting all users access to the table, you can use [dynamic views](https://docs.databricks.com/aws/en/views/dynamic) with custom criteria to grant groups certain access. For example, you could create a view that only shows records from a particular set of experiment IDs. After configuring a custom view, give the name of the view to your users so that they can query the dynamic view rather than the system table directly.

The following sections give examples of how you can use the MLflow system tables to answer questions about your MLflow experiments and runs.

### Configure a SQL alert for low experiment reliability[​](#configure-a-sql-alert-for-low-experiment-reliability "Direct link to Configure a SQL alert for low experiment reliability")

Using [Databricks SQL alerts](https://docs.databricks.com/aws/en/sql/user/alerts/), you can schedule a regularly recurring query and be notified if certain constraints are no longer met.

This example creates an alert that examines the most frequently run experiments within your workspace to determine whether they are experiencing low reliability and may need special attention. The query uses the `runs_latest` table to calculate the runs per experiment that are marked as finished, divided by the total number of runs.

1.  Click ![Alerts Icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAHqADAAQAAAABAAAAHgAAAADKQTcFAAAB6UlEQVRIDWNUsHT6zzAAgGkA7ARbOfIsZiElqGXEJRjyU+IYZCQlGCyM9MFaT5y7yPDk+QuGiXMWMTx5+YJo4xiJTVxJYcFgS/l4eLAa/unLF4YJcxYyzF+1Dqs8uiBRFtflZzMkhgeB9c5fuY5h16EjDCfOXwTzLQz1GdzsbFDkmyZORbcHg0/QYjdbG4aZnY0Mn798ZUgrr4VbiG4SyAGzOpsZeHm4GdLL6xl2HT6CrgSFTzBV99SWgTU0TZiK01KQAlAIgIIaBLprS8E0PgKvxVrKKmAfXL99l2HNtp34zAHLzVu1lgGkFpQOQHrxAfwWqyuD9V4DGkYsgKnVgurFpQ+vxaBsAwKg7EIsgKmF6cWlD6/FuDRRQ3zUYmqEIlFmDM6gRlQEF4jyBUjRiXMQtTC9uDTi9DGoENBUJT8fg/TiqlBAjsFpcU9NGVjjSWBRCKp5iAUgtSA9IEu7gWbgAlgrCVjFgEsTKeK4KgycPibFcHxqP335jFUaq4+xqqSyIEk+BkXB/WN7GfKT4sBxCIpHEBskBqqPSQEktblgBhekxDOAMCWAWUBWsYFYA+4+esSw+8AxBjERIQYxYWGGX79+Mxw6cZohr6aV4fy168QaA1Y3NOKYJC8RUExS4iJgFknSA2YxAIN1nX+i24hIAAAAAElFTkSuQmCC) Alerts in the sidebar and click **Create Alert**.
    
2.  Copy and paste the following query in the query editor.
    
    SQL
    
         SELECT   experiment_id,   AVG(CASE WHEN status = 'FINISHED' THEN 1.0 ELSE 0.0 END) AS success_ratio,   COUNT(status) AS run_count FROM system.mlflow.runs_latest WHERE status IS NOT NULL GROUP BY experiment_id ORDER BY run_count DESC LIMIT 20;
    
3.  In the **Condition** field, set the conditions to `MIN success_ratio < 0.9`. This will trigger the alert if any of the top 20 experiments (by number of runs) has a success ratio less than 90%.
    

Additionally, you can test the condition, set a schedule, and configure notifications. For more information on configuring the alert, see [setting up a SQL alert](https://docs.databricks.com/aws/en/sql/user/alerts/). Below is an example configuration using the query.

![SQL alert configuration](https://docs.databricks.com/aws/en/assets/images/sql-alert-d1555143c7749b637280fe2f034a922e.png)

### Sample queries[​](#sample-queries "Direct link to Sample queries")

You can use the following sample queries to get information about MLflow activity in your account using [Databricks SQL](https://docs.databricks.com/aws/en/sql/). You can also leverage tools like Python notebooks with Spark.

#### Get run information from `runs_latest`[​](#get-run-information-from-runs_latest "Direct link to get-run-information-from-runs_latest")

SQL

    SELECT  run_name,  date(start_time) AS start_date,  status,  TIMESTAMPDIFF(MINUTE, start_time, end_time) AS run_length_minutesFROM system.mlflow.runs_latestWHERE  experiment_id = :experiment_id  AND run_id = :run_idLIMIT 1

This returns information about the given run:

![Query results run information](https://docs.databricks.com/aws/en/assets/images/query-run-info-8ad6fa32ec3357b0376ccad2779c9543.png)

#### Get experiment and run information from `experiments_latest` and `runs_latest`[​](#get-experiment-and-run-information-from-experiments_latest-and-runs_latest "Direct link to get-experiment-and-run-information-from-experiments_latest-and-runs_latest")

SQL

    SELECT  runs.run_name,  experiments.name,  date(runs.start_time) AS start_date,  runs.status,  TIMESTAMPDIFF(MINUTE, runs.start_time, runs.end_time) AS run_length_minutesFROM system.mlflow.runs_latest runs  JOIN system.mlflow.experiments_latest experiments ON runs.experiment_id = experiments.experiment_id  WHERE    runs.experiment_id = :experiment_id    AND runs.run_id = :run_idLIMIT 1

#### Get summary statistics for a given run from `run_metrics_history`[​](#get-summary-statistics-for-a-given-run-from-run_metrics_history "Direct link to get-summary-statistics-for-a-given-run-from-run_metrics_history")

SQL

    SELECT  metric_name,  count(metric_time) AS num_data_points,  ROUND(avg(metric_value), 1) AS avg,  ROUND(max(metric_value), 1) AS max,  ROUND(min(metric_value), 1) AS min,  ROUND(PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY metric_value), 1) AS pct_25,  ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY metric_value), 1) AS median,  ROUND(PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY metric_value), 1) AS pct_75FROM  system.mlflow.run_metrics_historyWHERE  run_id = :run_idGROUP BY  metric_name, run_idLIMIT 100

This returns a summary of the metrics for the given `run_id`:

![Query results run summary metrics](https://docs.databricks.com/aws/en/assets/images/query-run-metrics-309322bb2dab21b9b0fcd1fc3548a64e.png)

### Dashboards for experiments and runs[​](#dashboards-for-experiments-and-runs "Direct link to Dashboards for experiments and runs")

You can build [dashboards](https://docs.databricks.com/aws/en/dashboards/) on top of MLflow system tables data to analyze your MLflow experiments and runs from the entire workspace.

For more details, see [Build dashboards with MLflow metadata in system tables](https://docs.databricks.com/aws/en/mlflow/build-dashboards)
