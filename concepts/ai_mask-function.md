---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1d2f72d8aeaff679ca3ac1a408a9c6e6a7ab3a3a7968ae2669f78eeb2e316ee5
  pageDirectory: concepts
  sources:
    - redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai_mask-function
    - ai_mask Function
    - Masking function
  citations:
    - file: redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md
title: ai_mask Function
description: An LLM-backed SQL function in Databricks that detects and masks standard PII types (email, phone, name, address, SSN, credit card, IP address, date of birth) across varied formats without requiring separate regex patterns.
tags:
  - data-privacy
  - sql
  - llm
  - databricks
timestamp: "2026-06-19T20:12:26.905Z"
---

# ai_mask Function

The **`ai_mask` function** is a Databricks AI Function that uses a large language model (LLM) to identify and redact personally identifiable information (PII) from text data. It is designed to handle varied PII formats without requiring explicit pattern matching for each variation. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Overview

`ai_mask` is an LLM-backed function that detects and masks standard PII categories in text, including email addresses, phone numbers, Social Security numbers, credit card numbers, names, physical addresses, IP addresses, and dates of birth. The function recognizes common format variations — for example, phone numbers written as `(555) 123-4567`, `555.123.4567`, or `+1 555-123-4567` — without requiring a separate pattern for each variation. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Availability

`ai_mask` is available through a Serverless SQL Warehouse or a serverless pipeline. It requires a Unity Catalog-enabled workspace with [AI Functions](/concepts/ai-functions.md) enabled. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Supported PII Categories

The function recognizes the following PII types by default:

- `email`
- `phone`
- `name`
- `address`
- `ssn` (Social Security Number)
- `credit_card`
- `ip_address`
- `date_of_birth`

^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Use Cases

### PII Redaction from OpenTelemetry Traces

A common use case for `ai_mask` is redacting PII from OpenTelemetry trace data stored in [Unity Catalog](/concepts/unity-catalog.md). OpenTelemetry trace data often contains PII such as email addresses, phone numbers, and credit card numbers embedded in span attributes, log bodies, and resource metadata. The function can be applied to the relevant fields in OTel span tables to produce a redacted copy suitable for broader sharing across analytics, dashboards, and observability workflows. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

### Combining with Regex for Custom Patterns

For PII types that match custom patterns — such as employee IDs following the format `EMP-XXXXXX` — `ai_mask` can be combined with the regexp_replace function. The recommended approach is to apply `regexp_replace` before `ai_mask` in the pipeline SQL to handle custom patterns first, then let the LLM-based function handle standard PII categories. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Alternatives

While `ai_mask` is the recommended approach for PII redaction in this context, users can alternatively use explicit regular expressions with `regexp_replace` for each PII category. The `ai_mask` approach is preferred because it eliminates the need to maintain separate patterns for every format variation. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [AI Functions](/concepts/ai-functions.md) — The family of LLM-backed functions in Databricks SQL, including `ai_mask`
- Serverless SQL Warehouse — Required compute infrastructure for using AI Functions
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer where raw and redacted tables are managed
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) — Pipeline framework for incrementally processing data with `ai_mask`
- [PII Redaction](/concepts/ai-functions-for-pii-redaction.md) — The broader practice of removing personally identifiable information from data
- Data Governance — Policies and procedures for managing sensitive data access
- OpenTelemetry — Observability framework for traces and spans

## Sources

- redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md

# Citations

1. [redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md](/references/redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws-b16a55be.md)
