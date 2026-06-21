---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6f7258cc877aeb8055153ff9629ddb0743f6d0ec495448b98e11f1bb95c2c62a
  pageDirectory: concepts
  sources:
    - arize-phoenix-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - arize-phoenix-scorers
    - APS
    - Phoenix scorers
  citations:
    - file: arize-phoenix-scorers-databricks-on-aws.md
title: Arize Phoenix Scorers
description: Built-in scorers from Arize Phoenix for evaluating LLM outputs, integrated with MLflow GenAI evaluation
tags:
  - llm-evaluation
  - mlflow
  - genai
timestamp: "2026-06-19T22:08:10.312Z"
---

```markdown
---
title: Arize Phoenix Scorers
summary: Pre-built evaluation scorers from Arize Phoenix integrated into MLflow GenAI for assessing LLM outputs, including Hallucination and Relevance detectors.
sources:
  - arize-phoenix-scorers-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:48:19.264Z"
updatedAt: "2026-06-19T14:03:38.432Z"
tags:
  - llm-evaluation
  - mlflow
  - arize-phoenix
aliases:
  - arize-phoenix-scorers
  - APS
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Arize Phoenix Scorers

**Arize Phoenix scorers** are built-in evaluation metrics from the Arize Phoenix open-source observability framework that plug directly into [[MLflow 3 for GenAI|MLflow GenAI]] evaluation. These scorers are designed for common LLM evaluation tasks, including hallucination detection and relevance assessment. Users import them from the `mlflow.genai.scorers.phoenix` module. ^[arize-phoenix-scorers-databricks-on-aws.md]

## Usage

Two primary scorers are available: `Hallucination` and `Relevance`. Each accepts a `model` parameter that specifies the endpoint for the evaluator language model, for example `databricks:/databricks-gpt-5-mini`. ^[arize-phoenix-scorers-databricks-on-aws.md]

The following example evaluates two input-output pairs by comparing each output against an expected context to measure hallucination and relevance:

```python
import mlflow
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

^[arize-phoenix-scorers-databricks-on-aws.md]

## Related Concepts

- [[MLflow GenAI Evaluation]] — The unified evaluation framework that hosts third-party scorers.
- [[Built-in LLM Judges]] — MLflow’s native evaluation metrics for common LLM tasks.
- [[Third-Party Scorers in MLflow GenAI|Third-Party Scorers]] — The broader category of evaluation integrations, including DeepEval, RAGAS, TruLens, and Guardrails AI.
- [[Code-Based Scorers]] — Custom Python-based scoring functions.

## Sources

- arize-phoenix-scorers-databricks-on-aws.md
```

# Citations

1. [arize-phoenix-scorers-databricks-on-aws.md](/references/arize-phoenix-scorers-databricks-on-aws-53f4b817.md)
