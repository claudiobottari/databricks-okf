---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8d451de962570a673499b493d4205ff3e432c15ae73d9d2ae7d246d7e578b47a
  pageDirectory: concepts
  sources:
    - correctness-judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - customizing-llm-judge-models
    - CLJM
    - Selecting a judge model
  citations:
    - file: correctness-judge-databricks-on-aws.md
title: Customizing LLM Judge Models
description: The ability to swap the underlying LLM powering a built-in judge by specifying a different model via the 'model' argument using LiteLLM-compatible provider format, enabling use of custom or proprietary models for evaluation.
tags:
  - mlflow
  - llm-evaluation
  - model-configuration
timestamp: "2026-06-18T11:12:01.251Z"
---

# Customizing LLM Judge Models

**Customizing LLM Judge Models** refers to the ability to select an alternative large language model (LLM) that powers a built-in judge in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) evaluation and monitoring. By default, built-in judges such as [Correctness Judge](/concepts/correctness-judge.md) use a Databricks-hosted LLM optimized for quality assessment, but you can override this to use a different model — either another Databricks serving endpoint or any model compatible with LiteLLM. ^[correctness-judge-databricks-on-aws.md]

## Prerequisites

- MLflow version 3.4.0 or later (`%pip install --upgrade "mlflow[databricks]>=3.4.0"`).
- A configured MLflow experiment (see Setting up an MLflow environment). ^[correctness-judge-databricks-on-aws.md]

## How to customize the judge model

When instantiating a built-in judge, pass a `model` argument in the format `<provider>:/<model-name>`. The provider must be a LiteLLM-compatible model provider. If you use `databricks` as the provider, the model name corresponds to a [Databricks Model Serving](/concepts/databricks-model-serving.md) endpoint name. ^[correctness-judge-databricks-on-aws.md]

The same customization applies whether you invoke the judge directly or use it within `mlflow.genai.evaluate()`.

### Example: Changing the Correctness judge model

```python
from mlflow.genai.scorers import Correctness

# Use a Databricks-hosted GPT-5 mini endpoint
correctness_judge = Correctness(
    model="databricks:/databricks-gpt-5-mini"
)

# Use in evaluation
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[correctness_judge]
)
```

^[correctness-judge-databricks-on-aws.md]

The same pattern works for other built-in judges (e.g., Flesch Kincaid Judge, [Answer Relevance Judge](/concepts/answerrelevancy-scorer.md), etc.) that accept a model argument. The model string can also reference any LiteLLM-compatible external provider, such as `openai:/gpt-4o` or `anthropic:/claude-sonnet-4`. ^[correctness-judge-databricks-on-aws.md]

## Considerations

- The alternative model must be accessible from your runtime environment — for Databricks endpoints, the appropriate permissions must be in place.
- Customization changes only the LLM that evaluates responses; the judge’s prompt, output schema, and behavior (e.g., returning `"yes"` or `"no"` with a rationale) remain the same.
- If you need fundamentally different evaluation logic, consider creating a [Custom Judge](/concepts/custom-judges.md) instead.

## Related concepts

- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — The full list of quality assessment judges that support model customization
- LiteLLM — The model provider abstraction used to specify the judge model
- [Databricks Model Serving](/concepts/databricks-model-serving.md) — Endpoints that can serve as judge models
- [Custom Judge](/concepts/custom-judges.md) — For domain-specific evaluation logic beyond model selection

## Sources

- correctness-judge-databricks-on-aws.md

# Citations

1. [correctness-judge-databricks-on-aws.md](/references/correctness-judge-databricks-on-aws-85181199.md)
