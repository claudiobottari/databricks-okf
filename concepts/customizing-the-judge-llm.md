---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5f0a3fbd9ce8abdf0f879b1393a713a893e1b011b6e0f4dec6efee791f593563
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - customizing-the-judge-llm
    - CTJL
  citations:
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
title: Customizing the Judge LLM
description: The ability to override the default Databricks-hosted LLM that powers built-in MLflow judges by specifying a different model via the 'model' argument in a provider:/model-name format.
tags:
  - llm-evaluation
  - mlflow
  - configuration
  - genai
timestamp: "2026-06-18T10:46:22.192Z"
---

# Customizing the Judge LLM

Built‑in [MLflow](/concepts/mlflow.md) LLM judges such as `RelevanceToQuery` and `RetrievalRelevance` can be configured to use a different underlying LLM instead of the default Databricks‑hosted model. This allows you to select a judge model that fits your accuracy requirements, latency budget, or compliance policies.^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Default Judge Model

By default, the built‑in judges use a Databricks‑hosted LLM that is specifically designed for evaluating generative AI quality (for example, answering relevance, groundedness, or safety). You do not need to specify any model when you create a judge—the default is applied automatically.^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Specifying a Custom Judge Model

To override the default, set the `model` argument when you instantiate the judge. The model identifier must follow the format `<provider>:/<model-name>`, where:

- `<provider>` is any LiteLLM‑compatible model provider (e.g., `databricks`, `openai`, `azure`, `anthropic`).
- For the `databricks` provider, the `<model-name>` is the name of a serving endpoint in your Databricks workspace (for example, `databricks-gpt-5-mini` or `databricks-claude-opus-4-5`).

The same pattern works for any provider that LiteLLM supports.^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Example

```python
from mlflow.genai.scorers import RelevanceToQuery, RetrievalRelevance

# Use a different Databricks serving endpoint
relevance_judge = RelevanceToQuery(
    model="databricks:/databricks-gpt-5-mini"
)

# Use a Claude model hosted on Databricks
retrieval_judge = RetrievalRelevance(
    model="databricks:/databricks-claude-opus-4-5"
)

# Pass to evaluation
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=rag_app,
    scorers=[relevance_judge, retrieval_judge]
)
```

^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Judge Output Format

Every judge returns a `Feedback` object with two fields:

| Field | Description |
|-------|-------------|
| `value` | `"yes"` if the assessment criterion is met, `"no"` otherwise. |
| `rationale` | A natural‑language explanation of why the judge assigned that value. |

You can inspect this object directly or use it in downstream analysis.^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Related Concepts

- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) – the family of pre‑configured judges (relevance, groundedness, safety, correctness)
- [RelevanceToQuery](/concepts/relevancetoquery.md) – evaluates if the response directly addresses the user input
- [RetrievalRelevance](/concepts/retrievalrelevance.md) – evaluates if each retrieved document is relevant to the query
- [MLflow](/concepts/mlflow.md) – the platform that provides these judges and the evaluation framework
- LiteLLM – the model routing layer that supports a wide range of LLM providers

## Sources

- answer-and-context-relevance-judges-databricks-on-aws.md

# Citations

1. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
