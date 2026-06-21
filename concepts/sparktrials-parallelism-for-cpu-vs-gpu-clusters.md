---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 73313271ab4976c5c2a6422875dc992ecdc11143acf4782d5a7953eb5e632713
  pageDirectory: concepts
  sources:
    - hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sparktrials-parallelism-for-cpu-vs-gpu-clusters
    - SPFCVGC
  citations:
    - file: hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md
title: SparkTrials Parallelism for CPU vs GPU Clusters
description: SparkTrials parallelism configuration differs between CPU clusters (multiple executor threads per node) and GPU clusters (one executor thread per node to avoid GPU conflicts).
tags:
  - spark
  - gpu
  - parallelism
  - hyperparameter-optimization
timestamp: "2026-06-19T19:07:39.516Z"
---

# SparkTrials Parallelism for CPU vs GPU Clusters

**SparkTrials Parallelism for CPU vs GPU Clusters** describes how to configure the parallelism parameter in [SparkTrials](/concepts/sparktrials.md) to match the underlying hardware architecture when running [Hyperopt](/concepts/hyperopt.md) on a Databricks cluster. The key difference is that CPU and GPU clusters use different numbers of executor threads per worker node, which directly affects the maximum parallelism that can be achieved.

## CPU vs GPU Threading

On CPU clusters, each worker node runs multiple executor threads. This means that many trials can execute in parallel on a single node, increasing throughput for CPU-bound workloads. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

On GPU clusters, each worker node runs only **one** executor thread. This is because multiple Spark tasks would otherwise attempt to use the same GPU hardware, causing resource conflicts. While this configuration is generally optimal for libraries designed for GPUs, it results in significantly lower maximum parallelism on GPU clusters compared to CPU clusters. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Selecting Parallelism for GPU Clusters

When using SparkTrials on GPU-enabled clusters, you must account for the reduced parallelism. Key considerations include:

- **Understanding per-trial GPU usage**: Before selecting GPU instance types, determine how many GPUs each individual trial requires. This influences the effective parallelism you can achieve. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]
- **Adjusting parallelism downward**: On GPU clusters, the parallelism value should be set lower than on equivalent CPU clusters because only one thread runs per node.
- **Instance type selection**: Choose GPU instance types that match the memory and compute requirements of your trials to avoid wasting GPU resources.

## Additional Considerations

- **Do not use SparkTrials on [autoscaling clusters](/concepts/fixed-size-vs-auto-scaling-ray-clusters.md)**: Hyperopt selects the parallelism value when execution begins. If the cluster later autoscales, Hyperopt will not be able to take advantage of the new cluster size. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]
- **Short trial overhead**: Both Hyperopt and Spark incur overhead that can dominate trial duration for short runs (low tens of seconds). The speedup you observe may be small or even zero on GPU clusters due to the reduced parallelism. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Best Practice Summary

- **CPU clusters**: Use higher parallelism to maximize throughput across multiple executor threads per node.
- **GPU clusters**: Use lower parallelism, accounting for the single-thread-per-node constraint, and select GPU instance types based on per-trial GPU requirements.

## Related Concepts

- [Hyperopt](/concepts/hyperopt.md)
- [SparkTrials](/concepts/sparktrials.md)
- [Databricks GPU Clusters](/concepts/databricks-serverless-gpu-clusters.md)
- [Distributed hyperparameter tuning](/concepts/raytune-for-distributed-hyperparameter-tuning-on-databricks.md)
- [MLflow](/concepts/mlflow.md)
- [Optuna](/concepts/optuna.md) — recommended alternative to Hyperopt for single-node optimization
- [RayTune](/concepts/raytune.md) — recommended alternative to Hyperopt for distributed tuning

## Sources

- hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md

# Citations

1. [hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md](/references/hyperopt-best-practices-and-troubleshooting-databricks-on-aws-838e4655.md)
