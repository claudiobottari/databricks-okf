---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 95a28c5ae09f5b12b9c9e432410b14a528de1f3099f26cdfa17a8a7e14187b59
  pageDirectory: concepts
  sources:
    - correctness-judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-judge-customization
    - LJC
    - LLM Judges with custom prompts
  citations:
    - file: correctness-judge-databricks-on-aws.md
title: LLM Judge Customization
description: The ability to change the underlying model that powers a built-in LLM judge by specifying a different model via the 'model' argument using LiteLLM-compatible format.
tags:
  - llm-judges
  - customization
  - mlflow
timestamp: "2026-06-19T09:26:15.852Z"
---

# LLM Judge Customization

**LLM Judge Customization** refers to the ability to modify the behavior of built-in LLM judges — such as the `Correctness` judge — by selecting a different underlying language model, or by creating entirely new judges tailored to domain-specific quality criteria. This flexibility allows teams to align automated evaluation with their application’s unique requirements.

## Customizing the Judge Model

By default, built-in judges like `Correctness` use a Databricks‑hosted LLM designed specifically for GenAI quality assessments. You can customize which LLM powers a judge by passing the `model` argument when instantiating the judge. The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM‑compatible model provider. Using `databricks` as the provider means the model name is the same as a Databricks serving endpoint name. ^[correctness-judge-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Correctness

# Use a different judge model
correctness_judge = Correctness(
    model="databricks:/databricks-gpt-5-mini"  # Or any LiteLLM-compatible model
)

# Use in evaluation
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[correctness_judge]
)
```

This customization can be applied to any built-in judge that supports the `model` argument, allowing you to choose a model that better suits your evaluation cost, latency, or accuracy targets. ^[correctness-judge-databricks-on-aws.md]

## Creating Custom Judges

Beyond selecting an alternative LLM for an existing built-in judge, you can build **custom judges** from scratch for domain‑specific evaluation criteria. Custom judges are LLM‑based scorers that evaluate outputs against your own definitions of quality, safety, or behavior. For detailed guidance, see the [Create custom judges](/concepts/custom-judges.md) documentation. ^[correctness-judge-databricks-on-aws.md]

## Related Concepts

- [Built‑in judges](/concepts/built-in-judges.md) – The set of pre‑built LLM judges (e.g., Correctness, Toxicity) that can be customized.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The evaluation framework where judges are used as scorers.
- make_judge()|Make Judge API – The `make_judge()` function for creating custom evaluators.

## Sources

- correctness-judge-databricks-on-aws.md

# Citations

1. [correctness-judge-databricks-on-aws.md](/references/correctness-judge-databricks-on-aws-85181199.md)
