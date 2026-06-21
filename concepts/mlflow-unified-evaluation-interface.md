---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 46f662ea38f15e90309f77b643c51d30d6ded46661141fd7f29e550ea63e3551
  pageDirectory: concepts
  sources:
    - third-party-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-unified-evaluation-interface
    - MUEI
  citations:
    - file: third-party-scorers-databricks-on-aws.md
title: MLflow Unified Evaluation Interface
description: The ability to combine scorers from multiple third-party frameworks in a single mlflow.genai.evaluate() call with unified results visualization
tags:
  - mlflow
  - evaluation
  - workflow
timestamp: "2026-06-19T23:07:03.734Z"
---

# [MLflow](/concepts/mlflow.md) Unified Evaluation Interface

The **MLflow Unified Evaluation Interface** is a single, centralized API for evaluating generative AI models and applications. It allows users to combine [Built-in LLM Judges](/concepts/built-in-llm-judges.md), custom [Code-based Scorers](/concepts/code-based-scorers.md), and third-party evaluation frameworks in one `mlflow.genai.evaluate()` call, with all results displayed together in the [MLflow](/concepts/mlflow.md) UI. ^[third-party-scorers-databricks-on-aws.md]

## Overview

[MLflow](/concepts/mlflow.md) provides a unified interface through the [`mlflow.genai.evaluate()`](https://[MLflow](/concepts/mlflow.md).org/docs/latest/api_reference/python_api/[MLflow](/concepts/mlflow.md).genai.html#mlflow.genai.evaluate) function. This function accepts a list of scorers—each of which can be a built-in LLM judge, a user-defined scorer, or a scorer from an integrated third-party library. By combining multiple [[scorers|Scorers]] from different sources, teams can perform comprehensive evaluations without switching between tools. ^[third-party-scorers-databricks-on-aws.md]

The unified interface is the entry point for all generative AI evaluation on [MLflow](/concepts/mlflow.md). Results from every scorer (whether built-in or third-party) are automatically recorded and visualized together in the [MLflow](/concepts/mlflow.md) UI, providing a single pane of glass for comparing model outputs across many metrics. ^[third-party-scorers-databricks-on-aws.md]

## Key Features

- **Single API for multiple frameworks**: Pass [[scorers|Scorers]] from DeepEval, [RAGAS](/concepts/ragas-retrieval-augmented-generation-assessment.md), Arize Phoenix, TruLens, [Guardrails AI](/concepts/guardrails-ai-framework.md), or any combination thereof, into the same `mlflow.genai.evaluate()` call. ^[third-party-scorers-databricks-on-aws.md]
- **Combined evaluation**: Mix [Built-in LLM Judges](/concepts/built-in-llm-judges.md), [Code-based Scorers](/concepts/code-based-scorers.md), and [Third-party scorers](/concepts/third-party-scorers-in-mlflow-genai.md) in one [Evaluation Run](/concepts/evaluation-run.md). ^[third-party-scorers-databricks-on-aws.md]
- **Unified visualization**: All metric scores and detailed results appear together in the [MLflow](/concepts/mlflow.md) UI, regardless of which framework produced them. ^[third-party-scorers-databricks-on-aws.md]
- **Extensible architecture**: Framework-specific metrics are wrapped as [MLflow](/concepts/mlflow.md) scorer objects, making them first-class citizens in the evaluation pipeline. ^[third-party-scorers-databricks-on-aws.md]

## How It Works

Third-party evaluation frameworks (such as DeepEval or Guardrails AI) provide wrapper classes that expose their metrics as [MLflow Scorers](/concepts/mlflow-scorers.md). To use them, install the framework’s package, import the desired scorer, and include it in the `scorers` parameter of `mlflow.genai.evaluate()`. [MLflow](/concepts/mlflow.md) then orchestrates the evaluation, invoking each scorer on the provided [Evaluation Dataset](/concepts/evaluation-dataset.md). ^[third-party-scorers-databricks-on-aws.md]

## Example

The following example combines a relevancy scorer from DeepEval and a toxicity scorer from Guardrails AI in a single evaluation call:

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

^[third-party-scorers-databricks-on-aws.md]

## When to Use Built-in vs. Third-party [[scorers|Scorers]]

[MLflow](/concepts/mlflow.md) recommends starting with [Built-in LLM Judges](/concepts/built-in-llm-judges.md) for common evaluation needs such as correctness, groundedness, and safety. Add third-party [[scorers|Scorers]] through the unified interface in the following situations: ^[third-party-scorers-databricks-on-aws.md]

- You already use third-party frameworks in your workflows and want to leverage other [MLflow](/concepts/mlflow.md) features.
- You need domain-specific metrics that [Built-in Judges](/concepts/built-in-judges.md) do not cover (e.g., agent step efficiency, conversation completeness).
- You require deterministic evaluation metrics that do not rely on an LLM, such as BLEU scores, exact match, or regex pattern matching.
- You need rule-based validators that run without LLM calls, for example PII detection or secrets scanning.

## Related Concepts

- [mlflow.genai.evaluate()](/concepts/mlflowgenaievaluate.md)
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md)
- [Code-based Scorers](/concepts/code-based-scorers.md)
- [Third-party scorers](/concepts/third-party-scorers-in-mlflow-genai.md)
- [DeepEval scorers](/concepts/deepeval-scorer-api.md)
- [RAGAS scorers](/concepts/ragas-scorers-in-mlflow.md)
- [Arize Phoenix Scorers](/concepts/arize-phoenix-scorers.md)
- [TruLens scorers](/concepts/trulens-scorers-integration.md)
- Guardrails AI scorers

## Sources

- third-party-scorers-databricks-on-aws.md

# Citations

1. [third-party-scorers-databricks-on-aws.md](/references/third-party-scorers-databricks-on-aws-3248b9c8.md)
