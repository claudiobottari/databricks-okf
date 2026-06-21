---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d3e3907eb13e4e852edf58290a6cfa40c21d327a9443b97bf0224e9e32127868
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-sessions-for-expert-review
    - LSFER
    - Labeling Sessions and Expert Review
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: Labeling Sessions for Expert Review
description: Structured expert review process where domain experts assess trace outputs using defined label schemas (e.g., categorical accuracy, ideal text responses) to establish ground truth.
tags:
  - mlflow
  - expert-review
  - labeling
  - evaluation
timestamp: "2026-06-19T13:48:21.670Z"
---

I'll write a wiki page for "Labeling Sessions for Expert Review" based on the source material provided, incorporating the existing page's structure and content where appropriate.

---

# Labeling Sessions for Expert Review

**Labeling Sessions for Expert Review** are a structured workflow in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) that allows teams to submit traces (app interactions) to domain experts for authoritative assessment. Experts can review the traces, provide ground-truth labels, and return structured feedback that can be used to evaluate and improve GenAI applications. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Overview

End-user feedback (e.g., thumbs-up/down) can signal potential quality issues, but only domain experts can confirm whether a response is truly correct and provide the ideal answer. Labeling sessions formalize this expert review process. They enable developers to collect high-quality labels — such as accuracy scores or ideal responses — that can serve as ground truth for downstream evaluation. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Key Concepts

### Label Schemas

A **label schema** defines what feedback to collect from expert reviewers. Schemas are created using the `create_label_schema` function. Each schema has:

- A **name** (e.g., `response_accuracy`).
- A **type** — `"feedback"` (for a rating) or `"expectation"` (for an ideal value).
- A **title** that is shown to the reviewer.
- An **input** type — for example, `InputCategorical` with predefined options (e.g., `["Accurate", "Partially Accurate", "Inaccurate"]`) or `InputText` for free-form text. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

Up to two schemas can be included in a session (one feedback and one expectation), and you can reuse schemas across sessions by setting `overwrite=True`. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Labeling Session

A **labeling session** groups together traces and the schemas that define what labels to collect. Sessions are created using `create_labeling_session`, which accepts a `name` and a list of schema names. Each session has a unique URL (`session.url`) that can be shared with reviewers. Labeling sessions are implemented as [MLflow Runs](/concepts/mlflow-run.md), so labeled traces can be retrieved later by querying the run ID (`session.mlflow_run_id`). ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Process

### 1. Define Label Schemas

Create the schemas that will guide expert review. For example:

```python
from mlflow.genai.label_schemas import create_label_schema, InputCategorical, InputText

accuracy_schema = create_label_schema(
    name="response_accuracy",
    type="feedback",
    title="Is the response factually accurate?",
    input=InputCategorical(options=["Accurate", "Partially Accurate", "Inaccurate"]),
    overwrite=True
)
ideal_response_schema = create_label_schema(
    name="expected_response",
    type="expectation",
    title="What would be the ideal response?",
    input=InputText(),
    overwrite=True
)
```

^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### 2. Create the Session and Add Traces

```python
from mlflow.genai.labeling import create_labeling_session

labeling_session = create_labeling_session(
    name="quickstart_review",
    label_schemas=[accuracy_schema.name, ideal_response_schema.name],
)
labeling_session.add_traces(traces)  # traces from mlflow.search_traces()
```

^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### 3. Share the Review Link

Share the session URL with expert reviewers. They open the URL and see the trace (including the question, response, and any existing end-user feedback). Reviewers then provide labels according to the defined schemas (e.g., select accuracy option, type ideal response). ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### 4. Retrieve Labeled Traces for Evaluation

After experts submit labels, retrieve the labeled traces:

```python
labeled_traces = mlflow.search_traces(run_id=labeling_session.mlflow_run_id)
```

These traces now contain the expert-provided labels. For example, the `expected_response` label can be used as ground truth with MLflow's [Correctness Scorer](/concepts/correctness-scorer.md):

```python
from mlflow.genai.scorers import Correctness

eval_results = mlflow.genai.evaluate(
    data=labeled_traces,
    predict_fn=my_chatbot,
    scorers=[Correctness()]
)
```

^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Alternative: Creating Sessions in the UI

You can also create labeling sessions directly in the MLflow UI:

1. On the Experiment page, click the **Labeling** tab.
2. Use the **Sessions** and **Schemas** tabs to add a new label schema and create a new session. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Best Practices

- Design label schemas to capture the specific quality dimensions (accuracy, completeness, tone, etc.) most relevant to your use case.
- Provide clear titles and instructions so reviewers understand what is expected.
- Start with a small pilot session to validate the schema before scaling to more traces.
- Use the expert-produced labels as ground truth when tuning [Custom Judges](/concepts/custom-judges.md) or evaluating model versions.

## Related Concepts

- [Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md) — End-user feedback and developer annotations.
- [[MLflow Trace|MLflow Traces]] — The execution records submitted to a labeling session.
- [Custom Judges](/concepts/custom-judges.md) — Automated scorers that can be aligned with expert labels.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) — Build versioned datasets from labeled traces.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploy judges to monitor ongoing quality.

## Sources

- 10-minute-demo-collect-human-feedback-databricks-on-aws.md

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
