---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6bd499df35a6c20bcd225075bccdef07573a09c1e15c187625db2fee22ade39c
  pageDirectory: concepts
  sources:
    - safety-judge-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-hosted-llm-for-judges
    - DLFJ
  citations:
    - file: safety-judge-databricks-on-aws.md
title: Databricks-hosted LLM for Judges
description: The default LLM model provided by Databricks that powers built-in GenAI quality assessment judges, with the option to switch to other models via the 'model' argument.
tags:
  - databricks
  - llm
  - mlflow
timestamp: "2026-06-19T20:17:59.215Z"
---

# Databricks-hosted LLM for Judges

The **Databricks-hosted LLM for Judges** is the default large language model used by MLflow's built-in GenAI quality judges (such as the [Safety judge](/concepts/safety-judge-mlflow.md), [Groundedness judge](/concepts/retrievalgroundedness-judge.md), [Correctness Judge](/concepts/correctness-judge.md), and Relevance judge). It is a proprietary model hosted on Databricks serving endpoints, designed specifically to perform GenAI quality assessments on text outputs.

## Default Behavior

When you create a built-in judge without specifying a `model` argument, the judge automatically uses the Databricks-hosted LLM. This model is optimized for evaluation tasks and provides consistent scoring with detailed rationales. The default setup requires no additional configuration, allowing you to start evaluating immediately after installing MLflow and setting up an experiment. ^[safety-judge-databricks-on-aws.md]

## Customizing the Judge Model

You can override the default Databricks-hosted LLM by passing the `model` argument when instantiating a judge. The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. If you use `databricks` as the provider, the model name corresponds to a Databricks serving endpoint name. ^[safety-judge-databricks-on-aws.md]

For example, to use a custom endpoint:

```python
from mlflow.genai.scorers import Safety

safety_judge = Safety(
    model="databricks:/databricks-claude-opus-4-5"
)
```

This flexibility allows you to switch to a different LLM – either another Databricks-hosted model or a third-party provider – while still using the same evaluation framework. ^[safety-judge-databricks-on-aws.md]

## Use Cases

The Databricks-hosted LLM for Judges is employed in all built-in MLflow judges for:

- **Safety assessment** – detecting harmful, offensive, or inappropriate content
- **Response quality evaluation** – correctness, relevance, and groundedness
- **Custom guidelines** – when combined with the [Guidelines judge](/concepts/guidelines-llm-judge.md)

These evaluations can be performed as single assessments or batched via `mlflow.genai.evaluate()`. ^[safety-judge-databricks-on-aws.md]

## Requirements

To use the Databricks-hosted LLM for Judges, you must have MLflow installed with the Databricks extras (`mlflow[databricks]>=3.4.0`) and a configured MLflow experiment. No additional API keys or endpoint setup is needed for the default model. ^[safety-judge-databricks-on-aws.md]

## Related Concepts

- MLflow make_judge|MLflow GenAI judges – Overview of built-in and custom judges
- [Safety judge](/concepts/safety-judge-mlflow.md) – The judge for content safety
- [Guidelines judge](/concepts/guidelines-llm-judge.md) – Custom safety guidelines
- [Production Monitoring](/concepts/production-monitoring.md) – Using judges for continuous evaluation
- LiteLLM – Model provider abstraction used for specifying custom models
- [MLflow experiments](/concepts/mlflow-experiment.md) – Required environment for running evaluations

## Sources

- safety-judge-databricks-on-aws.md

# Citations

1. [safety-judge-databricks-on-aws.md](/references/safety-judge-databricks-on-aws-d841b2a4.md)
