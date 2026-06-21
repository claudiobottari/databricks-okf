---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fa122020f0b716af810c84acf59e1390d0bf6fdc3877e1f0f84a5f31b5124b8d
  pageDirectory: concepts
  sources:
    - safety-judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - safety-judge-mlflow
    - SJ(
    - Safety Judge
    - Safety Judges
    - Safety judge
  citations:
    - file: safety-judge-databricks-on-aws.md
title: Safety Judge (MLflow)
description: A built-in MLflow judge that evaluates text content to identify potentially harmful, offensive, or inappropriate material, returning a pass/fail assessment with detailed rationale.
tags:
  - llm-evaluation
  - safety
  - mlflow
  - genai
timestamp: "2026-06-19T20:17:52.963Z"
---

# Safety Judge (MLflow)

The **Safety judge** is a built-in [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) scorer provided by [MLflow](/concepts/mlflow.md) that evaluates text content to identify potentially harmful, offensive, or inappropriate material. It returns a pass/fail assessment along with a detailed rationale explaining any safety concerns. ^[safety-judge-databricks-on-aws.md]

For API details, see the MLflow documentation. For detailed documentation and additional examples, see the MLflow Safety judge documentation. ^[safety-judge-databricks-on-aws.md]

## Prerequisites

To run the usage examples, you must first install MLflow and required packages, then create an MLflow experiment by following the “setup your environment” quickstart. ^[safety-judge-databricks-on-aws.md]

```python
%pip install --upgrade "mlflow[databricks]>=3.4.0"
dbutils.library.restartPython()
```

## Usage examples

The Safety judge can be invoked directly for single assessment or used with MLflow’s [MLflow Evaluation Framework|evaluation framework](/concepts/mlflow-genai-evaluation-framework.md) for batch evaluation. ^[safety-judge-databricks-on-aws.md]

### Invoke directly

```python
from mlflow.genai.scorers import Safety

# Assess the safety of a single output
assessment = Safety(
    outputs="MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models."
)
print(assessment)
```

### Invoke with evaluate()

To use the Safety judge as part of a batch evaluation, pass it in the `scorers` list to `mlflow.genai.evaluate()`. ^[safety-judge-databricks-on-aws.md]

## Select the LLM that powers the judge

By default, built-in judges use a Databricks-hosted LLM designed to perform GenAI quality assessments. You can change the judge model by using the `model` argument when you create the judge. The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. If you use `databricks` as the model provider, the model name is the same as the serving endpoint name. ^[safety-judge-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Safety

# Use a different model for safety evaluation
safety_judge = Safety(
    model="databricks:/databricks-claude-opus-4-5"
)

# Run evaluation with Safety judge
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[safety_judge]
)
```

## Next steps

- Explore other built-in judges – [Relevance Judge](/concepts/relevancetoquery.md), Groundedness Judge, [Correctness Judge](/concepts/correctness-judge.md).
- [Production Monitoring (MLflow)|Monitor safety in production](/concepts/production-monitoring-for-genai-applications.md) – Set up continuous safety monitoring for deployed applications.
- Guidelines Judge|Create custom safety guidelines – Define specific safety criteria for your use case.

## Related concepts

- [LLM-as-a-Judge](/concepts/llm-as-a-judge.md)
- [GenAI Evaluators](/concepts/mlflow-genai-evaluation.md)
- MLflow Evaluation Framework
- Safe AI

## Sources

- safety-judge-databricks-on-aws.md

# Citations

1. [safety-judge-databricks-on-aws.md](/references/safety-judge-databricks-on-aws-d841b2a4.md)
