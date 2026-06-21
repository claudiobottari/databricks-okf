---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 234ee96a45e61c5826ea4d613390622f4aa04e0fde8c1120faa9b008ca726b14
  pageDirectory: concepts
  sources:
    - backfill-historical-traces-with-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - safety-scorer-in-mlflow
    - SSIM
    - Safety Scorer
    - Safety scorer
    - Safety scorers
  citations:
    - file: backfill-historical-traces-with-scorers-databricks-on-aws.md
title: Safety Scorer in MLflow
description: A built-in MLflow GenAI scorer that evaluates content safety, registered and started with a sampling configuration.
tags:
  - mlflow
  - safety
  - evaluation
  - genai
timestamp: "2026-06-19T17:39:48.789Z"
---

Here is the wiki page for "Safety Scorer in MLflow", based solely on the provided source material.

---

## Safety Scorer in MLflow

The **Safety Scorer** is a built-in evaluator in [MLflow](/concepts/mlflow.md)'s [MLflow GenAI](/concepts/mlflow-3-for-genai.md) module that judges the safety of model outputs. It is designed to be used as part of an automated scoring pipeline for LLM agents and other generative AI applications. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

### Import and Instantiation

The Safety scorer is imported from the `mlflow.genai.scorers` module. It is instantiated like any other class:

```python
from mlflow.genai.scorers import Safety

safety_judge = Safety()
```

^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

### Registration and Starting

After creating a `Safety` instance, it must be registered with a name using the `.register()` method. Registration makes the scorer available to be used on traces and can be started with a [ScorerSamplingConfig](/concepts/scorersamplingconfig.md) to control how often it runs:

```python
safety_judge = safety_judge.register(name="safety_check")
safety_judge = safety_judge.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)
```

In this example, the scorer is registered under the name `"safety_check"` and started with a 50% sampling rate, meaning it will evaluate safety on half of the model outputs. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

### Use in Backfill

The Safety scorer can be used in a backfill operation to evaluate historical traces. When backfilling, you can define a custom sample rate for the Safety scorer via a [BackfillScorerConfig](/concepts/backfillscorerconfig.md):

```python
from databricks.agents.scorers import backfill_scorers, BackfillScorerConfig

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

This backfills safety evaluations for traces in the specified time range, using an 80% sample rate for the Safety scorer. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

### Related Concepts

- [[Scorers|Scorer]] — The base abstraction for evaluators in MLflow GenAI.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The module for generative AI evaluation and monitoring.
- [ScorerSamplingConfig](/concepts/scorersamplingconfig.md) — Configuration object for controlling scorer sampling behavior.
- [Backfill Scorer](/concepts/backfillscorers.md) — The process of scoring historical traces with a scorer.
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — The broader workflow for evaluating LLM agent performance.
- [Production Monitoring](/concepts/production-monitoring.md) — The practice of running scorers on live model outputs.

### Sources

- backfill-historical-traces-with-scorers-databricks-on-aws.md

# Citations

1. [backfill-historical-traces-with-scorers-databricks-on-aws.md](/references/backfill-historical-traces-with-scorers-databricks-on-aws-a980dd23.md)
