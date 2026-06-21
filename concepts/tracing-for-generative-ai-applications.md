---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d31dfc4e2154d5781841a9f4e4b56ea6a4815ed7404601480abd4ec468086d74
  pageDirectory: concepts
  sources:
    - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - tracing-for-generative-ai-applications
    - TFGAA
    - Generative AI Application
    - Generative AI Application Instrumentation
    - Generative AI Application Tracing
    - generative AI application
  citations:
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
title: Tracing for Generative AI Applications
description: The practice of adding trace instrumentation to generative AI applications for observability and debugging.
tags:
  - generative-ai
  - observability
  - tracing
timestamp: "2026-06-19T13:54:19.527Z"
---

# Tracing for Generative AI Applications

**Tracing for Generative AI Applications** refers to the practice of instrumenting generative AI application code to capture detailed execution traces. In [MLflow](/concepts/mlflow.md), this allows developers to monitor and debug complex workflows involving large language models, tool calls, and multi-step reasoning. MLflow provides three approaches to tracing for Python and [TypeScript](/concepts/mlflow-typescript-tracing-sdk.md): automatic, manual, and combined. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Automatic Tracing

Automatic tracing is the fastest way to add traces to an application. By adding a single line such as `mlflow.<library>.autolog()`, you automatically capture app logic for over 20 supported libraries. This approach is ideal for quickly gaining visibility into standard library calls without manual instrumentation. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Manual Tracing

Manual tracing is designed for custom logic and complex workflows. It gives you fine-grained control over what gets traced using either [Function Decorator APIs](/concepts/mlflowtrace-function-decorator.md) or low-level APIs. Use this approach when you need to trace custom code that is not covered by automatic tracing or when you require precise control over the trace structure. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Combined Approach

You can mix both automatic and manual tracing for complete coverage. This allows you to start with the speed of automatic tracing and then layer in manual instrumentation for specific custom logic or edge cases that need more detailed observation. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Which Approach Should I Use?

Start with automatic tracing. It is the fastest way to get traces working. Add manual tracing later if you need more control over what is captured. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Related Concepts

- [Automatic Tracing (MLflow)](/concepts/automatic-tracing-mlflow.md)
- [Manual Tracing (MLflow)](/concepts/manual-tracing-mlflow.md)
- Function Decorator API
- [Low-Level Tracing API](/concepts/common-pitfalls-of-low-level-tracing-apis.md)
- Supported libraries for MLflow tracing
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md)

## Sources

- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md

# Citations

1. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
