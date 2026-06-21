---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4930c4716df258588b971c5304014439902245b04d8ed8180b7cea7ed70067e6
  pageDirectory: concepts
  sources:
    - opentelemetry-export-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dual-export-mlflow-opentelemetry
    - DE(+O
    - Observability with OpenTelemetry
  citations:
    - file: opentelemetry-export-databricks-on-aws.md
title: Dual Export (MLflow + OpenTelemetry)
description: A mode where traces are sent simultaneously to both the MLflow Tracking Server and an OpenTelemetry Collector, enabled via the MLFLOW_ENABLE_DUAL_EXPORT environment variable.
tags:
  - export
  - MLflow
  - OpenTelemetry
  - configuration
timestamp: "2026-06-19T19:51:00.869Z"
---

## Dual Export (MLflow + OpenTelemetry)

**Dual Export** is a configuration mode in MLflow that enables traces to be sent to **both** the [MLflow Tracking Server](/concepts/remote-mlflow-tracking-server.md) and an OpenTelemetry Collector simultaneously. This approach allows organizations to leverage MLflow’s native tracking capabilities while also integrating with existing OpenTelemetry-based observability infrastructure. ^[opentelemetry-export-databricks-on-aws.md]

### Export Modes

MLflow supports three trace export modes:

1. **MLflow tracking only (Default)**: Traces are sent only to the MLflow Tracking Server.
2. **OpenTelemetry only**: Traces are sent only to an OpenTelemetry Collector.
3. **Dual export (MLflow + OpenTelemetry)**: Traces are sent to both destinations.

^[opentelemetry-export-databricks-on-aws.md]

### Enabling Dual Export

To enable dual export, set the environment variable `MLFLOW_ENABLE_DUAL_EXPORT` to `"true"` **before starting any trace**. You must also configure the OpenTelemetry Collector endpoint and, optionally, the service name. For example:

```python
import mlflow
import os

# Enable dual export mode
os.environ["MLFLOW_ENABLE_DUAL_EXPORT"] = "true"

# Configure OpenTelemetry Collector endpoint
os.environ["OTEL_EXPORTER_OTLP_TRACES_ENDPOINT"] = "http://localhost:4317/v1/traces"
os.environ["OTEL_SERVICE_NAME"] = "my-ml-service"

# Configure MLflow tracking URI to Databricks
mlflow.set_tracking_uri("databricks")

# Traces will be exported to BOTH MLflow and the OTel collector
with mlflow.start_span(name="dual_export_example") as span:
    span.set_inputs({"model": "gpt-4", "prompt": "Hello world"})
    result = "Generated response"
    span.set_outputs({"response": result})
    span.set_attributes({"token_count": 15})
```

When dual export is active, every trace created by `mlflow.start_span()` is sent to both the configured MLflow Tracking Server and the specified OpenTelemetry Collector endpoint. ^[opentelemetry-export-databricks-on-aws.md]

### Configuration Details

#### Environment Variables

| Variable | Purpose | Required |
|----------|---------|----------|
| `MLFLOW_ENABLE_DUAL_EXPORT` | Set to `"true"` to enable dual export | Yes |
| `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` (or `OTEL_EXPORTER_OTLP_ENDPOINT`) | The URL of the OpenTelemetry Collector (e.g., `http://localhost:4317/v1/traces`) | Yes |
| `OTEL_SERVICE_NAME` | A logical service name to group traces in the collector | Optional |

^[opentelemetry-export-databricks-on-aws.md]

#### Collector Protocol and Headers

MLflow uses the standard OTLP Exporter and supports all OpenTelemetry SDK configurations. For example, you can switch from gRPC to HTTP/protobuf or add custom headers:

```bash
export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT="http://localhost:4317/v1/traces"
export OTEL_EXPORTER_OTLP_TRACES_PROTOCOL="http/protobuf"
export OTEL_EXPORTER_OTLP_TRACES_HEADERS="api_key=12345"
```

^[opentelemetry-export-databricks-on-aws.md]

### Metrics Export

In addition to traces, MLflow can export OpenTelemetry metrics (such as span durations) when a metrics endpoint is configured. To enable metrics export, set the following environment variables:

```python
os.environ["OTEL_METRICS_EXPORTER"] = "otlp"
os.environ["OTEL_EXPORTER_OTLP_METRICS_ENDPOINT"] = "http://localhost:4317"
# Optional: set export interval in milliseconds
os.environ["OTEL_METRIC_EXPORT_INTERVAL"] = "60000"  # Export every 60 seconds
```

For a complete list of exported metrics, see MLflow’s exported metrics documentation. ^[opentelemetry-export-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The underlying trace generation mechanism from MLflow.
- OpenTelemetry Collector – The daemon that receives, processes, and exports telemetry data.
- OTLP Exporter – The standard OpenTelemetry protocol exporter used by MLflow.
- [MLflow Tracking Server](/concepts/remote-mlflow-tracking-server.md) – The native destination for MLflow traces.
- OpenTelemetry Integration – General overview of MLflow's OpenTelemetry compatibility.
- Production Tracing – Using exported traces to monitor production applications.

### Sources

- opentelemetry-export-databricks-on-aws.md

# Citations

1. [opentelemetry-export-databricks-on-aws.md](/references/opentelemetry-export-databricks-on-aws-d0c0ee4c.md)
