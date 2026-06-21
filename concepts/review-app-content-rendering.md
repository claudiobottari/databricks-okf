---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0af4c6452c25bcfc6243aab403a083e304c2668e18172c15588a5ac02f788201
  pageDirectory: concepts
  sources:
    - collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
    - test-an-app-version-with-the-review-apps-chat-ui-databricks-on-aws.md
  confidence: 0.97
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - review-app-content-rendering
    - RACR
  citations:
    - file: collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
    - file: test-an-app-version-with-the-review-apps-chat-ui-databricks-on-aws.md
title: Review App Content Rendering
description: The automatic rendering of different trace content types in the Review App, including retrieved documents from RETRIEVER spans, OpenAI format chat messages, and dicts as pretty-printed JSON.
tags:
  - mlflow
  - ui
  - tracing
  - rendering
timestamp: "2026-06-19T14:15:36.610Z"
---

# Review App Content Rendering

**Review App Content Rendering** refers to the automatic visualization of different data types within the MLflow Review App interface, enabling domain experts to examine and provide feedback on the inputs, outputs, and intermediate steps of GenAI application traces. The Review App interprets trace content based on its structure and renders it in a human-readable format optimized for review and feedback collection. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md, test-an-app-version-with-the-review-apps-chat-ui-databricks-on-aws.md]

## Context: Labeling vs. Chat UI Rendering

The rendering behavior is identical regardless of whether the Review App is used for labeling existing traces or for live chat testing, but the source of content differs:

- **When labeling existing traces**, the Review App reads inputs and outputs from previously logged traces and stores the resulting labels inside a [Labeling Session](/concepts/labeling-session.md). You must provide a custom [Labeling Schema](/concepts/labeling-schema.md) to define the questions and criteria for your use case. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]
- **When using the Review App Chat UI**, domain expert queries serve as input, live agent endpoint responses as output, and the interaction is stored as a new MLflow Trace. The Chat UI uses fixed feedback questions and does not require a custom labeling schema. ^[test-an-app-version-with-the-review-apps-chat-ui-databricks-on-aws.md]

## Rendered Content Types

The Review App automatically detects and renders the following content types from an MLflow Trace:

### Retrieved Documents

Documents within a **`RETRIEVER` span** are rendered in a dedicated display area. Each document is shown with its `id`, `page_content`, and `metadata` (including fields like `doc_uri`). This typically corresponds to retrieval-augmented generation (RAG) contexts. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md, test-an-app-version-with-the-review-apps-chat-ui-databricks-on-aws.md]

### OpenAI-Format Chat Messages

The Review App renders inputs and outputs that follow the OpenAI chat completion format:

- **`outputs`** containing an OpenAI-formatted `ChatCompletions` object. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md, test-an-app-version-with-the-review-apps-chat-ui-databricks-on-aws.md]
- **`inputs` or `outputs` dicts** that include a `messages` key with an array of OpenAI-format chat messages (system, user, assistant, and tool roles). Tool calls within the messages array are also rendered. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md, test-an-app-version-with-the-review-apps-chat-ui-databricks-on-aws.md]

This allows the expert to see the full conversational context, including system instructions, user queries, assistant responses, and any tool interactions.

### Dictionaries

Inputs or outputs that are plain dictionaries (but do not match the OpenAI message format) are rendered as pretty-printed JSONs. This provides a structured view of arbitrary key-value data. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md, test-an-app-version-with-the-review-apps-chat-ui-databricks-on-aws.md]

### Fallback: Root Span Content

If none of the above patterns match, the Review App uses the `input` and `output` from the **root span** of each trace as the primary content for review. This ensures that even traces with unusual structures can be meaningfully displayed. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md, test-an-app-version-with-the-review-apps-chat-ui-databricks-on-aws.md]

## Related Concepts

- [[MLflow Trace]] – The core data structure that captures application execution
- [Labeling Session](/concepts/labeling-session.md) – An [MLflow Run](/concepts/mlflow-run.md) that organizes a set of traces for review
- [Labeling Schema](/concepts/labeling-schema.md) – Defines the questions and input types used for labeling
- Review App Chat UI – Interactive chat interface for live app testing
- [RETRIEVER span](/concepts/retriever-spans.md) – Span type used to capture retrieved documents in RAG applications
- [OpenAI Chat Completions](/concepts/chat-completions-api.md) – Standard API format recognized by the Review App
- Feedback (MLflow) – The output of a labeling action stored as an Assessment object

## Sources

- collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
- test-an-app-version-with-the-review-apps-chat-ui-databricks-on-aws.md

# Citations

1. [collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md](/references/collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws-baf6bcf1.md)
2. [test-an-app-version-with-the-review-apps-chat-ui-databricks-on-aws.md](/references/test-an-app-version-with-the-review-apps-chat-ui-databricks-on-aws-ceb32818.md)
