---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8502c46bfdbaaf6f43d8f24037ff2670e7c72ecdacfbb43f38fb4386d1b5a81c
  pageDirectory: concepts
  sources:
    - built-in-llm-judges-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - ground-truth-in-llm-evaluation
    - GTILE
    - Ground Truth in GenAI Evaluation
    - Ground truth labels
  citations:
    - file: built-in-llm-judges-databricks-on-aws.md
title: Ground Truth in LLM Evaluation
description: A distinguishing feature of LLM judges where some judges require ground truth (expectations) to evaluate correctness or sufficiency, while others operate without it by evaluating based on inputs and outputs alone.
tags:
  - llm-evaluation
  - evaluation-methodology
  - mlflow
timestamp: "2026-06-19T17:42:31.447Z"
---

# Ground Truth in LLM Evaluation

**Ground truth** in LLM evaluation refers to the factual or expected answer for a given input in an evaluation dataset. It serves as a reference standard against which a model's outputs are compared to determine correctness, factual accuracy, or information coverage. In the MLflow evaluation framework, ground truth is typically provided through the `expectations` field of each evaluation record. ^[built-in-llm-judges-databricks-on-aws.md]

Not all evaluation judges require ground truth. Some judges assess inherent qualities of the output — such as relevance, safety, or groundedness — that do not depend on a pre‑defined answer. Other judges measure correctness or completeness and therefore need a reliable reference to compare against. ^[built-in-llm-judges-databricks-on-aws.md]

## Judges that require ground truth

The following built-in judges in MLflow explicitly require ground truth, passed via the `expectations` argument: ^[built-in-llm-judges-databricks-on-aws.md]

| Judge | Arguments | What it evaluates |
|-------|-----------|-------------------|
| [Correctness Judge](/concepts/correctness-judge.md) | `inputs`, `outputs`, `expectations` | Whether the response is correct when compared to the provided ground truth in `expectations`. |
| [RetrievalSufficiency Judge](/concepts/retrievalsufficiency-judge.md) | `inputs`, `outputs`, `expectations` | Whether the retrieved context contains all necessary information to generate a response that includes the ground‑truth facts. |
| ToolCallCorrectness judge | `inputs`, `outputs`, `expectations` | Whether the tool calls and arguments are correct for the user query. |

A fourth judge, [ExpectationsGuidelines](/concepts/expectationsguidelines-judge-per-row-guidelines.md), uses per‑example natural language guidelines that are placed in the `expectations` field, but it does not strictly require "ground truth" in the factual sense. Instead, it evaluates whether the response meets the given guidelines. ^[built-in-llm-judges-databricks-on-aws.md]

## Judges that do not require ground truth

Several judges evaluate outputs based solely on the input and output, without needing ground truth: ^[built-in-llm-judges-databricks-on-aws.md]

- **[RelevanceToQuery Judge](/concepts/relevancetoquery.md)** — Evaluates if the response is directly relevant to the user's request.
- **[RetrievalRelevance Judge](/concepts/retrievalrelevance.md)** — Evaluates if the retrieved context is directly relevant to the user's request.
- **[Safety judge](/concepts/safety-judge-mlflow.md)** — Evaluates if the content is free from harmful, offensive, or toxic material.
- **[RetrievalGroundedness judge](/concepts/retrievalgroundedness-judge.md)** — Evaluates if the response is grounded in the provided context.
- **[Guidelines judge](/concepts/guidelines-llm-judge.md)** — Evaluates if the response meets specified natural language criteria.
- **[ToolCallEfficiency judge](/concepts/tool-call-evaluation-judges.md)** — Evaluates if the tool calls are efficient without redundancy.

## How to provide ground truth

Ground truth is supplied as part of the evaluation dataset. When using `mlflow.genai.evaluate()`, each entry in the `data` argument can include an `expectations` field. The field contains the expected answer or facts that a judge such as `Correctness` or `RetrievalSufficiency` will reference. ^[built-in-llm-judges-databricks-on-aws.md]

Example structure for an evaluation record with ground truth:

```python
{
  "inputs": "What is the capital of France?",
  "outputs": "Paris",
  "expectations": "The capital of France is Paris."
}
```

## Why ground truth matters

- **Objective quality measurement.** Judges that require ground truth provide a factual check, reducing subjectivity in evaluation. ^[built-in-llm-judges-databricks-on-aws.md]
- **Regression detection.** Changes to an agent's prompt or model that degrade factual accuracy can be caught by comparing outputs to ground truth. ^[built-in-llm-judges-databricks-on-aws.md]
- **RAG pipeline validation.** The `RetrievalSufficiency` judge uses ground truth to determine whether the retrieval step has collected all necessary facts, helping to diagnose incomplete retrieval. ^[built-in-llm-judges-databricks-on-aws.md]
- **Tool call verification.** The `ToolCallCorrectness` judge uses ground truth to verify whether tool calls and their arguments match the expected behavior for a given user query. ^[built-in-llm-judges-databricks-on-aws.md]

## Multi-turn evaluation with ground truth

For conversational AI systems, [Multi-turn Judges](/concepts/multi-turn-judge.md) evaluate entire conversations rather than individual turns. These judges can also incorporate ground truth to assess quality patterns that emerge over multiple interactions, such as whether the assistant correctly maintained factual consistency across the dialogue. ^[built-in-llm-judges-databricks-on-aws.md]

## Related concepts

- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Predefined scorers that use Databricks‑hosted LLMs for evaluation.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) — The collection of inputs, outputs, and optional ground truth used in an evaluation run.
- [LLM evaluation](/concepts/llm-as-a-judge-evaluation.md) — The broader practice of assessing LLM output quality.
- [Custom LLM Judges](/concepts/custom-llm-judges.md) — User-defined judges for evaluation scenarios not covered by built-in options.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Comparing agent variants with the same set of judges and ground truth.
- [Production Monitoring](/concepts/production-monitoring.md) — Using ground truth judges to monitor deployed models in production.

## Sources

- built-in-llm-judges-databricks-on-aws.md

# Citations

1. [built-in-llm-judges-databricks-on-aws.md](/references/built-in-llm-judges-databricks-on-aws-15825704.md)
