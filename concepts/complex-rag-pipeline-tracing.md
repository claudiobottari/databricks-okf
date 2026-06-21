---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3175e0f96cb8b6a671a143f5420ce1800ac2b679ad629071ce058c36b2a91c71
  pageDirectory: concepts
  sources:
    - examples-analyzing-traces-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - complex-rag-pipeline-tracing
    - CRPT
  citations:
    - file: examples-analyzing-traces-databricks-on-aws.md
title: Complex RAG Pipeline Tracing
description: Comprehensive pattern for instrumenting a full RAG pipeline with multiple span types (CHAIN, RETRIEVER, CHAT_MODEL, TOOL), custom tags, Document objects, chat tools, and token usage tracking.
tags:
  - mlflow
  - tracing
  - rag
  - llm
timestamp: "2026-06-19T18:45:22.177Z"
---

# Complex RAG Pipeline Tracing

**Complex RAG pipeline tracing** refers to the practice of instrumenting a multi-step [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) system with detailed [MLflow Tracing](/concepts/mlflow-tracing.md) to capture every stage of the pipeline — including document retrieval, answer generation, tool calls, and orchestration logic — along with custom metadata, token usage statistics, assessments, and expectations. This approach provides comprehensive observability, debugging, and quality evaluation across the entire application. ^[examples-analyzing-traces-databricks-on-aws.md]

## Overview

A complex RAG pipeline typically orchestrates several stages: document retrieval from a vector store, context-aware answer generation via a chat model, and optional tool invocations such as fact-checking. By wrapping each stage with MLflow's `@mlflow.trace` decorator and specifying appropriate [span types](/concepts/mlflow-spans.md), developers create a hierarchical trace that shows the flow of data and the timing of each sub-operation. ^[examples-analyzing-traces-databricks-on-aws.md]

The example trace in the source material models four spans:

- **`rag_pipeline`** – The main orchestration span (type `CHAIN`), which calls the inner functions and returns the final answer, sources, and fact-check result.
- **`retrieve_documents`** – A retriever span (type `RETRIEVER`) that fetches documents from a vector store and sets span outputs to structured Document objects.
- **`generate_answer`** – A chat model span (type `CHAT_MODEL`) that records input messages, tool definitions, and token usage.
- **`fact_check_tool`** – A tool span (type `TOOL`) that simulates verifying facts; it may raise an error for demonstration.

^[examples-analyzing-traces-databricks-on-aws.md]

## Creating a Complex RAG Trace

### Decorating Functions with `@mlflow.trace`

Each function in the pipeline is annotated with `@mlflow.trace(span_type=<SpanType>)`. The decorator automatically creates a span that records start/end times, inputs, and outputs. Custom tags and metadata are added inside the orchestration function using `mlflow.update_current_trace()`: ^[examples-analyzing-traces-databricks-on-aws.md]

```python
@mlflow.trace(span_type=SpanType.CHAIN)
def rag_pipeline(question: str):
    mlflow.update_current_trace(
        tags={
            "environment": "production",
            "version": "2.1.0",
            "user_id": "U12345",
            "session_id": "S98765",
            "mlflow.traceName": "rag_pipeline"
        }
    )
    documents = retrieve_documents(question)
    response = generate_answer(question, documents)
    fact_check_result = fact_check_tool(response)
    return {"answer": response, "fact_check": fact_check_result, "sources": [...]}
```

### Setting Span Outputs for Retrievers

For [RETRIEVER Spans](/concepts/retriever-spans.md), outputs should be set using `span.set_outputs()` with a list of `Document` objects that conform to the MLflow schema. Each document carries `page_content`, a `doc_uri`, and optional metadata like `relevance_score`: ^[examples-analyzing-traces-databricks-on-aws.md]

```python
@mlflow.trace(span_type=SpanType.RETRIEVER)
def retrieve_documents(query: str):
    span = mlflow.get_current_active_span()
    documents = [
        Document(page_content="...", metadata={"doc_uri": "docs/guide.md", "relevance_score": 0.95}),
        # ...
    ]
    span.set_outputs(documents)
    return [doc.to_dict() for doc in documents]
```

### Recording Chat Model Invocations

For LLM calls, span inputs should be set to the list of messages, and tool definitions can be attached via `set_span_chat_tools()`. Token usage is recorded as span attributes (`llm.token_usage.*`): ^[examples-analyzing-traces-databricks-on-aws.md]

```python
@mlflow.trace(span_type=SpanType.CHAT_MODEL)
def generate_answer(question, documents):
    span = mlflow.get_current_active_span()
    messages = [
        {"role": "system", "content": "..."},
        {"role": "user", "content": f"Context: {documents}\nQuestion: {question}"}
    ]
    span.set_inputs(messages)
    set_span_chat_tools(span, tools)
    span.set_attribute("llm.token_usage.input_tokens", 150)
    # ...
```

## Adding Assessments and Expectations

After executing the pipeline, developers can attach qualitative and quantitative feedback to the trace. MLflow provides three methods: ^[examples-analyzing-traces-databricks-on-aws.md]

- **`mlflow.log_feedback()`** – Log human ratings, LLM judge scores, or code-based evaluations at the trace or span level.
- **`mlflow.log_expectation()`** – Record ground-truth expected values (e.g., facts that should appear in the answer) for later comparison.
- **`AssessmentSource`** – Each assessment includes a source type (`HUMAN`, `LLM_JUDGE`, or `CODE`) and an identifier.

Span-specific feedback can be added by passing the `span_id` to `log_feedback`. This enables granular evaluation of individual stages, such as retrieval quality. ^[examples-analyzing-traces-databricks-on-aws.md]

## Analyzing the Trace

The source material provides a reusable `TraceAnalyzer` class that extracts meaningful information from a completed trace: ^[examples-analyzing-traces-databricks-on-aws.md]

- **Error summary** – Finds all errors at the trace, span, and assessment levels.
- **LLM usage summary** – Aggregates token counts across all chat model spans.
- **Retrieval metrics** – Computes average/min/max relevance scores from retrieved documents.
- **Span hierarchy** – Builds a tree view showing parent–child relationships and durations.
- **Performance breakdown** – Calculates time spent per span type as a percentage of total.
- **Export for evaluation** – Packages request, response, retrieved context, expectations, and metadata into a dictionary suitable for downstream evaluation pipelines.

The `analyze_trace()` function in the source demonstrates a comprehensive report that includes basic info, tags, token usage, span counts, retrieval details, assessments, and performance breakdown. ^[examples-analyzing-traces-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The underlying mechanism for capturing execution spans
- Span Types – Categories like `CHAIN`, `RETRIEVER`, `CHAT_MODEL`, `TOOL`
- [Assessments](/concepts/assessments.md) – Human, LLM, or code feedback logged to traces
- Expectations – Ground-truth values for evaluating agent outputs
- [Trace Analysis Utilities](/concepts/comprehensive-trace-analysis-utility.md) – Programmatic tools for summarizing trace data
- [Production Monitoring](/concepts/production-monitoring.md) – Applying trace analysis in real-world environments

## Sources

- examples-analyzing-traces-databricks-on-aws.md

# Citations

1. [examples-analyzing-traces-databricks-on-aws.md](/references/examples-analyzing-traces-databricks-on-aws-ebc17f1a.md)
