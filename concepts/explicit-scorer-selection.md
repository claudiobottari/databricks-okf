---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 486a6c6f526a9cb18e6a2bb746a076e3a793fd08b803b2f590d96fa3a9ff0f1f
  pageDirectory: concepts
  sources:
    - migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - explicit-scorer-selection
    - ESS
    - scorer model selection
  citations:
    - file: migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md
title: Explicit Scorer Selection
description: MLflow 3 requires users to explicitly list all scorers for evaluation, unlike MLflow 2.x which automatically selected applicable judges based on data fields.
tags:
  - mlflow
  - evaluation
  - migration
timestamp: "2026-06-19T19:34:49.213Z"
---

# Explicit Scorer Selection

**Explicit Scorer Selection** is a design change in MLflow 3's GenAI evaluation that requires users to manually list the scorers (including [LLM Judges](/concepts/llm-judges.md)) they want to run during `mlflow.genai.evaluate()`. In contrast, MLflow 2.x automatically selected and ran a set of applicable judges based on the evaluation data, without requiring the user to specify them. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Motivation

The shift from automatic to explicit scorer selection gives users more control over which metrics are computed. Automatic selection could run judges that the user did not intend or was not aware of, potentially increasing cost, latency, or producing irrelevant results. Explicit selection avoids surprises and makes the evaluation configuration fully transparent. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## How to Use

In MLflow 3, you pass a list of scorer instances to the `scorers` parameter of `mlflow.genai.evaluate()`. These can be predefined scorers (such as `Correctness()`, `Safety()`, `RetrievalGroundedness()`) or custom scorers created with the `@scorer` decorator. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Correctness, Safety, RetrievalGroundedness

results = mlflow.genai.evaluate(
    data=eval_data,
    predict_fn=my_agent,
    scorers=[
        Correctness(),
        Safety(),
        RetrievalGroundedness()
    ]
)
```

If no scorers are provided, the evaluation will run without any scoring. This is a key difference from MLflow 2.x, where omitting the `metrics` configuration would still run all applicable judges. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Comparison with Automatic Selection

The following table summarises the behavioural change:

| Aspect | MLflow 2.x (Automatic) | MLflow 3.x (Explicit) |
|--------|------------------------|------------------------|
| Default behaviour | Runs all applicable judges based on data columns (e.g., `expected_response`, `retrieved_context`) | Runs no scorers unless explicitly listed |
| Control | Limited to filtering with `evaluator_config["metrics"]` | Full control: each scorer is individually included or excluded |
| Custom metrics | Added via `extra_metrics` alongside automatic judges | Custom scorers are simply included in `scorers` list |

To replicate MLflow 2.x’s automatic behaviour in MLflow 3, you must manually list every scorer you want to use, including those that require ground truth (e.g., `Correctness`) and those that do not (e.g., `RelevanceToQuery`). ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Common Pitfall

A frequent mistake during migration is forgetting to specify scorers. Because MLflow 3 does not automatically run judges, an evaluation that produces no scores is not necessarily an error—it simply means no scorers were configured. Always verify that the `scorers` parameter includes all desired metrics. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Related Concepts

- [LLM Judges](/concepts/llm-judges.md) – The underlying AI models that evaluate responses; wrapped by predefined scorers.
- [Predefined scorers](/concepts/mlflow-genai-predefined-scorers.md) – Ready-to-use scorers like `Correctness`, `Safety`, and `RetrievalGroundedness`.
- [Custom scorer](/concepts/custom-scorers-mlflow-genai.md) – User-defined evaluation functions created with the `@scorer` decorator.
- [mlflow.genai.evaluate()](/concepts/mlflowgenaievaluate.md) – The GenAI evaluation API that accepts explicit scorers.
- [Evaluation data schema](/concepts/evaluation-dataset-schema.md) – The `inputs`, `outputs`, `expectations` structure expected by MLflow 3.

## Sources

- migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md

# Citations

1. [migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md](/references/migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws-7eefbe86.md)
