---
title: Store OpenTelemetry traces in Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/trace-unity-catalog
ingestedAt: "2026-06-18T08:18:19.257Z"
---

Databricks supports storing OpenTelemetry (OTel) traces in Unity Catalog tables. By default, MLflow stores traces organized by experiments in the MLflow control plane service. However, storing traces in Unity Catalog using OTel format provides the following benefits:

*   Access control is managed through Unity Catalog schema and table permissions rather than experiment-level ACLs. Users with access to the Unity Catalog tables can view all traces stored in those tables, regardless of which experiment the traces belong to.
*   Trace IDs use URI format instead of the `tr-<UUID>` format, improving compatibility with external systems.
*   Store large volumes of traces in Delta tables for long-term retention and analysis.
*   Query trace data directly using SQL through a Databricks SQL warehouse, enabling advanced analytics and custom reporting.
*   OTel format ensures compatibility with other OpenTelemetry clients and tools.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

*   A Unity Catalog\-enabled workspace.
    
*   Ensure the "OpenTelemetry on Databricks" preview is enabled, along with "Variant Shredding for Optimized Read Performance on Semi-Structured Data." See [Manage Databricks previews](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews).
    
*   Permissions to create catalogs and schemas in Unity Catalog.
    
*   A [Databricks SQL warehouse](https://docs.databricks.com/aws/en/compute/sql-warehouse/) with `CAN USE` permissions. Save the warehouse ID for later reference.
    
*   A workspace in a supported region. See [Features with limited regional availability](https://docs.databricks.com/aws/en/resources/feature-region-support).
    
*   MLflow Python library version 3.11 or later installed in your environment:
    
    Bash
    
        pip install mlflow[databricks]>=3.11.0 --upgrade --force-reinstall
    

## Setup: Create an experiment with a Unity Catalog trace location[​](#-setup-create-an-experiment-with-a-unity-catalog-trace-location "Direct link to -setup-create-an-experiment-with-a-unity-catalog-trace-location")

Run the following code to create and bind an experiment to a Unity Catalog trace location:

Python

    # Example values for the placeholders below:# MLFLOW_TRACING_SQL_WAREHOUSE_ID: "abc123def456" (found in SQL warehouse URL)# experiment_name: "/Users/user@company.com/traces"# catalog_name: "main" or "my_catalog"# schema_name: "mlflow_traces" or "production_traces"# table_prefix: "my_otel"import osimport mlflowfrom mlflow.entities.trace_location import UnityCatalogmlflow.set_tracking_uri("databricks")# Specify the ID of a SQL warehouse you have access to.os.environ["MLFLOW_TRACING_SQL_WAREHOUSE_ID"] = "<SQL_WAREHOUSE_ID>"# Specify the name of the MLflow Experiment to use for viewing traces in the UI.experiment_name = "<MLFLOW_EXPERIMENT_NAME>"# Specify the name of the Catalog to use for storing traces.catalog_name = "<UC_CATALOG_NAME>"# Specify the name of the Schema to use for storing traces.schema_name = "<UC_SCHEMA_NAME>"# Specify the name of the prefix appended to every table storing trace data.table_prefix = "<UC_TABLE_PREFIX>"# mlflow.set_experiment is an upsert operationexperiment = mlflow.set_experiment(    experiment_name=experiment_name,    trace_location=UnityCatalog(        catalog_name=catalog_name,        schema_name=schema_name,        table_prefix=table_prefix,  # defaults to experiment id if not provided    ),)print(f"Experiment ID: {experiment.experiment_id}")print(experiment.trace_location.full_otel_spans_table_name)

You can also use [`mlflow.create_experiment`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.create_experiment) with the same `trace_location` parameter. Unlike `set_experiment`, `create_experiment` does not set the active experiment, so you must call `set_experiment` afterward in order to ensure that traces are routed to the correct location:

Python

    experiment_id = mlflow.create_experiment(    name=experiment_name,    trace_location=UnityCatalog(        catalog_name=catalog_name,        schema_name=schema_name,        table_prefix=table_prefix,    ),)# trace_location is optional here since# the experiment is already bound to the UC trace location above.mlflow.set_experiment(experiment_id=experiment_id)

Once you bind an experiment to a UC trace location, you cannot reassign the experiment to a different UC trace location. However, multiple experiments can share the same UC trace location.

### Verify tables[​](#verify-tables "Direct link to Verify tables")

After running the setup code, four new Unity Catalog tables appear in the schema in the Catalog Explorer UI:

*   `<table_prefix>_otel_annotations`
*   `<table_prefix>_otel_logs`
*   `<table_prefix>_otel_metrics`
*   `<table_prefix>_otel_spans`

## Grant permissions[​](#grant-permissions "Direct link to Grant permissions")

A Databricks user or service principal needs the following [Unity Catalog privileges](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/) to write or read MLflow traces from the Unity Catalog tables:

1.  **USE\_CATALOG** on the catalog.
2.  **USE\_SCHEMA** on the schema.
3.  **MODIFY** and **SELECT** on each of the `<table_prefix>_<type>` tables.

note

`ALL_PRIVILEGES` is not sufficient for accessing Unity Catalog trace tables. You must explicitly grant **MODIFY** and **SELECT**.

## Log traces to the Unity Catalog tables[​](#log-traces-to-the-unity-catalog-tables "Direct link to log-traces-to-the-unity-catalog-tables")

After creating the tables, you can write traces to them from various sources by specifying the trace location. How you do this depends on the source of the traces.

*   MLflow SDK
*   Model Serving endpoint
*   Third-party OTel client

The Unity Catalog trace location can be specified using the [`mlflow.set_experiment`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.set_experiment) Python API.

Python

    import mlflowfrom mlflow.entities.trace_location import UnityCatalogmlflow.set_tracking_uri("databricks")# Specify the catalog, schema, and table prefix to use for storing Tracescatalog_name = "<UC_CATALOG_NAME>"schema_name = "<UC_SCHEMA_NAME>"table_prefix = "<UC_TABLE_PREFIX>"# For existing experiments, it is not necessary to specify `trace_location`. MLflow# retrieves the UC trace location bound to the experiment and routes traces to# that location.mlflow.set_experiment(    experiment_name="...",    trace_location=UnityCatalog(        catalog_name=catalog_name,        schema_name=schema_name,        table_prefix=table_prefix,    ),  # optional for existing experiments)# Create and ingest an example trace using the `@mlflow.trace` decorator@mlflow.tracedef test(x):    return x + 1test(100)

## View traces in the UI[​](#view-traces-in-the-ui "Direct link to View traces in the UI")

View traces stored in OTel format the same way you view other traces:

1.  In your Workspace, go to **Experiments**.
    
2.  Find the experiment where your traces are logged. For example, the experiment set by `mlflow.set_experiment("/Shared/my-genai-app-traces")`.
    
3.  Click the **Traces** tab to see a list of all traces logged to that experiment.
    
    ![Trace List View](https://docs.databricks.com/aws/en/assets/images/trace-list-view-new-40f393cafd6308da13584c7f78049f9c.png)
    
4.  If you [stored your traces in a Unity Catalog table](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/trace-unity-catalog), Databricks retrieves traces using an [SQL warehouse](https://docs.databricks.com/aws/en/compute/sql-warehouse/). Select a SQL warehouse from the drop-down menu.
    

For more information on using the UI to search for traces, see [View traces in the Databricks MLflow UI](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/ui-traces).

## Enable production monitoring[​](#enable-production-monitoring "Direct link to enable-production-monitoring")

[Production monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) is a complementary scoring layer that runs scorers against your traces. It works on traces regardless of where they are stored, so you can use it alongside Unity Catalog trace storage.

To use production monitoring with traces stored in Unity Catalog, you must configure a SQL warehouse ID for the experiment. The monitoring job requires this configuration to run scorer queries against Unity Catalog tables.

Set the SQL warehouse ID using [`set_databricks_monitoring_sql_warehouse_id()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.tracing.html#mlflow.tracing.set_databricks_monitoring_sql_warehouse_id):

Python

    from mlflow.tracing import set_databricks_monitoring_sql_warehouse_id# Set the SQL warehouse ID for monitoringset_databricks_monitoring_sql_warehouse_id(    sql_warehouse_id="<SQL_WAREHOUSE_ID>",    experiment_id="<EXPERIMENT_ID>"  # Optional, uses active experiment if not specified)

Alternatively, you can set the `MLFLOW_TRACING_SQL_WAREHOUSE_ID` environment variable before starting monitoring.

If you skip this step, monitoring jobs fail with an error indicating that the `mlflow.monitoring.sqlWarehouseId` experiment tag is missing.

To configure monitoring for Unity Catalog traces, you need the following workspace-level permissions:

*   `CAN USE` permission on the SQL warehouse
*   `CAN EDIT` permission on the MLflow experiment
*   Permission on the monitoring job (automatically granted when you register the first scorer)

The monitoring job runs under the identity of the user who first registered a scorer on the experiment. This user's permissions determine what the monitoring job can access.

## Limitations[​](#-limitations "Direct link to -limitations")

*   Trace ingestion is initially limited to 200 traces per second per workspace and 100 MB per second per table. Contact your Databricks account team if you need higher limits.
    
*   An experiment can only be bound to a Unity Catalog trace location at experiment creation time.
    
*   Traces stored in Unity Catalog are not supported with [Knowledge Assistant](https://docs.databricks.com/aws/en/generative-ai/agent-bricks/knowledge-assistant) or [Supervisor Agent](https://docs.databricks.com/aws/en/generative-ai/agent-bricks/multi-agent-supervisor).
    
*   Deleting individual traces is not supported for traces stored in Unity Catalog. To remove traces, you must delete rows directly from the underlying Unity Catalog tables using SQL. This differs from experiment traces, which can be deleted using the MLflow UI or API.
    
*   [MLflow MCP server](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/mlflow-mcp) does not support interacting with traces stored in Unity Catalog.
    
*   Traces cannot yet be written to a [default storage](https://docs.databricks.com/aws/en/storage/default-storage) catalog.
    
*   Traces cannot yet be written to storage protected by Private Link.
    
*   Enabling tracing on a serving endpoint may reduce serving throughput.
    

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Query OpenTelemetry traces stored in Unity Catalog](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/query-dbsql)
*   [Search for traces by OTel span attributes](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/third-party/otel-span-attributes#search-for-traces-by-otel-span-attributes): Search for third-party OTel traces stored in Unity Catalog by span attributes.
*   [Migrate Beta traces to the latest Unity Catalog table format](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/migrate-uc-trace-table-prefix): Migrate traces from the older schema-linked format to the table-prefix format.
*   [Migrate experiment traces to Unity Catalog](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/migrate-traces-to-uc): Migrate existing traces to Unity Catalog from experiments that do not use Unity Catalog storage.
