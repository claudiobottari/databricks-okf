---
title: Migrate experiment traces to Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/migrate-traces-to-uc
ingestedAt: "2026-06-18T08:17:45.990Z"
---

If you have traces stored in an MLflow experiment, you can migrate them to Unity Catalog Delta tables. Storing traces in Unity Catalog removes trace storage limits, provides fine-grained access controls through Unity Catalog governance, and makes traces queryable from notebooks, SQL, Genie, AI/BI dashboards, and any Spark-based tool.

The migration copies traces, spans, assessments, tags, and metadata from the source experiment to Unity Catalog tables. The source experiment is not modified.

If you are starting from scratch and don't have existing traces to migrate, see [Store traces in Unity Catalog](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/trace-unity-catalog) to configure a new experiment to write traces directly to Unity Catalog.

note

The migration does not copy archived or deleted traces, dataset records, labeling sessions, runs, or non-trace entities.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

*   A Unity Catalog\-enabled workspace.
    
*   A Databricks cluster running Databricks Runtime 15.3 or above.
    
*   The `databricks-agents` Python package:
    
    Bash
    
        pip install "databricks-agents>=1.10.1"
    
*   The following permissions:
    
    *   Read access to the source experiment.
    *   `USE_CATALOG`, `USE_SCHEMA`, and `MODIFY` on the destination catalog and schema.

## Step 1: Create a destination experiment[​](#step-1-create-a-destination-experiment "Direct link to Step 1: Create a destination experiment")

The destination is a new MLflow experiment bound to a Unity Catalog trace location.

The trace location is a three-part path (`catalog.schema.table_prefix`). The table prefix is applied to the four Delta tables that back the experiment:

*   `<prefix>_otel_spans`
*   `<prefix>_otel_annotations`
*   `<prefix>_otel_logs`
*   `<prefix>_otel_metrics`

Run the following to create the destination experiment. For full setup details, see [Setup: Create an experiment with a Unity Catalog trace location](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/trace-unity-catalog#setup).

Python

    import mlflowfrom mlflow.entities.trace_location import UnityCatalogexperiment = mlflow.set_experiment(    experiment_name="/Workspace/Users/<user>/<experiment_name>",    trace_location=UnityCatalog(        catalog_name="<destination_catalog>",        schema_name="<destination_schema>",        table_prefix="<table_prefix>",    ),)print(f"Destination experiment ID: {experiment.experiment_id}")

Save the experiment ID printed by the code above. You use it in the next two steps: in [Step 2](#step-2-switch-trace-logging-and-stop-writes-to-the-source-experiment) to point your notebooks, jobs, and deployed models at the new Unity Catalog\-backed experiment, and in [Step 3](#step-3-run-the-migration) as the destination experiment ID for the migration command.

You can ingest a few test traces into the new experiment to verify that Unity Catalog tracing works for your workflow before proceeding. See [Log traces to the Unity Catalog tables](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/trace-unity-catalog#log-traces-to-the-unity-catalog-tables) for examples.

## Step 2: Switch trace logging and stop writes to the source experiment[​](#step-2-switch-trace-logging-and-stop-writes-to-the-source-experiment "Direct link to Step 2: Switch trace logging and stop writes to the source experiment")

Before running the migration, redirect trace logging to the destination experiment created in Step 1 and stop writes to the source experiment. This ensures new traces are written to the destination tables and that no traces are lost while the migration runs.

1.  Stop all writes to the source experiment. Any traces written to the source experiment during migration might not be copied. Verify that no notebooks, jobs, or deployed models are actively logging to the source experiment.
    
2.  Replace any existing `set_experiment` call that points to the source experiment with one that points to the destination experiment, either by name or by ID:
    
    Python
    
        import mlflow# By experiment namemlflow.set_experiment(    experiment_name="/Workspace/Users/<user>/<destination_experiment_name>",)# Or by experiment IDmlflow.set_experiment(experiment_id="<destination_experiment_id>")
    

note

Trace location can also be configured through other mechanisms, such as the `MLFLOW_EXPERIMENT_NAME` and `MLFLOW_EXPERIMENT_ID` environment variables, which are used by deployed applications, containerized services, model serving endpoint configurations, and IDE or local development setups. For details on configuring trace destinations in production, see [Trace agents deployed on Databricks](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/prod-tracing) and [Trace agents deployed outside of Databricks](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/prod-tracing-external).

## Step 3: Run the migration[​](#step-3-run-the-migration "Direct link to Step 3: Run the migration")

In a Databricks notebook on the cluster, run the following:

Python

    from databricks.migrations.migrate_traces_to_uc import runrun(    source_experiment_id="<source_experiment_id>",    target_experiment_id="<destination_experiment_id>",)

Replace the placeholders:

*   `<source_experiment_id>`: The experiment ID of your existing experiment that contains the traces you want to migrate.
*   `<destination_experiment_id>`: The experiment ID of the Unity Catalog\-backed experiment created in Step 1.

The migration is idempotent. If it is interrupted (for example, due to a cluster timeout), you can safely rerun the same command. The migration automatically resumes from where it left off. Already-migrated rows are skipped.

To migrate only traces created after a specific time, pass the `start_time_ms` parameter (epoch milliseconds). The migration will ingest all traces with a request time at or after the specified timestamp, skipping any that have already been migrated.

Python

    import timefrom databricks.migrations.migrate_traces_to_uc import runone_week_ago_ms = int((time.time() - 7 * 24 * 60 * 60) * 1000)run(    source_experiment_id="<source_experiment_id>",    target_experiment_id="<destination_experiment_id>",    start_time_ms=one_week_ago_ms,  # Only migrate traces from the last 7 days)

Once the migration completes, your traces are available in the new destination experiment. The source experiment is not modified by the migration and can be retained as a backup.
