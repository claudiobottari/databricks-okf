---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 560d1c2ee51dbe789d2e44897b7f3caf446e1f3e138c249867c265629b0ecb7b
  pageDirectory: concepts
  sources:
    - examples-analyzing-traces-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - traceanalyzer-pattern
  citations:
    - file: examples-analyzing-traces-databricks-on-aws.md
title: TraceAnalyzer Pattern
description: A reusable object-oriented utility class for advanced trace analysis, providing methods for error summaries, LLM usage aggregation, retrieval metrics, span hierarchy visualization, and evaluation data export.
tags:
  - mlflow
  - design-patterns
  - tracing
  - evaluation
timestamp: "2026-06-19T10:26:12.735Z"
---

Here is the wiki page for "TraceAnalyzer Pattern".

---

## TraceAnalyzer Pattern

The **TraceAnalyzer Pattern** is a code structure for programmatically inspecting [GenAI traces](/concepts/mlflow-genai-trace.md) logged by [MLflow Tracing](/concepts/mlflow-tracing.md). It wraps a single [`mlflow.entities.Trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.entities.Trace) object and exposes domain-specific analysis methods, providing a reusable alternative to ad‑hoc trace inspection scattered across application code. ^[examples-analyzing-traces-databricks-on-aws.md]

## Motivation

Raw trace objects contain nested spans, status codes, tags, token counts, assessments, and intermediate outputs. Without a dedicated abstraction, extracting information such as *“what errors occurred?”* or *“how many LLM calls were made?”* requires manual iteration over the trace’s `data.spans` list and inline attribute checks. The TraceAnalyzer Pattern centralizes this logic into a class, making analysis self-documenting and easier to test. ^[examples-analyzing-traces-databricks-on-aws.md]

## Structure

The pattern typically follows a class-based structure:

| Component | Description |
|---|---|
| **Constructor** | Accepts a `mlflow.entities.Trace` object and stores it as `self.trace`. |
| **Analysis methods** | Methods that traverse the trace’s `data.spans`, `info.tags`, `info.token_usage`, and `info.assessments` to return structured results. |
| **Utility methods** | Methods that pre-process or re-format trace data for downstream use (e.g., exporting for evaluation). |

Example skeleton:

```python
class TraceAnalyzer:
    def __init__(self, trace: mlflow.entities.Trace):
        self.trace = trace

    def get_error_summary(self):
        # Check trace status and span errors
        ...

    def get_llm_usage_summary(self):
        # Aggregate token usage across LLM spans
        ...
```

^[examples-analyzing-traces-databricks-on-aws.md]

## Common Analysis Methods

### Error Summary

`get_error_summary()` inspects both the top-level trace status and every span in `trace.data.spans`. It collects errors at three levels:

1. **Trace level** – if `trace.info.state == "ERROR"`, the trace’s `response_preview` is recorded.
2. **Span level** – for spans whose `status.status_code.name` equals `"ERROR"`, the span name, type, and `status.description` are recorded.
3. **Assessment level** – assessments with an `error` attribute are also included.

The method returns a list of error dictionaries, each tagged with the level (e.g. `"trace"`, `"span"`, `"assessment"`). ^[examples-analyzing-traces-databricks-on-aws.md]

### LLM Usage Summary

`get_llm_usage_summary()` iterates over spans whose `span_type` is `SpanType.CHAT_MODEL` or `"LLM"`. For each span it reads the `llm.token_usage.input_tokens` and `llm.token_usage.output_tokens` attributes. The aggregated result includes:

- `total_llm_calls`
- `total_input_tokens`
- `total_output_tokens`
- A list of per-span usage dictionaries.

This method provides a single view of all LLM consumption within a trace. ^[examples-analyzing-traces-databricks-on-aws.md]

### Retrieval Metrics

`get_retrieval_metrics()` queries spans of type `SpanType.RETRIEVER`. For each retriever span that has outputs, it extracts document metadata (specifically `relevance_score` from `doc['metadata']`) and computes:

- `num_documents`
- `avg_relevance`
- `max_relevance`
- `min_relevance`

The returned list of metrics enables quality checks on the retrieval stage of a [RAG pipeline](/concepts/rag-pipeline-txtai.md). ^[examples-analyzing-traces-databricks-on-aws.md]

### Span Hierarchy

`get_span_hierarchy()` builds a tree view of the trace’s spans. It identifies root spans (those with `parent_id == None`) and recursively collects child spans, recording each span’s `name`, `type`, `duration_ms`, and `status`. The result is a flat list of dictionaries with an `indent` field that can be used to render a visual tree. ^[examples-analyzing-traces-databricks-on-aws.md]

### Export for Evaluation

`export_for_evaluation()` reformats the trace into a dictionary suitable for downstream evaluation pipelines. It extracts:

- The raw request and response (parsed from JSON if available).
- The retrieved context (page content from [RETRIEVER Spans](/concepts/retriever-spans.md)).
- Expected facts from Trace Expectations.
- Metadata such as `user_id`, `session_id`, and duration.

This is useful when converting a single trace into a row in an [Evaluation Dataset](/concepts/evaluation-dataset.md). ^[examples-analyzing-traces-databricks-on-aws.md]

## Usage Example

```python
trace = mlflow.get_trace(trace_id)
analyzer = TraceAnalyzer(trace)

errors = analyzer.get_error_summary()
print(f"Errors found: {len(errors)}")

llm_usage = analyzer.get_llm_usage_summary()
print(f"LLM calls: {llm_usage['total_llm_calls']}, tokens: {llm_usage['total_tokens']}")

retrieval_metrics = analyzer.get_retrieval_metrics()
for m in retrieval_metrics:
    print(f"  {m['span_name']}: {m['num_documents']} docs, avg relevance: {m['avg_relevance']}")

eval_data = analyzer.export_for_evaluation()
```

^[examples-analyzing-traces-databricks-on-aws.md]

## Relationship to Other Patterns

The TraceAnalyzer Pattern complements the [Error Monitoring Pattern](/concepts/error-monitoring-with-mlflow-traces.md) and [Performance Monitoring Pattern](/concepts/performance-monitoring-with-mlflow-traces.md), which operate at the level of multiple traces returned by `mlflow.search_traces()`. While those patterns collect aggregate statistics, the TraceAnalyzer Pattern provides a fine-grained view of a single trace. ^[examples-analyzing-traces-databricks-on-aws.md]

The class can also be composed with MLflow log_feedback API|MLflow Feedback APIs: after analysis, developers can programmatically log assessments to the trace using `mlflow.log_feedback()` to enrich it with human or judge annotations. ^[examples-analyzing-traces-databricks-on-aws.md]

## When to Use

- You need to inspect or debug a specific trace after an error or performance anomaly.
- You want a single, testable abstraction that encapsulates all trace analysis logic.
- You are building a monitoring or evaluation tool that operates on traces produced by [MLflow GenAI](/concepts/mlflow-3-for-genai.md).

For aggregate analysis across many traces, see mlflow.search_traces() API|Search Traces Programmatically and the [Error Monitoring Pattern](/concepts/error-monitoring-with-mlflow-traces.md). ^[examples-analyzing-traces-databricks-on-aws.md]

## Sources

- examples-analyzing-traces-databricks-on-aws.md

# Citations

1. [examples-analyzing-traces-databricks-on-aws.md](/references/examples-analyzing-traces-databricks-on-aws-ebc17f1a.md)
