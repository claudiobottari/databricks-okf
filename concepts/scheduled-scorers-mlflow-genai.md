---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c3e5d7b6412e91ced51dad8790f66d07399bfbfe5482b890d6dfd4870eb6f191
  pageDirectory: concepts
  sources:
    - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scheduled-scorers-mlflow-genai
    - SS(G
    - Scheduled Scorers
    - Scheduled Scoring
    - Scheduled scorers
    - scheduled scorers
  citations:
    - file: production-monitoring-for-genai-evaluation-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
    - file: manage-production-scorers-databricks-on-aws.md
title: Scheduled Scorers (MLflow GenAI)
description: A serverless workload in Databricks MLflow that periodically evaluates GenAI applications in production, subject to budget policy controls.
tags:
  - mlflow
  - genai
  - monitoring
  - serverless
timestamp: "2026-06-18T11:08:24.169Z"
---

# Scheduled Scorers (MLflow GenAI)

**Scheduled scorers** in MLflow GenAI are [Code-based Scorers](/concepts/code-based-scorers.md) that run on a recurring schedule to automatically evaluate inference data stored in an [inference table](/concepts/inference-tables.md). They process new request/response pairs from a model serving endpoint as they arrive, applying custom evaluation logic defined by the scorer to produce feedback for every inference row that meets the scorer's sampling criteria.^[production-monitoring-for-genai-evaluation-databricks-on-aws.md]

## Overview

Scheduled scorers enable continuous, automated evaluation of production GenAI applications. They replace manual ad-hoc evaluation with a systematic pipeline that scores every inference (or a sampled subset) against custom criteria — such as correctness, safety, or business-specific quality metrics. The scorer function is invoked for each row in the inference table, and the resulting feedback is written back to the inference table so that it can be queried, monitored in dashboards, and used for drift detection or retraining triggers.^[production-monitoring-for-genai-evaluation-databricks-on-aws.md]

## How Scheduled Scorers Work

1. **Register** a code-based scorer using `Scorer.register()` or the `@scorer` decorator. This makes the scorer available in the workspace.
2. **Start** the scorer using `Scorer.start()` with a [ScorerSamplingConfig](/concepts/scorersamplingconfig.md). This creates a serverless job that monitors the inference table for new rows.
3. The serverless job polls the inference table on a schedule (for example, every few minutes or based on a trigger) and processes each new row through the scorer function.
4. The scorer returns a [Feedback](/concepts/feedback-object.md) object for each evaluated row, which is written to the inference table as an additional column.

The frequency of the schedule and the sampling rate are configured in the `ScorerSamplingConfig`.^[production-monitoring-for-genai-evaluation-databricks-on-aws.md]

## Budget Policy

Scheduled scorers are among the workloads that are affected by [Serverless Budget Policy](/concepts/serverless-budget-policy.md) settings. When a scorer runs, it creates serverless compute resources in the workspace. By default, these workloads use the workspace's default serverless budget policy. If the workspace has disabled the default policy (for example, when each user and service principal must select a dedicated policy), MLflow cannot pick a fallback and registering or starting a scorer fails with a `403 Client Error: ForbiddenPERMISSION_DENIED` error.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

To resolve this, set a budget policy on the MLflow experiment where the scorer is registered. MLflow then uses that policy for every serverless workload it creates for the experiment. You can set the policy either in the experiment UI or by setting the `mlflow.workload_creation_policy_id` tag on the experiment using `mlflow.set_experiment_tag()`.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Requirements

- The MLflow experiment must have an appropriate [Serverless Budget Policy](/concepts/serverless-budget-policy.md) set, or the workspace must have a default policy enabled.
- The user or service principal registering the scorer must have permission to use the budget policy.
- The model serving endpoint must have an inference table configured.
- The scorer code must be self-contained and importable by the serverless runtime.^[production-monitoring-for-genai-evaluation-databricks-on-aws.md, configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Example

The following example registers and starts a scheduled scorer that evaluates all traces (100% sampling rate):

```python
import mlflow
from mlflow.genai.scorers import Scorer, ScorerSamplingConfig

@mlflow.genai.scorers.scorer
def my_scorer(trace):
    # Custom evaluation logic
    score = evaluate_trace(trace)
    return mlflow.entities.Feedback(
        value=score,
        rationale="Automated scoring"
    )

# Register and start the scorer as a scheduled job
my_scorer.register()
my_scorer.start(
    sampling_config=ScorerSamplingConfig(sample_rate=1.0)
)
```

After starting, the scorer runs on a schedule and processes new rows as they arrive in the inference table.^[production-monitoring-for-genai-evaluation-databricks-on-aws.md]

## Stopping a Scheduled Scorer

To stop a scheduled scorer from running, use `Scorer.stop()`. This cancels the serverless job. You can also delete the scorer entirely using `Scorer.delete()`, which removes the registration and stops any running schedule.^[manage-production-scorers-databricks-on-aws.md]

## Related Concepts

- [Code-based Scorers](/concepts/code-based-scorers.md) — The underlying mechanism for defining evaluation logic
- [Inference table](/concepts/inference-tables.md) — The storage target for serving endpoint data and scorer feedback
- Feedback (MLflow) — The output structure returned by scorers
- [Scorer class](/concepts/scorer-class.md) — The programmatic API for registering and managing scorers
- [Production Monitoring](/concepts/production-monitoring.md) — The broader framework for monitoring GenAI apps in production
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Cost-control mechanism that affects scorer scheduling
- [MLflow Experiment](/concepts/mlflow-experiment.md) — The organizing unit for runs, scorers, and evaluations
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) — A related evaluation workload that also uses serverless compute

## Sources

- production-monitoring-for-genai-evaluation-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
- manage-production-scorers-databricks-on-aws.md

# Citations

1. production-monitoring-for-genai-evaluation-databricks-on-aws.md
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
3. [manage-production-scorers-databricks-on-aws.md](/references/manage-production-scorers-databricks-on-aws-ae58ef30.md)
