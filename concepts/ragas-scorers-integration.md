---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a752f9be1c36093359ba6f9b1254f521a6aac11cb06087c0109473c92cb5d6cd
  pageDirectory: concepts
  sources:
    - third-party-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ragas-scorers-integration
    - RSI
  citations:
    - file: third-party-scorers-databricks-on-aws.md
title: RAGAS Scorers Integration
description: MLflow integration with RAGAS providing deep RAG evaluation with fine-grained context metrics and deterministic text comparison scores like BLEU and ROUGE
tags:
  - mlflow
  - ragas
  - evaluation
  - rag
timestamp: "2026-06-19T23:06:58.935Z"
---

# RAGAS [[scorers|Scorers]] Integration

**RAGAS [[scorers|Scorers]] Integration** refers to the integration of the [RAGAS (Retrieval Augmented Generation Assessment)](/concepts/ragas-retrieval-augmented-generation-assessment.md) evaluation framework into [MLflow](/concepts/mlflow.md) as a set of third-party [[scorers|Scorers]]. These [[scorers|Scorers]] can be used directly with `mlflow.genai.evaluate()` through a unified interface, providing specialized metrics for evaluating [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) systems and other GenAI workloads. ^[third-party-scorers-databricks-on-aws.md]

## Overview

RAGAS [[scorers|Scorers]] are one of several third-party evaluation integrations available in [MLflow](/concepts/mlflow.md), alongside integrations with DeepEval, Arize Phoenix, TruLens, and [Guardrails AI](/concepts/guardrails-ai-framework.md). These integrations allow users to leverage specialized evaluation frameworks without changing their existing [MLflow](/concepts/mlflow.md) evaluation workflow. ^[third-party-scorers-databricks-on-aws.md]

## When to Use RAGAS [[scorers|Scorers]]

RAGAS [[scorers|Scorers]] are particularly useful in the following scenarios:

- **Deep RAG evaluation**: When you need fine-grained context metrics such as precision, recall, utilization, and noise sensitivity for RAG pipelines. ^[third-party-scorers-databricks-on-aws.md]
- **Agent goal accuracy**: For evaluating how well an agent achieves its intended goals. ^[third-party-scorers-databricks-on-aws.md]
- **Deterministic text comparison**: When you need metrics like BLEU, ROUGE, and semantic similarity scores that do not require LLM calls. ^[third-party-scorers-databricks-on-aws.md]

## Available Metrics

RAGAS provides a comprehensive set of evaluation metrics focused on RAG system performance. These include:

- **Context precision**: Measures how relevant the retrieved context is to the query.
- **Context recall**: Assesses whether all relevant information is retrieved.
- **Context utilization**: Evaluates how effectively the generated response uses the retrieved context.
- **Noise sensitivity**: Detects when the model is overly influenced by irrelevant context.
- **Agent goal accuracy**: Evaluates goal completion in agentic systems.
- **Deterministic scores**: BLEU, ROUGE, and semantic similarity metrics that run without LLM calls.

## Usage

To use RAGAS [[scorers|Scorers]], install the RAGAS package and import the desired scorer into your [MLflow](/concepts/mlflow.md) evaluation code. The scorer is then passed as part of the `scorers` list in `mlflow.genai.evaluate()`.

```python
import [[mlflow|MLflow]]
from [[mlflow|MLflow]].genai.[[scorers|Scorers]].ragas import RagasContextPrecision

eval_dataset = [
    {
        "inputs": {"query": "What is [[mlflow|MLflow]]?"},
        "outputs": "[[mlflow|MLflow]] is an open-source platform for managing ML and GenAI workloads.",
    },
]

results = [[mlflow|MLflow]].genai.evaluate(
    data=eval_dataset,
    scorers=[
        RagasContextPrecision(threshold=0.7),
    ],
)
```

RAGAS [[scorers|Scorers]] can be combined with [[scorers|Scorers]] from other frameworks — such as DeepEval or [Guardrails AI](/concepts/guardrails-ai-framework.md) — in a single `mlflow.genai.evaluate()` call, with results visualized together in the [MLflow UI](/concepts/mlflow.md).

## Comparison with Other [[scorers|Scorers]]

| Integration | Best For |
|---|---|
| **RAGAS** | Deep RAG evaluation with fine-grained context metrics, agent goal accuracy, and deterministic text comparison scores (BLEU, ROUGE, semantic similarity) |
| DeepEval | Broadest metric coverage across RAG, agents, conversational AI, and safety |
| Arize Phoenix | Lightweight, focused set of [[scorers|Scorers]] for hallucination detection and relevance assessment |
| TruLens | Agent execution trace analysis with goal-plan-action alignment metrics |
| [Guardrails AI](/concepts/guardrails-ai-framework.md) | Rule-based output validation without LLM calls |

^[third-party-scorers-databricks-on-aws.md]

## Integration with Built-in [[scorers|Scorers]]

Start with [Built-in LLM Judges](/concepts/built-in-llm-judges.md) for common evaluation needs like correctness, groundedness, and safety. Add RAGAS [[scorers|Scorers]] when you need:

- Metrics for a specific domain that [Built-in Judges](/concepts/built-in-judges.md) do not cover, such as context precision or noise sensitivity. ^[third-party-scorers-databricks-on-aws.md]
- Deterministic, non-LLM evaluation metrics like BLEU scores or exact match. ^[third-party-scorers-databricks-on-aws.md]
- Framework-specific strengths from libraries your team already uses, without changing your evaluation workflow. ^[third-party-scorers-databricks-on-aws.md]

## Related Concepts

- MLflow Evaluation Framework
- [Third-Party Scorers](/concepts/third-party-scorers-in-mlflow-genai.md)
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md)
- [Code-based Scorers](/concepts/code-based-scorers.md)
- RAG Evaluation

## Sources

- third-party-scorers-databricks-on-aws.md

# Citations

1. [third-party-scorers-databricks-on-aws.md](/references/third-party-scorers-databricks-on-aws-3248b9c8.md)
