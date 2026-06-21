---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 405e5be3fa7db0ecf46603ffe70deb0bb92da7639a2d4a4177ff4821d566e40b
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-and-autologging
    - Autologging and MLflow Trace
    - MTAA
    - MLflow Tracking and Autologging
    - autologging for MLflow tracking
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
title: MLflow Trace and Autologging
description: Automatic tracing of GenAI application calls (e.g., OpenAI) via mlflow.openai.autolog() to capture inputs, outputs, and metadata for evaluation and debugging.
tags:
  - mlflow
  - tracing
  - observability
timestamp: "2026-06-18T10:35:17.826Z"
---

# MLflow Trace and Autologging

MLflow Trace and Autologging provides a mechanism for automatically capturing execution traces and structured data from Generative AI (GenAI) applications and other ML workflows. By leveraging MLflow's tracing infrastructure, teams can record model inputs, outputs, and metadata without manual instrumentation, enabling observability and reproducibility in AI application development. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Overview

[MLflow Autologging](/concepts/mlflow-autologging.md) is a built-in feature that automatically records traces and associated metadata when using supported frameworks. When enabled, it captures detailed information about each invocation, including the model used, inputs passed, and outputs returned. This data is then stored as part of an MLflow Trace, which can be viewed in the MLflow UI and used for subsequent evaluation and analysis. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

Autologging reduces the overhead of manually adding tracing decorators to every function call. By calling a single `autolog()` setup method, MLflow instruments supported library calls to record full execution traces automatically. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Supported Frameworks

[MLflow Autologging](/concepts/mlflow-autologging.md) is available for several major GenAI and ML frameworks:

- **OpenAI**: `mlflow.openai.autolog()` — records interactions with the OpenAI API, including model, messages, and completion responses.
- Other supported providers can be enabled through the same pattern; see [MLflow Tracing](/concepts/mlflow-tracing.md) for the full list of integrations.

When autologging is enabled, the `autolog()` call sets up MLflow to intercept requests to the underlying service and record them as traces. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Manual Tracing with `@mlflow.trace`

For code paths that are not automatically instrumented, MLflow provides the `@mlflow.trace` decorator. This decorator can be applied to any Python function to explicitly mark it for tracing. Traced functions generate a structured record (a trace) of their execution, including parameters and outputs. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

```python
@mlflow.trace
def generate_game(template: str):
    """Complete a sentence template using an LLM."""
    response = client.chat.completions.create(
        model="databricks-claude-sonnet-4-5",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": template},
        ],
    )
    return response.choices[0].message.content
```

In this example, the `@mlflow.trace` decorator wraps the `generate_game` function, ensuring that every call to it — including the inputs (`template`) and the LLM response — is captured as part of the current [MLflow Run](/concepts/mlflow-run.md)'s trace. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Trace Structure and Contents

Each trace recorded by MLflow (whether via autologging or manual decoration) contains:

- **Inputs**: The arguments passed to the function, including the prompt template and any user-provided context.
- **Outputs**: The return value of the function, typically the LLM's completion text.
- **Metadata**: Additional information such as the model identifier, timing information, and any error details.

Traces are grouped under an MLflow Experiment; each invocation creates a new trace entry. Users can navigate to the Experiment via the MLflow UI to inspect individual traces. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Viewing Traces in the UI

When running in a Databricks notebook, MLflow displays an interactive trace viewer directly in the cell output after the function runs. Clicking on any trace in the notebook output opens a detailed view showing the full input/output chain. The same information is available in the Experiment UI under the **Logs** tab. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Evaluation with Traces

Traces recorded via autologging or manual tracing can be used as evaluation data. The [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) framework accepts traces as its `data` parameter, allowing scorers to assess the quality of outputs generated by the traced function. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

```python
results = mlflow.genai.evaluate(
    data=eval_data,      # Can be either explicit data or traced outputs
    predict_fn=generate_game,
    scorers=scorers
)
```

When `evaluate()` is called, MLflow uses the trace metadata to compute scores for each defined scorer (e.g., [Guidelines Scorer](/concepts/guidelines-scorer.md), [Correctness Scorer](/concepts/correctness-scorer.md)). Multiple evaluation runs can be compared side-by-side in the MLflow UI to track improvements as prompts or models are updated. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The underlying infrastructure that records execution details as structured traces.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The evaluation framework that uses traces to compute quality metrics.
- [MLflow Experiment](/concepts/mlflow-experiment.md) — Logical grouping of runs and traces in the MLflow UI.
- [Guidelines Scorer](/concepts/guidelines-scorer.md) — A built-in scorer that checks responses against configurable guidelines.
- [Safety Scorer](/concepts/safety-scorer-in-mlflow.md) — A built-in scorer for detecting unsafe or inappropriate content in LLM outputs.

## Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
