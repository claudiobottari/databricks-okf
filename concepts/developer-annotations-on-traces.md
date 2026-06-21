---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b0e9f6ee2a020ee13d05b40205f5d22fa74669823781e03e1ab36b9db2b6a4ce
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - developer-annotations-on-traces
    - DAOT
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: Developer Annotations on Traces
description: Interactive workflow for developers to add custom feedback assessments (e.g., accuracy scores) directly in the MLflow UI on individual trace spans.
tags:
  - mlflow
  - annotations
  - development
  - ui
timestamp: "2026-06-19T13:48:23.713Z"
---

# Developer Annotations on Traces

**Developer Annotations on Traces** refer to feedback and notes that developers attach to [trace](/concepts/traces.md) spans during the development or debugging phase of a GenAI application. These annotations provide a way to record qualitative assessments, correctness scores, or observations directly alongside the execution trace, enabling developers to capture context that complements automated evaluation and end-user feedback.

## Overview

MLflow allows developers to add annotations to any span within a trace, including the root span for trace-level feedback. These annotations are stored as assessments with a type, name, numeric or boolean value, and a rationale. Unlike end-user feedback (which originates from actual users) or expert review labels (which are collected in dedicated labeling sessions), developer annotations are created manually by the developer and serve as immediate notes during iterative development. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Adding Developer Annotations via the UI

The most common way to add developer annotations is through the MLflow UI:

1. Navigate to the **Logs** tab of the experiment.
2. Click on a trace to open the trace details dialog.
3. Click on any span (e.g., the root span for trace-level feedback).
4. In the **Assessments** tab on the right, click **Add new assessment**.
5. Fill in the following fields:
   - **Type**: `Feedback`
   - **Name**: A descriptive name, e.g., `accuracy_score`
   - **Value**: A numeric value, e.g., `.75`
   - **Rationale**: A free-text explanation of the assessment.
6. Click **Create**.

After refreshing the page, columns for the new assessments appear in the Logs table, making annotations visible alongside other trace metadata. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Adding Developer Annotations Programmatically

While the UI is the primary method described for developer annotations, the same feedback mechanism can also be invoked from code using the MLflow SDK. The `mlflow.log_feedback()` function allows you to record an assessment for a given trace ID, specifying the name, value, rationale, and source. The source should indicate that it came from a developer (e.g., `AssessmentSourceType.HUMAN` with a source_id like `dev_user_123`). This approach is useful for automated or batch annotation workflows. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
from mlflow.entities.assessment import AssessmentSource, AssessmentSourceType

mlflow.log_feedback(
    trace_id=trace_id,
    name="code_quality",
    value=0.9,
    rationale="Response covers all key features mentioned in the documentation.",
    source=AssessmentSource(
        source_type=AssessmentSourceType.HUMAN,
        source_id="dev_user_123",
    ),
)
```

## Viewing Annotations

Developer annotations appear in two places:

- **Trace details dialog**: Under the **Assessments** tab on the right side, each annotation is listed with its name, value, and rationale.
- **Logs table**: After adding an annotation, new columns appear in the experiment’s Logs table, allowing you to sort or filter traces by annotation values.

This visibility makes it easy to compare developer judgments across multiple traces during debugging or before releasing a new version. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Relationship to Other Feedback Types

Developer annotations are one of three feedback channels in MLflow:

| Feedback Type | Source | Use Case |
|---------------|--------|----------|
| **End-user feedback** | Actual users (simulated via `log_feedback`) | Thumbs up/down, satisfaction |
| **Developer annotations** | Developer via UI or SDK | Quick correctness scores, notes during development |
| **Expert review** | Domain experts via labeling sessions | Structured, authoritative labels with schemas |

All feedback types can coexist and be used together in evaluation workflows. For example, negative end-user feedback can prompt a developer to add an annotation, and later an expert can provide ground truth through a labeling session. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Best Practices

- **Use consistent naming conventions** for annotation names to enable filtering and aggregation across traces.
- **Include a rationale** so that other team members understand the context of the annotation.
- **Combine with automated scorers** by using developer annotations as a baseline against which to tune [MLflow GenAI Scorers](/concepts/mlflow-genai-scorers.md).
- **Do not overwrite end-user or expert feedback**; treat developer annotations as an independent layer of assessment.

## Related Concepts

- [Trace](/concepts/traces.md) — The execution record of an application call
- Span — A single operation within a trace
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The infrastructure for capturing trace data
- [Human Feedback](/concepts/mlflow-human-feedback-collection.md) — Overview of all feedback channels
- [Labeling Sessions](/concepts/labeling-sessions.md) — Structured expert review workflows
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — Automated evaluation using LLM-based scorers

## Sources

- 10-minute-demo-collect-human-feedback-databricks-on-aws.md

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
