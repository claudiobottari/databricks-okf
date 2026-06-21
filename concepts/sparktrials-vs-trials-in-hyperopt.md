---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0a5c306f8358188a9e8c2f8a8b471a09ad0a8958df8ae5fb8de91901a36d2235
  pageDirectory: concepts
  sources:
    - use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sparktrials-vs-trials-in-hyperopt
    - SVTIH
  citations:
    - file: use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md
title: SparkTrials vs Trials in Hyperopt
description: "Key distinction: SparkTrials distributes individual trials across workers for non-distributed algorithms, while Trials runs all trials on the driver for use with distributed training algorithms."
tags:
  - hyperparameter-tuning
  - hyperopt
  - architecture
timestamp: "2026-06-19T23:21:46.048Z"
---

# [SparkTrials](/concepts/sparktrials.md) vs Trials in [Hyperopt](/concepts/hyperopt.md)

**SparkTrials** and **Trials** are two trial‑execution classes in [Hyperopt](/concepts/hyperopt.md) that determine how hyperparameter optimisation tasks are distributed across a cluster. Their correct usage depends on whether the machine learning algorithm being tuned is itself distributed or single‑node.

## Key Differences

| Aspect | `SparkTrials` | `Trials` (default) |
|--------|---------------|--------------------|
| Execution model | Distributes individual trials across Spark worker nodes | Runs all trials on the cluster driver node |
| Intended use case | Tuning **single‑node** algorithms (e.g., scikit‑learn) where parallelism improves throughput | Tuning **distributed** algorithms (e.g., MLlib, [HorovodRunner](/concepts/horovodrunner.md)) that already use cluster resources |
| [MLflow](/concepts/mlflow.md) logging | Automatic logging supported | Manual logging required; Databricks does not support auto‑logging |

## When to Use Each

Use **`SparkTrials`** when the training algorithm is **not distributed** and you want to evaluate multiple hyperparameter configurations concurrently on different workers. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

Use the default **`Trials`** class when the training algorithm is itself **distributed** (e.g., [Apache Spark MLlib](/concepts/apache-spark-mllib.md), [HorovodRunner](/concepts/horovodrunner.md)). In this scenario, each trial runs on the driver node, giving it access to the full cluster resources for distributed training. Passing a `trials` argument to `fmin()` — and specifically using `SparkTrials` — would incorrectly distribute trial execution and prevent the algorithm from using the cluster’s distributed capabilities. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

## Automatic Logging Note

Databricks does not support automatic logging to [MLflow](/concepts/mlflow.md) when using the `Trials` class with distributed training algorithms. When you use `Trials`, you must **manually call MLflow** to log each trial’s parameters and metrics. `SparkTrials` does support automatic [MLflow](/concepts/mlflow.md) logging. ^[use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md]

## Usage Example (Distributed Algorithm)

```python
from [[hyperopt|Hyperopt]] import fmin, tpe, Trials

# Do NOT pass trials=SparkTrials()
best = fmin(
    fn=distributed_training_objective,
    space=search_space,
    algo=tpe.suggest,
    max_evals=100,
    trials=Trials()  # runs on driver; algorithm handles distribution
)
```

## Related Concepts

- [Hyperopt fmin()](/concepts/hyperopt-fmin.md) – The core optimisation function.
- Distributed training with Hyperopt – Broader workflow for tuning distributed algorithms.
- [Spark MLlib](/concepts/apache-spark-mllib.md) – A distributed machine learning library commonly tuned with `Trials`.
- [HorovodRunner](/concepts/horovodrunner.md) – API for distributed [Deep Learning on Databricks](/concepts/deep-learning-on-databricks.md).
- [Optuna](/concepts/optuna.md) – Databricks’ recommended replacement for single‑node [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md).
- [RayTune](/concepts/raytune.md) – Databricks’ recommended replacement for distributed [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md).

## Sources

- use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md

# Citations

1. [use-distributed-training-algorithms-with-hyperopt-databricks-on-aws.md](/references/use-distributed-training-algorithms-with-hyperopt-databricks-on-aws-29b4f334.md)
