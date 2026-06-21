---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 09805019451128babccbdd397d069741e562ece2a6989fd87aaa65f863c99006
  pageDirectory: concepts
  sources:
    - correctness-judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - judge-model-customization
    - JMC
  citations:
    - file: correctness-judge-databricks-on-aws.md
title: Judge Model Customization
description: The ability to change the underlying LLM that powers a built-in judge by specifying a model in '<provider>:/<model-name>' format, supporting Databricks-hosted models and other LiteLLM-compatible providers.
tags:
  - llm-evaluation
  - configuration
  - mlflow
timestamp: "2026-06-19T17:54:22.750Z"
---

```markdown
---
title: Judge Model Customization
summary: The ability to change the underlying LLM that powers a built-in judge by specifying a different model via the model argument, supporting any LiteLLM-compatible provider.
sources:
  - correctness-judge-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:46:05.604Z"
updatedAt: "2026-06-19T14:28:14.887Z"
tags:
  - llm-evaluation
  - model-configuration
  - mlflow
aliases:
  - judge-model-customization
  - JMC
confidence: 0.9
provenanceState: merged
inferredParagraphs: 0
---

## Judge Model Customization

**Judge Model Customization** refers to the ability to change the underlying large language model (LLM) that powers a built-in or custom judge in [[MLflow 3 for GenAI|MLflow GenAI]]. By default, built-in judges use a Databricks-hosted LLM designed to perform GenAI quality assessments. You can override this default by specifying a different model using the `model` argument when you create the judge. ^[correctness-judge-databricks-on-aws.md]

## Specification Format

The judge model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. If you use `databricks` as the model provider, the model name must match the serving endpoint name. ^[correctness-judge-databricks-on-aws.md]

## Example

The following example shows how to create a [[Correctness Judge]] that uses a different model instead of the default Databricks-hosted LLM:

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

^[correctness-judge-databricks-on-aws.md]

You can apply the same pattern to other built-in judges (e.g., [[Safety Judge (MLflow)|Safety Judge]]) and to custom judges created with make_judge()|Make Judge API. In each case, passing a `model` argument changes the LLM that performs the evaluation.

## Considerations

- **Model capability**: A more powerful model may produce more accurate evaluations but at higher cost and latency. A smaller model may be sufficient for straightforward criteria.
- **Consistency**: When running [[A/B Comparison of Agent Configurations|A/B comparisons]], using the same judge model across all evaluations ensures that score differences reflect changes in agent behavior, not differences in the evaluator.
- **Availability**: The model must be deployed and accessible from your MLflow environment. For Databricks-hosted models, the model name corresponds to a serving endpoint name.

## Related Concepts

- [[Correctness Judge]] – Built-in judge for factual correctness.
- [[Safety Judge (MLflow)|Safety Judge]] – Built-in judge for content safety.
- make_judge()|Make Judge API – API to create custom judges.
- [[MLflow Evaluation UI|MLflow Evaluation]] – The `mlflow.genai.evaluate()` API for offline assessment.
- LiteLLM – Supported model providers for judge models.

## Sources

- correctness-judge-databricks-on-aws.md
```

# Citations

1. [correctness-judge-databricks-on-aws.md](/references/correctness-judge-databricks-on-aws-85181199.md)
