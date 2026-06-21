---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 43e3a602c9a139d71df915cbad8bb44305b68d9591371b881fcb8271cc96e33a
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - configurable-judge-models
    - CJM
  citations:
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Configurable Judge Models
description: MLflow built-in judges can be backed by different LLMs specified in LiteLLM-compatible format, defaulting to a Databricks-hosted model
tags:
  - llm-judge
  - configuration
  - mlflow
timestamp: "2026-06-19T09:00:10.625Z"
---

# Configurable Judge Models

**Configurable Judge Models** refers to the ability to select which large language model (LLM) powers the built-in and custom judges used in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) evaluation. By changing the judge model, you can control the quality, cost, latency, and behavior of the scoring process. ^[answer-and-context-relevance-judges-databricks-on-aws.md, create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Overview

Judges are LLM-based scorers that evaluate outputs of GenAI applications against defined criteria. Both built-in judges and custom judges accept a `model` argument that specifies the underlying LLM. By default, built-in judges use a Databricks-hosted model, but you can override this to any LiteLLM-compatible model. ^[answer-and-context-relevance-judges-databricks-on-aws.md] Custom judges created with `make_judge()` also require a model specification, enabling you to tailor the evaluation to your use case. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Configuring Built-in Judges

Built-in judges such as `RelevanceToQuery` and `RetrievalRelevance` support a `model` parameter. The model must be specified in the format `<provider>:/<model-name>`. If the provider is `databricks`, the model name corresponds to a Databricks serving endpoint. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

```python
from mlflow.genai.scorers import RelevanceToQuery, RetrievalRelevance

# Use a different judge model
relevance_judge = RelevanceToQuery(
    model="databricks:/databricks-gpt-5-mini"
)
retrieval_judge = RetrievalRelevance(
    model="databricks:/databricks-claude-opus-4-5"
)
```

You can then pass these judges to `mlflow.genai.evaluate()`. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Configuring Custom Judges

Custom judges created with `make_judge()` also accept a `model` argument. This is required for [Trace-based Judges](/concepts/trace-based-judges.md), where the judge analyzes the execution trace. The model specification follows the same format. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
from mlflow.genai import make_judge

tool_call_judge = make_judge(
    name="tool_call_correctness",
    instructions=(
        "Analyze the execution {{ trace }} to determine if the agent "
        "called appropriate tools for the user's request."
    ),
    feedback_value_type=bool,
    model="databricks:/databricks-gpt-5-mini",   # Custom judge model
)
```

## Considerations

- **Default model**: Built-in judges default to a Databricks-hosted model designed for quality assessments. Override only when you need different behavior or want to use a model you already manage. ^[answer-and-context-relevance-judges-databricks-on-aws.md]
- **Model provider**: Any LiteLLM-compatible provider can be used (e.g., `openai`, `databricks`, `azure`). Changing the provider may require additional credentials or configuration. ^[answer-and-context-relevance-judges-databricks-on-aws.md]
- **Cost and latency**: Using a larger or private model may increase cost and latency. Test with a smaller model during development and use a more capable model for final validation.
- **Consistency in A/B comparisons**: When comparing [agent configurations](/concepts/ab-comparison-of-agent-configurations.md), use the same judge model across all variants to ensure differences in scores reflect changes in agent behavior, not judge model variations. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) – The set of pre‑defined judges (relevance, groundedness, safety, correctness).
- [Custom Judges](/concepts/custom-judges.md) – User‑defined scorers created with `make_judge()`.
- Judge Models – The underlying LLMs that power evaluation.
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) – Judges that analyze the full execution trace.

## Sources

- answer-and-context-relevance-judges-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
