---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 57ca7c05871f178b53887ce882f2b5d5a05879ad854863a55841a894e28af618
  pageDirectory: concepts
  sources:
    - deepeval-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-deepeval-integration
  citations:
    - file: deepeval-scorers-databricks-on-aws.md
title: MLflow-DeepEval Integration
description: MLflow integrates DeepEval metrics as scorers for use with mlflow.genai.evaluate(), enabling standardized LLM evaluation within the MLflow ecosystem.
tags:
  - mlflow
  - integration
  - llm-evaluation
timestamp: "2026-06-19T09:59:04.439Z"
---

Here is the wiki page for "MLflow-DeepEval Integration".

---

## MLflow-DeepEval Integration

**MLflow-DeepEval Integration** allows you to use [DeepEval](https://docs.confident-ai.com/) metrics as plug-in scorers inside [MLflow GenAI](/concepts/mlflow-3-for-genai.md) evaluation workflows. DeepEval is a comprehensive evaluation framework for LLM applications, providing metrics for RAG systems, agents, conversational AI, and safety evaluation. By integrating DeepEval with MLflow, you can score model outputs with these ready-made metrics during offline evaluation or production monitoring. ^[deepeval-scorers-databricks-on-aws.md]

### Requirements

Install the `deepeval` Python package in your environment before using DeepEval scorers. ^[deepeval-scorers-databricks-on-aws.md]

```bash
pip install deepeval
```

### Quick Start

To call a DeepEval scorer directly on a single input-output pair: ^[deepeval-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.deepeval import AnswerRelevancy

scorer = AnswerRelevancy(threshold=0.7, model="databricks:/databricks-gpt-5-mini")
feedback = scorer(
    inputs="What is MLflow?",
    outputs="MLflow is an open-source AI engineering platform for agents and LLMs.",
)
print(feedback.value)        # "yes" or "no"
print(feedback.metadata["score"])  # 0.85
```

To use DeepEval scorers with `mlflow.genai.evaluate()`: ^[deepeval-scorers-databricks-on-aws.md]

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

### Available DeepEval Scorers

MLflow exposes the full set of DeepEval metrics as scorers. They are grouped into the following categories: ^[deepeval-scorers-databricks-on-aws.md]

- **RAG metrics** – Evaluate retrieval quality and answer generation in [Retrieval Augmented Generation](/concepts/retrieval-augmented-generation-rag.md) applications.
- **Agentic metrics** – Evaluate AI agent behavior, including task completion and tool usage.
- **Conversational metrics** – Evaluate multi-turn Conversational AI quality.
- **Safety metrics** – Evaluate the safety and responsibility of model outputs.
- **Other metrics** – Additional metrics covering various aspects of [LLM Evaluation](/concepts/llm-as-a-judge-evaluation.md).
- **Non-LLM metrics** – Metrics that do not rely on an LLM judge (e.g., statistical or rule-based scores).

### Create a Scorer by Name

You can dynamically create a DeepEval scorer by passing the metric name as a string to `get_scorer()`: ^[deepeval-scorers-databricks-on-aws.md]

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

### Configuration

DeepEval scorers accept metric-specific parameters as keyword arguments to their constructor. LLM-based metrics require a `model` parameter, and many support options such as `threshold`, `include_reason`, `window_size`, or `strict_mode`. ^[deepeval-scorers-databricks-on-aws.md]

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

For a complete list of metric-specific parameters and advanced usage, consult the [DeepEval documentation](https://docs.confident-ai.com/). ^[deepeval-scorers-databricks-on-aws.md]

### Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The MLflow API used to run scorers over evaluation datasets
- [Custom Judges](/concepts/custom-judges.md) – Alternative approach for defining LLM-based evaluators
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying scorers for continuous quality tracking

### Sources

- deepeval-scorers-databricks-on-aws.md

# Citations

1. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
