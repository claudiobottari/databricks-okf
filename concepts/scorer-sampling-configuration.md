---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f5c470dc0c3aff901d814d108a4f840ebde08a75475b26ad5024a7bcae5aeb03
  pageDirectory: concepts
  sources:
    - backfill-historical-traces-with-scorers-databricks-on-aws.md
    - manage-production-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - scorer-sampling-configuration
    - SSC
    - Sampling Configuration
    - Sampling Configurations
    - sampling configuration
  citations:
    - file: manage-production-scorers-databricks-on-aws.md
    - file: backfill-historical-traces-with-scorers-databricks-on-aws.md
title: Scorer Sampling Configuration
description: Mechanism to control what fraction of traces are evaluated by a scorer using ScorerSamplingConfig and sample_rate parameters.
tags:
  - mlflow
  - evaluation
  - sampling
timestamp: "2026-06-19T22:12:34.049Z"
---

```yaml
---
title: Scorer Sampling Configuration
summary: The mechanism to control what fraction of traces a scorer evaluates by setting a sample rate via ScorerSamplingConfig.
sources:
  - backfill-historical-traces-with-scorers-databricks-on-aws.md
  - manage-production-scorers-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:52:18.281Z"
updatedAt: "2026-06-19T17:40:44.405Z"
tags:
  - mlflow
  - sampling
  - scoring
  - configuration
aliases:
  - scorer-sampling-configuration
  - SSC
confidence: 0.9
provenanceState: merged
inferredParagraphs: 2
---

# Scorer Sampling Configuration

**Scorer Sampling Configuration** (`ScorerSamplingConfig`) is a data class in MLflow that defines the fraction of incoming traces a scorer should evaluate, along with an optional filter string to narrow the set of traces before sampling. It is used when starting or updating a scorer to control monitoring cost and coverage.^[manage-production-scorers-databricks-on-aws.md]

## Properties

`ScorerSamplingConfig` has two attributes:

- **`sample_rate`** (float, optional): A value between 0.0 and 1.0 representing the fraction of traces to evaluate. A value of `1.0` evaluates all matching traces; `0.0` evaluates none. The default is `1.0`.^[manage-production-scorers-databricks-on-aws.md]
- **`filter_string`** (str, optional): An MLflow trace filter string that selects which traces to consider before sampling. This uses the same syntax as `mlflow.search_traces()` and can filter on trace attributes such as `attributes.status` or `attributes.timestamp_ms`.^[manage-production-scorers-databricks-on-aws.md]

The configuration is passed to lifecycle methods like `.start()` and `.update()` to govern how a scorer processes traces.^[manage-production-scorers-databricks-on-aws.md]

## Purpose

Sampling control is essential for balancing monitoring coverage with compute cost. By adjusting the sample rate, you can run critical scorers on every trace and expensive scorers on a smaller subset. The filter string further reduces the traces that enter the sampling pipeline.^[manage-production-scorers-databricks-on-aws.md]

## Usage

### Starting a scorer with sampling

When calling `.start()` on a registered scorer, supply a `ScorerSamplingConfig` to define the evaluation behavior:

```python
from mlflow.genai.scorers import Safety, ScorerSamplingConfig

safety_judge = Safety().register(name="safety_check")
safety_judge = safety_judge.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.7)
)
```

^[manage-production-scorers-databricks-on-aws.md]

### Filtering traces before sampling

Combine `filter_string` with `sample_rate` to evaluate only a subset of traces that meet certain criteria:

```python
from mlflow.genai.scorers import Safety, ScorerSamplingConfig

safety_judge = Safety().register(name="safety")
safety_judge = safety_judge.start(
    sampling_config=ScorerSamplingConfig(
        sample_rate=1.0,
        filter_string="attributes.status = 'OK'"
    )
)
```

^[manage-production-scorers-databricks-on-aws.md]

### Updating sampling configuration

Because scorers are [[Scorer lifecycle|immutable]], calling `.update()` returns a new scorer instance with the new sampling configuration. The original scorer remains unchanged.^[manage-production-scorers-databricks-on-aws.md]

```python
updated_judge = active_scorer.update(
    sampling_config=ScorerSamplingConfig(sample_rate=0.8),
)
```

### Backfilling with custom sample rates

When backfilling historical traces, you can provide per-scorer sampling configurations in a `BackfillScorerConfig` object. The `sample_rate` inside overrides the scorer's current setting for the backfill job.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from databricks.agents.scorers import backfill_scorers, BackfillScorerConfig

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

The `sample_rate` in `BackfillScorerConfig` is independent of the scorer's own `ScorerSamplingConfig` and only applies to the backfill run.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Best practices

- **Match sample rate to scorer criticality**: Use `sample_rate=1.0` for safety and security scorers; use lower rates for expensive LLM judges.
- **Leverage filtering to reduce noise**: Combine `filter_string` with sampling to concentrate scoring on specific trace conditions.
- **Respect immutability**: Always assign the result of `.update()` to a new variable.

## Related concepts

- [[Scorer lifecycle]] — The lifecycle management methods (`register`, `start`, `update`, `stop`) that accept sampling configuration.
- [[Production monitoring]] — The system that continuously runs scorers on incoming traces.
- [[Historical Trace Backfilling|Backfill historical traces]] — Applying scorers to past traces with possible custom sampling.
- [[LLM Judges]] — Pre-built or custom scorers that evaluate quality using language models.

## Sources

- backfill-historical-traces-with-scorers-databricks-on-aws.md
- manage-production-scorers-databricks-on-aws.md
```

# Citations

1. [manage-production-scorers-databricks-on-aws.md](/references/manage-production-scorers-databricks-on-aws-ae58ef30.md)
2. [backfill-historical-traces-with-scorers-databricks-on-aws.md](/references/backfill-historical-traces-with-scorers-databricks-on-aws-a980dd23.md)
