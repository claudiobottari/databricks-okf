---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 97c84e554e07724bd503af7a147d3497c199d07aebc54c7a4ff2ec3b6043e185
  pageDirectory: concepts
  sources:
    - scorer-lifecycle-management-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorersamplingconfig
    - Scorer Sampling Config
    - Scorer sampling config
  citations:
    - file: scorer-lifecycle-management-api-reference-databricks-on-aws.md
    - file: backfill-historical-traces-with-scorers-databricks-on-aws.md
title: ScorerSamplingConfig
description: Data class holding sampling rate and optional filter string configuration for controlling which traces a scorer evaluates
tags:
  - mlflow
  - configuration
  - sampling
timestamp: "2026-06-19T20:19:15.207Z"
---

# ScorerSamplingConfig

**`ScorerSamplingConfig`** is a data class that holds the sampling configuration for a [[Scorers|Scorer]] used in production monitoring of GenAI applications. It controls which traces are evaluated by a scorer and at what rate. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Attributes

`ScorerSamplingConfig` has two attributes:

- `sample_rate` (float, optional): The fraction of traces to evaluate, in the range `0.0` to `1.0`. Defaults to `1.0`. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]
- `filter_string` (str, optional): An [MLflow-compatible filter](/concepts/mlflow.md) string used to select which traces to evaluate. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Usage

`ScorerSamplingConfig` is provided when starting or updating a scorer’s online evaluation lifecycle.

### Starting a scorer

```python
from mlflow.genai.scorers import ScorerSamplingConfig

active_scorer = registered_scorer.start(
    sampling_config=ScorerSamplingConfig(
        sample_rate=0.5,
        filter_string="trace.status = 'OK'"
    ),
)
```

^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

### Updating a scorer

The `update()` method accepts a new `ScorerSamplingConfig`. The update is immutable: it returns a new [[Scorers|Scorer]] instance while leaving the original unchanged.

```python
updated_scorer = active_scorer.update(
    sampling_config=ScorerSamplingConfig(sample_rate=0.8)
)
# Original scorer remains unchanged
print(f"Original: {active_scorer.sample_rate}")  # 0.5
print(f"Updated: {updated_scorer.sample_rate}")   # 0.8
```

^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

### Backfilling historical traces

When performing a [backfill](/concepts/metric-backfill.md) of historical traces using `backfill_scorers()`, individual scorers can be configured with an explicit `sample_rate`. If not supplied, the backfill uses the scorer’s current registered sample rate. The backfill configuration is expressed via `BackfillScorerConfig` rather than `ScorerSamplingConfig`. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from databricks.agents.scorers import backfill_scorers, BackfillScorerConfig
from mlflow.genai.scorers import Safety, ScorerSamplingConfig

safety_judge = Safety().register(name="safety_check")
safety_judge = safety_judge.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)

custom_scorers = [
    BackfillScorerConfig(scorer=safety_judge, sample_rate=0.8),
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

- [[Scorers|Scorer]] – The base class that uses `ScorerSamplingConfig` to control online evaluation.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – The broader workflow that includes scorer lifecycle management.
- [BackfillScorerConfig](/concepts/backfillscorerconfig.md) – Configuration object for backfill jobs; accepts a custom `sample_rate` but not a `filter_string`.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The framework within which scorers and sampling configurations operate.

## Sources

- scorer-lifecycle-management-api-reference-databricks-on-aws.md
- backfill-historical-traces-with-scorers-databricks-on-aws.md

# Citations

1. [scorer-lifecycle-management-api-reference-databricks-on-aws.md](/references/scorer-lifecycle-management-api-reference-databricks-on-aws-55d28735.md)
2. [backfill-historical-traces-with-scorers-databricks-on-aws.md](/references/backfill-historical-traces-with-scorers-databricks-on-aws-a980dd23.md)
