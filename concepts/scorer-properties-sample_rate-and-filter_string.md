---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fa4d9c2cd199c25eeeed4a027b86dfee3496c9c4e0aa09eb68be83ce3fa25667
  pageDirectory: concepts
  sources:
    - scorer-lifecycle-management-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorer-properties-sample_rate-and-filter_string
    - filter_string) and Scorer Properties (sample_rate
    - SP(AF
  citations:
    - file: scorer-lifecycle-management-api-reference-databricks-on-aws.md
title: Scorer Properties (sample_rate and filter_string)
description: Instance attributes sample_rate (0.0-1.0) and filter_string that reflect the current sampling configuration of an active or stopped scorer
tags:
  - mlflow
  - properties
  - scorers
timestamp: "2026-06-19T20:19:35.856Z"
---

# Scorer Properties (sample_rate and filter_string)

**Scorer Properties** refer to the configurable attributes that control how [[Scorers]] evaluate production traces in MLflow. The two primary properties are `sample_rate` and `filter_string`, which together define the sampling behavior for online evaluation of GenAI Applications.

## Overview

When a [[Scorers|Scorer]] is started or updated, it accepts a [ScorerSamplingConfig](/concepts/scorersamplingconfig.md) object that defines both `sample_rate` and `filter_string` properties. These properties determine which traces are selected for evaluation and how frequently they are sampled. Both properties can be read from any [[Scorers|Scorer]] instance and are persisted with the scorer's server-side registration. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## sample_rate

The `sample_rate` property controls the fraction of traces that a scorer evaluates, expressed as a floating-point value between 0.0 and 1.0. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

- A `sample_rate` of `1.0` (the default) means 100% of eligible traces are evaluated.
- A `sample_rate` of `0.0` indicates the scorer is stopped (inactive).
- Intermediate values, such as `0.5`, evaluate 50% of eligible traces.

When a [[Scorers|Scorer]] is stopped via `Scorer.stop()`, its `sample_rate` is set to `0.0`, but the scorer remains registered and can be restarted with a new sampling configuration. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

### Accessing the sample_rate

The current sampling rate is available as a read-only property on any Scorer instance:

```python
print(f"Sampling {scorer.sample_rate * 100}% of traces")
``` ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## filter_string

The `filter_string` property specifies an optional MLflow Trace Filter that restricts which traces are eligible for scoring. When set, only traces matching the filter expression are considered for evaluation. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

### Example filter usage

```python
filter_string="trace.status = 'OK'"
``` ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

This filter selects only traces with a status of `'OK'` for evaluation. The filter is applied before the `sample_rate` is used for probabilistic sampling.

### Accessing the filter_string

The current filter string is available as a read-only property:

```python
print(f"Filter: {scorer.filter_string}")
``` ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

If no filter was configured, the property returns `None`.

## Setting Properties via ScorerSamplingConfig

Both properties are set together through the [ScorerSamplingConfig](/concepts/scorersamplingconfig.md) data class, which is passed to `Scorer.start()` and `Scorer.update()`:

```python
from mlflow.genai import ScorerSamplingConfig

config = ScorerSamplingConfig(
    sample_rate=0.5,
    filter_string="trace.status = 'OK'"
)
``` ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

The `Scorer.update()` method creates a new [[Scorers|Scorer]] instance with the updated configuration. The original scorer remains unchanged, making the update operation immutable. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Listing Properties Across Scorers

Use `mlflow.genai.scorers.list_scorers()` to enumerate all registered scorers for the current experiment and inspect their properties:

```python
from mlflow.genai.scorers import list_scorers

all_scorers = list_scorers()
for scorer in all_scorers:
    print(f"Name: {scorer._server_name}")
    print(f"Sample rate: {scorer.sample_rate}")
    print(f"Filter: {scorer.filter_string}")
``` ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Property Behavior Summary

| Property | Type | Range | Default | Description |
|---|---|---|---|---|
| `sample_rate` | float | 0.0 – 1.0 | 1.0 | Fraction of filtered traces to evaluate |
| `filter_string` | str or None | — | None | MLflow trace filter expression |

When a scorer has `filter_string=None`, all traces are eligible for sampling (subject to the `sample_rate`). When both properties are set, the filter is applied first, then the sample rate determines how many matching traces to evaluate. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Related Concepts

- [Scorer Lifecycle Management](/concepts/scorer-lifecycle-management.md) — Register, start, update, and stop scorers
- [Scorer Sampling Config](/concepts/scorersamplingconfig.md) — Data class for specifying sampling behavior
- [Production Monitoring](/concepts/production-monitoring.md) — Continuous quality assessment in production
- MLflow Trace Filters — Filter expression syntax for trace selection
- [Metric Backfill](/concepts/metric-backfill.md) — Evaluating scorers on historical traces

## Sources

- scorer-lifecycle-management-api-reference-databricks-on-aws.md

# Citations

1. [scorer-lifecycle-management-api-reference-databricks-on-aws.md](/references/scorer-lifecycle-management-api-reference-databricks-on-aws-55d28735.md)
