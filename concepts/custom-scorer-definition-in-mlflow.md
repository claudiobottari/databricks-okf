---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 137b51d38baec77aac531ebb4d07a3904aba4f6cc443f9b578b88da1b10aa86c
  pageDirectory: concepts
  sources:
    - backfill-historical-traces-with-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-scorer-definition-in-mlflow
    - CSDIM
    - Custom Scorer Functions
    - Custom scorer functions
  citations:
    - file: backfill-historical-traces-with-scorers-databricks-on-aws.md
title: Custom Scorer Definition in MLflow
description: Pattern for defining user-provided evaluation functions using the @scorer decorator with aggregation metrics (mean, min, max) for GenAI trace evaluation.
tags:
  - mlflow
  - custom-scorers
  - evaluation
  - decorator
timestamp: "2026-06-19T09:08:21.870Z"
---

# Custom Scorer Definition in MLflow

**Custom Scorer Definition in MLflow** refers to the process of creating user-defined evaluation functions, known as scorers, that can be used to assess model outputs in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) workflows. Scorers are central to production monitoring, offline evaluation, and backfill operations, allowing teams to define quality metrics that go beyond built-in evaluators. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Defining a Custom Scorer

A custom scorer is created by decorating a Python function with the `@scorer` decorator, imported from `mlflow.genai.scorers`. The function must accept an `outputs` parameter (typically a Pandas Series or a list of output strings) and return a value for each observation — often a numeric score or a boolean. The `@scorer` decorator can accept an `aggregations` parameter that specifies how the per‑observation scores should be aggregated over a batch (e.g., `["mean", "min", "max"]`). ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer

@scorer(aggregations=["mean", "min", "max"])
def response_length(outputs):
    """Measure response length in characters"""
    return len(outputs)
```

After defining the function, the scorer must be **registered** with a name using the `.register()` method. Registration makes the scorer available in the MLflow tracking server and assigns it a unique identifier that can be referenced in later operations. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
response_length = response_length.register(name="response_length")
```

### Starting a Scorer for Production Monitoring

Once registered, a scorer can be **started** to begin scoring live inference traces. The `.start()` method accepts a `ScorerSamplingConfig` object that controls the sampling rate — i.e., what fraction of all traces the scorer should evaluate. This allows controlling compute costs while still collecting representative quality signals. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import ScorerSamplingConfig

response_length = response_length.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)
```

The `sample_rate` is a float between 0 and 1. A rate of `0.5` means the scorer will evaluate 50% of all traces produced by the model endpoint.

## Using Custom Scorers in Backfill Operations

Registered and started scorers can be used in backfill workflows to score historical traces. The `backfill_scorers()` function accepts a list of `BackfillScorerConfig` objects, each pairing a scorer instance with an optional `sample_rate` that overrides the scorer’s default rate for the backfill run. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from databricks.agents.scorers import backfill_scorers, BackfillScorerConfig
from datetime import datetime

custom_scorers = [
    BackfillScorerConfig(scorer=response_length, sample_rate=0.9),
]

job_id = backfill_scorers(
    experiment_id="my_experiment_id",
    scorers=custom_scorers,
    start_time=datetime(2024, 6, 1),
    end_time=datetime(2024, 6, 30),
)
```

## Related Concepts

- [Scorer Sampling Configuration](/concepts/scorer-sampling-configuration.md) – Controlling the fraction of traces evaluated.
- [Backfill Historical Traces with Scorers](/concepts/backfillscorers.md) – Applying scorers to past inference data.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Using scorers for continuous quality tracking.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – Offline evaluation with scorers and judges.
- [Scorer Registration](/concepts/scorer-registration-and-registry.md) – How `.register()` makes a scorer identifiable.

## Sources

- backfill-historical-traces-with-scorers-databricks-on-aws.md

# Citations

1. [backfill-historical-traces-with-scorers-databricks-on-aws.md](/references/backfill-historical-traces-with-scorers-databricks-on-aws-a980dd23.md)
