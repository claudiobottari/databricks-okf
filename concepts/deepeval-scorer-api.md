---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 270951227338aa5d64b19b551bd15175e5e8a88cb8f2d81055e0857edb7eddbd
  pageDirectory: concepts
  sources:
    - deepeval-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deepeval-scorer-api
    - DSA
    - DeepEval Scorers
    - DeepEval scorer
    - DeepEval scorers
  citations:
    - file: deepeval-scorers-databricks-on-aws.md
title: DeepEval Scorer API
description: Python API for invoking DeepEval scorers directly or via mlflow.genai.evaluate(), with threshold, model and metric-specific parameters
tags:
  - api
  - python
  - evaluation
  - scoring
timestamp: "2026-06-18T15:14:06.281Z"
---

Here is the wiki page for "DeepEval Scorer API", written based solely on the provided source material.

---

## DeepEval Scorer API

The **DeepEval Scorer API** is an integration within [MLflow](/concepts/mlflow.md) that allows users to leverage the [DeepEval](https://docs.confident-ai.com/) evaluation framework as built-in scorers for LLM applications. DeepEval provides a comprehensive set of metrics for RAG systems, agents, conversational AI, and safety evaluation. Through this API, these metrics can be used directly or within the `mlflow.genai.evaluate()` function. ^[deepeval-scorers-databricks-on-aws.md]

### Requirements

To use the DeepEval Scorer API, the `deepeval` Python package must be installed. ^[deepeval-scorers-databricks-on-aws.md]

### Quickstart

DeepEval scorers can be invoked directly by instantiating a scorer class and calling it with the appropriate inputs and outputs. The scorer returns a feedback object containing a value (e.g., "yes" or "no") and a metadata dictionary with the underlying score. ^[deepeval-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.deepeval import AnswerRelevancy

scorer = AnswerRelevancy(threshold=0.7, model="databricks:/databricks-gpt-5-mini")
feedback = scorer(
    inputs="What is MLflow?",
    outputs="MLflow is an open-source AI engineering platform for agents and LLMs.",
)
print(feedback.value)  # "yes" or "no"
print(feedback.metadata["score"])  # 0.85
```

Scorers can also be used with `mlflow.genai.evaluate()` by passing them in the `scorers` list along with an evaluation dataset. ^[deepeval-scorers-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.scorers.deepeval import AnswerRelevancy, Faithfulness

eval_dataset = [
    {
        "inputs": {"query": "What is MLflow?"},
        "outputs": "MLflow is an open-source AI engineering platform for agents and LLMs.",
    },
    {
        "inputs": {"query": "How do I track experiments?"},
        "outputs": "You can use mlflow.start_run() to begin tracking experiments.",
    },
]

results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[
        AnswerRelevancy(threshold=0.7, model="databricks:/databricks-gpt-5-mini"),
        Faithfulness(threshold=0.8, model="databricks:/databricks-gpt-5-mini"),
    ],
)
```

### Creating a Scorer by Name

Scorers can be created dynamically by passing the metric name as a string to the `get_scorer` function. This enables programmatic selection of metrics. ^[deepeval-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.deepeval import get_scorer

scorer = get_scorer(
    metric_name="AnswerRelevancy",
    threshold=0.7,
    model="databricks:/databricks-gpt-5-mini",
)
feedback = scorer(
    inputs="What is MLflow?",
    outputs="MLflow is a platform for ML workflows.",
)
```

### Available Scorers

DeepEval provides several categories of metrics through the API. The exact list of available scorer classes within each category is determined by the DeepEval library.

| Category | Description |
|----------|-------------|
| **RAG Metrics** | Evaluate retrieval quality and answer generation in [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications |
| **Agentic Metrics** | Evaluate AI agent behavior, including task completion and tool usage |
| **Conversational Metrics** | Evaluate multi-turn conversational AI quality |
| **Safety Metrics** | Evaluate the safety and responsibility of model outputs |
| **Other Metrics** | Additional evaluation metrics |
| **Non-LLM Metrics** | Metrics that do not require an LLM judge |

### Configuration

DeepEval scorers accept metric-specific parameters as keyword arguments to the constructor. [LLM-based metrics](/concepts/llm-as-a-judge-evaluation-metrics.md) require a `model` parameter. For metric-specific parameters and advanced usage options, refer to the [DeepEval documentation](https://docs.confident-ai.com/). ^[deepeval-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.deepeval import AnswerRelevancy, TurnRelevancy

# LLM-based metric with common parameters
scorer = AnswerRelevancy(
    model="databricks:/databricks-gpt-5-mini",
    threshold=0.7,
    include_reason=True,
)

# Metric-specific parameters
conversational_scorer = TurnRelevancy(
    model="openai:/gpt-4o",
    threshold=0.8,
    window_size=3,
    strict_mode=True,
)
```

### Related Concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The MLflow framework for LLM evaluation and monitoring
- [DeepEval Framework](/concepts/deepeval-framework.md) — The underlying third-party evaluation library
- [Custom Judges](/concepts/custom-judges.md) — Alternative approach for creating custom LLM-based scorers
- RAG Evaluation — Evaluating retrieval-augmented generation systems
- Safety Evaluation — Assessing content safety of model outputs

### Sources

- deepeval-scorers-databricks-on-aws.md

# Citations

1. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
