---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 63f7d8fe07828e67049d03ccc9e834449f7322547050ec8045602aeb279a9ab4
  pageDirectory: concepts
  sources:
    - scorer-lifecycle-management-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metric-backfill
    - backfill
  citations:
    - file: scorer-lifecycle-management-api-reference-databricks-on-aws.md
title: Metric Backfill
description: backfill_scorers() function to evaluate historical traces by applying scorers to past time windows, returning a job ID for tracking
tags:
  - mlflow
  - backfill
  - monitoring
timestamp: "2026-06-19T20:19:23.401Z"
---

# Metric Backfill

**Metric Backfill** is the process of computing evaluation metrics on historical trace data after a [[Scorers|Scorer]] has been registered and configured. It allows teams to apply quality assessment logic retroactively to past production traces, filling in the gap between when traces were collected and when a scorer was deployed.

## Overview

When a scorer is first registered and started, it begins evaluating new traces as they arrive. However, any traces that were generated before the scorer was active remain unevaluated. Metric backfill addresses this by running the scorer's evaluation logic against a specified historical time range of traces, producing metrics for that period as if the scorer had been running all along. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## The `backfill_scorers()` Function

The primary API for performing a metric backfill is the `backfill_scorers()` function from the `databricks.agents.scorers` module. This function creates a backfill job that evaluates one or more scorers against historical traces. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

### Parameters

All parameters are keyword-only:

- **`experiment_id`** *(str, optional)*: The ID of the experiment containing the traces to backfill. If not provided, uses the current experiment context.
- **`scorers`** *(Union[List[BackfillScorerConfig], List[str]], required)*: The scorers to run during backfill. Can be specified as:
  - A list of `BackfillScorerConfig` objects, each allowing a custom sample rate (if `sample_rate` is not provided, defaults to the registered scorer's sample rate)
  - A list of scorer names (strings), which uses the current sample rates from the experiment's scheduled scorers
  - Cannot be empty
- **`start_time`** *(datetime, optional)*: The start of the time range for backfill evaluation. If not provided, no start time constraint is applied.
- **`end_time`** *(datetime, optional)*: The end of the time range for backfill evaluation. If not provided, no end time constraint is applied.

### Return Value

The function returns a job ID (string) that can be used to track the status of the backfill job. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

### Example Usage

```python
from databricks.agents.scorers import backfill_scorers, BackfillScorerConfig
from datetime import datetime

job_id = backfill_scorers(
    experiment_id="your-experiment-id",
    scorers=[
        BackfillScorerConfig(scorer=safety_scorer, sample_rate=0.8),
        BackfillScorerConfig(scorer=response_length, sample_rate=0.9)
    ],
    start_time=datetime(2024, 1, 1),
    end_time=datetime(2024, 1, 31)
)
```

^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Use Cases

- **New scorer deployment**: When a new quality scorer is added to production monitoring, backfill computes metrics for all existing traces so dashboards and alerts have complete historical data.
- **Scorer updates**: After updating a scorer's logic, backfill can recompute metrics for a historical period to maintain consistency.
- **Compliance and auditing**: Backfill ensures that all traces within a required retention period have been evaluated, even if the scorer was deployed after some traces were collected.

## Related Concepts

- [Scorer Lifecycle Management](/concepts/scorer-lifecycle-management.md) — The full lifecycle of registering, starting, updating, and stopping scorers
- [Production Monitoring](/concepts/production-monitoring.md) — Continuous quality assessment of GenAI applications in production
- [ScorerSamplingConfig](/concepts/scorersamplingconfig.md) — Configuration for controlling which traces a scorer evaluates
- [Trace Evaluation](/concepts/mlflow-trace-based-evaluation.md) — The process of running scorers against individual traces

## Sources

- scorer-lifecycle-management-api-reference-databricks-on-aws.md

# Citations

1. [scorer-lifecycle-management-api-reference-databricks-on-aws.md](/references/scorer-lifecycle-management-api-reference-databricks-on-aws-55d28735.md)
