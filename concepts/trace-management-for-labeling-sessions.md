---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b1448c7d1e00f8e6c881eb3e5f35ac36bfed070bb02b338004ca546d25dfcf9f
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-management-for-labeling-sessions
    - TMFLS
  citations:
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: Trace Management for Labeling Sessions
description: The process of selecting, adding, and retrieving MLflow Traces within labeling sessions for expert review, supporting both UI and API workflows.
tags:
  - mlflow
  - traces
  - labeling
  - api
timestamp: "2026-06-19T17:59:18.140Z"
---

## Trace Management for Labeling Sessions

**Trace Management for Labeling Sessions** refers to the workflows for adding, organizing, and retrieving [[MLflow Trace|MLflow Traces]] within a [Labeling Session](/concepts/labeling-session.md) on Databricks. A labeling session is a special type of [MLflow Run](/concepts/mlflow-run.md) that holds a curated set of traces for human review using the MLflow Review App. Effective trace management ensures that domain experts can efficiently label the right data points and that the resulting assessments can be used to improve GenAI applications. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Adding Traces to a Session

After a labeling session is created, traces must be added before reviewers can provide labels. Traces can be added through the UI, from search results, or as individual trace objects via the API. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

#### Using the UI

1. In the Databricks workspace, navigate to **Experiments**, select your experiment, then click **Traces** in the sidebar.
2. Check the box next to each trace you want to add.
3. From the **Actions** drop‑down menu, choose **Add to labeling session**.
4. In the dialog, click **Export** next to the target labeling session, then click **Done**. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

#### From Search Results

The `search_traces()` API can be used to programmatically find traces (for example, by filtering on tags) and then add the resulting DataFrame to a session:

```python
traces_df = mlflow.search_traces(
    filter_string="tags.test_tag = 'C001'",
    max_results=50
)
session.add_traces(traces_df)
```

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

#### As Individual Trace Objects

After generating traces with a traced function, you can obtain the trace objects via `mlflow.get_trace(trace_id)` and pass a list to `session.add_traces()`:

```python
trace1 = mlflow.get_trace(trace_id_1)
trace2 = mlflow.get_trace(trace_id_2)
session.add_traces([trace1, trace2])
```

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

#### Rendering Behavior

The Review App renders different data types (dictionaries, OpenAI‑formatted messages, tool calls) in a human‑readable way for labelers. The exact rendering rules are documented separately in the [Review App](/concepts/mlflow-review-app.md) content rendering guide. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Retrieving Feedback Responses

After reviewers submit their assessments, MLflow stores them as `Assessments` on each trace in the session. You can retrieve these responses either in the UI or via the MLflow API. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

- **UI:** Open the labeling session in the **Experiments** UI, click a trace request, then click **Assessments** in the upper‑right corner to see each reviewer’s answers.
- **API:** Use `mlflow.search_runs()` or trace‑focused APIs to access the assessment data programmatically. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Syncing Expectations to Evaluation Datasets

Collected expectations can be synchronized to an [Evaluation Dataset](/concepts/evaluation-dataset.md) using the `sync()` method on the labeling session object. This performs an intelligent upsert:
- The trace’s input acts as a unique key.
- Matching inputs overwrite existing expectations with the same name.
- Unmatched traces are added as new records.
- Existing dataset records with different inputs remain unchanged.

```python
session.sync(to_dataset="customer_service_eval_dataset")
```

^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Best Practices

- Use clear, date‑stamped session names (e.g., `customer_service_review_march_2024`).
- Keep sessions focused on specific evaluation goals or time periods.
- Aim for 25–100 traces per session to avoid reviewer fatigue.
- Always store `session.mlflow_run_id` upon creation, and use it for programmatic access instead of relying on session names, which may not be unique. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Related Concepts

- [Labeling Session](/concepts/labeling-session.md) – The container for traces and assessments.
- [Labeling Schemas](/concepts/labeling-schemas.md) – Define the questions and format for feedback.
- [Review App](/concepts/mlflow-review-app.md) – The UI where domain experts label traces.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) – A dataset that can be augmented with expectations from labeling sessions.
- [[MLflow Trace|MLflow Traces]] – The telemetry data collected from GenAI applications.

### Sources

- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
