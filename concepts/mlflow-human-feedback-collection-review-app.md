---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 636becaec65659a6cfbeb09accb44177329d31790b5f18e110c8d0382c818a57
  pageDirectory: concepts
  sources:
    - get-started-mlflow-3-for-genai-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-human-feedback-collection-review-app
    - MHFC(A
  citations:
    - file: get-started-mlflow-3-for-genai-databricks-on-aws.md
title: MLflow Human Feedback Collection (Review App)
description: A system for collecting structured feedback from domain experts on GenAI traces using labeling schemas, labeling sessions, and the Review App UI.
tags:
  - mlflow
  - human-feedback
  - labeling
  - review
timestamp: "2026-06-19T10:44:09.578Z"
---

# MLflow Human Feedback Collection (Review App)

**MLflow Human Feedback Collection (Review App)** is a feature within [MLflow 3 for GenAI](/concepts/mlflow-3-for-genai.md) that enables domain experts to review and rate GenAI application traces. While LLM-as-a-judge evaluation provides automated quality scoring, the Review App allows human evaluators to provide direct feedback, confirm correctness, and define guidelines for future evaluation. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Overview

After instrumenting a GenAI application with [MLflow Tracing](/concepts/mlflow-tracing.md) and running automated [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md), teams can collect human feedback by sharing traces with expert reviewers through the Review App. The process involves defining a labeling schema (the type of feedback to collect), creating a labeling session, adding traces to that session, and sharing a link with reviewers. Expert reviewers then rate individual traces using the schema defined. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Labeling Schemas

A labeling schema specifies what feedback to collect from human reviewers. Schemas are created using `mlflow.genai.label_schemas.create_label_schema()`. Common inputs include `InputCategorical` (for choosing among predefined options) and `InputText` (for free-text responses). Each schema has a name, title, and type (e.g., `"feedback"`). ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import create_label_schema, InputCategorical

humor_schema = create_label_schema(
    name="response_humor",
    type="feedback",
    title="Rate how funny the response is",
    input=InputCategorical(options=["Very funny", "Slightly funny", "Not funny"]),
    overwrite=True
)
```

## Creating a Labeling Session

A labeling session groups one or more label schemas together and manages the collection of feedback. Create a session using `mlflow.genai.labeling.create_labeling_session()`, providing a name and the list of label schemas to include. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

```python
from mlflow.genai.labeling import create_labeling_session

labeling_session = create_labeling_session(
    name="quickstart_review",
    label_schemas=[humor_schema.name],
)
```

## Adding Traces to a Session

Traces are added to a session using `labeling_session.add_traces()`. Traces can be retrieved from the current experiment using `mlflow.search_traces()`, which accepts a `max_results` parameter. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

```python
traces = mlflow.search_traces(max_results=10)
labeling_session.add_traces(traces)
```

Alternatively, users can create labeling sessions and add traces directly through the MLflow UI by opening the experiment, clicking the **Labeling** tab, and using the **Sessions** and **Schemas** tabs. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Sharing with Reviewers

After traces are added, the session provides a `url` property that can be shared with reviewers via a link. Reviewers open the link to access the Review App UI, where they can rate responses according to the defined labeling schema. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

```python
print(f"Share this link with reviewers: {labeling_session.url}")
```

## Viewing Feedback

To view collected feedback in the MLflow UI, open the active experiment and click the **Labeling** tab. The feedback is stored alongside the traces. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Programmatic Access

Feedback can be accessed programmatically:

- Use `mlflow.search_traces()` to analyze feedback associated with traces. See mlflow.search_traces() API|Search traces programmatically for details. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]
- Use `mlflow.log_feedback()` to log user feedback directly within an application. See Collect user feedback for details. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The mechanism that records agent executions as traces.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – Automated LLM-as-a-judge evaluation that complements human feedback.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying scorers to monitor production traffic, with human feedback as a validation layer.
- [Labeling Schema](/concepts/labeling-schema.md) – Definitions of feedback criteria for human reviewers.
- Review App UI – The user interface used by expert reviewers to provide feedback.

## Sources

- get-started-mlflow-3-for-genai-databricks-on-aws.md

# Citations

1. [get-started-mlflow-3-for-genai-databricks-on-aws.md](/references/get-started-mlflow-3-for-genai-databricks-on-aws-4186f156.md)
