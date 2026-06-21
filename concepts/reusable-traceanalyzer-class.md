---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1dc11584f2fb8a7576fa40b5cfb5ce692e67d57c61fa7b6a908c4dce3f59ff3a
  pageDirectory: concepts
  sources:
    - examples-analyzing-traces-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - reusable-traceanalyzer-class
    - RTC
  citations:
    - file: examples-analyzing-traces-databricks-on-aws.md
title: Reusable TraceAnalyzer class
description: Design pattern for a utility class that encapsulates advanced trace analysis including error summary, LLM usage aggregation, retrieval metrics, span hierarchy, and evaluation data export.
tags:
  - mlflow
  - code-patterns
  - trace-analysis
timestamp: "2026-06-18T12:14:37.635Z"
---

# Reusable TraceAnalyzer class

The **Reusable TraceAnalyzer class** is a Python utility class that provides a structured, programmatic interface for analyzing [MLflow](/concepts/mlflow.md) [Trace](/concepts/traces.md) objects. It encapsulates common analysis patterns — error summarization, LLM usage aggregation, retrieval quality metrics, span hierarchy visualization, and evaluation data export — into a single composable object. The class is designed to be instantiated once per trace and reused for multiple analytical queries without repeating trace traversal logic. ^[examples-analyzing-traces-databricks-on-aws.md]

## Constructor

```python
class TraceAnalyzer:
    def __init__(self, trace: mlflow.entities.Trace):
        self.trace = trace
```

The constructor accepts a single `Trace` object (obtained via `mlflow.get_trace()`) and stores it as an instance attribute. All subsequent methods operate on this stored trace. ^[examples-analyzing-traces-databricks-on-aws.md]

## Methods

### Error Summary

`get_error_summary()` returns a list of error dictionaries collected from three levels of the trace: the trace-level state, individual span statuses, and [assessment](/concepts/assessments.md) errors. Each dictionary contains the error level (`"trace"`, `"span"`, or `"assessment"`), the span or assessment name where the error occurred, and a human-readable message or description. ^[examples-analyzing-traces-databricks-on-aws.md]

### LLM Usage Summary

`get_llm_usage_summary()` aggregates token usage across all spans whose type is `CHAT_MODEL` or `"LLM"`. It returns a dictionary containing `total_llm_calls`, `total_input_tokens`, `total_output_tokens`, `total_tokens`, and a list of per-span usage details (name, input and output tokens). ^[examples-analyzing-traces-databricks-on-aws.md]

### Retrieval Metrics

`get_retrieval_metrics()` extracts quality metrics from all spans of type `RETRIEVER`. For each retriever span that has outputs, it calculates the number of retrieved documents, average relevance score, maximum relevance score, and minimum relevance score. The method returns a list of metric dictionaries, one per retriever span. ^[examples-analyzing-traces-databricks-on-aws.md]

### Span Hierarchy

`get_span_hierarchy()` builds a tree representation of the trace's spans by identifying root spans (those without a parent) and recursively listing their children in chronological order. Each node in the tree is a dictionary containing `name`, `type`, `duration_ms`, `status`, and `indent` level. This allows visualising the execution flow and latency breakdown. ^[examples-analyzing-traces-databricks-on-aws.md]

### Export for Evaluation

`export_for_evaluation()` transforms the trace into a structured dictionary suitable for downstream evaluation pipelines. The exported data includes the `trace_id`, the original `request` and `response` payloads, the full text of retrieved context documents (from [RETRIEVER Spans](/concepts/retriever-spans.md)), expected facts from expectation assessments, and metadata (user ID, session ID, duration, and timestamp). ^[examples-analyzing-traces-databricks-on-aws.md]

## Usage Example

```python
import mlflow
from trace_analyzer import TraceAnalyzer  # or inlined

trace_id = mlflow.get_last_active_trace_id()
trace = mlflow.get_trace(trace_id)

analyzer = TraceAnalyzer(trace)

# Get errors
errors = analyzer.get_error_summary()
print(f"Errors found: {len(errors)}")

# Get LLM token usage
llm_usage = analyzer.get_llm_usage_summary()
print(f"Total tokens: {llm_usage['total_tokens']}")

# Get retrieval metrics
retrieval_metrics = analyzer.get_retrieval_metrics()
for metric in retrieval_metrics:
    print(f"  - {metric['span_name']}: {metric['num_documents']} docs")

# Export for evaluation
eval_data = analyzer.export_for_evaluation()
```

^[examples-analyzing-traces-databricks-on-aws.md]

## Benefits

- **Encapsulation** – Analysis logic is self-contained; no repeated trace-searching code.
- **Composability** – Results from different methods can be combined into a single analysis report.
- **Consistency** – All methods follow the same pattern of iterating over `self.trace.data.spans` and `self.trace.info.*`.
- **Reusability** – The same `TraceAnalyzer` instance can be queried multiple times with different methods, and the class can be extended with additional analysis functions for custom requirements.

## Related Concepts

- [[MLflow Trace]] — The core data structure that `TraceAnalyzer` wraps
- Span — The unit of execution within a trace
- Error monitoring — Pattern for continuous error detection using `TraceAnalyzer`
- [Performance monitoring](/concepts/performance-monitoring-with-mlflow-traces.md) — Analyzing latency percentiles and outliers
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Building structured datasets from traces for offline evaluation
- [Assessments](/concepts/assessments.md) — Human or LLM feedback logged to traces

## Sources

- examples-analyzing-traces-databricks-on-aws.md

# Citations

1. [examples-analyzing-traces-databricks-on-aws.md](/references/examples-analyzing-traces-databricks-on-aws-ebc17f1a.md)
