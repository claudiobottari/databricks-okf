---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b574cf657d2ff8856ee6a18444251e37b146f95f0285cdd5c2c7d5803f33596a
  pageDirectory: concepts
  sources:
    - manage-production-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorer-lifecycle
    - Trace Lifecycle
  citations:
    - file: manage-production-scorers-databricks-on-aws.md
title: Scorer Lifecycle
description: The lifecycle states and transitions for production scorers in Databricks MLflow, centered around MLflow experiments.
tags:
  - mlflow
  - scorer
  - lifecycle-management
timestamp: "2026-06-19T19:27:56.065Z"
---

# Scorer Lifecycle

The **Scorer Lifecycle** describes the states and operations that a production scorer moves through during its use in [Production Monitoring](/concepts/production-monitoring.md) on Databricks. Scorers are immutable objects — each lifecycle operation returns a new scorer instance rather than modifying the original. ^[manage-production-scorers-databricks-on-aws.md]

## Lifecycle States

A scorer progresses through the following states during its lifecycle:

1. **Registered** — The scorer is created and registered with a name but is not yet actively monitoring.
2. **Started** — The scorer begins monitoring with a configured sampling rate.
3. **Updated** — The scorer's configuration is modified (e.g., changing the sample rate), producing a new immutable instance.
4. **Stopped** — The scorer's sample rate is set to 0, pausing monitoring while preserving the registration.
5. **Deleted** — The scorer is removed from the server entirely.

^[manage-production-scorers-databricks-on-aws.md]

### Lifecycle Example

The following example demonstrates a scorer moving through all lifecycle states:

```python
from mlflow.genai.scorers import Safety, scorer, ScorerSamplingConfig, delete_scorer

# Register → Start → Update → Stop → Delete
safety_judge = Safety().register(name="safety_check")
safety_judge = safety_judge.start(
    sampling_config=ScorerSamplingConfig(sample_rate=1.0),
)
safety_judge = safety_judge.update(
    sampling_config=ScorerSamplingConfig(sample_rate=0.8),
)
safety_judge = safety_judge.stop()
delete_scorer(name="safety_check")
```

^[manage-production-scorers-databricks-on-aws.md]

## Lifecycle Operations

### List Scorers

To view all registered scorers for an experiment, use `list_scorers()`:

```python
from mlflow.genai.scorers import list_scorers

scorers = list_scorers()
for scorer in scorers:
    print(f"Name: {scorer.name}")
    print(f"Sample rate: {scorer.sample_rate}")
    print(f"Filter: {scorer.filter_string}")
    print("---")
```

^[manage-production-scorers-databricks-on-aws.md]

### Get and Update a Scorer

Use `get_scorer()` to retrieve a scorer by name, then `update()` to modify its configuration. Because scorers are immutable, `update()` returns a new instance:

```python
from mlflow.genai.scorers import get_scorer, ScorerSamplingConfig

safety_judge = get_scorer(name="safety_monitor")
updated_judge = safety_judge.update(
    sampling_config=ScorerSamplingConfig(sample_rate=0.8)
)

# The original scorer remains unchanged
print(f"Original sample rate: {safety_judge.sample_rate}")  # Original rate
print(f"Updated sample rate: {updated_judge.sample_rate}")   # New rate
```

^[manage-production-scorers-databricks-on-aws.md]

### Stop and Delete Scorers

Stopping a scorer sets its sample rate to 0 but keeps it registered. Deleting a scorer removes it from the server entirely:

```python
from mlflow.genai.scorers import get_scorer, delete_scorer, ScorerSamplingConfig

databricks_scorer = get_scorer(name="databricks_mentions")

# Stop monitoring (sets sample_rate to 0, keeps scorer registered)
stopped_scorer = databricks_scorer.stop()
print(f"Sample rate after stop: {stopped_scorer.sample_rate}")  # 0

# Restart monitoring from a stopped scorer
restarted_scorer = stopped_scorer.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)

# Or remove scorer entirely from the server
delete_scorer(name=databricks_scorer.name)
```

^[manage-production-scorers-databricks-on-aws.md]

## Immutability

Scorers, including [LLM Judges](/concepts/llm-judges.md), are immutable objects. When you update a scorer, an updated copy is created rather than modifying the original. This immutability helps ensure that scorers meant for production are not accidentally modified:

```python
from mlflow.genai.scorers import Safety, ScorerSamplingConfig

original_judge = Safety().register(name="safety")
original_judge = original_judge.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.3),
)

# Update returns new instance
updated_judge = original_judge.update(
    sampling_config=ScorerSamplingConfig(sample_rate=0.8),
)

# Original remains unchanged
print(f"Original: {original_judge.sample_rate}")  # 0.3
print(f"Updated: {updated_judge.sample_rate}")    # 0.8
```

^[manage-production-scorers-databricks-on-aws.md]

## Best Practices

- Check the scorer state before operations using `sample_rate`.
- Use the immutable pattern: assign the results of `.start()`, `.update()`, and `.stop()` to variables.
- Understand the difference between `.stop()` (preserves registration) and `delete_scorer()` (removes entirely).

^[manage-production-scorers-databricks-on-aws.md]

## Related Concepts

- [Production Monitoring](/concepts/production-monitoring.md) — Setting up monitoring for GenAI applications
- [LLM Judges](/concepts/llm-judges.md) — Scorers used for evaluating model outputs
- [Scorer Sampling Configuration](/concepts/scorer-sampling-configuration.md) — Configuration for controlling sample rates
- [Backfill Historical Traces](/concepts/historical-trace-backfilling.md) — Applying scorers to historical traces
- 403 PERMISSION_DENIED Serverless Budget Policy Error — An error that can occur when registering scorers

## Sources

- manage-production-scorers-databricks-on-aws.md

# Citations

1. [manage-production-scorers-databricks-on-aws.md](/references/manage-production-scorers-databricks-on-aws-ae58ef30.md)
