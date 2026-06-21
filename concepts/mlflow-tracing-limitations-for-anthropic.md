---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4e401de1b1fd5b5741fd78a58095f5bf186f6ba4fc2b2041c576fe2b0d68035
  pageDirectory: concepts
  sources:
    - tracing-anthropic-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-limitations-for-anthropic
    - MTLFA
  citations:
    - file: tracing-anthropic-databricks-on-aws.md
title: MLflow Tracing Limitations for Anthropic
description: "Current constraints of the MLflow-Anthropic tracing integration: sync-only tracing (async added in 2.21.0), no multi-modal input recording, and serverless cluster autolog limitations"
tags:
  - mlflow
  - tracing
  - anthropic
  - limitations
timestamp: "2026-06-19T23:09:28.590Z"
---

# [MLflow Tracing](/concepts/mlflow-tracing.md) Limitations for Anthropic

**MLflow Tracing Limitations for Anthropic** describes the current constraints and requirements when using MLflow’s [Automatic Tracing](/concepts/automatic-tracing.md) integration with the Anthropic Python SDK. These limitations affect which platforms can auto‑trace, which API patterns are captured, and how much input data is recorded.

## Platform Limitations

On Databricks serverless compute clusters, autologging is **not** automatically enabled. Users must explicitly call `mlflow.anthropic.autolog()` to activate tracing for Anthropic calls. This is unlike non‑serverless environments where autologging may be enabled by default. Additionally, [MLflow 3](/concepts/mlflow-3.md) is strongly recommended for the best tracing experience with Anthropic; older versions may have reduced compatibility or missing features. ^[tracing-anthropic-databricks-on-aws.md]

## API and Input Limitations

Currently, the [MLflow](/concepts/mlflow.md) Anthropic integration only supports tracing for **synchronous** calls that produce text interactions. The following specific limitations apply:

- **Async APIs are not traced** – asynchronous methods such as `client.messages.create()` on `AsyncAnthropic` are not captured by auto‑tracing, even though the underlying SDK supports them.
- **Multi‑modal inputs are not fully recorded** – when the input contains images, audio, or other non‑text content, the trace cannot capture the full input payload. The trace will omit the multi‑modal portion.

^[tracing-anthropic-databricks-on-aws.md]

These restrictions mean that users relying on asynchronous programming or sending mixed‑media prompts (e.g., images with text) will have incomplete or missing [Traces](/concepts/traces.md). The integration is designed primarily for synchronous text‑based interactions.

## Supported APIs with Caveats

[MLflow](/concepts/mlflow.md) does trace synchronous `Messages: Create` and `Messages: Stream` calls, as well as asynchronous versions of those calls when using [MLflow](/concepts/mlflow.md) 2.21.0 or later. However, the core limitation regarding async tracing (stated above) indicates that async support may be partial or require specific version conditions. Users should verify their [MLflow](/concepts/mlflow.md) version and test thoroughly when using asynchronous Anthropic APIs. ^[tracing-anthropic-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Overview of [Automatic Tracing](/concepts/automatic-tracing.md) capabilities.
- [Autologging](/concepts/mlflow-autologging.md) – Mechanism for automatic instrumentation of ML libraries.
- Serverless Compute – Environment where autologging must be explicitly enabled.
- Anthropic SDK – Python client for Claude models.

## Sources

- tracing-anthropic-databricks-on-aws.md

# Citations

1. [tracing-anthropic-databricks-on-aws.md](/references/tracing-anthropic-databricks-on-aws-085cde5b.md)
