---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cee04daeac2faa58cf2e28f07a6a970cb35cb7c0e1cf335564fd0db4954925e9
  pageDirectory: concepts
  sources:
    - migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-human-feedback-and-labeling
    - Labeling and MLflow 3 Human Feedback
    - M3HFAL
  citations:
    - file: migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md
title: MLflow 3 Human Feedback and Labeling
description: The human feedback system in MLflow 3 moves from databricks.agents.review_app to mlflow.genai.labeling and mlflow.genai.label_schemas, with explicit schema creation and new dataset management via mlflow.genai.datasets.
tags:
  - mlflow
  - human-feedback
  - labeling
timestamp: "2026-06-19T19:35:25.969Z"
---

# MLflow 3 Human Feedback and Labeling

**Human feedback and labeling** in MLflow 3 enables collection, management, and reuse of human judgements against AI system outputs. It is part of the Agent Evaluation integration and is exposed via the `mlflow[databricks]>=3.1` SDK under the `mlflow.genai.labeling` and `mlflow.genai.label_schemas` namespaces. The feature provides a refreshed UI, a simplified SDK, and streamlined collection of human feedback. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

> **Important:** MLflow 3 with Agent Evaluation only works on Managed MLflow, not open source MLflow. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Labeling Sessions and Schemas

A **labeling session** groups a set of traces (recorded interactions) for human review. You can assign users to the session and attach one or more label schemas that define the feedback to collect. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

### Creating a Label Schema

Label schemas define what kind of feedback you want to collect (e.g., categorical ratings, text lists). Use `mlflow.genai.label_schemas.create_label_schema()` and set the schema type with `LabelSchemaType` constants. Built-in schema names are available as constants such as `schemas.EXPECTED_FACTS`. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

```python
import mlflow.genai.label_schemas as schemas

quality_schema = schemas.create_label_schema(
    name="response_quality",
    type=schemas.LabelSchemaType.FEEDBACK,
    title="Rate the response quality",
    input=schemas.InputCategorical(
        options=["Poor", "Fair", "Good", "Excellent"]
    ),
    overwrite=True
)
```

### Creating a Labeling Session

Use `mlflow.genai.labeling.create_labeling_session()` to start a session. Provide a name, list of assigned users, and the label schemas you want to use. Then add traces to the session for review. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

```python
import mlflow
import mlflow.genai.labeling as labeling

session = labeling.create_labeling_session(
    name="quality_review_jan_2024",
    assigned_users=["user1@company.com", "user2@company.com"],
    label_schemas=[
        schemas.EXPECTED_FACTS,
        "response_quality"
    ]
)

traces = mlflow.search_traces(run_id=session.mlflow_run_id)
session.add_traces(traces)
```

## Review App

The **Review App** provides a web interface where assigned users can view traces and provide labels. Get the review app URL using `labeling.get_review_app()`. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

```python
app = labeling.get_review_app()
print(f"Review app URL: {app.url}")
```

## Syncing Feedback to Datasets

Labeled feedback can be synced back to a Delta table and later used as a ground‑truth dataset for evaluation. Use the `session.sync()` method to write expectations and scores to a Unity Catalog table. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

```python
session.sync(to_dataset="catalog.schema.eval_dataset")
```

To load the synced dataset for evaluation, use `mlflow.genai.datasets.get_dataset()`:

```python
from mlflow.genai import datasets

dataset = datasets.get_dataset("catalog.schema.eval_dataset")
results = mlflow.genai.evaluate(
    data=dataset,
    predict_fn=my_agent,
    scorers=[...]
)
```

## Migration from Agent Evaluation (MLflow 2.x)

The human feedback functionality previously lived under `databricks.agents.review_app`. In MLflow 3 it has moved to the dedicated namespaces listed below. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

| MLflow 2.x | MLflow 3.x |
|------------|------------|
| `databricks.agents.review_app` | `mlflow.genai.labeling` |
| `review_app.label_schemas` | `mlflow.genai.label_schemas` |
| `review_app.create_labeling_session` | `labeling.create_labeling_session` |
| `review_app.get_review_app` | `labeling.get_review_app` |
| `review_app.label_schemas.EXPECTED_FACTS` | `schemas.EXPECTED_FACTS` (use as name, not object) |

In MLflow 3 you must explicitly create built‑in schemas before using them, whereas in MLflow 2 they were automatically available. The constant names (e.g., `schemas.EXPECTED_FACTS`) are provided to ensure compatibility with built‑in scorers. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Related Concepts

- [MLflow 3 Evaluation](/concepts/mlflow-evaluation-ui.md) – Overview of scoring and evaluation with LLM judges.
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) – The broader system for evaluating AI agents.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – How traces are captured and used for feedback.
- [Label Schema Types](/concepts/label-schemas.md) – Available schema types (`FEEDBACK`, `EXPECTATION`, etc.).
- Datasets in MLflow 3 – Managing evaluation datasets from human feedback.

## Sources

- migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md

# Citations

1. [migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md](/references/migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws-7eefbe86.md)
