---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 82901e028c90111b29b01fd272143a82938b04a50df1fc3926dc3f3be4a9e3dd
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - placeholder-scorers-for-trace-generation
    - PSFTG
  citations:
    - file: develop-code-based-scorers-databricks-on-aws.md
title: Placeholder Scorers for Trace Generation
description: The pattern of defining a minimal placeholder scorer (e.g., a no-op function returning a constant) when initially generating traces via mlflow.genai.evaluate(), since evaluate() requires at least one scorer.
tags:
  - mlflow
  - pattern
  - evaluation
  - scorers
timestamp: "2026-06-19T10:13:11.008Z"
---

# Placeholder Scorers for Trace Generation

**Placeholder Scorers for Trace Generation** are minimal, dummy scoring functions used during the initial evaluation run of a GenAI agent to satisfy the scorer requirement of `mlflow.genai.evaluate()` while collecting execution traces. They enable a two-phase workflow: first generate traces without meaningful metrics, then iterate on real scorers using the stored traces.

## Need for Placeholder Scorers

The `mlflow.genai.evaluate()` API requires at least one scorer to run. When the goal is to generate traces from an application (e.g., to inspect outputs or build an evaluation dataset) before developing a proper metric, a placeholder scorer must be provided. This allows trace collection to proceed without a substantive evaluation criterion.^[develop-code-based-scorers-databricks-on-aws.md]

## Defining a Placeholder Scorer

A placeholder scorer is created using the `@scorer` decorator from `mlflow.genai.scorers`. It must have an appropriate return type but its logic is trivial — typically returning a constant value. The example below defines a placeholder that always returns `1`:^[develop-code-based-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer

@scorer
def placeholder_metric() -> int:
    # placeholder return value
    return 1
```

## Workflow

### Step 1 – Generate traces with the placeholder

Pass the placeholder scorer to `mlflow.genai.evaluate()` along with the evaluation dataset and the application `predict_fn`. The function runs the app on each input and records a trace for every row, even though the scorer itself performs no meaningful evaluation.^[develop-code-based-scorers-databricks-on-aws.md]

```python
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=sample_app,
    scorers=[placeholder_metric])
```

### Step 2 – Store the resulting traces

After evaluation, the traces are stored in the experiment (visible in the Databricks trace UI). They can be retrieved as a Pandas DataFrame using `mlflow.search_traces()`:^[develop-code-based-scorers-databricks-on-aws.md]

```python
generated_traces = mlflow.search_traces(run_id=eval_results.run_id)
```

### Step 3 – Iterate with real scorers

Once the traces are collected, the developer can define actual [Code-based Scorers](/concepts/code-based-scorers.md) and call `evaluate()` again with the stored traces as the `data` parameter — without needing to re-run the original application. The `predict_fn` parameter is omitted in this second call.^[develop-code-based-scorers-databricks-on-aws.md]

```python
@scorer
def response_length(outputs: str) -> int:
    # Example metric
    return len(outputs)

mlflow.genai.evaluate(
    data=generated_traces,
    scorers=[response_length])
```

This iterative workflow avoids redundant application executions and speeds up scorer development.

## Related Concepts

- [Code-based Scorers](/concepts/code-based-scorers.md) — The general mechanism for custom evaluation metrics.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The evaluation framework that enforces the scorer requirement.
- [Trace generation](/concepts/custom-trace-id-generation.md) — The process of recording application execution traces.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The underlying instrumentation for capturing traces.
- [Developer workflow for code-based scorers](/concepts/developer-iteration-workflow-for-scorers.md) — The broader iterative process described in the source.

## Sources

- develop-code-based-scorers-databricks-on-aws.md

# Citations

1. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
