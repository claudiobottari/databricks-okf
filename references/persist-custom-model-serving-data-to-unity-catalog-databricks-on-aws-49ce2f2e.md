---
title: Persist custom model serving data to Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/custom-model-serving-uc-logs
ingestedAt: "2026-06-18T08:11:52.091Z"
---

Beta

This feature is in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types). It is not automatically enabled for all customers and functionality is subject to change. To request access, contact your Databricks account team.

Learn how to configure endpoint telemetry to persist OpenTelemetry logs, traces, and metrics from your [custom model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/custom-models) to Unity Catalog tables. Use the persisted telemetry data to perform root cause analysis, monitor endpoint health, and meet compliance requirements with standard SQL queries.

## Requirements[​](#requirements "Direct link to Requirements")

*   Your workspace must be enabled for Unity Catalog. Default storage (Arclight) is not supported.
    
*   You must have `USE CATALOG`, `USE SCHEMA`, `CREATE TABLE`, and `MODIFY` permissions on the destination Unity Catalog catalog and schema where the logs are stored.
    
*   An existing [custom model serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/custom-models) or permissions to create one.
    
*   Your workspace must be in a supported region:
    
    *   `us-east-1`
    *   `us-east-2`
    *   `us-west-2`
    *   `eu-central-1`
    *   `ap-southeast-1`
    *   `ap-southeast-2`
    *   `ap-northeast-1`
    *   `ca-central-1`
    *   `eu-west-1`

## Step 1: Instrument your model code[​](#step-1-instrument-your-model-code "Direct link to Step 1: Instrument your model code")

Add instrumentation to your model code to capture telemetry.

