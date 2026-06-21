---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 627a7ffb06facd578454835181f0197a4ce92255cbc16e3f1a423b85f3196a4d
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - placeholder-scorers
  citations:
    - file: develop-code-based-scorers-databricks-on-aws.md
title: Placeholder Scorers
description: Minimal scorer functions used solely to satisfy mlflow.genai.evaluate() requirements during initial trace generation, later replaced with real evaluation logic.
tags:
  - mlflow
  - scoring
  - patterns
timestamp: "2026-06-18T12:00:27.108Z"
---

# Placeholder Scorers

**Placeholder scorers** are minimal, temporary evaluation metrics used during the development workflow for [Code-based Scorers](/concepts/code-based-scorers.md) in MLflow Evaluation for GenAI. Their primary purpose is to satisfy MLflow's requirement for at least one scorer when calling `mlflow.genai.evaluate()` during trace generation, enabling developers to iterate on their main scorers without unnecessary re-execution of the application. ^[develop-code-based-scorers-databricks-on-aws.md]

## Purpose

When using the recommended developer workflow for building custom scorers, the first step often involves generating traces from an application using `mlflow.genai.evaluate()`. However, this function requires at least one scorer to be passed in. A placeholder scorer provides a stub metric that meets this requirement without performing meaningful evaluation. ^[develop-code-based-scorers-databricks-on-aws.md]

Once traces have been generated and stored, developers can iterate on their actual scorers by calling `evaluate()` against the stored traces directly, bypassing the application entirely. The placeholder scorer is no longer needed after this initial trace generation step. ^[develop-code-based-scorers-databricks-on-aws.md]

## Implementation

Placeholder scorers are defined using the `@scorer` decorator from `mlflow.genai.scorers`. They must return a value of the expected type, but the value itself is irrelevant and does not affect downstream evaluation. ^[develop-code-based-scorers-databricks-on-aws.md]

### Example

The following example creates a placeholder scorer that returns a constant integer value:

```python
from mlflow.genai.scorers import scorer

@scorer
def placeholder_metric() -> int:
    # placeholder return value
    return 1
```

^[develop-code-based-scorers-databricks-on-aws.md]

## Usage in the Developer Workflow

The placeholder scorer is used in the initial trace generation step of the developer workflow:

```python
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=sample_app,
    scorers=[placeholder_metric]
)
```

After this call, traces are available for querying via `mlflow.search_traces()`. Subsequent evaluations can use the stored traces as input data and replace the placeholder scorer with the actual metrics being developed. ^[develop-code-based-scorers-databricks-on-aws.md]

## Best Practices

- **Use the placeholder scorer only for initial trace generation.** Replace it with real scorers as soon as traces are available for offline evaluation.
- **Ensure the placeholder scorer returns a valid type** that does not interfere with any evaluation infrastructure requirements (typically a simple integer or boolean).
- **Do not confuse placeholder scorers with [Custom Judges](/concepts/custom-judges.md) or other LLM-as-a-judge metrics**, which perform semantic evaluation and are used in production monitoring.

## Related Concepts

- [Code-based Scorers](/concepts/code-based-scorers.md) — The main type of scorer that placeholder scorers substitute during development
- [Custom LLM scorers](/concepts/custom-judge-scorers.md) — LLM-as-a-judge metrics for semantic evaluation
- MLflow Evaluation for GenAI — The evaluation framework used with scorers
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying scorers for continuous monitoring
- [Developer workflow for code-based scorers](/concepts/developer-iteration-workflow-for-scorers.md) — The full workflow in which placeholder scorers are used

## Sources

- develop-code-based-scorers-databricks-on-aws.md

# Citations

1. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
