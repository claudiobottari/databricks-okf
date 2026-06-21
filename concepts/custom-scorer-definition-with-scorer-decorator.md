---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b03f9409eed18ebbb90984cd8dc4918f1f6dee9861ffab165e64778aecdbbdf6
  pageDirectory: concepts
  sources:
    - backfill-historical-traces-with-scorers-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-scorer-definition-with-scorer-decorator
    - CSDW@D
  citations:
    - file: backfill-historical-traces-with-scorers-databricks-on-aws.md
title: Custom Scorer Definition with @scorer Decorator
description: The pattern of defining custom evaluation functions in MLflow GenAI using the @scorer decorator, including aggregation configuration and manual registration/starting lifecycle.
tags:
  - mlflow
  - python
  - custom-evaluation
timestamp: "2026-06-18T10:52:18.985Z"
---

# Custom Scorer Definition with @scorer Decorator

**Custom scorer definition with the `@scorer` decorator** is a pattern provided by the `mlflow.genai.scorers` module for creating user-defined evaluation scorers for generative AI workloads. These scorers can then be registered, started with a sampling configuration, and used in operations such as backfilling historical traces.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Usage

The `@scorer` decorator is applied to a Python function that defines the scoring logic. The decorator accepts an `aggregations` parameter specifying how to aggregate per‑example scores across a trace or evaluation batch. Supported aggregation functions include `"mean"`, `"min"`, and `"max"`.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

### Defining a Custom Scorer

A custom scorer is a function that receives the `outputs` produced by a generative AI model and returns a numeric value. The function can include a docstring for documentation. Once defined, the function is decorated with `@scorer(aggregations=[...])`.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

**Example** – a scorer that measures response length in characters:

```python
from mlflow.genai.scorers import scorer

@scorer(aggregations=["mean", "min", "max"])
def response_length(outputs):
    """Measure response length in characters"""
    return len(outputs)
```

^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

### Registering and Starting the Scorer

After defining the scorer function, you must register it with a name and then start it with a sampling configuration before it can be used:

```python
from mlflow.genai.scorers import ScorerSamplingConfig

response_length = response_length.register(name="response_length")
response_length = response_length.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)
```

^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

### Sampling Configuration

The `start()` method accepts a `sampling_config` of type `ScorerSamplingConfig`, which defines the proportion of traces or outputs to evaluate (e.g., `sample_rate=0.5` for 50% sampling). This allows controlling the computational cost of scoring while still gathering representative metrics.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Using Custom Scorers for Backfill

Registered and started custom scorers can be used in a [BackfillScorerConfig](/concepts/backfillscorerconfig.md) to backfill historical traces. The `backfill_scorers` function (imported from `databricks.agents.scorers`) accepts a list of `BackfillScorerConfig` objects, each pairing a scorer with an optional override `sample_rate`. This enables re‑scoring historical traces with different sampling rates than the original configuration.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

**Example** – backfilling with custom sample rates:

```python
from databricks.agents.scorers import backfill_scorers, BackfillScorerConfig
from datetime import datetime

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

## Related Concepts

- [MLflow Scoring](/concepts/mlflow-scorers.md) – The broader evaluation framework for ML models.
- [ScorerSamplingConfig](/concepts/scorersamplingconfig.md) – Configuration for sampling rates when scoring.
- [BackfillScorerConfig](/concepts/backfillscorerconfig.md) – Configuration pairing a scorer with a sample rate for backfill operations.
- [Backfill historical traces](/concepts/historical-trace-backfilling.md) – The process of applying scorers to past experiment traces.
- [Safety Scorer](/concepts/safety-scorer-in-mlflow.md) – Another type of scorer (e.g., `Safety`) that can be used alongside custom scorers.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The MLflow sub‑package for generative AI evaluation.

## Sources

- backfill-historical-traces-with-scorers-databricks-on-aws.md

# Citations

1. [backfill-historical-traces-with-scorers-databricks-on-aws.md](/references/backfill-historical-traces-with-scorers-databricks-on-aws-a980dd23.md)
