---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f26344708301087ef2557367d3987f5580ed64e8f59bd15b20c9e8c5dfa2f931
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - expert-labeling-sessions-for-genai-review
    - ELSFGR
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: Expert Labeling Sessions for GenAI Review
description: Creating structured expert review workflows using create_labeling_session() and label schemas (categorical and text inputs) to collect authoritative ground-truth feedback on trace responses
tags:
  - mlflow
  - labeling
  - expert-review
  - evaluation
timestamp: "2026-06-19T21:53:09.759Z"
---

# Expert Labeling Sessions for GenAI Review

**Expert Labeling Sessions** are structured review workflows within [MLflow](/concepts/mlflow.md) that let domain experts evaluate GenAI app traces and provide authoritative assessments. These sessions serve as a mechanism for collecting ground‑truth feedback when automated scoring or end‑user signals are insufficient to confirm quality issues. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Overview

After a GenAI application is instrumented with [MLflow Tracing](/concepts/mlflow-tracing.md) and end‑user feedback (e.g., thumbs‑up/down) has been collected, expert labeling sessions provide a way for domain experts to review specific traces and decide whether the model’s response is actually correct. For example, if a user marks a response as negative, only an expert can confirm whether there is a genuine problem and supply the ideal answer. Labeling sessions formalize this review process. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

A labeling session is represented as an [MLflow Run](/concepts/mlflow-run.md). All traces added to the session are associated with that run, which makes it easy to retrieve labeled traces later for evaluation. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Creating a Labeling Session

### Using the SDK

You can create a labeling session programmatically with the `mlflow.genai.labeling.create_labeling_session` function. The session requires a name and one or more label schemas that define the feedback to collect. Once created, you can add traces to the session and share its URL with reviewers. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

Python example:

```python
from mlflow.genai.labeling import create_labeling_session

labeling_session = create_labeling_session(
    name="quickstart_review",
    label_schemas=[accuracy_schema.name, ideal_response_schema.name],
)
```

The returned `labeling_session` object has a `.url` attribute that provides a direct link to the Review App for reviewers.

### Using the UI

In the MLflow UI, you can also create labeling sessions from the experiment page:

1.  Open the experiment.
2.  Click the **Labeling** tab.
3.  Use the **Sessions** and **Schemas** tabs to add a new label schema and create a new session.

^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Label Schemas

Label schemas define what feedback the expert reviewers will provide. They are created with the `mlflow.genai.label_schemas.create_label_schema` function. Each schema has a name, type, title, and input specification. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

Two common types are:

- **Feedback** – A categorical choice (e.g., “Accurate”, “Partially Accurate”, “Inaccurate”).
- **Expectation** – A free‑text field where the reviewer provides the ideal response.

Example:

```python
from mlflow.genai.label_schemas import create_label_schema, InputCategorical, InputText

accuracy_schema = create_label_schema(
    name="response_accuracy",
    type="feedback",
    title="Is the response factually accurate?",
    input=InputCategorical(options=["Accurate", "Partially Accurate", "Inaccurate"]),
    overwrite=True,
)

ideal_response_schema = create_label_schema(
    name="expected_response",
    type="expectation",
    title="What would be the ideal response?",
    input=InputText(),
    overwrite=True,
)
```

Multiple schemas can be passed to a single labeling session.

## Adding Traces to Sessions

Traces are added to a labeling session using the `labeling_session.add_traces()` method, which accepts an MLflow Trace object or a list of traces. You can obtain traces by calling `mlflow.search_traces()` and specifying the appropriate experiment or run. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

Example:

```python
traces = mlflow.search_traces(max_results=1)
labeling_session.add_traces(traces)
```

## Expert Review Process

Reviewers access the labeling session via the shared URL. In the Review App they see:

- The trace, including the original question and model response.
- Any end‑user feedback already attached to the trace.
- The input fields defined by the label schemas (e.g., a drop‑down for accuracy, a text box for the ideal response).

Experts fill in the fields and submit their assessments, which become part of the trace’s annotations as ground truth. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Using Expert Feedback for Evaluation

Once experts have provided labels (especially the `expected_response` text), you can use [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) to measure how well your app aligns with expert expectations. The Correctness scorer compares the app’s output to the ideal response recorded in the labeling session. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

Example:

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

Databricks recommends adding labeled traces to an [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) for version tracking and lineage.

## Related Concepts

- [Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md) – End‑user feedback that may trigger expert review.
- [Developer Annotations](/concepts/developer-annotations-on-traces.md) – Inline feedback added by developers during development.
- [Label Schemas](/concepts/label-schemas.md) – Definitions of the feedback types collected during labeling.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The mechanism that records app invocations as traces.
- [Correctness Scorer](/concepts/correctness-scorer.md) – A metric that compares outputs to expert‑provided ideal responses.
- [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) – A dataset object for versioned evaluation data.

## Sources

- 10-minute-demo-collect-human-feedback-databricks-on-aws.md

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
