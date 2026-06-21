---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b9e716a36ebf4cb9f74c3cc86161da2b049ff80b527ff0464223532cb5f44a90
  pageDirectory: concepts
  sources:
    - third-party-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - when-to-use-third-party-vs-built-in-scorers
    - WTUTVBS
  citations:
    - file: third-party-scorers-databricks-on-aws.md
title: When to Use Third-Party vs Built-in Scorers
description: Decision framework for choosing between built-in MLflow LLM judges and third-party scorers based on evaluation needs, domain specificity, and cost considerations
tags:
  - mlflow
  - evaluation
  - best-practices
timestamp: "2026-06-19T23:08:27.564Z"
---

# When to Use Third-Party vs Built-in [[scorers|Scorers]]

When evaluating generative AI and ML models in [MLflow](/concepts/mlflow.md), you have two main categories of [[scorers|Scorers]]: [Built-in LLM Judges](/concepts/built-in-llm-judges.md) and third-party [[scorers|Scorers]] from integrated evaluation frameworks. The choice between them depends on your specific evaluation needs, the metrics you require, and whether your team already uses a particular framework.

## Start with [Built-in Judges](/concepts/built-in-judges.md)

For common evaluation needs — such as correctness, groundedness, and safety — start with [Built-in LLM Judges](/concepts/built-in-llm-judges.md). These are provided by [MLflow](/concepts/mlflow.md) and cover the most frequent use cases without requiring additional package installations. ^[third-party-scorers-databricks-on-aws.md]

## When to add third-party [[scorers|Scorers]]

Add third-party [[scorers|Scorers]] when any of the following conditions apply:

### 1. You need specialized metrics not covered by [Built-in Judges](/concepts/built-in-judges.md)

Third-party frameworks offer metrics for domains that [Built-in Judges](/concepts/built-in-judges.md) do not cover. For example:

- [DeepEval scorers](/concepts/deepeval-scorer-api.md) provide metrics for agent plan quality, step efficiency, multi-turn conversation completeness, and role adherence.
- [RAGAS scorers](/concepts/ragas-scorers-in-mlflow.md) offer fine-grained context metrics (precision, recall, utilization, noise sensitivity) and deterministic text comparison scores like BLEU and ROUGE.
- [Arize Phoenix Scorers](/concepts/arize-phoenix-scorers.md) focus on hallucination detection, relevance assessment, toxicity identification, and QA correctness.
- [TruLens scorers](/concepts/trulens-scorers-integration.md) analyze agent execution [Traces](/concepts/traces.md) with goal-plan-action alignment metrics.
- Guardrails AI scorers provide rule-based output validation (toxicity detection, PII scanning, jailbreak detection, secrets detection) without LLM calls.

^[third-party-scorers-databricks-on-aws.md]

### 2. You already use these libraries in your workflows

If your team already relies on DeepEval, RAGAS, Phoenix, TruLens, or Guardrails AI for evaluation, you can integrate their [[scorers|Scorers]] directly into `mlflow.genai.evaluate()` without changing your workflow. This lets you take advantage of other [MLflow](/concepts/mlflow.md) features while using metrics you already trust. ^[third-party-scorers-databricks-on-aws.md]

### 3. You need deterministic, non-LLM evaluation metrics

Third-party [[scorers|Scorers]] provide metrics that do not require an LLM call, such as:

- BLEU scores
- Exact match
- Regex pattern matching
- Semantic similarity (without LLM)

These are useful when you want to avoid the cost, latency, or variability of LLM-based evaluation. ^[third-party-scorers-databricks-on-aws.md]

### 4. You need rule-based validators

For [Production Monitoring](/concepts/production-monitoring.md) and safety checks, rule-based validators like those in Guardrails AI can run without LLM calls, making them fast and cost-effective for tasks like PII detection, secrets scanning, or gibberish identification. ^[third-party-scorers-databricks-on-aws.md]

## Combined evaluation in a single call

Third-party [[scorers|Scorers]] integrate directly into `mlflow.genai.evaluate()`, allowing you to combine [[scorers|Scorers]] from multiple frameworks in a single evaluation call. Results are visualized together in the [MLflow](/concepts/mlflow.md) UI, giving you a unified view of metrics from different sources. ^[third-party-scorers-databricks-on-aws.md]

### Example

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

This example combines a DeepEval scorer (answer relevancy, which uses an LLM) with a Guardrails AI scorer (toxic language detection, which runs without LLM calls) in a single evaluation. ^[third-party-scorers-databricks-on-aws.md]

## Decision framework

| Need | Recommendation |
|------|----------------|
| Common metrics (correctness, groundedness, safety) | [Built-in LLM Judges](/concepts/built-in-llm-judges.md) |
| Specialized domain metrics (agent, RAG, safety) | Third-party [[scorers|Scorers]] |
| Already using a framework in your team | Third-party [[scorers|Scorers]] |
| Deterministic, non-LLM metrics | Third-party [[scorers|Scorers]] (e.g., RAGAS, Guardrails) |
| Rule-based validation without LLM calls | Third-party [[scorers|Scorers]] (e.g., Guardrails AI) |
| Combined evaluation across multiple frameworks | Third-party [[scorers|Scorers]] with `mlflow.genai.evaluate()` |

## Related concepts

- [Built-in LLM Judges](/concepts/built-in-llm-judges.md)
- [Code-based Scorers](/concepts/code-based-scorers.md)
- [Third-party scorers](/concepts/third-party-scorers-in-mlflow-genai.md)
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md)
- [DeepEval scorers](/concepts/deepeval-scorer-api.md)
- [RAGAS scorers](/concepts/ragas-scorers-in-mlflow.md)
- [Arize Phoenix Scorers](/concepts/arize-phoenix-scorers.md)
- [TruLens scorers](/concepts/trulens-scorers-integration.md)
- Guardrails AI scorers

## Sources

- third-party-scorers-databricks-on-aws.md

# Citations

1. [third-party-scorers-databricks-on-aws.md](/references/third-party-scorers-databricks-on-aws-3248b9c8.md)
