---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 29a1dfa6549b0e82142dcda2b676f04674e4200052ce0e0c5d8d43bfc2f16e1c
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - human-feedback-collection-with-mlflowlog_feedback
    - HFCWM
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: Human Feedback Collection with mlflow.log_feedback()
description: Programmatic API for collecting end-user feedback (e.g., thumbs up/down) on GenAI app responses, associated with trace IDs and including rationale and source provenance.
tags:
  - mlflow
  - feedback
  - human-evaluation
  - genai
timestamp: "2026-06-19T17:22:55.288Z"
---

# Human Feedback Collection with mlflow.log_feedback()

**Human feedback collection with `mlflow.log_feedback()`** allows developers to instrument their generative AI applications to capture end-user ratings, developer annotations, and expert assessments directly within MLflow traces. This feedback can then be used to evaluate and improve application quality.

## Overview

MLflow provides a comprehensive framework for collecting human feedback at multiple stages of the application lifecycle. The `mlflow.log_feedback()` function is the primary SDK method for programmatically recording feedback associated with a specific trace. Feedback can be collected from end users through UI elements (such as thumbs up/down buttons), added interactively by developers through the MLflow UI, or gathered systematically through expert review sessions. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## End-User Feedback

The most common form of feedback collection captures user satisfaction signals from application end users. When users interact with a GenAI app, they can provide feedback through UI elements such as thumbs up/down buttons. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Using the SDK to Log Feedback

The `mlflow.log_feedback()` function accepts the following key parameters:

- `trace_id`: The ID of the trace associated with the user's interaction
- `name`: A descriptive name for the feedback (e.g., `"user_feedback"`)
- `value`: The feedback value (e.g., `True` for positive, `False` for negative)
- `rationale`: A text explanation of the feedback reason
- `source`: An `AssessmentSource` object identifying the feedback source type and source ID

The `AssessmentSource` requires two components:

- `source_type`: Set to `AssessmentSourceType.HUMAN` for human feedback
- `source_id`: A unique identifier for the user providing feedback (e.g., `"enduser_123"`) ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Example: Logging End-User Feedback

```python
from mlflow.entities.assessment import AssessmentSource, AssessmentSourceType

mlflow.log_feedback(
    trace_id=trace_id,
    name="user_feedback",
    value=False,  # False for thumbs down
    rationale="Missing details about MLflow's key features like Projects and Model Registry",
    source=AssessmentSource(
        source_type=AssessmentSourceType.HUMAN,
        source_id="enduser_123",
    ),
)
```

^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

In production, when a user clicks thumbs up or down in the frontend UI, your backend API should call `mlflow.log_feedback()` with the appropriate `trace_id` that was returned to the frontend with the response. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Developer Annotations via the UI

Developers can add their own feedback and notes directly through the MLflow UI without writing code:

1. Navigate to your MLflow experiment and open the **Logs** tab
2. Click on a trace to open the trace details dialog
3. Click on any span (choose the root span for trace-level feedback)
4. In the **Assessments** tab, click **Add new assessment** and provide:
   - **Type**: `Feedback`
   - **Name**: A descriptive name (e.g., `accuracy_score`)
   - **Value**: The assessment value (e.g., `.75`)
   - **Rationale**: A detailed explanation of the assessment

After creation, columns for the new assessments appear in the Logs table. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Expert Review with Labeling Sessions

For authoritative feedback, MLflow supports creating [Labeling Sessions](/concepts/labeling-sessions.md) that route traces to domain experts for structured review. This is particularly valuable when end-user feedback signals a potential quality issue that requires expert confirmation. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Creating a Labeling Session

Define what feedback to collect using [Label Schemas](/concepts/label-schemas.md), then create a session and add traces:

```python
from mlflow.genai.label_schemas import create_label_schema, InputCategorical, InputText
from mlflow.genai.labeling import create_labeling_session

accuracy_schema = create_label_schema(
    name="response_accuracy",
    type="feedback",
    title="Is the response factually accurate?",
    input=InputCategorical(options=["Accurate", "Partially Accurate", "Inaccurate"]),
    overwrite=True,
)

labeling_session = create_labeling_session(
    name="quickstart_review",
    label_schemas=[accuracy_schema.name],
)

traces = mlflow.search_traces(max_results=1)
labeling_session.add_traces(traces)
```

^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Expert Review Workflow

Expert reviewers can open the Review App URL provided by the labeling session, see the trace with the question and response (including any end-user feedback), assess the response, and submit their expert assessments as ground truth. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

Labeling sessions can also be created through the MLflow UI by navigating to the experiment's **Labeling** tab and using the **Sessions** and **Schemas** tabs. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Using Feedback for Evaluation

After expert feedback is collected, the labels (such as `expected_response`) can be used to evaluate your app automatically:

```python
from mlflow.genai.scorers import Correctness

labeled_traces = mlflow.search_traces(
    run_id=labeling_session.mlflow_run_id,
)

eval_results = mlflow.genai.evaluate(
    data=labeled_traces,
    predict_fn=my_chatbot,
    scorers=[Correctness()],
)
```

The `Correctness` scorer compares your app's outputs against expert-provided expected responses, providing quantitative feedback on alignment with expert expectations. Databricks recommends adding labeled traces to an [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) for version tracking and lineage. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The foundation for associating feedback with specific application invocations
- [Labeling Sessions](/concepts/labeling-sessions.md) — Structured expert review workflows for collecting ground truth
- [Label Schemas](/concepts/label-schemas.md) — Define the types of feedback to collect during expert review
- [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) — Versioned datasets for trace-based evaluation
- [Correctness Scorer](/concepts/correctness-scorer.md) — Automated evaluation comparing outputs to expert expectations
- GenAI App Development on Databricks — End-to-end workflow for building and monitoring GenAI applications

## Sources

- 10-minute-demo-collect-human-feedback-databricks-on-aws.md

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
