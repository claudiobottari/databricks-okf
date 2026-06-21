---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 70ea708e5821c545d2b15cf3866a0cec3819094aa404dd3abeefbd56120518bd
  pageDirectory: concepts
  sources:
    - get-started-mlflow-3-for-genai-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-labeling-sessions-and-schemas
    - Schemas and MLflow Labeling Sessions
    - MLSAS
  citations:
    - file: get-started-mlflow-3-for-genai-databricks-on-aws.md
title: MLflow Labeling Sessions and Schemas
description: Primitives for defining structured human feedback collection — create_label_schema defines what feedback to collect (e.g., categorical ratings), and create_labeling_session groups schemas and traces for reviewer access.
tags:
  - mlflow
  - labeling
  - human-feedback
  - schemas
timestamp: "2026-06-19T18:59:16.444Z"
---

# MLflow Labeling Sessions and Schemas

**MLflow Labeling Sessions and Schemas** are features in MLflow 3 for collecting human feedback on GenAI application traces. Label schemas define the structure of the feedback to collect (e.g., categorical ratings), and labeling sessions organize which traces are sent to expert reviewers for evaluation. Reviewers use the Review App to provide feedback through the defined schema. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Overview

Human feedback is a complement to automated [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) with LLM-as-a-judge scorers. Domain experts can confirm quality, supply correct answers, and define guidelines for future evaluation. Labeling sessions and schemas provide a structured way to collect this feedback on [Traces](/concepts/traces.md) from GenAI applications. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Label Schemas

A label schema defines what kind of feedback to collect. It is created using `mlflow.genai.label_schemas.create_label_schema()`. Key parameters include:

- `name`: A unique identifier for the schema.
- `type`: The category of feedback; common types include `"feedback"`.
- `title`: A human-readable prompt for the reviewer.
- `input`: The structure of the response options. Use `InputCategorical` to provide a list of fixed choices, or `InputText` for free‑text responses.
- `overwrite`: When set to `True`, allows updating an existing schema with the same name. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

Example of creating a categorical label schema: ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import create_label_schema, InputCategorical

humor_schema = create_label_schema(
    name="response_humor",
    type="feedback",
    title="Rate how funny the response is",
    input=InputCategorical(options=["Very funny", "Slightly funny", "Not funny"]),
    overwrite=True,
)
```

## Labeling Sessions

A labeling session groups one or more label schemas and the set of traces to be reviewed. Sessions are created with `mlflow.genai.labeling.create_labeling_session()`. After creation, traces can be added to the session using `add_traces()`. The session provides a `url` attribute that can be shared with reviewers. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

Example flow: ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

```python
from mlflow.genai.labeling import create_labeling_session

session = create_labeling_session(
    name="quickstart_review",
    label_schemas=[humor_schema.name],
)

traces = mlflow.search_traces(max_results=10)
session.add_traces(traces)

print(f"Share this link with reviewers: {session.url}")
```

## Using the UI

Labeling sessions and schemas can also be managed through the Databricks MLflow UI. On an experiment page, click the **Labeling** tab. The left panel contains two tabs: **Sessions** and **Schemas**. From here you can add new label schemas and create new sessions without writing code. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Viewing Feedback

After reviewers submit feedback via the Review App, the results appear in the MLflow experiment UI under the **Labeling** tab. Feedback can also be retrieved programmatically:

- Use `mlflow.search_traces()` to analyze feedback alongside trace data.
- Use `mlflow.log_feedback()` to log user feedback from within an application. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Record traces from GenAI applications.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – Automated evaluation with LLM‑as‑a‑judge scorers.
- [Review App](/concepts/mlflow-review-app.md) – The interface used by human evaluators to provide feedback.
- [Traces](/concepts/traces.md) – The execution records that are added to labeling sessions.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit for traces, evaluations, and labeling data.

## Sources

- get-started-mlflow-3-for-genai-databricks-on-aws.md

# Citations

1. [get-started-mlflow-3-for-genai-databricks-on-aws.md](/references/get-started-mlflow-3-for-genai-databricks-on-aws-4186f156.md)
