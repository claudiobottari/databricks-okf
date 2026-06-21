---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 59ab66e7475b4011a4cfed955e1c18f97ebb8ddbd9c3d3aabfacf9918b91282c
  pageDirectory: concepts
  sources:
    - evaluate-genai-apps-during-development-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rate-limiting-in-evaluation
    - RLIE
    - rate limiting
  citations:
    - file: evaluate-genai-apps-during-development-databricks-on-aws.md
title: Rate Limiting in Evaluation
description: Technique for wrapping predict functions with rate-limiting logic when evaluating models subject to API rate limits, using libraries like ratelimit.
tags:
  - mlflow
  - evaluation
  - rate-limiting
  - optimization
timestamp: "2026-06-19T10:24:09.049Z"
---

# Rate Limiting in Evaluation

**Rate Limiting in Evaluation** refers to the practice of controlling the frequency of calls made to a GenAI app during offline evaluation with `mlflow.genai.evaluate()`. This is especially important when the app under test uses third-party APIs or foundation model endpoints that enforce call quotas or rate limits.

## Overview

When you evaluate a GenAI application that depends on rate-limited services — such as external LLM APIs or Databricks foundation model endpoints — the evaluation harness may generate requests faster than the service permits, leading to throttling errors or degraded scores. To prevent this, you can wrap the application’s prediction function with rate-limiting logic before passing it to `mlflow.genai.evaluate()`. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Implementation

The recommended approach is to use Python’s `ratelimit` library (or a custom equivalent) to decorate the prediction function with a maximum call rate. The decorators `sleep_and_retry` and `limits` are applied to the wrapped function so that the evaluation waits automatically when the rate is exceeded.

```python
import mlflow
from mlflow.genai.scorers import RelevanceToQuery, Safety
from ratelimit import limits, sleep_and_retry

# Your prediction function, e.g. wrapping a model serving endpoint
predict_fn = mlflow.genai.to_predict_fn("endpoints:/databricks-gpt-oss-20b")

@sleep_and_retry
@limits(calls=10, period=60)  # max 10 calls per minute
def rate_limited_predict_fn(*args, **kwargs):
    return predict_fn(*args, **kwargs)

results = mlflow.genai.evaluate(
    data=[{"inputs": {"messages": [{"role": "user", "content": "How does MLflow work?"}]}}],
    predict_fn=rate_limited_predict_fn,
    scorers=[RelevanceToQuery(), Safety()]
)
```

The `rate_limited_predict_fn` is passed as the `predict_fn` parameter. This ensures that every call to the application during evaluation respects the defined limit. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Controlling Parallelism

In addition to rate-limiting the prediction function, you can control the number of concurrent workers used by the evaluation harness itself. By default, MLflow uses a background thread pool to speed up evaluation. To reduce the number of workers and thus the overall request rate, set the environment variable `MLFLOW_GENAI_EVAL_MAX_WORKERS` before running `mlflow.genai.evaluate()`:

```bash
export MLFLOW_GENAI_EVAL_MAX_WORKERS=10
```

Lowering this value can help avoid hitting rate limits when the prediction function’s own rate limiter is insufficient or when you want a simpler global throttle. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The evaluation harness provided by `mlflow.genai.evaluate()`.
- [Direct Evaluation](/concepts/direct-evaluation.md) – The mode where MLflow calls your app directly.
- [[Scorers]] – Quality metrics applied during evaluation.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Applying the same judges in a production setting where rate limits also apply.
- [Evaluation Datasets](/concepts/evaluation-datasets.md) – Structured test data used in evaluation runs.

## Sources

- evaluate-genai-apps-during-development-databricks-on-aws.md

# Citations

1. [evaluate-genai-apps-during-development-databricks-on-aws.md](/references/evaluate-genai-apps-during-development-databricks-on-aws-373c1693.md)
