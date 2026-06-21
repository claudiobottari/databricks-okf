---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bff4e2028d2568faa61330a06cf85734cdf62e879416ebbdc9f463fed69a2f72
  pageDirectory: concepts
  sources:
    - examples-analyzing-traces-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-assessments-and-feedback
    - Feedback and Trace Assessments
    - TAAF
    - trace-assessments-and-feedback-logging
    - Feedback Logging and Trace Assessments
    - TAAFL
  citations:
    - file: examples-analyzing-traces-databricks-on-aws.md
title: Trace Assessments and Feedback
description: Logging human feedback, LLM judge evaluations, ground truth expectations, and span-specific assessments to MLflow traces using log_feedback() and log_expectation().
tags:
  - mlflow
  - evaluation
  - feedback
  - tracing
timestamp: "2026-06-19T10:25:53.001Z"
---

# Trace Assessments and Feedback

**Trace Assessments and Feedback** refer to the mechanism in [MLflow Tracing](/concepts/mlflow-tracing.md) that allows you to attach qualitative and quantitative evaluations to a [Trace](/concepts/traces.md) — including human judgments, LLM-generated scores, expected outcomes, and span-level annotations. These assessments provide the structured signal needed to monitor, debug, and improve [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications in production.

## Overview

Assessments enable you to capture evaluation data directly on a trace after execution. They are stored as part of the trace and can be retrieved programmatically for analysis. MLflow supports three kinds of assessment objects: feedback (scores or qualitative ratings), expectations (ground-truth facts), and span-specific annotations. ^[examples-analyzing-traces-databricks-on-aws.md]

## Types of Assessments

| Type | Purpose | Example |
|------|---------|---------|
| **Human feedback** | A human evaluator rates the trace’s output. | `mlflow.log_feedback(trace_id, name="helpfulness", value=4, source=Human(...))` |
| **LLM judge assessment** | An automated LLM judge scores the trace. | `mlflow.log_feedback(trace_id, name="relevance_score", value=0.92, source=LLMJudge(...))` |
| **Expectation** | Ground-truth facts the trace output should contain. | `mlflow.log_expectation(trace_id, name="expected_facts", value=["observability", "spans"])` |
| **Span-specific feedback** | Feedback attached to a particular Span rather than the whole trace. | `mlflow.log_feedback(trace_id, span_id=span.span_id, name="retrieval_quality", value="excellent")` |

^[examples-analyzing-traces-databricks-on-aws.md]

## Logging Assessments

Use `mlflow.log_feedback()` to log human or LLM judge feedback, and `mlflow.log_expectation()` to log expected facts. Each function requires a `trace_id`, a source (with `source_type` — `HUMAN`, `LLM_JUDGE`, or `CODE` — and a `source_id` for identification), and the assessment `value`. An optional `rationale` provides explanation. For span-specific feedback, pass the `span_id` parameter. ^[examples-analyzing-traces-databricks-on-aws.md]

```python
# Human feedback on overall trace
mlflow.log_feedback(
    trace_id=trace_id,
    name="helpfulness",
    value=4,
    source=AssessmentSource(
        source_type=AssessmentSourceType.HUMAN,
        source_id="reviewer_alice@company.com"
    ),
    rationale="Clear and accurate response with good context usage"
)

# LLM judge assessment with metadata
mlflow.log_feedback(
    trace_id=trace_id,
    name="relevance_score",
    value=0.92,
    source=AssessmentSource(
        source_type=AssessmentSourceType.LLM_JUDGE,
        source_id="gpt-4-evaluator"
    ),
    metadata={"evaluation_prompt_version": "v2.1"}
)

# Ground-truth expectation
mlflow.log_expectation(
    trace_id=trace_id,
    name="expected_facts",
    value=["observability", "spans", "GenAI applications"],
    source=AssessmentSource(
        source_type=AssessmentSourceType.HUMAN,
        source_id="subject_matter_expert"
    )
)

# Span-specific feedback
mlflow.log_feedback(
    trace_id=trace_id,
    span_id=retriever_span.span_id,
    name="retrieval_quality",
    value="excellent",
    source=AssessmentSource(
        source_type=AssessmentSourceType.CODE,
        source_id="retrieval_evaluator.py"
    )
)
```

After logging assessments, the trace object must be refreshed (e.g., `trace = mlflow.get_trace(trace_id)`) to include the new data. ^[examples-analyzing-traces-databricks-on-aws.md]

## Retrieving and Analyzing Assessments

Assessments can be retrieved from a trace via `trace.search_assessments()` or from `trace.info.assessments`. A common pattern is to group assessments by `source_type` to separate human feedback from LLM judge scores: ^[examples-analyzing-traces-databricks-on-aws.md]

```python
assessments = trace.search_assessments()
by_source = {}
for assessment in assessments:
    source_type = assessment.source.source_type
    if source_type not in by_source:
        by_source[source_type] = []
    by_source[source_type].append(assessment)

for source_type, items in by_source.items():
    print(f"{source_type} ({len(items)}):")
    for assessment in items:
        value_str = f"{assessment.value}"
        if assessment.rationale:
            value_str += f" - {assessment.rationale[:50]}..."
        print(f"  {assessment.name}: {value_str}")
```

The `TraceAnalyzer` utility class in the source material demonstrates advanced analysis: it can extract error-related assessments, aggregate LLM usage, compute retrieval metrics, and export trace data for evaluation. ^[examples-analyzing-traces-databricks-on-aws.md]

## Use Cases

- **Error monitoring**: Detect spans where assessments flagged errors and correlate with trace-level failures. ^[examples-analyzing-traces-databricks-on-aws.md]
- **Quality dashboards**: Aggregate human and LLM judge scores over time to track application performance. ^[examples-analyzing-traces-databricks-on-aws.md]
- **A/B comparison**: Compare assessment scores across different agent configurations or model versions. ^[examples-analyzing-traces-databricks-on-aws.md]
- **Evaluation dataset creation**: Export assessments (especially expectations) as ground truth for offline evaluation sets. ^[examples-analyzing-traces-databricks-on-aws.md]

## Related Concepts

- [Traces](/concepts/traces.md) – The container for execution information and assessments.
- Spans – Individual units of work within a trace, each of which can receive its own feedback.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – Offline evaluation framework that can consume trace data.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying judges to continuously score traces in production.
- [Custom Judges](/concepts/custom-judges.md) – LLM-based scorers used to create automated assessments.

## Sources

- examples-analyzing-traces-databricks-on-aws.md

# Citations

1. [examples-analyzing-traces-databricks-on-aws.md](/references/examples-analyzing-traces-databricks-on-aws-ebc17f1a.md)
