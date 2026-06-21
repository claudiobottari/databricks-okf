---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 132e489e5eff66fe59829c727a531efece7697f0d0d55372fa466cab8fd21e9f
  pageDirectory: concepts
  sources:
    - backfill-historical-traces-with-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-scorers-mlflow-genai
    - CS(G
    - Custom Scorer (MLflow GenAI)
    - Custom scorers in MLflow
    - Custom Judges (MLflow GenAI)
    - Custom Scorer
    - Custom Scorers
    - Custom Scorers for GenAI Agents
    - Custom Scorers|custom scorers
    - Custom scorer
    - Custom scorer reference
    - Custom scorers
    - custom scorer
    - custom scorer reference
    - custom scorers
  citations:
    - file: backfill-historical-traces-with-scorers-databricks-on-aws.md
title: Custom Scorers (MLflow GenAI)
description: User-defined scoring functions created with the @scorer decorator that compute metrics on model outputs (e.g., response length) and can be registered and started with sampling configs.
tags:
  - MLflow
  - custom-metrics
  - scoring
timestamp: "2026-06-19T14:08:51.242Z"
---

# Custom Scorers (MLflow GenAI)

**Custom Scorers** in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) are user-defined evaluation functions that measure specific aspects of model outputs during inference monitoring. Unlike built-in MLflow scorers, custom scorers allow teams to define bespoke quality metrics tailored to their application domain.

## Overview

Custom scorers play a crucial role in [production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) by enabling teams to track application-specific metrics alongside MLflow’s default evaluation criteria. When registered and started with a [sampling configuration](/concepts/scorer-sampling-configuration.md), custom scorers evaluate model outputs in real time or during backfill operations. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Defining a Custom Scorer

Custom scorers are created using the `@scorer` decorator, which wraps a Python function that processes model outputs and returns a numeric or categorical score: ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer

@scorer(aggregations=["mean", "min", "max"])
def response_length(outputs):
    """Measure response length in characters"""
    return len(outputs)
```

### Aggregations

The `aggregations` parameter specifies how individual scores are aggregated across multiple inference calls (e.g., `"mean"`, `"min"`, `"max"`, `"sum"`). The MLflow platform computes these statistics from all scored outputs to provide dashboards and alerting. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Registration and Lifecycle

A custom scorer must be registered with MLflow before it can score traces. The registration step creates a named endpoint for the scorer within the MLflow experiment: ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
response_length = response_length.register(name="response_length")
```

After registration, the scorer must be **started** to begin processing traces. The `start()` method activates the scorer with a [Scorer Sampling Configuration](/concepts/scorer-sampling-configuration.md): ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
response_length = response_length.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)
```

## Sampling Configuration

The `[ScorerSamplingConfig](/concepts/scorersamplingconfig.md)` controls what fraction of traces the scorer should evaluate. The `sample_rate` parameter takes a value between 0.0 (no evaluation) and 1.0 (evaluate every trace). This allows teams to balance evaluation coverage against compute cost: ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import ScorerSamplingConfig

sampling = ScorerSamplingConfig(sample_rate=0.8)
```

## Backfilling Historical Traces

Custom scorers can be applied retroactively to historical traces using the [BackfillScorers](/concepts/backfillscorers.md) API. This is useful for adding new evaluation criteria to existing data without reprocessing the model: ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from databricks.agents.scorers import backfill_scorers, BackfillScorerConfig
from datetime import datetime

backfill_scorers(
    experiment_id=YOUR_EXPERIMENT_ID,
    scorers=[
        BackfillScorerConfig(scorer=safety_judge, sample_rate=0.8),
        BackfillScorerConfig(scorer=response_length, sample_rate=0.9),
    ],
    start_time=datetime(2024, 6, 1),
    end_time=datetime(2024, 6, 30),
)
```

The `[BackfillScorerConfig](/concepts/backfillscorerconfig.md)` object pairs a registered scorer with a specific sample rate for the backfill operation, allowing fine-grained control over which traces get scored during historical evaluation. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Using Built-In Scorers

In addition to fully custom scorers, MLflow provides built-in scorers like `Safety()` that can be configured, registered, and started using the same lifecycle methods: ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Safety

safety_judge = Safety()
safety_judge = safety_judge.register(name="safety_check")
safety_judge = safety_judge.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)
```

Built-in scorers follow the same registration and sampling patterns as custom scorers, making them interchangeable in monitoring workflows.

## Related Concepts

- [Scorer Sampling Configuration](/concepts/scorer-sampling-configuration.md) — Control over trace evaluation frequency
- [Backfill Scorers](/concepts/backfill-scorers.md) — Applying scorers to historical trace data
- [Backfill Scorer Config](/concepts/backfillscorerconfig.md) — Configuring scorer-specific sample rates for backfill
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Real-time scoring workflows
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational unit for runs and evaluations
- Safety Scorers — Built-in content safety evaluation

## Sources

- backfill-historical-traces-with-scorers-databricks-on-aws.md

# Citations

1. [backfill-historical-traces-with-scorers-databricks-on-aws.md](/references/backfill-historical-traces-with-scorers-databricks-on-aws-a980dd23.md)
