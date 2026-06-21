---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: df29ec33de76d50442d02e3b7d3670e28d511c5c1e9b04e8c10059c5eb6c8eb6
  pageDirectory: concepts
  sources:
    - pii-redaction-from-otel-traces-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-functions-for-pii-redaction
    - AFFPR
    - PII Redaction
    - PII redaction
  citations:
    - file: pii-redaction-from-otel-traces-reference-databricks-on-aws.md
title: AI Functions for PII Redaction
description: Built-in Databricks SQL functions (ai_mask) that use foundation models to detect and mask personally identifiable information in free-text columns.
tags:
  - pii
  - ai-functions
  - databricks-sql
  - redaction
timestamp: "2026-06-19T19:55:36.176Z"
---

# AI Functions for PII Redaction

**AI Functions for PII Redaction** refers to the use of Databricks' built-in SQL AI functions — primarily `ai_mask` — to detect and redact personally identifiable information (PII) from OpenTelemetry (OTel) trace data stored in [Unity Catalog](/concepts/unity-catalog.md). This approach enables organizations to comply with data privacy regulations while preserving the utility of trace data for debugging and monitoring.

## Overview

AI Functions provide a SQL-native interface for applying large language model (LLM) capabilities directly within queries. For PII redaction, the `ai_mask` function identifies sensitive content such as email addresses, phone numbers, social security numbers, credit card numbers, names, and physical addresses, then replaces them with masked values. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

The solution is designed for OpenTelemetry spans stored in Unity Catalog tables, which are automatically created when MLflow trace-to-Unity Catalog binding is configured. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## Key Function: `ai_mask`

The `ai_mask` function accepts two parameters: the text content to redact and an array of PII categories to detect. It is applied to free-text fields within OTel span data, including attributes, events, log bodies, and resource attributes. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

```sql
ai_mask(
  CAST(attributes AS STRING),
  array('email', 'phone', 'ssn', 'credit_card', 'name', 'address')
)
```

The function requires a SQL warehouse or serverless compute with AI Functions access, and it depends on a foundation model endpoint being available and sized for the expected throughput. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## Supported PII Categories

The configurable PII categories include:

- `email` — Email addresses
- `phone` — Phone numbers
- `ssn` — Social security numbers
- `credit_card` — Credit card numbers
- `name` — Personal names
- `address` — Physical addresses

These categories are passed as an array parameter and can be customized per deployment. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## Implementation Flows

### Flow 1: Server-Side Batch Processing (Recommended)

This approach uses [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) with streaming tables to materialize redacted copies of the raw OTel tables. AI Functions are embedded directly in the SQL pipeline definition. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

The pipeline creates three redacted streaming tables:
- `redacted_spans` — PII-redacted span data
- `redacted_logs` — PII-redacted log data
- `redacted_annotations` — Passthrough (no PII expected)

A unified view (`trace_unified`) is then created on top of the redacted tables for querying. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

**Advantages:**
- Preserves full-fidelity raw data for authorized debugging
- Optimizes query performance through materialization
- Supports GDPR compliance with auto-TTL retention on raw data
- Fully managed with built-in monitoring and alerting

### Flow 2: View-Based Redaction (No Data Duplication)

This approach applies `ai_mask` in a Unity Catalog view, so redaction happens at read time and no redacted copy is stored. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

**When to use:**
- Storage cost is a primary concern
- Redacted data is queried infrequently
- It is acceptable to pay the compute cost on every query

## Access Control

The solution implements a two-tier access model:

1. **Raw tables** — Access restricted to the pipeline service principal and administrator users
2. **Redacted tables/views** — Broader access granted to data teams and analysts

This ensures that sensitive PII is only visible to authorized personnel while redacted data is available for general use. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## Prerequisites

- AI Functions enabled on the workspace
- OTel traces stored in Unity Catalog tables with MLflow trace-to-Unity Catalog binding configured
- A service principal for pipeline execution with appropriate grants
- A foundation model endpoint for `ai_mask` that is available and sized for throughput

## Implementation Checklist

- Validate `ai_mask` behavior on VARIANT columns with sample OTel span data
- Benchmark `ai_mask` throughput to size the pipeline schedule interval
- Define allowlisted attribute keys that should skip redaction
- Set up access control groups (raw access versus redacted access)
- Configure auto-TTL for raw table retention
- Build a monitoring dashboard for pipeline health and redaction coverage

## Related Concepts

- [AI Functions](/concepts/ai-functions.md) — SQL-native LLM capabilities on Databricks
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance and lineage platform
- OpenTelemetry — Observability framework for distributed systems
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) — Declarative pipeline framework for data processing
- [Data Privacy and Compliance](/concepts/llm-judge-model-trust-and-data-privacy.md) — Regulatory requirements for PII handling
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Trace storage and management in MLflow

## Sources

- pii-redaction-from-otel-traces-reference-databricks-on-aws.md

# Citations

1. [pii-redaction-from-otel-traces-reference-databricks-on-aws.md](/references/pii-redaction-from-otel-traces-reference-databricks-on-aws-426a48ea.md)
