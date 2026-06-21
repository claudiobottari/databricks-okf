---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 889c42da905439f28ac9222f7f05d2b17301798f37ce0ee62b9c45f4951d60d3
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - adding-traces-to-labeling-sessions
    - ATTLS
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: Adding Traces to Labeling Sessions
description: The process of selecting and associating existing MLflow Traces (via UI or API) with a labeling session for expert review, supporting bulk selection from search results and individual trace objects.
tags:
  - mlflow
  - traces
  - human-feedback
timestamp: "2026-06-19T09:33:32.565Z"
---

# Adding Traces to Labeling Sessions

**Adding traces to labeling sessions** is the process of selecting MLflow traces — recorded interactions between a GenAI application and a user — and associating them with a [Labeling Session](/concepts/labeling-session.md) so that domain experts can review and assess them using the MLflow Review App.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

Traces are the core input to a labeling session. Without traces added to the session, there is nothing for reviewers to evaluate. You can add traces either through the Databricks UI or programmatically using the MLflow API. For details on how traces are rendered and displayed to labelers in the Review App UI, including how different data types (dictionaries, OpenAI messages, tool calls) are presented, see [Review App Content Rendering](/concepts/review-app-content-rendering.md).^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Prerequisites

Before you can add traces to a labeling session, you must have:

- A GenAI application instrumented with [MLflow Tracing](/concepts/mlflow-tracing.md) — see [MLflow Tracing](/concepts/mlflow-tracing.md) for setup guidance.
- An existing [Labeling Session](/concepts/labeling-session.md) — created via the UI or the `create_labeling_session()` API.
- A Databricks workspace with the **Experiments** sidebar enabled.

## Adding Traces Using the UI

The UI workflow is the simplest way to add traces to an existing labeling session:

1. Navigate to the **Experiments** page in the Databricks workspace (left sidebar → **Experiments**).
2. Click the name of your experiment to open it.
3. Click **Traces** in the sidebar.
4. Select the traces you want to add by checking the box to the left of the Trace ID.
5. From the **Actions** drop-down menu, select **Add to labeling session**.
6. In the dialog that appears, click **Export** next to the labeling session you want to add the traces to, then click **Done**.

A dialog appears listing existing labeling sessions for the experiment. After you confirm, the selected traces are associated with the session and become available for reviewers.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Adding Traces Using the API

For programmatic control, use the `add_traces()` method on a `LabelingSession` object. This approach is useful when you want to add traces as part of an automated pipeline or need to handle large numbers of traces.

### Adding Traces from Search Results

You can add traces by first searching for them with `mlflow.search_traces()` and then adding the results to a session:

```python
# Search for traces with a specific filter
traces_df = mlflow.search_traces(
    filter_string="tags.test_tag = 'C001'",
    max_results=50
)

# Create session and add traces
session = labeling.create_labeling_session(
    name="negative_feedback_review",
    assigned_users=["quality_expert@company.com"],
    label_schemas=["response_quality", "expected_facts"]
)

# Add traces from search results
session.add_traces(traces_df)
print(f"Added {len(traces_df)} traces to session")
```

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Adding Individual Trace Objects

You can also add individual trace objects directly:

```python
# Generate specific traces for edge cases
with mlflow.start_run() as run:
    # Create traces for specific scenarios
    support_app("What's your refund policy?")
    trace_id_1 = mlflow.get_last_active_trace_id()
    support_app("How do I cancel my subscription?")
    trace_id_2 = mlflow.get_last_active_trace_id()
    support_app("The website is down")
    trace_id_3 = mlflow.get_last_active_trace_id()

# Get the trace objects
trace1 = mlflow.get_trace(trace_id_1)
trace2 = mlflow.get_trace(trace_id_2)
trace3 = mlflow.get_trace(trace_id_3)

# Add individual traces
session.add_traces([trace1, trace2, trace3])
```

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## What Happens After Adding Traces

Once traces are added to a labeling session:

- **Reviewers are notified** — The system sends notifications to the assigned users, granting them access to the Review App.
- **Traces become available for labeling** — Reviewers can see the traces in the session and provide their assessments.
- **Assessments are stored** — When reviewers complete their work, MLflow stores their responses as `Assessments` on the traces in the session.

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Best Practices

- **Select a representative sample** — Choose traces that cover the range of scenarios you want to evaluate. Avoid adding every trace; aim for 25–100 traces per session to prevent reviewer fatigue.^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **Use clear filter strings** — When using the `add_traces` API, define filter strings that select traces matching your evaluation goals. Use [MLflow tags](/concepts/mlflow-trace-tags.md) to categorize traces by scenario or priority.
- **Store the session run ID** — Always save `session.mlflow_run_id` when creating a session. Use the run ID for programmatic access instead of relying on session names, which may not be unique.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md) — The container that holds traces and their assessments
- [Review App](/concepts/mlflow-review-app.md) — The interface where reviewers provide labels
- [Labeling Schemas](/concepts/labeling-schemas.md) — The questions and format for feedback collection
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The instrumentation layer that creates the traces
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Where labeled expectations can be synced for systematic evaluation

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
