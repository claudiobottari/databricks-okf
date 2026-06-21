---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9fe5d607ecfa6883f3659d70130f674c882ee4d30f5dcebe127446bb1483491e
  pageDirectory: concepts
  sources:
    - tracing-claude-code-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-evaluation-with-llm-as-judge
    - MGEWL
    - Evaluation with LLM Judges
  citations:
    - file: tracing-claude-code-databricks-on-aws.md
title: MLflow GenAI Evaluation with LLM-as-Judge
description: Using MLflow's make_judge to create LLM-based evaluators that assess agent outputs for relevance and other criteria, integrated with tracing.
tags:
  - mlflow
  - evaluation
  - llm-judge
  - genai
timestamp: "2026-06-19T23:11:12.915Z"
---

# [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) with LLM-as-Judge

**MLflow GenAI Evaluation with LLM-as-Judge** is a methodology within the [MLflow](/concepts/mlflow.md) GenAI] ecosystem that leverages a large language model (LLM) as an automated evaluator to assess the quality, relevance, and safety of outputs produced by other generative AI systems. This approach replaces or augments traditional human evaluation by using an LLM "judge" to score responses against predefined criteria, enabling scalable and consistent evaluation of AI-generated content.

## Overview

The LLM-as-Judge pattern is central to [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md)]. It works by defining a judge—typically a capable LLM like [GPT-4o]—that receives a set of evaluation instructions and scores model outputs based on those criteria. The judge operates by comparing the model's response against the input context and the evaluation rubric, returning a structured assessment such as "pass" or "fail" or a numeric score. ^[tracing-claude-code-databricks-on-aws.md]

This technique is particularly valuable for evaluating [generative AI] systems where traditional metrics (e.g., accuracy, F1 score) are insufficient. Automated judges can assess [relevance], [coherence], [factuality], and other qualitative dimensions that are hard to measure with conventional statistical methods.

## Key Components

### Judge Definition

A judge is created using `make_judge()`, which takes a name, instructions (a prompt template with placeholders for inputs and outputs), and a model specification. For example:

```python
relevance = make_judge(
    name="relevance",
    instructions=(
        "Evaluate if the response in {{ outputs }} is relevant to "
        "the question in {{ inputs }}. Return either 'pass' or 'fail'."
    ),
    model="openai:/gpt-4o",
)
```

The placeholders `{{ inputs }}` and `{{ outputs }}` are automatically filled with the actual evaluation data at runtime. ^[tracing-claude-code-databricks-on-aws.md]

### [Evaluation Dataset](/concepts/evaluation-dataset.md)

An [Evaluation Dataset](/concepts/evaluation-dataset.md) is a [Pandas DataFrame] containing rows with an `inputs` column and an `outputs` column, or predictions are generated on the fly by a `predict_fn`. The data is structured as records, each with `inputs` keyed to a query field. ^[tracing-claude-code-databricks-on-aws.md]

```python
eval_data = pd.DataFrame(
    [
        {"inputs": {"query": "What is machine learning?"}},
        {"inputs": {"query": "Explain neural networks"}},
    ]
)
```

### Prediction Function

The `predict_fn` is a synchronous wrapper that calls the generative AI model (e.g., a Claude agent) and returns a string for each input query. It is passed to `evaluate()` along with the evaluation data and judges. ^[tracing-claude-code-databricks-on-aws.md]

```python
def predict_fn(query: str) -> str:
    return asyncio.run(run_agent(query))
```

## Running an Evaluation

Evaluation is executed by calling `mlflow.evaluate()` with the evaluation data, prediction function, and a list of judges ([[scorers|Scorers]]). The experiment is set using `mlflow.set_experiment()` to organize results under a specific [MLflow Experiment](/concepts/mlflow-experiment.md)] name. ^[tracing-claude-code-databricks-on-aws.md]

```python
[[mlflow|MLflow]].set_experiment("claude_evaluation")
evaluate(data=eval_data, predict_fn=predict_fn, scorers=[relevance])
```

## [Automatic Tracing](/concepts/automatic-tracing.md)

When [MLflow Anthropic Autolog](/concepts/mlflow-anthropic-autolog.md)] is enabled, [MLflow](/concepts/mlflow.md) automatically [Traces](/concepts/traces.md) the execution of the agent inside `predict_fn`, capturing the full interaction chain. This enables detailed [Traces](/concepts/traces.md)] of the evaluation flow, including how the judge processes each output. ^[tracing-claude-code-databricks-on-aws.md]

```python
[[mlflow|MLflow]].anthropic.autolog()
```

## Use Cases

LLM-as-Judge evaluation is suitable for a wide range of generative AI tasks:

- **Question Answering**: Assessing if the response is relevant to the question.
- **Summarization**: Checking for conciseness and completeness.
- **Safety**: Detecting harmful or inappropriate content.
- **Instruction Following**: Verifying that the model followed user directives.

## Related Concepts

- [MLflow](/concepts/mlflow.md) GenAI] — The broader [MLflow](/concepts/mlflow.md) ecosystem for generative AI evaluation and management.
- [LLM-as-Judge] — The general pattern of using an LLM as an evaluator.
- [MLflow](/concepts/mlflow.md) Evaluation] — The core evaluation framework within [MLflow](/concepts/mlflow.md).
- [Judges] — Prebuilt judge definitions for common evaluation tasks.
- [Traces](/concepts/traces.md)] — Execution [Traces](/concepts/traces.md) captured by [MLflow Autologging](/concepts/mlflow-autologging.md).

## Sources

- tracing-claude-code-databricks-on-aws.md

# Citations

1. [tracing-claude-code-databricks-on-aws.md](/references/tracing-claude-code-databricks-on-aws-cfc0e415.md)
