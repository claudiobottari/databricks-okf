---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c8c12212f01ebd44ab29a12d29046292fb16e5db897fce36345326325aa2ae6e
  pageDirectory: concepts
  sources:
    - redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pii-redaction-pipeline-for-opentelemetry-traces
    - PRPFOT
    - PII Redaction from OpenTelemetry Traces
    - PII Redaction from OTel Traces
  citations:
    - file: redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md
title: PII Redaction Pipeline for OpenTelemetry Traces
description: An incremental pipeline pattern that uses AI Functions and Lakeflow Spark Declarative Pipelines to redact personally identifiable information from OpenTelemetry trace data stored in Unity Catalog, writing sanitized results to separate tables with broader access controls.
tags:
  - data-privacy
  - observability
  - databricks
  - pipeline
timestamp: "2026-06-19T20:12:35.435Z"
---

# PII Redaction Pipeline for OpenTelemetry Traces

**PII Redaction Pipeline for OpenTelemetry Traces** is a Databricks solution that uses [AI Functions](/concepts/ai-functions.md) and [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) to automatically remove personally identifiable information (PII) from OpenTelemetry (OTel) trace data stored in [Unity Catalog](/concepts/unity-catalog.md). The pipeline incrementally reads raw OTel spans, applies the `ai_mask` function to redact sensitive fields, and writes the sanitized results to separate tables with broader access controls. A configurable retention job handles cleanup of the raw data.^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Motivation

OpenTelemetry trace data often contains PII such as email addresses, phone numbers, and credit card numbers embedded in span attributes, log bodies, and resource metadata. Sharing this trace data broadly for debugging or observability can create compliance and privacy risks. This pipeline addresses those risks by separating raw (PII-containing) data from redacted data, and by enforcing retention policies on the raw tables.^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## How It Works

