---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 58afa5580f90c33d5bb90cbeb3c7c7a2fb4e1d99b6f63b99c876e5d0604dfff1
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - feedback-objects-in-mlflow
    - FOIM
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Feedback Objects in MLflow
description: Return type of make_judge() judges, represented as mlflow.entities.Feedback objects containing evaluation results with typed ratings
tags:
  - mlflow
  - feedback
  - evaluation
timestamp: "2026-06-18T14:46:28.652Z"
---

# Feedback Objects in MLflow

**Feedback Objects** in MLflow are the structured results returned by custom judges created with the [`make_judge()`](/wiki/make_judge) API. They encapsulate the output of an LLM-based evaluation of a GenAI agent's response against a specific quality criterion.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Usage in GenAI Evaluation

When you define a custom judge using `make_judge()` and pass it as a scorer to [`mlflow.genai.evaluate()`](/wiki/mlflow-genai-evaluate), the evaluation produces a Feedback object for each judge–input pair. The Feedback object contains the rating or score that the judge assigned (e.g., `"fully_resolved"`, `true`) along with any supporting rationale.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Structure

The Feedback object is part of the `mlflow.entities` module. Its type is [`mlflow.entities.Feedback`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Feedback). The exact fields are defined in the MLflow API documentation, but the key component is the `value` — a string, boolean, or enum literal that reflects the judge's evaluation outcome. The `feedback_value_type` parameter of `make_judge()` determines the type of value the Feedback object will carry.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [Custom Judges](/concepts/custom-judges.md) – LLM-based scorers that produce Feedback objects.
- make_judge()|Make Judge API – The `make_judge()` function used to create judges.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The `mlflow.genai.evaluate()` API that invokes judges and collects Feedback objects.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – Comparing Feedback object distributions across different agent versions.

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
