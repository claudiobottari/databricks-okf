---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bd04b99839d8e8b1f6e0e5788c374396f531026e0c7d409f2e8bb8cfbf7a765f
  pageDirectory: concepts
  sources:
    - evaluate-genai-apps-during-development-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - direct-evaluation-mode
    - DEM
  citations:
    - file: evaluate-genai-apps-during-development-databricks-on-aws.md
title: Direct Evaluation Mode
description: Evaluation mode where MLflow calls the GenAI app directly via a predict_fn to generate and evaluate traces, recommended for reusing scorers in production monitoring.
tags:
  - mlflow
  - evaluation
  - tracing
timestamp: "2026-06-19T10:23:47.941Z"
---

# Direct Evaluation Mode

**Direct Evaluation Mode** is a mode of MLflow GenAI evaluation where [`mlflow.genai.evaluate()`](/wiki/mlflow-genai-evaluate) orchestrates the end-to-end assessment by calling your application directly. Instead of providing pre‑computed outputs, you supply a callable entry point (the *predict function*) and the evaluation harness runs your app on each test input, captures the resulting traces, and applies scorers to assess quality — all in a single invocation.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## When to Use

Direct evaluation is the recommended approach for most development workflows, because the traces it produces are identical to those your app would emit in production. This consistency lets you reuse the same scorers across offline testing and [Production Monitoring for GenAI|production monitoring](/concepts/production-monitoring-for-genai-applications.md).^[evaluate-genai-apps-during-development-databricks-on-aws.md]

Use it for:^[evaluate-genai-apps-during-development-databricks-on-aws.md]

- Nightly or weekly checks of your app against curated evaluation datasets.
- Validating the impact of prompt or model changes across app versions.
- Pre‑release or pre‑PR quality validation to prevent regressions.

## How It Works

1. **Input**: You provide an [Evaluation Dataset](/concepts/evaluation-dataset.md) (or a list of dictionaries / DataFrame), a `predict_fn` that wraps your GenAI app, and a list of [[Scorers]] (built‑in or custom LLM judges).
2. **Execution**: For each row in the dataset, MLflow calls `predict_fn` with the fields from the `inputs` dictionary as keyword arguments. The call must be instrumented with [MLflow Tracing](/concepts/mlflow-tracing.md) and must emit exactly one trace per invocation.^[evaluate-genai-apps-during-development-databricks-on-aws.md]
3. **Scoring**: After each call, the captured trace is passed to the specified scorers, which produce feedback (ratings, rationales).^[evaluate-genai-apps-during-development-databricks-on-aws.md]
4. **Logging**: The results — traces, feedback, and aggregate metrics — are stored in an [Evaluation Run](/concepts/evaluation-run.md) in the active MLflow experiment.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

The process runs in parallel across multiple background workers. To control parallelism, set `MLFLOW_GENAI_EVAL_MAX_WORKERS`.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Requirements

The `predict_fn` parameter is required for direct evaluation and must meet the following criteria:^[evaluate-genai-apps-during-development-databricks-on-aws.md]

- Accept the keys from the `inputs` dictionary in the evaluation data as keyword arguments.
- Return a JSON‑serializable dictionary.
- Be instrumented with [MLflow Tracing](/concepts/mlflow-tracing.md) (using the `@mlflow.trace` decorator or the tracing API).
- Emit exactly one trace per call.

Additional setup:

```bash
pip install --upgrade "mlflow[databricks]>=3.1.0" openai "databricks-connect>=16.1"
```

Create an MLflow experiment as described in the [environment setup quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment).^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Example

The following code defines a simple chatbot app, wraps it with [MLflow Tracing](/concepts/mlflow-tracing.md), and runs direct evaluation on two sample inputs using built‑in scorers.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

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

## Rate Limiting Model Calls

When your predict function calls a third‑party API or a foundation model endpoint with rate limits, wrap it with rate‑limiting logic — for example, using the `ratelimit` library — and pass the wrapped function as `predict_fn`.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

```python
from ratelimit import limits, sleep_and_retry

predict_fn = mlflow.genai.to_predict_fn("endpoints:/databricks-gpt-oss-20b")

@sleep_and_retry
@limits(calls=10, period=60)  # 10 calls per minute
def rate_limited_predict_fn(*args, **kwargs):
    return predict_fn(*args, **kwargs)

results = mlflow.genai.evaluate(
    data=[{"inputs": {"messages": [{"role": "user", "content": "How does MLflow work?"}]}}],
    predict_fn=rate_limited_predict_fn,
    scorers=[RelevanceToQuery(), Safety()]
)
```

## Viewing Results in the UI

After an evaluation run completes, you can inspect aggregate metrics and individual trace‑level feedback in the MLflow experiment UI under **Evaluation runs**. Each trace shows ratings from the scorers, and you can drill into any request to see the full trace and add human feedback.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Related Concepts

- [Answer Sheet Evaluation](/concepts/answer-sheet-evaluation.md) — The alternative mode that scores pre‑computed outputs or existing traces.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) — How to build structured test data for direct evaluation.
- [[Scorers]] — Quality metrics (built‑in and custom) applied to traces.
- [Evaluation Runs](/concepts/evaluation-runs.md) — How results are stored and compared across experiments.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Reusing the same scorers in production for continuous monitoring.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Required instrumentation for direct evaluation.

## Sources

- evaluate-genai-apps-during-development-databricks-on-aws.md

# Citations

1. [evaluate-genai-apps-during-development-databricks-on-aws.md](/references/evaluate-genai-apps-during-development-databricks-on-aws-373c1693.md)
