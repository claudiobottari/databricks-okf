---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 632aaf34b2afcd5d147d4246264ab2717efd91940a5be9153feed507dcd09cfa
  pageDirectory: concepts
  sources:
    - pii-redaction-from-otel-traces-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - server-side-batch-pipeline-redaction
    - SBPR
    - Server-side Batch PII Redaction
  citations:
    - file: pii-redaction-from-otel-traces-reference-databricks-on-aws.md
title: Server-side Batch Pipeline Redaction
description: Recommended approach using Lakeflow Spark Declarative Pipelines to materialize redacted copies of OTel span, log, and annotation tables via incremental streaming.
tags:
  - pipeline
  - batch-processing
  - lakeflow
  - databricks
timestamp: "2026-06-19T19:55:46.973Z"
---

# Server-side Batch Pipeline Redaction

**Server-side Batch Pipeline Redaction** is a method for redacting personally identifiable information (PII) from OpenTelemetry (OTel) traces stored in [Unity Catalog](/concepts/unity-catalog.md). It uses a [Lakeflow Spark Declarative Pipeline](/concepts/lakeflow-spark-declarative-pipelines.md) to create materialized, PII‑redacted streaming tables from raw OTel span and log tables, and then grants broader access to the redacted outputs while locking down the original data. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## When to Use

This is the recommended approach for most enterprise deployments. It is the best fit when:

- Full‑fidelity raw data must be preserved for authorized debugging.
- Query performance matters, because redaction is applied once at write time and the results are materialized.
- Compliance requirements (e.g., GDPR) demand tight control over raw data, with automatic expiration via auto‑TTL.
- PII redaction and trace filtering can be handled in a single pipeline.

Use the alternative **view‑based redaction** (Flow 2) only when storage cost is the primary concern, redacted data is queried infrequently, or as a quick interim solution while setting up the batch pipeline. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## Architecture

The pipeline ingests the raw OTel tables (`{prefix}_otel_spans`, `{prefix}_otel_logs`, `{prefix}_otel_annotations`) as streaming sources. It applies the ai_mask SQL function on fields that may contain PII (attributes, events, log body, resource attributes), then writes the results into new streaming tables (`redacted_spans`, `redacted_logs`, `redacted_annotations`). Finally a unified view (`{prefix}_trace_unified`) is created on top of the redacted tables so that downstream consumers see only redacted data. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

![OTel PII redaction architecture](https://docs.databricks.com/aws/en/assets/images/otel-pii-redaction-arch-82ef68b664018915f5cccd1b607f277f.png)

## Implementation Steps

1. **Lock down raw tables** – Grant `SELECT` only to the pipeline service principal and admin users; revoke broad access. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

2. **Create the pipeline SQL** – Define streaming tables in a SQL file (e.g., `pii_redaction_pipeline.sql`). For each source table, the `SELECT` statement applies `ai_mask(CAST(field AS STRING), array(${pii_categories}))` to the relevant columns. Annotations are passed through unchanged because they are not expected to contain PII. The PII categories are parameterized (example: `array('email','phone','ssn','credit_card','name','address')`). ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

3. **Create the pipeline resource** – Provide a JSON configuration that specifies the pipeline name, target catalog/schema, serverless mode (set to `true`), and the `configuration` object with source locations and PII categories. The pipeline SQL file is referenced as a library. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

4. **Create the unified view** – Build a `CREATE OR REPLACE VIEW` that joins `redacted_spans` with `redacted_annotations` to produce the `trace_unified` view, matching the shape expected by MLflow Agent Evaluation and other tooling. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

5. **Grant broader access** – Assign `SELECT` on the target schema (which contains the redacted tables and view) to the data team or other consumers. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

6. **(Optional) Configure auto‑TTL** – If raw data retention is required, use `ALTER TABLE ... DELETE ROWS ${retention_days} DAYS AFTER time` to automatically expire rows from the raw OTel tables. This works because the tables are Unity Catalog managed Delta tables with a `time` column of type `TIMESTAMP`. Predictive optimization must be enabled on the workspace or table. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

The pipeline can be run in triggered mode (e.g., every 15 minutes or hourly) or in continuous mode (which increases cost). ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## Advantages

- **Performance** – Redaction is computed once at materialization time; queries against the redacted tables do not pay the cost of calling `ai_mask` on every read.
- **Security** – Raw tables have very restricted access; only the pipeline service principal can read them.
- **Compliance** – Auto‑TTL can automatically delete raw data after a configured retention period, supporting GDPR “right to erasure” requirements.
- **Fully managed** – The pipeline includes built‑in monitoring and alerting; no separate job scheduling is needed for auto‑TTL deletion. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## Prerequisites

- [AI Functions](/concepts/ai-functions.md) must be enabled on a SQL warehouse or serverless compute.
- OTel traces must be stored in Unity Catalog tables (configured via [MLflow trace-to-Unity Catalog binding](/concepts/mlflow-trace-storage-in-unity-catalog.md)).
- A service principal with appropriate grants on source tables must be available for pipeline execution.
- A foundation model endpoint (used by `ai_mask`) must be provisioned and scaled for the expected throughput. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## Related Concepts

- [View-based on-read redaction](/concepts/view-based-on-read-pii-redaction.md) – The alternative, storage‑light approach that redacts at query time.
- ai_mask – The SQL function used to redact PII from text fields.
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) – The engine that runs the batch redaction pipeline.
- [OpenTelemetry Traces in Unity Catalog](/concepts/opentelemetry-traces-in-unity-catalog.md) – The source data format.
- [Auto time-to-live (auto-TTL)](/concepts/auto-time-to-live-auto-ttl-for-unity-catalog-tables.md) – Mechanism for automatic row expiration on Delta tables.

## Sources

- pii-redaction-from-otel-traces-reference-databricks-on-aws.md

# Citations

1. [pii-redaction-from-otel-traces-reference-databricks-on-aws.md](/references/pii-redaction-from-otel-traces-reference-databricks-on-aws-426a48ea.md)
