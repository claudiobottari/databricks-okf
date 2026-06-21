---
title: Build dashboards with MLflow metadata in system tables | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow/build-dashboards
ingestedAt: "2026-06-18T08:13:54.154Z"
---

Using MLflow metadata in [system tables](https://docs.databricks.com/aws/en/admin/system-tables/mlflow), you can build [dashboards](https://docs.databricks.com/aws/en/dashboards/) to analyze your MLflow experiments and runs from the entire workspace. Using the existing MLflow UI and REST APIs for these tasks would require extensive, time-consuming iteration.

## Dashboard for single run details[​](#dashboard-for-single-run-details "Direct link to Dashboard for single run details")

To start visualizing your MLflow data, download [this example dashboard](https://docs.databricks.com/aws/en/assets/files/mlflow_system_tables_dashboard.lvdash-c47a9bd31724e4ee62a78acffc600d0b.json) as a JSON file and [import it into your workspace](https://docs.databricks.com/aws/en/dashboards/automate/import-export#import). This dashboard contains a skeleton of data to replicate what is shown on the run details page in the MLflow UI.

For a given experiment ID, run ID, and metric name, it displays run details along with tags, parameters, and a metric graph. You can obtain the experiment ID and run ID from the run details page, both from the UI and in the URL itself: `https://<workspace>.databricks.com/ml/experiments/<experiment_id>/runs/<run_id>`.

![run experiment ids](https://docs.databricks.com/aws/en/assets/images/run-experiment-ids-a370fb107de18540b3be8505e7dec9c5.png)

If you navigate to the dashboard panel from the left navigation menu, you can import the dashboard from a JSON file definition [here](https://gist.github.com/ian-ack-db/684a83040a557f92f1668449c0df75df). From there, you can use the input boxes on the top to filter for the relevant run and experiment within your workspace to plot. Feel free to explore the queries and change the plots to meet your needs.

![run details dashboard](https://docs.databricks.com/aws/en/assets/images/dashboard-run-details-7e80c6353e0efb82d838f0cf2ddbc1ad.png)

![dashboard queries](https://docs.databricks.com/aws/en/assets/images/dashboard-queries-8eb79b19670c742dd9ec0fbe02f7295c.png)

## Dashboard to monitor average GPU utilization across experiments[​](#dashboard-to-monitor-average-gpu-utilization-across-experiments "Direct link to Dashboard to monitor average GPU utilization across experiments")

On the fourth tab from the above dashboard, you can input a metric name to get summary statistics across all experiments with that metric within a given time window. This information can be useful for monitoring [system metrics](https://mlflow.org/docs/latest/ml/tracking/system-metrics/) recorded by MLflow across your workspace to monitor for inefficient CPU, memory, or GPU utilization.

![average GPU utilization dashboard](https://docs.databricks.com/aws/en/assets/images/dashboard-gpu-utilization-6d32069b826aad9ed769ef394b34dd76.png)

In the example, we can see several experiments with an average GPU utilization of less than 10% which we may want to investigate.
