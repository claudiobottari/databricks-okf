---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1e030e239c6ce9a73cdff56407bce6bec2e60e71384b186313a4ba72c5ea7a54
  pageDirectory: concepts
  sources:
    - function-decorators-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-trace-ui-previews
    - CTUP
  citations:
    - file: function-decorators-databricks-on-aws.md
title: Custom Trace UI Previews
description: The ability to set custom request_preview and response_preview strings via mlflow.update_current_trace() to control how traces are summarized in the MLflow UI's trace list view.
tags:
  - mlflow
  - tracing
  - ui
  - customization
timestamp: "2026-06-19T18:57:04.663Z"
---

# Custom Trace UI Previews

**Custom Trace UI Previews** allow you to control what appears in the `Request` and `Response` columns of the MLflow Traces tab, replacing the default truncated view with a customized preview that highlights the most relevant information for each trace.

## Overview

The Traces tab in the MLflow UI displays a list of traces, with `Request` and `Response` columns showing a preview of each trace's end-to-end input and output. By default, these previews are truncated to a fixed number of characters. When you have complex inputs or outputs—such as long documents, multiple prompt messages, or structured responses—the default truncation may not display the most meaningful information. ^[function-decorators-databricks-on-aws.md]

Custom Trace UI Previews solve this problem by letting you define what appears in these columns on a per-trace basis. This makes it easier to quickly identify and understand what each trace represents at a glance. ^[function-decorators-databricks-on-aws.md]

## How to Set Custom Previews

You set custom request and response previews using the `request_preview` and `response_preview` parameters within the [`mlflow.update_current_trace()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.update_current_trace) function. This is typically done inside a function decorated with `@mlflow.trace`, often at the root span level. ^[function-decorators-databricks-on-aws.md]

### Basic Example

The following example demonstrates a summarization pipeline where the request preview shows the beginning of the document and the user instructions, while the response preview shows the first 50 characters of the generated summary:

```python
import mlflow

@mlflow.trace(name="Summarization Pipeline")
def summarize_document(document_content: str, user_instructions: str):
    # Construct a custom preview for the request column
    # For example, show beginning of document and user instructions
    request_p = f"Doc: {document_content[:30]}... Instr: {user_instructions[:30]}..."
    mlflow.update_current_trace(request_preview=request_p)

    # Simulate LLM call
    summary = f"Summary of document starting with '{document_content[:20]}...' based on '{user_instructions}'"

    # Customize the response preview
    response_p = f"Summary: {summary[:50]}..."
    mlflow.update_current_trace(response_preview=response_p)

    return summary

# Example Call
long_document = "This is a very long document that contains many details about various topics..." * 10
instructions = "Focus on the key takeaways regarding topic X."
summary_result = summarize_document(long_document, instructions)
```

^[function-decorators-databricks-on-aws.md]

By setting `request_preview` and `response_preview` on the trace (typically the root span), you control how the overall interaction is summarized in the main trace list view. ^[function-decorators-databricks-on-aws.md]

## Best Practices

- **Set previews at the root span level** — The request and response previews represent the end-to-end input and output of the entire trace, so update them in the outermost function. ^[function-decorators-databricks-on-aws.md]
- **Keep previews concise** — Although you control the content, the columns have limited display space; aim for a brief but informative summary. ^[function-decorators-databricks-on-aws.md]
- **Highlight distinguishing information** — Show the parts of the input or output that help differentiate one trace from another, such as user instructions, document titles, or key output fields. ^[function-decorators-databricks-on-aws.md]
- **Handle edge cases** — Ensure your preview logic works when inputs are empty, None, or shorter than expected. ^[function-decorators-databricks-on-aws.md]

## Relationship to Other Preview Mechanisms

Custom Trace UI Previews are one of several ways to add metadata to traces. You can also set [Trace Tags](/concepts/trace-tags.md) using `mlflow.update_current_trace(tags=...)` to provide additional metadata at the trace level. Tags appear in the trace details view, while request and response previews control the columns in the main trace list. ^[function-decorators-databricks-on-aws.md]

## Related Concepts

- Function Decorators for Tracing — The `@mlflow.trace` decorator that creates spans for functions and provides the context for setting custom previews.
- mlflow.start_span() Context Manager|Span Tracing with Context Managers — An alternative way to create spans and update trace metadata.
- [Trace Tags](/concepts/trace-tags.md) — Additional metadata that can be attached to traces at the trace level.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The overall tracing framework for instrumenting GenAI applications.

## Sources

- function-decorators-databricks-on-aws.md

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
