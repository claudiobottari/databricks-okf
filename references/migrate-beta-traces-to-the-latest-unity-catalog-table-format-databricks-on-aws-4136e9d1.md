---
title: Migrate Beta traces to the latest Unity Catalog table format | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/migrate-uc-trace-table-prefix
ingestedAt: "2026-06-18T08:17:47.936Z"
---

If you [configured an MLflow experiment to store traces in Unity Catalog](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/trace-unity-catalog) during the Beta release using the schema-linked format (`catalog.schema`), you can migrate those traces to the table-prefix format (`catalog.schema.table_prefix`) introduced with the Public Preview release.

Databricks recommends the table-prefix format for all new and existing UC trace workloads. It provides faster time-range queries, richer attribute types, a dedicated annotations table, and support for multiple trace destinations per schema.

The migration copies spans and annotations (tags, assessments, metadata) using Spark SQL.

## Identify experiments that use the older format[​](#identify-experiments-that-use-the-older-format "Direct link to Identify experiments that use the older format")

Experiments that store traces in Unity Catalog use one of two formats:

*   **Schema-linked** (used during the Beta release): The experiment's trace destination is a two-part path (`catalog.schema`). Trace data is stored in fixed-name tables like `mlflow_experiment_trace_otel_spans` and `mlflow_experiment_trace_otel_logs`. Tags, assessments, and metadata are stored as log events in the logs table.
*   **Table-prefix** (used during the Public Preview release and later): The experiment's trace destination is a three-part path (`catalog.schema.table_prefix`). Trace data is stored in prefix-namespaced tables like `<table_prefix>_otel_spans`, and annotations have a dedicated table.

If your Unity Catalog schema contains tables named `mlflow_experiment_trace_otel_spans` and `mlflow_experiment_trace_otel_logs`, your experiment uses the older schema-linked format and is eligible for migration.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

*   A Unity Catalog\-enabled workspace.
    
*   A Databricks cluster running Databricks Runtime 15.3 or above.
    
*   The `databricks-agents` Python package:
    
    Bash
    
        pip install "databricks-agents>=1.10.0"
    
*   The following permissions:
    
    *   `USE_CATALOG` and `USE_SCHEMA` on the **source** catalog and schema.
    *   `USE_CATALOG`, `USE_SCHEMA`, and `MODIFY` on the **destination** catalog and schema.

## Step 1: Create a destination experiment[​](#step-1-create-a-destination-experiment "Direct link to Step 1: Create a destination experiment")

Create an experiment linked to a Unity Catalog table-prefix location. The migrated traces are stored here. For full setup details, see [Setup: Create an experiment with a Unity Catalog trace location](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/trace-unity-catalog#setup).

Python

    import mlflowfrom mlflow.entities.trace_location import UnityCatalogexperiment = mlflow.set_experiment(    experiment_name="/Workspace/Users/<user>/<experiment_name>",    trace_location=UnityCatalog(        catalog_name="<destination_catalog>",        schema_name="<destination_schema>",        table_prefix="<table_prefix>",    ),)print(f"Experiment ID: {experiment.experiment_id}")

Save the experiment ID. Use it to configure your notebooks, jobs, or deployed models to log traces to the new destination.

## Step 2: Switch trace logging and stop writes to the source experiment[​](#step-2-switch-trace-logging-and-stop-writes-to-the-source-experiment "Direct link to Step 2: Switch trace logging and stop writes to the source experiment")

Update your notebooks, jobs, or deployed models to log traces to the new experiment created in Step 1. This ensures new traces go directly to the destination tables.

important

Stop all writes to the source experiment before running the migration. Any traces written to the source tables during migration might not be copied. Verify that no notebooks, jobs, or deployed models are actively logging traces to the source experiment.

If you want to do a dry run first, you can skip this step and run the migration without switching your production workloads.

## Step 3: Run the migration[​](#step-3-run-the-migration "Direct link to Step 3: Run the migration")

In a Databricks notebook on the cluster, run the following:

Python

    from databricks.migrations.v1_to_v2 import V1ToV2SqlMigrationmigration = V1ToV2SqlMigration(    v1_source_schema="<source_catalog>.<source_schema>",    v2_destination_prefix="<destination_catalog>.<destination_schema>.<table_prefix>",)migration.run()

Replace the placeholders:

*   `<source_catalog>.<source_schema>`: The Unity Catalog catalog and schema where your source trace tables are stored.
*   `<destination_catalog>.<destination_schema>.<table_prefix>`: The Unity Catalog catalog, schema, and table prefix for the destination. This must match the location configured in Step 1.

The migration is idempotent. If it fails partway through (for example, due to a cluster timeout), you can safely rerun it. Already-migrated rows are skipped automatically.

Once the migration completes, your traces are available in the new destination experiment. The source tables are not modified by the migration and can be retained as a backup.
