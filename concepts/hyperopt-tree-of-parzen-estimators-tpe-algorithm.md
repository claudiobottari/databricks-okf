---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b422e42efd27e41fee3c272dbd4a4d40cea725529251e83e6793340089930801
  pageDirectory: concepts
  sources:
    - hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hyperopt-tree-of-parzen-estimators-tpe-algorithm
    - HTOPE(A
    - Tree of Parzen Estimators (TPE) algorithm
    - Hyperopt TPE Algorithm
    - Tree of Parzen Estimators (TPE)
    - Tree-structured Parzen Estimator (TPE)
    - Tree‑structured Parzen Estimator
  citations:
    - file: hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md
title: Hyperopt Tree of Parzen Estimators (TPE) Algorithm
description: Bayesian hyperparameter optimization algorithm used by Hyperopt that is more efficient than grid search or random search.
tags:
  - hyperparameter-optimization
  - machine-learning
  - bayesian-optimization
timestamp: "2026-06-19T19:07:46.381Z"
---

# Hyperopt Tree of Parzen Estimators (TPE) Algorithm

The **Tree of Parzen Estimators (TPE) algorithm** is a Bayesian hyperparameter optimization method implemented in the [Hyperopt](https://github.com/hyperopt/hyperopt) library. TPE is a sequential model-based optimization (SMBO) approach that builds a probabilistic model of the objective function to guide the search for optimal hyperparameters more efficiently than grid search or random search. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Overview

TPE works by modeling the probability density of the hyperparameter space in two regions: one for configurations that produced good results (below a threshold) and one for configurations that produced poor results. It then samples new candidate hyperparameters from the "good" region, favoring points where the density of good results is high relative to the density of poor results. This approach can explore more hyperparameters and larger ranges than traditional methods. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Key Characteristics

### Efficiency
Bayesian approaches like TPE can be much more efficient than grid search and random search. Using domain knowledge to restrict the search domain can optimize tuning and produce better results. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

### Non-Monotonic Behavior
Because TPE uses stochastic search algorithms, the loss usually does not decrease monotonically with each run. However, these methods often find the best hyperparameters more quickly than other methods. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

### Handling of NaN Values
A reported loss of NaN (not a number) usually means the objective function passed to `fmin()` returned NaN. This does not affect other runs and you can safely ignore it. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Usage with `hp.choice()`

When you use `hp.choice()`, Hyperopt returns the index of the choice list. Therefore the parameter logged in [MLflow](/concepts/mlflow.md) is also the index. Use `hyperopt.space_eval()` to retrieve the actual parameter values. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Conditional Dimensions

TPE supports conditional dimensions and hyperparameters. For example, when evaluating multiple flavors of gradient descent, instead of limiting the hyperparameter space to just the common hyperparameters, you can have Hyperopt include conditional hyperparameters—the ones that are only appropriate for a subset of the flavors. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Distributed Training with `SparkTrials`

When using `SparkTrials`, configure parallelism appropriately for CPU-only versus GPU-enabled clusters. In Databricks, CPU clusters use multiple executor threads per node, while GPU clusters use only one executor thread per node to avoid conflicts among multiple Spark tasks trying to use the same GPU. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

Do not use `SparkTrials` on autoscaling clusters. Hyperopt selects the parallelism value when execution begins. If the cluster later autoscales, Hyperopt will not be able to take advantage of the new cluster size. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Related Concepts

- [Hyperopt](/concepts/hyperopt.md) — The library implementing TPE and other optimization algorithms
- Bayesian optimization — The family of algorithms to which TPE belongs
- Sequential Model-Based Optimization (SMBO) — The general framework used by TPE
- Random Search — A simpler alternative to TPE
- Grid Search — An exhaustive search method
- [Optuna](/concepts/optuna.md) — An alternative to Hyperopt for single-node optimization
- [Ray Tune](/concepts/ray-tune.md) — A distributed alternative for similar functionality
- [SparkTrials](/concepts/sparktrials.md) — The Hyperopt interface for distributed execution on Apache Spark
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) — The broader practice of optimizing model parameters

## Sources

- hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md

# Citations

1. [hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md](/references/hyperopt-best-practices-and-troubleshooting-databricks-on-aws-838e4655.md)
