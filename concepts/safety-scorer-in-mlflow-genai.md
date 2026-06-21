---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b79d2f5f3bd184300cf4d5369b550d8f1f8025971aeb320daa5c3c6e85ad93b2
  pageDirectory: concepts
  sources:
    - backfill-historical-traces-with-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - safety-scorer-in-mlflow-genai
    - SSIMG
  citations:
    - file: backfill-historical-traces-with-scorers-databricks-on-aws.md
title: Safety Scorer in MLflow GenAI
description: A built-in MLflow GenAI scorer that evaluates the safety of model outputs, registered and started with optional sampling configuration before use.
tags:
  - mlflow
  - safety
  - evaluation
timestamp: "2026-06-18T10:52:29.746Z"
---

# Safety Scorer in MLflow GenAI

**Safety Scorer** is a built-in evaluator in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) that assesses the safety and appropriateness of model-generated content. It provides automated safety evaluation for text outputs from large language models and AI agents, helping organizations maintain content safety standards at scale.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Overview

The Safety Scorer is implemented through the `Safety` class from the `mlflow.genai.scorers` module. It enables automated safety checks on model outputs without requiring manual review of every response. The scorer can be configured with different sampling rates to balance coverage against computational cost.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Basic Usage

To use the Safety Scorer, create an instance of the `Safety` class, register it with a name, and start it with an optional sampling configuration:^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Safety

safety_judge = Safety()
safety_judge = safety_judge.register(name="safety_check")
safety_judge = safety_judge.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)
```

## Sampling Configuration

The Safety Scorer supports configurable sampling through `ScorerSamplingConfig`. The `sample_rate` parameter controls what proportion of outputs are evaluated for safety, allowing you to balance thoroughness with performance:^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

- A `sample_rate` of `0.5` evaluates 50% of all generated outputs
- A `sample_rate` of `1.0` evaluates every output (full coverage)
- Lower rates reduce computational overhead but may miss safety violations

## Backfilling Historical Traces

The Safety Scorer can be used with `backfill_scorers()` to evaluate safety on historical traces. This enables retrospective safety analysis of previously generated content:^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from databricks.agents.scorers import backfill_scorers, BackfillScorerConfig
from datetime import datetime

custom_scorers = [
    BackfillScorerConfig(scorer=safety_judge, sample_rate=0.8)
]

job_id = backfill_scorers(
    experiment_id=YOUR_EXPERIMENT_ID,
    scorers=custom_scorers,
    start_time=datetime(2024, 6, 1),
    end_time=datetime(2024, 6, 30)
)
```

When backfilling, you can specify different sample rates per scorer, independent of the rate used during live evaluation.^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Combining with Custom Scorers

The Safety Scorer can be used alongside custom [MLflow GenAI Scorers](/concepts/mlflow-genai-scorers.md) in the same evaluation pipeline. For example, you might combine safety evaluation with a custom `response_length` scorer that measures output length:^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
@scorer(aggregations=["mean", "min", "max"])
def response_length(outputs):
    """Measure response length in characters"""
    return len(outputs)

response_length = response_length.register(name="response_length")
response_length = response_length.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)
```

## Related Concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The MLflow subsystem for generative AI evaluation and monitoring
- [MLflow GenAI Scorers](/concepts/mlflow-genai-scorers.md) — The framework for creating and managing evaluators
- [Backfill Historical Traces](/concepts/historical-trace-backfilling.md) — The process of running scorers on past inference data
- [MLflow Model Evaluation](/concepts/mlflow-evaluation-ui.md) — The broader evaluation framework in MLflow
- Model Monitoring — Ongoing monitoring of model performance and safety in production

## Sources

- backfill-historical-traces-with-scorers-databricks-on-aws.md

# Citations

1. [backfill-historical-traces-with-scorers-databricks-on-aws.md](/references/backfill-historical-traces-with-scorers-databricks-on-aws-a980dd23.md)
