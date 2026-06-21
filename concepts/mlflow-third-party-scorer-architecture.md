---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3e76ba6f5b7271a77ebe27617dfab2c47f22dd7aa3d87ee08843649c9c8af20a
  pageDirectory: concepts
  sources:
    - third-party-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-third-party-scorer-architecture
    - MTSA
  citations:
    - file: third-party-scorers-databricks-on-aws.md
title: MLflow Third-Party Scorer Architecture
description: MLflow's integration layer that wraps evaluation metrics from third-party frameworks as MLflow scorers usable with mlflow.genai.evaluate()
tags:
  - mlflow
  - evaluation
  - architecture
timestamp: "2026-06-19T23:06:57.601Z"
---

# [MLflow](/concepts/mlflow.md) Third-Party Scorer Architecture

**MLflow Third-Party Scorer Architecture** describes how [MLflow](/concepts/mlflow.md) integrates with popular open-source evaluation frameworks to allow their specialized metrics to be used as [[scorers|Scorers]] alongside [Built-in LLM Judges](/concepts/built-in-llm-judges.md) and [custom code-based scorers](/concepts/code-based-scorers.md). Third-party [[scorers|Scorers]] plug directly into `mlflow.genai.evaluate()` through a unified wrapper interface, giving users access to a broad library of evaluation metrics without leaving the [MLflow](/concepts/mlflow.md) ecosystem. ^[third-party-scorers-databricks-on-aws.md]

## Overview

[MLflow](/concepts/mlflow.md) provides a set of [Built-in LLM Judges](/concepts/built-in-llm-judges.md) for common evaluation needs such as correctness, groundedness, and safety. However, when specialized metrics are required—for example, agent plan quality, jailbreak detection, or BLEU/ROUGE text comparison scores—the platform allows users to bring in external evaluation frameworks. Each integration wraps the third-party framework’s metrics as [MLflow Scorers](/concepts/mlflow-scorers.md) that are compatible with `mlflow.genai.evaluate()`. This design preserves a consistent evaluation workflow while enabling access to domain-specific strengths. ^[third-party-scorers-databricks-on-aws.md]

## Architecture

The architecture follows a wrapper pattern:

1. **Library installation** – The third-party framework’s package is installed in the Python environment.
2. **Scorer import** – [MLflow](/concepts/mlflow.md) provides scorer classes (e.g., `AnswerRelevancy`, `ToxicLanguage`) that internally call the framework’s functions.
3. **Unified evaluation** – These scorer objects are passed in a list to `mlflow.genai.evaluate()`. [MLflow](/concepts/mlflow.md) orchestrates their execution alongside other [[scorers|Scorers]] and aggregates results in the [MLflow](/concepts/mlflow.md) UI.

This design allows multiple frameworks to be combined in a single evaluation call, with results visualized together. ^[third-party-scorers-databricks-on-aws.md]

## Available Integrations

[MLflow](/concepts/mlflow.md) currently supports five third-party frameworks. Each integration targets specific evaluation domains:

| Integration | When to use |
|-------------|------------|
| DeepEval | Broadest metric coverage across RAG, agents, conversational AI, and safety. Offers specialized [[scorers|Scorers]] for agent plan quality, step efficiency, multi-turn conversation completeness, and role adherence. |
| [RAGAS](/concepts/ragas-retrieval-augmented-generation-assessment.md) | Deep RAG evaluation with fine-grained context metrics (precision, recall, utilization, noise sensitivity), agent goal accuracy, and deterministic text comparison (BLEU, ROUGE, semantic similarity) without LLM calls. |
| Arize Phoenix | Lightweight, focused set of [[scorers|Scorers]] for hallucination detection, relevance assessment, toxicity identification, QA correctness, and summarization quality. |
| TruLens | Analysis of agent execution [Traces](/concepts/traces.md) with goal-plan-action alignment metrics like logical consistency, execution efficiency, plan adherence, and tool selection. |
| [Guardrails AI](/concepts/guardrails-ai-framework.md) | Rule-based output validation that runs without LLM calls: toxicity detection, PII scanning, jailbreak detection, secrets detection, gibberish identification. |

^[third-party-scorers-databricks-on-aws.md]

## Usage Example

The following example combines a DeepEval scorer and a Guardrails AI scorer in a single `mlflow.genai.evaluate()` call:

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

Each third-party scorer is instantiated with a threshold and any required model reference, then passed as a list item. [MLflow](/concepts/mlflow.md) runs them as part of the evaluation job. ^[third-party-scorers-databricks-on-aws.md]

## When to Use Third-Party vs. Built-in [[scorers|Scorers]]

Start with [Built-in LLM Judges](/concepts/built-in-llm-judges.md) for common evaluation needs. Add third-party [[scorers|Scorers]] in these situations:

- You already use the third-party libraries in your workflows and want to combine them with other [MLflow](/concepts/mlflow.md) features.
- You need metrics for a specific domain that [Built-in Judges](/concepts/built-in-judges.md) do not cover (e.g., agent step efficiency, conversation completeness).
- You need deterministic, non-LLM evaluation metrics (e.g., BLEU scores, exact match, regex pattern matching).
- You need rule-based validators that run without LLM calls (e.g., PII detection, secrets scanning).

^[third-party-scorers-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) – The platform that provides the evaluation framework.
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) – Pre-built [[scorers|Scorers]] for common GenAI evaluation.
- [Custom Scorers](/concepts/custom-scorers-mlflow-genai.md) – User-defined [Code-based Scorers](/concepts/code-based-scorers.md).
- [mlflow.genai.evaluate()](/concepts/mlflowgenaievaluate.md) – The unified evaluation function.
- RAG Evaluation – Common use case for third-party [[scorers|Scorers]].
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) – Domain where specialized [[scorers|Scorers]] like DeepEval and TruLens excel.

## Sources

- third-party-scorers-databricks-on-aws.md

# Citations

1. [third-party-scorers-databricks-on-aws.md](/references/third-party-scorers-databricks-on-aws-3248b9c8.md)
