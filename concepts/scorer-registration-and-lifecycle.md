---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f693a043006db469fed1c3fa2d6d148534251f4be870b7bf4f033738bc686771
  pageDirectory: concepts
  sources:
    - backfill-historical-traces-with-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorer-registration-and-lifecycle
    - Lifecycle and Scorer Registration
    - SRAL
  citations:
    - file: backfill-historical-traces-with-scorers-databricks-on-aws.md
title: Scorer Registration and Lifecycle
description: "Two-phase lifecycle pattern for scorers: .register(name=...) to assign a name, then .start(sampling_config=...) to activate the scorer with a sampling configuration."
tags:
  - mlflow
  - lifecycle
  - scorers
  - registration
timestamp: "2026-06-19T09:08:22.725Z"
---

# Scorer Registration and Lifecycle

**Scorer Registration and Lifecycle** describes the steps required to create, register, start, and use scorers for evaluating [MLflow](/concepts/mlflow.md) GenAI traces and outputs. A scorer is a function or judge that computes a metric (e.g., safety score, response length) on model outputs. Its lifecycle consists of registration, starting, and subsequent usage in evaluation or backfill tasks.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Overview

Scorers can be created from built-in judges (like a `Safety` judge) or custom functions decorated with `@scorer`. After instantiation, a scorer must be registered with a unique name before it can be started. Starting configures its sampling behavior and makes it available for scoring runs or traces. Once started, the scorer can be referenced in backfill operations or online evaluation.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Registration

Registration assigns a human-readable name to the scorer object. This is done by calling `.register(name=...)` on the scorer instance. The name is used to identify the scorer in logs, dashboards, and API calls.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
safety_judge = safety_judge.register(name="safety_check")
response_length = response_length.register(name="response_length")
```

Registration is a required step before starting a scorer.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Starting a Scorer

After registration, the scorer must be started by calling `.start(sampling_config=...)`. The `sampling_config` is a `ScorerSamplingConfig` object that defines the sample rate (`sample_rate`) at which the scorer is applied to traces.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import ScorerSamplingConfig

safety_judge = safety_judge.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)
response_length = response_length.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)
```

The `sample_rate` is a float between 0 and 1 that determines the proportion of traces the scorer will evaluate. Starting a scorer makes it active for the experiment or backfill operation.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Custom Scorers with the `@scorer` Decorator

User-defined metrics can be created as custom scorers using the `@scorer` decorator. The decorator accepts an `aggregations` parameter that specifies how the metric is aggregated across traces (e.g., `"mean"`, `"min"`, `"max"`). The function receives the `outputs` (and optionally `inputs` or `trace`) and returns a numeric score.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer

@scorer(aggregations=["mean", "min", "max"])
def response_length(outputs):
    """Measure response length in characters"""
    return len(outputs)
```

Custom scorers follow the same registration and starting lifecycle as built-in judges.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Using Scorers in Backfill

After a scorer is registered and started, it can be used in backfill operations to score historical traces using `backfill_scorers()`. The function accepts a list of `BackfillScorerConfig` objects, each pairing a started scorer with an optional custom `sample_rate` that overrides the scorer’s own sampling configuration for the backfill.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from databricks.agents.scorers import backfill_scorers, BackfillScorerConfig

custom_scorers = [
    BackfillScorerConfig(scorer=safety_judge, sample_rate=0.8),
    BackfillScorerConfig(scorer=response_length, sample_rate=0.9),
]
job_id = backfill_scorers(
    experiment_id="your-experiment-id",
    scorers=custom_scorers,
    start_time=datetime(2024, 6, 1),
    end_time=datetime(2024, 6, 30),
)
```

The backfill runs asynchronously and returns a job ID. Scorers must be in the started state before being used in `backfill_scorers`.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Lifecycle Summary

| Step | Action | Required? |
|------|--------|-----------|
| Create | Instantiate a judge or define a `@scorer` function | Yes |
| Register | Call `.register(name=...)` to assign a name | Yes, before starting |
| Start | Call `.start(sampling_config=...)` to activate | Yes, before use |
| Use | Pass to `backfill_scorers()` or evaluation APIs | After start |

A scorer cannot be used in evaluation or backfill until it has been both registered and started. Once started, it remains active for the lifetime of the experiment or until stopped.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Related Concepts

- [Backfill Historical Traces with Scorers](/concepts/backfillscorers.md) – Asynchronous scoring of historical runs
- [ScorerSamplingConfig](/concepts/scorersamplingconfig.md) – Controls sample rate for scorer application
- [Safety Judge](/concepts/safety-judge-mlflow.md) – A built-in judge for content safety scoring
- [Custom Scorer](/concepts/custom-scorers-mlflow-genai.md) – User-defined metrics via the `@scorer` decorator
- [GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – Online evaluation workflows that use started scorers

## Sources

- backfill-historical-traces-with-scorers-databricks-on-aws.md

# Citations

1. [backfill-historical-traces-with-scorers-databricks-on-aws.md](/references/backfill-historical-traces-with-scorers-databricks-on-aws-a980dd23.md)
