---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cddc9ab5a7d7a76319c1fd0dc2306c2248611062d891ee93ab98e1797558fb5e
  pageDirectory: concepts
  sources:
    - evaluate-genai-apps-during-development-databricks-on-aws.md
    - tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-evaluation-harness
    - MGEH
    - MLflow Evaluation Harness
    - MLflow evaluation harness
  citations:
    - file: evaluate-genai-apps-during-development-databricks-on-aws.md
title: MLflow GenAI Evaluation Harness
description: A structured framework using `mlflow.genai.evaluate()` to systematically test GenAI app quality against curated datasets using scorers, with support for both direct and answer-sheet modes.
tags:
  - mlflow
  - genai
  - evaluation
  - testing
timestamp: "2026-06-19T18:43:56.890Z"
---

# MLflow GenAI Evaluation Harness

The **MLflow GenAI Evaluation Harness** is a structured testing framework provided by the [`mlflow.genai.evaluate()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate) function that systematically evaluates generative AI application quality by running the app against curated test data ([Evaluation Datasets](/concepts/evaluation-datasets.md)) and applying automated [[scorers]] to assess the results. Instead of manually running an app and checking outputs one by one, the harness provides a repeatable, shareable way to feed in test data, run the app, and automatically score the results, making it easier to compare versions, track improvements, and share results across teams. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

The evaluation harness connects offline testing with [Production quality monitoring](/concepts/production-monitoring.md). The same evaluation logic used in development can also run in production, providing a consistent view of quality across the entire AI lifecycle. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Quick reference

The `mlflow.genai.evaluate()` function runs the app against an evaluation dataset using specified scorers and optionally a prediction function or model ID, returning an `EvaluationResult`: ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

```python
def mlflow.genai.evaluate(
    data: Union[pd.DataFrame, List[Dict], mlflow.genai.datasets.EvaluationDataset],
    scorers: list[mlflow.genai.scorers.Scorer],
    predict_fn: Optional[Callable[..., Any]] = None,
    model_id: Optional[str] = None,
) -> mlflow.models.evaluation.base.EvaluationResult:
```

For full parameter details, see the #Parameters section below or the [MLflow Python API documentation](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate). ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## When to use

The evaluation harness is appropriate for several recurring quality assurance scenarios: ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

- Nightly or weekly checks of the app against curated evaluation datasets
- Validating prompt or model changes across app versions
- Before a release or pull request to prevent quality regressions

## Requirements

1. Install MLflow and required packages:
   ```bash
   pip install --upgrade "mlflow[databricks]>=3.1.0" openai "databricks-connect>=16.1"
   ```
2. Create an MLflow experiment by following the setup environment quickstart. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

### (Optional) Configure parallelization

MLflow by default uses a background thread pool to speed up evaluation. To configure the number of workers, set the environment variable `MLFLOW_GENAI_EVAL_MAX_WORKERS`: ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

```bash
export MLFLOW_GENAI_EVAL_MAX_WORKERS=10
```

## Evaluation modes

There are two evaluation modes: ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

### Direct evaluation (recommended)

MLflow calls the GenAI app directly to generate and evaluate traces. In this mode, MLflow: ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

1. Runs the app on test inputs, capturing [[MLflow Trace|traces (MLflow)|traces]].
2. Applies scorers or LLM judges to assess quality, creating feedback assessments.
3. Stores results in an [Evaluation Run](/concepts/evaluation-run.md) in the active MLflow experiment.

The app entry point is passed as a Python function (`predict_fn`), or, if the app is deployed as a Databricks Model Serving endpoint, that endpoint can be wrapped in `to_predict_fn`. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

By calling the app directly, this mode reuses the same scorers defined for offline evaluation in production monitoring, since the resulting traces are identical in structure. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

#### Example

```python
import mlflow
from mlflow.genai.scorers import RelevanceToQuery, Safety

@mlflow.trace
def my_chatbot_app(question: str) -> dict:
    if "MLflow" in question:
        response = "MLflow is an open-source platform for managing ML and GenAI workflows."
    else:
        response = "I can help you with MLflow questions."
    return {"response": response}

results = mlflow.genai.evaluate(
    data=[
        {"inputs": {"question": "What is MLflow?"}},
        {"inputs": {"question": "How do I get started?"}}
    ],
    predict_fn=my_chatbot_app,
    scorers=[RelevanceToQuery(), Safety()]
)
```

^[evaluate-genai-apps-during-development-databricks-on-aws.md]

### Answer sheet evaluation

Use this mode when the app cannot run directly during evaluation, such as when evaluating pre-computed outputs from external systems, historical traces, or batch jobs. The user provides inputs and outputs, and `evaluate()` runs scorers and logs an evaluation run. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

Answer sheet evaluation can accept inputs and pre-computed outputs or existing traces. If inputs and pre-computed outputs are provided, `mlflow.genai.evaluate()` constructs traces from them. For both input options, MLflow runs the scorers on the traces and outputs feedback from the scorers. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

#### Example using inputs and outputs

```python
import mlflow
from mlflow.genai.scorers import Safety, RelevanceToQuery

results_data = [
    {
        "inputs": {"question": "What is MLflow?"},
        "outputs": {"response": "MLflow is an open-source platform for managing machine learning workflows..."}
    },
    {
        "inputs": {"question": "How do I get started?"},
        "outputs": {"response": "To get started with MLflow, install it using 'pip install mlflow'..."}
    }
]

evaluation = mlflow.genai.evaluate(
    data=results_data,
    scorers=[Safety(), RelevanceToQuery()]
)
```

^[evaluate-genai-apps-during-development-databricks-on-aws.md]

#### Example using existing traces

```python
import mlflow

traces = mlflow.search_traces(
    filter_string="trace.status = 'OK'",
)

evaluation = mlflow.genai.evaluate(
    data=traces,
    scorers=[Safety(), RelevanceToQuery()]
)
```

^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Rate limiting model calls

When evaluating models with rate limits, wrap the predict function with rate-limiting logic. This example uses the `ratelimit` library: ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.scorers import RelevanceToQuery, Safety
from ratelimit import limits, sleep_and_retry

predict_fn = mlflow.genai.to_predict_fn("endpoints:/databricks-gpt-oss-20b")

@sleep_and_retry
@limits(calls=10, period=60)
def rate_limited_predict_fn(*args, **kwargs):
    return predict_fn(*args, **kwargs)

results = mlflow.genai.evaluate(
    data=[{"inputs": {"messages": [{"role": "user", "content": "How does MLflow work?"}]}}],
    predict_fn=predict_fn,
    scorers=[RelevanceToQuery(), Safety()]
)
```

## Viewing results in the UI

An evaluation run is a test report that captures everything about how the app performed on a specific dataset. It contains a trace for each row in the evaluation dataset annotated with feedback from each judge. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

To view results: ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

1. Click **Experiments** in the sidebar to display the Experiments page.
2. Click the experiment name to open it.
3. In the left sidebar, click **Evaluation runs**. The right pane shows a table of traces.
4. To see the rationale for a **Pass** or **Fail** label, hover over the label.
5. To see full trace details, click the request identifier in the **Request** column.
6. Add feedback or expectations to a response using the Assessments pane.

## Parameters

### `data`

The evaluation dataset must be in one of the following formats: ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

- `EvaluationDataset` (recommended)
- List of dictionaries
- Pandas DataFrame
- Spark DataFrame

Databricks recommends using an `EvaluationDataset` as it enforces schema validation and tracks the lineage of each record. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

### `scorers`

List of quality metrics to apply. You can provide: ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

- Built-in scorers such as `RelevanceToQuery` and `Safety`
- Custom scorers

### `predict_fn`

The GenAI app's entry point, used only with direct evaluation. `predict_fn` must: ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

- Accept the keys from the `inputs` dictionary in `data` as keyword arguments
- Return a JSON-serializable dictionary
- Be instrumented with [MLflow Tracing](/concepts/mlflow-tracing.md)
- Emit exactly one trace per call

### `model_id`

Optional model identifier to link results to the app version (for example, `"models:/my-app/1"`). ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Relationship to production monitoring

The same scorers used in the evaluation harness can be scheduled in production using `mlflow.genai.Scorer.start()`. This allows running scorers on production traces to continuously monitor quality. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Related concepts

- [Traces (MLflow)](/concepts/trace-tags-mlflow.md) — Execution logs that capture app inputs, outputs, and intermediate steps
- [[Scorers]] — Functions that analyze trace quality and create feedback assessments
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Curated test case collections for systematic testing
- [Evaluation Runs](/concepts/evaluation-runs.md) — Results of testing an app version against a dataset
- Feedback (MLflow) — Quality assessments attached to traces
- [Production quality monitoring](/concepts/production-monitoring.md) — Scheduling scorers on production traces
- [LLM Judges](/concepts/llm-judges.md) — SDK functions that evaluate text based on specific criteria
- [MLflow experiments](/concepts/mlflow-experiment.md) — Containers that organize all GenAI application data

## Sources

- concepts-data-model-databricks-on-aws.md
- evaluate-genai-apps-during-development-databricks-on-aws.md

# Citations

1. [evaluate-genai-apps-during-development-databricks-on-aws.md](/references/evaluate-genai-apps-during-development-databricks-on-aws-373c1693.md)
