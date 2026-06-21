---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8e7b7c6db819cf8633d37044fba85654a8540553a3a2b50e699d7ef4c4bda9f9
  pageDirectory: concepts
  sources:
    - hyperopt-concepts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - parallelism-vs-adaptivity-trade-off
    - PVAT
  citations:
    - file: hyperopt-concepts-databricks-on-aws.md
title: Parallelism vs adaptivity trade-off
description: In Hyperopt, higher parallelism speeds up trials but reduces adaptivity since each iteration has fewer past results to inform new hyperparameter suggestions.
tags:
  - hyperparameter-tuning
  - optimization
  - trade-offs
  - Hyperopt
timestamp: "2026-06-19T19:08:13.426Z"
---

# Parallelism vs Adaptivity Trade-off

The **parallelism vs adaptivity trade-off** is a fundamental consideration in [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) methods that use sequential model-based optimization, such as [Hyperopt](/concepts/hyperopt.md). It describes the tension between running many hyperparameter evaluations concurrently (parallelism) and the algorithm’s ability to learn from previous results to propose better new settings (adaptivity). ^[hyperopt-concepts-databricks-on-aws.md]

## Explanation

When using an iterative optimizer like Hyperopt’s [`fmin()`](https://github.com/hyperopt/hyperopt/wiki/FMin), new trial configurations are proposed based on the outcomes of previous trials. A higher degree of parallelism allows more trials to be evaluated at the same time, speeding up the overall tuning process for a fixed budget of total evaluations (`max_evals`). However, because each parallel batch of trials is started before the results of trials in the same batch are known, the optimizer has fewer past observations to guide its proposals. Lower parallelism means the optimizer sees more results between decisions, which can lead to better hyperparameter choices at the cost of longer wall-clock time. The trade-off is thus between speed and the quality of the search. ^[hyperopt-concepts-databricks-on-aws.md]

## Context in SparkTrials

In Databricks’ [`SparkTrials`](/wiki/sparktrials) class, the `parallelism` argument controls this trade-off explicitly. The default value is the number of Spark executors available, with a maximum of 128. If the configured parallelism exceeds the number of concurrent tasks allowed by the cluster, `SparkTrials` automatically reduces it. A user seeking faster tuning may increase parallelism, while a user prioritising optimal results may lower it. ^[hyperopt-concepts-databricks-on-aws.md]

## Related Concepts

- [Hyperopt](/concepts/hyperopt.md) – The hyperparameter optimization framework in which this trade-off is documented.
- [SparkTrials](/concepts/sparktrials.md) – The Databricks implementation that exposes the parallelism argument.
- fmin – The core function that executes a Hyperopt run.
- Bayesian Optimization – The underlying approach where adaptivity is a key benefit.
- Parallel Computing – The general technique of running multiple evaluations at once.

## Sources

- hyperopt-concepts-databricks-on-aws.md

# Citations

1. [hyperopt-concepts-databricks-on-aws.md](/references/hyperopt-concepts-databricks-on-aws-853fbb92.md)
