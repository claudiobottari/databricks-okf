---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 995f2a8cfa2ce661ad710672be5f1778fc3dc7b7fc53d07edb599835ce1560ac
  pageDirectory: concepts
  sources:
    - view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-in-databricks-notebooks
    - MTIDN
  citations:
    - file: view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md
title: MLflow Tracing in Databricks Notebooks
description: Seamless integration that displays interactive trace exploration directly in notebook cell outputs when MLflow Tracking URI is set to 'databricks', available in MLflow 2.20+, with programmatic enable/disable controls.
tags:
  - mlflow
  - tracing
  - databricks
  - notebook
timestamp: "2026-06-19T23:25:06.713Z"
---

# [MLflow Tracing in Databricks](/concepts/mlflow-tracing-in-databricks.md) Notebooks

**MLflow Tracing in Databricks Notebooks** is a feature that integrates [MLflow Tracing](/concepts/mlflow-tracing.md) directly into the output of a Databricks notebook cell, enabling you to view and interact with [Traces](/concepts/traces.md) without leaving the notebook environment. It is designed to support rapid iteration during development and experimentation. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Availability

The [MLflow Tracing](/concepts/mlflow-tracing.md) Databricks Notebook integration is available starting from **MLflow 2.20** and above. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## How It Works

When your [MLflow tracking URI](/concepts/mlflow-tracking-uri.md) is set to `"databricks"` (the default in many Databricks environments, or set explicitly via `mlflow.set_tracking_uri("databricks")`), the trace UI can be automatically displayed in the output of a cell. This typically occurs under the following conditions: ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

1. **A cell’s code execution generates a trace** – For example, by calling a function decorated with `@mlflow.trace` or using an auto-instrumented library call (such as OpenAI or LangChain).
2. **You explicitly call `mlflow.search_traces()`** and the result is displayed.
3. **An `mlflow.entities.Trace` object is the last expression in a cell** – or is passed to `display()`. This can come from functions like `mlflow.get_trace()`.

The in-notebook view provides the same rich, interactive trace exploration capabilities found in the main [MLflow](/concepts/mlflow.md) Experiments UI, including span hierarchies, input/output details, attributes, events, and [Assessments](/concepts/assessments.md). ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Controlling Notebook Display

You can enable or disable the automatic display of [Traces](/concepts/traces.md) in notebook cell outputs using two dedicated functions: ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

```python
# Disable automatic trace display
[[mlflow|MLflow]].tracing.disable_notebook_display()

# Re-enable automatic trace display
[[mlflow|MLflow]].tracing.enable_notebook_display()
```

These functions allow you to control when the trace UI appears, which is useful in workflows where you want to suppress [Traces](/concepts/traces.md) in certain cells or re-enable them later.

## Benefits

- **Seamless workflow**: View [Traces](/concepts/traces.md) directly in the notebook, reducing context switching between the notebook and the Experiments UI.
- **Immediate feedback**: Inspect latency bottlenecks, errors, user feedback, and assessment results as you develop your application.
- **Same capabilities**: The in-notebook trace view supports search, filtering, span details, and assessment logging, identical to the Databricks MLflow UI for experiments. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The underlying tracing framework for instrumenting GenAI applications.
- Databricks MLflow UI – The full experiment-level interface for viewing [Traces](/concepts/traces.md) outside notebooks.
- Auto-instrumented library call – [Automatic Tracing](/concepts/automatic-tracing.md) of libraries like OpenAI, LangChain, and others.
- Trace agents deployed on Databricks – Production deployment of trace agents for real-time tracing.
- Collect user feedback – Using [Assessments](/concepts/assessments.md) to capture feedback on [Traces](/concepts/traces.md) directly from the UI.

## Sources

- view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md

# Citations

1. [view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md](/references/view-traces-in-the-databricks-mlflow-ui-databricks-on-aws-d0ec6f89.md)
