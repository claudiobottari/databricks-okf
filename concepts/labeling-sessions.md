---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea95266567f61017b7b8e168ae07a0c014a2480482e7b18ae9dd673f4bb97981
  pageDirectory: concepts
  sources:
    - collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-sessions
    - Create labeling sessions
  citations:
    - file: collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: Labeling Sessions
description: A special type of MLflow Run that organizes a set of traces for review by specific experts using selected labeling schemas, acting as a queue for the review process.
tags:
  - mlflow
  - labeling
  - workflow
timestamp: "2026-06-19T17:46:02.489Z"
---

# Labeling Sessions

**Labeling Sessions** are a special type of [MLflow Run](/concepts/mlflow-run.md) that organizes a set of traces for review by domain experts using selected labeling schemas. A labeling session acts as a container for traces and their associated labels, enabling systematic feedback collection that can drive evaluation and improvement workflows.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## How Labeling Sessions Work

When you create a labeling session, you define several key parameters:

- **Name** – A descriptive identifier for the session.
- **Assigned users** – Domain experts who will provide labels.
- **Agent** – (Optional) The GenAI app to generate responses if needed.
- **Labeling schemas** – The questions and format for feedback collection. You can use built-in schemas or create custom ones.
- **Multi-turn chat** – Whether to support conversation-style labeling.

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

When you add traces to a labeling session, they are copied into the session, so any labels or modifications made during the review process do not affect the original logged traces.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

Labeling sessions appear in the **Evaluations** tab of the MLflow UI. Because labeling sessions are logged as MLflow runs, you can also access the traces and associated assessments using the MLflow API.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## When to Use Labeling Sessions

Labeling sessions are valuable for several use cases:

- Understanding what high-quality, correct responses look like for specific queries.
- Collecting input to align [LLM Judges](/concepts/llm-judges.md) with business requirements.
- Creating [Evaluation Datasets](/concepts/evaluation-datasets.md) from production traces.
- Reviewing traces with ambiguous or borderline quality.
- Handling edge cases not covered by automated judges.
- Evaluating examples where automated metrics disagree with expected quality.
- Reviewing representative samples of different user interaction patterns.

^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Prerequisites

Before creating labeling sessions, ensure the following requirements are met:

- **MLflow version**: MLflow 3.1.0 or above is required.
- **Development environment**: Must be connected to the [MLflow Experiment](/concepts/mlflow-experiment.md) where your GenAI application traces are logged.
- **Domain expert permissions**: Experts must be provisioned in your Databricks account and have `CAN_EDIT` permission on the MLflow experiment. They do not need access to your Databricks workspace.

^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Creating Labeling Sessions

You can create labeling sessions using the UI or the API. Session names might not be unique, so you should use the [MLflow Run](/concepts/mlflow-run.md) ID (`session.mlflow_run_id`) to store and reference sessions programmatically.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Create Using the UI

1. In the Databricks workspace, in the left sidebar, click **Experiments**.
2. Click the name of your experiment to open it.
3. Click **Labeling sessions** in the sidebar.
4. Click **Create session**.
5. Enter a name for the session. You can also optionally specify an evaluation dataset or select labeling schemas. The **Label preview** section lets you view how the questions appear for reviewers.
6. When ready, click **Create Session**.
7. To share the session with reviewers, click the session name in the list, then click **Share** at the upper right, enter an email address for each reviewer, and click **Save**. Reviewers are notified and given access to the review app.

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Create Using the API

The following examples demonstrate common API usage patterns.

#### Create a Basic Session

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

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

#### Create a Session Using Custom Label Schemas

```python
import mlflow.genai.labeling as labeling
import mlflow.genai.label_schemas as schemas

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

## Adding Traces to Sessions

After creating a labeling session, you must add traces to it for expert review. You can add traces using the UI or the `add_traces()` API.

### Add Using the UI

1. In the Databricks workspace, click **Experiments**, then the experiment name.
2. Click **Traces** in the sidebar.
3. Select the traces by checking the box to the left of the Trace ID.
4. From the **Actions** drop-down menu, select **Add to labeling session**.
5. In the dialog, click **Export** next to the labeling session you want to add the traces to, then click **Done**.

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Add Using the API

```python
import mlflow

traces = mlflow.search_traces(model_id=tracked_model.model_id)

label_summaries.add_traces(traces)

print(f"Share this Review App with your team: {label_summaries.url}")
```

^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Labeling Schemas

Labeling schemas define the questions and input types that domain experts use to provide feedback. There are two main types:

- **Expectation Type (`type="expectation"`)**: Used when the expert provides a "ground truth" or correct answer. These labels can often be directly used in evaluation datasets.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]
- **Feedback Type (`type="feedback"`)**: Used for subjective assessments, ratings, or classifications.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

Schemas support various input methods including categorical choices, numeric scales, and free-form text. You can use built-in schemas (`EXPECTED_FACTS`, `EXPECTED_RESPONSE`, `GUIDELINES`) or create custom ones.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md, create-and-manage-labeling-sessions-databricks-on-aws.md]

## Managing Labeling Sessions

### Retrieve Sessions

```python
import mlflow.genai.labeling as labeling

all_sessions = labeling.get_labeling_sessions()
print(f"Found {len(all_sessions)} sessions")
for session in all_sessions:
    print(f"- {session.name} (ID: {session.labeling_session_id})")
    print(f"  Assigned users: {session.assigned_users}")
