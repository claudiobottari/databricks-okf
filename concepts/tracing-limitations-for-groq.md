---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 392a990452237ab9bd8ac6cd91f7abf4359c039ab63e23a328f176eb1ce67149
  pageDirectory: concepts
  sources:
    - tracing-groq-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tracing-limitations-for-groq
    - TLFG
  citations:
    - file: tracing-groq-databricks-on-aws.md
title: Tracing Limitations for Groq
description: Only synchronous Groq SDK calls are traced; async and streaming methods are not supported
tags:
  - tracing
  - groq
  - limitations
  - async
timestamp: "2026-06-19T23:12:10.338Z"
---

# Tracing Limitations for Groq

**Tracing Limitations for Groq** refers to the specific constraints and behavioral characteristics of [Automatic Tracing](/concepts/automatic-tracing.md) in [MLflow](/concepts/mlflow.md) when integrated with the Groq SDK. [MLflow Tracing](/concepts/mlflow-tracing.md) provides automatic trace recording for Groq SDK usage, but has notable limitations that users should understand before relying on it for [Production Monitoring](/concepts/production-monitoring.md) or debugging.

## Supported Operations

When Groq auto-tracing is enabled via `mlflow.groq.autolog()`, only **synchronous** API calls are traced. The tracing system captures [Traces](/concepts/traces.md) generated during interactive development when using the Groq SDK's synchronous methods. ^[tracing-groq-databricks-on-aws.md]

## Unsupported Operations

### Asynchronous API Calls

Asynchronous API methods provided by the Groq SDK are **not traced**. Any calls made using async patterns will not appear in the [[mlflow-trace|MLflow Trace]] data, which may limit observability for applications that rely on asynchronous processing. ^[tracing-groq-databricks-on-aws.md]

### Streaming Methods

Streaming responses from the Groq SDK are **not traced**. Applications that use streaming to receive partial responses incrementally will not have those interactions recorded as [Traces](/concepts/traces.md). ^[tracing-groq-databricks-on-aws.md]

## Autologging Behavior on Serverless Compute

On serverless compute clusters, autologging is **not automatically enabled**. Unlike other compute environments where autologging may activate by default, users on Serverless Compute must explicitly call `mlflow.groq.autolog()` to enable [Automatic Tracing](/concepts/automatic-tracing.md) for the Groq integration. ^[tracing-groq-databricks-on-aws.md]

## Disabling Auto-Tracing

Auto-tracing for Groq can be disabled globally using either of the following approaches:

- `mlflow.groq.autolog(disable=True)` — Disables only Groq-specific auto-tracing
- `mlflow.autolog(disable=True)` — Disables auto-tracing for all integrations globally

^[tracing-groq-databricks-on-aws.md]

## Summary Table

| Feature | Supported | Notes |
|---------|-----------|-------|
| Synchronous API calls | Yes | Fully traced during interactive development |
| Asynchronous API calls | No | Not captured in [Traces](/concepts/traces.md) |
| Streaming methods | No | Not captured in [Traces](/concepts/traces.md) |
| Serverless autologging | Manual | Must call `mlflow.groq.autolog()` explicitly |

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The core tracing framework that records and organizes trace data
- [Groq SDK Integration](/concepts/groq-sdk-integration-with-mlflow.md) — The full integration details for connecting Groq with [MLflow](/concepts/mlflow.md)
- Tracing 101 — Foundational concepts for understanding [[mlflow-trace|MLflow Trace]] data
- Trace UI — The interface for debugging and observing traced applications
- [App Quality Evaluation](/concepts/genai-application-evaluation-lifecycle.md) — Setting up quality assessment for Groq-powered applications

## Sources

- tracing-groq-databricks-on-aws.md

# Citations

1. [tracing-groq-databricks-on-aws.md](/references/tracing-groq-databricks-on-aws-121d088c.md)
