---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b5f8223d38e814e9d078dcb12f9f81974b32c0395993db9215fa4d4df9de9301
  pageDirectory: concepts
  sources:
    - backfill-historical-traces-with-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - safety-judge-scorer
    - SJS
    - Safety LLM Judge
  citations:
    - file: backfill-historical-traces-with-scorers-databricks-on-aws.md
    - file: backfill-historical-tra traces-with-scorers-databricks-on-aws.md
title: Safety Judge Scorer
description: A pre-built safety evaluation scorer in Databricks that can be registered, started, and configured with sampling to assess content safety of model outputs.
tags:
  - databricks
  - safety
  - evaluation
timestamp: "2026-06-18T14:31:49.973Z"
---

# Safety Judge Scorer

**Safety Judge Scorer** is an [MLflow GenAI](/concepts/mlflow-3-for-genai.md) scorer that evaluates whether an AI agent's responses contain harmful, unsafe, or inappropriate content. It is one of the [[scorers]] that can be registered, started, and configured for both real-time and [backfill historical traces with scorers](/concepts/backfillscorers.md) workloads.

## Overview

Safety Judge Scorer is a predefined scorer in the `mlflow.genai.scorers` module that provides automated safety evaluation for AI agent outputs. When instantiated, it creates a safety assessment judge that can be registered and deployed to monitor agent responses for potential safety concerns. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Registration

To use the Safety Judge Scorer, you first instantiate the `Safety` class and register it with a name:

```python
from mlflow.genai.scorers import Safety

safety_judge = Safety()
safety_judge = safety_judge.register(name="safety_check")
```

^[backfill-historical-tra traces-with-scorers-databricks-on-aws.md]

## Starting the Scorer

After registration, the scorer can be started with a [ScorerSamplingConfig](/concepts/scorersamplingconfig.md) that defines the sampling rate for evaluation:

```python
safety_judge = safety_judge.start(sampling_config=ScorerSamplingConfig(sample_rate=0.5))
```

^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Use in Backfill Operations

Safety Judge Scorer can be used in [BackfillScorers](/concepts/backfillscorers.md) operations to apply safety evaluations to historical traces. When configuring backfill, you can specify custom sample rates for the safety judge:

```python
from databricks.agents.scorers import backfill_scorers, BackfillScorerConfig
from mlflow.genai.scorers import Safety, ScorerSamplingConfig

safety_judge = Safety()
safety_judge = safety_judge.register(name="safety_check")
safety_judge = safety_judge.start(sampling_config=ScorerSamplingConfig(sample_rate=0.5))

custom_scorers = [
    BackfillScorerConfig(scorer=safety_judge, sample_rate=0.8),
    # Additional scorers...
]

job_id = backfill_scorers(
    experiment_id=YOUR_EXPERIMENT_ID,
    scorers=custom_scorers,
    start_time=datetime(2024, 6, 1),
    end_time=datetime(2024, 6, 30),
)
```

^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Related Concepts

- [[Scorers|Scorer]] — The base concept for evaluation scorers in MLflow GenAI
- [ScorerSamplingConfig](/concepts/scorersamplingconfig.md) — Configuration for controlling how often a scorer samples outputs
- [ScorerSamplingConfig](/concepts/scorersamplingconfig.md) — Configuration for sampling rate and behavior
- Backfill historical traces with scorers — Applying scorers retrospectively to historical agent traces
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The broader framework for AI agent evaluation and monitoring

## Sources

- backfill-historical-traces-with-scorers-databricks-on-aws.md

# Citations

1. [backfill-historical-traces-with-scorers-databricks-on-aws.md](/references/backfill-historical-traces-with-scorers-databricks-on-aws-a980dd23.md)
2. backfill-historical-tra traces-with-scorers-databricks-on-aws.md
