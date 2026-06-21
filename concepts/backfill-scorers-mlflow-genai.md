---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4695176676d408d1c8fc96614dcd1ff234f2cdb9dda12dab5b91c65edd48c993
  pageDirectory: concepts
  sources:
    - backfill-historical-traces-with-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - backfill-scorers-mlflow-genai
    - BS(G
  citations:
    - file: backfill-historical-traces-with-scorers-databricks-on-aws.md
title: Backfill Scorers (MLflow GenAI)
description: Technique for retroactively applying scoring functions to historical trace data within a specified time range using the databricks.agents.scorers.backfill_scorers() API.
tags:
  - mlflow
  - genai
  - evaluation
  - backfill
timestamp: "2026-06-19T09:07:56.369Z"
---

# Backfill Scorers (MLflow GenAI)

**Backfill Scorers** refers to the ability to apply [[scorers]] to historical traces or predictions in an [MLflow Experiment](/concepts/mlflow-experiment.md) for retrospective evaluation. This is part of [MLflow GenAI](/concepts/mlflow-3-for-genai.md)’s production monitoring capabilities, allowing teams to compute quality metrics on past agent responses without re-running inference. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Overview

In production monitoring, scorers (such as safety judges or custom metrics) are typically applied in real time or on recent predictions. However, there are scenarios where you need to evaluate a new scorer against past data — for example, to test a new safety judge against historical traces or to backfill a custom metric like response length. The `backfill_scorers()` function enables this by processing existing traces within a specified time window. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Usage

The `backfill_scorers()` function is imported from `databricks.agents.scorers`. It accepts an experiment ID, a list of scorer configurations, and a date range. The function returns a job ID that can be used to monitor the backfill progress.

### Example

```python
from databricks.agents.scorers import backfill_scorers, BackfillScorerConfig
from datetime import datetime
from mlflow.genai.scorers import Safety, scorer, ScorerSamplingConfig

# Register and start a safety judge
safety_judge = Safety()
safety_judge = safety_judge.register(name="safety_check")
safety_judge = safety_judge.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)

# Define a custom scorer for response length
@scorer(aggregations=["mean", "min", "max"])
def response_length(outputs):
    """Measure response length in characters"""
    return len(outputs)

response_length = response_length.register(name="response_length")
response_length = response_length.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)

# Define custom sample rates for backfill
custom_scorers = [
    BackfillScorerConfig(scorer=safety_judge, sample_rate=0.8),
    BackfillScorerConfig(scorer=response_length, sample_rate=0.9),
]

job_id = backfill_scorers(
    experiment_id=YOUR_EXPERIMENT_ID,
    scorers=custom_scorers,
    start_time=datetime(2024, 6, 1),
    end_time=datetime(2024, 6, 30),
)
```

^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `experiment_id` | string | The ID of the [MLflow Experiment](/concepts/mlflow-experiment.md) containing the historical traces. |
| `scorers` | list of `BackfillScorerConfig` | A list of `BackfillScorerConfig` objects, each pairing a registered scorer with a desired sample rate for backfill. The sample rate can differ from the one used during regular monitoring. |
| `start_time` | `datetime` | The beginning of the time window (inclusive) for traces to evaluate. |
| `end_time` | `datetime` | The end of the time window (exclusive) for traces to evaluate. |

The `BackfillScorerConfig` wrapper allows you to specify a `sample_rate` that overrides the scorer’s original sampling configuration for the backfill job only. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Return Value

The function returns a `job_id` (string) that identifies the asynchronous backfill job. This ID can be used to check the job status or cancel the operation through the [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) API or UI. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Prerequisites

- The scorers must be created and started (via `.register()` and `.start()`) before being passed to `backfill_scorers()`. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]
- The experiment must contain logged traces (predictions) within the specified time range.

## Related Concepts

- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Real-time and periodic evaluation of agent responses.
- [[Scorers]] – Functions that compute quality metrics on predictions.
- [Safety Scorer](/concepts/safety-scorer-in-mlflow.md) – A built-in scorer for content safety assessment.
- [Custom Scorers](/concepts/custom-scorers-mlflow-genai.md) – User-defined metrics created with the `@scorer` decorator.
- [Sampling Configurations](/concepts/scorer-sampling-configuration.md) – Controlling which percentage of predictions a scorer evaluates.
- Databricks Agents – The broader framework for deploying and monitoring AI agents.

## Sources

- backfill-historical-traces-with-scorers-databricks-on-aws.md

# Citations

1. [backfill-historical-traces-with-scorers-databricks-on-aws.md](/references/backfill-historical-traces-with-scorers-databricks-on-aws-a980dd23.md)
