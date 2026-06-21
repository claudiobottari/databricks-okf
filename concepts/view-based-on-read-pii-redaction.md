---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c811b1d93811ecb8516a7f8e1c798e45cd7f6a8d2913bc7c0096307809a39be5
  pageDirectory: concepts
  sources:
    - pii-redaction-from-otel-traces-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - view-based-on-read-pii-redaction
    - VOPR
    - View-based on-read redaction
  citations:
    - file: pii-redaction-from-otel-traces-reference-databricks-on-aws.md
title: View-based On-Read PII Redaction
description: Alternative approach that applies ai_mask in a Unity Catalog view to redact PII at query time without duplicating storage.
tags:
  - views
  - on-read
  - unity-catalog
  - redaction
timestamp: "2026-06-19T19:55:51.528Z"
---

## View-based On-Read PII Redaction

**View-based On-Read PII Redaction** is a pattern for redacting personally identifiable information (PII) from [OpenTelemetry] (OTel) traces stored in [Unity Catalog] without duplicating data. Redaction is applied at query time by defining a [Unity Catalog] view that uses [`ai_mask`] – an AI function – to mask PII fields on the fly. Because no redacted copy is persisted, this approach avoids storage costs but incurs compute cost on every query. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

### When to use

The view‑based approach is recommended when:

- **Storage cost** is a primary concern – no additional tables are created.
- **Redacted data is queried infrequently** – each query pays the redaction compute cost, so it is only economical when reads are sporadic.
- **The compute cost per query is acceptable** – every SELECT triggers `ai_mask` calls, which consume foundation‑model endpoint throughput. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

### Architecture

In this pattern, the raw OTel span table remains unchanged in Unity Catalog. A view is created on top of it that transforms PII‑sensitive columns (attributes, events, resource attributes) using `ai_mask`. Users query the view instead of the raw table, and redaction happens transparently at read time. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

![OTel PII redaction view architecture](https://docs.databricks.com/aws/en/assets/images/otel-pii-redaction-view-685df4102ffde29c018f7db71c30c55e.png)

### Implementation

The view is created with a single SQL statement that wraps `ai_mask` over the columns that may contain PII.

```sql
CREATE OR REPLACE VIEW ${target_catalog}.${target_schema}.${table_prefix}_otel_spans_redacted AS
SELECT
  trace_id,
  span_id,
  parent_span_id,
  name,
  kind,
  start_time,
  end_time,
  status,
  date,
  service_name,
  time,
  instrumentation_scope,
  links,
  ai_mask(
    CAST(attributes AS STRING),
    array(${pii_categories})
  ) AS attributes,
  ai_mask(
    CAST(events AS STRING),
    array(${pii_categories})
  ) AS events,
  named_struct(
    'attributes',
    ai_mask(CAST(resource:attributes AS STRING), array(${pii_categories})),
    'dropped_attributes_count',
    resource:dropped_attributes_count
  ) AS resource
FROM ${source_catalog}.${source_schema}.${table_prefix}_otel_spans;
```

^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

The `${pii_categories}` parameter accepts an array of PII types (e.g., `'email','phone','ssn','credit_card','name','address'`) which `ai_mask` uses to determine what to redact. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

### Trade-offs

The source documentation lists the following trade-offs for the view‑based flow compared to the server‑side batch pipeline:

| Aspect | Trade‑off |
|--------|-----------|
| **Data duplication** | None – no redacted copy is stored. |
| **Query cost** | Higher – `ai_mask` runs on every query, consuming compute and foundation‑model endpoint throughput. |
| **Query performance** | Slower – redaction is applied inline during query execution. |
| **Historical debugging** | Limited – the raw table may still contain PII, but the view always redacts; no materialized snapshot exists for debugging. |
| **Automation** | Minimal – no pipeline to manage; the view is a single SQL object. |
| **Compliance** | Relies on access controls to restrict querying the raw table (if that table is not locked down, PII remains accessible). |

^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

### Comparison with the server‑side batch pipeline

The view‑based approach is one of two complementary flows described in the reference architecture. The other (recommended) flow, **Server-side Batch PII Redaction**, materializes redacted tables using a [Lakeflow Spark Declarative Pipeline] and retains full‑fidelity data for debugging. The table below summarises the key differences:

| Feature | View‑based (on‑read) | Server‑side batch |
|---------|----------------------|-------------------|
| Storage cost | No additional cost | Additional storage for redacted tables |
| Query performance | Slower (call `ai_mask` on every read) | Fast (pre‑computed) |
| Data fidelity | No persistent redacted copy | Persistent redacted copy available for debugging |
| Operational overhead | Low (one SQL view) | Higher (pipeline management, scheduling) |
| Recommended use case | Low‑query‑volume, cost‑sensitive | Primary enterprise deployment |

^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

The source explicitly recommends using the batch pipeline as the primary solution and the view‑based approach as a lightweight option for low‑query‑volume scenarios or as an interim solution while setting up the batch pipeline. ^[pii-redaction-from-otel-traces-reference-databricks-on-aws.md]

### Related concepts

- [AI Functions](/concepts/ai-functions.md) – The `ai_mask` function used for PII detection and masking.
- OpenTelemetry – The observability framework that produces the trace data.
- [Unity Catalog](/concepts/unity-catalog.md) – The metadata catalog where tables and views are stored.
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) – The engine used in the server‑side batch alternative.
- Server-side Batch PII Redaction – The complementary batch processing flow.
- [Foundation Model Endpoint](/concepts/foundation-model-serving-endpoints.md) – Required to serve `ai_mask` calls.
- Data Retention and auto-TTL – Policy for deleting raw trace data after a retention period (applies to the batch flow but not to the view).

### Sources

- pii-redaction-from-otel-traces-reference-databricks-on-aws.md

# Citations

1. [pii-redaction-from-otel-traces-reference-databricks-on-aws.md](/references/pii-redaction-from-otel-traces-reference-databricks-on-aws-426a48ea.md)
