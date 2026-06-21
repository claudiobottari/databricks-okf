---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 406a4c503ac7626376e3291d6e24a600a02b0fd65ba5b8873fe11adfa088cd1f
  pageDirectory: concepts
  sources:
    - opentelemetry-export-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-opentelemetry-metrics-export
    - MOME
    - OpenTelemetry Export
    - OpenTelemetry Metrics
  citations:
    - file: opentelemetry-export-databricks-on-aws.md
title: MLflow OpenTelemetry Metrics Export
description: MLflow can export OpenTelemetry metrics such as span durations to a configured metrics endpoint using OTLP protocol.
tags:
  - observability
  - MLflow
  - metrics
  - OpenTelemetry
timestamp: "2026-06-19T19:51:14.748Z"
---

## MLflow OpenTelemetry Metrics Export

**MLflow OpenTelemetry Metrics Export** enables sending trace-related metrics, such as span durations, from MLflow to compatible monitoring systems via the OpenTelemetry Collector. This integrates MLflow’s built-in tracing with existing observability infrastructure. ^[opentelemetry-export-databricks-on-aws.md]

### Overview

When MLflow’s [tracing](/concepts/mlflow-tracing.md) is enabled, traces are compatible with the OpenTelemetry trace specification. MLflow can export **metrics** in addition to traces when a metrics endpoint is configured. The exported metrics cover span durations and other trace-related statistics. For a complete list of the metrics that MLflow exports, see the [MLflow exported metrics documentation](https://mlflow.org/docs/latest/genai/tracing/prod-tracing/#exported-metrics). ^[opentelemetry-export-databricks-on-aws.md]

### Enable Metrics Export

To export metrics to an OpenTelemetry Collector, set the following environment variables **before** starting any trace: ^[opentelemetry-export-databricks-on-aws.md]

```python
import os

# Enable the OTLP metrics exporter
os.environ["OTEL_METRICS_EXPORTER"] = "otlp"

# Set the endpoint of the OpenTelemetry Collector for metrics
os.environ["OTEL_EXPORTER_OTLP_METRICS_ENDPOINT"] = "http://localhost:4317"

# Optional: Set the metric export interval (in milliseconds)
os.environ["OTEL_METRIC_EXPORT_INTERVAL"] = "60000"  # Export every 60 seconds
```

`OTEL_METRICS_EXPORTER` must be set to `"otlp"` to activate the OTLP exporter. `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT` specifies the collector’s metrics endpoint. The optional `OTEL_METRIC_EXPORT_INTERVAL` controls how frequently metrics are sent, with a default interval determined by the OpenTelemetry SDK. ^[opentelemetry-export-databricks-on-aws.md]

### Related Export Modes

MLflow offers three export modes for traces and metrics: ^[opentelemetry-export-databricks-on-aws.md]

- **MLflow tracking only (default):** Data is sent only to the MLflow Tracking Server.
- **OpenTelemetry only:** Data is sent only to an OpenTelemetry Collector.
- **Dual export:** Data is sent to both MLflow Tracking and an OpenTelemetry Collector simultaneously.

When dual export is enabled via `MLFLOW_ENABLE_DUAL_EXPORT`, metrics can be exported to both destinations if the metrics endpoint is configured. The metrics export behavior follows the same mode as traces. ^[opentelemetry-export-databricks-on-aws.md]

### Configuration Details

MLflow uses the standard OTLP Exporter for exporting metrics. Therefore, all configurations supported by OpenTelemetry’s OTLP exporter (e.g., protocol, headers) are applicable. For example, to use HTTP/protobuf instead of the default gRPC and set custom headers: ^[opentelemetry-export-databricks-on-aws.md]

```bash
export OTEL_EXPORTER_OTLP_METRICS_ENDPOINT="http://localhost:4318/v1/metrics"
export OTEL_EXPORTER_OTLP_METRICS_PROTOCOL="http/protobuf"
export OTEL_EXPORTER_OTLP_METRICS_HEADERS="api_key=12345"
```

Refer to the [OpenTelemetry SDK configuration documentation](https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/) for a full list of options. ^[opentelemetry-export-databricks-on-aws.md]

### Related Concepts

- OpenTelemetry Collector
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- Dual Export (MLflow)
- OTLP Exporter

### Sources

- opentelemetry-export-databricks-on-aws.md

# Citations

1. [opentelemetry-export-databricks-on-aws.md](/references/opentelemetry-export-databricks-on-aws-d0c0ee4c.md)
