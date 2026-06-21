---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1c074d86d6128183e22ed8dd912b3cdbe7d86f46145044c2819cae57cb6965d4
  pageDirectory: concepts
  sources:
    - evaluate-genai-apps-during-development-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - evaluation-production-consistency
  citations:
    - file: evaluate-genai-apps-during-development-databricks-on-aws.md
title: Evaluation-Production Consistency
description: The principle that same evaluation logic and scorers used in offline development can be reused in production monitoring, providing consistent quality views across the AI lifecycle.
tags:
  - mlflow
  - evaluation
  - production-monitoring
timestamp: "2026-06-18T12:13:10.756Z"
---

# Evaluation-Production Consistency

**Evaluation-Production Consistency** is the principle that the same evaluation logic, scorers, and metrics used during development should also be applied in production monitoring to provide a consistent view of [GenAI](/concepts/mlflow-genai-evaluate-api.md) application quality across the entire AI lifecycle.

MLflow Evaluation connects offline testing with [Production Monitoring](/concepts/production-monitoring.md). This means the same evaluation logic you use in development can also run in production, giving you a consistent view of quality across the entire AI lifecycle.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Key Principles

### Reuse Scorers Across Environments

When using [Direct Evaluation](/concepts/direct-evaluation.md) mode, MLflow calls your application directly to generate traces. By calling your app directly, this mode enables you to reuse the scorers defined for offline evaluation in [Production Monitoring](/concepts/production-monitoring.md) since the resulting traces will be identical.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

### Consistent Trace Format for Production Monitoring

If you use an answer sheet with different traces than your production environment, you may need to re-write your scorer functions to use them for [Production Monitoring](/concepts/production-monitoring.md).^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Benefits of Consistency

- **Comparable results**: The same scorers applied to development and production traces produce comparable quality metrics, enabling data-driven decisions about when to promote a model version.
- **Reduced rework**: Scorers developed and validated during offline testing can be deployed directly to production without modification.
- **Unified quality view**: Teams can track quality trends across the entire AI lifecycle, from experimentation through deployment.

## Achieving Consistency

### Use Direct Evaluation

When you evaluate your GenAI app using the `predict_fn` parameter, MLflow calls your application directly and generates traces. These traces have the same structure as production traces, allowing you to directly apply production scorers to development traces.

```python
# Development evaluation
results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=my_chatbot_app,
    scorers=[RelevanceToQuery(), Safety()]
)
```

^[evaluate-genai-apps-during-development-databricks-on-aws.md]

### Use Consistent Scoring Functions

When you define [Custom Judges](/concepts/custom-judges.md) using `make_judge()`, the same judge can be used for both development and production evaluation. This ensures that the quality criteria applied during development match those applied in production.

### Track Model Versions

Use the `model_id` parameter to link evaluation results to your app version. This creates an auditable trail connecting development evaluations to production deployments.

```python
model_id = "models:/my-app/1"
results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=my_chatbot_app,
    scorers=[RelevanceToQuery(), Safety()],
    model_id=model_id
)
```

^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The structured evaluation framework for GenAI applications
- [Production Monitoring](/concepts/production-monitoring.md) — Applying evaluation logic in production
- [Custom Judges](/concepts/custom-judges.md) — Scoring functions that can be used in both development and production
- [Trace-based evaluation](/concepts/mlflow-trace-based-evaluation.md) — Using execution traces for consistent quality assessment
- [Evaluation Runs](/concepts/evaluation-runs.md) — Test reports that capture app performance on specific datasets
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Structured test data used for consistent evaluation

## Sources

- evaluate-genai-apps-during-development-databricks-on-aws.md

# Citations

1. [evaluate-genai-apps-during-development-databricks-on-aws.md](/references/evaluate-genai-apps-during-development-databricks-on-aws-373c1693.md)
