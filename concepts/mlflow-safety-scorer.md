---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7738138c4bb05cbac5e5e8174626bc53db2a125f6768ef38a37505ec419f608a
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-safety-scorer
    - MSS
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
title: MLflow Safety Scorer
description: Built-in MLflow scorer that evaluates LLM outputs for safety and harmful content, used as part of GenAI application evaluation.
tags:
  - mlflow
  - evaluation
  - safety
timestamp: "2026-06-19T13:49:40.604Z"
---

---
title: MLflow Safety Scorer
summary: A built-in safety scorer in MLflow that automatically evaluates GenAI outputs for harmful or unsafe content.
sources:
  - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:15:13.759Z"
updatedAt: "2026-06-18T14:15:13.759Z"
tags:
  - mlflow
  - safety
  - evaluation
aliases:
  - mlflow-safety-scorer
  - MSS
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# MLflow Safety Scorer

The **MLflow Safety Scorer** is a built-in scorer provided by `mlflow.genai.scorers` that automatically evaluates the outputs of a [GenAI](/concepts/mlflow-genai-evaluate-api.md) application for harmful, toxic, or otherwise unsafe content. It requires no user‑defined rubric or additional configuration. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Usage

To use the Safety Scorer, import `Safety` from `mlflow.genai.scorers` and include it in the list of scorers passed to `mlflow.genai.evaluate()`.

```python
from mlflow.genai.scorers import Safety

scorers = [
    Guidelines(...),
    Safety(),  # Built-in safety scorer
]
```

^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

When included alongside other scorers—such as [Guidelines Scorer](/concepts/guidelines-scorer.md)—the Safety Scorer assesses each model response for safety issues using built-in criteria. It can be used without specifying any additional parameters. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Evaluation Criteria

The Safety Scorer applies a pre‑defined set of safety criteria that are part of the [MLflow GenAI](/concepts/mlflow-3-for-genai.md) evaluation framework. These criteria are designed to flag content that may be harmful, offensive, or inappropriate. The exact rubric is determined by MLflow and is not configurable by the user. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Integration with MLflow Evaluation

The Safety Scorer is typically used as part of an evaluation run created with `mlflow.genai.evaluate()`. It can be combined with other built‑in scorers like `Guidelines` to cover multiple quality dimensions. Results are recorded in the MLflow Experiment UI, where scores per input can be reviewed and compared across runs. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The framework that provides the scoring infrastructure.
- [Scorers and LLM Judges](/concepts/scorers-and-llm-judges.md) – Overview of the scoring system.
- [Guidelines Scorer](/concepts/guidelines-scorer.md) – A user‑configurable scorer for application‑specific criteria.
- [Custom Judges](/concepts/custom-judges.md) – User‑defined judges for evaluation beyond built‑in scorers.
- [GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The offline evaluation workflow.

## Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