A [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) pipeline incrementally reads new OTel spans, applies [`ai_mask`](https://docs.databricks.com/aws/en/sql/language-manual/functions/ai_mask) to redact PII, and writes to the redacted tables. A scheduled job handles optional retention cleanup on the raw tables. The pipeline supports two execution modes:

- **triggered**: Creates a scheduled job that triggers the pipeline on a chosen frequency. The pipeline processes new data on each run and then stops.
- **continuous**: Runs the pipeline continuously, processing new data as it arrives. No scheduling job is created. This mode has higher compute costs than triggered mode because the pipeline is always running.

^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Prerequisites

- A Unity Catalog-enabled workspace.
- [AI Functions](/concepts/ai-functions.md) available through a serverless SQL warehouse or serverless pipeline.
- The Databricks CLI authenticated to your workspace.
- OTel trace data in Unity Catalog tables, written through MLflow, an OTel exporter, or any OTLP client. See [Store OpenTelemetry traces in Unity Catalog](/concepts/opentelemetry-traces-in-unity-catalog.md).

^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## What Gets Redacted

The pipeline applies `ai_mask` to the following fields:

- `attributes`
- `body`
- `resource`

The pipeline preserves non-PII fields unchanged, such as trace IDs, span IDs, timestamps, service names, and status codes.^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

### Supported PII Categories

`ai_mask` is LLM-backed and recognizes standard PII types, including:

- `email`
- `phone`
- `name`
- `address`
- `ssn`
- `credit_card`
- `ip_address`
- `date_of_birth`

`ai_mask` is recommended because it handles varied PII formats (for example, phone numbers written as `(555) 123-4567`, `555.123.4567`, or `+1 555-123-4567`) without requiring a separate pattern for each variation. You can adapt the pipeline to use a different redaction method, such as explicit regular expressions with `regexp_replace`. For custom patterns, such as employee IDs like `EMP-XXXXXX`, use `regexp_replace` before `ai_mask` in the pipeline SQL.^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Deployment

Download the following assets and import them into your workspace:

- `deploy_notebook.py` (guided deployment notebook, recommended)
- Pipeline SQL files
- `setup_schema_and_grants.sql`
- `send_pii_traces.py` (for testing)

Three deployment methods are available:

1. **Guided notebook (recommended)**: Import `deploy_notebook.py` and run it interactively. Each step validates before proceeding. This approach uses the Databricks Python SDK (no CLI required), is safe to re-run, and provides interactive feedback.
2. **CLI**: Use the Databricks CLI to deploy the assets.
3. **Manual**: Configure each component individually.

^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Parameters

The guided deployment notebook (`deploy_notebook.py`) accepts the following widget parameters:

| Parameter | Description |
|-----------|-------------|
| **Source catalog** | The Unity Catalog catalog that contains the source OTel tables. |
| **Source schema** | The Unity Catalog schema that contains the source OTel tables. |
| **Target catalog** | The Unity Catalog catalog where redacted tables are written. |
| **Target schema** | The Unity Catalog schema where redacted tables are written. |
| **Table prefix** | A prefix used to name the source OTel tables. Source tables are named `{catalog}.{source_schema}.{table_prefix}_otel_spans`, `{catalog}.{source_schema}.{table_prefix}_otel_logs`, and `{catalog}.{source_schema}.{table_prefix}_otel_annotations`. |
| **Pipeline mode** | `triggered` or `continuous` (see above). |
| **Retention days** | Number of days to retain raw data (default: 90). |

^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Retention and Access Control

### Raw Data Retention

The deployment configures [auto time-to-live](/concepts/auto-time-to-live-for-compliance.md) (auto-TTL) on the raw OTel tables to automatically delete trace data older than a configurable number of days (default: 90). This helps comply with GDPR and other data protection regulations that require personal data to be deleted after it is no longer needed for its original purpose. After the pipeline processes the raw spans, auto-TTL removes the originals that contain PII according to your retention policy. Set `retention_days` to `0` or `none` to disable automatic deletion if you manage retention separately. If your compliance requirements demand strict deletion timelines, you can set up a manual scheduled job with `DELETE` and `VACUUM` instead, as exact auto-TTL deletion timing is not guaranteed.^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

### Limiting Access to Raw Tables

The raw OTel tables contain unredacted PII and should have restricted access. Grant access to the raw source schema only to pipeline service principals and administrators who need it for debugging or incident response. All routine analytics, dashboards, and observability workflows should query the redacted tables instead. The `setup_schema_and_grants.sql` file includes example grants to help enforce this separation. For more information about Unity Catalog privileges, see Manage privileges in Unity Catalog.^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Testing

### Send Test PII Data

Generate test spans with known PII to validate redaction:

```bash
pip install opentelemetry-exporter-otlp-proto-http
python send_pii_traces.py <WORKSPACE_HOST> <CATALOG.SCHEMA.PREFIX_otel_spans>
```

This sends 50 test traces that contain emails, phones, SSNs, credit cards, names, and addresses.^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

### Validate the Output

After running the pipeline, compare the raw and redacted spans:

```sql
SELECT
  s.span_id,
  CAST(s.attributes AS STRING) AS raw,
  CAST(r.attributes AS STRING) AS redacted
FROM <source_catalog>.<source_schema>.<prefix>_otel_spans s
JOIN <target_catalog>.<target_schema>.redacted_spans r
  ON s.trace_id = r.trace_id AND s.span_id = r.span_id
WHERE s.name = 'pii-test-interaction'
LIMIT 5;
```

^[redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- OpenTelemetry Tracing on Databricks
- [AI Functions](/concepts/ai-functions.md)
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Store OpenTelemetry traces in Unity Catalog](/concepts/opentelemetry-traces-in-unity-catalog.md)
- Query OpenTelemetry traces stored in Unity Catalog
- Enrich data using AI Functions

## Sources

- redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md

# Citations

1. [redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws.md](/references/redact-pii-from-opentelemetry-traces-in-unity-catalog-databricks-on-aws-b16a55be.md)
