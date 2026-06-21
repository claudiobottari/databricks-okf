---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 738818a76c3ab5dd1bc5395e2dbeef54104acf39b1ed4e4a80be2fab1ccbd54e
  pageDirectory: concepts
  sources:
    - add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-recommendation-strategy
    - MTRS
  citations:
    - file: add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md
title: MLflow Tracing Recommendation Strategy
description: Recommended workflow of starting with automatic tracing and adding manual tracing when more control is needed.
tags:
  - mlflow
  - tracing
  - best-practices
timestamp: "2026-06-19T13:54:24.470Z"
---

# [MLflow Tracing](/concepts/mlflow-tracing.md) Recommendation Strategy

**MLflow Tracing Recommendation Strategy** provides guidance on choosing the right instrumentation approach for adding [[MLflow Trace|MLflow Traces]] to generative AI applications. MLflow offers three complementary tracing methods—automatic, manual, and combined—each suited to different levels of application complexity and control requirements. The recommended strategy is to start with automatic tracing and escalate to manual or combined tracing only when finer-grained control is needed. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Tracing Approaches Overview

| Approach | Description | Best Suited For |
|---|---|---|
| **Automatic** | One‑line `mlflow.<library>.autolog()` call that automatically captures calls to supported frameworks | Rapid instrumentation, standard patterns, 20+ supported libraries |
| **Manual** | Explicit control using [Function Decorator APIs](/concepts/mlflowtrace-function-decorator.md) or Low-Level APIs to define which operations are traced | Custom logic, complex workflows, non‑standard libraries |
| **Combined** | Automatic tracing for standard components plus manual tracing for custom parts | Complete observability across the entire application |

^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Recommended Strategy: Automatic First, Then Manual

The primary recommendation is to **start with automatic tracing**. It is the fastest way to get traces working and covers the majority of common generative AI frameworks (such as LangChain, LlamaIndex, OpenAI, and others included in the 20+ supported integrations). With a single line of code—`mlflow.<library>.autolog()`—the application’s interactions with those libraries are captured without any additional instrumentation. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

If automatic tracing does not capture certain custom logic or complex workflows (e.g., custom API calls, non‑instrumented libraries, or proprietary business logic), add **manual tracing** selectively using function decorators or the low‑level span API. For applications that require complete coverage, use the **combined** approach: keep `autolog()` for the standard components and wrap the remaining custom code with manual instrumentation. ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

> **Summary recommendation:** “Start with automatic tracing. It's the fastest way to get traces working. Add manual tracing later if you need more control.” ^[add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md]

## Implementing the Strategy

### Step 1: Automatic Tracing

Add a single call to `mlflow.<library>.autolog()` at the start of your application (e.g., `mlflow.langchain.autolog()` for LangChain applications). Verify in the [MLflow Tracing](/concepts/mlflow-tracing.md) UI that the expected spans are recorded. If all operations are captured, no further instrumentation is required.

### Step 2: Evaluate Coverage

Review trace output to identify any missing spans for custom functions, third‑party API calls, or un‑instrumented frameworks.

### Step 3: Manual Tracing (If Needed)

For each missing piece, choose the appropriate manual method:
- **Function decorator**: annotate a Python function with `@mlflow.trace` to automatically capture its inputs, outputs, and duration.
- **Low‑level API**: using `mlflow.start_span()` and `mlflow.end_span()` for fine‑grained control over span lifecycle and attributes.

See [Manual Tracing](/concepts/manual-tracing.md) for detailed usage.

### Step 4: Combined Tracing (For Full Coverage)

Keep the automatic `autolog()` call in place and layer manual tracing on top. The combined approach gives you complete observability with minimal effort.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The overall framework for capturing and analyzing traces
- [Automatic Tracing](/concepts/automatic-tracing.md) — Instrumentation via `autolog()`
- [Manual Tracing](/concepts/manual-tracing.md) — Instrumentation via decorators or low-level APIs
- [Function Decorator APIs](/concepts/mlflowtrace-function-decorator.md) — `@mlflow.trace` decorator for manual tracing
- Low-Level APIs — `mlflow.start_span()` / `mlflow.end_span()` for manual tracing
- [Best Practices for MLflow Trace Context](/concepts/best-practices-for-mlflow-trace-context.md) — Guidelines for enriching traces with context

## Sources

- add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md

# Citations

1. [add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws.md](/references/add-traces-to-applications-automatic-and-manual-tracing-databricks-on-aws-91d388aa.md)
