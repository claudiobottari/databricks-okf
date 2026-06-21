---
title: PII redaction from OTel traces reference | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/redact-pii-otel-traces-reference
ingestedAt: "2026-06-18T08:18:12.100Z"
---

This page describes a reference architecture for redacting PII from OpenTelemetry (OTel) spans stored in Unity Catalog. It covers two complementary flows: server-side batch processing and view-based on-read redaction. Both flows use [AI Functions](https://docs.databricks.com/aws/en/large-language-models/ai-functions) and [Lakeflow Spark Declarative Pipelines](https://docs.databricks.com/aws/en/ldp/). For deployment instructions and downloadable assets, see [Redact PII from OpenTelemetry traces in Unity Catalog](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/redact-pii-otel-traces).

## Parameters[​](#parameters "Direct link to Parameters")

All components in this solution are parameterized for reuse across environments.

### Table parameters[​](#table-parameters "Direct link to Table parameters")

Derived source table names:

*   `{source_catalog}.{source_schema}.{table_prefix}_otel_spans`
*   `{source_catalog}.{source_schema}.{table_prefix}_otel_logs`
*   `{source_catalog}.{source_schema}.{table_prefix}_otel_annotations`

### PII redaction rules[​](#pii-redaction-rules "Direct link to PII redaction rules")

## Flow 1: Server-side batch processing (recommended)[​](#flow-1-server-side-batch-processing-recommended "Direct link to Flow 1: Server-side batch processing (recommended)")

This flow uses [Lakeflow Spark Declarative Pipelines](https://docs.databricks.com/aws/en/ldp/) to materialize redacted tables from the raw OTel tables.

### Why use a declarative pipeline[​](#why-use-a-declarative-pipeline "Direct link to Why use a declarative pipeline")

Lakeflow Spark Declarative Pipelines with streaming tables is the best fit. OTel spans are append-only, making them ideal for incremental streaming table ingestion. AI functions such as `ai_mask` are built-in in SQL, so a SQL pipeline is the simplest implementation.

### Architecture[​](#architecture "Direct link to Architecture")

![OTel PII redaction architecture](https://docs.databricks.com/aws/en/assets/images/otel-pii-redaction-arch-82ef68b664018915f5cccd1b607f277f.png)

### Implementation[​](#implementation "Direct link to Implementation")

#### Step 1: Lock down the raw tables[​](#step-1-lock-down-the-raw-tables "Direct link to Step 1: Lock down the raw tables")

Grant access to the raw tables only to the pipeline service principal and administrator users.

SQL

    -- Restrict raw table accessGRANT USE CATALOG ON CATALOG ${source_catalog} TO `pii_pipeline_sp`;GRANT USE SCHEMA ON SCHEMA ${source_catalog}.${source_schema} TO `pii_pipeline_sp`;GRANT SELECT ON TABLE ${source_catalog}.${source_schema}.${table_prefix}_otel_spans TO `pii_pipeline_sp`;GRANT SELECT ON TABLE ${source_catalog}.${source_schema}.${table_prefix}_otel_logs TO `pii_pipeline_sp`;-- Revoke broader accessREVOKE SELECT ON TABLE ${source_catalog}.${source_schema}.${table_prefix}_otel_spans FROM `data_team`;

#### Step 2: Create the pipeline SQL[​](#step-2-create-the-pipeline-sql "Direct link to Step 2: Create the pipeline SQL")

Define the redacted streaming tables in `pii_redaction_pipeline.sql`.

SQL

    -- =============================================================-- Streaming Table: Redacted Spans-- =============================================================CREATE OR REFRESH STREAMING TABLE redacted_spansCOMMENT 'PII-redacted OTel spans'TBLPROPERTIES (  'quality' = 'gold',  'pipelines.autoOptimize.zOrderCols' = 'trace_id,date')ASSELECT  trace_id,  span_id,  parent_span_id,  name,  kind,  start_time,  end_time,  status,  date,  record_id,  service_name,  time,  instrumentation_scope,  -- Redact span attributes (VARIANT field)  -- ai_mask replaces PII with masked values in free-text content  CASE    WHEN attributes IS NOT NULL THEN      ai_mask(        CAST(attributes AS STRING),        array(${pii_categories})  -- e.g. array('email','phone','ssn','name','address')      )    ELSE attributes  END AS attributes,  -- Redact resource attributes  CASE    WHEN resource:attributes IS NOT NULL THEN      named_struct(        'attributes',        ai_mask(          CAST(resource:attributes AS STRING),          array(${pii_categories})        ),        'dropped_attributes_count',        resource:dropped_attributes_count      )    ELSE resource  END AS resource,  -- Redact events (may contain exception messages with PII)  CASE    WHEN events IS NOT NULL THEN      ai_mask(        CAST(events AS STRING),        array(${pii_categories})      )    ELSE events  END AS events,  -- Pass through links unchanged (typically just trace/span IDs)  linksFROM STREAM(${source_catalog}.${source_schema}.${table_prefix}_otel_spans);-- =============================================================-- Streaming Table: Redacted Logs-- =============================================================CREATE OR REFRESH STREAMING TABLE redacted_logsCOMMENT 'PII-redacted OTel logs'ASSELECT  trace_id,  span_id,  severity_number,  severity_text,  date,  record_id,  service_name,  time,  instrumentation_scope,  -- Redact log body  CASE    WHEN body IS NOT NULL THEN      ai_mask(        CAST(body AS STRING),        array(${pii_categories})      )    ELSE body  END AS body,  -- Redact log attributes  CASE    WHEN attributes IS NOT NULL THEN      ai_mask(        CAST(attributes AS STRING),        array(${pii_categories})      )    ELSE attributes  END AS attributes,  -- Redact resource attributes  CASE    WHEN resource:attributes IS NOT NULL THEN      named_struct(        'attributes',        ai_mask(          CAST(resource:attributes AS STRING),          array(${pii_categories})        ),        'dropped_attributes_count',        resource:dropped_attributes_count      )    ELSE resource  END AS resourceFROM STREAM(${source_catalog}.${source_schema}.${table_prefix}_otel_logs);-- =============================================================-- Streaming Table: Annotations (passthrough — no PII expected)-- =============================================================CREATE OR REFRESH STREAMING TABLE redacted_annotationsCOMMENT 'OTel annotations (passthrough, no PII redaction applied)'ASSELECT *FROM STREAM(${source_catalog}.${source_schema}.${table_prefix}_otel_annotations);

#### Step 3: Create the pipeline resource[​](#step-3-create-the-pipeline-resource "Direct link to Step 3: Create the pipeline resource")

Use the following configuration as a template.

JSON

    {  "name": "otel-pii-redaction",  "catalog": "${target_catalog}",  "schema": "${target_schema}",  "serverless": true,  "continuous": false,  "channel": "CURRENT",  "configuration": {    "source_catalog": "<value>",    "source_schema": "<value>",    "table_prefix": "<value>",    "pii_categories": "'email','phone','ssn','credit_card','name','address'"  },  "libraries": [{ "file": { "path": "/Workspace/path/to/pii_redaction_pipeline.sql" } }]}

Run the pipeline in triggered mode (for example, every 15 minutes or hourly) depending on your latency requirements. Continuous mode is also an option, but it increases cost.

#### Step 4: Create the unified view on the redacted tables[​](#step-4-create-the-unified-view-on-the-redacted-tables "Direct link to Step 4: Create the unified view on the redacted tables")

SQL

    -- Recreate the trace_unified view pointing at redacted tablesCREATE OR REPLACE VIEW ${target_catalog}.${target_schema}.${table_prefix}_trace_unified ASSELECT  s.trace_id,  s.date,  min(s.start_time) AS request_time,  max(s.end_time) - min(s.start_time) AS execution_duration,  collect_list(    named_struct(      'span_id', s.span_id,      'parent_span_id', s.parent_span_id,      'name', s.name,      'kind', s.kind,      'start_time', s.start_time,      'end_time', s.end_time,      'status', s.status,      'attributes', s.attributes,      'events', s.events    )  ) AS spans,  a.tags,  a.assessmentsFROM ${target_catalog}.${target_schema}.redacted_spans sLEFT JOIN ${target_catalog}.${target_schema}.redacted_annotations a  ON s.trace_id = a.target_idGROUP BY s.trace_id, s.date, a.tags, a.assessments;

#### Step 5: Grant broader access to the redacted tables[​](#step-5-grant-broader-access-to-the-redacted-tables "Direct link to Step 5: Grant broader access to the redacted tables")

SQL

    GRANT USE CATALOG ON CATALOG ${target_catalog} TO `data_team`;GRANT USE SCHEMA ON SCHEMA ${target_catalog}.${target_schema} TO `data_team`;GRANT SELECT ON SCHEMA ${target_catalog}.${target_schema} TO `data_team`;

If `retention_days` is configured (greater than `0`), use [auto time-to-live](https://docs.databricks.com/aws/en/tables/operations/auto-ttl) to automatically delete expired rows. The OTel trace tables are Unity Catalog managed Delta tables with `time TIMESTAMP` columns, so auto-TTL is supported. [Predictive optimization](https://docs.databricks.com/aws/en/optimizations/predictive-optimization) must be enabled on the workspace (or table).

SQL

    ALTER TABLE ${source_catalog}.${source_schema}.${table_prefix}_otel_spans  DELETE ROWS ${retention_days} DAYS AFTER time;ALTER TABLE ${source_catalog}.${source_schema}.${table_prefix}_otel_logs  DELETE ROWS ${retention_days} DAYS AFTER time;

Databricks runs `DELETE`, `PURGE`, and `VACUUM` operations in the background automatically — no scheduled job is required.

note

Exact deletion timing is not guaranteed. There can be a buffer of up to 6 days between row expiration and permanent deletion, plus the data retention duration (default 7 days). If your compliance requirements demand strict deletion timelines, use a scheduled job with manual `DELETE` and `VACUUM` as a fallback. See [auto time-to-live](https://docs.databricks.com/aws/en/tables/operations/auto-ttl) for details on calculating configuration values for a target expiration period.

## Flow 2: View-based redaction (no data duplication)[​](#flow-2-view-based-redaction-no-data-duplication "Direct link to Flow 2: View-based redaction (no data duplication)")

This flow applies `ai_mask` in a Unity Catalog view, so redaction happens at read time and no redacted copy is stored.

### When to use[​](#when-to-use "Direct link to When to use")

*   Storage cost is a primary concern.
*   Redacted data is queried infrequently.
*   It is acceptable to pay the compute cost on every query.

### Architecture[​](#architecture-1 "Direct link to Architecture")

![OTel PII redaction architecture](https://docs.databricks.com/aws/en/assets/images/otel-pii-redaction-view-685df4102ffde29c018f7db71c30c55e.png)

### Implementation[​](#implementation-1 "Direct link to Implementation")

SQL

    CREATE OR REPLACE VIEW ${target_catalog}.${target_schema}.${table_prefix}_otel_spans_redactedASSELECT  trace_id,  span_id,  parent_span_id,  name,  kind,  start_time,  end_time,  status,  date,  service_name,  time,  instrumentation_scope,  links,  ai_mask(    CAST(attributes AS STRING),    array(${pii_categories})  ) AS attributes,  ai_mask(    CAST(events AS STRING),    array(${pii_categories})  ) AS events,  named_struct(    'attributes',    ai_mask(CAST(resource:attributes AS STRING), array(${pii_categories})),    'dropped_attributes_count',    resource:dropped_attributes_count  ) AS resourceFROM ${source_catalog}.${source_schema}.${table_prefix}_otel_spans;

### Trade-offs[​](#trade-offs "Direct link to Trade-offs")

## Flow comparison[​](#flow-comparison "Direct link to Flow comparison")

## Recommended approach[​](#recommended-approach "Direct link to Recommended approach")

Use **Flow 1 (batch pipeline)** as the primary solution for most enterprise deployments:

*   Preserves full-fidelity data for authorized debugging.
*   Optimizes query performance through materialization.
*   Supports GDPR compliance with auto-TTL retention on raw data.
*   Handles both PII redaction and trace filtering in one pipeline.
*   Is fully managed with built-in monitoring and alerting.

Use **Flow 2 (view-based)** as a lightweight option for low-query-volume scenarios, or as a quick interim solution while you set up Flow 1.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

*   **AI Functions enabled** — requires a SQL warehouse or serverless compute with AI Functions access.
*   **Unity Catalog** — OTel traces must be stored in Unity Catalog tables with MLflow trace-to-Unity Catalog binding configured. See [Store OpenTelemetry traces in Unity Catalog](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/trace-unity-catalog).
*   **Service principal** — for pipeline execution, with appropriate grants on the source tables.
*   **Foundation model endpoint** — `ai_mask` uses a foundation model. Verify that the endpoint is available and sized for throughput.

## Implementation checklist[​](#implementation-checklist "Direct link to Implementation checklist")

*   Validate `ai_mask` behavior on VARIANT columns with sample OTel span data.
*   Benchmark `ai_mask` throughput to size the pipeline schedule interval.
*   Define the allowlisted attribute keys that should skip redaction.
*   Set up access control groups (raw access versus redacted access).
*   Configure auto-TTL for raw table retention (or a scheduled `DELETE` and `VACUUM` job if strict deletion timing is required).
*   Build a monitoring dashboard for pipeline health and redaction coverage.
