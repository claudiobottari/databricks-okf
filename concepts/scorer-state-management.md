---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bc45f53cc3e5d4a4ecb61377a90d15b472b5831b92e854f69ee3688da83719cc
  pageDirectory: concepts
  sources:
    - manage-production-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorer-state-management
    - SSM
    - Scorer management
  citations:
    - file: manage-production-scorers-databricks-on-aws.md
title: Scorer State Management
description: Management of scorer states including registration, start (active monitoring), stop (sample rate set to 0, kept registered), update, and deletion from the server.
tags:
  - mlflow
  - scorer
  - state-management
timestamp: "2026-06-19T19:29:33.895Z"
---

# Scorer State Management

**Scorer State Management** refers to the lifecycle operations that control the state of MLflow scorers used for [Production Monitoring](/concepts/production-monitoring.md) in Databricks AI applications. Scorers are immutable objects whose state transitions—registration, starting, updating, stopping, and deletion—each produce new scorer instances rather than modifying existing ones. ^[manage-production-scorers-databricks-on-aws.md]

## Scorer Lifecycle

A scorer's lifecycle is centered around an [MLflow Experiment](/concepts/mlflow-experiment.md). The complete lifecycle state machine consists of the following states and transitions: ^[manage-production-scorers-databricks-on-aws.md]

1. **Registered** — The scorer is created and registered but not yet monitoring.
2. **Started** — The scorer actively monitors inference data according to its sampling configuration.
3. **Updated** — A started scorer receives a new configuration (e.g., changed sample rate), returning a new instance with the updated settings.
4. **Stopped** — The scorer stops monitoring (sets sample rate to 0) but remains registered.
5. **Deleted** — The scorer is removed entirely from the server.

### Lifecycle Example

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

## State Operations

### Register

Scorers are created through the `.register()` method on a scorer class such as `Safety()`. Registration makes the scorer known to the server but does not begin monitoring. ^[manage-production-scorers-databricks-on-aws.md]

### Start

The `.start()` method activates monitoring, requiring a `ScorerSamplingConfig` to define the sampling behavior. ^[manage-production-scorers-databricks-on-aws.md]

### Update

Use the `.update()` method to modify an active scorer's configuration. Because scorers are immutable, `.update()` returns a new scorer instance; the original remains unchanged. This immutability helps ensure that production scorers are not accidentally modified. ^[manage-production-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import get_scorer, ScorerSamplingConfig

safety_judge = get_scorer(name="safety_monitor")
updated_judge = safety_judge.update(
    sampling_config=ScorerSamplingConfig(sample_rate=0.8)
)
print(f"Original sample rate: {safety_judge.sample_rate}")  # Original rate
print(f"Updated sample rate: {updated_judge.sample_rate})     # New rate
```

^[manage-production-scorers-databricks-on-aws.md]

### Stop

The `.stop()` method sets the scorer's sample rate to 0, effectively pausing monitoring. The scorer remains registered and can be restarted later. ^[manage-production-scorers-databricks-on-aws.md]

```python
stopped_scorer = databricks_scorer.stop()
print(f"Sample rate after stop: {stopped_scorer.sample_rate}")  # 0
```

### Restart

A stopped scorer can be restarted using the `.start()` method again with a new sampling configuration. ^[manage-production-scorers-databricks-on-aws.md]

```python
restarted_scorer = stopped_scorer.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)
```

### Delete

The `delete_scorer()` function removes the scorer entirely from the server. Unlike `.stop()`, this operation is destructive and cannot be reversed. ^[manage-production-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import delete_scorer

delete_scorer(name=databricks_scorer.name)
```

## Immutable Design

Scorers, including [LLM Judges](/concepts/llm-judges.md), are immutable objects. Every lifecycle operation—`.start()`, `.update()`, `.stop()`—returns a new scorer instance rather than modifying the original. This design prevents accidental modification of production configurations and ensures traceability of state changes. ^[manage-production-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Safety, ScorerSamplingConfig

original_judge = Safety().register(name="safety")
original_judge = original_judge.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.3)
)

# Update returns new instance
updated_judge = original_judge.update(
    sampling_config=ScorerSamplingConfig(sample_rate=0.8)
)

print(f"Original: {original_judge.sample_rate}")  # 0.3
print(f"Updated: {updated_judge.sample_rate}")     # 0.8
```

^[manage-production-scorers-databricks-on-aws.md]

## Best Practices

- Check the scorer state before operations by inspecting the `sample_rate` attribute. A sample rate of 0 indicates a stopped scorer. ^[manage-production-scorers-databricks-on-aws.md]
- Always assign the results of `.start()`, `.update()`, and `.stop()` to variables to capture the new instance returned by these immutable operations. ^[manage-production-scorers-databricks-on-aws.md]
- Understand the difference between `.stop()` (preserves registration for future restart) and `delete_scorer()` (removes the scorer entirely). ^[manage-production-scorers-databricks-on-aws.md]

## Listing Scorers

To view all registered scorers for an experiment, use `list_scorers()`: ^[manage-production-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import list_scorers

scorers = list_scorers()
for scorer in scorers:
    print(f"Name: {scorer.name}")
    print(f"Sample rate: {scorer.sample_rate}")
    print(f"Filter: {scorer.filter_string}")
```

## Related Concepts

- [Production Monitoring](/concepts/production-monitoring.md) — Setting up monitoring for GenAI applications in production
- [LLM Judges](/concepts/llm-judges.md) — Pre-built and custom judges used as scorers
- [Scorer Sampling Configuration](/concepts/scorer-sampling-configuration.md) — Configuration governing how scorers sample inference data
- [Backfill Historical Traces](/concepts/historical-trace-backfilling.md) — Applying scorers to historical traces
- 403 PERMISSION_DENIED Serverless Budget Policy Error — An error that can occur when registering scorers due to budget policy misconfiguration

## Sources

- manage-production-scorers-databricks-on-aws.md

# Citations

1. [manage-production-scorers-databricks-on-aws.md](/references/manage-production-scorers-databricks-on-aws-ae58ef30.md)
