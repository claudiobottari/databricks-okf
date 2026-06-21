---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 514f889c4fa999c955b02ac0927c65078d8d87d7ad6086d0b83000b85ed98060
  pageDirectory: concepts
  sources:
    - tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md
    - tracing-gemini-databricks-on-aws.md
    - tracing-langgraph-databricks-on-aws.md
  confidence: 0.98
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - disabling-mlflow-auto-tracing
    - DMAT
  citations:
    - file: tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md
    - file: tracing-gemini-databricks-on-aws.md
    - file: tracing-langgraph-databricks-on-aws.md
title: Disabling MLflow Auto Tracing
description: Auto-tracing for Amazon Bedrock can be disabled globally by calling mlflow.bedrock.autolog(disable=True) or mlflow.autolog(disable=True).
tags:
  - mlflow
  - tracing
  - configuration
timestamp: "2026-06-19T23:09:14.424Z"
---

```yaml
---
title: Disabling [[mlflow|MLflow]] Auto Tracing
summary: Methods to disable auto tracing for specific libraries or all autologging integrations at once via [[mlflow|MLflow]].<library>.autolog(disable=True).
sources:
  - tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md
  - tracing-gemini-databricks-on-aws.md
  - tracing-langgraph-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T19:41:08.648Z"
updatedAt: "2026-06-19T19:41:08.648Z"
tags:
  - [[mlflow|MLflow]]
  - tracing
  - configuration
aliases:
  - disabling-mlflow-auto-tracing
  - DMAT
confidence: 0.92
provenanceState: merged
inferredParagraphs: 0
---

# Disabling [[mlflow|MLflow]] Auto Tracing

**MLflow Auto Tracing** is a feature that automatically captures [[traces|Traces]] from supported Generative AI libraries and frameworks with minimal setup. When auto tracing is enabled, [[mlflow|MLflow]] logs detailed observability data — such as prompts, completions, latencies, and model metadata — to the active experiment. To stop tracing for a particular integration or for all integrations, you can call the appropriate `autolog()` function with `disable=True`. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md, tracing-gemini-databricks-on-aws.md, tracing-langgraph-databricks-on-aws.md]

> **Note:** On serverless compute clusters, autologging is **not** automatically enabled. You must explicitly call `mlflow.<library>.autolog()` to enable tracing for that integration. Disabling auto tracing works regardless of whether autolog was previously enabled. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md, tracing-gemini-databricks-on-aws.md, tracing-langgraph-databricks-on-aws.md]

## Disabling a Specific Integration

To disable auto tracing for a particular library, call the corresponding `autolog()` function with `disable=True`. For example:

- **Amazon Bedrock:** `mlflow.bedrock.autolog(disable=True)` ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]
- **Google Gemini:** `mlflow.gemini.autolog(disable=True)` ^[tracing-gemini-databricks-on-aws.md]
- **LangGraph** (traced via the LangChain integration): `mlflow.langchain.autolog(disable=True)` ^[tracing-langgraph-databricks-on-aws.md]

The same pattern applies to any supported library.

```python
import [MLflow](/concepts/mlflow.md)

# Disable auto tracing for a specific integration
[MLflow](/concepts/mlflow.md).bedrock.autolog(disable=True)
[MLflow](/concepts/mlflow.md).gemini.autolog(disable=True)
[MLflow](/concepts/mlflow.md).langchain.autolog(disable=True)
```

## Disabling All Integrations

If you want to disable auto tracing for every library at once, use `mlflow.autolog(disable=True)`. This single call turns off all [[automatic-tracing|Automatic Tracing]] that was previously enabled via `mlflow.<library>.autolog()`. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md, tracing-gemini-databricks-on-aws.md, tracing-langgraph-databricks-on-aws.md]

```python
import [MLflow](/concepts/mlflow.md)

# Disable all autologging
[MLflow](/concepts/mlflow.md).autolog(disable=True)
```

## Related Concepts

- [[MLflow Tracing]] — Overview of MLflow’s tracing capabilities.
- [[MLflow Autologging|Autologging]] — Automatic logging of metrics, parameters, and models.
- Amazon Bedrock Tracing — Specific tracing integration for Amazon Bedrock.
- Gemini Tracing — Specific tracing integration for Google Gemini.
- [[MLflow LangGraph Tracing|LangGraph Tracing]] — Tracing for LangGraph applications via the LangChain integration.

## Sources

- tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md
- tracing-gemini-databricks-on-aws.md
- tracing-langgraph-databricks-on-aws.md
```

# Citations

1. [tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md](/references/tracing-amazon-bedrock-with-mlflow-databricks-on-aws-2f3942c6.md)
2. [tracing-gemini-databricks-on-aws.md](/references/tracing-gemini-databricks-on-aws-52fc6461.md)
3. [tracing-langgraph-databricks-on-aws.md](/references/tracing-langgraph-databricks-on-aws-6240217a.md)
