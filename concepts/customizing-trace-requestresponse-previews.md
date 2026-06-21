---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fd94cb272211e3edd89eafdcfcc7bc089f5dee3f43b60c1fea1612a8c0d0d8f6
  pageDirectory: concepts
  sources:
    - function-decorators-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - customizing-trace-requestresponse-previews
    - CTRP
  citations:
    - file: function-decorators-databricks-on-aws.md
title: Customizing Trace Request/Response Previews
description: Using mlflow.update_current_trace() with request_preview and response_preview parameters to control how traces appear in the MLflow UI's trace list view.
tags:
  - mlflow
  - tracing
  - ui
  - visualization
timestamp: "2026-06-19T10:42:06.194Z"
---

# Customizing Trace Request/Response Previews

**Customizing Trace Request/Response Previews** refers to controlling how the overall input and output of a traced operation appear in the **Request** and **Response** columns of the [MLflow Tracing](/concepts/mlflow-tracing.md) UI. By default, these columns show a truncated version of the end-to-end input and output, but you can override the preview to display the most relevant information for each trace. ^[function-decorators-databricks-on-aws.md]

## Default behavior

The Traces tab lists every recorded trace. The **Request** and **Response** columns contain a preview (truncated to a fixed number of characters) of the root span’s input and output. This default may hide the most important parts of complex inputs (e.g., long documents, nested prompts) or outputs (e.g., summaries, extracted JSON). ^[function-decorators-databricks-on-aws.md]

## Customizing previews

To set a custom preview, call `mlflow.update_current_trace()` inside the traced function (usually the root span) and pass the `request_preview` and/or `response_preview` parameters as strings. These strings are then displayed in the respective columns of the main trace list. ^[function-decorators-databricks-on-aws.md]

### Example

The following example shows a summarization pipeline that logs a shortened version of the input document and instructions for the **Request** column, and a truncated summary for the **Response** column:

```python
import mlflow

@mlflow.trace(name="Summarization Pipeline")
def summarize_document(document_content: str, user_instructions: str):
    # Construct a custom preview for the request column
    request_p = f"Doc: {document_content[:30]}... Instr: {user_instructions[:30]}..."
    mlflow.update_current_trace(request_preview=request_p)

    # Simulate LLM call
    summary = f"Summary of document starting with '{document_content[:20]}...' based on '{user_instructions}'"

    # Customize the response preview
    response_p = f"Summary: {summary[:50]}..."
    mlflow.update_current_trace(response_preview=response_p)

    return summary
```

After calling `summarize_document`, the trace list shows:

- **Request**: `Doc: This is a very long documen... Instr: Focus on the key takea...`
- **Response**: `Summary: Summary of document starting with 'This is a...' base...`

This makes it easy to identify traces at a glance without opening each one. ^[function-decorators-databricks-on-aws.md]

## Best practices

- Set previews on the root span of the trace to control the top-level display.
- Keep previews short — they are meant for quick scanning, not full detail.
- Use meaningful fragments that help distinguish traces (e.g., first few tokens of a document, key parameters).

## Related concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Overview of the tracing system.
- Trace Decorator (@mlflow.trace) – How to create spans for functions.
- Span Customization – Other ways to modify span attributes and tags.
- [MLflow UI](/concepts/mlflow.md) – The interface where request/response previews appear.

## Sources

- function-decorators-databricks-on-aws.md (lines from "Customize request and response previews in the UI" heading to before "Automatic exception handling")

# Citations

1. [function-decorators-databricks-on-aws.md](/references/function-decorators-databricks-on-aws-0ffe82de.md)
