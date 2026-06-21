---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 92096c5a1ad8102eb3ae2221927879ffa813b79288ce2a7784364f99fd24c939
  pageDirectory: concepts
  sources:
    - examples-analyzing-traces-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - traceanalyzer-reusable-utility-class
    - TRUC
    - Trace Analyzer Utility
    - TraceAnalyzer Utility
  citations:
    - file: examples-analyzing-traces-databricks-on-aws.md
title: TraceAnalyzer Reusable Utility Class
description: Advanced reusable Python class for trace analysis providing error summary, LLM usage aggregation, retrieval metrics extraction, span hierarchy building, and evaluation data export.
tags:
  - mlflow
  - tracing
  - utility
  - python
timestamp: "2026-06-19T18:44:53.024Z"
---

# TraceAnalyzer Reusable Utility Class

The **TraceAnalyzer** is a Python utility class designed for advanced analysis of GenAI traces logged via [MLflow Tracing](/concepts/mlflow-tracing.md). Wrapping a `mlflow.entities.Trace` object, it provides structured methods for extracting errors, aggregating LLM token usage, computing retrieval quality metrics, building span hierarchies, and exporting evaluation-ready data. ^[examples-analyzing-traces-databricks-on-aws.md]

## Overview

The `TraceAnalyzer` class offers a reusable, object-oriented interface for common trace analysis tasks. By encapsulating trace inspection logic, it simplifies repeated patterns such as error summarization, performance breakdown, and data export for evaluation pipelines. The class is intended for use in production monitoring, debugging, and offline analysis workflows. ^[examples-analyzing-traces-databricks-on-aws.md]

## Constructor

```python
def __init__(self, trace: mlflow.entities.Trace):
```

The constructor accepts a single `mlflow.entities.Trace` object and stores it as `self.trace` for subsequent method calls. ^[examples-analyzing-traces-databricks-on-aws.md]

## Methods

### `get_error_summary()`

Returns a list of dictionaries describing all errors found in the trace. It checks three levels:

1. **Trace-level**: If the trace status is `ERROR`, it records a trace-level error.
2. **Span-level**: For each span whose status code is `ERROR`, it records the span name, type, and status description.
3. **Assessment-level**: For each assessment that contains an error, it records the assessment name and error string.

Each error dictionary contains keys `level`, `message`, and optionally `span_name`, `span_type`, `span_id`, `assessment_name`, or `details`. ^[examples-analyzing-traces-databricks-on-aws.md]

### `get_llm_usage_summary()`

Aggregates LLM token usage across all spans in the trace. Returns a dictionary with:

- `total_llm_calls` — total number of spans with `SpanType.CHAT_MODEL` or type `"LLM"`
- `total_input_tokens` — sum of `llm.token_usage.input_tokens` across those spans
- `total_output_tokens` — sum of `llm.token_usage.output_tokens` across those spans
- `total_tokens` — sum of input and output tokens
- `spans` — a list of dictionaries, each containing `name`, `input_tokens`, and `output_tokens` for every LLM span

^[examples-analyzing-traces-databricks-on-aws.md]

### `get_retrieval_metrics()`

Extracts retrieval quality metrics from spans of type `SpanType.RETRIEVER`. For each retriever span that has outputs, it computes:

- `num_documents` — count of retrieved documents
- `avg_relevance` — mean of `relevance_score` values from document metadata
- `max_relevance` — maximum relevance score
- `min_relevance` — minimum relevance score

Returns a list of dictionaries, one per retriever span. ^[examples-analyzing-traces-databricks-on-aws.md]

### `get_span_hierarchy()`

Builds a hierarchical view of the trace's spans. It first identifies root spans (those with no parent), then recursively builds a tree by finding each span's children. For each span, the result includes:

- `indent` — nesting level (0 for roots)
- `name` — span name
- `type` — span type (e.g., `CHAIN`, `RETRIEVER`, `CHAT_MODEL`)
- `duration_ms` — execution duration in milliseconds
- `status` — span status code name

Returns a flat list of dictionaries ordered by start time within each parent. ^[examples-analyzing-traces-databricks-on-aws.md]

### `export_for_evaluation()`

Exports trace data in a format suitable for evaluation pipelines. The returned dictionary contains:

- `trace_id` — trace identifier
- `request` — parsed JSON request data (if available)
- `response` — parsed JSON response data (if available)
- `retrieved_context` — list of `page_content` strings from retriever span outputs
- `expected_facts` — values from assessments of type `expectation`, keyed by `name`
- `metadata` — dictionary with `user_id`, `session_id`, `duration_ms`, and `timestamp`

^[examples-analyzing-traces-databricks-on-aws.md]

## Usage Example

```python
analyzer = TraceAnalyzer(trace)

# Get various analyses
errors = analyzer.get_error_summary()
print(f"Errors found: {len(errors)}")
for error in errors:
    print(f"  - {error['level']}: {error.get('message', error.get('error'))}")

llm_usage = analyzer.get_llm_usage_summary()
print(f"\nLLM Usage: {llm_usage['total_tokens']} total tokens across {llm_usage['total_llm_calls']} calls")

retrieval_metrics = analyzer.get_retrieval_metrics()
print(f"\nRetrieval Metrics:")
for metric in retrieval_metrics:
    print(f"  - {metric['span_name']}: {metric['num_documents']} docs, avg relevance: {metric['avg_relevance']}")

# Export for evaluation
eval_data = analyzer.export_for_evaluation()
print(f"\nExported evaluation data with {len(eval_data['retrieved_context'])} context chunks")
```

^[examples-analyzing-traces-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The observability framework that produces the traces analyzed by this utility
- [GenAI Trace Analysis](/concepts/genai-trace-analysis-and-debugging.md) — Broader topic of analyzing traces from generative AI applications
- Error Monitoring — Using traces to detect and analyze production errors
- [Performance Monitoring](/concepts/performance-monitoring-with-mlflow-traces.md) — Analyzing trace latency and identifying bottlenecks
- [RAG Pipeline Tracing](/concepts/rag-pipeline-tracing-with-mlflow.md) — Tracing retrieval-augmented generation pipelines, a common use case for this analyzer

## Sources

- examples-analyzing-traces-databricks-on-aws.md

# Citations

1. [examples-analyzing-traces-databricks-on-aws.md](/references/examples-analyzing-traces-databricks-on-aws-ebc17f1a.md)
