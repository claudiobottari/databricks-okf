---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6f725350ca42a6981339d0735c02b942ab557f97cedadcf920fc8cf712a62c8b
  pageDirectory: concepts
  sources:
    - genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-instrumentation-guidance
    - MIG
    - Instrumentation Guidance
    - Instrument your app
    - instrument your app
  citations:
    - file: genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md
title: MLflow Instrumentation Guidance
description: The ability to get help adding tracing to GenAI agent code using autolog(), @mlflow.trace decorator, or manual spans, with runnable code snippets for Databricks notebooks.
tags:
  - mlflow
  - instrumentation
  - tracing
  - code-snippets
timestamp: "2026-06-19T10:43:46.866Z"
---

## MLflow Instrumentation Guidance

**MLflow Instrumentation Guidance** refers to a set of interactive helpers provided by [Genie Code](/concepts/genie-code.md) within the MLflow experiment UI that assist developers in adding observability to their GenAI applications. It offers natural‑language‑based advice and runnable code snippets for instrumenting agent code with tracing, enabling end‑to‑end visibility into agent behavior.^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

### Overview

Instrumentation guidance is one of the capabilities of Genie Code, a natural language interface for understanding, debugging, and improving GenAI applications inside [MLflow experiments](/concepts/mlflow-experiment.md). Instead of manually consulting documentation or writing trace‑setup code from scratch, developers can ask Genie Code for help adding tracing and receive ready‑to‑use snippets that can be pasted directly into Databricks notebooks.^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

### Available Instrumentation Methods

Genie Code can provide guidance on three tracing approaches:

- **`autolog()`** – Automatic instrumentation that captures traces with minimal code changes.
- **`@mlflow.trace`** – A decorator for instrumenting individual functions within an agent’s execution flow.
- **Manual spans** – Fine‑grained control over what gets traced by creating and managing spans explicitly.

The guidance includes runnable code examples for each method, tailored to the user’s specific agent architecture.^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

### How to Access

To use instrumentation guidance, open an MLflow experiment in your workspace and click the **Genie Code** icon in the top‑right corner. You can then ask questions such as:

- “Help me add tracing to my code with `autolog()`, `@mlflow.trace`, or manual spans.”

Genie Code will respond with code snippets that you can immediately run in a Databricks notebook.^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

### Requirements

- The workspace must have [partner‑powered AI features](https://docs.databricks.com/aws/en/databricks-ai/partner-powered) enabled at the account and workspace level.
- The workspace must be in a [supported region](https://docs.databricks.com/aws/en/genie-code/#geo-availability).^[genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The underlying observability framework that instrumentation guidance helps you set up.
- [Genie Code](/concepts/genie-code.md) – The conversational interface that provides instrumentation guidance.
- [Autolog](/concepts/mlflow-autologging.md) – Automatic trace capture for MLflow experiments.
- @mlflow.trace – Decorator‑based manual tracing.
- [Manual spans](/concepts/manual-tracing.md) – Low‑level tracing control.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit where tracing and evaluation data live.

### Sources

- genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md

# Citations

1. [genie-code-for-agent-observability-and-evaluation-databricks-on-aws.md](/references/genie-code-for-agent-observability-and-evaluation-databricks-on-aws-deaf4f1f.md)
