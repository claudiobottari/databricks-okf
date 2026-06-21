---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 23de2927d525634f174cece841cdffad1daa5e0cc89b9e978feb1cada4fa3e59
  pageDirectory: concepts
  sources:
    - backfill-historical-traces-with-scorers-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-agent-evaluation-scorers
    - DAES
    - databricks.agents.scorers
  citations:
    - file: backfill-historical-traces-with-scorers-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Databricks Agent Evaluation Scorers
description: Framework from Databricks for evaluating AI agent outputs, including built-in scorers like Safety() and a lifecycle of register/start.
tags:
  - databricks
  - evaluation
  - ai-agents
  - safety
timestamp: "2026-06-19T22:12:50.685Z"
---

# Databricks Agent Evaluation Scorers

**Databricks Agent Evaluation Scorers** are programmable evaluation functions that compute metrics on outputs or traces produced by AI agents. They are used within [MLflow experiments](/concepts/mlflow-experiment.md) to assess agent performance, enabling both real-time monitoring and historical analysis. Scorers can be built-in (e.g., safety judges) or custom user‑defined functions, and they support configurable sampling rates and aggregation methods. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md] ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Scorer Registration and Configuration

A scorer must be **registered** with a name and then **started** to begin evaluation. During this process, you provide a `SamplingConfig` that defines the fraction of traces to evaluate (e.g., `sample_rate=0.5` for 50% sampling). The following example registers and starts a built-in `Safety` scorer and a custom `response_length` scorer: ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Safety, scorer, ScorerSamplingConfig

# Built-in safety judge
safety_judge = Safety()
safety_judge = safety_judge.register(name="safety_check")
safety_judge = safety_judge.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)

# Custom scorer
@scorer(aggregations=["mean", "min", "max"])
def response_length(outputs):
    """Measure response length in characters"""
    return len(outputs)

response_length = response_length.register(name="response_length")
response_length = response_length.start(
    sampling_config=ScorerSamplingConfig(sample_rate=0.5)
)
```

^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Custom Scorers

Custom scorers are defined by decorating a function with `@scorer` from `mlflow.genai.scorers`. The function receives agent **outputs** (or trace data) and returns a numeric metric. You can specify aggregation methods (e.g., `mean`, `min`, `max`) to compute summary statistics across traces. After definition, the custom scorer must be registered and started, just like built-in scorers. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Backfilling Historical Traces

Scorers can be applied to historical traces within a specified time range using the `backfill_scorers` function from `databricks.agents.scorers`. This is useful for evaluating past agent behavior or re-scoring with updated metrics. Each scorer can have its own sample rate during backfill by wrapping it in a `BackfillScorerConfig`. The backfill is submitted as a serverless job that runs the scorers over the defined window. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

```python
from databricks.agents.scorers import backfill_scorers, BackfillScorerConfig
from datetime import datetime

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

^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

## Budget Policy Requirement

Scoring workloads — including scheduled scorers, synthetic evaluation set generation, and agent evaluation — run as serverless workloads on Databricks. If the workspace’s default serverless budget policy is disabled, MLflow returns a `403 PERMISSION_DENIED` error when attempting to register a scorer or run an evaluation. To resolve this, a serverless budget policy must be explicitly set on the MLflow experiment via the UI or the API using the tag `mlflow.workload_creation_policy_id`. Only users and service principals who have permission to use that policy can assign it. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

```python
mlflow.set_experiment_tag(
    experiment_id="<your-experiment-id>",
    key="mlflow.workload_creation_policy_id",
    value="<your-policy-id>",
)
```

^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md) – Organizational unit for runs and evaluation workflows.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) – Controls spending for serverless workloads like scorers.
- [Production Monitoring](/concepts/production-monitoring.md) – Scheduled scoring workflows for deployed agents.
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) – Broader workflow for assessing agent performance using scorers.
- [Synthetic evaluation generation](/concepts/synthetic-evaluation-data-generation.md) – Serverless workload that benefits from budget policy configuration.
- 403 PERMISSION_DENIED Serverless Budget Policy Error – Common error when no budget policy is set.

## Sources

- backfill-historical-traces-with-scorers-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [backfill-historical-traces-with-scorers-databricks-on-aws.md](/references/backfill-historical-traces-with-scorers-databricks-on-aws-a980dd23.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
