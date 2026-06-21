---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b275964c9b3fa2625a2f47bf3f1a630694e83fb9a28c9902fa70da14c49a840
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - human-feedback-collection-in-mlflow
    - HFCIM
    - Feedback collection in MLflow
    - Human feedback collection with MLflow
    - Human Feedback (MLflow GenAI)
    - Human Feedback System
    - Human feedback in MLflow
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: Human Feedback Collection in MLflow
description: Mechanism to collect end-user feedback (thumbs up/down) on GenAI app outputs using mlflow.log_feedback with assessment metadata.
tags:
  - mlflow
  - feedback
  - genai
  - evaluation
timestamp: "2026-06-19T13:49:05.532Z"
---

Here is the wiki page for "Human Feedback Collection in MLflow".

---

## Human Feedback Collection in MLflow

**Human Feedback Collection in MLflow** refers to the process of gathering qualitative and quantitative evaluations from users, developers, and domain experts on the outputs of a GenAI agent or application. This feedback is crucial for assessing application quality, debugging issues, and creating ground truth data for automated evaluation. MLflow integrates feedback collection directly into its tracing and evaluation framework, allowing teams to instrument apps, collect ratings, and create structured review sessions.

### Overview

Collecting human feedback is a core component of building reliable GenAI applications. MLflow enables three distinct modes of feedback collection: end-user feedback, developer annotations, and expert review sessions. Each mode serves a different purpose and audience, and all are stored alongside the trace data they evaluate. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Modes of Feedback Collection

#### End-User Feedback
End-user feedback captures the reactions of the people who interact with your application in real time. This is typically binary or categorical feedback (e.g., thumbs up or thumbs down) provided through UI elements in the application frontend. In a development or testing context, this feedback can be simulated using the MLflow SDK. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

To log end-user feedback programmatically, use `mlflow.log_feedback()`:

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

In production, the `trace_id` is returned with the response to the frontend. When a user clicks a feedback button, the frontend calls a backend API that logs the feedback against the corresponding trace. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

#### Developer Annotations
Developers can add their own annotations directly in the MLflow UI without needing to write code. This is useful for quick quality checks during development or for adding notes to specific traces. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

To add a developer annotation in the UI:

1.  Open a trace in the **Logs** tab of your experiment.
2.  Click on any span (select the root span for trace-level feedback).
3.  In the **Assessments** tab on the right, click **Add new assessment**.
4.  Choose the type (`Feedback`), provide a name, a numeric or categorical value, and an optional rationale.
5.  Click **Create**.

These annotations appear as columns in the Logs table and can be used for filtering and comparison. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

#### Expert Review Sessions
Expert review sessions, also called labeling sessions, are structured review workflows designed for domain experts to provide authoritative feedback. These sessions are particularly useful when end-user feedback signals a potential quality issue that only a subject matter expert can confirm or resolve. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

To create a labeling session, define "label schemas" that specify what feedback to collect. Schemas can be categorical (e.g., "Accurate", "Partially Accurate", "Inaccurate") or free-text (e.g., "What would be the ideal response?"). ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import create_label_schema, InputCategorical, InputText
from mlflow.genai.labeling import create_labeling_session

accuracy_schema = create_label_schema(
    name="response_accuracy",
    type="feedback",
    title="Is the response factually accurate?",
    input=InputCategorical(options=["Accurate", "Partially Accurate", "Inaccurate"]),
)

ideal_response_schema = create_label_schema(
    name="expected_response",
    type="expectation",
    title="What would be the ideal response?",
    input=InputText(),
)

labeling_session = create_labeling_session(
    name="quickstart_review",
    label_schemas=[accuracy_schema.name, ideal_response_schema.name],
)

labeling_session.add_traces(traces)
```

After creation, the session provides a shareable URL that reviewers can open. In the Review App, experts see the trace (including any end-user feedback), assess the response against the defined schemas, and submit their assessments. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

Labeling sessions can also be created directly from the MLflow UI via the **Labeling** tab on the Experiment page, where users can manage sessions and schemas. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Using Feedback for Evaluation

Expert-provided labels, particularly free-text expectations like an ideal response, can be used as ground truth to evaluate an agent. The `Correctness` scorer in MLflow GenAI compares an app's actual outputs against the expert-provided `expected_response` label, producing quantitative alignment scores. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Correctness

labeled_traces = mlflow.search_traces(
    run_id=labeling_session.mlflow_run_id,
)

eval_results = mlflow.genai.evaluate(
    data=labeled_traces,
    predict_fn=my_chatbot,
    scorers=[Correctness()]
)
```

### Viewing Feedback in the UI

All collected feedback—end-user, developer, and expert—is visible alongside the trace data in the MLflow UI. In the **Logs** tab, opening a trace reveals an **Assessments** panel on the right side of the trace details dialog, where all evaluations for that trace are displayed. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- GenAI Agent Evaluation
- [Labeling Sessions](/concepts/labeling-sessions.md)
- [Correctness Scorer](/concepts/correctness-scorer.md)
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md)

### Sources

- 10-minute-demo-collect-human-feedback-databricks-on-aws.md

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
