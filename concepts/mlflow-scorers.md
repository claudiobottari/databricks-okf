---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 716ece1bff25e8f5e0447bd325c240cae1fdb60b9d93a030440eb8ed7b6ab5e5
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-scorers
    - MLflow 3 Scorers
    - MLflow Scorer
    - MLflow Scoring
    - scorers (MLflow)|scorers
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
    - file: evaluate-genai-apps-during-development-databricks-on-aws.md
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
    - file: optimize-multiple-prompts-together-databricks-on-aws.md
title: MLflow Scorers
description: Pluggable evaluation criteria in MLflow that assess LLM outputs against custom guidelines or built-in policies, including Guidelines scorer and Safety scorer.
tags:
  - mlflow
  - evaluation
  - scorers
timestamp: "2026-06-19T13:49:10.164Z"
---

# MLflow Scorers

**MLflow Scorers** are configurable evaluation criteria used to automatically assess the outputs of a GenAI application during evaluation. They are passed as a list to `mlflow.genai.evaluate()` and applied to each row of an evaluation dataset, producing structured feedback—such as pass/fail labels, numeric scores, or categorical ratings—that is recorded as [MLflow Assessment|assessments](/concepts/mlflow-assessment-and-assessmentsource-api.md) on the generated traces. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Types of Scorers

MLflow provides several built-in scorers that cover common evaluation dimensions:

- **`Guidelines`** – Checks whether a response adheres to one or more natural-language rules (e.g., "Response must be funny", "Response must be appropriate for children"). You provide the guidelines as strings, and MLflow uses an LLM to evaluate compliance. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]
- **`Safety`** – A built-in scorer that detects harmful or unsafe content in the output. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]
- **`RelevanceToQuery`** – Measures how relevant the response is to the user's question. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]
- **`Correctness`** – Compares the app's output against an expert-provided expected response, producing a quantitative correctness score. This scorer is particularly useful when [Human Feedback Collection|human feedback](/concepts/mlflow-human-feedback-collection.md) has been collected via labeling sessions. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md] ^[optimize-multiple-prompts-together-databricks-on-aws.md]

For use cases beyond these built-in options, you can define [Custom Scorers|custom scorers](/concepts/custom-scorers-mlflow-genai.md) that implement your own evaluation logic. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Usage

Scorers are imported from `mlflow.genai.scorers` and passed to `mlflow.genai.evaluate()` as the `scorers` parameter:

```python
from mlflow.genai.scorers import Guidelines, Safety, RelevanceToQuery

scorers = [
    Guidelines(guidelines="Response must be in the same language as the input", name="same_language"),
    Guidelines(guidelines="Response must be funny or creative", name="funny"),
    Safety(),
]

results = mlflow.genai.evaluate(
    data=eval_data,
    predict_fn=my_app,
    scorers=scorers,
)
```

^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

When using the `Correctness` scorer, the evaluation data must include an `expected_response` field (typically populated by expert reviewers). The scorer then judges how well the generated output matches that expected answer. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### LLM-as-Judge Scorers

Some built-in scorers, such as `Correctness`, can also be configured to use a specific judge model by passing the `model` parameter:

```python
Correctness(model="databricks:/databricks-claude-sonnet-4-5")
```

This is useful when you want to control which LLM performs the evaluation. ^[optimize-multiple-prompts-together-databricks-on-aws.md]

## Viewing Scorer Results in the UI

After an evaluation run, the results appear in the MLflow Experiment UI as **Assessments**. Each scorer's output is shown as a column in the trace table, with **Pass**/**Fail** labels (for binary scorers) or numeric values. Hovering over a label reveals the underlying rationale. You can also open individual traces to inspect the full input, output, and per-scorer feedback. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Relationship to Evaluation Runs

Scorers are a core component of [MLflow GenAI evaluation runs](/concepts/mlflow-genai-evaluation.md). Each evaluation run logs one trace per test input, annotated with the feedback produced by each scorer. This makes it easy to compare versions of an app, track regressions, and share results across teams. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Sources

- [10-minute demo: Evaluate a GenAI app | Databricks on AWS](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/eval) ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]
- [Evaluate GenAI apps during development | Databricks on AWS](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/eval-harness) ^[evaluate-genai-apps-during-development-databricks-on-aws.md]
- [10-minute demo: Collect human feedback | Databricks on AWS](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/human-feedback) ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]
- [Optimize multiple prompts together | Databricks on AWS](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/optimize-multiple-prompts-together) ^[optimize-multiple-prompts-together-databricks-on-aws.md]

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
2. [evaluate-genai-apps-during-development-databricks-on-aws.md](/references/evaluate-genai-apps-during-development-databricks-on-aws-373c1693.md)
3. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
4. [optimize-multiple-prompts-together-databricks-on-aws.md](/references/optimize-multiple-prompts-together-databricks-on-aws-a41f0275.md)
