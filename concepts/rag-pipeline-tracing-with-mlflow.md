---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b0581172185e56d1931ac91f3aa902b621c5715dced94e9410bb4ad563478429
  pageDirectory: concepts
  sources:
    - examples-analyzing-traces-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rag-pipeline-tracing-with-mlflow
    - RPTWM
    - Agent Tracing with MLflow
    - RAG Pipeline Tracing
  citations:
    - file: examples-analyzing-traces-databricks-on-aws.md
title: RAG Pipeline Tracing with MLflow
description: Instrumenting a Retrieval-Augmented Generation pipeline with MLflow traces using RETRIEVER, CHAT_MODEL, TOOL, and CHAIN span types, including document metadata, token usage, and tool definitions.
tags:
  - mlflow
  - rag
  - tracing
  - generative-ai
timestamp: "2026-06-19T10:25:55.221Z"
---

# RAG Pipeline Tracing with MLflow

**RAG Pipeline Tracing with MLflow** refers to the practice of instrumenting a [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) application with [MLflow Tracing](/concepts/mlflow-tracing.md)](https://mlflow.org/docs/latest/llms/tracing/index.html) to capture detailed execution information across the retrieval, generation, and optional tool-use steps. By creating structured traces, developers can monitor performance, debug errors, and collect assessments for later analysis. ^[examples-analyzing-traces-databricks-on-aws.md]

## Creating a RAG pipeline trace

A RAG pipeline can be traced by applying the `@mlflow.trace` decorator to each logical component and assigning an appropriate `SpanType`. The outermost orchestrator function typically uses `SpanType.CHAIN`, while retrieval is tagged with `SpanType.RETRIEVER`, generation with `SpanType.CHAT_MODEL`, and any auxiliary tools (e.g., fact check) with `SpanType.TOOL`. ^[examples-analyzing-traces-databricks-on-aws.md]

The decorator automatically creates a span that records inputs, outputs, timing, and status. Custom tags (e.g., `environment`, `version`, `user_id`, `session_id`) can be added to the trace via `mlflow.update_current_trace(tags={...})` and are available for later filtering and analysis. ^[examples-analyzing-traces-databricks-on-aws.md]

## Capturing retrieval details

Within a retriever span, documents can be structured using `mlflow.entities.Document` objects. Each document should contain `page_content` (the text chunk) and a `metadata` dictionary that typically includes fields such as `doc_uri`, `chunk_id`, and `relevance_score`. After constructing the documents, call `span.set_outputs(documents)` to attach the retrieved items to the span. The retriever function can then return the documents in a serializable format (e.g., `to_dict()`). ^[examples-analyzing-traces-databricks-on-aws.md]

## Capturing generation details

For the LLM generation step, set the span’s inputs to the messages list and optionally define available functions using `mlflow.tracing.set_span_chat_tools()`. Token usage can be recorded by calling `span.set_attribute()` with keys such as `llm.token_usage.input_tokens`, `llm.token_usage.output_tokens`, and `llm.token_usage.total_tokens`. These attributes are later aggregated during analysis. ^[examples-analyzing-traces-databricks-on-aws.md]

## Adding assessments and expectations

After the trace is created, feedback can be logged at both the trace level and the span level using `mlflow.log_feedback()`. Each assessment requires:

- `trace_id` (and optionally `span_id`),
- a `name` (e.g., `"helpfulness"`, `"retrieval_quality"`),
- a `value` (numeric, string, or boolean),
- a `source` (constructed from `AssessmentSource` with a `source_type` and `source_id`).

Supported source types include `HUMAN`, `LLM_JUDGE`, and `CODE`. A rationale and additional metadata can also be supplied. ^[examples-analyzing-traces-databricks-on-aws.md]

Expectations — ground-truth facts that the agent should have produced — can be logged with `mlflow.log_expectation()`, using a similar structure. These expectations can later be compared against the actual response during evaluation. ^[examples-analyzing-traces-databricks-on-aws.md]

## Analyzing traces

The `TraceAnalyzer` utility class provides a reusable way to extract meaningful information from a single trace:

- **Error summary**: Find all errors at the trace, span, and assessment level.
- **LLM usage summary**: Aggregate token counts across all chat model spans.
- **Retrieval metrics**: Extract document counts and relevance scores from [RETRIEVER Spans](/concepts/retriever-spans.md).
- **Span hierarchy**: Build a tree view of spans with duration and status.
- **Evaluation export**: Package request, response, retrieved context, expected facts, and metadata into a dictionary suitable for downstream evaluation. ^[examples-analyzing-traces-databricks-on-aws.md]

Additionally, the source material demonstrates functions for [error monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/analyze-traces#error-monitoring) and [performance monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/analyze-traces#performance-monitoring) over multiple traces, including calculating latency percentiles and identifying outliers. ^[examples-analyzing-traces-databricks-on-aws.md]

## Related concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Core mechanism for recording execution spans.
- Span Types – Classification of spans (CHAIN, RETRIEVER, CHAT_MODEL, TOOL).
- [GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – Offline and online evaluation of agent quality.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – High-level APIs for building and monitoring generative AI applications.
- Trace Analysis – Programmatic query and analysis of traces with `mlflow.search_traces()`.

## Sources

- examples-analyzing-traces-databricks-on-aws.md

# Citations

1. [examples-analyzing-traces-databricks-on-aws.md](/references/examples-analyzing-traces-databricks-on-aws-ebc17f1a.md)
