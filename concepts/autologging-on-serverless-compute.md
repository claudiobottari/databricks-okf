---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1729c90b0d510cc4b8e8bca23f8e4576b1bb8aedad008e5e57f0c3b602a1ed3d
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - autologging-on-serverless-compute
    - AOSC
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: Autologging on Serverless Compute
description: Databricks Autologging is not automatically enabled on serverless compute; users must explicitly call mlflow.autolog() to use it
tags:
  - databricks
  - serverless
  - mlflow
timestamp: "2026-06-19T09:45:53.949Z"
---

# Autologging on Serverless Compute

**Autologging on Serverless Compute** refers to the behavior of [Databricks Autologging](/concepts/databricks-autologging.md) when training machine learning models on serverless compute clusters in Databricks. Unlike interactive notebook sessions on classic clusters, where autologging is automatically enabled, serverless compute **does not** automatically activate autologging. Users must explicitly enable it via `mlflow.autolog()` or framework-specific autolog functions. ^[databricks-autologging-databricks-on-aws.md]

## Key Facts

- Autologging is **not automatically enabled on serverless compute** clusters. For serverless compute, you must explicitly call [`mlflow.autolog()`](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.autolog) to enable autologging functionality. ^[databricks-autologging-databricks-on-aws.md]
- For [MLflow Tracing](/concepts/mlflow-tracing.md) enablement, serverless compute also requires explicit activation. You must call the appropriate framework-specific autolog function with `log_traces=True`, for example `mlflow.openai.autolog(log_traces=True)`. ^[databricks-autologging-databricks-on-aws.md]

## Enabling Autologging on Serverless Compute

To use autologging in a serverless notebook or job, call `mlflow.autolog()` at the beginning of your code:

```python
import mlflow
mlflow.autolog(log_input_examples=False, log_model_signatures=True, log_models=True)
```

The same customization options available for classic clusters apply. See Customize Autologging Behavior for details.

## Enabling Tracing on Serverless Compute

For frameworks that support tracing (e.g., OpenAI, LangChain, LlamaIndex, LangGraph, [AutoGen](/concepts/autogen-auto-tracing.md)), you must explicitly enable autologging for that integration on serverless compute:

```python
import mlflow
mlflow.openai.autolog(log_traces=True)
```

Without this explicit call, traces will not be captured on serverless clusters. ^[databricks-autologging-databricks-on-aws.md]

## Limitations

- Autologging on serverless compute is subject to the same general limitations as on classic clusters: it is only enabled on the driver node. To use autologging from worker nodes, you must call `mlflow.autolog()` from within the code executing on each worker. ^[databricks-autologging-databricks-on-aws.md]

## Related Concepts

- [Databricks Autologging](/concepts/databricks-autologging.md) — The general feature for automatic MLflow tracking
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The backend that stores autologged data
- Serverless Compute — The compute model where autologging is opt-in
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Trace logging for generative AI workloads
- [MLflow](/concepts/mlflow.md) — The open-source ML lifecycle platform

## Sources

- databricks-autologging-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
