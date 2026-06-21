---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f77899312fe4387c0d07707d453350d29aff51c2ad613557ca26823939e1f407
  pageDirectory: concepts
  sources:
    - safety-judge-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - built-in-judges-mlflow
    - BJ(
    - Built-in Judges (MLflow GenAI)
    - Judge (MLflow GenAI)
    - judge (MLflow)
  citations:
    - file: safety-judge-databricks-on-aws.md
title: Built-in Judges (MLflow)
description: Pre-configured LLM-based judges for assessing GenAI quality dimensions including safety, relevance, groundedness, and correctness.
tags:
  - mlflow
  - llm-evaluation
  - genai
timestamp: "2026-06-19T20:17:51.509Z"
---

# Built-in Judges (MLflow)

**Built-in Judges** in MLflow are pre-configured LLM-based evaluation scorers that assess the quality, safety, and relevance of generative AI model outputs. These judges use an underlying language model to perform automated assessments, returning structured scores and detailed rationales for each evaluation dimension.^[safety-judge-databricks-on-aws.md]

## Overview

Built-in judges provide standardized evaluation capabilities without requiring manual human review or custom scoring logic. Each judge is designed to assess a specific quality dimension, such as safety, correctness, or groundedness. The judges return both a scoring decision (typically pass/fail for safety assessments) and a detailed rationale explaining the assessment.^[safety-judge-databricks-on-aws.md]

## Judge Types

MLflow offers several built-in judges, each focused on a particular evaluation dimension:

- **Safety judge** – Evaluates text content to identify potentially harmful, offensive, or inappropriate material. Returns a pass/fail assessment with a detailed rationale.^[safety-judge-databricks-on-aws.md]
- **Guidelines judge** – Assesses output against user-defined custom safety criteria, enabling tailored evaluation for specific use cases.^[safety-judge-databricks-on-aws.md]
- Other built-in judges cover dimensions like relevance, groundedness, and correctness.^[safety-judge-databricks-on-aws.md]

## Judge Model Selection

By default, built-in judges use a Databricks-hosted LLM designed specifically for performing GenAI quality assessments. Users can customize the underlying model using the `model` argument when creating a judge instance. The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. If using `databricks` as the provider, the model name corresponds to the serving endpoint name.^[safety-judge-databricks-on-aws.md]

## Usage

Built-in judges can be invoked directly for single assessments or used with MLflow's evaluation framework (`mlflow.genai.evaluate()`) for batch evaluation. The following examples demonstrate common usage patterns.^[safety-judge-databricks-on-aws.md]

### Direct Invocation

```python
from mlflow.genai.scorers import Safety

# Assess the safety of a single output
assessment = Safety(
    outputs="MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models."
)
print(assessment)
```
^[safety-judge-databricks-on-aws.md]

### Batch Evaluation

```python
from mlflow.genai.scorers import Safety

safety_judge = Safety()

# Run evaluation with Safety judge
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[safety_judge]
)
```
^[safety-judge-databricks-on-aws.md]

### Custom Judge Model

```python
from mlflow.genai.scorers import Safety

# Use a different model for safety evaluation
safety_judge = Safety(
    model="databricks:/databricks-claude-opus-4-5"
)

eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[safety_judge]
)
```
^[safety-judge-databricks-on-aws.md]

## Related Concepts

- [LLM Evaluation](/concepts/llm-as-a-judge-evaluation.md) – Broader context for evaluating generative AI model outputs
- [Production Monitoring](/concepts/production-monitoring.md) – Continuous monitoring of deployed applications using built-in judges
- [Guidelines Judge](/concepts/guidelines-llm-judge.md) – Custom safety criteria evaluation
- [MLflow Experiments](/concepts/mlflow-experiment.md) – Organizational unit for evaluation runs

## Sources

- safety-judge-databricks-on-aws.md

# Citations

1. [safety-judge-databricks-on-aws.md](/references/safety-judge-databricks-on-aws-d841b2a4.md)
