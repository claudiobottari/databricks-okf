---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3b98bb499a9411568df5ecf9f3edbc39229da9570171a609629919645de76b0a
  pageDirectory: concepts
  sources:
    - deepeval-scorers-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deepeval-metric-categories
    - DMC
  citations:
    - file: deepeval-scorers-databricks-on-aws.md
title: DeepEval Metric Categories
description: "DeepEval provides five categories of metrics: RAG metrics, Agentic metrics, Conversational metrics, Safety metrics, and Non-LLM metrics."
tags:
  - metrics
  - categorization
  - llm-evaluation
timestamp: "2026-06-18T11:47:55.089Z"
---

I'll write the wiki page for "DeepEval Metric Categories" based on the source material provided.

---

---
title: DeepEval Metric Categories
summary: An overview of the metric categories available in DeepEval for evaluating LLM applications, including RAG, agentic, conversational, safety, and other metrics.
sources:
  - deepeval-scorers-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:15:33.969Z"
updatedAt: "2026-06-18T08:15:33.969Z"
tags:
  - mlflow
  - deepeval
  - evaluation
  - LLM
  - genai
aliases:
  - deepeval-metric-categories
  - DMC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# DeepEval Metric Categories

**DeepEval** is a comprehensive evaluation framework for LLM applications that provides metrics organized into several categories: RAG systems, agents, conversational AI, safety evaluation, and additional general-purpose or non-LLM metrics. MLflow integrates with DeepEval so that you can use DeepEval metrics as scorers in [MLflow](/concepts/mlflow.md) evaluation workflows. ^[deepeval-scorers-databricks-on-aws.md]

## Available Metric Categories

DeepEval offers the following metric categories for evaluating different aspects of LLM application quality:

### RAG Metrics

These scorers evaluate retrieval quality and answer generation in [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications. They assess how well the system retrieves relevant context and generates responses based on that context. ^[deepeval-scorers-databricks-on-aws.md]

### Agentic Metrics

These scorers evaluate AI agent behavior, including task completion and tool usage. They assess whether agents correctly execute tasks, use appropriate tools, and follow intended workflows. ^[deepeval-scorers-databricks-on-aws.md]

### Conversational Metrics

These scorers evaluate multi-turn [conversational AI](/concepts/conversation-evaluation.md) quality. They assess how well the system maintains context across turns, responds appropriately to user inputs, and manages dialogue coherence. ^[deepeval-scorers-databricks-on-aws.md]

### Safety Metrics

These scorers evaluate the safety and responsibility of model outputs. They assess whether outputs contain harmful content, violate policies, or pose risks to users. ^[deepeval-scorers-databricks-on-aws.md]

### Other Metrics

General-purpose metrics for evaluating aspects not covered by the specialized categories above. ^[deepeval-scorers-databricks-on-aws.md]

### Non-LLM Metrics

These metrics evaluate aspects of application quality that do not require an LLM judge, such as computational efficiency or rule-based checks. ^[deepeval-scorers-databricks-on-aws.md]

## Using DeepEval Scorers in MLflow

DeepEval scorers can be used directly as standalone evaluators or composed into [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) workflows via `mlflow.genai.evaluate()`. ^[deepeval-scorers-databricks-on-aws.md]

### Direct Scorer Invocation

To call a DeepEval scorer directly:

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

^[deepeval-scorers-databricks-on-aws.md]

### Evaluation with Multiple Scorers

To call DeepEval scorers using `mlflow.genai.evaluate()`:

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

^[deepeval-scorers-databricks-on-aws.md]

### Creating a Scorer by Name

You can dynamically create a scorer using `get_scorer` by passing the metric name as a string:

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

^[deepeval-scorers-databricks-on-aws.md]

## Configuration

DeepEval scorers accept metric-specific parameters as keyword arguments to the constructor. LLM-based metrics require a `model` parameter. For metric-specific parameters and advanced usage options, see the DeepEval documentation. ^[deepeval-scorers-databricks-on-aws.md]

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

## Requirements

Install the `deepeval` package to use DeepEval scorers with MLflow. ^[deepeval-scorers-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — MLflow's GenAI evaluation framework for LLM applications
- [Custom Judges](/concepts/custom-judges.md) — Creating custom LLM-based evaluators in MLflow
- RAG Evaluation — Evaluating retrieval-augmented generation quality
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluating AI agent behavior and tool usage
- [Conversational AI Evaluation](/concepts/conversation-evaluation.md) — Evaluating multi-turn dialogue quality
- Safety Evaluation — Evaluating model output safety and responsibility

## Sources

- deepeval-scorers-databricks-on-aws.md

# Citations

1. [deepeval-scorers-databricks-on-aws.md](/references/deepeval-scorers-databricks-on-aws-95eb5ac0.md)
