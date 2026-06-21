---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cfc28e87733e90ae645c0c631c47250642526ec142ac9e8d0cb42170d95a7a96
  pageDirectory: concepts
  sources:
    - collect-user-feedback-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-dimensional-feedback-assessment
    - MFA
  citations:
    - file: collect-user-feedback-databricks-on-aws.md
title: Multi-Dimensional Feedback Assessment
description: Collecting separate ratings for different quality dimensions (accuracy, helpfulness, relevance) and logging each as an individual assessment on a single trace.
tags:
  - mlflow
  - genai
  - feedback
  - evaluation
timestamp: "2026-06-19T09:17:00.407Z"
---

# Multi-Dimensional Feedback Assessment

**Multi-Dimensional Feedback Assessment** is a structured approach to collecting user feedback on GenAI application outputs by capturing separate ratings for distinct quality dimensions such as accuracy, helpfulness, and relevance. Instead of a single thumbs-up or thumbs-down, each dimension is logged as an independent assessment, enabling granular analysis of application performance. ^[collect-user-feedback-databricks-on-aws.md]

## Overview

Collecting single-dimensional feedback (e.g., “Was this response correct?”) provides a coarse quality signal. Multi-dimensional feedback breaks quality into separate axes, allowing teams to identify which aspects of an agent’s behavior need improvement. In MLflow, each dimension is stored as a separate [Assessment](/concepts/assessments.md) on the trace, using the `mlflow.log_feedback()` API with a unique name per dimension (e.g., `user_accuracy`, `user_helpfulness`). ^[collect-user-feedback-databricks-on-aws.md]

## Implementation Example

The following endpoint demonstrates how to collect multi-dimensional feedback. Each dimension (accuracy, helpfulness, relevance) is logged as a separate assessment, with values normalized to a 0–1 scale. The `AssessmentSource` records the human user providing the feedback. ^[collect-user-feedback-databricks-on-aws.md]

```python
from mlflow.entities import AssessmentSource

@app.post("/detailed-feedback")
def submit_detailed_feedback(
    trace_id: str,
    accuracy: int = Query(..., ge=1, le=5, description="Accuracy rating from 1-5"),
    helpfulness: int = Query(..., ge=1, le=5, description="Helpfulness rating from 1-5"),
    relevance: int = Query(..., ge=1, le=5, description="Relevance rating from 1-5"),
    user_id: str = Query(..., description="User identifier"),
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
            value=score / 5.0,  # Normalize to 0-1 scale
            source=AssessmentSource(
                source_type="HUMAN",
                source_id=user_id
            ),
            rationale=comment if dimension == "accuracy" else None
        )
    return {"status": "success", "trace_id": trace_id, "feedback_recorded": dimensions}
```

## Analyzing Multi-Dimensional Feedback

After collection, you can retrieve traces and aggregate ratings per dimension. The following function computes average scores for each dimension across a set of traces: ^[collect-user-feedback-databricks-on-aws.md]

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

This analysis can be used to track quality trends over time and to identify dimensions that consistently score low, guiding development priorities.

## Benefits

- **Granular insight**: Understand exactly which quality aspect (accuracy vs. helpfulness vs. relevance) underperforms.
- **Targeted improvement**: Focus engineering effort on the weakest dimensions.
- **Consistent tracking**: Compare dimension scores across different agent configurations or over time.
- **Integration with monitoring**: Feed dimension scores into [production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) dashboards.

## Related Concepts

- [User Feedback Collection](/concepts/end-user-feedback-collection-via-sdk.md) – The general mechanism for logging feedback on traces.
- [Assessments](/concepts/assessments.md) – The data entity that stores feedback values.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – Using multi-dimensional feedback to compare agent variants.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Applying ongoing quality monitoring with feedback data.
- [Custom Judges](/concepts/custom-judges.md) – LLM-based judges that score similar dimensions automatically.

## Sources

- collect-user-feedback-databricks-on-aws.md

# Citations

1. [collect-user-feedback-databricks-on-aws.md](/references/collect-user-feedback-databricks-on-aws-0b0ba83c.md)
