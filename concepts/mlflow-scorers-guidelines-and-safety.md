---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7fb71edcd5c70c3bc4b893bea47290a663e6f72c95e4e66dc7a5cac8f043717f
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-scorers-guidelines-and-safety
    - Safety) and MLflow Scorers (Guidelines
    - MS(AS
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
title: MLflow Scorers (Guidelines and Safety)
description: Built-in evaluation criteria in MLflow for assessing GenAI outputs, including Guidelines scorer for custom rules and Safety scorer for content safety checks.
tags:
  - llm-evaluation
  - mlflow
  - scorers
timestamp: "2026-06-19T17:22:45.546Z"
---

## MLflow Scorers (Guidelines and Safety)

**MLflow Scorers (Guidelines and Safety)** are built-in evaluation criteria that measure specific qualities of a GenAI application’s output. They are part of the [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) framework and allow developers to define custom guidelines or use a pre‑built safety scorer without writing separate judge logic. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Guidelines scorer

The `Guidelines` scorer evaluates whether a response adheres to one or more natural‑language rules. It is instantiated with a `guidelines` string that describes the desired property and an optional `name` for identification in evaluation results. For example:

```python
from mlflow.genai.scorers import Guidelines

scorer = Guidelines(
    guidelines="Response must be funny or creative",
    name="funny"
)
```

Multiple `Guidelines` scorers can be combined in a list to assess different aspects of the output (e.g., language matching, child safety, template adherence). ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Safety scorer

The `Safety` scorer is a built‑in scorer that evaluates whether the generated content is safe and appropriate. It requires no additional configuration and can be instantiated simply as `Safety()`. This scorer is typically used alongside custom guidelines to ensure the application produces family‑friendly or policy‑compliant responses. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Usage in evaluation

Both scorers are passed to the `mlflow.genai.evaluate()` function via the `scorers` parameter. The function applies each scorer to every example in the evaluation dataset, producing scores that can be reviewed in the MLflow UI. The following snippet shows how to define and use a set of scorers:

```python
from mlflow.genai.scorers import Guidelines, Safety
import mlflow.genai

scorers = [
    Guidelines(guidelines="Response must be in the same language as the input", name="same_language"),
    Guidelines(guidelines="Response must be funny or creative", name="funny"),
    Guidelines(guidelines="Response must be appropriate for children", name="child_safe"),
    Guidelines(guidelines="Response must follow the input template structure", name="template_match"),
    Safety(),
]

results = mlflow.genai.evaluate(
    data=eval_data,
    predict_fn=generate_game,
    scorers=scorers
)
```

The evaluation results include per‑scorer scores that help identify areas for improvement. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Related concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The overall framework for evaluating GenAI applications.
- [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) – The methodology behind automated scoring using large language models.
- [GenAI Application Evaluation](/concepts/genai-application-evaluation-lifecycle.md) – End‑to‑end workflow for assessing generative AI outputs.
- Prompt Engineering – Iterative improvement informed by scorer feedback.

### Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
