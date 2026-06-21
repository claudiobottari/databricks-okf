---
title: Span concepts | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/span-concepts
ingestedAt: "2026-06-18T08:18:13.881Z"
---

The [Span](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Span) object is a fundamental building block in the Trace data model. Each span captures a single step in a trace, for example, an LLM call, a tool execution, or a retrieval operation.

Spans are organized hierarchically in a trace to represent your application's execution flow. Each span captures:

*   Input and output data
*   Timing information (start and end times)
*   Status (success or error)
*   Metadata and attributes about the operation
*   Relationship to other spans (parent-child connections)

![Span Architecture](https://docs.databricks.com/aws/en/assets/images/trace-span-a0ce1bb4698cf4ba9a5910029a8be6cf.png)

## Span object schema[​](#span-object-schema "Direct link to Span object schema")

The MLflow Span schema is compatible with the [OpenTelemetry specification](https://opentelemetry.io/docs/concepts/signals/traces#spans). The schema has 11 core properties:

For more information, see the [MLflow API reference](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Span).

## Span attributes[​](#span-attributes "Direct link to Span attributes")

Attributes are key-value pairs that provide insight into behavioral modifications for function and method calls. They capture metadata about the operation's configuration and execution context.

You can add platform-specific attributes to enrich observability. For example, you can add the [Unity Catalog objects](https://docs.databricks.com/aws/en/data-governance/unity-catalog/) the span touched, the [model serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/), or the [compute resource](https://docs.databricks.com/aws/en/compute/).

For example, set attributes on a span that wraps an LLM call:

Python

    span.set_attributes({    "ai.model.name": "claude-3-5-sonnet-20250122",    "ai.model.version": "2025-01-22",    "ai.model.provider": "anthropic",    "ai.model.temperature": 0.7,    "ai.model.max_tokens": 1000,})

## Span types[​](#span-types "Direct link to span-types")

MLflow provides predefined [`SpanType`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.SpanType) values for common operations. For specialized cases, pass a custom string value as the span type.

### Setting span types[​](#setting-span-types "Direct link to Setting span types")

To set the [`SpanType`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.SpanType) for a span, pass `span_type` to the decorator or context manager:

Python

    import mlflowfrom mlflow.entities import SpanType# Using a built-in span type@mlflow.trace(span_type=SpanType.RETRIEVER)def retrieve_documents(query: str):    ...# Using a custom span type@mlflow.trace(span_type="ROUTER")def route_request(request):    ...# With context managerwith mlflow.start_span(name="process", span_type=SpanType.TOOL) as span:    span.set_inputs({"data": data})    result = process_data(data)    span.set_outputs({"result": result})

### Searching spans by type[​](#searching-spans-by-type "Direct link to Searching spans by type")

Query spans programmatically using [MLflow `search_spans()`](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/access-trace-data#search-span):

Python

    import mlflowfrom mlflow.entities import SpanTypetrace = mlflow.get_trace("<trace_id>")retriever_spans = trace.search_spans(span_type=SpanType.RETRIEVER)

You can also filter by span type in the MLflow UI when viewing traces.

## Active vs. finished spans[​](#active-vs-finished-spans "Direct link to Active vs. finished spans")

An active span, represented by [`LiveSpan`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.LiveSpan), is one that MLflow is currently writing. Active spans are produced by a [function decorated with `@mlflow.trace`](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/function-decorator) or by a [span context manager](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/span-tracing). After the decorated function exits or the context manager closes, the span is finished and becomes an immutable [`Span`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Span).

To modify the active span, retrieve it with [`mlflow.get_current_active_span()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.get_current_active_span).

## `RETRIEVER` span schema[​](#-retriever-span-schema "Direct link to -retriever-span-schema")

The `RETRIEVER` span type represents operations that fetch data from a data store, for example, querying documents from a vector store. RETRIEVER spans use a fixed output schema, which unlocks richer UI rendering and evaluation features in MLflow. The output must be a list of documents, where each document is a dictionary with:

*   **`page_content`** (`str`): Text content of the retrieved document chunk
*   **`metadata`** (`Optional[Dict[str, Any]]`): Additional metadata, including:
    *   `doc_uri` (`str`): The document source URI. When you use [AI Search](https://docs.databricks.com/aws/en/ai-search/ai-search) on Databricks, you can record Unity Catalog volume paths in `doc_uri` for full lineage tracking.
    *   `chunk_id` (`str`): Identifier if the document is part of a larger chunked document.
*   **`id`** (`Optional[str]`): Unique identifier for the document chunk.

Use the MLflow [`Document` entity](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Document) to construct this output structure.

**Example implementation**:

Python

    import mlflowfrom mlflow.entities import SpanType, Documentdef search_store(query: str) -> list[tuple[str, str]]:    # Simulate retrieving documents (content, doc_uri pairs) from a vector database.    return [        ("MLflow Tracing helps debug GenAI applications...", "docs/mlflow/tracing_intro.md"),        ("Key components of a trace include spans...", "docs/mlflow/tracing_datamodel.md"),        ("MLflow provides automatic instrumentation...", "docs/mlflow/auto_trace.md"),    ]@mlflow.trace(span_type=SpanType.RETRIEVER)def retrieve_relevant_documents(query: str):    docs = search_store(query)    span = mlflow.get_current_active_span()    # Set outputs in the expected format    outputs = [        Document(page_content=doc, metadata={"doc_uri": uri})        for doc, uri in docs    ]    span.set_outputs(outputs)    # Return the raw tuples for the caller; the trace records the structured Document objects.    return docs# Usageuser_query = "MLflow Tracing benefits"retrieved_docs = retrieve_relevant_documents(user_query)

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Trace concepts](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/tracing-101) — Understand trace-level concepts and structure.
*   [Get started: MLflow Tracing for GenAI (Databricks Notebook)](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/tracing/tracing-notebook) — Get hands-on experience with tracing in a notebook.
