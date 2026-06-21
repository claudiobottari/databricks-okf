---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e44a2a583ed626aa0180ca1f44ff8b09411b8d8504a74bf13a20c2a3a414aaf7
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-scorers-guidelines-safety
    - MS(&S
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
title: MLflow Scorers (Guidelines & Safety)
description: Modular evaluation criteria in MLflow for assessing GenAI outputs against custom guidelines and built-in safety checks.
tags:
  - mlflow
  - evaluation
  - guidelines
  - safety
  - scorers
timestamp: "2026-06-19T21:53:46.565Z"
---

# MLflow Scorers (Guidelines & Safety)

**MLflow Scorers (Guidelines & Safety)** are evaluation components in the MLflow GenAI framework that enable quantitative assessment of large language model (LLM) outputs using either custom criteria defined in natural language or built-in safety checks. They are used with `mlflow.genai.evaluate()` to measure how well a GenAI application satisfies specific requirements such as language consistency, creativity, or child-appropriateness. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Guidelines Scorer

The `Guidelines` scorer from `mlflow.genai.scorers` lets you define a custom evaluation criterion by providing a natural language instruction. Each instance requires a `guidelines` string that describes the desired behavior and a `name` to identify the criterion in evaluation results. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

Typical uses include:

- Verifying that the response is in the same language as the input.
- Checking that the output is funny, creative, or follows a specific template structure.
- Ensuring content is appropriate for a target audience (e.g., child-safe). ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

Multiple `Guidelines` scorers can be composed in a single evaluation run, each producing a separate score.

## Safety Scorer

The `Safety` scorer from `mlflow.genai.scorers` is a built-in evaluator that checks for harmful or unsafe content in model outputs. It requires no configuration and can be added as a single instance to the scorer list. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Usage Example

In a typical evaluation workflow, both custom guidelines and the safety checker are assembled into a list and passed to `mlflow.genai.evaluate()`:

```python
from mlflow.genai.scorers import Guidelines, Safety

scorers = [
    Guidelines(guidelines="Response must be in the same language as the input", name="same_language"),
    Guidelines(guidelines="Response must be funny or creative", name="funny"),
    Guidelines(guidelines="Response must be appropriate for children", name="child_safe"),
    Guidelines(
        guidelines="Response must follow the input template structure...",
        name="template_match",
    ),
    Safety(),  # Built-in safety scorer
]

results = mlflow.genai.evaluate(
    data=eval_data,
    predict_fn=generate_game,
    scorers=scorers,
)
```

^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

Each scorer produces a numeric or categorical result visible in the MLflow UI alongside the model outputs.

## Related Concepts

- [GenAI evaluation](/concepts/mlflow-genai-evaluation.md) – The overarching process of assessing LLM-based applications.
- [Scorers and LLM Judges](/concepts/scorers-and-llm-judges.md) – Broader concept of evaluation functions in MLflow.
- MLflow GenAI framework – The toolkit that includes `mlflow.genai.evaluate`.
- [Inference Log Analysis](/concepts/inferencelog-analysis.md) – Monitoring approach that can surface score trends over time.

## Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
