---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1f9350a908c93dfaea7cef74f27d4dfc534bba7024c560fc6e577ac28546d6fe
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-judge-model-selection
    - CJMS
    - Model selection
  citations:
    - file: "answer-and-context-relevance-judges-databricks-on-aws.md: Select the LLM that powers the judge section"
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
title: Custom Judge Model Selection
description: The ability to override MLflow's default judge LLM with any LiteLLM-compatible model, specified using the format '<provider>:/<model-name>', enabling tailored evaluation.
tags:
  - llm-evaluation
  - mlflow
  - customization
timestamp: "2026-06-18T14:26:09.851Z"
---

## Custom Judge Model Selection

**Custom Judge Model Selection** refers to the process of choosing the LLM that powers a judge — either a built-in MLflow judge or a user-[custom judge](/concepts/custom-judges.md) — to evaluate GenAI application outputs. The model choice directly affects the judge’s scoring behavior, cost, and latency.

### Default Model

By default, built-in judges such as `RelevanceToQuery` and `RetrievalRelevance` use a Databricks-hosted LLM that is designed specifically for GenAI quality assessments. ^[answer-and-context-relevance-judges-databricks-on-aws.md: Select the LLM that powers the judge section]

### Overriding the Judge Model

You can change the judge model by passing the `model` argument when you create the judge. This applies to both built-in judges and judges created with `make_judge`. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. If you use `databricks` as the provider, the model name is the same as the serving endpoint name (e.g., `databricks:/databricks-gpt-5-mini`). ^[answer-and-context-relevance-judges-databricks-on-aws.md]

#### Example

```python
from mlflow.genai.scorers import RelevanceToQuery

# Use a Databricks-hosted model
relevance_judge = RelevanceToQuery(
    model="databricks:/databricks-gpt-5-mini"
)

# Use an external provider model (LiteLLM-compatible)
retrieval_judge = RetrievalRelevance(
    model="openai:/gpt-4o"
)

# Use in evaluation
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=my_app,
    scorers=[relevance_judge, retrieval_judge]
)
```

^[answer-and-context-relevance-judges-databricks-on-aws.md]

### Considerations for Custom Judge Model Selection

When building a [custom judge](/concepts/custom-judges.md) with `make_judge`, the `model` parameter must be provided (for trace-based judges it is required; for I/O judges it is optional and defaults to a Databricks-hosted model). Choose a model that is:

- **Capable enough** to reliably follow the judge instructions and produce accurate assessments.
- **Consistent** across evaluation runs; using the same model for A/B comparisons ensures differences reflect agent behavior, not judge variability.
- **Cost-effective** for your evaluation volume; larger models may be more accurate but incur higher inference costs.

### Related Concepts

- [Built-in Judges](/concepts/built-in-judges.md) — Predefined judges for relevance, groundedness, safety, and correctness
- make_judge()|Make Judge API — How to create a custom judge and specify its model
- LiteLLM — The model provider interface used by MLflow judges
- [Serving Endpoints](/concepts/serving-endpoint-acls.md) — When using `databricks` as provider, the model name is the endpoint name

### Sources

- answer-and-context-relevance-judges-databricks-on-aws.md

# Citations

1. answer-and-context-relevance-judges-databricks-on-aws.md: Select the LLM that powers the judge section
2. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
