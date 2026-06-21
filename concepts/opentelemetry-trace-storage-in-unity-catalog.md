---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ade82c12290c1ece044fd19088d832cfa981ced7eea02d950af9c0a37fb080db
  pageDirectory: concepts
  sources:
    - redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md
  confidence: 0.75
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - opentelemetry-trace-storage-in-unity-catalog
    - OTSIUC
    - Query OpenTelemetry traces stored in Unity Catalog
  citations:
    - file: redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md
title: OpenTelemetry Trace Storage in Unity Catalog
description: The foundational capability to store OTel trace data (spans, logs, annotations) as Delta tables in Unity Catalog, enabling SQL-based querying and integration with Databricks governance and processing tools.
tags:
  - observability
  - databricks
  - unity-catalog
  - opentelemetry
timestamp: "2026-06-19T20:12:44.562Z"
---

# OpenTelemetry Trace Storage in Unity Catalog

**OpenTelemetry Trace Storage in Unity Catalog** refers to the capability of persisting OpenTelemetry (OTel) trace data into managed tables within [Unity Catalog](/concepts/unity-catalog.md), enabling query, analysis, and governance of trace data alongside other enterprise data assets.

## Overview

OpenTelemetry trace data is stored in Unity Catalog as Delta tables. These tables contain raw span, log, and annotation information produced by instrumented applications. The storage scheme follows a consistent naming pattern: source tables are named `{catalog}.{source_schema}.{table_prefix}_otel_spans`, `{catalog}.{source_schema}.{table_prefix}_otel_logs`, and `{catalog}.{source_schema}.{table_prefix}_otel_annotations`. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

This storage foundation supports both observability workflows and downstream processing, such as PII redaction, dashboarding, and drift analysis. The trace data can be ingested through multiple channels: [MLflow](/concepts/mlflow.md) (which can write OTel traces to Unity Catalog), a standard OTel exporter, or any OTLP-compatible client. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Table Structure

The three tables serve distinct roles:

- **`{prefix}_otel_spans`** — Contains the core span records, including trace ID, span ID, parent span ID, start and end timestamps, service name, status codes, and a `attributes` column (typically a structured map or JSON string) that holds span-level key-value pairs.
- **`{prefix}_otel_logs`** — Stores log records associated with spans, with fields such as timestamp, severity, body, and additional attributes.
- **`{prefix}_otel_annotations`** — Holds annotation or event data that is linked to specific spans, capturing custom metadata.

All tables are managed by Unity Catalog, so they inherit Unity Catalog’s access controls, lineage, and governance features. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Writing Traces

Traces are written to Unity Catalog by configuring an OTel exporter or by using MLflow’s tracing integration. The Databricks documentation provides a dedicated guide, *[Store OpenTelemetry traces in Unity Catalog](/concepts/opentelemetry-traces-in-unity-catalog.md)*, which covers the setup steps. Once written, the tables can be queried using standard SQL or the Unity Catalog API. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Data Governance and Access Control

Because the trace tables reside in Unity Catalog, each table is subject to fine-grained privilege management. Raw trace tables often contain personally identifiable information (PII) and should be restricted to administrators and pipeline service principals. Broader access can be granted to redacted copies of the data. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

A common deployment pattern is to create a secondary set of redacted tables (see [PII Redaction from OTel Traces](/concepts/pii-redaction-pipeline-for-opentelemetry-traces.md)) for analytics and observability, while the original raw tables are retained only as long as compliance permits. Auto time-to-live (TTL) can be configured on the raw tables to automatically delete data older than a set retention period (default 90 days). ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The unified governance layer for Databricks assets.
- OpenTelemetry — The observability framework that produces trace, log, and metric data.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — MLflow’s integration for recording OTel traces.
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) — A pipeline technology used to incrementally process OTel traces.
- [AI Functions](/concepts/ai-functions.md) — Used for redacting PII from trace attributes.
- [PII Redaction from OTel Traces](/concepts/pii-redaction-pipeline-for-opentelemetry-traces.md) — An example solution that processes raw trace tables and writes redacted copies.

## Sources

- redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md

# Citations

1. [redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md](/references/redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws-b16a55be.md)
