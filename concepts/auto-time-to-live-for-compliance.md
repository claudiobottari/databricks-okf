---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ad606da83a1a08d15f6c94809c38fc69bb5303878139658e5f88862fb062e554
  pageDirectory: concepts
  sources:
    - pii-redaction-from-otel-traces-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - auto-time-to-live-for-compliance
    - ATFC
    - auto time-to-live
  citations:
    - file: pii-redaction-from-otel-traces-reference-databricks-on-aws.md
title: Auto Time-to-Live for Compliance
description: Automatic row deletion based on a time column in Unity Catalog managed Delta tables, used to enforce data retention policies without scheduled jobs.
tags:
  - data-retention
  - compliance
  - auto-ttl
  - unity-catalog
timestamp: "2026-06-19T19:56:20.952Z"
---

# Auto Time-to-Live for Compliance

**Auto Time-to-Live (Auto TTL)** is a Databricks feature for automatically deleting expired rows from [Unity Catalog](/concepts/unity-catalog.md) managed Delta Table|Delta tables based on a configured retention period. It is designed to support compliance requirements such as GDPR data retention policies by removing data after a specified number of days without requiring a scheduled maintenance job. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## How It Works

Auto TTL is configured using the `ALTER TABLE ... DELETE ROWS` SQL command on a table that has a `TIMESTAMP` column. The command specifies how many days after a row’s timestamp the row should be considered expired. Once set, Databricks automatically runs `DELETE`, `PURGE`, and `VACUUM` operations in the background on the table — no separate scheduled job is needed. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

### Example

```sql
ALTER TABLE ${source_catalog}.${source_schema}.${table_prefix}_otel_spans
  DELETE ROWS ${retention_days} DAYS AFTER time;
```

After this command, rows whose `time` column is older than `retention_days` days are automatically removed. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

### Prerequisite

Predictive Optimization must be enabled on the workspace (or on the specific table) for auto TTL to function. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## Deletion Timing and Compliance Guarantees

**Exact deletion timing is not guaranteed.** There can be a buffer of up to 6 days between row expiration and permanent deletion, plus the data retention duration (default 7 days) that Databricks uses for internal operations. If your compliance requirements demand strict deletion timelines (e.g., immediate removal upon expiry), you should use a scheduled job with manual `DELETE` and `VACUUM` commands as a fallback. See the Databricks documentation on auto time-to-live for details on calculating configuration values to achieve a target expiration period. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## Use Case in PII Redaction

In the reference architecture for redacting PII from OpenTelemetry traces, auto TTL is recommended on the raw OTel span and log tables to enforce a retention window (e.g., 30 days) for compliance purposes. After the raw data is redacted via a batch pipeline, the original data can be automatically purged using auto TTL. This supports GDPR compliance|GDPR and other data privacy regulations. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) that manages tables and permissions.
- [Delta Table](/concepts/delta-lake-table.md) – The underlying storage format for managed tables.
- Predictive Optimization – Required for auto TTL to work.
- Data Retention Policy – Broader concept of defining how long data is kept.
- GDPR – Common regulatory driver for data deletion automation.
- [PII Redaction](/concepts/ai-functions-for-pii-redaction.md) – The process of masking or removing personally identifiable information; auto TTL is used alongside it to manage raw data lifecycle.

## Sources

- pii-redaction-from-otel-traces-reference-databricks-on-aws.md

# Citations

1. [pii-redaction-from-otel-traces-reference-databricks-on-aws.md](/references/pii-redaction-from-otel-traces-reference-databricks-on-aws-426a48ea.md)
