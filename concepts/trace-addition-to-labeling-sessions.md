---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eef8f038ec4b91637ed9f22e17140461ffec2ec4f67baa6392eef2d4445f9adb
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-addition-to-labeling-sessions
    - TATLS
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: Trace Addition to Labeling Sessions
description: The workflow of selecting MLflow Traces (via UI or API) and adding them to a labeling session so domain experts can review and label them.
tags:
  - tracing
  - mlflow
  - labeling
  - workflow
timestamp: "2026-06-19T14:34:10.602Z"
---

# Trace Addition to Labeling Sessions

**Trace Addition to Labeling Sessions** is the process of associating [[MLflow Trace|MLflow Traces]] with a [Labeling Session](/concepts/labeling-session.md) so that domain experts can review them and provide [Human Feedback](/concepts/mlflow-human-feedback-collection.md) assessments in the [MLflow Review App](/concepts/mlflow-review-app.md). A labeling session must contain traces before experts can begin labeling; adding traces is the prerequisite step that makes the session ready for review.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Overview

A labeling session is a container for traces and their associated labels (human-generated assessments).^[create-and-manage-labeling-sessions-databricks-on-aws.md] After creating a session, you must populate it with traces. You can add traces using either the MLflow UI or the `add_traces()` API. For API details, see `mlflow.genai.LabelingSession.add_traces`.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

The goal is to collect [Feedback](/concepts/feedback-object.md) or [Expectation](/concepts/feedback-vs-expectation-labels.md) data on existing traces, which can then be used to improve your GenAI application through systematic evaluation.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Adding Traces Using the UI

To add traces to a labeling session in the MLflow UI:

1. In the Databricks workspace, in the left sidebar, click **Experiments**.
2. Click the name of your experiment to open it.
3. Click **Traces** in the sidebar.
4. Select the traces you want to add by checking the box to the left of the Trace ID.
5. From the **Actions** drop-down menu, select **Add to labeling session**.
6. In the dialog, click **Export** next to the labeling session that you want to add the traces to, then click **Done**.

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Adding Traces Using the API

### From Search Results

You can add traces programmatically by first generating them, then searching for traces, and finally adding them to a session.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
import mlflow.genai.labeling as labeling

# Create session and add traces
session = labeling.create_labeling_session(
    name="negative_feedback_review",
    assigned_users=["quality_expert@company.com"],
    label_schemas=["response_quality", "expected_facts"])

# Add traces from search results
session.add_traces(traces_df)
print(f"Added {len(traces_df)} traces to session")
```

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Individual Trace Objects

You can also add individual trace objects to a session. This is useful for targeted scenarios like specific edge cases.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
# Get the trace objects
trace1 = mlflow.get_trace(trace_id_1)
trace2 = mlflow.get_trace(trace_id_2)
trace3 = mlflow.get_trace(trace_id_3)

# Create session and add traces
session = labeling.create_labeling_session(
    name="negative_feedback_review",
    assigned_users=["name@databricks.com"],
    label_schemas=["response_quality", schemas.EXPECTED_FACTS])

# Add individual traces
session.add_traces([trace1, trace2, trace3])
```

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Trace Rendering in the Review App

For details on how traces are rendered and displayed to labelers in the Review App UI — including how different data types (dictionaries, OpenAI messages, tool calls) are presented — see [Review App Content Rendering](/concepts/review-app-content-rendering.md).^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Best Practices

- **Aim for 25–100 traces per session** to avoid reviewer fatigue.^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **Use the `mlflow_run_id`** for programmatic access instead of relying on session names, as session names might not be unique.^[create-and-manage-labeling-sessions-databricks-on-aws.md]
- **Keep sessions focused** on specific evaluation goals or time periods.^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Related Concepts

- [Labeling Session](/concepts/labeling-session.md) — The container for organizing traces and human feedback.
- [[MLflow Trace|MLflow Traces]] — The trace objects that are added to sessions for review.
- [Human Feedback](/concepts/mlflow-human-feedback-collection.md) — Expert assessments collected through the labeling process.
- [MLflow Review App](/concepts/mlflow-review-app.md) — The UI where domain experts review and label traces.
- [Labeling Schema](/concepts/labeling-schema.md) — The structure for feedback and expectation questions.
- [Add Traces to Labeling Session UI](/concepts/add-traces-to-labeling-session.md) — UI-based trace addition workflow.
- Retrieve Feedback Responses — Accessing stored Assessments after labeling.

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
