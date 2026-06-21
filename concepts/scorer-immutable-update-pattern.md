---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1650061a5737ad78e8d408429c6944c8c8e1fd36e8d3500d7579fe516a2d99f9
  pageDirectory: concepts
  sources:
    - scorer-lifecycle-management-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorer-immutable-update-pattern
    - SIUP
  citations:
    - file: scorer-lifecycle-management-api-reference-databricks-on-aws.md
title: Scorer Immutable Update Pattern
description: Scorer instances are immutable — update() and stop() return new Scorer instances with modified configuration rather than mutating the original
tags:
  - mlflow
  - immutability
  - pattern
timestamp: "2026-06-19T20:19:48.735Z"
---

# Scorer Immutable Update Pattern

The **Scorer Immutable Update Pattern** is a design principle in [MLflow](/concepts/mlflow.md) GenAI scorers where all lifecycle methods — `register`, `start`, `update`, and `stop` — return new [[Scorers|Scorer]] instances instead of mutating the original object. This pattern enables safe, predictable state management for continuous quality assessment on production traces. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Overview

MLflow scorers run online evaluation on production traces using configurable sampling. Every lifecycle method that changes a scorer’s state (registration, activation, configuration update, or deactivation) produces a fresh `Scorer` instance. The original instance remains unchanged, which prevents accidental side effects and makes it possible to keep a reference to a specific configuration. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## How It Works

The immutable pattern is most visible in the `Scorer.update()` method, which is explicitly documented as an immutable operation:

- `Scorer.update()` takes a `ScorerSamplingConfig` (with `sample_rate` and optional `filter_string`) and returns a **new** `Scorer` instance with the updated configuration. The original scorer is not modified.
- `Scorer.start()` returns a new `Scorer` instance in an active state.
- `Scorer.stop()` returns a new `Scorer` instance with `sample_rate=0`.
- `Scorer.register()` returns a new `Scorer` instance after server registration.

All methods accept an optional `name` parameter; if not provided, the current name of the scorer is used. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

### Example: Updating a Sampling Configuration

```python
active_scorer = registered_scorer.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)

# Update sampling rate (returns new scorer instance)
updated_scorer = active_scorer.update(
    sampling_config=ScorerSamplingConfig(sample_rate=0.8)
)

# Original scorer remains unchanged
print(f"Original: {active_scorer.sample_rate}")  # 0.5
print(f"Updated: {updated_scorer.sample_rate}")   # 0.8
```

^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Benefits

- **Predictability**: A stored reference to a scorer always reflects the configuration that was active when it was obtained.
- **Side-effect safety**: Calling an update on one reference does not affect other references to the same logical scorer.
- **Version tracking**: Each returned instance captures a distinct point in the scorer’s lifecycle, which can simplify auditing or rollback logic.

## Related Concepts

- [Scorer Lifecycle Management](/concepts/scorer-lifecycle-management.md) – The full set of lifecycle methods for scorers.
- [MLflow GenAI monitoring](/concepts/mlflow-genai-production-monitoring.md) – The broader system for monitoring GenAI applications in production.
- [ScorerSamplingConfig](/concepts/scorersamplingconfig.md) – The data class that holds sampling configuration for a scorer.
- Production monitoring on Databricks – The task-based guide for setting up continuous evaluation.

## Sources

- scorer-lifecycle-management-api-reference-databricks-on-aws.md

# Citations

1. [scorer-lifecycle-management-api-reference-databricks-on-aws.md](/references/scorer-lifecycle-management-api-reference-databricks-on-aws-55d28735.md)
