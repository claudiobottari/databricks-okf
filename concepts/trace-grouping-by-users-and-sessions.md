---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60fd1334d923cb0bb6a000701d7fe3049300a03e0d10e7a4a159649a849e4491
  pageDirectory: concepts
  sources:
    - instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-grouping-by-users-and-sessions
    - Sessions and Trace Grouping by Users
    - TGBUAS
    - tracking users and sessions
  citations:
    - file: instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md
title: Trace Grouping by Users and Sessions
description: MLflow supports grouping per-request traces by user sessions to maintain multi-turn interaction context and help understand end-user journeys across requests.
tags:
  - sessions
  - users
  - grouping
timestamp: "2026-06-19T19:11:33.690Z"
---

## Trace Grouping by Users and Sessions

**Trace Grouping by Users and Sessions** is a feature of [MLflow Tracing](/concepts/mlflow-tracing.md) that allows traces — which are typically generated per-request — to be associated with a user session. This enables developers to reconstruct the full end-user journey across multiple interactions, making it easier to understand behavior, debug issues, and monitor application quality in multi-turn conversational or transactional workflows. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

### Motivation

Modern GenAI applications often maintain sessions to support multi-turn user interactions. Without session-level grouping, each request produces an isolated trace, making it difficult to connect a sequence of requests that belong to the same user or conversation. By grouping traces by user sessions, teams can:

- Understand an end-user's complete journey across multiple turns.
- Identify issues that span multiple requests (e.g., context loss, accumulation of errors).
- Correlate user satisfaction or feedback with session-level traces.

^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

### How It Works

[MLflow Tracing](/concepts/mlflow-tracing.md) supports grouping traces by user sessions through the [Add Context to Traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) mechanism. When a session identifier is attached to spans or traces, the MLflow Trace UI can aggregate them under a common session view. The grouping is applied at the trace level, so every span within a session-linked trace inherits that association. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

### Usage

To enable user and session grouping, developers must set contextual metadata on their traces. The exact API is provided in the **Add context to traces** guide (referenced in the source). Common approaches include setting a `session_id` or `user_id` attribute on the root span or using the SDK's context propagation features so that all subsequent spans automatically belong to the same session. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The observability framework used to capture and visualize traces.
- Spans – The building blocks of a trace; sessions group multiple spans across requests.
- [Add Context to Traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) – The mechanism for attaching user, session, or other metadata to traces.
- MLflow TypeScript SDK – The SDK for instrumenting Node.js applications with tracing support.
- User Sessions – The concept of a sequence of interactions by a single user.

### Sources

- instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md

# Citations

1. [instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md](/references/instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws-1c7052f5.md)
