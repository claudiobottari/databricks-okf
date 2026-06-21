---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8f054ff8dc45224a301e6e2995910361427991ad62551ef1d9b5f70632522d00
  pageDirectory: concepts
  sources:
    - collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - review-app-trace-content-rendering
    - RATCR
  citations:
    - file: collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
title: Review App Trace Content Rendering
description: The automatic rendering behavior of the MLflow Review App for different trace content types, including RETRIEVER span documents, OpenAI-format messages, and dictionary inputs/outputs.
tags:
  - mlflow
  - tracing
  - ui
timestamp: "2026-06-19T17:46:04.715Z"
---

```markdown
---
title: Review App Trace Content Rendering
summary: Automatic rendering of different MLflow Trace content types in the Review App, including RETRIEVER span documents, OpenAI format messages, and dictionaries
sources:
  - collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:38:30.353Z"
updatedAt: "2026-06-18T14:38:30.353Z"
tags:
  - mlflow
  - tracing
  - ui
  - rendering
aliases:
  - review-app-trace-content-rendering
  - RATCR
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Review App Trace Content Rendering

**Review App Trace Content Rendering** refers to the automatic presentation of [[MLflow Trace|MLflow Traces|trace]] data within the [[MLflow Review App|Review App]] when domain experts review and label existing interactions with a GenAI agent. The Review App intelligently parses the inputs, outputs, and intermediate spans of each trace and displays them in a human-readable format, enabling experts to provide structured feedback via [[Labeling Schema|labeling schemas]]. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## How Content Rendering Works

When a labeling session is opened in the Review App, the app reads the trace’s root span `input` and `output` fields, as well as any nested spans of specific types. Based on the structure of this data, the app chooses an appropriate renderer. The rendered view is shown alongside the labeling questions defined in the session’s labeling schemas. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Rendered Content Types

### Retrieved Documents

If the trace contains a span of type `RETRIEVER` (see [[RETRIEVER Spans|RETRIEVER Span]]), the documents returned by that span are displayed in the Review App. Each document shows its `page_content` and metadata (such as `doc_uri` or `id`), allowing reviewers to evaluate the relevance of the retrieved context. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

### OpenAI-Format Messages

The Review App renders inputs and outputs that follow the OpenAI Chat Format. Specifically:

- **ChatCompletion outputs**: If the trace’s `output` is an OpenAI-format `ChatCompletions` object, the assistant’s message and any tool calls are displayed.
- **Message arrays in `inputs` or `outputs`**: If either field is a dictionary containing a `messages` key whose value is an array of OpenAI-format chat messages, the entire conversation thread (including tool calls and their results) is rendered as a readable chat history.
- **Tool calls**: Any tool calls embedded in the message array are rendered inline, showing the tool name, arguments, and results. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

### Dictionaries

If the input or output of the root span is a plain dictionary (not matching the OpenAI chat structure), the Review App renders it as a pretty-printed JSON object. This allows reviewers to inspect structured data. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

### Fallback

If none of the above patterns match, the Review App simply shows the raw `input` and `output` from the root span as the primary content for review. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Customization

For use cases that require specialized trace visualization or a different rendering layout, teams can deploy a [[Custom Review App UI|Custom Review App]] using the open-source template provided by Databricks. This template gives full control over how trace data is displayed to reviewers, while still using the same MLflow backend APIs and data model (labeling sessions, schemas, assessments). Customization options include specialized renderers for agent types, custom labeling interfaces, and domain-specific visualizations. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Related Concepts

- [[MLflow Review App|Review App]]
- [[Labeling Session]]
- [[Labeling Schema]]
- [[MLflow Trace|MLflow Traces]]
- [[RETRIEVER Spans|RETRIEVER Span]]
- OpenAI Chat Format
- [[MLflow Assessments (Feedback and Expectation)|Collect Feedback and Expectations by Labeling Existing Traces]]

## Sources

- collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
```

# Citations

1. [collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md](/references/collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws-baf6bcf1.md)
