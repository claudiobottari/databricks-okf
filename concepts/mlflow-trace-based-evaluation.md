---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 724378efb1f72f4641f9776de71c4827a7c838210bcd06f0c887da52893cc2c4
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-based-evaluation
    - MTE
    - Trace-Based Evaluation
    - Trace-based Evaluation
    - Trace-based evaluation
    - Trace‑Based Evaluation
    - trace-based evaluation
    - Trace Evaluation
  citations:
    - file: develop-code-based-scorers-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: MLflow Trace-based Evaluation
description: Technique of passing a Pandas DataFrame of precomputed MLflow traces directly to mlflow.genai.evaluate() instead of a predict_fn, enabling rapid scorer iteration without re-running the application.
tags:
  - mlflow
  - tracing
  - evaluation
  - optimization
timestamp: "2026-06-18T12:00:21.589Z"
---

# MLflow Trace-based Evaluation

**MLflow Trace-based Evaluation** is a method of evaluating GenAI agents and applications by using [MLflow Tracing](/concepts/mlflow-tracing.md) execution traces as the input to scorers and judges. This approach decouples trace generation from metric computation, allowing developers to iterate on evaluation criteria without re-running the full application.

## Overview

In a typical MLflow Evaluation workflow, the evaluation function (`mlflow.genai.evaluate()`) calls the application’s prediction function, captures traces, and scores the outputs in a single pass. Trace-based evaluation instead first generates and stores traces, then runs scorers or judges against those stored traces. By separating trace generation from scoring, developers can rapidly iterate on evaluation logic—changing a scorer’s definition and re-evaluating without invoking the underlying model or agent again. ^[develop-code-based-scorers-databricks-on-aws.md]

## Developer Workflow for Code-Based Scorers

The recommended workflow for developing code-based scorers with traces has four steps: ^[develop-code-based-scorers-databricks-on-aws.md]

1.  **Define evaluation data** — Create a list of test inputs (conversations, queries) that represent the scenarios you want to evaluate.
2.  **Generate traces from your app** — Run `mlflow.genai.evaluate()` with a placeholder scorer and your prediction function to record execution traces.
3.  **Query and store the resulting traces** — Use `mlflow.search_traces()` to retrieve the generated traces as a Pandas DataFrame.
4.  **Iterate on your scorer using stored traces** — Pass the DataFrame directly to `evaluate()` in subsequent calls (without a `predict_fn`). Changing the scorer’s logic now runs only the metric against the precomputed traces.

```python
# Step 2: Generate traces using a placeholder scorer
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=sample_app,
    scorers=[placeholder_metric],
)

# Step 3: Store traces
traces_df = mlflow.search_traces(run_id=eval_results.run_id)

# Step 4: Iterate on the scorer
@scorer
def response_length(outputs: str) -> int:
    return len(outputs)

mlflow.genai.evaluate(
    data=traces_df,          # ← use stored traces
    scorers=[response_length],  # ← no predict_fn
)
```

^[develop-code-based-scorers-databricks-on-aws.md]

This pattern is especially helpful when the application is slow to run or depends on external APIs—the traces are recorded once and reused across many scoring iterations.

## Trace-Based Judges

In addition to code-based scorers, trace-based evaluation can be performed using [Custom Judges](/concepts/custom-judges.md)—LLM-as-a-judge metrics that use a language model to score outputs. A **trace-based judge** analyzes the full execution trace, including tool invocation calls, intermediate reasoning steps, and their results. To create such a judge, include the template variable `{{ trace }}` in the judge’s instructions. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
from mlflow.genai import make_judge

tool_call_judge = make_judge(
    name="tool_call_correctness",
    instructions=(
        "Analyze the execution {{ trace }} to determine if the agent "
        "called appropriate tools for the user's request."
    ),
    feedback_value_type=bool,
    # Trace-based judges require a model specification
    model="databricks:/databricks-gpt-5-mini",
)
```

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

Trace-based judges are particularly useful for evaluating multi-step agent behavior, such as correct tool selection and proper sequencing of calls, which cannot be assessed from final output alone.

## Benefits

- **Faster iteration** — Scorers and judges can be refined and re-run against the same trace dataset without incurring application inference costs.
- **Reproducibility** — Stored traces provide a fixed snapshot of model responses, enabling consistent comparisons across different evaluation metrics.
- **Deep inspection** — Trace-based judges have access to the complete execution path, allowing validation of intermediate steps rather than only the final answer.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The underlying instrumentation that captures execution traces.
- [Code-based Scorers](/concepts/code-based-scorers.md) — Custom Python functions that compute metrics from trace data.
- [Custom Judges](/concepts/custom-judges.md) — LLM-powered evaluators that use natural language criteria.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The broader framework for offline and online evaluation of GenAI applications.
- Developer Workflow for Scorers — The iterative loop of trace generation and scoring.

## Sources

- develop-code-based-scorers-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
