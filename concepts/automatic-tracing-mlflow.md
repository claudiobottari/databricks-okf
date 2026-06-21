---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d520e11abb91076b31a8ede2aadaef4c8261c2f82b601ad518f9527b32dffd4d
  pageDirectory: concepts
  sources:
    - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-tracing-mlflow
    - AT(
    - Automatic Tracing for MLflow
    - Automatic Tracing in MLflow
    - Automatic Tracing with MLflow
  citations:
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
title: Automatic Tracing (MLflow)
description: One-line mlflow.<library>.autolog() approach to automatically capture traces for 20+ supported libraries without manual instrumentation.
tags:
  - mlflow
  - tracing
  - observability
timestamp: "2026-06-18T14:19:36.835Z"
---

# Automatic Tracing (MLflow)

**Automatic Tracing** is the simplest approach to add traces to generative AI applications using MLflow. By adding a single line of code — `mlflow.<library>.autolog()` — you can automatically capture application logic for over 20 supported libraries without manual instrumentation. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Overview

Automatic tracing is the recommended starting point for instrumenting generative AI applications. It provides the fastest path to getting traces working, requiring minimal code changes. For most use cases, automatic tracing captures sufficient detail for debugging and monitoring. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Supported Libraries

MLflow automatic tracing supports over 20 libraries out of the box. These include popular LLM frameworks, vector stores, and other AI infrastructure components. The specific list of supported integrations is maintained in the MLflow documentation. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Implementation

To enable automatic tracing, call the `autolog()` method for your specific library:

```python
import mlflow

# Enable automatic tracing for a supported library
mlflow.<library>.autolog()
```

The exact syntax varies by library. For example, using `mlflow.openai.autolog()` would automatically trace OpenAI API calls, capturing inputs, outputs, and timing information. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## When to Use Automatic Tracing

Automatic tracing is ideal for:

- **Getting started quickly** — Minimal code changes required
- **Standard use cases** — When your application uses supported libraries
- **Initial debugging** — Capturing traces without deep instrumentation

## Limitations

Automatic tracing may not capture:

- Custom logic or complex workflows
- Steps outside supported libraries
- Specific details that require fine-grained control

For these cases, consider [Manual Tracing (MLflow)](/concepts/manual-tracing-mlflow.md) or a [Combined Tracing Approach](/concepts/combined-tracing-approach.md). ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Combining with Manual Tracing

You can mix automatic and manual tracing for complete coverage. Start with automatic tracing, then add [Manual Tracing (MLflow)](/concepts/manual-tracing-mlflow.md) for custom logic or complex workflows where you need finer control over what gets traced. This combined approach gives you the best of both methods. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Recommendation

The recommended workflow is to start with automatic tracing as the fastest way to get traces working. Add manual tracing later only if you need more control over specific parts of your application. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Related Concepts

- [Manual Tracing (MLflow)](/concepts/manual-tracing-mlflow.md) — Fine-grained control for custom logic
- [Combined Tracing Approach](/concepts/combined-tracing-approach.md) — Using both automatic and manual tracing
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The broader tracing framework
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — Generative AI evaluation and monitoring

## Sources

- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md

# Citations

1. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
