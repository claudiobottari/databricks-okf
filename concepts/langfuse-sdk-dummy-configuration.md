---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f858b6529e9bba716b8a9943116153df35ef441d00687c65f2057ce39c44ca4d
  pageDirectory: concepts
  sources:
    - export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - langfuse-sdk-dummy-configuration
    - LSDC
  citations:
    - file: export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md
title: Langfuse SDK Dummy Configuration
description: A technique that disables Langfuse's own trace collection by setting LANGFUSE_HOST, LANGFUSE_PUBLIC_KEY, and LANGFUSE_SECRET_KEY to dummy values, so only an attached OTLP exporter receives spans.
tags:
  - langfuse
  - configuration
  - observability
timestamp: "2026-06-19T10:27:37.813Z"
---

# Langfuse SDK Dummy Configuration

**Langfuse SDK Dummy Configuration** refers to setting placeholder or empty values for the required Langfuse environment variables (`LANGFUSE_HOST`, `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`) so that the Langfuse SDK initializes without sending traces to a Langfuse server. This is commonly used when exporting Langfuse‑instrumented OpenTelemetry spans exclusively to an alternative backend, such as the Databricks MLflow OTLP endpoint. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## When to Use

Use a dummy configuration when you want to:
- Keep Langfuse as the instrumentation framework (using its `@observe()` decorator) but route all trace spans to Databricks MLflow (or another OTLP‑compatible backend).
- Avoid sending data to the Langfuse cloud or self‑hosted server.
- Consolidate traces from multiple frameworks into a single Unity Catalog table for governance and analysis. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## How to Configure

The Langfuse SDK requires the environment variables `LANGFUSE_HOST`, `LANGFUSE_PUBLIC_KEY`, and `LANGFUSE_SECRET_KEY` to initialize. Setting them to dummy values prevents the SDK from establishing a connection to a real Langfuse server. The SDK still registers its OpenTelemetry `TracerProvider`, which can then be augmented with a custom span processor that forwards spans to a different destination. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

### Example

In a Databricks notebook or Python environment:

```python
import os

os.environ["LANGFUSE_HOST"] = "localhost"
os.environ["LANGFUSE_PUBLIC_KEY"] = ""
os.environ["LANGFUSE_SECRET_KEY"] = ""
```

After setting these, initialize the Langfuse client (e.g., `langfuse = get_client()`). The SDK will create a `TracerProvider`, but no spans will be sent to Langfuse because the host and credentials are invalid. You can then attach a `BatchSpanProcessor` with an `OTLPSpanExporter` pointing to Databricks or any other OTLP endpoint. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Alternative Method

Instead of dummy environment variables, you can disable Langfuse’s built‑in trace collection by setting the environment variable:

```python
os.environ["LANGFUSE_TRACING_ENABLED"] = "False"
```

This prevents Langfuse from collecting and sending traces on its own, while still allowing the OpenTelemetry `TracerProvider` to be used by a custom exporter. The dummy‑variable approach is simpler for most use cases, but the `LANGFUSE_TRACING_ENABLED` flag provides an explicit switch. ^[export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md]

## Related Concepts

- Langfuse Integration with Databricks – Full guide to exporting Langfuse traces to Databricks MLflow.
- [OpenTelemetry OTLP Exporter](/concepts/opentelemetry-export-for-mlflow-traces.md) – How to configure an OTLP exporter to send spans to Databricks.
- MLflow Tracing and Unity Catalog – Storing and querying traces in Unity Catalog tables.
- Langfuse SDK Initialization – Required environment variables and client setup.
- [Trace Governance with Unity Catalog](/concepts/ai-governance-unity-catalog.md) – Applying access controls and lineage to traces.

## Sources

- export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md

# Citations

1. [export-langfuse-traces-to-databricks-mlflow-databricks-on-aws.md](/references/export-langfuse-traces-to-databricks-mlflow-databricks-on-aws-edce6b99.md)
