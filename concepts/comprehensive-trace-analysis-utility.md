---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2ff869e89349911fc75b35b5400343716bbd023bec30953de7ddc32ad672e310
  pageDirectory: concepts
  sources:
    - examples-analyzing-traces-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - comprehensive-trace-analysis-utility
    - CTAU
    - Trace Analysis Utilities
  citations:
    - file: examples-analyzing-traces-databricks-on-aws.md
title: Comprehensive Trace Analysis Utility
description: Pattern for building a complete trace analyzer that extracts basic info, tags, token usage, span types, retrieval metrics, assessments, performance breakdown, and data flow from a trace.
tags:
  - mlflow
  - tracing
  - analytics
  - observability
timestamp: "2026-06-19T18:44:42.559Z"
---

---
title: Comprehensive Trace Analysis Utility
summary: Building reusable analysis functions that extract basic information, tags, token usage, span types, errors, retrieval metrics, assessments, performance breakdowns, and data flow from a trace.
sources:
  - examples-analyzing-traces-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T12:00:00.000Z"
updatedAt: "2026-06-19T12:00:00.000Z"
tags:
  - mlflow
  - analysis
  - tracing
  - utilities
aliases:
  - comprehensive-trace-analysis-utility
  - CTAU
confidence: 0.99
provenanceState: extracted
inferredParagraphs: 0
---

# Comprehensive Trace Analysis Utility

The **Comprehensive Trace Analysis Utility** is a programmatic pattern for extracting all meaningful information from a [GenAI](/concepts/mlflow-genai-evaluate-api.md) trace in [MLflow](/concepts/mlflow.md). It provides a structured method for analyzing trace data, including performance metrics, error patterns, token usage, span hierarchies, and assessment summaries. ^[examples-analyzing-traces-databricks-on-aws.md]

## Overview

A comprehensive trace analysis utility consolidates multiple analysis dimensions into a single function or reusable class. The canonical implementation uses `mlflow.get_trace()` to retrieve a trace by its ID and then extracts information across several categories: basic metadata, tags, token usage, span analysis, retrieval metrics, assessments, performance breakdowns, and data flow. ^[examples-analyzing-traces-databricks-on-aws.md]

## Core Implementation (Function-Based)

The utility is typically implemented as a function that accepts a `trace_id` parameter and returns the analyzed trace object, with analysis organized into distinct sections. ^[examples-analyzing-traces-databricks-on-aws.md]

### Basic Information

The utility first retrieves the trace's fundamental properties:
- **State**: Whether the trace completed successfully or encountered an error (`trace.info.state`)
- **Duration**: Total execution time in milliseconds (`trace.info.execution_duration`)
- **Start time**: The timestamp when the trace began, converted from milliseconds to a human-readable format using `datetime.datetime.fromtimestamp()`
- **Experiment**: The associated experiment ID, if available
- **Request/Response previews**: Short text snippets showing the inputs and outputs for quick context

^[examples-analyzing-traces-databricks-on-aws.md]

### Tags Analysis

The utility iterates through all tags stored in `trace.info.tags`, displaying each key-value pair in sorted order. Tags provide contextual metadata such as environment, version, user IDs, and session identifiers. ^[examples-analyzing-traces-databricks-on-aws.md]

### Token Usage

Token usage is extracted primarily from `trace.info.token_usage`, which provides `input_tokens`, `output_tokens`, and `total_tokens`. The utility also calculates token usage independently by iterating through spans of type `CHAT_MODEL` and summing their `llm.token_usage.input_tokens` and `llm.token_usage.output_tokens` attributes, providing a cross-reference for verification. ^[examples-analyzing-traces-databricks-on-aws.md]

### Span Analysis

The span analysis section performs several tasks:
- **Counts spans by type**, showing how many spans of each SpanType (e.g., CHAIN, RETRIEVER, CHAT_MODEL, TOOL) are present in the trace
- **Identifies error spans** by checking each span's `status.status_code.name` for `ERROR` values, collecting the span name and status description

^[examples-analyzing-traces-databricks-on-aws.md]

### Retrieval Analysis

When the trace contains spans of type `RETRIEVER`, the utility examines their outputs to extract retrieval quality metrics. For each retriever span, it shows the number of documents retrieved and, for the first three documents, their `doc_uri` (source location) and `relevance_score`. ^[examples-analyzing-traces-databricks-on-aws.md]

### Assessment Summary

Assessments are collected via `trace.search_assessments()` and grouped by source type (e.g., `HUMAN`, `LLM_JUDGE`, `CODE`). For each assessment, the utility displays the assessment name, value, and an optional rationale (truncated to 50 characters). This enables quick review of human feedback and [LLM judge evaluations](/concepts/llm-as-a-judge-evaluation.md). ^[examples-analyzing-traces-databricks-on-aws.md]

### Performance Breakdown

The utility calculates time distribution across span types by first identifying the root span (the span with no parent, found by checking `span.parent_id is None`). It then sums the duration (in milliseconds) of all spans grouped by type, computing each type's percentage of the total root span duration. This reveals which components are performance bottlenecks. ^[examples-analyzing-traces-databricks-on-aws.md]

