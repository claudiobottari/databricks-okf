---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1227b412d4ac1cc9d7245fc45abe06216a3fdecae6e5d83b988eb72962c56319
  pageDirectory: concepts
  sources:
    - get-started-mlflow-3-for-genai-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genaievaluate-function
    - MGF
  citations:
    - file: get-started-mlflow-3-for-genai-databricks-on-aws.md
title: MLflow genai.evaluate Function
description: The mlflow.genai.evaluate() function runs a GenAI application against an evaluation dataset and applies scorers to judge outputs, logging results to the active MLflow experiment.
tags:
  - mlflow
  - evaluation
  - genai
  - api
timestamp: "2026-06-19T18:59:10.937Z"
---

# MLflow genai.evaluate Function

The `mlflow.genai.evaluate()` function is a core component of MLflow 3 for GenAI that runs a generative AI application (model or agent) on a dataset and then automatically judges the outputs using one or more scorers. It logs the resulting evaluation metrics to the active [MLflow Experiment](/concepts/mlflow-experiment.md), enabling developers to assess quality during development and prepare for production monitoring. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Overview

`mlflow.genai.evaluate()` combines model inference with automated evaluation in a single call. You provide:

- **`data`** – An evaluation dataset (typically a list of dictionaries with input fields).
- **`predict_fn`** – The function or model that generates responses (e.g., a traced GenAI application).
- **`scorers`** – A list of scorer objects ([built-in scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers) or [custom LLM-as-a-judge scorers](/concepts/custom-llm-as-a-judge-in-scorers.md)) that define the evaluation criteria.

The function runs `predict_fn` on each example in `data`, collects the outputs, and then applies each scorer to produce quality metrics such as `Safety`, `Correctness`, or custom guidelines. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Usage Example

The following snippet from the MLflow 3 for GenAI getting‑started guide illustrates the typical workflow:

```python
results = mlflow.genai.evaluate(
    data=eval_data,
    predict_fn=generate_game,
    scorers=scorers
)
```

After execution, the metrics are logged to the active experiment and can be reviewed in the Experiment UI under the **Evaluations** tab. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Logging Behavior

- Evaluation results are automatically logged to the currently active MLflow experiment. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]
- The logged data includes per‑example scores and aggregate metrics computed by each scorer. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]
- Users can inspect the results interactively in the notebook cell output or by navigating to the experiment’s **Evaluations** tab in the MLflow UI. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Related Concepts

- MLflow Evaluation and Monitoring – The broader framework for assessing GenAI applications.
- [[Scorers]] – Components that define evaluation criteria (built‑in or custom).
- [Custom LLM-as-a-Judge Scorers](/concepts/custom-llm-as-a-judge-in-scorers.md) – User‑defined guidelines used in evaluation.
- [MLflow Experiment](/concepts/mlflow-experiment.md) – The organizational unit where evaluation metrics are stored.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) – The input data used for evaluation.
- [Production Monitoring](/concepts/production-monitoring.md) – Where the same scorers can be reused to monitor live traffic.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – Instrumentation that records the inputs and outputs of GenAI applications.

## Sources

- get-started-mlflow-3-for-genai-databricks-on-aws.md

# Citations

1. [get-started-mlflow-3-for-genai-databricks-on-aws.md](/references/get-started-mlflow-3-for-genai-databricks-on-aws-4186f156.md)
