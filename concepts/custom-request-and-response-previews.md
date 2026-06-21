---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea7677eba816de39605a120c1e1e0fb24ac4154461f47e0dee669dfbea227c34
  pageDirectory: concepts
  sources:
    - function-decorators-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-request-and-response-previews
    - response previews and Custom request
    - CRARP
  citations:
    - file: function-decorators-databricks-on-aws.md
title: Custom request and response previews
description: Ability to customize the Request and Response column previews in the MLflow Tracing UI using mlflow.update_current_trace() with request_preview and response_preview parameters.
tags:
  - mlflow
  - tracing
  - ui
  - observability
timestamp: "2026-06-18T12:27:30.810Z"
---

# Custom Request and Response Previews

**Custom request and response previews** allow you to override the default truncated input/output display in the MLflow Traces tab by specifying custom text for the `Request` and `Response` columns. This gives you control over which part of a trace’s end-to-end interaction is shown at a glance, making it easier to identify and understand traces in a list view. ^[function-decorators-databricks-on-aws.md]

## Default Behavior

The **Traces** tab in the MLflow UI lists all recorded [Traces](/concepts/traces.md). By default, the `Request` and `Response` columns display a preview of the entire input and output of each trace, truncated to a fixed number of characters. While this works for simple interactions, it may not show the most relevant information for complex or multi‑step workflows. ^[function-decorators-databricks-on-aws.md]

## Customizing Previews

You can control what appears in the `Request` and `Response` columns by passing the `request_preview` and `response_preview` parameters to the `mlflow.update_current_trace()` function. These parameters accept a string that will be used as the column value in the trace list. Typically, you call `update_current_trace()` on the root span of the trace. ^[function-decorators-databricks-on-aws.md]

### Example

The following example shows a summarization pipeline where the document content and user instructions are long. By constructing a custom preview, only the most meaningful fragment appears in the UI:

```python
import mlflow

@mlflow.trace(name="Summarization Pipeline")
def summarize_document(document_content: str, user_instructions: str):
    # Build a custom preview for the Request column
    request_p = f"Doc: {document_content[:30]}... Instr: {user_instructions[:30]}..."
    mlflow.update_current_trace(request_preview=request_p)

    # Simulate LLM call …
    summary = f"Summary of document starting with '{document_content[:20]}...' based on '{user_instructions}'"

    # Customize the Response column preview
    response_p = f"Summary: {summary[:50]}..."
    mlflow.update_current_trace(response_preview=response_p)

    return summary
```

After setting these previews, the trace list shows the customized strings instead of the default truncated content. ^[function-decorators-databricks-on-aws.md]

## Best Practices

- Set previews on the root span (the top‑level function decorated with `@mlflow.trace`) so they represent the entire interaction.
- Keep previews short and informative — they are meant for quick scanning.
- If inputs or outputs contain sensitive data, consider redacting or summarising the preview string.

## Related Concepts

- [Traces](/concepts/traces.md) — The recorded execution flow of an instrumented application
- [@mlflow.trace decorator](/concepts/mlflowtrace-decorator.md) — The primary way to create spans and traces
- mlflow.update_current_trace()|mlflow.update_current_trace — API used to attach tags and custom previews to the current trace
- Span attributes — Additional metadata that can be added to individual spans

## Sources

- function-decorators-databricks-on-aws.md

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
