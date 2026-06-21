---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 55a28074a3777f501bef8fc632567924c2f1a24ac9d9df6edf8ccd2723abe34b
  pageDirectory: concepts
  sources:
    - redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lakeflow-spark-declarative-pipelines
    - LSDP
    - Databricks Lakeflow Spark Declarative Pipelines
    - Lakeflow Spark Declarative Pipeline
    - Declarative Pipelines
    - Lakeflow Spark Declarative Pipelines Python programming interface
  citations:
    - file: redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md
    - file: |-
        redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md

        - **Continuous mode**: Runs the pipeline continuously
    - file: processing new data as it arrives. No separate scheduling job is created. This mode offers lower latency but has higher compute costs because the pipeline infrastructure is always running. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md
title: Lakeflow Spark Declarative Pipelines
description: A Databricks pipeline framework supporting incremental (triggered or continuous) data processing, used here to read new OTel spans, apply transformations like PII redaction, and write results to target tables.
tags:
  - data-engineering
  - databricks
  - pipeline
  - spark
timestamp: "2026-06-19T20:12:24.437Z"
---

# Lakeflow Spark Declarative Pipelines

**Lakeflow Spark Declarative Pipelines** is a pipeline framework on Databricks that enables incremental, declarative data processing using Spark and [Unity Catalog](/concepts/unity-catalog.md). It allows users to define transformations in SQL or Python and have them executed incrementally as new data arrives, without manual orchestration. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Overview

Lakeflow Spark Declarative Pipelines provide a declarative approach to building data pipelines: you specify *what* transformation to apply, and the framework handles *how* and *when* to process it. The pipelines can be configured to run in either a triggered mode (on a schedule) or a continuous mode (processing data as it arrives). ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## How it works

A Lakeflow Spark Declarative Pipeline incrementally reads new data from source tables in Unity Catalog, applies user-defined transformations (e.g., using SQL or Python with [AI Functions](/concepts/ai-functions.md)), and writes the results to target tables. The pipeline automatically tracks which data has already been processed, so subsequent runs only handle new or changed records. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

A common use case is [PII redaction](/concepts/ai-functions-for-pii-redaction.md) of OpenTelemetry traces: the pipeline reads new raw span records, applies the `ai_mask` function to redact sensitive fields, and writes the redacted results to a separate table. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Execution modes

- **Triggered mode**: Creates a scheduled job that triggers the pipeline at a chosen frequency. The pipeline processes new data on each run and then stops. This mode is cost-efficient for workloads that can tolerate some latency. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md

- **Continuous mode**: Runs the pipeline continuously, processing new data as it arrives. No separate scheduling job is created. This mode offers lower latency but has higher compute costs because the pipeline infrastructure is always running. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Prerequisites

To use Lakeflow Spark Declarative Pipelines, you need:

- A [Unity Catalog](/concepts/unity-catalog.md)-enabled workspace.
- Access to AI Functions via a serverless SQL warehouse or a serverless pipeline (if using AI Functions in transformations).
- Data stored in Unity Catalog tables. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Related concepts

- [AI Functions](/concepts/ai-functions.md) – Used to enrich or redact data within pipeline transformations.
- OpenTelemetry – Observability data that can be processed by these pipelines.
- [Unity Catalog](/concepts/unity-catalog.md) – The metadata and governance layer that stores input and output tables.
- Incremental Processing – The core mechanism that avoids reprocessing old data.
- [PII Redaction](/concepts/ai-functions-for-pii-redaction.md) – A typical use case for Lakeflow pipelines.
- Serverless Pipeline – The compute infrastructure that runs continuous pipelines.

## Sources

- redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md

# Citations

1. [redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md](/references/redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws-b16a55be.md)
2. redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md

- **Continuous mode**: Runs the pipeline continuously
3. processing new data as it arrives. No separate scheduling job is created. This mode offers lower latency but has higher compute costs because the pipeline infrastructure is always running. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md
