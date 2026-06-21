---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 58cebed147b71bbbd265e38d489ab789a299de880deab32d7020f4aaf18d10f1
  pageDirectory: concepts
  sources:
    - pii-redaction-from-otel-traces-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-unified-view-pattern
    - TUVP
  citations:
    - file: pii-redaction-from-otel-traces-reference-databricks-on-aws.md
title: Trace Unified View Pattern
description: A join pattern that aggregates OTel spans, annotations, and tags into a single denormalized trace record, enabling unified querying across redacted trace data.
tags:
  - tracing
  - views
  - unified-schema
  - observability
timestamp: "2026-06-19T19:56:10.138Z"
---

Here is the wiki page for "Trace Unified View Pattern".

---

## Trace Unified View Pattern

The **Trace Unified View Pattern** is a reference architecture for exposing redacted OpenTelemetry (OTel) trace data to downstream consumers through a single, denormalized view. It is part of a broader solution for [PII Redaction from OTel Traces](/concepts/pii-redaction-pipeline-for-opentelemetry-traces.md) on Databricks. The pattern is defined in the `trace_unified` view, which joins redacted span data with annotation data (tags and assessments) to provide a complete picture of each trace for querying and monitoring. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## Overview

The view is created by a `CREATE OR REPLACE VIEW` statement that materializes the join between redacted spans and annotations. It is designed to be the primary interface for non-administrative users needing access to trace data. In the batch processing flow (Flow 1), the view is created against the redacted streaming tables produced by the PII redaction pipeline. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## View Definition

The view assembles each trace by grouping spans by `trace_id` and `date`, and joining on the corresponding annotations. Spans are collected into an ordered list using `collect_list` with a `named_struct` that preserves key span fields. This provides a single row per trace with all associated spans, annotations, and computed metrics. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

```sql
CREATE OR REPLACE VIEW ${target_catalog}.${target_schema}.${table_prefix}_trace_unified AS
SELECT
  s.trace_id,
  s.date,
  min(s.start_time) AS request_time,
  max(s.end_time) - min(s.start_time) AS execution_duration,
  collect_list(
    named_struct(
      'span_id', s.span_id,
      'parent_span_id', s.parent_span_id,
      'name', s.name,
      'kind', s.kind,
      'start_time', s.start_time,
      'end_time', s.end_time,
      'status', s.status,
      'attributes', s.attributes,
      'events', s.events
    )
  ) AS spans,
  a.tags,
  a.assessments
FROM ${target_catalog}.${target_schema}.redacted_spans s
LEFT JOIN ${target_catalog}.${target_schema}.redacted_annotations a
  ON s.trace_id = a.target_id
GROUP BY s.trace_id, s.date, a.tags, a.assessments;
```

^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## Key Computed Fields

- **request_time**: The earliest `start_time` across all spans in a trace, representing the overall request start time. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]
- **execution_duration**: The difference between the latest end time and the earliest start time across all spans, representing the total trace duration. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]
- **spans**: A collected list of structured span objects, each containing span metadata and PII-redacted attributes and events. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## Role in the PII Redaction Architecture

The Trace Unified View Pattern is the final output component of the server-side batch processing flow (Flow 1). It is created after the PII redaction pipeline materializes the `redacted_spans`, `redacted_logs`, and `redacted_annotations` tables. Broader access (e.g., to a `data_team` group) is then granted to the target schema containing this view, rather than to the raw source tables. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

### Data Flow

1. Raw OTel span, log, and annotation tables are ingested into Unity Catalog.
2. A declarative pipeline reads the raw tables and produces redacted streaming tables using `ai_mask` for PII redaction.
3. The `trace_unified` view is created on top of the redacted tables, joining spans and annotations.
4. End users query the view instead of the raw tables. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

## Related Concepts

- [PII Redaction from OTel Traces](/concepts/pii-redaction-pipeline-for-opentelemetry-traces.md) — The broader reference solution that includes the Trace Unified View.
- OpenTelemetry (OTel) Spans — The core data structure collected and redacted.
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer where raw, redacted, and view tables reside.
- [AI Functions](/concepts/ai-functions.md) (specifically `ai_mask`) — Used to redact PII from free-text span and log fields.
- [Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) — The mechanism for materializing redacted tables incrementally.
- Auto Time-to-Live (Auto TTL) — Used to manage retention of raw trace data.

## Sources

- pii-redaction-from-otel-traces-reference-databricks-on-aws.md

# Citations

1. [pii-redaction-from-otel-traces-reference-databricks-on-aws.md](/references/pii-redaction-from-otel-traces-reference-databricks-on-aws-426a48ea.md)
