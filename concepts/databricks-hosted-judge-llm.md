---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a6930e48b7e122bacb343fe0e7763ba12afef9e578b500d4c262f0e8dd099402
  pageDirectory: concepts
  sources:
    - correctness-judge-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-hosted-judge-llm
    - DJL
  citations:
    - file: correctness-judge-databricks-on-aws.md
title: Databricks-Hosted Judge LLM
description: The default LLM used by built-in judges in Databricks, designed specifically for performing GenAI quality assessments and accessible via Databricks serving endpoints.
tags:
  - databricks
  - llm-judges
  - infrastructure
timestamp: "2026-06-19T09:26:37.098Z"
---

# Databricks-hosted Judge LLM

**Databricks-hosted Judge LLM** is a large language model hosted by Databricks that is specifically designed to perform GenAI quality assessments. It acts as the default evaluation engine for [MLflow](/concepts/mlflow.md)'s built-in judges. ^[correctness-judge-databricks-on-aws.md]

## Default Model

By default, every built-in judge – such as [Correctness](/concepts/correctness-judge.md) – uses the Databricks-hosted Judge LLM to evaluate responses. This eliminates the need for users to bring their own model for common quality evaluations. ^[correctness-judge-databricks-on-aws.md]

## Selecting a Judge Model

You can override the default Databricks-hosted Judge LLM by providing a `model` argument when creating a judge. The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. If you use `databricks` as the provider, the model name corresponds to a Databricks serving endpoint. For example: ^[correctness-judge-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Correctness

# Use a different judge model
correctness_judge = Correctness(
    model="databricks:/databricks-gpt-5-mini"
)
```

## Related Concepts

- [Built-in Judges](/concepts/built-in-judges.md) – Pre-configured quality scorers that use the Databricks-hosted Judge LLM by default.
- [Correctness Judge](/concepts/correctness-judge.md) – An example built-in judge that evaluates factual correctness.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The framework for running evaluations with judges.
- [Selecting a judge model](/concepts/customizing-llm-judge-models.md) – How to change the underlying LLM for any built-in or custom judge.

## Sources

- correctness-judge-databricks-on-aws.md

# Citations

1. [correctness-judge-databricks-on-aws.md](/references/correctness-judge-databricks-on-aws-85181199.md)
