---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2dd89e3cceb5ffbd14f556c672f9762115f494fa5ba7ac3beaa9b4c620b8ddc6
  pageDirectory: concepts
  sources:
    - evaluate-genai-apps-during-development-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-evaluation-runs
    - MER
  citations:
    - file: evaluate-genai-apps-during-development-databricks-on-aws.md
title: MLflow Evaluation Runs
description: Test report capturing everything about how a GenAI app performed on a specific dataset, including per-row traces annotated with feedback from each judge.
tags:
  - mlflow
  - evaluation
  - runs
timestamp: "2026-06-18T12:13:18.261Z"
---

# MLflow Evaluation Runs

**MLflow Evaluation Runs** are structured test reports that capture how a GenAI application performed against a specific [Evaluation Dataset](/concepts/evaluation-dataset.md). Each evaluation run contains a [trace](/concepts/traces.md) for every row in the evaluation dataset, annotated with feedback from each [[Scorers|scorer]] or judge applied during evaluation. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Overview

When you use `mlflow.genai.evaluate()`, MLflow creates an evaluation run in the active [MLflow Experiment](/concepts/mlflow-experiment.md). The run stores the results of systematically testing a GenAI app against test data using specified scorers, enabling teams to compare versions, track improvements, and share results. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

MLflow Evaluation connects offline testing with [Production Monitoring](/concepts/production-monitoring.md). The same evaluation logic used in development can run in production, providing a consistent view of quality across the entire AI lifecycle. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## What an Evaluation Run Contains

Each evaluation run stores: ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

- **Traces** — One trace per record in the evaluation dataset, capturing the full execution of your app for that input.
- **Feedback** — Annotations from each scorer or judge applied to each trace.
- **Aggregate metrics** — Summary statistics across all evaluation records.
- **Model ID** — Optional version tracking identifier (e.g., `"models:/my-app/1"`).

## Viewing Evaluation Results in the UI

### Assessment Summary

1. Click **Experiments** in the sidebar to display the Experiments page.
2. Click on the name of your experiment to open it.
3. In the left sidebar, click **Evaluation runs**. The right pane shows a table of traces with assessment results.
4. To see whether a trace passed or failed a given assessment, scroll to the right or expand the pane.
5. Hover over the **Pass** or **Fail** label to see the rationale from the judge. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

### Details and Adding Feedback

1. Click on the request identifier in the **Request** column. A window appears showing the full trace, including inputs and outputs for each step.
2. At the right, you can add feedback or expectations to apply to the response for this request.
3. Use the arrows at either side of the window to step through requests. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Evaluation Modes

### Direct Evaluation (Recommended)

MLflow calls your app directly to generate and evaluate traces. You pass your application's entry point wrapped in a Python function (`predict_fn`) or, if your app is deployed as a [Databricks Model Serving](/concepts/databricks-model-serving.md) endpoint, pass that endpoint wrapped in `to_predict_fn`. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

By calling your app directly, this mode enables you to reuse the scorers defined for offline evaluation in production monitoring, since the resulting traces are identical. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

### Answer Sheet Evaluation

Use this mode when you cannot or do not want to run your GenAI app directly during evaluation. You provide the inputs and pre-computed outputs (or existing traces), and `evaluate()` runs scorers and logs an evaluation run. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

This mode is useful for: ^[evaluate-genai-apps-during-development-databricks-on-aws.md]
- Outputs from external systems
- Historical traces
- Batch job results

However, if you use an answer sheet with different traces than your production environment, you may need to re-write your scorer functions to use them for production monitoring. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Scorers and Feedback

Each scorer applied during evaluation generates feedback for every trace. Scorers can be: ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

- **Built-in scorers** — Pre-defined quality metrics provided by MLflow
- **Custom scorers** — User-defined metrics tailored to specific use cases
- **LLM judges** — Language model-based evaluators that assess quality criteria

See [[Scorers]] for more details.

## Data Formats

For direct evaluation, data must follow the schema used by `EvaluationDataset`: ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

- `inputs` — A dictionary of input parameters passed to your `predict_fn`
- `outputs` — (For answer sheet mode) Pre-computed outputs
- `expectations` — (Optional) Expected results that judges can reference

For answer sheet evaluation, you can provide either: ^[evaluate-genai-apps-during-development-databricks-on-aws.md]
- Inputs and pre-computed outputs
- Existing traces retrieved via `mlflow.search_traces()`

## When to Use Evaluation Runs

- Nightly or weekly checks of your app against curated evaluation datasets
- Validating prompt or model changes across app versions
- Before a release or pull request to prevent quality regressions

## Parameters Reference

```python
def mlflow.genai.evaluate(
    data: Union[pd.DataFrame, List[Dict], mlflow.genai.datasets.EvaluationDataset],
    scorers: list[mlflow.genai.scorers.Scorer],
    predict_fn: Optional[Callable[..., Any]] = None,
    model_id: Optional[str] = None,
) -> mlflow.models.evaluation.base.EvaluationResult:
```

### `data`
The evaluation dataset. Can be an `EvaluationDataset` (recommended), list of dictionaries, Pandas DataFrame, or Spark DataFrame. Databricks recommends using `EvaluationDataset` as it enforces schema validation and tracks lineage. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

### `scorers`
List of quality metrics to apply. See [[Scorers]] for details. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

### `predict_fn`
The GenAI app's entry point, used only with direct evaluation. Must: ^[evaluate-genai-apps-during-development-databricks-on-aws.md]
- Accept the keys from the `inputs` dictionary as keyword arguments
- Return a JSON-serializable dictionary
- Be instrumented with [MLflow Tracing](/concepts/mlflow-tracing.md)
- Emit exactly one trace per call

### `model_id`
Optional model identifier to link results to your app version (e.g., `"models:/my-app/1"`). ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for runs
- [Traces](/concepts/traces.md) — Execution records captured during evaluation
- [[Scorers]] — Quality metrics applied during evaluation
- [Custom Judges](/concepts/custom-judges.md) — LLM-based evaluators for quality assessment
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying evaluation logic in production
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Structured test data for evaluation
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Comparing app versions using evaluation runs

## Sources

- evaluate-genai-apps-during-development-databricks-on-aws.md

# Citations

1. [evaluate-genai-apps-during-development-databricks-on-aws.md](/references/evaluate-genai-apps-during-development-databricks-on-aws-373c1693.md)
