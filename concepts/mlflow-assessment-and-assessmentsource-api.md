---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9660abfe750263103f3e67ef90d9bd2adaf74eb717bad1b327eba6b11cf6a471
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-assessment-and-assessmentsource-api
    - AssessmentSource API and MLflow Assessment
    - MAAAA
    - Assessment (MLflow)|Assessment
    - MLflow Assessment|assessments
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: MLflow Assessment and AssessmentSource API
description: MLflow SDK entities (Assessment, AssessmentSource, AssessmentSourceType) used to log structured human feedback on traces with rationale and source provenance.
tags:
  - mlflow
  - sdk
  - feedback
timestamp: "2026-06-18T10:34:29.191Z"
---

## MLflow Assessment and AssessmentSource API

The MLflow Assessment and AssessmentSource API provides a structured way to log and manage human feedback on traces. Assessments capture evaluative signals—such as end-user ratings, developer annotations, and expert judgments—directly linked to specific trace spans. This enables teams to collect qualitative and quantitative feedback throughout the AI application lifecycle, from development to production. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Core Components

**`mlflow.entities.assessment.AssessmentSource`** is the data class that identifies the origin of a feedback entry. It accepts two parameters:

- `source_type`: An `AssessmentSourceType` enum value. The documented type is `HUMAN`, representing a human evaluator (end-user, developer, or expert).
- `source_id`: A string identifier for the specific evaluator (e.g., `"enduser_123"`). In production, this is typically the actual user ID.

`AssessmentSourceType` is imported from `mlflow.entities.assessment` and provides the available source categories. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Logging Feedback with `mlflow.log_feedback()`

Feedback is recorded on a trace using the `mlflow.log_feedback()` function. The call requires:

| Parameter    | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `trace_id`   | The ID of the trace to which the feedback applies.                         |
| `name`       | A human‑readable label for the assessment (e.g., `"user_feedback"`).       |
| `value`      | The assessment value – a boolean, number, or string (e.g., `False` for thumbs‑down). |
| `rationale`  | Optional free‑text explanation for the assessment.                         |
| `source`     | An `AssessmentSource` object indicating who provided the feedback.         |

The following example simulates an end-user giving negative feedback:

```python
from mlflow.entities.assessment import AssessmentSource, AssessmentSourceType

mlflow.log_feedback(
    trace_id=trace_id,
    name="user_feedback",
    value=False,          # False for thumbs down
    rationale="Missing details about MLflow's key features like Projects and Model Registry",
    source=AssessmentSource(
        source_type=AssessmentSourceType.HUMAN,
        source_id="enduser_123",
    ),
)
```

`log_feedback` stores the assessment as part of the trace’s metadata. It can be called from a backend API when a user interacts with a UI element (e.g., thumbs‑up/down button). ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Viewing Assessments in the UI

After logging feedback, assessments appear in the MLflow UI under the **Logs** tab of an experiment. When a trace is opened, the **Assessments** panel (right side) displays all logged feedback for that trace. Columns for assessment names (e.g., `user_feedback`) are added to the trace table after page refresh. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Relationship to Developer Annotations and Expert Review

The same mechanism powers developer annotations, which can be added interactively through the UI’s **Assessments** tab by specifying a name, value, and rationale. For expert review, the [Labeling Sessions](/concepts/labeling-sessions.md) API (via `create_labeling_session`) uses separate label schemas (`InputCategorical`, `InputText`) rather than raw `AssessmentSource`. However, expert feedback collected in a labeling session can later be used as ground truth for evaluation with [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) scorers (e.g., `Correctness`). The Assessment API provides the low‑level feedback logging that complements these higher‑level workflows. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Practical Use Cases

- **Collect end‑user feedback** at inference time by logging thumbs‑up/down responses.  
- **Add developer annotations** during debugging or manual review to flag accuracy issues.  
- **Instrumentation of any Gen AI app** – when combined with [MLflow Tracing](/concepts/mlflow-tracing.md), assessments provide a complete audit trail of both model outputs and human evaluations. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Sources

- [10-minute-demo-collect-human-feedback-databricks-on-aws.md](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/human-feedback) (ingested 2026-06-18) ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
