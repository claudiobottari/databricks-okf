---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 15123c5217f4105422d77e69fc8859b88c3f8e80e2bfebecb11fb86ce802c4f8
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - placeholder-scorer-pattern
    - PSP
  citations:
    - file: develop-code-based-scorers-databricks-on-aws.md
title: Placeholder Scorer Pattern
description: Using a minimal temporary scorer (e.g., returning a constant value) as a required argument to mlflow.genai.evaluate() to bootstrap trace generation before developing real metrics.
tags:
  - pattern
  - MLflow
  - scorers
  - workflow
timestamp: "2026-06-19T18:31:28.230Z"
---

```yaml
---
title: Placeholder Scorer Pattern
summary: Using a minimal placeholder scorer (returning a constant value) during initial trace generation, since mlflow.genai.evaluate() requires at least one scorer even when the goal is just to capture traces.
sources:
  - develop-code-based-scorers-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:27:42.077Z"
updatedAt: "2026-06-18T15:27:42.077Z"
tags:
  - mlflow
  - pattern
  - workflow
aliases:
  - placeholder-scorer-pattern
  - PSP
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Placeholder Scorer Pattern

The **Placeholder Scorer Pattern** is a workflow technique used during the iterative development of [[Code-based Scorers|custom code‑based scorers]] in MLflow Evaluation for GenAI. It enables you to generate execution traces from an AI application without implementing a real evaluation metric, then run later scoring iterations against those stored traces without re‑executing the application.

## Purpose

MLflow’s `mlflow.genai.evaluate()` function requires at least one scorer to be passed in the `scorers` argument. When the primary goal is to capture traces for subsequent metric development—rather than computing actual metrics in the first pass—a placeholder scorer satisfies this requirement with minimal overhead. ^[develop-code-based-scorers-databricks-on-aws.md]

## Implementation

A placeholder scorer is defined using the `@scorer` decorator and returns a constant value (typically `1`) that carries no semantic meaning. ^[develop-code-based-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer

@scorer
def placeholder_metric() -> int:
    # placeholder return value
    return 1
```

The function signature must be valid for the framework: in this case it takes no arguments and returns an `int`.

## Workflow

The placeholder scorer pattern fits into a four‑step iterative development cycle:

1. **Define evaluation data** – Prepare a dataset of inputs to pass to the application (e.g., a list of messages or questions). ^[develop-code-based-scorers-databricks-on-aws.md]
2. **Generate traces** – Call `mlflow.genai.evaluate()` with the evaluation data, the application’s prediction function, and the placeholder scorer. This produces a trace for every row in the dataset. ^[develop-code-based-scorers-databricks-on-aws.md]
3. **Store the traces** – Use `mlflow.search_traces(run_id=eval_results.run_id)` to retrieve the generated traces as a Pandas DataFrame. ^[develop-code-based-scorers-databricks-on-aws.md]
4. **Iterate on the scorer** – Pass the stored DataFrame directly to `evaluate()` (omitting `predict_fn`) while replacing the placeholder with a real scorer. This runs the new metric against the same traces without re‑invoking the application. ^[develop-code-based-scorers-databricks-on-aws.md]

In Databricks notebooks, traces appear in the Trace UI as part of cell results, and the LLM’s response is shown in the **Outputs** field. ^[develop-code-based-scorers-databricks-on-aws.md]

## Benefits

The primary benefit of the pattern is that it allows you to iterate on scorer logic without rerunning the entire application each time, which can be slow or expensive (e.g., when calling external LLMs). ^[develop-code-based-scorers-databricks-on-aws.md] Because the traces are fixed after the first pass, any change in metric scores is due solely to the scorer logic, enabling deterministic comparisons during development.

## Related Concepts

- [[Code-based Scorers|Custom code‑based scorers]] – The fully featured scorers that replace the placeholder during iteration.
- MLflow Evaluation for GenAI – The framework that supports the `evaluate()` API and trace storage.
- [[Traces]] – Execution traces recorded by [[mlflow-tracing|MLflow Tracing]], used as input for scorer iteration.
- Predict function – The application function that generates outputs; omitted when scoring stored traces.

## Sources

- develop-code-based-scorers-databricks-on-aws.md
```

# Citations

1. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
