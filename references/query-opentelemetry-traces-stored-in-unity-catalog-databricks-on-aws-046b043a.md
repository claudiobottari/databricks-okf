---
title: Query OpenTelemetry traces stored in Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/query-dbsql
ingestedAt: "2026-06-18T08:17:57.963Z"
---

By storing trace data in OpenTelemetry format in Unity Catalog, you can query traces using the MLflow Python SDK or through Databricks SQL using Unity Catalog tables and views.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

*   Store traces to Unity Catalog tables and generate traces. See [Store OpenTelemetry traces in Unity Catalog](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/trace-unity-catalog).

## Query traces using the MLflow Python SDK[​](#query-traces-using-the-mlflow-python-sdk "Direct link to Query traces using the MLflow Python SDK")

Use the MLflow Python SDK to search and load trace objects.

*   Use the `MLFLOW_TRACING_SQL_WAREHOUSE_ID` environment variable to specify a [Databricks SQL warehouse](https://docs.databricks.com/aws/en/compute/sql-warehouse/) to execute search queries.
*   Use the `locations` argument of `mlflow.search_traces` to specify one or more MLflow experiments or Unity Catalog schemas containing traces.
*   You can specify either the name of a Unity Catalog schema, or the ID of an MLflow experiment linked to a Unity Catalog schema. See [Setup: Create an experiment with a Unity Catalog trace location](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/trace-unity-catalog#setup).

Python

    import osimport mlflowfrom mlflow.entities.trace_location import UnityCatalog# Specify the name of a catalog and schema containing tracescatalog_name = "<UC_CATALOG>"schema_name = "<UC_SCHEMA>"table_prefix = "<UC_TABLE_PREFIX>"mlflow.set_tracking_uri("databricks")mlflow.set_experiment(    experiment_name="...",    trace_location=UnityCatalog(        catalog_name=catalog_name,        schema_name=schema_name,        table_prefix=table_prefix,    ),  # optional for existing experiments)# Specify the ID of a Databricks SQL warehouse for executing search queriesos.environ["MLFLOW_TRACING_SQL_WAREHOUSE_ID"] = "<SQL_WAREHOUSE_ID>"traces = mlflow.search_traces(    filter_string="trace.status = 'OK'",    order_by=["timestamp_ms DESC"],    include_spans=False,)print(traces)

To load the found trace:

Python

    import osimport mlflowmlflow.set_tracking_uri("databricks")# Specify the name of a catalog and schema containing tracescatalog_name = "<UC_CATALOG>"schema_name = "<UC_SCHEMA>"table_prefix = "<UC_TABLE_PREFIX>"# Specify the trace UUID (example: "13ffa97d571048d69d21da12240d5863")trace_uuid = "<TRACE_UUID>"# Specify the ID of a Databricks SQL warehouse for executing search queriesos.environ["MLFLOW_TRACING_SQL_WAREHOUSE_ID"] = "<SQL_WAREHOUSE_ID>"trace = mlflow.get_trace(    trace_id=f"trace:/{catalog_name}.{schema_name}.{table_prefix}/{trace_uuid}")print(trace)

## Query traces using Databricks SQL[​](#query-traces-using-databricks-sql "Direct link to query-traces-using-databricks-sql")

While the underlying data is stored in OpenTelemetry-compliant table formats, the MLflow service automatically creates Databricks SQL views alongside them. These views transform the OpenTelemetry data into the MLflow format.

For large trace volumes, query performance on these views can degrade. To maintain performance, create a [materialized view](https://docs.databricks.com/aws/en/ldp/concepts/materialized-views) over them and incrementally update the materialized view. For best performance on recent data, use the [API](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/query-via-sdk) to query traces.

Databricks recommends querying the views or using the API instead of relying on the underlying tables, because the schemas for those tables can change over time.

### `{table_prefix}_trace_unified`[​](#table_prefix_trace_unified "Direct link to table_prefix_trace_unified")

This view provides a unified look across all trace data grouped by each trace ID. Each row contains the [raw span data](https://mlflow.org/docs/latest/genai/concepts/trace/) and the [trace info metadata](https://mlflow.org/docs/latest/genai/concepts/trace/#core-structure). The metadata includes MLflow tags, metadata, and assessments.

#### Schema[​](#schema "Direct link to Schema")

Python

    trace_id: STRINGclient_request_id: STRINGrequest_time: TIMESTAMPstate: STRINGexecution_duration_ms: DECIMAL(30,9)request: STRINGresponse: STRINGtrace_metadata: MAP<STRING, STRING>tags: MAP<STRING, STRING>spans: LIST<STRUCT>    trace_id: STRING    span_id: STRING    trace_state: STRING    parent_span_id: STRING    flags: INT    name: STRING    kind: STRING    start_time_unix_nano: BIGINT    end_time_unix_nano: BIGINT    attributes: MAP<STRING, STRING>    dropped_attributes_count: INT    events: LIST<STRUCT>        time_unix_nano: BIGINT        name: STRING        attributes: MAP<STRING, STRING>        dropped_attributes_count: INT    dropped_events_count: INT    links: LIST<STRUCT>        trace_id: STRING        span_id: STRING        trace_state: STRING        attributes: MAP<STRING, STRING>        dropped_attributes_count: INT        flags: INT    dropped_links_count: INT    status: STRUCT        message: STRING        code: STRING    resource: STRUCT        attributes: MAP<STRING, STRING>        dropped_attributes_count: INT    resource_schema_url: STRING    instrumentation_scope: STRUCT        name: STRING        version: STRING        attributes: MAP<STRING, STRING>        dropped_attributes_count: INT    span_schema_url: STRINGassessments: LIST<STRUCT>    assessment_id: STRING    trace_id: STRING    assessment_name: STRING    source: STRUCT        source_id: STRING        source_type: STRING    create_time: TIMESTAMP    last_update_time: TIMESTAMP    expectation: STRUCT        value: STRING        serialized_value: STRUCT            serialization_format: STRING            value: STRING            stack_trace: STRING    feedback: STRUCT        value: STRING        error: STRUCT            error_code: STRING            error_message: STRING            stack_trace: STRING    rationale: STRING    metadata: MAP<STRING, STRING>    span_id: STRING    overrides: STRING    valid: STRING

### `{table_prefix}_trace_metadata`[​](#table_prefix_trace_metadata "Direct link to table_prefix_trace_metadata")

This view contains just the MLflow tags, metadata, and assessments grouped by trace ID and is more performant than the unified view for retrieving MLflow data.

#### Schema[​](#schema-1 "Direct link to Schema")

Python

    trace_id: STRINGclient_request_id: STRINGtags: MAP<STRING, STRING>trace_metadata: MAP<STRING, STRING>assessments: LIST<STRUCT>    assessment_id: STRING    trace_id: STRING    assessment_name: STRING    source: STRUCT        source_id: STRING        source_type: STRING    create_time: TIMESTAMP    last_update_time: TIMESTAMP    expectation: STRUCT        value: STRING        serialized_value: STRUCT            serialization_format: STRING            value: STRING            stack_trace: STRING    feedback: STRUCT        value: STRING        error: STRUCT            error_code: STRING            error_message: STRING            stack_trace: STRING    rationale: STRING    metadata: MAP<STRING, STRING>    span_id: STRING    overrides: STRING    valid: STRING

## MLflow annotation data formats[​](#mlflow-annotation-data-formats "Direct link to MLflow annotation data formats")

The data for MLflow tracing entities like metadata, tags, assessments, and links to runs are stored in the `{table_prefix}_otel_annotations` table. Each entity is stored as a single row with a typed `annotation_type`, and its fields are split across top-level columns (`name`, `value`, `comment`, `metadata`). The annotations table is append-only with soft-deletes, so you must de-duplicate on retrieval by taking the latest row per `annotation_id` (ordering by `updated_at` descending) and filtering out rows where `deleted_at` is set. The `value` and `metadata` columns are `VARIANT` (JSON).

The table has the following columns:

Python

    annotation_id: STRINGtarget_type: STRING ("TRACE" or "SPAN")target_id: STRING ("{trace_id}" for TRACE, "{trace_id}:{span_id}" for SPAN)annotation_type: STRING ("METADATA", "TAG", "FEEDBACK", "EXPECTATION", "RUN_LINK")name: STRINGvalue: VARIANTcomment: STRINGmetadata: VARIANTcreated_at: TIMESTAMPcreated_by: STRINGupdated_at: TIMESTAMPupdated_by: STRINGdeleted_at: TIMESTAMPdeleted_by: STRING

### MLflow metadata[​](#mlflow-metadata "Direct link to MLflow metadata")

Only one of these rows exists per trace. The `value` column is a JSON struct containing the trace's client request ID, metadata map, and request/response previews.

Python

    annotation_type: "METADATA"target_type: "TRACE"name: "metadata"value: VARIANT (includes `client_request_id`, `trace_metadata`, `request_preview`, `response_preview`)

### MLflow tags[​](#mlflow-tags "Direct link to MLflow tags")

Each tag is stored as a separate row. You can de-duplicate them within each trace using the `annotation_id` attribute, which is derived deterministically from the trace ID and tag key.

Python

    annotation_type: "TAG"target_type: "TRACE"name: STRING (the tag key)value: STRING (the tag value)

### MLflow assessments[​](#mlflow-assessments "Direct link to MLflow assessments")

Each assessment is stored as a `FEEDBACK` or `EXPECTATION` row depending on its type. You can de-duplicate them within each trace using the `annotation_id` attribute, which matches the assessment ID. The rationale is stored in the top-level `comment` column. User-supplied assessment metadata is stored in the `metadata` column alongside internal MLflow-managed fields (keys prefixed with `mlflow.`), which you should ignore when reading user metadata.

Python

    annotation_type: "FEEDBACK" | "EXPECTATION"target_type: "TRACE"name: STRING (the assessment name)value: VARIANT (feedback value, expectation value, or JSON-serialized expectation string)comment: STRING (the rationale)metadata: VARIANT (user-supplied assessment metadata)

### MLflow run links[​](#mlflow-run-links "Direct link to MLflow run links")

Each link between a trace and an MLflow run is stored as a separate row. You can de-duplicate them within each trace using the `annotation_id` attribute, which is derived deterministically from the trace ID and run ID.

Python

    annotation_type: "RUN_LINK"target_type: "TRACE"name: "run_link"value: STRING (the run ID)

## Analyze query performance[​](#analyze-query-performance "Direct link to Analyze query performance")

To diagnose slow queries, inspect query profiles in the SQL warehouse [query history](https://docs.databricks.com/aws/en/sql/user/queries/query-history):

1.  Go to the **SQL warehouses** page in your Databricks workspace.
2.  Select your SQL warehouse and click the **Query history** tab.
3.  Look for queries with **MLflow** specified as the source.
4.  Click a query to view its query profile.

In the query profile, inspect the following:

*   **Scheduling time**: If scheduling time is high, your queries are waiting due to heavy load on the warehouse. Switch to a different SQL warehouse using the drop-down menu in the MLflow UI, or configure a different warehouse in your client.
*   **Overall query performance**: For consistently slow queries, use a [larger SQL warehouse](https://docs.databricks.com/aws/en/compute/sql-warehouse/create), tighten upper and lower bounds on `trace.timestamp_ms`, and remove other filter predicates where possible.
