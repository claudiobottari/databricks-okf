---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 28cadb5fdfcd99cc724c6468891f7b9f283a0268c8addecf3b12b4996fb88402
  pageDirectory: concepts
  sources:
    - deepeval-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deepeval-mlflow-integration
  citations:
    - file: deepeval-scorers-databricks-on-aws.md
title: DeepEval-MLflow Integration
description: MLflow natively integrates DeepEval scorers for evaluating LLM applications within the MLflow evaluation framework.
tags:
  - mlflow
  - llm-evaluation
  - integration
timestamp: "2026-06-19T14:58:31.968Z"
---

Here is the wiki page for "DeepEval-MLflow Integration", written based solely on the provided source material.

---

## DeepEval-MLflow Integration

The **DeepEval-MLflow Integration** allows users to apply metrics from the DeepEval evaluation framework directly within MLflow as scorers. This enables the evaluation of [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) systems, AI Agent behavior, conversational AI quality, and model safety as part of MLflow's evaluation workflows. ^[deepeval-scorers-databricks-on-aws.md]

### Requirements

To use DeepEval scorers, the `deepeval` package must be installed in the environment. ^[deepeval-scorers-databricks-on-aws.md]

### Quick Start

DeepEval scorers can be called directly to get feedback on a single input-output pair. The scorer returns a `feedback` object containing a pass/fail `value` and a `metadata` dictionary that includes the numerical `score`. ^[deepeval-scorers-databricks-on-aws.md]

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

For batch evaluation, scorers can be passed to `mlflow.genai.evaluate()` to score an entire evaluation dataset. ^[deepeval-scorers-databricks-on-aws.md]

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

The integration provides access to several categories of DeepEval metrics:

- **RAG Metrics** — Evaluate retrieval quality and answer generation in retrieval-augmented generation (RAG) applications.
- **Agentic Metrics** — Evaluate AI agent behavior, including task completion and tool usage.
- **Conversational Metrics** — Evaluate multi-turn conversational AI quality.
- **Safety Metrics** — Evaluate the safety and responsibility of model outputs.
- **Other Metrics** — Additional general-purpose evaluation metrics.
- **Non-LLM Metrics** — Metrics that do not require an LLM for scoring.

^[deepeval-scorers-databricks-on-aws.md]

### Creating a Scorer by Name

Scorers can be created dynamically using `get_scorer()` by passing the metric name as a string. This allows for programmatic construction of evaluation metrics. ^[deepeval-scorers-databricks-on-aws.md]

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

DeepEval scorers accept metric-specific parameters as keyword arguments to their constructor. LLM-based metrics require a `model` parameter specifying the underlying language model to use for evaluation. Common parameters include `threshold` and `include_reason`. Some metrics accept additional metric-specific parameters such as `window_size` and `strict_mode`. ^[deepeval-scorers-databricks-on-aws.md]

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

For metric-specific parameters and advanced usage options, refer to the DeepEval documentation. ^[deepeval-scorers-databricks-on-aws.md]

### Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The broader MLflow framework for model evaluation and scoring.
- RAG Evaluation — Evaluation strategies specifically for retrieval-augmented generation systems.
- [LLM Evaluation Metrics](/concepts/llm-as-a-judge-evaluation-metrics.md) — Other metrics and frameworks available for evaluating large language models.
- Databricks-GPT — The model serving endpoint used as the evaluation model in the examples.

### Sources

- deepeval-scorers-databricks-on-aws.md

# Citations

1. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
