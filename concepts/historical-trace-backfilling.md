---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cfdec732a06951cd61e71e2a78a971910d176d299200d9becc251ee8370c5c32
  pageDirectory: concepts
  sources:
    - backfill-historical-traces-with-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - historical-trace-backfilling
    - HTB
    - Backfill Historical Traces
    - Backfill Historical Traces with Scorers|backfilling historical traces
    - Backfill historical traces
  citations:
    - file: backfill-historical-traces-with-scorers-databricks-on-aws.md
title: Historical Trace Backfilling
description: The pattern of retrospectively applying evaluation scorers to previously collected trace data over a date range using the backfill_scorers API.
tags:
  - databricks
  - mlflow
  - observability
timestamp: "2026-06-18T14:32:06.075Z"
---

# Historical Trace Backfilling

**Historical Trace Backfilling** is the process of applying [[scorers]] to past GenAI agent traces that were logged without evaluation, generating quality metrics retroactively. This allows teams to establish baselines, compare performance across time periods, or retroactively apply new judges that were developed after the traces were collected.

## Overview

When [Production Monitoring](/concepts/production-monitoring.md) is set up for a GenAI agent, scorers are typically applied to incoming traces in real time or at a defined sampling rate. In some cases, however, traces from an earlier period may not have been scored — either because no scorers were configured at the time or because a new evaluation criterion was developed later. Historical trace backfilling solves this by running the desired scorers against all traces in a specified time window. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

The backfill operation creates a new evaluation job that replays the scorers over the historical traces and stores the results, making them visible in the monitoring dashboard and available for comparison with current scores. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## API Reference: `backfill_scorers`

The primary interface for backfilling is the `backfill_scorers` function from `databricks.agents.scorers`.

### Required Parameters

| Parameter     | Type               | Description                                                                 |
|---------------|--------------------|-----------------------------------------------------------------------------|
| `experiment_id` | `str`            | The [MLflow Experiment](/concepts/mlflow-experiment.md) whose traces should be backfilled.                |
| `scorers`       | `list[BackfillScorerConfig]` | A list of scorer configurations, each specifying a registered scorer and its sample rate for the backfill. |
| `start_time`    | `datetime`       | The start of the time window to backfill (inclusive).                       |
| `end_time`      | `datetime`       | The end of the time window to backfill (exclusive).                         |

^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

The function returns a `job_id` that can be used to track the progress of the backfill operation. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

### `BackfillScorerConfig`

Each entry in the `scorers` list is a `BackfillScorerConfig` object with:

- `scorer` — A registered [[Scorers|scorer]] instance (e.g., a safety judge or response-length metric).
- `sample_rate` — A float between 0.0 and 1.0 indicating the fraction of historical traces to score with this scorer.

Setting different sample rates for different scorers allows you to balance compute cost against coverage for each evaluation criterion. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Prerequisites

Before backfilling, each scorer must be:

1. **Registered** — The scorer must have been previously deployed using its `.register()` method.
2. **Started** — The scorer must be in the `running` state via its `.start()` method, so it is available to process traces.

^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Example

The following example backfills a safety judge (checking for harmful content) and a response length metric across all traces logged in June 2024 for a given experiment. The safety judge is applied to 80% of traces, and the response length scorer to 90% of traces.

```python
from databricks.agents.scorers import backfill_scorers, BackfillScorerConfig
from datetime import datetime
from mlflow.genai.scorers import Safety, scorer, ScorerSamplingConfig

safety_judge = Safety()
safety_judge = safety_judge.register(name="safety_check")
safety_judge = safety_judge.start(sampling_config=ScorerSamplingConfig(sample_rate=0.5))

@scorer(aggregations=["mean", "min", "max"])
def response_length(outputs):
    """Measure response length in characters"""
    return len(outputs)

response_length = response_length.register(name="response_length")
response_length = response_length.start(sampling_config=ScorerSamplingConfig(sample_rate=0.5))

# Define custom sample rates for backfill
custom_scorers = [
    BackfillScorerConfig(scorer=safety_judge, sample_rate=0.8),
    BackfillScorerConfig(scorer=response_length, sample_rate=0.9)
]

job_id = backfill_scorers(
    experiment_id=YOUR_EXPERIMENT_ID,
    scorers=custom_scorers,
    start_time=datetime(2024, 6, 1),
    end_time=datetime(2024, 6, 30)
)
```

^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Use Cases

- **New judge deployment** — After developing a custom judge (e.g., for issue resolution quality), backfill it on recent traces to see how the agent performed historically before the judge existed.
- **A/B baseline comparison** — Before running an [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md), backfill existing scorers on a pre-change time window to establish a baseline.
- **Metric recalculation** — When a scoring function (e.g., response length) is improved or its aggregation logic changes, backfill the new version over old traces for consistency.
- **Compliance auditing** — Retroactively apply safety or privacy judges to verify that historical agent behavior met policy standards.

## Related Concepts

- [[Scorers]] — The base abstraction for evaluating GenAI agent outputs
- [BackfillScorerConfig](/concepts/backfillscorerconfig.md) — Configuration object for specifying scorer and sample rate
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Ongoing evaluation of live agent traces
- [Custom Judges](/concepts/custom-judges.md) — Creating new scorers tailored to specific quality criteria
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit that groups related traces

## Sources

- backfill-historical-traces-with-scorers-databricks-on-aws.md

# Citations

1. [backfill-historical-traces-with-scorers-databricks-on-aws.md](/references/backfill-historical-traces-with-scorers-databricks-on-aws-a980dd23.md)
