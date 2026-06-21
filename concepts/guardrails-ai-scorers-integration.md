---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cf5a40b669d039337bed042047ee10c9c5d0e1d052288d1ad9070c7cab81497d
  pageDirectory: concepts
  sources:
    - third-party-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - guardrails-ai-scorers-integration
    - GASI
    - Guardrails AI Scorers
    - Guardrails AI documentation
  citations:
    - file: third-party-scorers-databricks-on-aws.md
title: Guardrails AI Scorers Integration
description: MLflow integration with Guardrails AI for rule-based output validation without LLM calls such as toxicity detection, PII scanning, and jailbreak detection
tags:
  - mlflow
  - guardrails
  - evaluation
  - safety
timestamp: "2026-06-19T23:07:16.455Z"
---

# Guardrails AI [[scorers|Scorers]] Integration

**Guardrails AI [[scorers|Scorers]] Integration** refers to the set of [MLflow Scorers](/concepts/mlflow-scorers.md) that wrap metrics from the [Guardrails AI](/concepts/guardrails-ai-framework.md) framework for use within `mlflow.genai.evaluate()`. These [[scorers|Scorers]] provide rule-based output validation that runs without LLM calls, offering a computationally efficient approach to content safety evaluation. ^[third-party-scorers-databricks-on-aws.md]

## Overview

Guardrails AI [[scorers|Scorers]] are one of several third-party scorer integrations available in [MLflow](/concepts/mlflow.md). They are particularly valuable when you need deterministic, rule-based validation metrics that do not require invoking a language model. ^[third-party-scorers-databricks-on-aws.md]

The integration is especially well-suited for tasks such as toxicity detection, PII scanning, jailbreak detection, secrets detection, and gibberish identification. These [[scorers|Scorers]] plug directly into `mlflow.genai.evaluate()`, enabling users to incorporate Guardrails AI's specialized metrics alongside [Built-in LLM Judges](/concepts/built-in-llm-judges.md) and [[scorers|Scorers]] from other frameworks. ^[third-party-scorers-databricks-on-aws.md]

## Use Cases

Guardrails AI [[scorers|Scorers]] are recommended when you need output validation that runs without LLM calls. This includes: ^[third-party-scorers-databricks-on-aws.md]

- Toxicity detection in generated content
- Personally Identifiable Information (PII) scanning
- Jailbreak detection in model inputs or outputs
- Secrets detection (e.g., API keys, passwords)
- Gibberish identification

## Getting Started

To use Guardrails AI [[scorers|Scorers]], import them from the `mlflow.genai.[[scorers|Scorers]].guardrails` module. Each scorer can be instantiated with configuration options such as a threshold value, then passed to `mlflow.genai.evaluate()` alongside other [[scorers|Scorers]]. ^[third-party-scorers-databricks-on-aws.md]

### Example: Using [ToxicLanguage Scorer](/concepts/toxiclanguage-scorer.md)

The following example combines a Guardrails AI scorer with a DeepEval scorer in a single evaluation call:

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

## When to Use Guardrails AI [[scorers|Scorers]]

Use Guardrails AI [[scorers|Scorers]] in the following situations: ^[third-party-scorers-databricks-on-aws.md]

- You need rule-based validators that run without LLM calls, such as PII detection or secrets scanning
- You need deterministic, non-LLM evaluation metrics like regex pattern matching
- You already use Guardrails AI in your workflows and want to take advantage of other [MLflow](/concepts/mlflow.md) features
- You need metrics for a specific domain that [Built-in LLM Judges](/concepts/built-in-llm-judges.md) don't cover

## Comparison with Other Third-Party [[scorers|Scorers]]

- [DeepEval scorers](/concepts/deepeval-scorer-api.md): Offer the broadest metric coverage across RAG, agents, conversational AI, and safety, but typically require LLM calls
- [RAGAS scorers](/concepts/ragas-scorers-in-mlflow.md): Focus on deep RAG evaluation with fine-grained context metrics and deterministic text comparison scores like BLEU and ROUGE
- [Arize Phoenix Scorers](/concepts/arize-phoenix-scorers.md): Provide a lightweight, focused set of [[scorers|Scorers]] for hallucination detection, relevance assessment, and toxicity identification
- [TruLens scorers](/concepts/trulens-scorers-integration.md): Focus on analyzing agent execution [Traces](/concepts/traces.md) with goal-plan-action alignment metrics
- Guardrails AI [[scorers|Scorers]]: Specialize in rule-based output validation that runs without LLM calls

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md)
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md)
- [Code-based Scorers](/concepts/code-based-scorers.md)
- Third-Party Scorer Integrations
- Content Safety Evaluation

## Sources

- third-party-scorers-databricks-on-aws.md

# Citations

1. [third-party-scorers-databricks-on-aws.md](/references/third-party-scorers-databricks-on-aws-3248b9c8.md)
