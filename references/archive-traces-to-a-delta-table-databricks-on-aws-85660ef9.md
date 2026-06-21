---
title: Archive traces to a Delta table | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/archive-traces
ingestedAt: "2026-06-18T08:14:38.069Z"
---

*   [](https://docs.databricks.com/aws/en/)
*   [Agents](https://docs.databricks.com/aws/en/agents/)
*   [Evaluate and monitor agents](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/)
*   [Production monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring)
*   Archive traces

Last updated on **Apr 16, 2026**

You can save traces and their associated assessments to a Unity Catalog Delta table for long-term storage and advanced analysis. This is useful for building custom dashboards, performing in-depth analytics on trace data, and maintaining a durable record of your application's behavior.

note

You must have the necessary permissions to write to the specified Unity Catalog Delta table. The target table will be created if it does not already exist.

If the table already exists, traces are appended to it.

## Enable trace archiving[​](#enable-trace-archiving "Direct link to Enable trace archiving")

*   MLflow API
*   Databricks UI

To begin archiving traces for an experiment, use the `enable_databricks_trace_archival` function. You must specify the full name of the target Delta table, including catalog and schema. If you don't provide an `experiment_id`, archiving traces is enabled for the currently active experiment.

Python

    from mlflow.tracing.archival import enable_databricks_trace_archival# Archive traces from a specific experiment to a Unity Catalog Delta tableenable_databricks_trace_archival(    delta_table_fullname="my_catalog.my_schema.archived_traces",    experiment_id="YOUR_EXPERIMENT_ID",)

## Disable trace archiving[​](#disable-trace-archiving "Direct link to Disable trace archiving")

*   MLflow API
*   Databricks UI

Stop archiving traces for an experiment at any time by using the `disable_databricks_trace_archival` function.

Python

    from mlflow.tracing.archival import disable_databricks_trace_archival# Stop archiving traces for the specified experimentdisable_databricks_trace_archival(experiment_id="YOUR_EXPERIMENT_ID")

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Monitor GenAI apps in production](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) - Set up production monitoring.
*   [Building MLflow evaluation datasets](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/build-eval-dataset) - Use archived traces to build evaluation datasets.
