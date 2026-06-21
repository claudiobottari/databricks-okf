---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4db39dfbaa57145450a4586f736f5e656a1e50b4329a0ab73376600ac01951c6
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - retrieving-labeling-session-feedback-responses
    - RLSFR
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: Retrieving Labeling Session Feedback Responses
description: The mechanism for accessing reviewer assessments after a labeling session completes, available via the MLflow Experiments UI or programmatically through the MLflow API.
tags:
  - mlflow
  - human-feedback
  - api
timestamp: "2026-06-19T09:33:35.711Z"
---

# Retrieving Labeling Session Feedback Responses

**Retrieving Labeling Session Feedback Responses** refers to the process of accessing human-generated assessments (labels) collected during a labeling session in [MLflow](/concepts/mlflow.md) on Databricks. After domain experts complete their reviews using the [MLflow Review App](/concepts/mlflow-review-app.md), their feedback is stored as `Assessments` on the traces within the session and can be retrieved through either the user interface or the MLflow API. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Overview

Labeling sessions capture feedback or expectation data from domain experts on GenAI applications. When reviewers submit their assessments, MLflow persists these responses and associates them with the specific [[MLflow Trace|MLflow Traces]] that were reviewed. This enables teams to systematically collect and analyze human evaluations for improving their applications. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Retrieving Feedback in the UI

To view reviewer feedback through the MLflow user interface:

1. In the Databricks workspace, click **Experiments** in the left sidebar.
2. Click the experiment name to open it.
3. Click **Labeling sessions** in the sidebar.
4. Click the session name from the list, then click the specific review request.
5. To display reviewers' input, click **Assessments** at the upper right of the page.

A notification appears showing the trace and the reviewer's assessments. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Retrieving Feedback with the API

Reviewer assessments can also be retrieved programmatically using the MLflow API. Since labeling sessions are logged as MLflow runs, you can access the traces and associated assessments using [`mlflow.search_runs()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_runs). ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
import mlflow
import mlflow.genai.labeling as labeling
import pandas as pd

# Get all labeling sessions
all_sessions = labeling.get_labeling_sessions()

# Find session by name (note: names may not be unique)
target_session = None
for session in all_sessions:
    if session.name == "customer_service_review_jan_2024":
        target_session = session
        break

if target_session:
    print(f"Session name: {target_session.name}")
    print(f"Experiment ID: {target_session.experiment_id}")
    print(f"[[mlflow-run|MLflow Run]] ID: {target_session.mlflow_run_id}")
    print(f"Label schemas: {target_session.label_schemas}")
else:
    print("Session not found")

# Alternative: Get session by [[mlflow-run|MLflow Run]] ID (if you know it)
run_id = "your_labeling_session_run_id"
run = mlflow.search_runs(
    experiment_ids=["your_experiment_id"],
    filter_string=f"tags.mlflow.runName LIKE '%labeling_session%' AND attribute.run_id = '{run_id}'"
).iloc[0]
print(f"Found labeling session run: {run['run_id']}")
print(f"Session name: {run['tags.mlflow.runName']}")
```

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Data Structure of Feedback Responses

Each reviewer's assessment contains:

- **Trace reference**: The specific MLflow Trace being evaluated
- **Schema responses**: Answers to the labeling schema questions defined in the session (built-in schemas like `EXPECTED_FACTS`, `EXPECTED_RESPONSE`, `GUIDELINES`, or custom schemas)
- **Reviewer identity**: The assigned user who provided the assessment

Assessments can contain either `Feedback` or `Expectation` data, which can be used for evaluation and improvement workflows. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Best Practices

- **Store the session's [MLflow Run](/concepts/mlflow-run.md) ID** when creating sessions. Use the run ID for programmatic access instead of relying on session names, as session names may not be unique. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

```python
import mlflow.genai.labeling as labeling

# Good: Store run ID for later reference
session = labeling.create_labeling_session(name="my_session", ...)
session_run_id = session.mlflow_run_id  # Store this!

# Later: Use run ID to find session via mlflow.search_runs()
# rather than searching by name through all sessions
```
^[create-and-manage-labeling-sessions-databricks-on-aws.md]

- **Use distinct session names** with date stamps (e.g., `customer_service_review_march_2024`) for better organization.
- **Keep focused sessions** with 25-100 traces to avoid reviewer fatigue.

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md) — The container for traces and feedback collection
- [MLflow Review App](/concepts/mlflow-review-app.md) — The interface where reviewers provide assessments
- [Labeling Schemas](/concepts/labeling-schemas.md) — The questions and format for feedback collection
- [[MLflow Trace|MLflow Traces]] — The execution traces that reviewers evaluate
- Sync to Evaluation Datasets — Converting collected expectations into reusable test datasets
- Human Feedback Alignment — Using expert annotations to improve evaluation quality

## Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
