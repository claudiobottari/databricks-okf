---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f53bd23a0b5400d9c81108c24f6b925c8c9a844d757de8f262622541f2d2e37d
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-labelingsession-api
    - MLA
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: MLflow LabelingSession API
description: The programmatic Python API (mlflow.genai.labeling) for creating, retrieving, deleting labeling sessions, managing users, adding traces, and syncing expectations to evaluation datasets.
tags:
  - mlflow
  - api
  - labeling
  - python
timestamp: "2026-06-18T11:19:26.049Z"
---

# MLflow LabelingSession API

The **MLflow LabelingSession API** provides a programmatic interface for creating, managing, and interacting with [Labeling Sessions](/concepts/labeling-sessions.md) in MLflow GenAI. Labeling sessions are a special type of [MLflow Run](/concepts/mlflow-run.md) that collect structured human feedback (labels) on existing [[MLflow Trace|MLflow Traces]] from domain experts using the MLflow Review App.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Overview

A labeling session acts as a container for traces and their associated labels, enabling systematic feedback collection that can drive evaluation and improvement workflows. The LabelingSession API exposes methods to create sessions, assign reviewers, add traces, retrieve feedback responses, manage users, and synchronize collected expectations to evaluation datasets.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

The primary API functions are provided under `mlflow.genai.labeling` and `mlflow.genai`:

- `mlflow.genai.labeling.create_labeling_session()` — create a new session
- `mlflow.genai.labeling.get_labeling_sessions()` — retrieve one or all sessions
- `mlflow.genai.labeling.delete_labeling_session()` — remove a session
- `mlflow.genai.LabelingSession.add_traces()` — add traces to a session
- `mlflow.genai.LabelingSession.set_assigned_users()` — manage reviewers
- `mlflow.genai.LabelingSession.sync()` — sync expectations to an evaluation dataset

Because labeling sessions are logged as MLflow runs, you can also access them through `mlflow.search_runs()`.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Creating Sessions

### Basic Session

To create a labeling session, use `create_labeling_session()`. At minimum, you must provide a name, a list of assigned users (email addresses), and at least one label schema.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
import mlflow.genai.labeling as labeling
import mlflow.genai.label_schemas as schemas

session = labeling.create_labeling_session(
    name="customer_service_review_jan_2024",
    assigned_users=["alice@company.com", "bob@company.com"],
    label_schemas=[schemas.EXPECTED_FACTS]
)
print(f"Created session: {session.name}")
print(f"Session ID: {session.labeling_session_id}")
```

### Session with Custom Schemas

You can also supply custom label schemas created via `schemas.create_label_schema()`:^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
quality_schema = schemas.create_label_schema(
    name="response_quality",
    type="feedback",
    title="Rate the response quality",
    input=schemas.InputCategorical(options=["Poor", "Fair", "Good", "Excellent"]),
    overwrite=True,
)

session = labeling.create_labeling_session(
    name="quality_assessment_session",
    assigned_users=["expert@company.com"],
    label_schemas=["response_quality", schemas.EXPECTED_FACTS],
)
```

### Important Notes

- Session names might not be unique. Always store and use the [MLflow Run](/concepts/mlflow-run.md) ID (`session.mlflow_run_id`) for reliable programmatic access.^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- An optional **Agent** field can connect the session to a deployed [Model Serving Endpoint](/concepts/model-serving-endpoint.md) for interactive Chat UI testing. Reviewing existing traces works regardless of deployment method.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Managing Sessions

### Retrieving Sessions

Use `get_labeling_sessions()` to list all sessions. You can filter by name or scan for a specific session:^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
all_sessions = labeling.get_labeling_sessions()
for session in all_sessions:
    if session.name == "customer_service_review_jan_2024":
        target_session = session
        break
print(f"Session name: {target_session.name}")
print(f"[[mlflow-run|MLflow Run]] ID: {target_session.mlflow_run_id}")
```

Alternatively, use `mlflow.search_runs()` with the experiment ID and a filter string to locate a session by its run ID.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Deleting Sessions

Use `delete_labeling_session()` to remove a session from the Review App. The method accepts a session object or its identifier.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
review_app = labeling.delete_labeling_session(session_to_delete)
print(f"Deleted session: {session_to_delete.name}")
```

### Managing Assigned Users

The `set_assigned_users()` method replaces the current list of reviewers. You can add users by combining the existing list with new emails:^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
session.set_assigned_users(session.assigned_users + ["expert2@company.com", "expert3@company.com"])
print(f"Session now has users: {session.assigned_users}")
```

When users are assigned, the system automatically grants `WRITE` permissions on the containing MLflow Experiment. Users requiring workspace access must first be provisioned via ecosystem or account-level SCIM provisioning.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Adding Traces to Sessions

### From a DataFrame of Traces

After creating sample traces, search for them and add them to a session using `add_traces()`:^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
session = labeling.create_labeling_session(
    name="negative_feedback_review",
    assigned_users=["quality_expert@company.com"],
    label_schemas=["response_quality", "expected_facts"],
)

traces_df = mlflow.search_traces(
    filter_string="tags.test_tag = 'C001'",
    max_results=50,
)
session.add_traces(traces_df)
```

### Adding Individual Trace Objects

You can also obtain trace objects directly via `mlflow.get_trace()` and pass a list to `add_traces()`:^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
trace1 = mlflow.get_trace(trace_id_1)
trace2 = mlflow.get_trace(trace_id_2)
session.add_traces([trace1, trace2, trace3])
```

## Retrieving Feedback Responses

After reviewers complete a labeling session, their responses are stored as **Assessments** on the traces. You can retrieve them using the MLflow API by accessing the trace's attributes. The source does not provide a specific retrieval API call, but it notes that assessments can be viewed in the UI under the **Assessments** button. To access them programmatically, you can fetch the trace via `mlflow.get_trace()` and inspect its feedback attributes, or search runs that belong to the labeling session’s experiment.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Syncing to Evaluation Datasets

The `sync()` method transfers collected **Expectations** from the labeling session into an [Evaluation Dataset](/concepts/evaluation-dataset.md). It performs an intelligent upsert:^[create-and-manage-labeling-sessions-databricks-on-aws.md]

- Each trace's inputs serve as a unique key.
- For traces with matching inputs, expectations overwrite existing entries when the expectation names match.
- New traces from the session are added as fresh records.
- Existing dataset records with different inputs remain unchanged.

```python
session.sync(to_dataset="customer_service_eval_dataset")
```

## Best Practices

### Session Organization
- Use clear, descriptive, date-stamped names (e.g., `customer_service_review_march_2024`).
- Keep sessions focused on specific evaluation goals or time periods.
- Aim for 25–100 traces per session to avoid reviewer fatigue.
- Always store `session.mlflow_run_id` for reliable programmatic access.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### User Management
- Assign users based on domain expertise and availability.
- Distribute labeling work evenly across multiple experts.
- Ensure users have access to the Databricks workspace (if needed, provision via SCIM).^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md) — Overview of human feedback collection
- [Labeling Schemas](/concepts/labeling-schemas.md) — Structured feedback questions used in sessions
- [[MLflow Trace|MLflow Traces]] — Execution traces that are added to sessions
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Target of the sync operation
- [Review App](/concepts/mlflow-review-app.md) — UI where reviewers provide labels
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) — Required for optional Chat UI integration
- Human Feedback Alignment — Improving judge accuracy with expert annotations

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
