---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7fcfa26f8635e34b916324e9e57a88717b3c84f99d7ee6cecb62742fb0bce116
  pageDirectory: concepts
  sources:
    - opentelemetry-export-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opentelemetry-collector-configuration-for-mlflow
    - OCCFM
    - OpenTelemetry Collector Setup
  citations:
    - file: opentelemetry-export-databricks-on-aws.md
title: OpenTelemetry Collector Configuration for MLflow
description: MLflow uses the standard OTLP exporter to send traces and metrics to an OpenTelemetry Collector, supporting configuration of endpoint URL, protocol (gRPC vs HTTP), headers, and service name through environment variables.
tags:
  - OpenTelemetry
  - configuration
  - MLflow
timestamp: "2026-06-19T19:52:02.606Z"
---

# OpenTelemetry Collector Configuration for MLflow

**OpenTelemetry Collector Configuration for MLflow** refers to the setup and configuration required to export MLflow traces to an OpenTelemetry Collector, enabling integration with various observability platforms. MLflow traces are compatible with the OpenTelemetry trace specification, allowing them to be exported to any observability solution that supports OpenTelemetry. ^[opentelemetry-export-databricks-on-aws.md]

## Export Modes

MLflow supports three export modes for traces:

1. **MLflow tracking only (Default)**: Traces are sent only to the MLflow Tracking Server.
2. **OpenTelemetry only**: Traces are sent only to an OpenTelemetry Collector.
3. **Dual export**: Traces are sent to both MLflow Tracking and an OpenTelemetry Collector.

^[opentelemetry-export-databricks-on-aws.md]

## Basic OpenTelemetry Export Configuration

To export traces *only* to an OpenTelemetry Collector instead of the MLflow Tracking Server, set the `OTEL_EXPORTER_OTLP_ENDPOINT` or `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` environment variable to the target URL of the OpenTelemetry Collector *before starting any trace*. Optionally, set the `OTEL_SERVICE_NAME` to group traces by service. ^[opentelemetry-export-databricks-on-aws.md]

```python
import mlflow
import os

# Set the endpoint of the OpenTelemetry Collector
os.environ["OTEL_EXPORTER_OTLP_TRACES_ENDPOINT"] = "http://localhost:4317/v1/traces"

# Optionally, set the service name to group traces
os.environ["OTEL_SERVICE_NAME"] = "<your-service-name>"

# Trace will be exported ONLY to the OTel collector
with mlflow.start_span(name="foo") as span:
    span.set_inputs({"a": 1})
    span.set_outputs({"b": 2})
```

## Dual Export Configuration

Dual export sends traces to *both* Databricks MLflow and an OpenTelemetry Collector simultaneously. This allows you to maintain MLflow's tracking capabilities while also integrating with existing observability infrastructure. ^[opentelemetry-export-databricks-on-aws.md]

### Enabling Dual Export

Set the `MLFLOW_ENABLE_DUAL_EXPORT` environment variable along with your OpenTelemetry configuration: ^[opentelemetry-export-databricks-on-aws.md]

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
    # Your ML workflow here
    result = "Generated response"
    span.set_outputs({"response": result})
    span.set_attributes({"token_count": 15})
```

## Metrics Export Configuration

MLflow can also export [OpenTelemetry Metrics](/concepts/mlflow-opentelemetry-metrics-export.md) when a metrics endpoint is configured. This enables monitoring of span durations and other trace-related metrics in compatible monitoring systems. For a complete list of exported metrics, see MLflow's exported metrics documentation. ^[opentelemetry-export-databricks-on-aws.md]

### Enabling Metrics Export

To export metrics to an OpenTelemetry Collector, set the following environment variables: ^[opentelemetry-export-databricks-on-aws.md]

```python
import os

# Enable metrics export
os.environ["OTEL_METRICS_EXPORTER"] = "otlp"
os.environ["OTEL_EXPORTER_OTLP_METRICS_ENDPOINT"] = "http://localhost:4317"

# Optional: Configure metric export interval (in milliseconds)
os.environ["OTEL_METRIC_EXPORT_INTERVAL"] = "60000"  # Export every 60 seconds
```

## Collector Configuration Options

MLflow uses the standard OTLP Exporter for exporting traces to OpenTelemetry Collector instances. This means you can use all configurations supported by the OpenTelemetry SDK, including protocol selection, custom headers, and other exporter settings. ^[opentelemetry-export-databricks-on-aws.md]

The following example configures the OTLP Exporter to use HTTP protocol instead of the default gRPC and sets custom headers: ^[opentelemetry-export-databricks-on-aws.md]

```bash
export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT="http://localhost:4317/v1/traces"
export OTEL_EXPORTER_OTLP_TRACES_PROTOCOL="http/protobuf"
export OTEL_EXPORTER_OTLP_TRACES_HEADERS="api_key=12345"
```

## Related Concepts

- OpenTelemetry — The observability framework underlying MLflow's trace export
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing system that generates OpenTelemetry-compatible spans
- OTLP Exporter — The standard exporter used for sending traces to OpenTelemetry Collectors
- [OpenTelemetry Metrics](/concepts/mlflow-opentelemetry-metrics-export.md) — Metrics export capability for monitoring span durations
- [MLflow Tracking Server](/concepts/remote-mlflow-tracking-server.md) — The default destination for MLflow traces
- [OpenTelemetry Collector Setup](/concepts/opentelemetry-collector-configuration-for-mlflow.md) — Instructions for setting up collectors for specific observability platforms

## Sources

- opentelemetry-export-databricks-on-aws.md

# Citations

1. [opentelemetry-export-databricks-on-aws.md](/references/opentelemetry-export-databricks-on-aws-d0c0ee4c.md)
