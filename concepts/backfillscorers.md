---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b9442c48cd554d79e8c77b05a19bce44a6409fee69eb212a5751d91c4e987d5b
  pageDirectory: concepts
  sources:
    - backfill-historical-traces-with-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - backfillscorers
  citations:
    - file: backfill-historical-traces-with-scorers-databricks-on-aws.md
title: BackfillScorers
description: A Databricks function that applies scorers to historical trace data over a specified time range, returning a job ID.
tags:
  - databricks
  - mlflow
  - evaluation
timestamp: "2026-06-18T14:31:21.725Z"
---

Here is the wiki page for "BackfillScorers".

---

## BackfillScorers

**BackfillScorers** refers to the process of applying [[scorers]] to historical traces in an [MLflow Experiment](/concepts/mlflow-experiment.md). This is useful for retroactively evaluating past inference data with newly defined or updated quality judges, enabling consistent assessment across time windows without re-running the original agent workloads. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

### Overview

The `backfill_scorers()` function from `databricks.agents.scorers` allows you to score a range of historical traces by specifying an experiment, a time window, and one or more [[scorers]] with custom sampling configurations. This operation creates scoring jobs that process the stored traces and record the results, which can then be used for monitoring, analysis, or model improvement. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

### Usage

#### BackfillScorerConfig

Each scorer to be backfilled is wrapped in a `BackfillScorerConfig` object, which holds:

- `scorer` – a previously registered and started [[Scorers|scorer]] instance (e.g., a `Safety` judge).
- `sample_rate` – the fraction of traces to score (a float between 0 and 1). This allows you to control which proportion of historical traces are evaluated by each scorer, enabling cost or resource management when backfilling large volumes.

^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

#### The `backfill_scorers()` function

The function accepts the following parameters:

- `experiment_id` – the ID of the experimental endpoint whose traces you want to score.
- `scorers` – a list of [BackfillScorerConfig](/concepts/backfillscorerconfig.md) objects defining the scorers and their sample rates.
- `start_time` – a `datetime` object marking the beginning of the time window for backfilling.
- `end_time` – a `datetime` object marking the end of the time window for backfilling.

It returns a `job_id` that can be used to track the status of the backfill operation. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

### Example

The following example registers and starts two scorers (a safety judge and a response-length metric), then backfills historical traces from June 1 to June 30, 2024 with custom sample rates:

```python
from databricks.agents.scorers import backfill_scorers, BackfillScorerConfig
from datetime import datetime
from mlflow.genai.scorers import Safety, scorer, ScorerSamplingConfig

safety_judge = Safety()
safety_judge = safety_judge.register(name="safety_check")
safety_judge = safety_judge.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)

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

In this example, the safety judge scores 80% of historical traces (overriding its original running sample rate) and the response length metric scores 90% of the traces. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

### Related Concepts

- [[Scorers]] – Functions or judges that evaluate model outputs.
- [BackfillScorerConfig](/concepts/backfillscorerconfig.md) – Configuration object that pairs a scorer with a sample rate for backfill operations.
- [ScorerSamplingConfig](/concepts/scorersamplingconfig.md) – Defines the sampling rate for a running scorer.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – The broader monitoring workflow into which backfilled scores feed.
- [MLflow experiments](/concepts/mlflow-experiment.md) – The organizational unit for traces and evaluation results.

### Sources

- backfill-historical-traces-with-scorers-databricks-on-aws.md

# Citations

1. [backfill-historical-traces-with-scorers-databricks-on-aws.md](/references/backfill-historical-traces-with-scorers-databricks-on-aws-a980dd23.md)
