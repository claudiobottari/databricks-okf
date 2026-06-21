---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 473b58e67c8546a80b152b5239c6f3d19dc9c4447a0acbf4cecaaa11346a8ca9
  pageDirectory: concepts
  sources:
    - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
    - manual-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - automatic-tracing
    - Automatic MLflow Tracing
    - Auto-Tracing
    - Auto-tracing
    - Automatic Instrumentation
  citations:
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
title: Automatic Tracing
description: An MLflow tracing approach that uses a single line of code (mlflow.<library>.autolog()) to automatically capture traces for 20+ supported libraries without manual instrumentation.
tags:
  - mlflow
  - automatic-tracing
  - instrumentation
timestamp: "2026-06-19T17:27:48.779Z"
---

# Automatic Tracing

**Automatic Tracing** is an MLflow approach to instrumenting generative AI applications that requires minimal code changes. By adding a single line of code — `mlflow.<library>.autolog()` — you can automatically capture traces for over 20 supported libraries without manually defining spans or managing trace structure. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Overview

Automatic tracing is the recommended starting point for adding observability to GenAI applications. It provides instant trace capture for supported frameworks with zero configuration beyond the autolog call. This approach is designed to get traces working as quickly as possible, making it ideal for initial development and debugging. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Supported Libraries

MLflow's automatic tracing supports over 20 libraries out of the box. These include popular generative AI frameworks, LLM providers, and vector stores. For the complete list of supported integrations, see the [MLflow Tracing Integrations](/concepts/mlflow-tracing-integrations.md) documentation. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Usage

To enable automatic tracing, add a single line of code at the start of your application:

```python
import mlflow

mlflow.<library>.autolog()
```

Replace `<library>` with the name of the supported library you want to trace. For example, `mlflow.openai.autolog()` for OpenAI calls or `mlflow.langchain.autolog()` for LangChain workflows. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## When to Use Automatic Tracing

Automatic tracing is the fastest way to get traces working. It is the recommended first approach for any GenAI application built on supported frameworks. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Limitations

Automatic tracing only works with the supported libraries. For custom logic, proprietary frameworks, or complex workflows that require fine-grained control over span structure, you need to use [Manual Tracing](/concepts/manual-tracing.md). ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Combining Automatic and Manual Tracing

You can combine automatic and manual tracing for complete coverage. Use automatic tracing for the supported library calls and add manual tracing for custom logic, complex nested operations, or custom metadata. This combined approach gives you the best of both approaches: instant coverage for standard components and full control for custom code. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Related Concepts

- [Manual Tracing](/concepts/manual-tracing.md) — Full control over trace structure for custom and complex workflows
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Overview of the [MLflow Tracing](/concepts/mlflow-tracing.md) system
- [MLflow Tracing Integrations](/concepts/mlflow-tracing-integrations.md) — Complete list of supported libraries for automatic tracing
- Function Decorator API — Manual tracing approach using decorators
- [Low-Level Tracing API](/concepts/common-pitfalls-of-low-level-tracing-apis.md) — Manual tracing approach for maximum control
- [Combined Tracing](/concepts/combined-tracing.md) — Using automatic and manual tracing together

## Sources

- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
- manual-tracing-databricks-on-aws.md

# Citations

1. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
