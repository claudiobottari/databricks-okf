---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 05839e39f17b08357e1dbe36badb0d9f03b267c18f863a8d7c4490f96c7f69ca
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-session
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: Labeling Session
description: A structured MLflow run container that collects human-generated assessments (feedback or expectations) from domain experts on GenAI application traces using the MLflow Review App.
tags:
  - mlflow
  - human-feedback
  - genai
  - labeling
timestamp: "2026-06-18T14:51:21.254Z"
---

# Labeling Session

A **labeling session** is a structured container within [MLflow](/concepts/mlflow.md) that collects human-generated assessments (labels) from domain experts on the behavior of GenAI applications. It is a special type of [MLflow Run](/concepts/mlflow-run.md) that holds a specific set of [[MLflow Trace|MLflow Traces]] for review using the [MLflow Review App](/concepts/mlflow-review-app.md). The goal is to capture either **Feedback** or **Expectation** data, which can then drive systematic evaluation and improvement of the GenAI app. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

Labeling sessions appear in the **Evaluations** tab of the MLflow UI. Because they are logged as MLflow runs, you can also access the traces and associated assessments programmatically via `mlflow.search_runs()`. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## How Labeling Sessions Work

A labeling session acts as a container that groups traces with their associated labels. When creating a session, you define:

- **Name**: A descriptive identifier.
- **Assigned users**: Domain experts who will provide labels.
- **Agent** (optional): The GenAI app to generate responses if needed (connects to the Review App's Chat UI for interactive testing).
- **Labeling schemas**: Questions and format for feedback collection. You can use built-in schemas (`EXPECTED_FACTS`, `EXPECTED_RESPONSE`, `GUIDELINES`) or create custom ones. See [Create and manage labeling schemas](/concepts/labeling-schemas.md).
- **Multi-turn chat**: Whether to support conversation-style labeling.

The optional **Agent** field connects the session to the Review App's Chat UI for interactive testing. The Chat UI requires an agent deployed to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) and does not currently support agents deployed on Databricks Apps. Reviewing and labeling existing traces works regardless of how the agent is deployed. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Creating Labeling Sessions

Sessions can be created through the UI or the API. Session names might not be unique, so always use the [MLflow Run](/concepts/mlflow-run.md) ID (`session.mlflow_run_id`) to store and reference sessions programmatically. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Using the UI

1. In the Databricks workspace, click **Experiments** in the left sidebar.
2. Click your experiment to open it.
3. Click **Labeling sessions** in the sidebar.
4. Click **Create session**, fill in the name, optionally specify an evaluation dataset or select labeling schemas, and preview how questions will appear.
5. Click **Create Session**.
6. To share the session with reviewers, click the session name, then **Share** at the upper right, enter email addresses, and save. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Using the API

Use `mlflow.genai.labeling.create_labeling_session()` for full programmatic control. At minimum you must provide a name, a list of assigned users (email addresses), and one or more label schemas.

**Basic example:**

```python
import mlflow.genai.labeling as labeling
import mlflow.genai.label_schemas as schemas

session = labeling.create_labeling_session(
    name="customer_service_review_jan_2024",
    assigned_users=["alice@company.com", "bob@company.com"],
    label_schemas=[schemas.EXPECTED_FACTS]
)
```

**Using custom schemas:**

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

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Managing Labeling Sessions

### Retrieving Sessions

Use `mlflow.genai.get_labeling_sessions()` to list all sessions. You can filter by name, but remember names may not be unique; prefer using the [MLflow Run](/concepts/mlflow-run.md) ID.

```python
all_sessions = labeling.get_labeling_sessions()
for session in all_sessions:
    print(f"- {session.name} (ID: {session.labeling_session_id})")
```

### Getting a Specific Session

To retrieve a specific session, iterate through all sessions and match by name, or use `mlflow.search_runs()` filtering on the experiment and run ID.

```python
run_id = "your_labeling_session_run_id"
run = mlflow.search_runs(
    experiment_ids=["your_experiment_id"],
    filter_string=f"tags.mlflow.runName LIKE '%labeling_session%' AND attribute.run_id = '{run_id}'"
).iloc[0]
```

### Deleting Sessions

Use `mlflow.genai.delete_labeling_session()` to remove a session from the Review App.

```python
review_app = labeling.delete_labeling_session(session_to_delete)
```

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Adding Traces to Sessions

After creating a session, you must add traces for expert review. Traces can be added via the UI or the `add_traces()` API.

### Using the UI

1. Open the experiment, click **Traces** in the sidebar.
2. Select traces by checking the box to the left of the Trace ID.
3. From the **Actions** drop-down menu, select **Add to labeling session**.
4. In the dialog, click **Export** next to the target labeling session, then click **Done**.

### Using the API

You can add traces from search results:

```python
traces_df = mlflow.search_traces(filter_string="tags.test_tag = 'C001'", max_results=50)
session.add_traces(traces_df)
```

Or add individual trace objects:

```python
trace1 = mlflow.get_trace(trace_id_1)
session.add_traces([trace1, trace2, trace3])
```

For details on how traces are rendered in the Review App UI (e.g., dictionaries, OpenAI messages, tool calls), see [Review App Content Rendering](/concepts/review-app-content-rendering.md). ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Retrieving Feedback Responses

After reviewers complete a session, MLflow stores their responses as **Assessments** on the traces. You can view them in the UI:

- Open the **Experiments** UI, click the labeling session, then click the request.
- Click **Assessments** at the upper right to see each reviewer's responses.

You can also retrieve assessments programmatically using the MLflow API. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Managing Assigned Users

Any user in the Databricks account can be assigned to a labeling session, regardless of workspace access. Granting permission to a session also grants access to the session’s MLflow experiment. When users are assigned, the system automatically grants necessary `WRITE` permissions on the experiment. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Adding Users to Existing Sessions

Use `set_assigned_users()` to update the user list.

```python
session.set_assigned_users(session.assigned_users + ["expert2@company.com"])
```

### Replacing Users

```python
session.set_assigned_users(["new_expert@company.com", "lead_reviewer@company.com"])
```

### User Access Setup

- For users without workspace access, an account admin uses account-level SCIM provisioning to sync users from the identity provider.
- For users who already have workspace access, no additional configuration is required. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Syncing to Evaluation Datasets

Expectations collected in a labeling session can be synchronized to [Evaluation Datasets](/concepts/evaluation-datasets.md) using the `sync()` method. This performs an intelligent upsert: trace inputs serve as unique keys; matching expectations overwrite existing ones; non-matching traces are added as new records; existing records with different inputs remain unchanged.

```python
session.sync(to_dataset="customer_service_eval_dataset")
```

This allows iterative improvement of evaluation datasets by adding new examples and updating ground truth. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Best Practices

- Use clear, descriptive, date-stamped names (e.g., `customer_service_review_march_2024`).
- Keep sessions focused on specific evaluation goals or time periods.
- Aim for **25–100 traces per session** to avoid reviewer fatigue.
- Always store `session.mlflow_run_id` for reliable programmatic access; do not rely on session names alone.
- Assign users based on domain expertise and availability; distribute work evenly.
- Ensure users have access to the Databricks workspace. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
