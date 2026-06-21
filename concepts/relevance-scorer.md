---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 95aeb4dc06e3a81d9643d4cbf746d0af2279d35a4a17deaacac55895d4d396db
  pageDirectory: concepts
  sources:
    - arize-phoenix-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - relevance-scorer
  citations:
    - file: arize-phoenix-scorers-databricks-on-aws.md
title: Relevance Scorer
description: An Arize Phoenix scorer that measures how relevant an LLM's output is to the given query and context
tags:
  - llm-evaluation
  - relevance
timestamp: "2026-06-19T22:08:21.477Z"
---

```markdown
---
title: Relevance Scorer
summary: A scorer from the mlflow.genai.scorers.phoenix module used in MLflow GenAI evaluations.
sources:
  - arize-phoenix-scorers-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:48:28.596Z"
updatedAt: "2026-06-18T10:48:28.596Z"
tags:
  - llm-evaluation
  - scorer
  - relevance
aliases:
  - relevance-scorer
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Relevance Scorer

**Relevance Scorer** is a scorer available from the `mlflow.genai.scorers.phoenix` module. ^[arize-phoenix-scorers-databricks-on-aws.md]

## Usage

The Relevance Scorer is imported alongside the [[Hallucination Scorer]] from the `mlflow.genai.scorers.phoenix` module. It accepts a `model` parameter that specifies the LLM judge to use for scoring. ^[arize-phoenix-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.phoenix import Hallucination, Relevance

eval_dataset = [
    {
        "inputs": {"query": "What is MLflow?"},
        "outputs": "MLflow is an open-source AI engineering platform for agents and LLMs.",
        "expectations": {
            "context": "MLflow is an ML platform for experiment tracking and model deployment."
        },
    },
    {
        "inputs": {"query": "How do I track experiments?"},
        "outputs": "You can use mlflow.start_run() to begin tracking experiments.",
        "expectations": {
            "context": "MLflow provides APIs like mlflow.start_run() for experiment tracking."
        },
    },
]

results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[
        Hallucination(model="databricks:/databricks-gpt-5-mini"),
        Relevance(model="databricks:/databricks-gpt-5-mini"),
    ],
)
```

In the evaluation dataset, each entry includes `inputs` (with a `query` field), `outputs` (the response to evaluate), and `expectations` (with a `context` field). The list of scorers, including `Relevance`, is passed to `mlflow.genai.evaluate`. ^[arize-phoenix-scorers-databricks-on-aws.md]

## Related Concepts

- [[Hallucination Scorer]] — A complementary scorer imported from the same module.
- [[MLflow 3 for GenAI|MLflow GenAI]] — The evaluation framework that integrates Phoenix scorers.
- [[Evaluation Datasets]] — Structured data used for LLM output assessment.
- Arize Phoenix — The third‑party observability library that provides the Relevance Scorer.

## Sources

- arize-phoenix-scorers-databricks-on-aws.md
```

# Citations

1. [arize-phoenix-scorers-databricks-on-aws.md](/references/arize-phoenix-scorers-databricks-on-aws-53f4b817.md)
