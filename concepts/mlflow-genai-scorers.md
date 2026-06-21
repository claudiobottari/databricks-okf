---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8581fe09dcdf7512a6c851e54e83eed9f25acb8766d8cc332b94e28afa03babd
  pageDirectory: concepts
  sources:
    - get-started-mlflow-3-for-genai-databricks-on-aws.md
    - mlflow-evaluation-examples-for-genai-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-scorers
    - MGS
    - mlflow.genai.Scorer.start()
    - GenAI Scorers
  citations:
    - file: get-started-mlflow-3-for-genai-databricks-on-aws.md
    - file: mlflow-evaluation-examples-for-genai-databricks-on-aws.md
title: MLflow GenAI Scorers
description: Modular scoring components (built-in like Safety, and custom like Guidelines) used to evaluate GenAI outputs programmatically within MLflow Evaluation workflows.
tags:
  - mlflow
  - evaluation
  - scorers
  - genai
timestamp: "2026-06-19T18:59:00.341Z"
---

# MLflow GenAI Scorers

**MLflow GenAI Scorers** are evaluation components used by MLflow to judge the quality of outputs from [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications. They serve as the core building block for automated evaluation, enabling both offline evaluation during development and continuous monitoring in production. Scorers assess outputs against defined quality criteria using [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) techniques or custom logic.^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

During evaluation, scorers are applied to each row of an evaluation dataset, producing scores that are logged to the active MLflow experiment. Results can be reviewed in the Experiment UI under the **Evaluations** tab.^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Types of Scorers

### Built‑in Scorers

MLflow provides several built‑in LLM‑as‑a‑judge scorers for common quality dimensions:

- **Safety**: Evaluates whether responses contain harmful, toxic, or unsafe content.^[get-started-mlflow-3-for-genai-databricks-on-aws.md]
- **Correctness**: Assesses how accurately the response matches expected facts or ground truth.^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]
- **RelevanceToQuery**: Measures how relevant the response is to the user’s query.^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

These scorers are imported from `mlflow.genai.scorers` and can be passed directly to `mlflow.genai.evaluate()`.

### Custom Scorers

#### Guidelines Scorer

The `Guidelines` scorer is a custom LLM‑as‑a‑judge scorer that evaluates responses against user‑defined criteria expressed in natural language. You create a `Guidelines` instance with a `guidelines` string describing the expected behavior and an optional `name`.^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Guidelines

scorers = [
    Guidelines(
        guidelines="Response must be in the same language as the input",
        name="same_language",
    ),
    Guidelines(
        guidelines="Response must be funny or creative",
        name="funny"
    ),
]
```

Multiple `Guidelines` scorers can be combined in a single evaluation to cover different aspects of quality.

#### Custom Code‑Based Scorers

MLflow also supports fully custom code‑based scorers for evaluation logic that cannot be expressed through guidelines alone. This allows you to implement arbitrary scoring functions.^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Using Scorers in Evaluation

Scorers are passed as a list to the `mlflow.genai.evaluate()` function, which runs the agent on the evaluation data and then applies all specified scorers to judge the outputs.^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.scorers import Correctness, Safety

results = mlflow.genai.evaluate(
    data=eval_data,
    predict_fn=agent,
    scorers=[Correctness(), Safety()],
)
```

Evaluation data can be provided as an [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md), a list of dictionaries, a Pandas DataFrame, or a Spark DataFrame. The `predict_fn` can be a traced function, a wrapped callable, or a deployed endpoint via `to_predict_fn`.^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## Development‑to‑Production Pipeline

A key advantage of MLflow GenAI Scorers is their reusability across the development lifecycle. The same scorers used during offline evaluation can be deployed for [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md), ensuring consistent quality assessment from development through production.^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The overall evaluation framework that uses scorers.
- [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) — The technique underlying MLflow’s built‑in and custom scorers.
- Custom Judges (make_judge)|Custom Judges Using Make Judge — Advanced custom judge creation for specialized evaluation needs.
- [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) — Versioned datasets used with scorers during evaluation.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Using scorers to compare different agent versions.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying scorers for continuous quality monitoring.
- [Human feedback collection with MLflow](/concepts/human-feedback-collection-in-mlflow.md) — Complementary human evaluation to supplement scorer‑based judgments.

## API Reference

- [`mlflow.genai.scorer()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorer)
- [`mlflow.genai.evaluate()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate)

## Sources

- get-started-mlflow-3-for-genai-databricks-on-aws.md
- mlflow-evaluation-examples-for-genai-databricks-on-aws.md

# Citations

1. [get-started-mlflow-3-for-genai-databricks-on-aws.md](/references/get-started-mlflow-3-for-genai-databricks-on-aws-4186f156.md)
2. [mlflow-evaluation-examples-for-genai-databricks-on-aws.md](/references/mlflow-evaluation-examples-for-genai-databricks-on-aws-2da85b83.md)
