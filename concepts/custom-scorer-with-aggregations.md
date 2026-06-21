---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3a7e6e30d078ff666938e53ab26518064ab1029242fd8c2236d220451b42c7ee
  pageDirectory: concepts
  sources:
    - backfill-historical-traces-with-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-scorer-with-aggregations
    - CSWA
  citations:
    - file: backfill-historical-traces-with-scorers-databricks-on-aws.md
title: Custom Scorer with Aggregations
description: Pattern to define user-defined evaluation scorers using the @scorer decorator with aggregate statistics like mean, min, and max.
tags:
  - mlflow
  - custom-evaluation
  - aggregation
timestamp: "2026-06-19T22:12:41.618Z"
---

---
title: Custom Scorer with Aggregations
summary: A user-defined scoring function in MLflow that computes aggregate statistics (mean, min, max) across model outputs, decorated with the `@scorer` decorator and registered as a named scorer.
sources:
  - backfill-historical-traces-with-scorers-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T17:39:55.092Z"
updatedAt: "2026-06-19T17:39:55.092Z"
tags:
  - mlflow
  - custom-scoring
  - aggregations
  - genai
aliases:
  - custom-scorer-with-aggregations
  - CSWA
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Custom Scorer with Aggregations

A **Custom Scorer with Aggregations** is a user-defined function that scores model outputs and automatically computes aggregate statistics — such as mean, minimum, and maximum — across those outputs. These scorers are created using the `@scorer` decorator from `mlflow.genai.scorers` and can be registered as named scorers, started with a [Scorer Sampling Configuration](/concepts/scorer-sampling-configuration.md), and used in workflows like backfilling historical traces. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Defining a Custom Scorer with Aggregations

To define a custom scorer with aggregations, apply the `@scorer` decorator to a function that accepts model outputs and returns a numeric value. The `aggregations` parameter of the decorator specifies which aggregate functions should be computed across all scored outputs in a batch or time window. In the following example, the `response_length` scorer measures the length of a model's response in characters and requests three aggregate statistics: `"mean"`, `"min"`, and `"max"`. These aggregations are computed automatically when the scorer is evaluated. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
@scorer(aggregations=["mean", "min", "max"])
def response_length(outputs):
    """Measure response length in characters"""
    return len(outputs)
```

## Registration and Sampling

After defining the scorer, it must be registered with a name and started with a sampling configuration. The sampling configuration controls the fraction of traces to which the scorer is applied. In the source example, `response_length` is registered as `"response_length"` and started with a sample rate of 0.5 (50% of traces). ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
response_length = response_length.register(name="response_length")
response_length = response_length.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)
```

## Use in Backfill

Custom scorers with aggregations can be passed to the `backfill_scorers()` function to compute scores and their aggregates over a historical time window. Each scorer is wrapped in a [BackfillScorerConfig](/concepts/backfillscorerconfig.md) that can optionally override the sampling rate for the backfill operation. In the following example, `safety_judge` and `response_length` are configured with higher sample rates for the backfill period. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

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

When the backfill job runs, MLflow evaluates the scorer on each trace in the time window and computes the declared aggregate statistics (`mean`, `min`, `max`) across all scored outputs. The aggregates can then be used to monitor overall model behavior over the backfill period. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Related Concepts

- [Scorer Sampling Configuration](/concepts/scorer-sampling-configuration.md) – Defines the sampling rate for a scorer.
- [BackfillScorerConfig](/concepts/backfillscorerconfig.md) – Wraps a scorer with an optional override sampling rate for backfill operations.
- [Backfill Historical Traces with Scorers](/concepts/backfillscorers.md) – The workflow for applying scorers to past trace data.

## Sources

- backfill-historical-traces-with-scorers-databricks-on-aws.md

# Citations

1. [backfill-historical-traces-with-scorers-databricks-on-aws.md](/references/backfill-historical-traces-with-scorers-databricks-on-aws-a980dd23.md)
