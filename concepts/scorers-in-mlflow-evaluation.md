---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bfa0d4478c043c973783a7912bc4dac892dc4adc0a4db6a236cb876c5808e544
  pageDirectory: concepts
  sources:
    - evaluate-genai-apps-during-development-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorers-in-mlflow-evaluation
    - SIME
  citations:
    - file: evaluate-genai-apps-during-development-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Scorers in MLflow Evaluation
description: Quality metrics (built-in or custom) applied by mlflow.genai.evaluate() to assess GenAI app outputs, including LLM judges for relevance, safety, and more.
tags:
  - mlflow
  - evaluation
  - metrics
  - scorers
timestamp: "2026-06-19T10:24:04.934Z"
---

# Scorers in MLflow Evaluation

**Scorers** are quality metrics that assess the outputs of GenAI applications during evaluation with `mlflow.genai.evaluate()`. They provide automated, structured scoring of app outputs against defined criteria, enabling teams to measure quality consistently across development and production. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Overview

When you call `mlflow.genai.evaluate()`, you provide a list of scorers that are applied to each evaluation record. Scorers analyze the inputs, outputs, and optionally the full execution trace of your GenAI app, returning structured feedback values such as pass/fail labels, numeric scores, or categorical ratings. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

Scorers serve as the bridge between offline testing and [production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md). The same scorers defined during development can be reused in production, providing a consistent view of quality across the entire AI lifecycle. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Types of Scorers

### Built-in Scorers

MLflow provides several built-in scorers that cover common evaluation needs. These include:

- **RelevanceToQuery** – Assesses how relevant the app's response is to the user's query.
- **Safety** – Evaluates whether the app's output contains harmful or unsafe content.

Built-in scorers are imported from `mlflow.genai.scorers` and can be used directly in the `scorers` parameter of `mlflow.genai.evaluate()`. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

### Custom Scorers

For application-specific quality criteria, you can define [custom scorers](/concepts/custom-scorers-mlflow-genai.md) that implement your own evaluation logic. Custom scorers can be tailored to assess domain-specific behaviors, adherence to guidelines, or any other quality dimension relevant to your use case. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

### LLM Judges

A common pattern for custom scorers is to use an LLM as a judge. These [LLM Judges](/concepts/llm-judges.md) are scorers that use a language model to evaluate outputs against a rubric or set of criteria. The `make_judge()` API simplifies creating such judges by allowing you to define evaluation instructions, feedback types, and grading scales. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## How Scorers Work

During evaluation, each scorer receives the evaluation data (inputs and outputs) and optionally the full execution [trace](/concepts/traces.md) of the app call. The scorer processes this information and returns feedback, which is stored as annotations on the trace in the [Evaluation Run](/concepts/evaluation-run.md). ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

Scorers can be categorized by what they analyze:

- **Input/Output scorers** – Evaluate the agent's behavior by analyzing conversation history (inputs) and agent responses (outputs). Common criteria include issue resolution status and adherence to expected behaviors. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Trace-based scorers** – Analyze the full execution trace of an agent call, including tool invocations, intermediate reasoning steps, and their results. These scorers can validate whether appropriate tools were called for a given user request. To create a trace-based scorer, include `{{ trace }}` in the judge's instructions. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Using Scorers in Evaluation

Scorers are passed as a list to the `scorers` parameter of `mlflow.genai.evaluate()`:

```python
import mlflow
from mlflow.genai.scorers import RelevanceToQuery, Safety

results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=my_chatbot_app,
    scorers=[RelevanceToQuery(), Safety()]
)
```

^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Viewing Scorer Results

After evaluation, results are stored in an [Evaluation Run](/concepts/evaluation-run.md). In the MLflow UI, you can view aggregate metrics and investigate individual test cases. Each scorer's assessment is displayed with a **Pass** or **Fail** label, and hovering over the label reveals the rationale behind the assessment. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The evaluation harness that applies scorers to GenAI apps.
- [Custom Judges](/concepts/custom-judges.md) – LLM-based scorers created with `make_judge()`.
- [Evaluation Datasets](/concepts/evaluation-datasets.md) – The test data that scorers evaluate against.
- [Evaluation Runs](/concepts/evaluation-runs.md) – The container for evaluation results and scorer feedback.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Reusing scorers in production for continuous quality monitoring.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – Using consistent scorers to compare agent variants.

## Sources

- evaluate-genai-apps-during-development-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [evaluate-genai-apps-during-development-databricks-on-aws.md](/references/evaluate-genai-apps-during-development-databricks-on-aws-373c1693.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
