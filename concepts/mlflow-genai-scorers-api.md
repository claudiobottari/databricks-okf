---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d5158c71efef504ec89c1912216c87e0f2b58fcfbd1af32dccc236c31ff6b6eb
  pageDirectory: concepts
  sources:
    - backfill-historical-traces-with-scorers-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-scorers-api
    - MGSA
  citations:
    - file: backfill-historical-traces-with-scorers-databricks-on-aws.md
title: MLflow GenAI Scorers API
description: Python API within Databricks for registering, starting, and backfilling scorers on MLflow traces, including both built-in and custom scoring functions.
tags:
  - Databricks
  - MLflow
  - API
timestamp: "2026-06-19T14:08:27.836Z"
---

# MLflow GenAI Scorers API

The **MLflow GenAI Scorers API** provides a framework for defining, registering, and running custom quality and safety measurements on GenAI agent outputs. Scorers are reusable evaluation functions that can be applied to production traces (for monitoring) or backfilled on historical data to re-evaluate past agent behavior.

## Overview

Scorers in MLflow GenAI are functions that take one or more fields from an agent’s trace (such as `outputs`, `inputs`, or `trace`) and return a numeric or categorical score. Built-in scorers like [Safety Scorer](/concepts/safety-scorer-in-mlflow.md) automate common safety checks, while the `@scorer` decorator lets you create domain-specific metrics.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

Scorers support **aggregations** (e.g., `mean`, `min`, `max`) that are computed over batches of evaluations, making them suitable for dashboards and alerting in production monitoring.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Defining Custom Scorers

Use the `@scorer` decorator from `mlflow.genai.scorers` to wrap a Python function as a scorer. The decorator accepts an `aggregations` list that defines how individual scores are aggregated across multiple traces.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer

@scorer(aggregations=["mean", "min", "max"])
def response_length(outputs):
    """Measure response length in characters"""
    return len(outputs)
```

The function receives the `outputs` field from each agent trace by default. You can design scorers that inspect other trace fields or metadata by accepting the appropriate keyword arguments.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Registering and Starting Scorers

After defining a scorer, you must **register** it with a name and then **start** it to activate its collection on live traces. Registration makes the scorer known to the MLflow tracking server; starting it begins sampling agent responses for evaluation.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
# Register the scorer
response_length = response_length.register(name="response_length")

# Start the scorer with a sampling configuration
response_length = response_length.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)
```

Starting a scorer is required for both production monitoring and backfill scenarios. Once started, the scorer will be invoked on a sampled subset of subsequent agent traces.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Sampling Configuration

The `ScorerSamplingConfig` class controls the fraction of traces that a scorer processes. The `sample_rate` parameter (a float between 0 and 1) determines the proportion of traces to score.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import ScorerSamplingConfig

config = ScorerSamplingConfig(sample_rate=0.5)
```

Sampling allows you to balance computational cost and monitoring granularity. High-volume deployments may use low sample rates for expensive scorers (e.g., LLM-based safety checks) and higher rates for lightweight metrics like response length.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Backfilling Historical Traces

The `backfill_scorers` function from `databricks.agents.scorers` re-runs a set of scorers on traces that were recorded within a specified time window. This is useful when you add a new scorer or update an existing one and want consistent scores across past data.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

Each scorer is configured with a `BackfillScorerConfig` that pairs the scorer instance with a unique sample rate for the backfill (which may differ from the ongoing production rate).^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from datetime import datetime
from databricks.agents.scorers import backfill_scorers, BackfillScorerConfig

scorers_to_backfill = [
    BackfillScorerConfig(scorer=safety_judge, sample_rate=0.8),
    BackfillScorerConfig(scorer=response_length, sample_rate=0.9),
]

job_id = backfill_scorers(
    experiment_id=YOUR_EXPERIMENT_ID,
    scorers=scorers_to_backfill,
    start_time=datetime(2024, 6, 1),
    end_time=datetime(2024, 6, 30),
)
```

The function returns a `job_id` that can be used to monitor the backfill progress or cancel it. The scorers must already be registered and started before they can be used in a backfill.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Related Concepts

- [Safety Scorer](/concepts/safety-scorer-in-mlflow.md) – Built-in scorer for content safety evaluation.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying scorers to continuously evaluate agent quality.
- [Scorer Sampling Config](/concepts/scorersamplingconfig.md) – Controlling the fraction of traces evaluated.
- [Backfill Scorers](/concepts/backfill-scorers.md) – Re-evaluating historical traces with new or updated scorers.
- [MLflow GenAI Agent Evaluation](/concepts/mlflow-agent-evaluation.md) – Offline evaluation using judges, distinct from live scoring.

## Source

- backfill-historical-traces-with-scorers-databricks-on-aws.md

# Citations

1. [backfill-historical-traces-with-scorers-databricks-on-aws.md](/references/backfill-historical-traces-with-scorers-databricks-on-aws-a980dd23.md)
