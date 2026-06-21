---
title: Export Langfuse traces to Databricks MLflow | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/third-party/langfuse
ingestedAt: "2026-06-18T08:18:15.535Z"
---

Configure [Langfuse](https://langfuse.com/) to send OpenTelemetry-based trace spans to the Databricks MLflow OTLP endpoint, so that traces are stored in Unity Catalog tables alongside your other MLflow traces.

Consolidating traces on Databricks provides the following benefits:

*   Query and compare Langfuse-instrumented calls together with traces from other frameworks in a single place.
*   Use Databricks SQL to analyze trace data at scale.
*   Apply Unity Catalog governance such as access controls and lineage to all your traces.

## Requirements[​](#requirements "Direct link to Requirements")

*   A Databricks workspace with the "OpenTelemetry on Databricks" preview enabled. See [Manage Databricks previews](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews).
*   A new MLflow experiment.

## Step 1: Install packages[​](#step-1-install-packages "Direct link to Step 1: Install packages")

Install the required packages in your Databricks notebook:

Python

    %pip install "langfuse>=3.14.5" "mlflow[databricks]>=3.10.0" opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp-proto-http%restart_python

## Step 2: Disable Langfuse trace collection[​](#step-2-disable-langfuse-trace-collection "Direct link to Step 2: Disable Langfuse trace collection")

Langfuse requires the `LANGFUSE_HOST`, `LANGFUSE_PUBLIC_KEY`, and `LANGFUSE_SECRET_KEY` environment variables to initialize its SDK. Set these variables to dummy values to prevent traces from being sent to a Langfuse server. Only the OTEL exporter, configured in [Add the OTLP exporter](#otlp-exporter), will receive the spans.

Python

    import osos.environ["LANGFUSE_HOST"] = "localhost"os.environ["LANGFUSE_PUBLIC_KEY"] = ""os.environ["LANGFUSE_SECRET_KEY"] = ""

note

This is the simplest approach to prevent Langfuse from collecting traces on its own servers. Alternatively, you can set `LANGFUSE_TRACING_ENABLED=False` to disable Langfuse's built-in trace collection.

## Step 3: Configure Databricks connection[​](#step-3-configure-databricks-connection "Direct link to step-3-configure-databricks-connection")

Retrieve the workspace host URL and an API token. In a Databricks notebook, you can get these from the notebook context:

Python

    # If running outside a Databricks notebook, set DATABRICKS_HOST and DATABRICKS_TOKEN environment variables manually.context = dbutils.notebook.entry_point.getDbutils().notebook().getContext()DATABRICKS_HOST = context.apiUrl().get().rstrip("/")DATABRICKS_TOKEN = context.apiToken().get()

## Step 4: Link an experiment to Unity Catalog[​](#step-4-link-an-experiment-to-unity-catalog "Direct link to step-4-link-an-experiment-to-unity-catalog")

Define your Unity Catalog catalog and schema, then link them to an MLflow experiment using `set_experiment_trace_location`. This tells Databricks where to store the incoming traces.

Python

    import mlflowfrom mlflow.entities import UCSchemaLocationfrom mlflow.tracing.enablement import set_experiment_trace_locationCATALOG_NAME = "<UC_CATALOG_NAME>"SCHEMA_NAME = "<UC_SCHEMA_NAME>"EXPERIMENT_ID = "<EXPERIMENT_ID>"trace_location = set_experiment_trace_location(    location=UCSchemaLocation(catalog_name=CATALOG_NAME, schema_name=SCHEMA_NAME),    experiment_id=EXPERIMENT_ID,)

## Step 5: Add the Databricks OTLP exporter[​](#step-5-add-the-databricks-otlp-exporter "Direct link to step-5-add-the-databricks-otlp-exporter")

Get the `TracerProvider` that Langfuse uses, then attach a `BatchSpanProcessor` with an `OTLPSpanExporter` that points to the Databricks OTLP endpoint.

Python

    from langfuse import get_clientfrom opentelemetry import trace as otel_tracefrom opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporterfrom opentelemetry.sdk.trace.export import BatchSpanProcessor# Initialize the Langfuse client. Langfuse registers its own TracerProvider as the global OpenTelemetry TracerProvider.langfuse = get_client()# Retrieve the global TracerProvider.# Use this to attach an additional span processor that forwards Langfuse spans to Databricks.provider = otel_trace.get_tracer_provider()# Configure the OTLP exporter to send spans to the Databricks MLflow endpoint.# The X-Databricks-UC-Table-Name header routes incoming spans to the Unity Catalog table defined by the trace location.databricks_exporter = OTLPSpanExporter(    endpoint=f"{DATABRICKS_HOST}/api/2.0/otel/v1/traces",    headers={        "content-type": "application/x-protobuf",        "Authorization": f"Bearer {DATABRICKS_TOKEN}",        "X-Databricks-UC-Table-Name": trace_location.full_otel_spans_table_name,    },)# Attach the Databricks exporter to Langfuse's provider. Because the Langfuse# env vars are set to dummy values, this processor is the only active exporter,# so all spans are sent exclusively to Databricks.provider.add_span_processor(BatchSpanProcessor(databricks_exporter))

## Step 6: Run a traced function[​](#step-6-run-a-traced-function "Direct link to Step 6: Run a traced function")

Use Langfuse's `@observe()` decorator to instrument your functions. The decorator creates OTEL spans that the exporter sends to Databricks.

Python

    from langfuse import observe@observe()def my_llm_call(prompt: str) -> str:    # Replace with your LLM logic (OpenAI, Anthropic, etc.)    return f"Response to: {prompt}"@observe()def my_pipeline(user_input: str) -> str:    result = my_llm_call(user_input)    return resultmy_pipeline("Hello, world!")

## Step 7: View traces[​](#step-7-view-traces "Direct link to Step 7: View traces")

Open the MLflow experiment in your Databricks workspace and click the **Traces** tab. The trace from the `my_pipeline` call should appear.

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Store OpenTelemetry traces in Unity Catalog](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/trace-unity-catalog): Learn more about storing and managing traces in Unity Catalog tables.
*   [View traces in the Databricks MLflow UI](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/ui-traces): Search and filter traces in the MLflow UI.
*   [Query OpenTelemetry traces stored in Unity Catalog](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/query-dbsql): Query trace data directly using SQL through a Databricks SQL warehouse.
*   [Search for traces by OTel span attributes](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/third-party/otel-span-attributes#search-for-traces-by-otel-span-attributes): Search for ingested Langfuse traces by OpenTelemetry span attributes.
