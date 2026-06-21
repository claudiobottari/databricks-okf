---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 678caeee97e4d13710251e428bd53b9ec2ba983b791317b007b4588487cba25b
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-labeling-sessions
    - MLS
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: MLflow Labeling Sessions
description: A structured mechanism for gathering human-generated assessments (labels) from domain experts on GenAI application traces, implemented as a special type of MLflow run.
tags:
  - mlflow
  - human-feedback
  - genai
  - labeling
timestamp: "2026-06-19T17:59:07.524Z"
---

# MLflow Labeling Sessions

**MLflow Labeling Sessions** provide a structured mechanism for collecting expert feedback on GenAI application traces. A labeling session is a special type of [MLflow Run](/concepts/mlflow-run.md) that groups a set of traces for review by domain experts, who can then submit structured assessments such as accuracy scores or ideal responses. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## How Labeling Sessions Work

A labeling session acts as a container for traces and their associated labels, enabling systematic feedback collection that can drive evaluation and improvement workflows. When you create a labeling session, you define a name, assigned users, optional agent connection, labeling schemas, and whether to support multi-turn chat. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

Because labeling sessions are logged as MLflow runs, you can access the traces and associated assessments using the MLflow API `mlflow.search_runs()`. Labeling sessions appear in the **Evaluations** tab of the MLflow UI. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

The optional **Agent** field connects a labeling session to the Review App's Chat UI for interactive testing. The Chat UI requires an agent deployed to a Model Serving endpoint and does not currently support agents deployed on Databricks Apps. Reviewing and labeling existing traces works regardless of how your agent is deployed. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Creating Labeling Sessions

You can create labeling sessions using the UI or the API. Session names might not be unique, so use the [MLflow Run](/concepts/mlflow-run.md) ID (`session.mlflow_run_id`) to store and reference sessions. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Create Sessions Using the UI

To create a labeling session in the MLflow UI:

1. In the Databricks workspace, click **Experiments** in the left sidebar.
2. Click the name of your experiment to open it.
3. Click **Labeling sessions** in the sidebar.
4. Click **Create session**.
5. Enter a name for the session. You can also optionally specify an evaluation dataset or select labeling schemas.
6. Click **Create Session**.
7. To share the session with reviewers, click the session name, then click **Share** at the upper right.
8. Enter an email address for each reviewer and click **Save**. Reviewers are notified and given access to the review app.

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Create Sessions Using the API

To create sessions with full programmatic control, use `mlflow.genai.labeling.create_labeling_session()`. The following example creates a basic session with built-in schemas: ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

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

You can also create sessions using custom label schemas: ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

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

## Managing Labeling Sessions

You can retrieve, view, and delete labeling sessions using the API. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Retrieve Sessions

```python
all_sessions = labeling.get_labeling_sessions()
for session in all_sessions:
    print(f"- {session.name} (ID: {session.labeling_session_id})")
```

### Get a Specific Session

```python
all_sessions = labeling.get_labeling_sessions()
target_session = None
for session in all_sessions:
    if session.name == "customer_service_review_jan_2024":
        target_session = session
        break
if target_session:
    print(f"Session name: {target_session.name}")
    print(f"[[mlflow-run|MLflow Run]] ID: {target_session.mlflow_run_id}")
```

### Delete Sessions

```python
session_to_delete = None
for session in labeling.get_labeling_sessions():
    if session.name == "customer_service_review_jan_2024":
        session_to_delete = session
        break
if session_to_delete:
    labeling.delete_labeling_session(session_to_delete)
```

## Adding Traces to Sessions

After creating a session, you must add traces for expert review. You can do this using the UI or the `add_traces()` API. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Add Traces Using the UI

1. Click **Experiments** in the left sidebar, then click your experiment.
2. Click **Traces** in the sidebar.
3. Select the traces by checking the box to the left of the Trace ID.
4. From the **Actions** drop-down menu, select **Add to labeling session**.
5. In the dialog, click **Export** next to the labeling session, then click **Done**.

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Add Traces Using the API

```python
traces_df = mlflow.search_traces(
    filter_string="tags.test_tag = 'C001'",
    max_results=50
)
session = labeling.create_labeling_session(
    name="negative_feedback_review",
    assigned_users=["quality_expert@company.com"],
    label_schemas=["response_quality", "expected_facts"]
)
session.add_traces(traces_df)
```

You can also add individual trace objects: ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
trace1 = mlflow.get_trace(trace_id_1)
trace2 = mlflow.get_trace(trace_id_2)
session.add_traces([trace1, trace2])
```

## Retrieving Feedback Responses

After reviewers complete a labeling session, MLflow stores their responses as `Assessments` on the traces. You can retrieve them in the UI or with the MLflow API. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

To view reviewer feedback in the UI, click the session name in the list, then click the request. Click **Assessments** at the upper right to view each reviewer's responses. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Managing Assigned Users

Any user in the Databricks account can be assigned to a labeling session, regardless of whether they have workspace access. However, granting a user permission to a labeling session gives them access to the labeling session's MLflow experiment. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

When you assign users to a labeling session, the system automatically grants necessary `WRITE` permissions on the MLflow Experiment containing the labeling session. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Add Users to Existing Sessions

```python
session.set_assigned_users(session.assigned_users + ["expert2@company.com", "expert3@company.com"])
```

### Replace Assigned Users

```python
session.set_assigned_users(["new_expert@company.com", "lead_reviewer@company.com"])
```

## Syncing to Evaluation Datasets

You can synchronize collected `Expectations` to Evaluation Datasets using the `sync()` method. The method performs an intelligent upsert operation: ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

- Each trace's inputs serve as a unique key to identify records in the dataset.
- For traces with matching inputs, expectations from the labeling session overwrite existing expectations when the expectation names are the same.
- Traces that do not match existing trace inputs are added as new records.
- Existing dataset records with different inputs remain unchanged.

```python
session.sync(to_dataset="customer_service_eval_dataset")
```

## Best Practices

- Use clear, descriptive, date-stamped names, such as `customer_service_review_march_2024`.
- Keep sessions focused on specific evaluation goals or time periods.
- Aim for 25-100 traces per session to avoid reviewer fatigue.
- Always store the `session.mlflow_run_id` when creating a session for programmatic access instead of relying on session names, as session names might not be unique.
- Assign users based on domain expertise and availability.
- Distribute labeling work evenly across multiple experts.

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Related Concepts

- [Labeling Schemas](/concepts/labeling-schemas.md) — The structured feedback templates used within labeling sessions
- [[MLflow Trace|MLflow Traces]] — The execution records that are reviewed in labeling sessions
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational context under which labeling sessions are logged
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Convert labeled sessions into test datasets
- Human Feedback Alignment — Using expert annotations to improve judge accuracy
- [Review App](/concepts/mlflow-review-app.md) — The interface where domain experts review and label traces

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
