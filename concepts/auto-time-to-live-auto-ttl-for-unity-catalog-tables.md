---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4e1601a96c67ba6a7f3e2d978fde695443a2be61b73fb586dca62de96a0fb3b
  pageDirectory: concepts
  sources:
    - redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - auto-time-to-live-auto-ttl-for-unity-catalog-tables
    - AT(FUCT
    - Auto time-to-live (auto-TTL)
  citations:
    - file: redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md
title: Auto Time-to-Live (Auto-TTL) for Unity Catalog Tables
description: A configurable automatic retention mechanism in Databricks Unity Catalog that deletes trace data older than a specified number of days, helping comply with GDPR and other data protection regulations.
tags:
  - data-governance
  - databricks
  - compliance
  - unity-catalog
timestamp: "2026-06-19T20:12:15.380Z"
---

# Auto Time-to-Live (Auto-TTL) for Unity Catalog Tables

**Auto Time-to-Live (Auto-TTL)** is a data retention feature for Unity Catalog tables that automatically deletes rows older than a configurable number of days. It is primarily used to manage data lifecycle and comply with data protection regulations such as GDPR, which require personal data to be deleted after it is no longer needed for its original purpose. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Overview

Auto-TTL is configured on a per-table basis and operates by automatically removing rows whose timestamps fall outside the specified retention window. The feature is commonly applied to raw data tables that contain sensitive information, such as OpenTelemetry trace data with Personally Identifiable Information (PII). After a downstream pipeline processes and redacts the sensitive data, Auto-TTL removes the original raw records according to the configured retention policy. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Configuration

To enable Auto-TTL on a Unity Catalog table, set the `retention_days` parameter to the desired number of days. The system will then automatically delete rows that are older than this threshold. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

### Disabling Auto-TTL

Set `retention_days` to `0` or `none` to disable automatic deletion. This is useful when you manage retention separately through other mechanisms, such as manual scheduled jobs. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Limitations

Exact auto-TTL deletion timing is not guaranteed. If your compliance requirements demand strict deletion timelines, you should set up a manual scheduled job using `DELETE` and `VACUUM` statements instead of relying solely on Auto-TTL. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Use Cases

### PII Redaction Pipeline

A common use case for Auto-TTL is in [PII Redaction from OpenTelemetry Traces](/concepts/pii-redaction-pipeline-for-opentelemetry-traces.md) pipelines. In this scenario:

1. Raw OTel trace data containing PII is ingested into Unity Catalog tables.
2. A [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) pipeline incrementally reads new spans, applies [AI Functions](/concepts/ai-functions.md) like `ai_mask` to redact PII, and writes the redacted results to separate tables.
3. Auto-TTL on the raw tables automatically deletes the original PII-containing data after a configurable retention period (default: 90 days). ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

### GDPR Compliance

Auto-TTL helps organizations comply with data protection regulations that require personal data to be deleted after it is no longer needed for its original purpose. By automatically removing raw data after processing, organizations can reduce their data footprint and associated compliance risks. ^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform that hosts tables with Auto-TTL.
- Data Retention Policies — Broader strategies for managing data lifecycle.
- [PII Redaction from OpenTelemetry Traces](/concepts/pii-redaction-pipeline-for-opentelemetry-traces.md) — A solution that uses Auto-TTL for raw data cleanup.
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) — The pipeline framework used to process data before Auto-TTL cleanup.
- [AI Functions](/concepts/ai-functions.md) — Functions like `ai_mask` used to redact sensitive data before retention policies apply.
- [DELETE and VACUUM](/concepts/vacuum-and-file-visibility-in-delta-lake.md) — Manual alternatives for strict deletion timing requirements.

## Sources

- redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md

# Citations

1. [redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md](/references/redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws-b16a55be.md)
