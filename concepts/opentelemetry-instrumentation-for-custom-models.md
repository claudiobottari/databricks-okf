---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a218a611c36acb675554416284ec1ab7341d9c2659e1e72d8d828597715d3d93
  pageDirectory: concepts
  sources:
    - persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opentelemetry-instrumentation-for-custom-models
    - OIFCM
  citations:
    - file: persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md
title: OpenTelemetry Instrumentation for Custom Models
description: Using the OpenTelemetry SDK to instrument MLflow pyfunc models with custom counters, spans, attributes, and logging for endpoint telemetry capture.
tags:
  - opentelemetry
  - model-instrumentation
  - mlflow
  - python
timestamp: "2026-06-19T19:54:59.531Z"
---

# OpenTelemetry Instrumentation for Custom Models

**OpenTelemetry Instrumentation for Custom Models** refers to the process of adding OpenTelemetry SDK instrumentation to custom model serving code on Databricks to capture custom metrics, traces, and logs beyond the basic logging that is automatically collected. This instrumentation enables root cause analysis, endpoint health monitoring, and compliance reporting through persisted telemetry data stored in Unity Catalog tables. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Overview

When deploying custom models on Databricks Model Serving, endpoint telemetry can be configured to persist OpenTelemetry logs, traces, and metrics to Unity Catalog tables. While standard Python `logging` output is automatically captured without any OpenTelemetry SDK instrumentation, custom metrics and traces require explicit instrumentation using the OpenTelemetry SDK. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Basic Logging (No Instrumentation Required)

Endpoint telemetry automatically captures standard Python `logging` output. No OpenTelemetry SDK instrumentation is needed for basic logging. The root logging level defaults to `WARNING`, meaning only warnings and errors are captured by default. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

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

^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Custom Metrics and Traces (OpenTelemetry SDK Required)

To capture custom metrics and traces beyond basic logging, add OpenTelemetry SDK instrumentation to your model code. This allows you to create counters, record spans, and attach custom attributes. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

### Important: Model Serialization Limitation

Due to limitations in model serialization, you must write your model to a separate file before logging to avoid errors. Use `%%writefile` in a notebook cell to create the model file. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

### Example: Custom Metrics, Spans, and Model Logging

The following example demonstrates how to initialize OpenTelemetry providers, create a counter metric, record spans with custom attributes, and log the model with the required dependencies: ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

```python
%%writefile return_input_model.py

import os
import mlflow
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.metrics import get_meter, set_meter_provider
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.trace import get_tracer, set_tracer_provider

# ---- OTel initialization (per-worker) ----
resource = Resource.create({
    "worker.pid": str(os.getpid()),
})

otlp_trace_exporter = OTLPSpanExporter()
tracer_provider = TracerProvider(resource=resource)
tracer_provider.add_span_processor(BatchSpanProcessor(otlp_trace_exporter))
set_tracer_provider(tracer_provider)

otlp_metric_exporter = OTLPMetricExporter()
metric_reader = PeriodicExportingMetricReader(otlp_metric_exporter)
meter_provider = MeterProvider(metric_readers=[metric_reader], resource=resource)
set_meter_provider(meter_provider)

_tracer = get_tracer(__name__)
_meter = get_meter(__name__)

_prediction_counter = _meter.create_counter(
    name="prediction_count",
    description="Number of predictions made",
    unit="1"
)

class ReturnInputModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        self.tracer = _tracer
        self.prediction_counter = _prediction_counter

    def predict(self, context, model_input):
        with self.tracer.start_as_current_span("ReturnInputModel.predict") as span:
            span.set_attribute("input_shape", str(model_input.shape))
            span.set_attribute("input_columns", str(list(model_input.columns)))
            self.prediction_counter.add(1)
            return model_input

mlflow.models.set_model(ReturnInputModel())
```

### Logging and Registering the Model

After creating the model file, log and register the model with the required OpenTelemetry dependencies: ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

```python
import pandas as pd
import mlflow
from mlflow.models import infer_signature

# Prepare tabular input/output for signature (pyfunc expects DataFrame)
input_df = pd.DataFrame({"inputs": ["hello world"]})
output_df = input_df.copy()  # model returns input unchanged

# Log the model with OpenTelemetry dependencies
with mlflow.start_run():
    signature = infer_signature(input_df, output_df)
    model_info = mlflow.pyfunc.log_model(
        name="model",
        python_model="return_input_model.py",
        signature=signature,
        input_example=input_df,
        pip_requirements=[
            "mlflow==3.1",
            "opentelemetry-sdk",
            "opentelemetry-exporter-otlp-proto-http",
        ],
    )

# Register with express deployment environment packing
registered = mlflow.register_model(
    model_info.model_uri,
    MODEL_NAME,
    env_pack="databricks_model_serving",
)
```

## Telemetry Tables

When endpoint telemetry is enabled, Databricks automatically creates three Unity Catalog tables in the configured schema: ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

| Table Name | Description |
|---|---|
| `<prefix>_otel_logs` | Captured log records from the model |
| `<prefix>_otel_spans` | Captured trace spans |
| `<prefix>_otel_metrics` | Captured metric data points |

The prefix is optional and configurable when enabling telemetry. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Querying Telemetry Data

Telemetry data can be queried using standard SQL. Key columns for filtering and correlation include: ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

- `timestamp`
- `severity_text`
- `body`
- `trace_id`
- `span_id`
- `attributes` — a map containing event-specific metadata

### Example: Check for Errors in the Last Hour

```sql
SELECT
  timestamp,
  severity_text,
  body,
  attributes
FROM <catalog>.<schema>.<prefix>_otel_logs
WHERE
  severity_text = 'ERROR'
  AND timestamp > current_timestamp() - INTERVAL 1 HOUR
ORDER BY timestamp DESC;
```

^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Troubleshooting

**Logs not appearing in table**: The root logging level defaults to `WARNING` to reduce overhead. To capture lower-severity logs, change the level in your model code: ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

```python
class MyModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        for handler in root.handlers:
            handler.setLevel(logging.DEBUG)
```

## Limitations

The following limits apply to endpoint telemetry: ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

- Schema evolution on the target table is not supported.
- Only managed Delta tables are supported. External storage and Arclight default storage are not supported.
- The table location must be in the same region as your workspace.
- Only table names with ASCII letters, digits, and underscores are supported.
- Recreating a target table is not supported.
- Only single availability zone (single-az) durability is supported.
- Delivery is at-least-once.
- Records must be less than 10 MB each.
- Requests must be less than 30 MB each.
- Log lines must be less than 1 MB each.
- Telemetry latency degrades beyond 2500 QPS.
- Logs appear in the Unity Catalog table a few seconds after they are emitted.

## Related Concepts

- [Custom Model Serving](/concepts/custom-model-serving-endpoint-support.md) — The deployment infrastructure for custom models on Databricks
- [Unity Catalog](/concepts/unity-catalog.md) — The governance and storage layer for telemetry data
- MLflow PyFunc — The model flavor used for custom model serving
- OpenTelemetry — The observability framework used for instrumentation
- [Model Serving Endpoint Telemetry](/concepts/model-serving-endpoint-telemetry.md) — The broader feature for persisting endpoint observability data

## Sources

- persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md

# Citations

1. [persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md](/references/persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws-49ce2f2e.md)
