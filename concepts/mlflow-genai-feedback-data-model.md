---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 714f48e30bf86766f9e053a65c8ee6cb2f47b5e0f9d69e67a74053dc7cf45f19
  pageDirectory: concepts
  sources:
    - collect-user-feedback-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-feedback-data-model
    - MGFDM
  citations:
    - file: collect-user-feedback-databricks-on-aws.md
title: MLflow GenAI Feedback Data Model
description: The structured Feedback entity in MLflow that captures user assessments on traces, including value, source, rationale, and metadata fields.
tags:
  - mlflow
  - genai
  - feedback
  - data-model
timestamp: "2026-06-19T09:16:39.014Z"
---

# MLflow GenAI Feedback Data Model

The **MLflow GenAI Feedback Data Model** defines the structured schema used to capture, store, and analyze user feedback for GenAI applications within the [MLflow Tracing](/concepts/mlflow-tracing.md) system. In MLflow, user feedback is captured using the **Feedback** entity, which is a type of Assessment that can be attached to traces or specific spans. ^[collect-user-feedback-databricks-on-aws.md]

## Overview

The Feedback entity provides a structured way to store evaluation data about GenAI application outputs. Understanding this data model helps you design effective feedback collection systems that integrate seamlessly with MLflow's evaluation and monitoring capabilities. ^[collect-user-feedback-databricks-on-aws.md]

The feedback data model enables several key use cases:
- **Real-world quality signals** — Understanding how actual users perceive your application's outputs
- **Continuous improvement** — Identifying patterns in negative feedback to guide development
- **Training data creation** — Using feedback to build high-quality evaluation datasets
- **Quality monitoring** — Tracking satisfaction metrics over time and across different user segments
- **Model fine-tuning** — Leveraging feedback data to improve your underlying models

^[collect-user-feedback-databricks-on-aws.md]

## Entity Structure

The Feedback entity contains the following fields:

<!-- Field descriptions are inferred from the usage patterns in the source material -->
- **Value**: The actual feedback content — this can be a boolean (e.g., thumbs up/down), numeric (e.g., ratings on a scale), text (e.g., comments), or structured data (e.g., multi-dimensional ratings).
- **Source**: Information about who or what provided the feedback — such as a human user, an LLM judge, or code.
- **Rationale**: An optional explanation for the feedback.
- **Metadata**: Additional context like timestamps or custom attributes.

For detailed information about the Feedback entity schema and all available fields, see the Feedback section in the Span concepts. ^[collect-user-feedback-databricks-on-aws.md]

## AssessmentSource Object

The `AssessmentSource` object identifies who or what provided the feedback: ^[collect-user-feedback-databricks-on-aws.md]

- `source_type`: Can be `"HUMAN"` for user feedback or `"LLM_JUDGE"` for automated evaluation.
- `source_id`: Identifies the specific user or system providing feedback.

## Feedback as Assessments on Traces

Feedback is stored as assessments on the trace, which means: ^[collect-user-feedback-databricks-on-aws.md]

- It is permanently associated with the specific interaction.
- It can be queried alongside the trace data.
- It is visible in the MLflow UI when viewing the trace.

## Types of Feedback

MLflow supports various types of feedback through its assessment system, including boolean feedback (thumbs up/down), numeric ratings, text comments, and structured multi-dimensional feedback. ^[collect-user-feedback-databricks-on-aws.md]

### Multi-Dimensional Feedback Example

You can log separate assessments for different quality dimensions, such as accuracy, helpfulness, and relevance. Each dimension is logged as a separate assessment for granular analysis: ^[collect-user-feedback-databricks-on-aws.md]

```python
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
```

## Feedback Storage and Retrieval

Feedback data is stored as part of the trace record. You can retrieve and analyze feedback by searching for traces and examining their assessments: ^[collect-user-feedback-databricks-on-aws.md]

```python
from mlflow.client import MlflowClient

client = MlflowClient()
trace_detail = client.get_trace(trace_id)
if trace_detail.data.assessments:
    for assessment in trace_detail.data.assessments:
        if assessment.name == "user_feedback":
            # Process feedback value and metadata
            pass
```

## Related Concepts

- Collect User Feedback — Implementation patterns for gathering feedback from end users
- [Traces and Spans](/concepts/trace-spans.md) — The execution context to which feedback assessments attach
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The broader evaluation framework that includes both automated and human feedback
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Using feedback data for continuous quality monitoring
- [Build Evaluation Datasets](/concepts/evaluation-datasets.md) — Leveraging collected feedback to create test datasets
- [Human Feedback Annotations](/concepts/mlflow-human-feedback-collection.md) — The developer annotation system that feedback extends to production

## Sources

- collect-user-feedback-databricks-on-aws.md

# Citations

1. [collect-user-feedback-databricks-on-aws.md](/references/collect-user-feedback-databricks-on-aws-0b0ba83c.md)
