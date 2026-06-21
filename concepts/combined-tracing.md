---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9a7bb18ad9cb04aac3d19d33b0c2f1c3ca1079ca985b87185fe1a55c544f2e2d
  pageDirectory: concepts
  sources:
    - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - combined-tracing
  citations:
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
title: Combined Tracing
description: A hybrid MLflow tracing approach that mixes automatic and manual instrumentation for complete coverage of generative AI application logic.
tags:
  - mlflow
  - hybrid-tracing
  - instrumentation
timestamp: "2026-06-19T17:27:55.427Z"
---

# Combined Tracing

**Combined Tracing** refers to the approach of mixing automatic and manual tracing within the same generative AI application to achieve complete coverage of all relevant spans. MLflow supports three tracing approaches for Python and TypeScript: automatic, manual, and combined. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Overview

Combined tracing allows you to use the speed and simplicity of [Automatic Tracing](/concepts/automatic-tracing.md) for well‑supported libraries while adding [Manual Tracing](/concepts/manual-tracing.md) for custom logic or complex workflows that automatic instrumentation does not cover. The result is a single trace that includes both automatically captured spans and manually created spans, giving you full visibility into the application's execution. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## How It Works

You enable automatic tracing for a supported library (for example, `mlflow.langchain.autolog()`) to capture standard operations. Then you use manual tracing APIs — such as the Function Decorator API or the Low-Level API — to wrap custom functions or to add additional context to the trace. MLflow merges the two into one coherent trace. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Recommended Workflow

The Databricks documentation recommends starting with [Automatic Tracing](/concepts/automatic-tracing.md) because it is the fastest way to get traces working. If you need more control over what is captured, you can add manual tracing later, naturally leading to a combined tracing setup. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## When to Use Combined Tracing

Use combined tracing when:

- Your application uses libraries that support automatic tracing (see the [list of supported libraries](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/)) but also contains custom or complex logic that requires manual instrumentation.
- You want to augment automatically generated spans with additional attributes, metadata, or sub‑spans that are not captured by the automatic mechanism.
- You are migrating from a purely automatic setup to a more fine‑grained manual approach and want to incrementally add manual spans without losing existing visibility.

## Related Concepts

- [Automatic Tracing](/concepts/automatic-tracing.md)
- [Manual Tracing](/concepts/manual-tracing.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- Function Decorator API
- Low-Level API
- [Generative AI Application Instrumentation](/concepts/tracing-for-generative-ai-applications.md)

## Sources

- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md

# Citations

1. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
