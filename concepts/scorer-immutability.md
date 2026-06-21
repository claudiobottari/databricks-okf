---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f650b03f5ecc4820a4b677860052a78ad6e2a74fd2d86c55c21dc9fccedcf96b
  pageDirectory: concepts
  sources:
    - manage-production-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorer-immutability
  citations:
    - file: manage-production-scorers-databricks-on-aws.md
title: Scorer Immutability
description: Scorers are immutable objects; every lifecycle operation returns a new scorer instance rather than modifying the original, preventing accidental modifications in production.
tags:
  - mlflow
  - scorer
  - immutability
  - software-design
timestamp: "2026-06-19T19:27:59.706Z"
---

# Scorer Immutability

**Scorer Immutability** is a design principle in MLflow's production monitoring system where scorers — including LLM Judges — are immutable objects. Each lifecycle operation returns a new scorer instance rather than modifying the original. This immutability helps ensure that scorers meant for production are not accidentally modified. ^[manage-production-scorers-databricks-on-aws.md]

## Overview

Scorers are immutable objects. When you update a scorer, an updated copy is created rather than modifying the original. This means that operations such as `.start()`, `.update()`, and `.stop()` all return new scorer instances, leaving the original unchanged. ^[manage-production-scorers-databricks-on-aws.md]

## Immutable Update Pattern

The following example demonstrates how immutability works in practice. When `update()` is called, it returns a new instance with the updated configuration, while the original scorer retains its original settings:

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

## Lifecycle Operations

Scorer lifecycles are centered around [MLflow experiments](/concepts/mlflow-experiment.md). Because scorers are immutable, each lifecycle operation returns a new scorer instance rather than modifying the original. ^[manage-production-scorers-databricks-on-aws.md]

The following example demonstrates a scorer moving through all lifecycle states, with each operation producing a new instance:

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

## Best Practices

- **Use the immutable pattern**: Always assign the results of `.start()`, `.update()`, and `.stop()` to variables. Because these operations return new instances, failing to capture the return value means losing the updated scorer. ^[manage-production-scorers-databricks-on-aws.md]
- **Check the scorer state before operations** using `sample_rate`. ^[manage-production-scorers-databricks-on-aws.md]
- **Understand the difference between `.stop()` and `delete_scorer()`**: `.stop()` sets the sample rate to 0 but preserves registration, while `delete_scorer()` removes the scorer from the server entirely. ^[manage-production-scorers-databricks-on-aws.md]

## Related Concepts

- [Production Monitoring](/concepts/production-monitoring.md) — The system that uses scorers to evaluate model outputs.
- [LLM Judges](/concepts/llm-judges.md) — A type of scorer that evaluates language model outputs.
- [Scorer Lifecycle Management](/concepts/scorer-lifecycle-management.md) — The full API for managing scorers through their lifecycle.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit around which scorer lifecycles are centered.

## Sources

- manage-production-scorers-databricks-on-aws.md

# Citations

1. [manage-production-scorers-databricks-on-aws.md](/references/manage-production-scorers-databricks-on-aws-ae58ef30.md)
