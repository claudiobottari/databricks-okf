---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9f2ffef3b81eda27330d33cc9d552da9e199c82c704535b29f714e086b911d49
  pageDirectory: concepts
  sources:
    - view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-debugging-workflows-in-mlflow
    - TDWIM
  citations:
    - file: view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md
title: Trace Debugging Workflows in MLflow
description: Common observability and debugging patterns using the MLflow Tracing UI, including identifying slow traces (sort by execution time), finding user-specific traces (filters/tags), locating error traces (filter by State=ERROR), and identifying negative feedback traces (assessment filters).
tags:
  - mlflow
  - tracing
  - debugging
  - observability
timestamp: "2026-06-19T23:25:14.840Z"
---

# Trace Debugging Workflows in [MLflow](/concepts/mlflow.md)

**Trace Debugging Workflows in MLflow** describes how to use the Databricks [MLflow](/concepts/mlflow.md) UI to inspect, search, and analyze [traces](/concepts/mlflow-tracing.md) for debugging and observability of GenAI applications. The UI provides tools to identify latency bottlenecks, locate user-specific [Traces](/concepts/traces.md), find errors, and detect negative feedback, all within the context of an [MLflow Experiments|MLflow Experiment](/concepts/mlflow-experiment.md). ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Accessing and Navigating [Traces](/concepts/traces.md)

All captured [Traces](/concepts/traces.md) are logged to an [MLflow Experiment](/concepts/mlflow-experiment.md). To view them, navigate to the experiment in the Databricks workspace and open the **Traces** tab. The trace list shows a high-level overview with sortable columns, including Trace ID, Request preview, Response preview, Execution time, State (e.g., `OK`, `ERROR`, `IN_PROGRESS`), and assessment columns. You can customize which columns appear using the **Columns** dropdown. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

The UI offers several ways to filter and search [Traces](/concepts/traces.md):

- **Search bar**: Find [Traces](/concepts/traces.md) by searching the content of the `Request` (input) field.
- **Filters dropdown**: Build structured queries based on attributes (e.g., `Request` content, `Session time`, `Execution time`), [Assessments](/concepts/assessments.md) (e.g., `my_scorer`, `professional`), state, trace name, session, user, or tags (e.g., `tags.persona = 'expert'`).
- **Sort dropdown**: Order [Traces](/concepts/traces.md) by columns like `Request time` or `Execution time`.
- **Metadata filters**: Use search queries such as `` metadata.`mlflow.trace.user` = 'user-123' `` or `` metadata.`mlflow.source.type` = 'production' `` to filter by attached metadata. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Exploring an Individual Trace

Clicking a trace’s **Request** or **Trace Name** opens the detailed trace view with three main panels:

- **Trace breakdown (Left Panel)**: Displays the span hierarchy as a tree or waterfall chart, showing parent–child relationships, execution order, and duration. Selecting a span reveals its details.
- **Span Details (Center Panel)**: Shows information for the selected span, organized into tabs – **Chat** (rendered conversation for LLM chat interactions), **Inputs / Outputs** (raw data), **Attributes** (key-value metadata like `model` name or `temperature`), and **Events** (exception details, stack [Traces](/concepts/traces.md), or streaming data chunks).
- **Assessments (Right Panel)**: Displays any user feedback or evaluation scores for the entire trace or the selected span. Includes an **"+ Add new assessment"** button to log feedback directly from the UI. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

The detailed view also provides overall trace information, including trace-level tags and [Assessments](/concepts/assessments.md), which may originate from direct User Feedback|user feedback or systematic [Evaluations|evaluations](/concepts/evaluation-runs.md). ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Common Debugging Scenarios

### Identify Slow [Traces](/concepts/traces.md) (Latency Bottlenecks)

In the trace list, sort by **Execution time** descending to bring the slowest [Traces](/concepts/traces.md) to the top. Opening a slow trace and examining the **Trace breakdown** panel reveals which spans took the longest, helping pinpoint Latency Bottlenecks|latency bottlenecks within the application flow. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

### Find [Traces](/concepts/traces.md) from a Particular User

If user information is tracked (e.g., via `mlflow.trace.user`), use the **Filters** dropdown to select the user attribute, or search with a tag query like `tags.[MLflow](/concepts/mlflow.md).trace.user = 'user_example_123'`. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

### Locate [Traces](/concepts/traces.md) with Failures (Errors)

Use the **Filters** dropdown to set `State` to `ERROR`. In the detailed view, select the error-marked span in the **Trace breakdown** and navigate to its **Events** tab to view exception messages and stack [Traces](/concepts/traces.md). ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

### Identify [Traces](/concepts/traces.md) with Negative Feedback or Issues

If [assessments](/concepts/assessments.md) (user feedback or evaluation scores) are collected, use the **Filters** dropdown to filter by assessment name and value (e.g., `is_correct = false` or `relevance_score < 0.5`). Opening a trace reveals logged feedback in the **Assessments** panel, helping understand why a response was marked poor quality. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Tracing in Databricks Notebooks

[MLflow Tracing](/concepts/mlflow-tracing.md) (available in [MLflow](/concepts/mlflow.md) 2.20 and above) provides a seamless experience within Databricks Notebooks. When the [MLflow tracking URI](/concepts/mlflow-tracking-uri.md) is set to `"databricks"`, [Traces](/concepts/traces.md) are automatically displayed in cell outputs when code generates a trace, `mlflow.search_traces()` is called, or an `mlflow.entities.Trace` object is the last expression in a cell. The in-notebook view offers the same interactive trace exploration as the Experiments UI, enabling faster iteration. To control automatic display, use `mlflow.tracing.disable_notebook_display()` or `mlflow.tracing.enable_notebook_display()`. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Limitations

- The trace list returns at most 1,000 [Traces](/concepts/traces.md); filters and trace ID search apply only to this set, so older [Traces](/concepts/traces.md) in large experiments might not appear. Narrowing the time range can include them.
- Experiments not in [Unity Catalog](/concepts/unity-catalog.md) are capped at 100,000 [Traces](/concepts/traces.md). To remove both limits and search across all [Traces](/concepts/traces.md) in a time range, migrate to [Traces in Unity Catalog](/concepts/model-traces-in-unity-catalog.md). ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- Observability
- [User Feedback](/concepts/multi-dimensional-user-feedback.md)
- [Evaluations](/concepts/evaluation-runs.md)
- Databricks Notebooks
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md

# Citations

1. [view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md](/references/view-traces-in-the-databricks-mlflow-ui-databricks-on-aws-d0ec6f89.md)
