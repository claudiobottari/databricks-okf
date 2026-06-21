---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bbfd4b066112f062c0d1e3b6d836a3be1cf749ddd62eb3157fe7d1a1cbc37efe
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-query-and-reuse
    - Reuse and MLflow Trace Query
    - MTQAR
  citations:
    - file: develop-code-based-scorers-databricks-on-aws.md
title: MLflow Trace Query and Reuse
description: The pattern of using mlflow.search_traces() to query stored evaluation traces and pass the resulting DataFrame directly to mlflow.genai.evaluate() for rapid metric iteration.
tags:
  - mlflow
  - tracing
  - evaluation
  - data-reuse
timestamp: "2026-06-19T15:11:24.717Z"
---

---
title: MLflow Trace Query and Reuse
summary: A developer workflow that captures execution traces from an AI application and reuses them to iterate on code-based scorers without rerunning the application.
sources:
  - develop-code-based-scorers-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T10:00:00.000Z"
updatedAt: "2026-06-20T10:00:00.000Z"
tags:
  - mlflow
  - evaluation
  - traces
  - developer-workflow
aliases:
  - mlflow-trace-query-and-reuse
  - MTQR
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# MLflow Trace Query and Reuse

**MLflow Trace Query and Reuse** is a development practice that accelerates the iteration of [custom code-based scorers](/concepts/code-based-scorers.md) for MLflow Evaluation for GenAI. The workflow first generates execution traces from an AI application (such as an LLM agent or chatbot) using [MLflow Tracing](/concepts/mlflow-tracing.md), then queries and stores those traces as a Pandas DataFrame. Subsequent calls to `mlflow.genai.evaluate()` can use the stored traces directly as input data, allowing the scorer logic to be refined without re-running the application. ^[develop-code-based-scorers-databricks-on-aws.md]

## Workflow Overview

The recommended developer workflow consists of four steps: ^[develop-code-based-scorers-databricks-on-aws.md]

1. **Define evaluation data** – A dataset of inputs (e.g., lists of messages) for the application.
2. **Generate traces from the application** – Run `mlflow.genai.evaluate()` with a placeholder scorer to produce execution traces. MLflow automatically records the input, output, and any intermediate steps when autologging is enabled (e.g., `mlflow.openai.autolog()`).
3. **Query and store the resulting traces** – Use `mlflow.search_traces()` to retrieve the traces as a Pandas DataFrame, typically filtered by the evaluation run ID.
4. **Iterate on the scorer** – Call `mlflow.genai.evaluate()` with the stored traces DataFrame (and without a `predict_fn` parameter) to run new scorer logic on the previously captured outputs.

## Querying Traces

After generating traces (step 2), the traces are stored in the active [MLflow Experiment](/concepts/mlflow-experiment.md). The function `mlflow.search_traces(run_id=<eval_results.run_id>)` returns a Pandas DataFrame where each row corresponds to one recorded trace. This DataFrame contains the original inputs, the application’s outputs, and any metadata captured during tracing. ^[develop-code-based-scorers-databricks-on-aws.md]

## Reusing Traces for Scorer Iteration

Once the traces are stored locally, you can define a new scorer (using the `@scorer` decorator) and pass the DataFrame directly to `mlflow.genai.evaluate()` via the `data` parameter. Because the traces already contain the application’s outputs, the `predict_fn` argument is omitted. This enables fast iteration: the scorer can be modified and re-run against the same set of traces without any latency from the application. ^[develop-code-based-scorers-databricks-on-aws.md]

### Example

The pattern is illustrated in the following code snippet: ^[develop-code-based-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer

@scorer
def response_length(outputs: str) -> int:
    return len(outputs)

mlflow.genai.evaluate(
    data=generated_traces,       # DataFrame from mlflow.search_traces()
    scorers=[response_length],
)
```

## Benefits

- **Faster iteration** – Scorers can be developed and tested against a fixed set of application outputs, eliminating the time and cost of rerunning the application.
- **Isolated debugging** – The same traces can be inspected and re-evaluated to compare different metric implementations.
- **Deterministic evaluation** – Since the application outputs are frozen, scorer changes do not introduce variability from the underlying model.

## Prerequisites

- MLflow with Databricks integration (`mlflow[databricks]>=3.1`).
- Application instrumentation via [MLflow Autologging](/concepts/mlflow-autologging.md) (e.g., `mlflow.openai.autolog()`) or explicit `@mlflow.trace` decorators.
- At least one placeholder scorer for the initial trace generation, because `mlflow.genai.evaluate()` requires a `scorers` argument.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The underlying telemetry system that records execution traces.
- [Code-based Scorers](/concepts/code-based-scorers.md) – Custom evaluation metrics defined with the `@scorer` decorator.
- MLflow Evaluation for GenAI – The broader framework for evaluating generative AI applications.
- [MLflow Experiment](/concepts/mlflow-experiment.md) – The organizational unit where traces and evaluation results are stored.
- [Custom LLM judge scorers](/concepts/custom-judge-scorers.md) – An alternative semantic evaluation approach that can also benefit from trace reuse.

## Sources

- develop-code-based-scorers-databricks-on-aws.md

# Citations

1. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
