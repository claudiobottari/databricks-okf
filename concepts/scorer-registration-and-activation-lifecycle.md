---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2e90510e47374d7018a2aa1701f163e86cffe0f019e6d9fa06bb1e19fa4432e1
  pageDirectory: concepts
  sources:
    - backfill-historical-traces-with-scorers-databricks-on-aws.md
  confidence: 0.8
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - scorer-registration-and-activation-lifecycle
    - Activation Lifecycle and Scorer Registration
    - SRAAL
  citations:
    - file: backfill-historical-traces-with-scorers-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Scorer Registration and Activation Lifecycle
description: The pattern of registering a scorer with a name and starting it with a sampling configuration before use, as seen with both built-in and custom scorers.
tags:
  - mlflow
  - lifecycle
  - scoring
  - patterns
timestamp: "2026-06-19T17:39:56.790Z"
---

Based solely on the provided source material, here is the wiki page for **Scorer Registration and Activation Lifecycle**.

---

## Scorer Registration and Activation Lifecycle

The **Scorer Registration and Activation Lifecycle** describes the two-stage process required to deploy a [[Scorers|Scorer]] for use in production monitoring and evaluation on Databricks MLflow. A scorer must first be **registered** (creating a named, versioned entity) and then **activated** (starting its serverless inference workload) before it can score traces or participate in Backfill Historical Traces with Scorers|backfill.

### Registration

Registration is the act of creating a named scorer that can be referenced in subsequent operations. During registration, the scorer is assigned an identifier and made available for activation. The API typically follows a pattern of creating a scorer instance and then calling a `.register()` method, specifying a name. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

For example, a safety judge scorer is registered with:

```python
safety_judge = Safety()
safety_judge = safety_judge.register(name="safety_check")
```

A custom Python function decorated with `@scorer` can also be registered:

```python
@scorer(aggregations=["mean", "min", "max"])
def response_length(outputs):
    """Measure response length in characters"""
    return len(outputs)

response_length = response_length.register(name="response_length")
```

^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

### Activation (Starting)

Activation is the separate step that starts the scorer’s serverless workload. Activation applies a Sampling Configuration that controls how the scorer will be invoked — e.g., what fraction of traces it will evaluate. The `.start()` method is called on the registered scorer with a `sampling_config` argument. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

Continuing the example:

```python
from mlflow.genai.scorers import ScorerSamplingConfig

safety_judge = safety_judge.start(sampling_config=ScorerSamplingConfig(sample_rate=0.5))

response_length = response_length.start(sampling_config=ScorerSamplingConfig(sample_rate=0.5))
```

^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

Until a scorer is started, it cannot be used for scoring. Activation is required for both live production monitoring and for historical backfill.

### Prerequisites: Serverless Budget Policy

Registration and activation of a scorer both create serverless workloads on the experiment. The experiment must have a valid [Serverless Budget Policy](/concepts/serverless-budget-policy.md) assigned. By default, MLflow uses the workspace’s default budget policy. If that default is disabled and no policy is configured on the experiment, attempts to register a scorer will fail with a **403 PERMISSION_DENIED** error. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

To resolve this, set a budget policy on the experiment either through the UI or by setting the `mlflow.workload_creation_policy_id` tag on the experiment. Once the tag is set, subsequent calls such as `Scorer.register()` will use the specified policy. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Using Registered and Activated Scorers for Backfill

After a scorer has been registered and started, it can be used in a backfill operation to score historical traces. The `backfill_scorers` function accepts a list of `BackfillScorerConfig` objects, each containing a reference to the registered and activated scorer along with a separate sample_rate for backfill. The backfill sample rate can differ from the activation sample rate. ^[backfill-historical-traces-with-scorers-databricks-on-aws.md]

Example:

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

### Lifecycle Summary

1. **Define** a scorer (using `Safety()` or the `@scorer` decorator).
2. **Register** it with a unique name (`scorer.register(name="...")`) — this requires a valid serverless budget policy on the experiment.
3. **Activate** it by calling `scorer.start(sampling_config=...)` — this begins the serverless workload.
4. **Use** the activated scorer for live scoring or reference it in a `BackfillScorerConfig` for historical backfill.

## Related Concepts

- [[Scorers|Scorer]]
- [Backfill Historical Traces with Scorers](/concepts/backfillscorers.md)
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md)
- 403 PERMISSION_DENIED Serverless Budget Policy Error
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Production Monitoring](/concepts/production-monitoring.md)

## Sources

- backfill-historical-traces-with-scorers-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [backfill-historical-traces-with-scorers-databricks-on-aws.md](/references/backfill-historical-traces-with-scorers-databricks-on-aws-a980dd23.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
