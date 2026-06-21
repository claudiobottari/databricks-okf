---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4e728f93ee9a6a04c1c02b619bc6024bd162ebd0f9822036ae9cf37b0e05e14f
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-guidelines-scorer
    - MGS
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
title: MLflow Guidelines Scorer
description: A scorer that evaluates LLM outputs against custom natural-language guidelines such as language consistency, humor, child safety, and template adherence.
tags:
  - mlflow
  - scorers
  - evaluation
timestamp: "2026-06-18T14:15:09.849Z"
---

# MLflow Guidelines Scorer

The **MLflow Guidelines Scorer** is a built-in [MLflow Scorer](/concepts/mlflow-scorers.md) that evaluates whether [GenAI](/concepts/mlflow-genai-evaluate-api.md) model outputs comply with a set of user-defined guidelines or rules. It is a key component of the [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) framework, designed to help developers systematically assess the quality and consistency of AI-generated content against predefined behavioral criteria. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Overview

The Guidelines Scorer provides a structured way to define and enforce quality criteria for GenAI applications. It allows developers to specify custom guidelines that the model's responses must follow, and then evaluates the responses against those guidelines at inference time. This is particularly useful for ensuring that AI outputs align with specific requirements, such as language constraints, content appropriateness, or structural fidelity to input templates. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Creating a Guidelines Scorer

The Guidelines Scorer is created using the `mlflow.genai.scorers.Guidelines` class, which requires two parameters: the guidelines text and a name for the scorer. The guidelines text contains the rules that the model's responses should follow, written in natural language. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Syntax

```python
from mlflow.genai.scorers import Guidelines
import mlflow.genai

scorers = [
    Guidelines(
        guidelines="Response must be in the same language as the input",
        name="same_language"
    ),
    Guidelines(
        guidelines="Response must be funny or creative",
        name="funny"
    ),
]
```

### Common Use Cases

The following examples show typical guidelines used in the 10-minute demo: ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

| Guidelines | Name | Purpose |
|-----------|------|---------|
| "Response must be in the same language as the input" | same_language | Ensures language consistency |
| "Response must be funny or creative" | funny | Evaluates creativity |
| "Response must be appropriate for children" | child_safe | Filters for child safety |
| "Response must follow the input template structure from the request - filling in the blanks without changing the other words" | template_match | Checks structural fidelity |

## Using the Guidelines Scorer in Evaluation

The Guidelines Scorer is used as part of the `scorers` parameter in `mlflow.genai.evaluate()`. It runs alongside other scorers, such as the [Safety Scorer](/concepts/safety-scorer-in-mlflow.md), to provide a comprehensive evaluation of the GenAI application. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Example

```python
result = mlflow.genai.evaluate(
    data=eval_data,
    predict_fn=generate_game,
    scorers=scorers
)
```

In this example, the Guidelines Scorer evaluates whether the generated sentence completions follow the specified rules, including language consistency, humor, child-appropriateness, and template structure. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Guidelines vs Safety Scorer

While the [Safety Scorer](/concepts/safety-scorer-in-mlflow.md) provides built-in safety checks for content, the Guidelines Scorer allows for fully customizable criteria. Users can define any set of rules in natural language, making it suitable for domain-specific requirements. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Iterative Improvement

The Guidelines Scorer supports iterative development. After running an initial evaluation, developers can refine their guidelines and re-run the evaluation to compare results in the [MLflow UI](/concepts/mlflow.md). This allows teams to systematically improve the quality and consistency of their GenAI applications. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The framework for evaluating GenAI applications
- [MLflow Scorers](/concepts/mlflow-scorers.md) — The scoring framework that evaluates model outputs
- [Safety Scorer](/concepts/safety-scorer-in-mlflow.md) — A built-in scorer for content safety
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The evaluation API for running assessments
- [Evaluation Dataset](/concepts/evaluation-dataset.md) — The data used for evaluation

## Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
