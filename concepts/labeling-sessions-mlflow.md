---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1d32c6970766ecf36f5d13ea09e1fdc218ebdf5e8b07070995d50e4ac536c34f
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-sessions-mlflow
    - LS(
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: Labeling Sessions (MLflow)
description: Structured containers within MLflow that collect human-generated assessments (labels) on MLflow Traces from domain experts via the MLflow Review App.
tags:
  - mlflow
  - human-feedback
  - genai
timestamp: "2026-06-19T09:33:11.823Z"
---

# Labeling Sessions (MLflow)

**Labeling Sessions** in [MLflow](/concepts/mlflow.md) provide a structured way to gather feedback from domain experts on the behavior of GenAI applications. A labeling session is a special type of [MLflow Run](/concepts/mlflow-run.md) that contains a specific set of traces that domain experts review using the MLflow Review App. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Overview

The goal of a labeling session is to collect human-generated assessments (labels) on existing [[MLflow Trace|MLflow Traces]]. You can capture either `Feedback` or `Expectation` data, which can then be used to improve your GenAI application through systematic evaluation. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

Labeling sessions appear in the **Evaluations** tab of the MLflow UI. Because labeling sessions are logged as MLflow runs, you can also access the traces and associated assessments using the MLflow API [`mlflow.search_runs()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_runs). ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## How Labeling Sessions Work

A labeling session acts as a container for traces and their associated labels, enabling systematic feedback collection that can drive evaluation and improvement workflows. When you create a labeling session, you define: ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

- **Name**: A descriptive identifier for the session.
- **Assigned users**: Domain experts who will provide labels.
- **Agent**: (Optional) The GenAI application to generate responses if needed.
- **Labeling schemas**: The questions and format for feedback collection. You can use built-in schemas (`EXPECTED_FACTS`, `EXPECTED_RESPONSE`, `GUIDELINES`) or create custom ones.
- **Multi-turn chat**: Whether to support conversation-style labeling.

The optional **Agent** field connects a labeling session to the Review App's Chat UI for interactive testing. The Chat UI requires an agent deployed to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) and does not currently support agents deployed on Databricks Apps. Reviewing and labeling existing traces works regardless of how your agent is deployed. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Creating Labeling Sessions

You can create labeling sessions using the UI or the API. Session names might not be unique, so use the [MLflow Run](/concepts/mlflow-run.md) ID (`session.mlflow_run_id`) to store and reference sessions. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Using the UI

To create a labeling session in the MLflow UI:

1. In the Databricks workspace, in the left sidebar, click **Experiments**.
2. Click the name of your experiment to open it.
3. Click **Labeling sessions** in the sidebar.
4. Click **Create session**.
5. Enter a name for the session. You can optionally specify an evaluation dataset or select labeling schemas.
6. When ready, click **Create Session**.
7. To share the session with reviewers, click the session name, then click **Share** and enter email addresses for each reviewer.

### Using the API

To create sessions with full programmatic control, use the MLflow API [`mlflow.genai.labeling.create_labeling_session()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.create_labeling_session). ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
import mlflow.genai.labeling as labeling
import mlflow.genai.label_schemas as schemas

session = labeling.create_labeling_session(
    name="customer_service_review_jan_2024",
    assigned_users=["alice@company.com", "bob@company.com"],
    label_schemas=[schemas.EXPECTED_FACTS]
)
```

## Adding Traces to Sessions

After creating a session, you must add traces for expert review. You can do this using the UI or the `add_traces()` API. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Using the UI

1. Open the experiment and click **Traces** in the sidebar.
2. Select the traces by checking the box to the left of the Trace ID.
3. From the **Actions** drop-down menu, select **Add to labeling session**.
4. In the dialog, click **Export** next to the target labeling session.

### Using the API

You can add traces from search results or individual trace objects:

```python
# Add traces from search results
traces_df = mlflow.search_traces(
    filter_string="tags.test_tag = 'C001'",
    max_results=50
)
session.add_traces(traces_df)

# Add individual trace objects
trace1 = mlflow.get_trace(trace_id_1)
session.add_traces([trace1, trace2, trace3])
```

## Managing Labeling Sessions

### Retrieving Sessions

Use `mlflow.genai.get_labeling_sessions()` to retrieve all sessions: ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
all_sessions = labeling.get_labeling_sessions()
for session in all_sessions:
    print(f"- {session.name} (ID: {session.labeling_session_id})")
```

### Deleting Sessions

Use `mlflow.genai.delete_labeling_session()` to remove a session from the Review App: ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
labeling.delete_labeling_session(session_to_delete)
```

## Managing Assigned Users

Any user in the Databricks account can be assigned to a labeling session, regardless of whether they have workspace access. However, granting a user permission to a labeling session gives them access to the labeling session's MLflow experiment. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

When you assign users to a labeling session, the system automatically grants necessary `WRITE` permissions on the MLflow Experiment containing the labeling session. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

To add users to existing sessions, use `set_assigned_users()`: ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
session.set_assigned_users(session.assigned_users + ["expert2@company.com"])
```

## Retrieving Feedback Responses

After reviewers complete a labeling session, MLflow stores their responses as `Assessments` on the traces. You can retrieve them in the UI by opening the session, clicking the request, and then clicking **Assessments** at the upper right. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Syncing to Evaluation Datasets

You can synchronize collected `Expectations` to [Evaluation Datasets](/concepts/evaluation-datasets.md) using the `sync()` method. The method performs an intelligent upsert operation: ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

- Each trace's inputs serve as a unique key to identify records in the dataset.
- For traces with matching inputs, expectations from the labeling session overwrite existing expectations when the expectation names are the same.
- Traces that do not match existing trace inputs are added as new records.
- Existing dataset records with different inputs remain unchanged.

```python
session.sync(to_dataset="customer_service_eval_dataset")
```

## Best Practices

### Session Organization

- Use clear, descriptive, date-stamped names, such as `customer_service_review_march_2024`. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- Keep sessions focused on specific evaluation goals or time periods.
- Aim for 25-100 traces per session to avoid reviewer fatigue.
- Always store the `session.mlflow_run_id` when creating a session for programmatic access instead of relying on session names.

### User Management

- Assign users based on domain expertise and availability. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- Distribute labeling work evenly across multiple experts.
- Remember that users must have access to the Databricks workspace.

## Related Concepts

- [Labeling Schemas](/concepts/labeling-schemas.md) — Define structured feedback questions for labeling sessions
- [[MLflow Trace|MLflow Traces]] — The execution traces that are reviewed in labeling sessions
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Convert labeled sessions into test datasets
- Human Feedback in MLflow — Broader framework for collecting human assessments
- [MLflow Review App](/concepts/mlflow-review-app.md) — The interface where domain experts review and label traces
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges for continuous quality monitoring

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
