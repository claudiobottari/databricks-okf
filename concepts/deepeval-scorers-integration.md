---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bf8642f7d84e8b79372a34d12aa5753f09d5fd5b458e14fc42e7f6ecd6bc1056
  pageDirectory: concepts
  sources:
    - third-party-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deepeval-scorers-integration
    - DSI
  citations:
    - file: third-party-scorers-databricks-on-aws.md
title: DeepEval Scorers Integration
description: MLflow integration with DeepEval offering the broadest metric coverage across RAG, agents, conversational AI, and safety including agent plan quality and multi-turn conversation completeness
tags:
  - mlflow
  - deepeval
  - evaluation
  - third-party
timestamp: "2026-06-19T23:06:55.210Z"
---

---
title: DeepEval [[scorers|Scorers]] Integration
summary: [MLflow](/concepts/mlflow.md) integration with the [DeepEval Evaluation Framework](/concepts/deepeval-evaluation-framework.md), providing specialized [[scorers|Scorers]] for RAG, agents, conversational AI, and safety.
sources:
  - third-party-scorers-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T20:00:00.000Z"
updatedAt: "2026-06-19T20:00:00.000Z"
tags:
  - [MLflow](/concepts/mlflow.md)
  - evaluation
  - deepeval
  - third-party-scorers
aliases:
  - deepeval-scorers-integration
  - deepeval-scorers
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# DeepEval [[scorers|Scorers]] Integration

The **DeepEval [[scorers|Scorers]] Integration** allows you to use metrics from the [DeepEval](https://docs.confident-ai.com/) evaluation framework as [[Scorers]] in [MLflow](/concepts/mlflow.md). Through this integration, you can pass DeepEval-defined metrics directly into [`mlflow.genai.evaluate()`](https://[MLflow](/concepts/mlflow.md).org/docs/latest/api_reference/python_api/[MLflow](/concepts/mlflow.md).genai.html#mlflow.genai.evaluate) without leaving the [MLflow](/concepts/mlflow.md) evaluation pipeline. ^[third-party-scorers-databricks-on-aws.md]

## Overview

[MLflow](/concepts/mlflow.md) integrates with popular open-source evaluation frameworks so that you can use their specialized metrics as [[scorers|Scorers]] alongside [Built-in LLM Judges](/concepts/built-in-llm-judges.md) and [Custom (Code-Based) Scorers](/concepts/code-based-scorers.md). DeepEval is one of the supported third-party integrations. Its [[scorers|Scorers]] plug into the same unified `mlflow.genai.evaluate()` interface, giving you access to a broad library of evaluation metrics. ^[third-party-scorers-databricks-on-aws.md]

## Why Use DeepEval [[scorers|Scorers]]

DeepEval offers the broadest metric coverage across several domains: ^[third-party-scorers-databricks-on-aws.md]

- **[Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md)** – metrics for evaluating retrieval quality, context relevance, and answer faithfulness.
- **[Agent Evaluation](/concepts/mlflow-agent-evaluation.md)** – specialized [[scorers|Scorers]] for agent plan quality, step efficiency, multi-turn conversation completeness, and role adherence that other frameworks do not provide.
- **Conversational AI** – metrics designed for multi-turn dialogue.
- **Safety** – [Assessments](/concepts/assessments.md) for toxicity, hallucination, and other safety dimensions.

Because DeepEval includes metrics that [Built-in LLM Judges](/concepts/built-in-llm-judges.md) and other frameworks may lack, it is particularly useful when you need to evaluate agent behavior or conversation history. ^[third-party-scorers-databricks-on-aws.md]

## Key [[scorers|Scorers]]

The integration exposes DeepEval metrics as [MLflow Scorers](/concepts/mlflow-scorers.md), for example:

- `AnswerRelevancy` – measures how relevant the generated answer is to the given query.
- (Other [[scorers|Scorers]] are available; see the DeepEval documentation for the full list.)

To use a DeepEval scorer, import it from `mlflow.genai.[[scorers|Scorers]].deepeval` and pass it to `mlflow.genai.evaluate()`.

## Example

The following example uses the `AnswerRelevancy` scorer from DeepEval alongside a `ToxicLanguage` scorer from [Guardrails AI Scorers](/concepts/guardrails-ai-scorers-integration.md) in a single evaluation call: ^[third-party-scorers-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]
from [[mlflow|MLflow]].genai.[[scorers|Scorers]].deepeval import AnswerRelevancy
from [[mlflow|MLflow]].genai.[[scorers|Scorers]].guardrails import ToxicLanguage

eval_dataset = [
    {
        "inputs": {"query": "What is [[mlflow|MLflow]]?"},
        "outputs": "[[mlflow|MLflow]] is an open-source platform for managing ML and GenAI workloads.",
    },
]

results = [[mlflow|MLflow]].genai.evaluate(
    data=eval_dataset,
    scorers=[
        AnswerRelevancy(threshold=0.7, model="databricks:/databricks-gpt-5-mini"),
        ToxicLanguage(threshold=0.7),
    ],
)
```

## When to Use DeepEval vs. Built-in [[scorers|Scorers]]

Start with [Built-in LLM Judges](/concepts/built-in-llm-judges.md) for common evaluation needs like correctness, groundedness, and safety. Add DeepEval [[scorers|Scorers]] when: ^[third-party-scorers-databricks-on-aws.md]

- You already use DeepEval in your workflows and want to take advantage of other [MLflow](/concepts/mlflow.md) features.
- You need metrics for a specific domain that [Built-in Judges](/concepts/built-in-judges.md) do not cover, such as agent step efficiency or conversation completeness.
- You need deterministic, non-LLM evaluation metrics (DeepEval includes some deterministic [[scorers|Scorers]], though the integration primarily provides LLM-based judges).

## Related Concepts

- [Third-Party Scorers](/concepts/third-party-scorers-in-mlflow-genai.md) – Overview of all supported external evaluation frameworks.
- [RAGAS Scorers Integration](/concepts/ragas-scorers-integration.md) – Another third-party integration focused on RAG evaluation.
- [Arize Phoenix Scorers Integration](/concepts/arize-phoenix-scorers-integration.md) – Lightweight set of [[scorers|Scorers]] for hallucination and relevance.
- [TruLens Scorers Integration](/concepts/trulens-scorers-integration.md) – [[scorers|Scorers]] for analyzing agent execution [Traces](/concepts/traces.md).
- [Guardrails AI Scorers Integration](/concepts/guardrails-ai-scorers-integration.md) – Rule-based validators that run without LLM calls.
- Evaluation with MLflow – General concepts for evaluating GenAI applications.

## Sources

- third-party-scorers-databricks-on-aws.md

# Citations

1. [third-party-scorers-databricks-on-aws.md](/references/third-party-scorers-databricks-on-aws-3248b9c8.md)