1.  Add application logging to your model. Endpoint telemetry automatically captures standard Python `logging` output. No OpenTelemetry SDK instrumentation is required for basic logging.
    
    Python
    
        import loggingclass MyCustomModel(mlflow.pyfunc.PythonModel):    def predict(self, context, model_input):        # This log will be persisted to the <prefix>_otel_logs table        logging.warning("Received inference request")        try:            # Your model logic here            result = model_input * 2            return result        except Exception as e:            # Error logs are also captured with severity 'ERROR'            logging.error(f"Inference failed: {e}")            raise e
    
    The root logging level is set to `WARNING`. See [Troubleshooting](#troubleshooting) to change the logging level.
    
2.  (Optional) Instrument custom metrics and traces with OpenTelemetry. To capture custom metrics and traces beyond basic logging, add OpenTelemetry SDK instrumentation to your model. Expand the following section for a complete example that shows how to create counters, record spans, and attach custom attributes.
    
     ![Brackets square icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xIDEuNzVDMSAxLjMzNTc5IDEuMzM1NzkgMSAxLjc1IDFINVYyLjVIMi41VjEzLjVINVYxNUgxLjc1QzEuMzM1NzkgMTUgMSAxNC42NjQyIDEgMTQuMjVWMS43NVpNMTMuNSAyLjVIMTFWMUgxNC4yNUMxNC42NjQyIDEgMTUgMS4zMzU3OSAxNSAxLjc1VjE0LjI1QzE1IDE0LjY2NDIgMTQuNjY0MiAxNSAxNC4yNSAxNUgxMVYxMy41SDEzLjVWMi41WiIgZmlsbD0iIzZGNkY2RiIvPgo8L3N2Zz4K) **Example: Custom metrics, spans, and model logging with OpenTelemetry**
    
    note
    
    Due to limitations in model serialization, you must write your model to a separate file before logging to avoid errors, as shown below using `%%writefile return_input_model.py`.
    
    Python
    
        %%writefile return_input_model.pyimport osimport mlflowfrom opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporterfrom opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporterfrom opentelemetry.metrics import get_meter, set_meter_providerfrom opentelemetry.sdk.metrics import MeterProviderfrom opentelemetry.sdk.metrics.export import PeriodicExportingMetricReaderfrom opentelemetry.sdk.resources import Resourcefrom opentelemetry.sdk.trace import TracerProviderfrom opentelemetry.sdk.trace.export import BatchSpanProcessorfrom opentelemetry.trace import get_tracer, set_tracer_provider# ---- OTel initialization (per-worker) ----resource = Resource.create({    "worker.pid": str(os.getpid()),})otlp_trace_exporter = OTLPSpanExporter()tracer_provider = TracerProvider(resource=resource)tracer_provider.add_span_processor(BatchSpanProcessor(otlp_trace_exporter))set_tracer_provider(tracer_provider)otlp_metric_exporter = OTLPMetricExporter()metric_reader = PeriodicExportingMetricReader(otlp_metric_exporter)meter_provider = MeterProvider(metric_readers=[metric_reader], resource=resource)set_meter_provider(meter_provider)_tracer = get_tracer(__name__)_meter = get_meter(__name__)_prediction_counter = _meter.create_counter(    name="prediction_count",    description="Number of predictions made",    unit="1")class ReturnInputModel(mlflow.pyfunc.PythonModel):    def load_context(self, context):        self.tracer = _tracer        self.prediction_counter = _prediction_counter    def predict(self, context, model_input):        with self.tracer.start_as_current_span("ReturnInputModel.predict") as span:            span.set_attribute("input_shape", str(model_input.shape))            span.set_attribute("input_columns", str(list(model_input.columns)))            self.prediction_counter.add(1)            return model_inputmlflow.models.set_model(ReturnInputModel())
3.  Log and register the model.
    
    Python
    
        import pandas as pdimport mlflowfrom mlflow.models import infer_signature# Prepare tabular input/output for signature (pyfunc expects DataFrame)input_df = pd.DataFrame({"inputs": ["hello world"]})output_df = input_df.copy()  # model returns input unchanged# Log the model with OpenTelemetry dependencies (using code-based logging to avoid serialization issues)with mlflow.start_run():    signature = infer_signature(input_df, output_df)    model_info = mlflow.pyfunc.log_model(        name="model",        python_model="return_input_model.py",        signature=signature,        input_example=input_df,        pip_requirements=[            "mlflow==3.1",            "opentelemetry-sdk",            "opentelemetry-exporter-otlp-proto-http",        ],    )# Register with express deployment environment packing# Use Unity Catalog name: catalog.schema.model_nameregistered = mlflow.register_model(    model_info.model_uri,    MODEL_NAME,    env_pack="databricks_model_serving")
    

## Step 2: Prepare the Unity Catalog destination[​](#step-2-prepare-the-unity-catalog-destination "Direct link to step-2-prepare-the-unity-catalog-destination")

Before creating your endpoint, ensure you have a catalog and schema ready to receive the telemetry data. Databricks automatically creates the necessary tables in this schema if they do not already exist.

1.  In Catalog Explorer, navigate to the catalog and schema you want to use (for example, `my_catalog.observability`).

## Step 3: Enable endpoint telemetry[​](#step-3-enable-endpoint-telemetry "Direct link to Step 3: Enable endpoint telemetry")

You can enable telemetry when creating a new endpoint or add it to an existing one.

*   New endpoint
*   Existing endpoint

To enable telemetry in the UI:

1.  Navigate to **Serving** in the left sidebar.
2.  Click **Create serving endpoint**.
3.  In the **Endpoint telemetry** section (marked Preview), expand the configuration options.
4.  **Unity Catalog location**: Select the destination **Catalog** and **Schema** prepared in step 2.
5.  (Optional) **Table prefix**: Enter a prefix for the generated tables. If left blank, there is no prefix. The tables are named `<prefix>_otel_logs`, `<prefix>_otel_spans`, and `<prefix>_otel_metrics`.
6.  Complete the rest of the endpoint configuration (Model selection, Compute settings) and click **Create**.

To do this with the API:

 ![Brackets square icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xIDEuNzVDMSAxLjMzNTc5IDEuMzM1NzkgMSAxLjc1IDFINVYyLjVIMi41VjEzLjVINVYxNUgxLjc1QzEuMzM1NzkgMTUgMSAxNC42NjQyIDEgMTQuMjVWMS43NVpNMTMuNSAyLjVIMTFWMUgxNC4yNUMxNC42NjQyIDEgMTUgMS4zMzU3OSAxNSAxLjc1VjE0LjI1QzE1IDE0LjY2NDIgMTQuNjY0MiAxNSAxNC4yNSAxNUgxMVYxMy41SDEzLjVWMi41WiIgZmlsbD0iIzZGNkY2RiIvPgo8L3N2Zz4K) **Enable telemetry using the API**

Bash

    curl -X POST -H "Authorization: Bearer <your-token>" \https://<workspace-url>/api/2.0/serving-endpoints \-d '{  "name": "my-custom-logging-endpoint",  "config": {    "served_entities": [      {        "name": "my-model",        "entity_name": "my-model",        "entity_version": "1",        "workload_size": "Small",        "scale_to_zero_enabled": true      }    ]  },  "telemetry_config": {    "table_names": {      "logs_table": "my_catalog.observability.custom_endpoint_logs",      "metrics_table": "my_catalog.observability.custom_endpoint_metrics",      "traces_table": "my_catalog.observability.custom_endpoint_spans"    }  }}'

## Step 4: Verify and query telemetry data[​](#step-4-verify-and-query-telemetry-data "Direct link to Step 4: Verify and query telemetry data")

After the endpoint receives traffic, telemetry data streams to the configured Unity Catalog tables.

1.  Go to **Catalog Explorer** or the **SQL Editor**.
    
2.  Locate the table named `<prefix>_otel_logs` in your configured schema.
    
3.  Run a query to verify data is flowing:
    
    SQL
    
        SELECT * FROM <catalog>.<schema>.<prefix>_otel_logsLIMIT 10;
    

### Query telemetry data[​](#query-telemetry-data "Direct link to Query telemetry data")

The following examples show common queries.

To view the full schema of any telemetry table, run:

SQL

    DESCRIBE TABLE <catalog>.<schema>.<prefix>_otel_logs;

Use these columns to filter and correlate telemetry data:

*   `timestamp`
*   `severity_text`
*   `body`
*   `trace_id`
*   `span_id`
*   `attributes` — a map that contains event-specific metadata.

### Check for errors in the last hour[​](#check-for-errors-in-the-last-hour "Direct link to Check for errors in the last hour")

SQL

    SELECT  timestamp,  severity_text,  body,  attributesFROM <catalog>.<schema>.<prefix>_otel_logsWHERE  severity_text = 'ERROR'  AND timestamp > current_timestamp() - INTERVAL 1 HOURORDER BY timestamp DESC;

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

**Logs not appearing in table**: The root logging level defaults to `WARNING` to reduce overhead. To capture lower-severity logs, change the level in your model code:

Python

    class MyModel(mlflow.pyfunc.PythonModel):    def load_context(self, context):        root = logging.getLogger()        root.setLevel(logging.DEBUG)        for handler in root.handlers:            handler.setLevel(logging.DEBUG)

## Limitations[​](#limitations "Direct link to Limitations")

The following limits apply to endpoint telemetry:

*   Schema evolution on the target table is not supported.
    
*   Only managed Delta tables are supported. External storage and Arclight default storage are not supported.
    
*   The table location must be in the same region as your workspace.
    
*   Only table names with ASCII letters, digits, and underscores are supported.
    
*   Recreating a target table is not supported.
    
*   Only single availability zone (single-az) durability is supported.
    
*   Delivery is at-least-once. An acknowledgement from the server means the record is durable and in the Delta table.
    
*   Records must be less than 10 MB each.
    
*   Requests must be less than 30 MB each.
    
*   Log lines must be less than 1 MB each.
    
*   Telemetry latency degrades beyond 2500 QPS.
    
*   Logs appear in the Unity Catalog table a few seconds after they are emitted.
