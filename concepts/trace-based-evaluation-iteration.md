---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a63fd372f34e3831dc697d1ecfda30f04fb90b281e9fad8223dea6cd2eea32a2
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-based-evaluation-iteration
    - TEI
  citations:
    - file: develop-code-based-scorers-databricks-on-aws.md
title: Trace-based Evaluation Iteration
description: Technique of passing a Pandas DataFrame of pre-computed MLflow traces directly to mlflow.genai.evaluate() to iterate on scorers without rerunning the application.
tags:
  - MLflow
  - traces
  - optimization
  - evaluation
timestamp: "2026-06-19T18:31:12.504Z"
---

# Trace-based Evaluation Iteration

**Trace-based Evaluation Iteration** is a developer workflow for [Code-based Scorers](/concepts/code-based-scorers.md) in [MLflow](/concepts/mlflow.md) Evaluation for GenAI. It allows developers to quickly update a scorer and re-evaluate it without rerunning the entire application, by reusing stored traces from a previous evaluation run. ^[develop-code-based-scorers-databricks-on-aws.md]

## Workflow

The workflow consists of four steps:

1. **Define evaluation data** – Create a dataset of inputs for the application (e.g., a list of questions or conversation turns).
2. **Generate traces from your app** – Run `mlflow.genai.evaluate()` with a placeholder scorer to produce traces. The application is called for each input row, and MLflow records a [trace](/concepts/traces.md) for each call.
3. **Query and store the resulting traces** – Use `mlflow.search_traces()` to retrieve the generated traces as a Pandas DataFrame. Save this DataFrame in a local variable.
4. **Iterate on your scorer using the stored traces** – Pass the stored traces DataFrame directly as the `data` argument to `mlflow.genai.evaluate()`, along with the new scorer(s). Because the traces already contain the application outputs, no `predict_fn` is required, and the scorer runs only on the cached responses.

^[develop-code-based-scorers-databricks-on-aws.md]

## Benefits

The primary benefit of trace-based evaluation iteration is **speed**. Developing a custom scorer often involves multiple rounds of tuning logic, thresholds, or aggregation. Without this workflow, each change would require re-running the full application (including expensive LLM calls) against the evaluation dataset. By storing traces once and reusing them, developers can iterate on the scorer in isolation, dramatically reducing turnaround time. ^[develop-code-based-scorers-databricks-on-aws.md]

## Example

A complete example notebook is available in the source documentation. The key pattern is shown below:

```python
# Step 2: Generate traces with a placeholder scorer
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=sample_app,
    scorers=[placeholder_metric]
)

# Step 3: Store the traces
generated_traces = mlflow.search_traces(run_id=eval_results.run_id)

# Step 4: Iterate on the scorer using stored traces
@scorer
def response_length(outputs: str) -> int:
    return len(outputs)

mlflow.genai.evaluate(
    data=generated_traces,
    scorers=[response_length],
)
```

The placeholder scorer in step 2 can be any minimal scorer (e.g., one that always returns a constant). Its only purpose is to satisfy the `scorers` parameter of `evaluate()` so that traces are generated. ^[develop-code-based-scorers-databricks-on-aws.md]

## Related Concepts

- [Code-based Scorers](/concepts/code-based-scorers.md) – Custom evaluation metrics defined using the `@scorer` decorator.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The framework for evaluating generative AI applications.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The instrumentation layer that records traces for each application call.
- [Evaluation Datasets](/concepts/evaluation-datasets.md) – Input datasets used to drive evaluation and trace generation.

## Sources

- develop-code-based-scorers-databricks-on-aws.md

# Citations

1. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
