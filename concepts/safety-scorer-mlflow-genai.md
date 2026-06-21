---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2d52113562828eed9b6862b102449888658bc1068d6c7305e50c7d8628adc2c0
  pageDirectory: concepts
  sources:
    - backfill-historical-traces-with-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - safety-scorer-mlflow-genai
    - SS(G
  citations:
    - file: backfill-historical-traces-with-scorers-databricks-on-aws.md
title: Safety Scorer (MLflow GenAI)
description: Pre-built safety evaluation judge from mlflow.genai.scorers that can be registered and configured with sampling rates to assess safety of model outputs.
tags:
  - MLflow
  - safety
  - evaluation
timestamp: "2026-06-19T14:08:11.332Z"
---

# Safety Scorer (MLflow GenAI)

The **Safety Scorer** is a predefined evaluation judge in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) that assesses the safety of model outputs. It is part of the `mlflow.genai.scorers` module and is designed to detect potentially harmful, unsafe, or policy-violating content in generated responses from GenAI agents. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Usage

The `Safety` class provides a convenient interface for creating a safety evaluation judge. After instantiation, the scorer must be registered with a name and started with a [ScorerSamplingConfig](/concepts/scorersamplingconfig.md) to begin collecting evaluations on live traces. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Safety, ScorerSamplingConfig

safety_judge = Safety()
safety_judge = safety_judge.register(name="safety_check")
safety_judge = safety_judge.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)
```

The `sample_rate` parameter (0.0 to 1.0) controls the fraction of traces that the scorer evaluates. A sample rate of 0.5 means 50% of all traces will be scored for safety. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Backfill Support

The Safety Scorer can be used with [BackfillScorers](/concepts/backfillscorers.md) to evaluate historical traces within a specified time window. When included in a `BackfillScorerConfig`, a custom sample rate can be set independently of the scorer's current running configuration, allowing for more comprehensive historical analysis. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from databricks.agents.scorers import backfill_scorers, BackfillScorerConfig
from datetime import datetime
from mlflow.genai.scorers import Safety, ScorerSamplingConfig

safety_judge = Safety()
safety_judge = safety_judge.register(name="safety_check")
safety_judge = safety_judge.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)

# Define custom sample rate for backfill
custom_scorers = [
    BackfillScorerConfig(scorer=safety_judge, sample_rate=0.8),
]

job_id = backfill_scorers(
    experiment_id=YOUR_EXPERIMENT_ID,
    scorers=custom_scorers,
    start_time=datetime(2024, 6, 1),
    end_time=datetime(2024, 6, 30),
)
```

## Deployment Considerations

The Safety Scorer requires a [Serverless Budget Policy](/concepts/serverless-budget-policy.md) to be configured on the MLflow experiment. If the workspace's default serverless budget policy is disabled and no fallback policy is available, MLflow returns a `403 PERMISSION_DENIED` error when attempting to register or start the scorer. Setting the `mlflow.workload_creation_policy_id` tag on the experiment resolves this issue.

## Related Concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The framework for evaluating and monitoring generative AI agents.
- [[Scorers|Scorer]] – Base abstraction for custom or predefined evaluation judges.
- [ScorerSamplingConfig](/concepts/scorersamplingconfig.md) – Configuration for controlling the evaluation sampling rate.
- [BackfillScorerConfig](/concepts/backfillscorerconfig.md) – Configuration for applying scorers to historical traces.
- Response Length Scorer – Another example of a predefined scorer in the `mlflow.genai.scorers` module.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying scorers for continuous quality monitoring.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) – Required infrastructure for running serverless scorer workloads.

## Sources

- backfill-historical-traces-with-scorers-databricks-on-aws.md

# Citations

1. [backfill-historical-traces-with-scorers-databricks-on-aws.md](/references/backfill-historical-traces-with-scorers-databricks-on-aws-a980dd23.md)
