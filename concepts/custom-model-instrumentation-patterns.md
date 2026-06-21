---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f865362aab15ec9b63f240d250344fe0db9b7aeb65c4641062aceb19c081b441
  pageDirectory: concepts
  sources:
    - persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - custom-model-instrumentation-patterns
    - CMIP
  citations:
    - file: persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md
title: Custom Model Instrumentation Patterns
description: Best practices for adding logging and OpenTelemetry instrumentation to MLflow pyfunc models, including Python logging capture, logging level configuration, and model code organization.
tags:
  - mlflow
  - python
  - model-development
  - best-practices
timestamp: "2026-06-19T19:56:20.975Z"
---

# Custom Model Instrumentation Patterns

**Custom Model Instrumentation Patterns** refer to the techniques and configurations used to add telemetry capture — including logs, traces, and metrics — to custom model serving endpoints on Databricks. These patterns enable root cause analysis, endpoint health monitoring, and compliance auditing by persisting OpenTelemetry data to [Unity Catalog](/concepts/unity-catalog.md) tables. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Overview

When serving custom models via [Model Serving](/concepts/model-serving.md), you can configure endpoint telemetry to automatically capture and persist observability data. The telemetry data is stored in three Unity Catalog tables: one for logs (`_otel_logs`), one for spans/traces (`_otel_spans`), and one for metrics (`_otel_metrics`). This data can be queried using standard SQL. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Pattern 1: Basic Application Logging

The simplest instrumentation pattern is to use standard Python logging in your model code. The endpoint telemetry system automatically captures any output from Python's `logging` module — no OpenTelemetry SDK instrumentation is required for basic log capture. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

```python
import logging

class MyCustomModel(mlflow.pyfunc.PythonModel):
    def predict(self, context, model_input):
        # This log will be persisted to the <prefix>_otel_logs table
        logging.warning("Received inference request")
        try:
            # Your model logic here
            result = model_input * 2
            return result
        except Exception as e:
            # Error logs are also captured with severity 'ERROR'
            logging.error(f"Inference failed: {e}")
            raise e
```

The root logging level defaults to `WARNING`. To capture lower-severity logs, you must change the level in the model's `load_context` method. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Pattern 2: OpenTelemetry Custom Metrics and Traces

For richer observability beyond basic logging, you can instrument your model with the OpenTelemetry SDK to create custom counters, record spans, and attach custom attributes. This pattern requires adding the OpenTelemetry SDK and exporter packages as pip requirements when logging the model. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

### OpenTelemetry Initialization

Instrumentation typically includes:
- Creating a `TracerProvider` with a `BatchSpanProcessor` using an `OTLPSpanExporter`
- Creating a `MeterProvider` with a `PeriodicExportingMetricReader` using an `OTLPMetricExporter`
- Creating counters, histograms, or other metric instruments
- Starting spans within prediction methods and attaching attributes

Because of model serialization limitations, the model class must be written to a separate file before logging using `%%writefile` or equivalent, rather than defined inline. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

### Model Logging with Dependencies

When using OpenTelemetry instrumentation, the model must be logged with the required pip dependencies:

```python
mlflow.pyfunc.log_model(
    python_model="return_input_model.py",
    pip_requirements=[
        "opentelemetry-sdk",
        "opentelemetry-exporter-otlp-proto-http",
    ],
)
```

The model should be registered with `env_pack="databricks_model_serving"` to ensure proper packaging for the serving environment. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Pattern 3: Telemetry Configuration

Telemetry can be enabled when creating a new serving endpoint or added to an existing endpoint. The configuration specifies a Unity Catalog destination for the telemetry tables. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

### UI Configuration

In the endpoint creation UI, expand the **Endpoint telemetry** section and select the target [Catalog and Schema](/concepts/catalog-and-schema.md). An optional table prefix can be provided; if blank, the tables are named `_otel_logs`, `_otel_spans`, and `_otel_metrics`. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

### API Configuration

Using the Serving Endpoints API, you can specify the full table names in the `telemetry_config`:

```json
{
  "telemetry_config": {
    "table_names": {
      "logs_table": "my_catalog.observability.custom_endpoint_logs",
      "metrics_table": "my_catalog.observability.custom_endpoint_metrics",
      "traces_table": "my_catalog.observability.custom_endpoint_spans"
    }
  }
}
```

Tables are automatically created in the specified schema if they do not already exist. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Querying Telemetry Data

Once the endpoint receives traffic, telemetry data streams to the Unity Catalog tables. You can query the data using standard SQL. Common queries include: ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

- Viewing all log entries: `SELECT * FROM <catalog>.<schema>.<prefix>_otel_logs`
- Checking for errors in the last hour: `SELECT timestamp, severity_text, body, attributes FROM ... WHERE severity_text = 'ERROR' AND timestamp > current_timestamp() - INTERVAL 1 HOUR`

Useful columns for filtering include `timestamp`, `severity_text`, `body`, `trace_id`, `span_id`, and `attributes` (a map containing event-specific metadata). ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Requirements and Limitations

### Requirements
- The workspace must be enabled for Unity Catalog (default Arclight storage is not supported). ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]
- Users need `USE CATALOG`, `USE SCHEMA`, `CREATE TABLE`, and `MODIFY` permissions on the destination [Catalog and Schema](/concepts/catalog-and-schema.md). ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]
- The workspace must be in a supported region (including `us-east-1`, `us-east-2`, `us-west-2`, `eu-central-1`, and others). ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

### Limitations
- Schema evolution on target tables is not supported. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]
- Only managed Delta tables are supported; external storage and Arclight default storage are not. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]
- Table names must contain only ASCII letters, digits, and underscores. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]
- Delivery is at-least-once. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]
- Individual records must be less than 10 MB, log lines less than 1 MB, and requests less than 30 MB. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]
- Telemetry latency degrades beyond 2500 QPS. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]
- Logs typically appear in the Unity Catalog table a few seconds after emission. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The serving infrastructure that hosts custom models
- [Unity Catalog](/concepts/unity-catalog.md) — The governance and storage layer for telemetry data
- OpenTelemetry — The observability framework used for instrumentation
- MLflow PyFunc — The model flavor used for custom model serving
- [Delta Tables](/concepts/delta-lake-table.md) — The storage format for telemetry tables

## Sources

- persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md

# Citations

1. [persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md](/references/persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws-49ce2f2e.md)
