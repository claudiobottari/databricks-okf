---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fd62442a9becae5e7ccf59ef2565df592bc8720904b4e08c9bf1475565e832bb
  pageDirectory: concepts
  sources:
    - hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sparktrials-incompatibility-with-autoscaling-clusters
    - SIWAC
  citations:
    - file: hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md
title: SparkTrials Incompatibility with Autoscaling Clusters
description: SparkTrials should not be used on autoscaling clusters because Hyperopt sets the parallelism value at execution start and cannot adapt if the cluster later rescales.
tags:
  - spark
  - autoscaling
  - hyperparameter-optimization
timestamp: "2026-06-19T19:08:11.103Z"
---

# SparkTrials Incompatibility with Autoscaling Clusters

**SparkTrials Incompatibility with Autoscaling Clusters** refers to a fundamental limitation of [Hyperopt](/concepts/hyperopt.md)'s `SparkTrials` class: it cannot adapt to changes in cluster size after execution begins. When a cluster autoscales, `SparkTrials` is unable to take advantage of the additional resources, leading to suboptimal performance and inefficient resource utilization.^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Cause

Hyperopt selects the parallelism value for `SparkTrials` when execution begins. This value determines how many trials can run concurrently across the cluster. If the cluster later autoscales — either scaling up with more worker nodes or scaling down — Hyperopt does not dynamically adjust its parallelism setting to match the new cluster size.^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Impact

Using `SparkTrials` on an autoscaling cluster results in:

- **Underutilization**: If the cluster scales up, the additional worker nodes remain idle because Hyperopt continues running with the original parallelism setting.
- **No performance benefit**: The speedup expected from adding more resources is not realized.
- **Wasted compute costs**: Users pay for expanded cluster resources without gaining corresponding throughput improvements.

## Recommended Practice

Do not use `SparkTrials` on autoscaling clusters. Instead, use a fixed-size cluster when running Hyperopt with `SparkTrials`. This ensures that Hyperopt's parallelism setting matches the actual cluster capacity throughout the optimization run.^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Related Considerations

When configuring parallelism for `SparkTrials`, note that CPU and GPU clusters behave differently:

- **CPU clusters**: Use multiple executor threads per worker node, allowing higher parallelism.
- **GPU clusters**: Use only one executor thread per node to avoid conflicts among multiple Spark tasks trying to use the same GPU, reducing maximum parallelism.

See GPU-enabled Clusters for detailed guidance on selecting instance types and understanding parallelism implications.^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Alternatives

For hyperparameter tuning needs where autoscaling is desired, consider alternatives to `SparkTrials`:

- [Optuna](/concepts/optuna.md) for single-node optimization
- [RayTune](/concepts/raytune.md) for distributed hyperparameter tuning with autoscaling support

Both options are recommended by Databricks as replacements for the deprecated Hyperopt distributed tuning functionality.^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Sources

- hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md

# Citations

1. [hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md](/references/hyperopt-best-practices-and-troubleshooting-databricks-on-aws-838e4655.md)
