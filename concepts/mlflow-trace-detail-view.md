---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1730e79a009b83f823076f5bb034233e6228878342264785ddcd5c471702a3fe
  pageDirectory: concepts
  sources:
    - view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-detail-view
    - MTDV
    - Trace Detail View
  citations:
    - file: view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md
title: MLflow Trace Detail View
description: "A deep-dive view into an individual trace with two main tabs: Summary (root span inputs/outputs, exceptions) and Details & Timeline (span hierarchy/waterfall, per-span details including Chat, Inputs/Outputs, Attributes, Events tabs, and an Assessments panel)."
tags:
  - mlflow
  - tracing
  - ui
  - debugging
timestamp: "2026-06-19T23:25:09.149Z"
---

# [[mlflow-trace|MLflow Trace]] Detail View

**MLflow Trace Detail View** is the in-depth inspection interface within the Databricks MLflow UI for examining individual [Traces](/concepts/traces.md) captured during [MLflow Tracing](/concepts/mlflow-tracing.md) of generative AI applications. It provides a comprehensive breakdown of each trace's execution, including a span hierarchy, per-span details, and assessment information.

## Accessing the Detail View

To open a trace's detail view, click on its **Request** or **Trace Name** in the [MLflow Trace List View](/concepts/mlflow-trace-list-view.md). This navigates to a dedicated page with two main tabs: **Summary** and **Details & Timeline**. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Summary Tab

The **Summary** tab provides a high-level overview of the trace. It displays the root span's inputs and outputs, any key intermediate spans, and any exceptions raised during the trace. Users can toggle between **Default**, **JSON**, and **Table** rendering modes to view the input and output data in different formats. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Details & Timeline Tab

The **Details & Timeline** tab contains three main panels for in-depth analysis. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

### Trace Breakdown (Left Panel)

This panel displays the **span hierarchy** as a tree or waterfall chart. It shows all operations (spans) within the trace, their parent-child relationships, execution order, and duration. The waterfall visualization helps visually highlight operations that took the longest, enabling rapid identification of latency bottlenecks. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

### Span Details (Center Panel)

When a span is selected from the Trace Breakdown, this panel shows its detailed information, organized into the following tabs: ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

- **Chat**: For LLM interactions that are chat-based, this tab provides a rendered view of the conversation flow showing user, assistant, and tool messages. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]
- **Inputs / Outputs**: Displays the raw input data passed to the operation and the raw output data it returned. For large content, a "See more" / "See less" toggle allows expanding or collapsing the view. Some output fields may also have a **Markdown toggle** to switch between raw and rendered views if the content is in Markdown format. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]
- **Attributes**: Shows key-value metadata specific to the span, such as the `model` name and `temperature` for an LLM call, or `doc_uri` for a retriever span. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]
- **Events**: For spans that encountered errors, this tab displays exception details and stack [Traces](/concepts/traces.md). For streaming spans, it may show individual data chunks as they were yielded. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

### [Assessments](/concepts/assessments.md) (Right Panel)

This panel displays any [Assessments](/concepts/assessments.md) (user feedback or evaluations) logged for the **entire trace** or for the **currently selected span**. It includes an **"+ Add new assessment"** button, allowing users to log new feedback or evaluation scores directly from the UI while reviewing a trace — useful for manual review and labeling workflows. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Trace-Level Information

Beyond individual span details, the view also provides access to overall trace information, including trace-level tags and [Assessments](/concepts/assessments.md) logged for the entire trace. These may originate from direct user feedback or systematic evaluations. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Common Debugging Scenarios

The trace detail view supports several key debugging and observability workflows: ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

- **Identify slow traces**: In the trace list, sort by "Execution time" in descending order. In the detail view, examine the waterfall chart in the Trace Breakdown panel to pinpoint latency bottlenecks.
- **Find [Traces](/concepts/traces.md) from a particular user**: Use filters for user information (e.g., `metadata.[MLflow](/concepts/mlflow.md).trace.user`) or search tags like `tags.[MLflow](/concepts/mlflow.md).trace.user = 'user_example_123'`.
- **Locate [Traces](/concepts/traces.md) with failures**: Filter by `State = ERROR` in the trace list. In the detail view, select the error-marked span and examine its **Events** tab for exception messages and stack [Traces](/concepts/traces.md).
- **Identify [Traces](/concepts/traces.md) with negative feedback**: Use assessment filters (e.g., `is_correct = false` or `relevance_score < 0.5`). Open the trace and check the [Assessments](/concepts/assessments.md) panel for logged feedback, scores, and rationales.

## Notebook Integration

[MLflow Tracing](/concepts/mlflow-tracing.md) also offers a seamless experience within Databricks Notebooks (available in [MLflow](/concepts/mlflow.md) 2.20 and above). When the [MLflow tracking URI](/concepts/mlflow-tracking-uri.md) is set to `"databricks"`, the trace UI can be automatically displayed in cell output. This occurs when a cell generates a trace (via `@mlflow.trace` or auto-instrumentation), when `mlflow.search_traces()` is called, or when an `mlflow.entities.Trace` object is the last expression in a cell or passed to `display()`. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

To enable or disable this automatic display, use `mlflow.tracing.enable_notebook_display()` or `mlflow.tracing.disable_notebook_display()`. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Related Concepts

- [MLflow Trace List View](/concepts/mlflow-trace-list-view.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- Databricks MLflow UI
- [Span Hierarchy](/concepts/trace-span-hierarchy.md)
- [Trace Assessments](/concepts/trace-assessments.md)

## Sources

- view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md

# Citations

1. [view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md](/references/view-traces-in-the-databricks-mlflow-ui-databricks-on-aws-d0ec6f89.md)
