---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2d0c1a2daa098d7cc444236b30d0f1322c4e9248852426e97684bb9c86dfc128
  pageDirectory: concepts
  sources:
    - export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - cross-framework-trace-consolidation
    - CTC
  citations:
    - file: export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
title: Cross-Framework Trace Consolidation
description: The practice of routing traces from multiple instrumentation frameworks (Langfuse, OpenTelemetry SDKs, etc.) to a single Databricks MLflow backend for unified querying, comparison, and governance.
tags:
  - observability
  - databricks
  - tracing
timestamp: "2026-06-19T10:27:42.045Z"
---

# Cross-Framework Trace Consolidation

**Cross-Framework Trace Consolidation** is the practice of centralizing OpenTelemetry-based trace spans from multiple instrumentation frameworks — such as Langfuse, OpenAI, Anthropic, and custom applications — into a single storage and analysis platform. On Databricks, this is achieved by routing traces from various frameworks to [MLflow](/concepts/mlflow.md)'s OTLP endpoint, where they are stored in [Unity Catalog](/concepts/unity-catalog.md) tables alongside native MLflow traces. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Benefits

Consolidating traces across frameworks onto Databricks provides several advantages: ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

- **Unified querying**: Langfuse-instrumented calls can be queried and compared together with traces from other frameworks in a single place.
- **Scalable analysis**: Databricks SQL can be used to analyze trace data at scale.
- **Governance**: [Unity Catalog governance](/concepts/unity-catalog-governance.md) mechanisms such as access controls and lineage apply to all consolidated traces.

## How It Works

### OTLP Endpoint

Databricks MLflow exposes an OpenTelemetry Protocol (OTLP) endpoint at `https://<workspace-host>/api/2.0/otel/v1/traces`. Framework-specific exporters can be configured to send spans to this endpoint. A custom HTTP header (`X-Databricks-UC-Table-Name`) routes incoming spans to the appropriate Unity Catalog table. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

### Framework Configuration

Each third-party framework requires its own configuration to redirect trace output to the Databricks OTLP endpoint rather than its native server. For Langfuse, this involves: ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

1. Setting dummy environment variables (`LANGFUSE_HOST`, `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`) to prevent traces from being sent to the Langfuse server.
2. Initializing the Langfuse client to register its TracerProvider as the global OpenTelemetry TracerProvider.
3. Retrieving the global provider and attaching a BatchSpanProcessor with an OTLPSpanExporter configured to point to the Databricks endpoint.

### Trace Location

Before ingesting traces, a Unity Catalog location must be linked to an [MLflow Experiment](/concepts/mlflow-experiment.md) using `set_experiment_trace_location()`. This defines the [Catalog and Schema](/concepts/catalog-and-schema.md) where trace data is stored and returns the fully qualified OTel spans table name needed for the `X-Databricks-UC-Table-Name` header. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Supported Frameworks

Cross-framework trace consolidation supports any framework that emits OpenTelemetry spans. Documented integrations include:

- Langfuse — Using the Langfuse SDK's `@observe()` decorator, with spans redirected via the OTLP exporter. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Implementation Requirements

- A Databricks workspace with the "OpenTelemetry on Databricks" preview enabled. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]
- A new MLflow experiment to receive the traces. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]
- Appropriate packages for the framework being integrated (e.g., `langfuse>=3.14.5`, `mlflow[databricks]>=3.10.0`, OpenTelemetry SDK and exporter packages). ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Related Concepts

- OpenTelemetry Tracing on Databricks
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- Unity Catalog Integration for Traces
- Querying Trace Data with Databricks SQL
- Third-Party Trace Ingestion

## Sources

- export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md

# Citations

1. [export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md](/references/export-langfuse-traces-to-databricks-mlflow-databricks-on-aws-edce6b99.md)
