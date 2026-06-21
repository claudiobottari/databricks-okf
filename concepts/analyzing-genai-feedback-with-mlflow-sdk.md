---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8f01683fd4071f0f8eeb1be4b04eda19bc3b5e7e56a7590529864c20ede1e3dc
  pageDirectory: concepts
  sources:
    - collect-user-feedback-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - analyzing-genai-feedback-with-mlflow-sdk
    - AGFWMS
  citations:
    - file: collect-user-feedback-databricks-on-aws.md
title: Analyzing GenAI Feedback with MLflow SDK
description: Using MlflowClient to search traces, retrieve assessments, and compute feedback metrics (feedback rate, positive rate, per-dimension averages) from production data.
tags:
  - mlflow
  - genai
  - analytics
  - sdk
timestamp: "2026-06-19T09:17:18.224Z"
---

## Analyzing GenAI Feedback with MLflow SDK

Once user feedback has been collected against GenAI application traces, the MLflow SDK provides programmatic methods to retrieve, aggregate, and interpret that feedback. Analysis of feedback data helps teams understand real-world quality, detect regressions, and build evaluation datasets from production interactions. ^[collect-user-feedback-databricks-on-aws.md]

### Prerequisites

The `log_feedback` and analysis APIs require **MLflow 3**. The `mlflow-tracing` package (recommended for production) or the core MLflow package both support feedback analysis. ^[collect-user-feedback-databricks-on-aws.md]

### Getting Traces with Feedback

To analyze feedback, first retrieve traces from a specific time window using the `MlflowClient.search_traces()` method. Each returned trace object can then be expanded to include its attached assessments (feedback). ^[collect-user-feedback-databricks-on-aws.md]

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

After obtaining a list of traces, call `client.get_trace(trace.info.trace_id)` to retrieve the full trace details, including the `assessments` attribute that holds feedback entries. ^[collect-user-feedback-databricks-on-aws.md]

### Analyzing Feedback Patterns

The SDK can be used to compute aggregate metrics such as feedback submission rate and positive/negative ratio. The following function demonstrates how to iterate over traces, count feedback by value, and derive summary statistics: ^[collect-user-feedback-databricks-on-aws.md]

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

    feedback_rate = (traces_with_feedback / total_traces * 100) if traces_with_feedback > 0 else 0
    positive_rate = (positive_count / traces_with_feedback * 100) if traces_with_feedback > 0 else 0

    return {
        "total_traces": total_traces,
        "traces_with_feedback": traces_with_feedback,
        "feedback_rate": feedback_rate,
        "positive_rate": positive_rate,
        "positive_count": positive_count,
        "negative_count": negative_count
    }
```

### Analyzing Multi‑Dimensional Feedback

If your application collects separate ratings for dimensions such as accuracy, helpfulness, and relevance, the SDK can average scores per dimension. Each dimension is stored as a distinct assessment with a `name` like `user_accuracy` or `user_helpfulness`. ^[collect-user-feedback-databricks-on-aws.md]

```python
def analyze_ratings(traces):
    """Analyze rating-based feedback by dimension."""
    client = MlflowClient()
    ratings_by_dimension = {}

    for trace in traces:
        trace_detail = client.get_trace(trace.info.trace_id)
        if trace_detail.data.assessments:
            for assessment in trace_detail.data.assessments:
                if assessment.name.startswith("user_") and assessment.name != "user_feedback":
                    dimension = assessment.name.replace("user_", "")
                    ratings_by_dimension.setdefault(dimension, []).append(assessment.value)

    return {
        dim: sum(scores) / len(scores)
        for dim, scores in ratings_by_dimension.items()
        if scores
    }
```

### Viewing Feedback in the Trace UI

Feedback is also visible in the MLflow Trace UI. Each trace displays its attached assessments, making it easy to inspect individual instances of positive or negative feedback alongside the full execution trace. ^[collect-user-feedback-databricks-on-aws.md]

### Related Concepts

- Collecting User Feedback on Traces
- [Trace Assessments](/concepts/trace-assessments.md)
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md)
- GenAI Quality Monitoring
- Building Evaluation Datasets from Feedback

### Sources

- collect-user-feedback-databricks-on-aws.md

# Citations

1. [collect-user-feedback-databricks-on-aws.md](/references/collect-user-feedback-databricks-on-aws-0b0ba83c.md)
