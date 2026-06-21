---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2723e2e2d3c7f684e0f6cd44a964af867aed4dacbf1e6e81a9d0bcf6a78297bd
  pageDirectory: concepts
  sources:
    - collect-user-feedback-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - assessmentsource-in-mlflow
    - AIM
  citations:
    - file: collect-user-feedback-databricks-on-aws.md
title: AssessmentSource in MLflow
description: Entity that identifies the origin of feedback, supporting source types like HUMAN for user feedback and LLM_JUDGE for automated evaluation.
tags:
  - mlflow
  - feedback
  - entity
  - source-type
timestamp: "2026-06-18T14:38:44.057Z"
---

---
title: AssessmentSource in MLflow
summary: The AssessmentSource entity identifies who or what provided a feedback assessment on a trace, supporting source types like HUMAN and LLM_JUDGE.
sources:
  - collect-user-feedback-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:00:00.000Z"
updatedAt: "2026-06-18T11:00:00.000Z"
tags:
  - mlflow
  - feedback
  - tracing
  - assessment
aliases:
  - AssessmentSource
  - mlflow-entity-assessment-source
  - AFS
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# AssessmentSource in MLflow

**AssessmentSource** is an entity used in MLflow's [feedback collection](/concepts/mlflow-human-feedback-collection.md) system to identify who or what provided an assessment (such as a user rating or LLM judge score) on a [trace](/concepts/traces.md) or span. It is a required parameter when logging feedback via `mlflow.log_feedback()`.

## Structure

The `AssessmentSource` object has two key fields:^[collect-user-feedback-databricks-on-aws.md]

- **`source_type`** — A string indicating the category of the feedback provider. Valid values include:
  - `"HUMAN"` — for feedback provided by an end user.
  - `"LLM_JUDGE"` — for automated scoring by an LLM-based judge.
- **`source_id`** — A string that identifies the specific provider (e.g., a user ID or system identifier).

These fields are used together to attribute feedback to a particular source for auditing and analysis.^[collect-user-feedback-databricks-on-aws.md]

## Usage

When collecting [user feedback in production](/concepts/end-user-feedback-collection-via-sdk.md), you construct an `AssessmentSource` object and pass it to `mlflow.log_feedback()`:^[collect-user-feedback-databricks-on-aws.md]

```python
from mlflow.entities import AssessmentSource

mlflow.log_feedback(
    trace_id=trace_id,
    name="user_feedback",
    value=is_correct,
    source=AssessmentSource(
        source_type="HUMAN",
        source_id=user_id
    ),
    rationale=comment
)
```

For [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) evaluations, the `source_type` is set to `"LLM_JUDGE"`.

## Significance

Capturing the source type and identifier enables:

- **Attribution**: Knowing whether feedback came from a human or an automated judge.
- **User‑specific analysis**: Understanding satisfaction trends per user (via `source_id`).
- **Auditability**: Tracing the origin of any assessment for debugging or compliance purposes.^[collect-user-feedback-databricks-on-aws.md]

## Related Concepts

- Feedback collection in MLflow
- [Trace Assessments](/concepts/trace-assessments.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [User feedback integration](/concepts/end-user-feedback-collection-via-sdk.md)
- [LLM judge evaluation](/concepts/llm-as-a-judge-evaluation.md)

## Sources

- collect-user-feedback-databricks-on-aws.md

# Citations

1. [collect-user-feedback-databricks-on-aws.md](/references/collect-user-feedback-databricks-on-aws-0b0ba83c.md)
