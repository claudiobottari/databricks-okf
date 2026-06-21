---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dbbd6774f66402c75b6421e5dc2d740d6611cf091fa4eef8a4dde331137c54ed
  pageDirectory: concepts
  sources:
    - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-tracing-autolog
    - AT(
    - Automated Logging (autolog)
  citations:
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
title: Automatic Tracing (autolog)
description: One-line `mlflow.<library>.autolog()` approach to automatically capture traces for 20+ supported libraries
tags:
  - mlflow
  - tracing
  - automatic-instrumentation
timestamp: "2026-06-19T21:59:18.563Z"
---

Here is the wiki page for "Automatic Tracing (autolog)".

---

## Automatic Tracing (autolog)

**Automatic Tracing**, commonly referred to as **autolog** or `mlflow.autolog()`, is a feature in [MLflow](/concepts/mlflow.md) that automatically captures traces from supported generative AI and [machine learning](/concepts/cicd-for-machine-learning.md) libraries with minimal code changes. It is the recommended starting point for adding [tracing](/concepts/mlflow-tracing.md) to an application.

### Overview

Automatic tracing works by instrumenting supported libraries to record traces of function calls and data flow without requiring manual instrumentation. To enable it, you add a single line of code: `mlflow.<library>.autolog()`. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

MLflow supports automatic tracing for over 20 libraries, including popular frameworks for LLM usage, vector stores, and agents. For a full list, see the documentation on [supported tracing integrations](/concepts/mlflow-supported-tracing-libraries.md). ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### When to Use Automatic Tracing

| Approach | Recommendation |
|----------|----------------|
| Automatic | Start here – the fastest way to get traces working. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md] |
| Manual | Add later if you need more control over what gets traced. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md] |

### Combined Use

You can mix automatic and manual tracing for complete coverage. Use `autolog()` to handle standard library calls and add [Manual Tracing](/concepts/manual-tracing.md) for custom logic or complex workflows that require finer-grained control. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

### Related Concepts

- [Manual Tracing](/concepts/manual-tracing.md) – Function decorator and low-level APIs for custom trace control.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The overarching tracing system in MLflow.
- [Supported Tracing Integrations](/concepts/mlflow-supported-tracing-libraries.md) – The list of 20+ libraries that support autolog.
- [Generative AI Application Tracing](/concepts/tracing-for-generative-ai-applications.md) – The broader topic of instrumenting GenAI apps.

### Sources

- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md

# Citations

1. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
