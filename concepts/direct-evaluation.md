---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 29b65e881c1e963650a96ede841bdbee2cea7bcee6b1c07f8594dd721b4730f2
  pageDirectory: concepts
  sources:
    - evaluate-genai-apps-during-development-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - direct-evaluation
  citations:
    - file: evaluate-genai-apps-during-development-databricks-on-aws.md
title: Direct Evaluation
description: An evaluation mode where MLflow calls the GenAI app directly via a predict_fn, generates traces, and applies scorers in parallel to assess quality.
tags:
  - mlflow
  - evaluation
  - tracing
timestamp: "2026-06-19T18:42:31.393Z"
---

# Direct Evaluation

**Direct Evaluation** is the recommended mode for evaluating GenAI applications using `mlflow.genai.evaluate()`. In this mode, MLflow calls your application directly, generates [Traces](/concepts/traces.md), applies [[scorers]] (quality metrics), and stores the results in an [Evaluation Run](/concepts/evaluation-run.md) within the active [MLflow Experiment](/concepts/mlflow-experiment.md).^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Overview

Direct evaluation automates the process of testing a GenAI app against a curated evaluation dataset. Instead of manually running the app and inspecting outputs one by one, MLflow handles execution and scoring in parallel. The workflow is:

1. Run your app on test inputs, capturing traces.
2. Apply scorers or [LLM Judges](/concepts/llm-judges.md) to assess quality, creating feedback annotations.
3. Store results in an Evaluation Run.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

This mode reuses the same scorers defined for offline evaluation in [Production Monitoring](/concepts/production-monitoring.md), ensuring consistency across development and production environments.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## When to Use

Direct evaluation is suitable for:
- Nightly or weekly checks of your app against curated evaluation datasets.
- Validating prompt or model changes across app versions.
- Before a release or pull request to prevent quality regressions.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Requirements

1. Install MLflow and required packages:
   ```bash
   pip install --upgrade "mlflow[databricks]>=3.1.0" openai "databricks-connect>=16.1"
   ```
2. Create an MLflow experiment (see setup your environment quickstart).^[evaluate-genai-apps-during-development-databricks-on-aws.md]

### (Optional) Configure Parallelization

Set the environment variable `MLFLOW_GENAI_EVAL_MAX_WORKERS` to control the number of background worker threads used during evaluation (default is recommended for most cases). Example:
```bash
export MLFLOW_GENAI_EVAL_MAX_WORKERS=10
```
^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Data Formats for Direct Evaluation

The `data` argument must follow the schema consistent with [EvaluationDataset](/concepts/evaluation-dataset.md). Databricks recommends using `EvaluationDataset` objects because they enforce schema validation and track record lineage. Accepted formats: `EvaluationDataset`, list of dictionaries, pandas DataFrame, or Spark DataFrame.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

Each record must contain an `inputs` dictionary whose keys match the keyword arguments expected by the `predict_fn` function. For full schema details, see evaluation dataset reference.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Example Using Direct Evaluation

The following code shows how to evaluate a GenAI app with tracing:

```python
import mlflow
from mlflow.genai.scorers import RelevanceToQuery, Safety

# Your GenAI app with [[mlflow-tracing|MLflow Tracing]]
@mlflow.trace
def my_chatbot_app(question: str) -> dict:
    # Your app logic here
    if "MLflow" in question:
        response = "MLflow is an open-source platform for managing ML and GenAI workflows."
    else:
        response = "I can help you with MLflow questions."
    return {"response": response}

# Evaluate your app
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

## Rate Limiting Model Calls

When your app calls an API with rate limits (e.g., third-party APIs or foundation model endpoints), wrap the `predict_fn` with rate-limiting logic, for example using `ratelimit`:

```python
import mlflow
from mlflow.genai.scorers import RelevanceToQuery, Safety
from ratelimit import limits, sleep_and_retry

predict_fn = mlflow.genai.to_predict_fn("endpoints:/databricks-gpt-oss-20b")

@sleep_and_retry
@limits(calls=10, period=60)  # 10 calls per minute
def rate_limited_predict_fn(*args, **kwargs):
    return predict_fn(*args, **kwargs)

results = mlflow.genai.evaluate(
    data=[{"inputs": {"messages": [{"role": "user", "content": "How does MLflow work?"}]}}],
    predict_fn=predict_fn,
    scorers=[RelevanceToQuery(), Safety()]
)
```

^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Viewing Results in the UI

After running an evaluation, you can view aggregate metrics and inspect individual test cases:

1. Navigate to **Experiments** in the sidebar, then click on your experiment.
2. In the left sidebar, click **Evaluation runs** to see a table of traces.
3. Each row shows a **Pass** or **Fail** label per scorer; hover over the label to see the rationale.
4. Click a request identifier to view the full trace (inputs and outputs for each step). You can also add feedback or expectations there.
5. Use the arrows at the side to step through requests.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Parameters for `mlflow.genai.evaluate()`

Key parameters relevant to direct evaluation:

- **`data`** – Test dataset (see [Data Formats](#data-formats-for-direct-evaluation)).
- **`scorers`** – List of quality metrics (built-in or custom) to apply.
- **`predict_fn`** – The GenAI app's entry point. Required for direct evaluation. Must:
  - Accept the keys from the `inputs` dictionary as keyword arguments.
  - Return a JSON-serializable dictionary.
  - Be instrumented with [MLflow Tracing](/concepts/mlflow-tracing.md).
  - Emit exactly one trace per call.
- **`model_id`** – Optional model identifier (e.g., `"models:/my-app/1"`) for version tracking.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

The function returns `mlflow.models.evaluation.base.EvaluationResult`.

## Comparison with Answer Sheet Evaluation

In contrast to direct evaluation, [Answer Sheet Evaluation](/concepts/answer-sheet-evaluation.md) does not run the app; instead, you provide pre-computed outputs or existing traces, and `evaluate()` scores those. Direct evaluation is recommended because it generates traces identical to those that will appear in production monitoring, enabling consistent scorer reuse.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Related Concepts

- [mlflow.genai.evaluate()](/concepts/mlflowgenaievaluate.md)
- [[Scorers]]
- [Evaluation Dataset](/concepts/evaluation-dataset.md)
- [Evaluation Run](/concepts/evaluation-run.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- Production Quality Monitoring

## Sources

- evaluate-genai-apps-during-development-databricks-on-aws.md

# Citations

1. [evaluate-genai-apps-during-development-databricks-on-aws.md](/references/evaluate-genai-apps-during-development-databricks-on-aws-373c1693.md)
