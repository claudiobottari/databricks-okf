---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 902ddad500043d54c8cde42fbf36715e95625cd8c826387bddfe71bce3e09f7b
  pageDirectory: concepts
  sources:
    - pii-redaction-from-otel-traces-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opentelemetry-traces-in-unity-catalog
    - OTIUC
    - Store OpenTelemetry Traces in Unity Catalog
    - Store OpenTelemetry traces in Unity Catalog
    - Storing OpenTelemetry Traces in Unity Catalog
  citations:
    - file: pii-redaction-from-otel-traces-reference-databricks-on-aws.md
title: OpenTelemetry Traces in Unity Catalog
description: Storage of OTel spans, logs, and annotations as managed Delta tables in Unity Catalog with a defined schema and trace_unified view.
tags:
  - opentelemetry
  - unity-catalog
  - delta-tables
  - tracing
timestamp: "2026-06-19T19:56:03.895Z"
---

# OpenTelemetry Traces in Unity Catalog

**OpenTelemetry (OTel) Traces in Unity Catalog** refers to the storage and management of OpenTelemetry span data as managed tables within [Unity Catalog](/concepts/unity-catalog.md). Databricks enables this through an [MLflow](/concepts/mlflow.md) trace-to-Unity Catalog binding, which writes OTel spans, logs, and annotations into three Delta tables: `{table_prefix}_otel_spans`, `{table_prefix}_otel_logs`, and `{table_prefix}_otel_annotations`. These tables are defined using parameters such as `source_catalog`, `source_schema`, and `table_prefix`, allowing reuse across environments. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

When storing OTel traces in Unity Catalog, users can leverage a reference architecture for redacting Personally Identifiable Information (PII) from the spans. The architecture provides two complementary flows: a server‑side batch processing pipeline (recommended) and a view‑based on‑read redaction approach. Both flows use [AI Functions](/concepts/ai-functions.md) (such as `ai_mask`) and [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md). ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## Flow 1: Server‑Side Batch Processing (Recommended)

This flow materializes redacted tables from the raw OTel tables using a Lakeflow Spark Declarative Pipeline with streaming tables. OTel spans are append‑only, making them ideal for incremental ingestion in streaming tables. AI functions are built into SQL, so a SQL pipeline is the simplest implementation. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

### Architecture

The pipeline reads from the raw OTel tables (`_otel_spans`, `_otel_logs`, `_otel_annotations`), applies `ai_mask` to redact PII from the `attributes`, `resource:attributes`, `events`, and `body` columns (VARIANT or STRING fields), and writes redacted streaming tables (`redacted_spans`, `redacted_logs`, `redacted_annotations`). The annotations table is passed through without redaction because no PII is expected. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

### Implementation Steps

1. **Lock down raw tables** – Grant access only to the pipeline service principal and administrators. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]
2. **Create the pipeline SQL** – Define three `CREATE OR REFRESH STREAMING TABLE` statements that apply `ai_mask` to the appropriate columns. The PII categories to redact (e.g., `'email','phone','ssn','name','address'`) are passed as a parameter. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]
3. **Create the pipeline resource** – Configure a pipeline with `serverless: true`, `continuous: false` (triggered mode is typical), and the path to the SQL file. A triggered schedule (e.g., every 15 minutes or hourly) is recommended; continuous mode increases cost. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]
4. **Create a unified view** – A view (e.g., `trace_unified`) joins the redacted spans and annotations tables to reconstruct full traces with PII removed. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]
5. **Grant broader access** – Provide `SELECT` on the redacted tables to the data team. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

If `retention_days` is configured, use **auto time‑to‑live (auto‑TTL)** on the raw tables to automatically delete expired rows. The OTel tables have `time TIMESTAMP` columns, so auto‑TTL is supported when Predictive Optimization is enabled. Exact deletion timing is not guaranteed; there can be a buffer of up to 6 days plus the data retention duration. For strict compliance, a scheduled job with manual `DELETE` and `VACUUM` is recommended as a fallback. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## Flow 2: View‑Based Redaction (No Data Duplication)

This flow applies `ai_mask` in a Unity Catalog view, so redaction happens at query time and no redacted copy is materialized. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

### When to Use

- Storage cost is a primary concern.
- Redacted data is queried infrequently.
- It is acceptable to pay the compute cost on every query.

### Implementation

A single `CREATE OR REPLACE VIEW` statement wraps the raw spans table and applies `ai_mask` to the `attributes`, `events`, and `resource:attributes` columns. The view is stored in the target [Catalog and Schema](/concepts/catalog-and-schema.md). ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

### Trade‑Offs

The flow comparison highlights that Flow 1 (batch pipeline) preserves full‑fidelity raw data for authorized debugging, optimizes query performance through materialization, and supports GDPR compliance with auto‑TTL. Flow 2 is lighter but lacks those benefits^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md].

## Recommended Approach

Use **Flow 1 (batch pipeline)** as the primary solution for most enterprise deployments because it:

- Preserves full‑fidelity data for authorized debugging.
- Optimizes query performance through materialization.
- Supports GDPR compliance with auto‑TTL retention on raw data.
- Handles both PII redaction and trace filtering in one pipeline.
- Is fully managed with built‑in monitoring and alerting.

Use **Flow 2 (view‑based)** as a lightweight option for low‑query‑volume scenarios, or as a quick interim solution while setting up Flow 1. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## Prerequisites

- **AI Functions enabled** – Requires a SQL warehouse or serverless compute with AI Functions access.
- **Unity Catalog** – OTel traces must be stored in Unity Catalog tables with MLflow trace‑to‑Unity Catalog binding configured (see [Store OpenTelemetry traces in Unity Catalog](/concepts/opentelemetry-traces-in-unity-catalog.md)).
- **Service principal** – For pipeline execution, with appropriate grants on the source tables.
- **Foundation model endpoint** – `ai_mask` uses a foundation model. The endpoint must be available and sized for throughput. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## Sources

- pii-redaction-from-otel-traces-reference-databricks-on-aws.md

# Citations

1. [pii-redaction-from-otel-traces-reference-databricks-on-aws.md](/references/pii-redaction-from-otel-traces-reference-databricks-on-aws-426a48ea.md)
