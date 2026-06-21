---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0bec83e03bf49dc56ac2349d2dbe516f5a509f6d100300526d56867aa36f9c91
  pageDirectory: concepts
  sources:
    - view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-list-view
    - MTLV
  citations:
    - file: view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md
title: MLflow Trace List View
description: A tabular overview of all captured traces in an MLflow Experiment, displaying sortable columns such as Trace ID, Request, Response, Session, User, Execution time, State, Source, and custom assessment/tag columns.
tags:
  - mlflow
  - tracing
  - ui
  - observability
timestamp: "2026-06-19T23:24:50.076Z"
---

## [[mlflow-trace|MLflow Trace]] List View

The **MLflow Trace List View** is the primary interface for browsing and inspecting [Traces](/concepts/traces.md) logged to an [MLflow Experiment](/concepts/mlflow-experiment.md) within the Databricks [MLflow](/concepts/mlflow.md) UI. All captured [Traces](/concepts/traces.md) are stored and served by the managed [MLflow Tracking](/concepts/mlflow-tracking.md) service when `MLFLOW_TRACKING_URI` is set to `databricks`. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

To access the list, navigate to the experiment where [Traces](/concepts/traces.md) are logged and click the **Traces** tab. The view displays a paginated table of all [Traces](/concepts/traces.md) in that experiment, with a set of customizable columns and filtering tools. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

### Columns

The trace list includes sortable columns that give a high‑level summary of each trace:

| Column             | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| Trace ID           | Unique identifier for the trace.                                           |
| Request            | Preview of the input that triggered the trace.                             |
| Response           | Preview of the final output.                                               |
| Session            | Session identifier (if provided), grouping related [Traces](/concepts/traces.md) (e.g., conversation turns). |
| User               | User identifier (if provided).                                             |
| Execution time     | Total wall‑clock duration of the trace.                                    |
| Request time       | Timestamp when the trace was initiated.                                    |
| Run name           | Name of the associated [MLflow Run](/concepts/mlflow-run.md), if linked.                          |
| Source             | Origin of the trace (e.g., instrumented library like `openai`, `langchain`, or a custom name). |
| State              | Status – `OK`, `ERROR`, or `IN_PROGRESS`.                                  |
| Trace name         | Name assigned to the trace (often the root span’s name).                   |
| [Assessments](/concepts/assessments.md)        | One column per assessment type (e.g., `my_scorer`, `professional`). A summary section above the list shows aggregated metrics (averages, pass/fail rates) across visible [Traces](/concepts/traces.md). |
| Tags               | Individual tags can be displayed as columns (e.g., `persona`, `style`).     |

^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

### Search and Filter

The UI provides several ways to narrow down [Traces](/concepts/traces.md):

- **Search bar** – Quickly find [Traces](/concepts/traces.md) by searching the `Request` (input) field.
- **Filters dropdown** – Build structured queries on attributes (`Request`, `Session time`, `Execution time`, `Request time`), [Assessments](/concepts/assessments.md) (`my_scorer`, `professional`), `State`, `Trace name`, `Session`, `User`, and `Tags` (e.g., `tags.persona = 'expert'`).
- **Sort dropdown** – Order by columns like `Request time` or `Execution time`.
- **Columns dropdown** – Show/hide columns, including specific tag or assessment columns.

Metadata filters can be entered directly in the search bar using expressions such as `metadata.\`mlflow.trace.user\` = 'user-123'` or `metadata.app_version = '1.0.0'`. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

### Limitations

- The trace list returns **at most 1,000 traces**. Filters and trace ID search apply only to this set, not the full experiment. Older [Traces](/concepts/traces.md) in large experiments may not appear unless the time range is narrowed to include them.
- Experiments that are **not in [Unity Catalog](/concepts/unity-catalog.md)** are capped at 100,000 total [Traces](/concepts/traces.md). To remove both limits and search across all [Traces](/concepts/traces.md) in a time range, migrate the [Traces](/concepts/traces.md) to [Unity Catalog](/concepts/unity-catalog.md). ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

### Notebook Integration

In Databricks notebooks ([MLflow](/concepts/mlflow.md) 2.20+), the trace UI can appear automatically in cell output when a trace is generated, when `mlflow.search_traces()` is called, or when an `mlflow.entities.Trace` object is the last expression of a cell (or passed to `display()`). The in‑notebook view offers the same rich exploration capabilities as the main Experiments UI. Display can be toggled with `mlflow.tracing.disable_notebook_display()` or `mlflow.tracing.enable_notebook_display()`. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

### Related Concepts

- [MLflow Experiment](/concepts/mlflow-experiment.md)
- [[MLflow Trace]]
- [MLflow Run](/concepts/mlflow-run.md)
- [Traces tab](/concepts/traces.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow Tracing SDK](/concepts/mlflow-tracing.md)
- [Trace Detail View](/concepts/mlflow-trace-detail-view.md)

### Sources

- view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md

# Citations

1. [view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md](/references/view-traces-in-the-databricks-mlflow-ui-databricks-on-aws-d0ec6f89.md)
