---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c90800628dce573ed264537b4b23f73f9c8f160b59c1e099f61443b53270c98
  pageDirectory: concepts
  sources:
    - evaluate-genai-apps-during-development-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rate-limiting-in-genai-evaluation
    - RLIGE
  citations:
    - file: evaluate-genai-apps-during-development-databricks-on-aws.md
title: Rate Limiting in GenAI Evaluation
description: Techniques for controlling API call rates during evaluation, including wrapping predict functions with rate-limit decorators and configuring parallel worker count via environment variables.
tags:
  - mlflow
  - evaluation
  - performance
timestamp: "2026-06-19T18:42:46.965Z"
---

# Rate Limiting in GenAI Evaluation

**Rate Limiting in GenAI Evaluation** refers to techniques for controlling the frequency of calls made to external model endpoints during offline evaluation with `mlflow.genai.evaluate()`—a necessity when the evaluated model or LLM judge API imposes request caps (e.g., third‑party APIs or foundation model endpoints). Proper rate limiting prevents evaluation failures caused by hitting rate limits and ensures fair usage of shared resources. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Why Rate Limiting Is Needed

When evaluating a GenAI application, `mlflow.genai.evaluate()` calls a `predict_fn` (the app’s entry point) for each row in the evaluation dataset. If that function invokes an external model serving endpoint—such as a [Foundation Model API](/concepts/foundation-model-apis.md) or a third‑party LLM—the endpoint may enforce per‑minute or per‑second rate limits. Without rate limiting, evaluation can produce `429 Too Many Requests` errors or be throttled, yielding incomplete results. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Wrapping `predict_fn` with Rate‑Limiting Logic

The recommended approach is to wrap the `predict_fn` with a rate‑limiting decorator. The MLflow documentation provides an example using the `ratelimit` library:

```python
import mlflow
from mlflow.genai.scorers import RelevanceToQuery, Safety
from ratelimit import limits, sleep_and_retry

# Replace with your own predict_fn
predict_fn = mlflow.genai.to_predict_fn("endpoints:/databricks-gpt-oss-20b")

@sleep_and_retry
@limits(calls=10, period=60)  # 10 calls per minute
def rate_limited_predict_fn(*args, **kwargs):
    return predict_fn(*args, **kwargs)

results = mlflow.genai.evaluate(
    data=[{"inputs": {"messages": [{"role": "user", "content": "How does MLflow work?"}]}}],
    predict_fn=predict_fn,
    scorers=[RelevanceToQuery(), Safety()],
)
```

^[evaluate-genai-apps-during-development-databricks-on-aws.md]

Key points:
- `@limits(calls=N, period=seconds)` defines the maximum number of calls in a sliding time window.
- `@sleep_and_retry` causes the thread to sleep until the rate limit resets, then retries the call automatically.
- This pattern works with any `predict_fn`, whether it calls a Databricks [Model Serving](/concepts/model-serving.md) endpoint or an external API.

## Configuring Parallelization (Worker Threads)

By default, MLflow uses a background thread pool to evaluate multiple rows concurrently. The number of workers can be overridden with the environment variable `MLFLOW_GENAI_EVAL_MAX_WORKERS`. Reducing the number of workers may help avoid rate limits when each worker independently calls the rate‑limited function. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

```bash
export MLFLOW_GENAI_EVAL_MAX_WORKERS=10
```

A lower value (e.g., `1`) forces serial execution, guaranteeing that only one rate‑limited call is made at a time. Higher values increase parallelism but may exhaust the rate limit faster if the limit is shared across all workers.

## Best Practices

- **Measure actual rate limits** of the endpoint before setting `calls` and `period`. Many APIs document limits per minute (e.g., 60 calls/min). Use slightly lower values to leave headroom.
- **Combine rate‑limiting with worker control**: if the rate limit is per‑client, a single worker with a conservative limit may be safest. If the limit is per‑API‑key and parallel calls are allowed, use a higher worker count but enforce the per‑worker limit so the aggregate does not exceed the total allowed.
- **Log rate‑limit errors** to detect when the limit is too aggressive or the endpoint has changed its policy.
- **Test with a small dataset** first to validate that the rate‑limited function works without errors.

## Related Concepts

- [Direct Evaluation](/concepts/direct-evaluation.md) – The evaluation mode that calls `predict_fn`.
- [[Scorers]] – Quality metrics applied during evaluation, which may also call LLMs and need their own rate limiting.
- [Answer Sheet Evaluation](/concepts/answer-sheet-evaluation.md) – An evaluation mode that does not call `predict_fn`, and thus may not require rate limiting.
- Production Quality Monitoring – Uses the same scorers in production; rate limiting policies can be reused.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) – The input data that drives the number of calls to `predict_fn`.

## Sources

- evaluate-genai-apps-during-development-databricks-on-aws.md

# Citations

1. [evaluate-genai-apps-during-development-databricks-on-aws.md](/references/evaluate-genai-apps-during-development-databricks-on-aws-373c1693.md)
