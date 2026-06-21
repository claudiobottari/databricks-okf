---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 27a141487e1d35d7331575f097b39c5911183ff10542b96237da16c977be2748
  pageDirectory: concepts
  sources:
    - collect-user-feedback-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feedback-analysis-and-monitoring-with-mlflow-sdk
    - Monitoring with MLflow SDK and Feedback Analysis
    - FAAMWMS
  citations:
    - file: collect-user-feedback-databricks-on-aws.md
title: Feedback Analysis and Monitoring with MLflow SDK
description: Using the MLflow SDK to query traces, extract feedback assessments, calculate metrics like feedback rate and positive rate, and analyze multi-dimensional ratings over time windows.
tags:
  - mlflow
  - analytics
  - monitoring
  - sdk
timestamp: "2026-06-19T14:18:04.897Z"
---

# Feedback Analysis and Monitoring with MLflow SDK

**Feedback Analysis and Monitoring with MLflow SDK** refers to the process of using `mlflow.client.MlflowClient` to retrieve traces, extract user feedback stored as assessments, and derive quality metrics from production GenAI applications. The SDK provides programmatic access to feedback data logged via `mlflow.log_feedback()`, enabling teams to build dashboards, trigger alerts, and track satisfaction trends over time.^[collect-user-feedback-databricks-on-aws.md]

## Prerequisites

To collect and analyze user feedback, MLflow 3 is required. MLflow 2.x is not supported due to performance limitations and missing features essential for production use. For production deployments, install the `mlflow-tracing` package, which is optimized with minimal dependencies and better performance characteristics. The `log_feedback` API is available in both the standard `mlflow` package and `mlflow-tracing`, so you can collect user feedback regardless of which installation method you choose.^[collect-user-feedback-databricks-on-aws.md]

```bash
pip install --upgrade mlflow-tracing
```

## Retrieving Traces with Feedback

To analyze feedback, first retrieve traces from a specific time window using `MlflowClient.search_traces()`. This returns trace summaries that can then be expanded to include assessment data.^[collect-user-feedback-databricks-on-aws.md]

```python
from mlflow.client import MlflowClient
from datetime import datetime, timedelta

def get_recent_traces(experiment_name: str, hours: int = 24):
    """Get traces from the last N hours."""
    client = MlflowClient()
    cutoff_time = datetime.now() - timedelta(hours=hours)
    cutoff_timestamp_ms = int(cutoff_time.timestamp() * 1000)

    traces = client.search_traces(
        experiment_names=[experiment_name],
        filter_string=f"trace.timestamp_ms > {cutoff_timestamp_ms}"
    )
    return traces
```

Once you have trace summaries, use `client.get_trace(trace_id)` to retrieve full trace details including assessments. The `trace.data.assessments` field contains all feedback objects attached to that trace.^[collect-user-feedback-databricks-on-aws.md]

## Analyzing Feedback Patterns

You can analyze feedback patterns by iterating over traces, extracting assessments, and computing metrics such as feedback rate and positive/negative ratios.^[collect-user-feedback-databricks-on-aws.md]

```python
def analyze_user_feedback(traces):
    """Analyze feedback patterns from traces."""
    client = MlflowClient()

    total_traces = len(traces)
    traces_with_feedback = 0
    positive_count = 0
    negative_count = 0

    for trace in traces:
        trace_detail = client.get_trace(trace.info.trace_id)
        if trace_detail.data.assessments:
            traces_with_feedback += 1
            for assessment in trace_detail.data.assessments:
                if assessment.name == "user_feedback":
                    if assessment.value:
                        positive_count += 1
                    else:
                        negative_count += 1

    if traces_with_feedback > 0:
        feedback_rate = (traces_with_feedback / total_traces) * 100
        positive_rate = (positive_count / traces_with_feedback) * 100
    else:
        feedback_rate = 0
        positive_rate = 0

    return {
        "total_traces": total_traces,
        "traces_with_feedback": traces_with_feedback,
        "feedback_rate": feedback_rate,
        "positive_rate": positive_rate,
        "positive_count": positive_count,
        "negative_count": negative_count
    }

traces = get_recent_traces("/Shared/production-genai-app", hours=24)
results = analyze_user_feedback(traces)
print(f"Feedback rate: {results['feedback_rate']:.1f}%")
print(f"Positive feedback: {results['positive_rate']:.1f}%")
```

## Analyzing Multi-Dimensional Feedback

When you collect feedback with multiple rating dimensions (e.g., accuracy, helpfulness, relevance), each dimension is logged as a separate assessment. You can compute average ratings per dimension across all traces.^[collect-user-feedback-databricks-on-aws.md]

```python
def analyze_ratings(traces):
    """Analyze rating-based feedback."""
    client = MlflowClient()
    ratings_by_dimension = {}

    for trace in traces:
        trace_detail = client.get_trace(trace.info.trace_id)
        if trace_detail.data.assessments:
            for assessment in trace_detail.data.assessments:
                if assessment.name.startswith("user_") and assessment.name != "user_feedback":
                    dimension = assessment.name.replace("user_", "")
                    if dimension not in ratings_by_dimension:
                        ratings_by_dimension[dimension] = []
                    ratings_by_dimension[dimension].append(assessment.value)

    average_ratings = {}
    for dimension, scores in ratings_by_dimension.items():
        if scores:
            average_ratings[dimension] = sum(scores) / len(scores)

    return average_ratings

ratings = analyze_ratings(traces)
for dimension, avg_score in ratings.items():
    print(f"{dimension}: {avg_score:.2f}/1.0")
```

## Feedback Data Model

User feedback is captured using the **Feedback** entity, which is a type of [Assessment (MLflow GenAI)](/concepts/assessments-mlflow-genai.md) that can be attached to traces or specific spans. The Feedback entity provides structured storage for:^[collect-user-feedback-databricks-on-aws.md]

- **Value**: The actual feedback (boolean, numeric, text, or structured data)
- **Source**: Information about who or what provided the feedback (human user, LLM judge, or code), represented as an `AssessmentSource` object with `source_type` (e.g., `"HUMAN"` or `"LLM_JUDGE"`) and `source_id` (identifying the specific user or system)
- **Rationale**: Optional explanation for the feedback
- **Metadata**: Additional context like timestamps or custom attributes

When using `mlflow.log_feedback()`, the feedback is stored as an assessment on the trace, permanently associating it with the specific interaction. It can be queried alongside the trace data and is visible in the MLflow UI when viewing the trace.^[collect-user-feedback-databricks-on-aws.md]

## Viewing Feedback in the Trace UI

![Trace assessments UI](https://assets.docs.databricks.com/_static/images/mlflow3-genai/tracing/trace-assessment-ui.gif)^[collect-user-feedback-databricks-on-aws.md]

The MLflow Trace UI provides a visual interface for inspecting feedback attached to individual traces. Assessment values, rationales, and source information are displayed alongside the trace timeline.^[collect-user-feedback-databricks-on-aws.md]

## Related Concepts

- MlflowClient – The SDK client used for trace and assessment retrieval
- Trace (MLflow) – The execution record on which feedback assessments are stored
- [Assessment (MLflow GenAI)](/concepts/assessments-mlflow-genai.md) – The data model underlying user feedback
- MLflow log_feedback API|Log User Feedback – The API used to record feedback from production
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Using feedback data to monitor application quality over time

## Sources

- collect-user-feedback-databricks-on-aws.md

# Citations

1. [collect-user-feedback-databricks-on-aws.md](/references/collect-user-feedback-databricks-on-aws-0b0ba83c.md)
