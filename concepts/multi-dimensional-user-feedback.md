---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8f3cda69bc444e4abcdf0a901039605dceae5667b9816c73e750e7ac8cf9b3db
  pageDirectory: concepts
  sources:
    - collect-user-feedback-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-dimensional-user-feedback
    - MUF
    - User Feedback
    - user feedback
  citations:
    - file: collect-user-feedback-databricks-on-aws.md
title: Multi-Dimensional User Feedback
description: Logging separate assessments for different quality dimensions (accuracy, helpfulness, relevance) to enable granular analysis
tags:
  - mlflow
  - feedback
  - evaluation
timestamp: "2026-06-19T17:46:18.577Z"
---

# Multi-Dimensional User Feedback

**Multi-Dimensional User Feedback** refers to the practice of collecting separate ratings for distinct quality aspects of a GenAI application’s response—such as accuracy, helpfulness, and relevance—rather than a single binary or scalar score. Logging each dimension as an independent assessment on a trace enables granular analysis and targeted improvements. ^[collect-user-feedback-databricks-on-aws.md]

## Overview

In production [MLflow GenAI](/concepts/mlflow-3-for-genai.md) systems, understanding *why* a user was dissatisfied requires more than a thumbs-up or thumbs-down. Multi-dimensional feedback captures the user’s perception across multiple facets of quality, allowing teams to pinpoint specific weaknesses—for example, low accuracy but high relevance. Each dimension is logged as a separate assessment, making it possible to compute per‑dimension averages and track trends over time. ^[collect-user-feedback-databricks-on-aws.md]

## Prerequisites

Collecting multi-dimensional user feedback requires:

- MLflow 3 (MLflow 2.x is not supported due to performance and feature limitations).  
- The `mlflow-tracing` package for production use, or the full `mlflow` package for development.  
- The `log_feedback` API, available in both packages.

^[collect-user-feedback-databricks-on-aws.md]

## Implementation

Multi-dimensional feedback is typically collected through a dedicated endpoint that receives separate scores for each quality dimension. The example below logs three dimensions (accuracy, helpfulness, relevance) as individual assessments, each normalised to a 0–1 scale. ^[collect-user-feedback-databricks-on-aws.md]

```python
from mlflow.entities import AssessmentSource

@app.post("/detailed-feedback")
def submit_detailed_feedback(
    trace_id: str,
    accuracy: int = Query(..., ge=1, le=5),
    helpfulness: int = Query(..., ge=1, le=5),
    relevance: int = Query(..., ge=1, le=5),
    user_id: str = Query(...),
    comment: Optional[str] = None):
    dimensions = {
        "accuracy": accuracy,
        "helpfulness": helpfulness,
        "relevance": relevance
    }
    for dimension, score in dimensions.items():
        mlflow.log_feedback(
            trace_id=trace_id,
            name=f"user_{dimension}",
            value=score / 5.0,
            source=AssessmentSource(
                source_type="HUMAN",
                source_id=user_id
            ),
            rationale=comment if dimension == "accuracy" else None
        )
    return {"status": "success", "feedback_recorded": dimensions}
```

Each call to `log_feedback` creates a separate assessment that is permanently attached to the trace. The assessment name (e.g., `user_accuracy`, `user_helpfulness`) distinguishes the dimension. ^[collect-user-feedback-databricks-on-aws.md]

## Analyzing Multi-Dimensional Feedback

After collection, traces can be queried and analysed using the MLflow Client SDK. The following function extracts ratings per dimension and computes averages: ^[collect-user-feedback-databricks-on-aws.md]

```python
def analyze_ratings(traces):
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
```

This pattern enables dashboards that display per‑dimension satisfaction scores, highlight dimensions with the lowest average ratings, and track improvement after changes to the agent. ^[collect-user-feedback-databricks-on-aws.md]

## Best Practices

- **Define a consistent set of dimensions** relevant to your application (e.g., accuracy, helpfulness, relevance, tone).  
- **Normalise scores** to a 0–1 scale for easier aggregation.  
- **Log each dimension as a separate assessment** using a structured naming convention (`user_{dimension}`).  
- **Include a rationale only on one dimension** to avoid duplication.  
- **Query traces periodically** using the SDK to build monitoring dashboards.  
- **Use multi-dimensional feedback to build evaluation datasets** that are balanced across poor‑performing dimensions.

## Related Concepts

- [User Feedback](/concepts/multi-dimensional-user-feedback.md) – The general mechanism for collecting human evaluations on traces.  
- [Trace Assessments](/concepts/trace-assessments.md) – The data entity that stores feedback, including multi-dimensional ratings.  
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying judges and collecting feedback for continuous quality monitoring.  
- [Evaluation Datasets](/concepts/evaluation-datasets.md) – Using collected feedback to create ground‑truth test cases.  
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The platform that provides the tracing, feedback, and evaluation APIs.

## Sources

- collect-user-feedback-databricks-on-aws.md

# Citations

1. [collect-user-feedback-databricks-on-aws.md](/references/collect-user-feedback-databricks-on-aws-0b0ba83c.md)
