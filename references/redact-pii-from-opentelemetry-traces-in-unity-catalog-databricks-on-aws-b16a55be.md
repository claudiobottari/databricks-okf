---
title: Redact PII from OpenTelemetry traces in Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/redact-pii-otel-traces
ingestedAt: "2026-06-18T08:18:09.612Z"
---

OpenTelemetry (OTel) trace data often contains personally identifiable information (PII) such as email addresses, phone numbers, and credit card numbers embedded in span attributes, log bodies, and resource metadata. Sharing this trace data broadly for debugging or observability can create compliance and privacy risks.

This page describes an example solution that uses [AI Functions](https://docs.databricks.com/aws/en/large-language-models/ai-functions) and [Lakeflow Spark Declarative Pipelines](https://docs.databricks.com/aws/en/ldp/) to incrementally redact PII from raw OTel tables and write the results to a separate set of tables with broader access controls. A configurable retention job handles cleanup of the raw data. Deploy the downloadable assets into your own workspace and adapt them to your requirements.

You can use this solution with any OTel traces stored in Unity Catalog, including [Store OpenTelemetry traces in Unity Catalog](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/trace-unity-catalog).

## How it works[​](#how-it-works "Direct link to How it works")

![OTel PII redaction overview](https://docs.databricks.com/aws/en/assets/images/otel-pii-overview-13cec10c83d05a98830f1afc7a399c86.png)

A [Lakeflow Spark Declarative Pipelines](https://docs.databricks.com/aws/en/ldp/) pipeline incrementally reads new OTel spans, applies [`ai_mask`](https://docs.databricks.com/aws/en/sql/language-manual/functions/ai_mask) to redact PII (emails, phones, SSNs, credit cards, names, and addresses), and writes to the redacted tables. A scheduled job handles optional retention cleanup on the raw tables.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

*   A Unity Catalog\-enabled workspace.
*   [AI Functions](https://docs.databricks.com/aws/en/large-language-models/ai-functions) available through a serverless SQL warehouse or serverless pipeline.
*   The [Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/) authenticated to your workspace.
*   OTel trace data in Unity Catalog tables, written through MLflow, an OTel exporter, or any OTLP client. See [Store OpenTelemetry traces in Unity Catalog](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/trace-unity-catalog).

## Download the assets[​](#download-the-assets "Direct link to Download the assets")

Download the following files and import them into your workspace:

For more details, see the [reference documentation](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/redact-pii-otel-traces-reference).

## Deploy the solution[​](#deploy-the-solution "Direct link to Deploy the solution")

Select one of the following deployment methods.

*   Guided notebook (recommended)
*   CLI
*   Manual

For a step-by-step deployment directly in your workspace:

1.  Import [deploy\_notebook.py](https://docs.databricks.com/aws/en/assets/files/deploy_notebook-6d5bd510704301514d7e8cebc95fd5ed.py) into your workspace, along with the other downloaded assets. See [Databricks Git folders](https://docs.databricks.com/aws/en/repos/).
2.  Open `deploy_notebook.py` in your workspace.
3.  Fill in the widget parameters at the top (catalog, source schema, target schema, and table prefix).
4.  Click **Run all**. Each step validates before proceeding.

This approach uses the Databricks Python SDK (no CLI required), is safe to re-run, and provides interactive feedback at each step.

## Parameters[​](#parameters "Direct link to Parameters")

The following table describes the widget parameters in the guided deployment notebook (`deploy_notebook.py`):

Source tables are named `{catalog}.{source_schema}.{table_prefix}_otel_spans`, `{catalog}.{source_schema}.{table_prefix}_otel_logs`, and `{catalog}.{source_schema}.{table_prefix}_otel_annotations`.

The pipeline supports two execution modes:

*   **triggered**: Creates a scheduled job that triggers the pipeline on the chosen frequency. The pipeline processes new data on each run and then stops.
*   **continuous**: Runs the pipeline continuously, processing new data as it arrives. No scheduling job is created. This mode has higher compute costs than triggered mode because the pipeline is always running.

## What gets redacted[​](#what-gets-redacted "Direct link to What gets redacted")

The pipeline applies `ai_mask` to the following fields:

The pipeline preserves non-PII fields unchanged, such as trace IDs, span IDs, timestamps, service names, and status codes.

### Supported PII categories[​](#supported-pii-categories "Direct link to Supported PII categories")

`ai_mask` is LLM-backed and recognizes standard PII types, including `email`, `phone`, `name`, `address`, `ssn`, `credit_card`, `ip_address`, and `date_of_birth`.

`ai_mask` is recommended because it handles varied PII formats (for example, phone numbers written as `(555) 123-4567`, `555.123.4567`, or `+1 555-123-4567`) without requiring a separate pattern for each variation. You can adapt the pipeline to use a different redaction method, such as explicit regular expressions with [`regexp_replace`](https://docs.databricks.com/aws/en/sql/language-manual/functions/regexp_replace).

For custom patterns, such as employee IDs like `EMP-XXXXXX`, use `regexp_replace` before `ai_mask` in the pipeline SQL. For details, see [PII redaction from OTel traces reference](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/redact-pii-otel-traces-reference).

## Retention and access control[​](#retention-and-access-control "Direct link to Retention and access control")

### Raw data retention[​](#raw-data-retention "Direct link to Raw data retention")

The deployment configures [auto time-to-live](https://docs.databricks.com/aws/en/tables/operations/auto-ttl) on the raw OTel tables to automatically delete trace data older than a configurable number of days (default: 90). This helps you comply with GDPR and other data protection regulations that require personal data to be deleted after it is no longer needed for its original purpose. After the pipeline processes the raw spans, auto-TTL removes the originals that contain PII according to your retention policy. Set `retention_days` to `0` or `none` to disable automatic deletion if you manage retention separately. If your compliance requirements demand strict deletion timelines, you can set up a manual scheduled job with `DELETE` and `VACUUM` instead, as exact auto-TTL deletion timing is not guaranteed.

### Limit access to raw tables[​](#limit-access-to-raw-tables "Direct link to Limit access to raw tables")

The raw OTel tables contain unredacted PII and should have restricted access. Grant access to the raw source schema only to pipeline service principals and administrators who need it for debugging or incident response. All routine analytics, dashboards, and observability workflows should query the redacted tables instead. The `setup_schema_and_grants.sql` file includes example grants to help enforce this separation. For more information about Unity Catalog privileges, see [Manage privileges in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/).

## Test the redaction[​](#test-the-redaction "Direct link to Test the redaction")

### Send test PII data[​](#send-test-pii-data "Direct link to Send test PII data")

Generate test spans with known PII to validate redaction:

Bash

    pip install opentelemetry-exporter-otlp-proto-httppython send_pii_traces.py <WORKSPACE_HOST> <CATALOG.SCHEMA.PREFIX_otel_spans>

This sends 50 test traces that contain emails, phones, SSNs, credit cards, names, and addresses.

### Validate the output[​](#validate-the-output "Direct link to Validate the output")

After running the pipeline, compare the raw and redacted spans:

SQL

    SELECT  s.span_id,  CAST(s.attributes AS STRING) AS raw,  CAST(r.attributes AS STRING) AS redactedFROM <source_catalog>.<source_schema>.<prefix>_otel_spans sJOIN <target_catalog>.<target_schema>.redacted_spans r  ON s.trace_id = r.trace_id AND s.span_id = r.span_idWHERE s.name = 'pii-test-interaction'LIMIT 5;

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Store OpenTelemetry traces in Unity Catalog](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/trace-unity-catalog)
*   [Query OpenTelemetry traces stored in Unity Catalog](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/query-dbsql)
*   [Enrich data using AI Functions](https://docs.databricks.com/aws/en/large-language-models/ai-functions)