```

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Get a Specific Session

```python
import mlflow.genai.labeling as labeling

all_sessions = labeling.get_labeling_sessions()
target_session = None
for session in all_sessions:
    if session.name == "customer_service_review_jan_2024":
        target_session = session
        break

if target_session:
    print(f"Session name: {target_session.name}")
    print(f"Experiment ID: {target_session.experiment_id}")
    print(f"[[mlflow-run|MLflow Run]] ID: {target_session.mlflow_run_id}")
```

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Delete Sessions

```python
import mlflow.genai.labeling as labeling

all_sessions = labeling.get_labeling_sessions()
session_to_delete = None
for session in all_sessions:
    if session.name == "customer_service_review_jan_2024":
        session_to_delete = session
        break

if session_to_delete:
    labeling.delete_labeling_session(session_to_delete)
    print(f"Deleted session: {session_to_delete.name}")
```

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Manage Assigned Users

To add users to existing sessions, use `set_assigned_users`:

```python
import mlflow.genai.labeling as labeling

all_sessions = labeling.get_labeling_sessions()
session = None
for s in all_sessions:
    if s.name == "customer_review_session":
        session = s
        break

if session:
    new_users = ["expert2@company.com", "expert3@company.com"]
    session.set_assigned_users(session.assigned_users + new_users)
    print(f"Session now has users: {session.assigned_users}")
```

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

To replace all assigned users, pass a new list:

```python
session.set_assigned_users(["new_expert@company.com", "lead_reviewer@company.com"])
```

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Review App Integration

After a labeling session is populated with traces, you can share its URL with domain experts. They use the [Review App](/concepts/mlflow-review-app.md) to view traces and provide feedback using the configured labeling schemas.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md] The Review App automatically renders different content types from MLflow Traces, including:

- **Retrieved documents**: Documents within a `RETRIEVER` span are rendered for display.
- **OpenAI format messages**: Inputs and outputs following OpenAI chat conversation format.
- **Dictionaries**: Inputs and outputs that are dicts are rendered as pretty-printed JSONs.

^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Retrieving Collected Labels

After domain experts complete their reviews, the collected feedback is attached to the traces within the labeling session. Labels are stored as `Assessment` objects on each `Trace` within the session. You can retrieve them programmatically:^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

```python
labeled_traces_df = mlflow.search_traces(run_id=label_summaries.mlflow_run_id)
```

^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

To view labels using the UI, open the **Experiments** UI, click the labeling session, then click the request. Click **Assessments** at the upper right to view each reviewer's responses.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Sync to Evaluation Datasets

You can synchronize collected expectations (labels of type `"expectation"`) to [Evaluation Datasets](/concepts/evaluation-datasets.md) using the `sync()` method. The sync performs an intelligent upsert operation:

- Each trace's inputs serve as a unique key to identify records in the dataset.
- For traces with matching inputs, expectations from the labeling session overwrite existing expectations when the expectation names are the same.
- Traces from the labeling session that do not match existing trace inputs are added as new records.
- Existing dataset records with different inputs remain unchanged.

This approach allows you to iteratively improve your evaluation dataset by adding new examples and updating ground truth for existing examples.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
import mlflow.genai.labeling as labeling

all_sessions = labeling.get_labeling_sessions()
session = None
for s in all_sessions:
    if s.name == "completed_review_session":
        session = s
        break

if session:
    session.sync(to_dataset="customer_service_eval_dataset")
    print("Synced expectations to evaluation dataset")
```

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Customizing the Review App UI

For use cases requiring custom trace visualization, tailored labeling interfaces, or specific workflows, you can deploy a customizable Review App template. This open-source template uses the same MLflow backend APIs and data model (labeling sessions, schemas, and assessments) while giving you full control over the frontend experience. Customization options include specialized trace renderers, custom labeling interface layouts, and domain-specific visualizations. The template deploys as a Databricks App and integrates directly with your existing MLflow experiments and labeling sessions.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Best Practices

### Session Organization

- Use clear, descriptive, date-stamped names, such as `customer_service_review_march_2024`.
- Keep sessions focused on specific evaluation goals or time periods.
- Aim for 25–100 traces per session to avoid reviewer fatigue.
- Always store the `session.mlflow_run_id` when you create a session. Use the run ID for programmatic access instead of relying on session names, as the session name might not be unique.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### User Management

- Assign users based on domain expertise and availability.
- Distribute labeling work evenly across multiple experts.
- Any user in the Databricks account can be assigned to a labeling session, regardless of whether they have workspace access. When you assign users, the system automatically grants necessary `WRITE` permissions on the MLflow Experiment containing the labeling session.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Related Concepts

- [Review App](/concepts/mlflow-review-app.md) — The interface used by domain experts to label traces.
- [Labeling Schemas](/concepts/labeling-schemas.md) — Definitions of questions and input types for feedback collection.
- [MLflow Experiment](/concepts/mlflow-experiment.md) — The container for traces and labeling sessions.
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Datasets created from expectation-type labels.
- [LLM Judges](/concepts/llm-judges.md) — Automated evaluation tools that can be aligned using expert feedback.
- [Traces](/concepts/traces.md) — The execution records that are reviewed in labeling sessions.

## Sources

- collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md](/references/collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws-baf6bcf1.md)
2. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
