---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0500b19601fe438a19aa09521c7fcac304f4a228ad9bb2c77c4bfd58303969e7
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
    - mlflow-tracing-integrations-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - serverless-compute-autologging-requirement
    - SCAR
    - Serverless Compute and Autologging
    - serverless-compute-cluster-autolog-requirements
    - SCCAR
  citations:
    - file: automatic-tracing-databricks-on-aws.md
    - file: mlflow-tracing-integrations-databricks-on-aws.md
title: Serverless Compute Autologging Requirement
description: On Databricks serverless compute clusters, autologging for GenAI tracing frameworks is not automatically enabled and must be explicitly enabled by calling the appropriate mlflow.<library>.autolog() function.
tags:
  - databricks
  - serverless
  - autologging
  - configuration
timestamp: "2026-06-19T22:10:54.960Z"
---

```markdown
---
title: Serverless Compute Autologging Requirement
summary: On Databricks serverless compute clusters, genAI tracing autologging is not automatically enabled and must be explicitly invoked by calling the appropriate mlflow.<library>.autolog() function.
sources:
  - automatic-tracing-databricks-on-aws.md
  - mlflow-tracing-integrations-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:50:28.751Z"
updatedAt: "2026-06-19T18:00:00.000Z"
tags:
  - databricks
  - serverless
  - mlflow
  - configuration
aliases:
  - serverless-compute-autologging-requirement
  - SCAR
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Serverless Compute Autologging Requirement

**Serverless Compute Autologging Requirement** refers to the mandatory step of explicitly enabling [`mlflow.<library>.autolog()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.autolog) when running generative AI tracing workloads on Databricks serverless compute clusters. Unlike standard clusters, serverless compute **does not** automatically activate autologging for GenAI tracing frameworks. ^[automatic-tracing-databricks-on-aws.md, mlflow-tracing-integrations-databricks-on-aws.md]

## Why This Requirement Exists

On Databricks serverless compute, the automatic instrumentation of supported LLM and agent libraries (such as OpenAI, LangChain, and Databricks Foundation Models) is **not enabled by default**. To capture traces, you must call the appropriate integration-specific `autolog()` function (e.g., `mlflow.openai.autolog()`) explicitly in your code before making any traced calls. ^[automatic-tracing-databricks-on-aws.md, mlflow-tracing-integrations-databricks-on-aws.md]

## Implications

- **All GenAI tracing integrations** require explicit `autolog()` calls on serverless compute. This applies to any of the [20+ supported frameworks](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/) as well as Databricks Foundation Models. ^[automatic-tracing-databricks-on-aws.md, mlflow-tracing-integrations-databricks-on-aws.md]
- Failing to call `autolog()` means no traces are generated, even if the code otherwise runs correctly. (inferred)
- The requirement applies **only to serverless compute**; other compute types (e.g., classic clusters) may have autologging enabled automatically or through default settings. ^[automatic-tracing-databricks-on-aws.md]

## How to Meet the Requirement

1. Install the required MLflow and library packages (e.g., `mlflow[databricks]>=3.1` and the SDK for the integration you use). ^[automatic-tracing-databricks-on-aws.md]
2. Before making any LLM calls, call the appropriate `autolog()` function:
   ```python
   mlflow.openai.autolog()        # For OpenAI / Databricks Foundation Model APIs
   mlflow.langchain.autolog()     # For LangChain chains
   # Repeat for each integration you want traced
   ```
3. Ensure the `autolog()` call is executed **before** the code that uses the library.

## Related Concepts

- [[Automatic tracing]] – General approach to instrumenting GenAI apps with one line of code
- [[MLflow Tracing]] – The MLflow component that captures and stores trace data
- [[Serverless GPU Compute|Serverless compute]] – The Databricks compute type that requires explicit autologging
- [[@mlflow.trace decorator|Manual tracing with decorators]] – Alternative to automatic tracing for custom spans
- [[Databricks Autologging]] – Broader automatic logging for ML training (separate from GenAI tracing)

## Sources

- automatic-tracing-databricks-on-aws.md
- mlflow-tracing-integrations-databricks-on-aws.md
```

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
2. [mlflow-tracing-integrations-databricks-on-aws.md](/references/mlflow-tracing-integrations-databricks-on-aws-22e947f8.md)