### Data Flow

If the trace contains intermediate outputs (`trace.data.intermediate_outputs`), the utility displays each output along with its name. Outputs over 100 characters are truncated. ^[examples-analyzing-traces-databricks-on-aws.md]

## Reusable TraceAnalyzer Class

For more advanced use cases, the pattern is encapsulated in a `TraceAnalyzer` class that accepts a `mlflow.entities.Trace` object and provides multiple analysis methods. ^[examples-analyzing-traces-databricks-on-aws.md]

### Error Summary (get_error_summary)

The `get_error_summary()` method checks three levels of errors:
- **Trace-level**: If the trace's state is `"ERROR"`, it reports the trace failure with the response preview
- **Span-level**: Each span with an `ERROR` status code is reported with its name, type, and description
- **Assessment-level**: Assessments that have an `error` property are included

This multi-level check ensures that errors at any layer are captured. ^[examples-analyzing-traces-databricks-on-aws.md]

### LLM Usage Summary (get_llm_usage_summary)

The `get_llm_usage_summary()` method aggregates usage across all spans with `SpanType.CHAT_MODEL` or type `"LLM"`. It calculates total calls, input tokens, output tokens, and total tokens, and provides per-span breakdowns. ^[examples-analyzing-traces-databricks-on-aws.md]

### Retrieval Metrics (get_retrieval_metrics)

The `get_retrieval_metrics()` method scans all `RETRIEVER`-type spans and computes for each:
- Number of documents retrieved
- Average, maximum, and minimum relevance scores among retrieved documents

^[examples-analyzing-traces-databricks-on-aws.md]

### Span Hierarchy (get_span_hierarchy)

The `get_span_hierarchy()` method builds a tree structure of spans by identifying root spans and recursively finding their children. Each node reports the span name, type, duration in milliseconds, and status. This provides a visual representation of the execution flow. ^[examples-analyzing-traces-databricks-on-aws.md]

### Evaluation Data Export (export_for_evaluation)

The `export_for_evaluation()` method converts trace data into a format suitable for [Evaluation Dataset](/concepts/evaluation-dataset.md) creation. It extracts:
- The request (inputs) and response (outputs) from the root span
- Expected values from assessment expectations (retrieved via `trace.search_assessments(type="expectation")`)
- Retrieved context from `RETRIEVER` spans (specifically `page_content` fields)
- Metadata including user ID, session ID, duration, and timestamp

^[examples-analyzing-traces-databricks-on-aws.md]

## Error Monitoring

The utility pattern can be extended to monitor errors across multiple traces. By using `mlflow.search_traces()` with the filter `trace.status = 'ERROR'` and a time window, the function groups errors by function name (from the `tags.mlflow.traceName` tag) and shows the most recent error samples with request previews and timestamps. ^[examples-analyzing-traces-databricks-on-aws.md]

## Performance Monitoring

Performance analysis functions can compute latency percentiles (P50, P95, P99) across a set of traces using `traces['execution_time_ms'].describe()`. By defining a percentile threshold such as P99, the utility can identify outlier traces that represent performance anomalies. ^[examples-analyzing-traces-databricks-on-aws.md]

## Feature Flag Analysis

The utility pattern supports comparing performance between different feature flag states. By searching traces with filter strings like `metadata.feature_flag_<name> = 'false'` versus `'true'`, analysts can measure average latency differences between control and treatment groups. ^[examples-analyzing-traces-databricks-on-aws.md]

## Best Practices

- **Use a class-based approach** for reusability, encapsulating analysis logic in methods like `get_error_summary()` and `get_retrieval_metrics()`
- **Cross-reference token counts** by comparing `trace.info.token_usage` against aggregated span-level token attributes
- **Convert timestamps to human-readable formats** using `datetime.datetime.fromtimestamp()` for easier interpretation
- **Truncate long output previews** to improve readability in analysis summaries
- **Combine trace-level and span-level error checks** to capture failures at every layer of the execution

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The underlying observability framework for GenAI applications
- Span Analysis Methods — Techniques for analyzing individual spans within traces
- [Token Usage Tracking](/concepts/mlflow-token-usage-tracking.md) — Monitoring LLM token consumption across spans
- Retrieval Quality Metrics — Evaluating document retrieval performance
- Human Feedback Logging — Adding human assessments to traces
- [LLM Judge Evaluations](/concepts/llm-as-a-judge-evaluation.md) — Programmatic quality scoring using LLMs
- [Feature Flag Performance Analysis](/concepts/feature-flag-performance-analysis-with-traces.md) — A/B testing with trace metadata
- mlflow.search_traces() API|Search Traces Programmatically — The `mlflow.search_traces()` API
- [Build Evaluation Datasets from Traces](/concepts/evaluation-datasets.md) — Converting trace data for model evaluation

## Sources

- examples-analyzing-traces-databricks-on-aws.md

# Citations

1. [examples-analyzing-traces-databricks-on-aws.md](/references/examples-analyzing-traces-databricks-on-aws-ebc17f1a.md)
