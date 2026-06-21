---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b54ac47610c06e4abeec08dee2a6d10cdf807aa6d5a5463b236c8737bdd7d47
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prerequisites-for-mlflow-3-genai-tracing
    - PFM3GT
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: Prerequisites for MLflow 3 GenAI Tracing
description: Installation requirements including `mlflow[databricks]>=3.1`, provider SDKs, and LLM API key configuration for automatic tracing on Databricks.
tags:
  - mlflow
  - prerequisites
  - installation
  - databricks
timestamp: "2026-06-18T14:29:45.466Z"
---

# Prerequisites for MLflow 3 GenAI Tracing

To use [MLflow 3](/concepts/mlflow-3.md) [GenAI Tracing](/concepts/mlflow-genai-tracing.md) effectively, you must meet several installation, credential, and environment prerequisites. This page covers the requirements for automatic tracing of generative AI applications using supported frameworks. ^[automatic-tracing-databricks-on-aws.md]

## Required Packages

Install the `mlflow` package with Databricks connectivity enabled, along with the SDK for the framework you intend to trace. For example, to trace OpenAI calls: ^[automatic-tracing-databricks-on-aws.md]

```python
%pip install --upgrade "mlflow[databricks]>=3.1" openai>=1.0.0
# Also install libraries for other integrations (langchain, anthropic, etc.)
dbutils.library.restartPython()
```

- **`mlflow[databricks]>=3.1`** provides core MLflow functionality with GenAI features and Databricks connectivity. ^[automatic-tracing-databricks-on-aws.md]
- **Framework SDKs** (e.g., `openai>=1.0.0`, `langchain`, `anthropic`) are required only when using that specific integration. ^[automatic-tracing-databricks-on-aws.md]
- `dbutils.library.restartPython()` is necessary in a Databricks notebook after installing packages to reload the Python environment. ^[automatic-tracing-databricks-on-aws.md]

## Configure Credentials

Set API keys as environment variables for the LLM providers you plan to use. ^[automatic-tracing-databricks-on-aws.md]

**In a Databricks notebook:**

```python
import os
os.environ["OPENAI_API_KEY"] = "your-api-key"
# Add other provider keys as needed
# os.environ["ANTHROPIC_API_KEY"] = "your-api-key"
# os.environ["MISTRAL_API_KEY"] = "your-api-key"
```

^[automatic-tracing-databricks-on-aws.md]

**In an external environment**, configure credentials according to your provider's instructions — typically through environment variables or configuration files. ^[automatic-tracing-databricks-on-aws.md]

When using [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) with the OpenAI client, ensure `DATABRICKS_TOKEN` and `DATABRICKS_HOST` are set appropriately. ^[automatic-tracing-databricks-on-aws.md]

## Environment Considerations

- **Serverless compute clusters:** On serverless clusters, autologging for GenAI tracing frameworks is **not automatically enabled**. You must explicitly call the appropriate `mlflow.<library>.autolog()` function for each integration you want to trace (e.g., `mlflow.openai.autolog()`). ^[automatic-tracing-databricks-on-aws.md]
- **MLflow version:** Databricks recommends MLflow 3 for the latest GenAI tracing capabilities. ^[automatic-tracing-databricks-on-aws.md]

## Next Steps

After meeting the prerequisites, you can enable automatic tracing with a single line of code:

```python
mlflow.openai.autolog()
```

Then run your application code as usual — traces are generated automatically for supported frameworks. For manual control, see [Manual tracing with decorators](/concepts/mlflowtrace-decorator.md).

## Related Concepts

- [Automatic Tracing](/concepts/automatic-tracing.md) — Single-line `autolog()` activation
- [MLflow 3](/concepts/mlflow-3.md) — The recommended MLflow version for GenAI Tracing
- Supported frameworks — Over 20 libraries supported out of the box
- [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) — How to trace models hosted on Databricks
- OpenAI integration
- LangChain integration

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
