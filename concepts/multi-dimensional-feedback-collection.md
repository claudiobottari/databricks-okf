---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c5cef343ee7777179dcdc2dcb05195ecb9a05eddbf5e3268467232b89fa7421
  pageDirectory: concepts
  sources:
    - collect-user-feedback-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-dimensional-feedback-collection
    - MFC
  citations:
    - file: collect-user-feedback-databricks-on-aws.md
title: Multi-Dimensional Feedback Collection
description: Collecting feedback across multiple rating dimensions (e.g., accuracy, helpfulness, relevance) by logging each as a separate assessment with normalized scores, enabling granular quality analysis.
tags:
  - mlflow
  - feedback
  - ratings
  - evaluation
timestamp: "2026-06-19T14:16:37.397Z"
---

```markdown
# Multi-Dimensional Feedback Collection

**Multi-dimensional feedback collection** is an approach to capturing user feedback in which separate ratings are collected for different quality aspects of a GenAI application’s response — such as accuracy, helpfulness, and relevance — rather than a single thumbs-up/thumbs-down. By logging each dimension as a separate [[Assessments (MLflow GenAI)|Assessment (MLflow)]] entity on a Trace (MLflow), MLflow enables granular analysis and targeted improvement.^[collect-user-feedback-databricks-on-aws.md]

## Why Multi-Dimensional Feedback

User feedback provides ground truth about an application’s performance. Multi-dimensional feedback supports the following key goals:^[collect-user-feedback-databricks-on-aws.md]

- **Real-world quality signals** — Understand how actual users perceive different aspects of the application’s outputs.
- **Continuous improvement** — Identify patterns in negative feedback to guide development.
- **Training data creation** — Build high-quality evaluation datasets from production feedback.
- **Quality monitoring** — Track satisfaction metrics over time and across user segments.
- **Model fine-tuning** — Leverage feedback data to improve underlying models.

## Data Model

In MLflow, each feedback dimension is logged as a separate **Feedback** entity (a type of Assessment) attached to the same trace. This allows each aspect to be queried independently. The Feedback entity stores:^[collect-user-feedback-databricks-on-aws.md]

- **Value** — The rating for that dimension (boolean, numeric, or structured data).
- **Name** — A unique identifier for the dimension (e.g., `user_accuracy`, `user_helpfulness`).
- **Source** — Who or what provided the feedback, using `AssessmentSource` with `source_type = "HUMAN"`.
- **Rationale** — Optional explanatory comment, typically attached to the primary dimension.
- **Metadata** — Additional context such as timestamps or custom attributes.

## Implementation

### Backend Example

The following example logs three separate dimensions — accuracy, helpfulness, and relevance — each on a 1–5 scale, normalized to a 0–1 range for consistency:^[collect-user-feedback-databricks-on-aws.md]

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
    """Collect multi-dimensional feedback with separate ratings for different aspects.
    Each aspect is logged as a separate assessment for granular analysis."""
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
    return {
        "status": "success",
        "trace_id": trace_id,
        "feedback_recorded": dimensions
    }
```

### Frontend Considerations

The front end submits multiple rating values in a single request. For streaming responses, the trace ID is only available after the stream completes; feedback controls should remain disabled until the trace ID is received.^[collect-user-feedback-databricks-on-aws.md]

## Analyzing Multi-Dimensional Feedback

Once collected, dimension-level ratings can be extracted and analyzed independently:^[collect-user-feedback-databricks-on-aws.md]

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
```

## Best Practices

- **Normalize ratings** — Convert raw scales (e.g., 1–5) to a 0–1 range for consistent comparison across dimensions.^[collect-user-feedback-databricks-on-aws.md]
- **Attach rationale to one dimension** — Include the user’s explanatory comment on only the primary dimension to avoid data duplication.^[collect-user-feedback-databricks-on-aws.md]
- **Name dimensions consistently** — Use a prefix like `user_` to distinguish human feedback from LLM-judge or code-based assessments.^[collect-user-feedback-databricks-on-aws.md]
- **Log each dimension as a separate assessment** — This enables independent querying and aggregation per dimension.^[collect-user-feedback-databricks-on-aws.md]
- **Delay feedback UI for streaming** — In streaming responses, disable feedback controls until the trace ID is received after the stream completes.^[collect-user-feedback-databricks-on-aws.md]

## Related Concepts

- Feedback (MLflow) — The structured output object for feedback values.
- [[AssessmentSource Entity|AssessmentSource]] — Identifies the provider of feedback (human, LLM judge, or code).
- [[Assessments (MLflow GenAI)|Assessment (MLflow)]] — The entity type for feedback stored on traces.
- End-user feedback collection — General patterns for collecting feedback in production.
- Trace (MLflow) — The interaction record to which feedback is attached.
- [[Production monitoring]] — Monitoring quality metrics based on collected feedback.

## Sources

- collect-user-feedback-databricks-on-aws.md
```

# Citations

1. [collect-user-feedback-databricks-on-aws.md](/references/collect-user-feedback-databricks-on-aws-0b0ba83c.md)
