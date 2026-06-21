---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dcc8123287eea439953948e9c7694dbca601cb757f7653ee17d035b9d360c2a5
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - end-user-feedback-collection-via-sdk
    - EFCVS
    - End-user feedback collection
    - Collect End-User Feedback
    - Collect end user feedback
    - Collect end-user feedback
    - Collecting user feedback (implementation)
    - User Feedback Collection
    - User feedback integration
    - end-user feedback
    - user feedback in production
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: End-User Feedback Collection via SDK
description: Using mlflow.log_feedback() to programmatically collect end-user feedback (like thumbs up/down) and associate it with specific traces for quality monitoring
tags:
  - mlflow
  - feedback
  - user-experience
  - monitoring
timestamp: "2026-06-19T21:53:49.922Z"
---

Here is the wiki page for "End-User Feedback Collection via SDK".

---

## End-User Feedback Collection via SDK

**End-User Feedback Collection via SDK** is the programmatic method of capturing user satisfaction signals — such as thumbs up/down ratings, free-text rationales, and categorical scores — directly from a GenAI application using the MLflow SDK. This is the primary mechanism for instrumenting production apps to gather human feedback for debugging, evaluation, and monitoring. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Overview

When users interact with a GenAI application, they can provide feedback through UI elements like thumbs up/down buttons. This method uses the SDK programmatically, which is useful for simulated testing and for integrating real user feedback into the platform. The SDK can embed user feedback alongside [MLflow Tracing](/concepts/mlflow-tracing.md) data, tying each assessment to a specific trace and span. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### API Reference: `mlflow.log_feedback()`

The core API for end-user feedback collection is `mlflow.log_feedback()`. This function records an assessment on an existing trace, including the feedback name, value, optional rationale, and an `AssessmentSource` object that identifies the source type (e.g., human) and a source ID (e.g., the end-user's unique identifier). ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

#### Required Imports

```python
from mlflow.entities.assessment import AssessmentSource, AssessmentSourceType
```

#### Function Parameters

The `mlflow.log_feedback()` function takes the following parameters:

| Parameter | Type | Description |
|-----------|------|-------------|
| `trace_id` | str | The ID of the trace to which the feedback applies. |
| `name` | str | A user-defined name for the feedback, e.g., `"user_feedback"`. |
| `value` | bool or str | The feedback value. For thumbs up/down, use `True` (positive) or `False` (negative). For other rating schemes, a string value can be used. |
| `rationale` | str (optional) | Free-text explanation for the feedback, e.g., "Missing details about key features". |
| `source` | AssessmentSource | Object specifying the source type and source ID. |

^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Example Usage: Simulating End-User Feedback

The following example simulates an end user giving negative feedback (thumbs down) on a trace: ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
from mlflow.entities.assessment import AssessmentSource, AssessmentSourceType

mlflow.log_feedback(
    trace_id=trace_id,
    name="user_feedback",
    value=False,  # False for thumbs down - user is unsatisfied
    rationale="Missing details about MLflow's key features like Projects and Model Registry",
    source=AssessmentSource(
        source_type=AssessmentSourceType.HUMAN,
        source_id="enduser_123",  # In production, this is the actual user ID
    ),
)
```

### Production Integration Pattern

In a production GenAI application, the feedback collection pattern typically follows this flow: ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

1. The app returns the `trace_id` with the response to the frontend.
2. When the user clicks "thumbs up" or "thumbs down", the frontend calls a backend API.
3. The backend API calls `mlflow.log_feedback()` with the corresponding `trace_id`.

### Viewing Collected Feedback

After feedback is logged, it can be viewed in the MLflow UI alongside the traces: ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

1. Navigate to the MLflow experiment.
2. Go to the **Logs** tab.
3. Click on the trace to open the trace details dialog.
4. Under **Assessments** on the right side of the dialog, the `user_feedback` field displays the value (e.g., `false` for thumbs down).

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The system that records execution traces for GenAI apps.
- [Developer Annotations via UI](/concepts/developer-annotations-via-mlflow-ui.md) — A complementary method for adding feedback interactively through the user interface.
- Expert Review Sessions and Labeling — The process of sending traces to domain experts for authoritative feedback.
- Correctness Evaluation with Expert Labels — Using expert-provided labels to evaluate app quality.

### Sources

- 10-minute-demo-collect-human-feedback-databricks-on-aws.md

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
