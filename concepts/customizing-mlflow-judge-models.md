---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: da697ec353ea518ade42317533cfd32fc80309d5948a298ce3666aad6959080f
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - customizing-mlflow-judge-models
    - CMJM
  citations:
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Customizing MLflow Judge Models
description: The ability to replace the default Databricks-hosted LLM powering MLflow's built-in judges with any LiteLLM-compatible model, specified in the format <provider>:/<model-name>.
tags:
  - mlflow
  - llm-evaluation
  - configuration
  - litellm
timestamp: "2026-06-19T14:01:35.695Z"
---

# Customizing MLflow Judge Models

**Customizing MLflow Judge Models** refers to the ability to change the underlying large language model (LLM) that powers MLflow's built-in and custom judges. By default, judges use a Databricks-hosted LLM designed for GenAI quality assessments, but you can substitute any LiteLLM-compatible model to better suit your evaluation needs.

## Overview

MLflow judge models are LLMs that evaluate the quality of GenAI application outputs. Both built-in judges (such as [RelevanceToQuery](/concepts/relevancetoquery.md) and [RetrievalRelevance](/concepts/retrievalrelevance.md)) and custom judges created with make_judge() use an underlying model to perform assessments. Customizing the judge model allows you to control evaluation cost, accuracy, and alignment with your specific domain. ^[answer-and-context-relevance-judges-databricks-on-aws.md, create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Customizing the Judge Model

### Specifying a Different Model

When creating a judge, use the `model` argument to specify an alternative LLM. The model string must follow the format `<provider>:/<model-name>`, where:
- `<provider>` is a LiteLLM-compatible model provider (e.g., `databricks`, `openai`, `anthropic`)
- `<model-name>` is the serving endpoint name or model identifier

For Databricks models, the model name corresponds to the serving endpoint name. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

```python
from mlflow.genai.scorers import RelevanceToQuery, RetrievalRelevance

# Use a smaller, faster model for lower cost
relevance_judge = RelevanceToQuery(
    model="databricks:/databricks-gpt-5-mini"
)

# Use a powerful model for complex evaluations
retrieval_judge = RetrievalRelevance(
    model="databricks:/databricks-claude-opus-4-5"
)

# Use in evaluation
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=rag_app,
    scorers=[relevance_judge, retrieval_judge]
)
```

### Custom Judges with Custom Models

The same approach applies to custom judges created with `make_judge()`. If you do not specify a model, a default Databricks model is used. To override it, pass the `model` parameter:

```python
custom_judge = make_judge(
    name="issue_resolution",
    instructions="...",
    feedback_value_type=str,
    model="databricks:/databricks-gpt-5-mini"  # Custom model specification
)
```

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## When to Customize the Judge Model

### Cost Optimization
Smaller or more efficient models (e.g., `databricks-gpt-5-mini`) can reduce evaluation costs while still providing reliable assessments for well-defined criteria. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Accuracy Improvements
For complex evaluation tasks—such as assessing nuanced domain-specific outputs or multi-turn conversation quality—a more capable model may produce more accurate judgments. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

### Consistency Across Evaluations
Using the same judge model across all evaluations in a project ensures that score differences reflect changes in agent behavior rather than model variability. This is especially important in [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md). ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Considerations

- **LiteLLM Compatibility**: The model provider must be supported by LiteLLM. Databricks models use the `databricks` prefix with the serving endpoint name. ^[answer-and-context-relevance-judges-databricks-on-aws.md]
- **Access Permissions**: Ensure that the service principal or user running the evaluation has access to the specified model endpoint. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Latency and Throughput**: More powerful models typically have higher latency and lower throughput, which may affect evaluation run time for large datasets. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Related Concepts

- [Built-in Judges](/concepts/built-in-judges.md) — Pre-built judges that support model customization
- make_judge()|Make Judge API — Creating custom judges with configurable models
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for running evaluations
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Consistent model usage for fair comparisons
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying customized judges for continuous monitoring

## Sources

- answer-and-context-relevance-judges-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
