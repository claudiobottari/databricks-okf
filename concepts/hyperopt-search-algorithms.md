---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6a0a4fba256bbbdc71a2b6681db4a2c343a319a242e3a9ddc3b8151a943812cb
  pageDirectory: concepts
  sources:
    - parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hyperopt-search-algorithms
    - HSA
    - algorithms
  citations:
    - file: parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md
title: Hyperopt Search Algorithms
description: "Hyperopt provides two main search algorithms: TPE (Tree of Parzen Estimators) for adaptive Bayesian optimization and random search for non-adaptive sampling over the hyperparameter space."
tags:
  - hyperopt
  - bayesian-optimization
  - random-search
timestamp: "2026-06-19T19:54:13.740Z"
---

# Hyperopt Search Algorithms

**Hyperopt Search Algorithms** are the optimization strategies used by [Hyperopt](https://github.com/hyperopt/hyperopt) to search over hyperparameter spaces during model tuning. When using Hyperopt's `fmin()` function, the `algo` parameter specifies which search algorithm to use for selecting new hyperparameter configurations to evaluate. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

## Available Search Algorithms

Hyperopt provides two primary search algorithms:

### Tree of Parzen Estimators (TPE)

`hyperopt.tpe.suggest` implements the **Tree of Parzen Estimators** algorithm, a Bayesian optimization approach. TPE iteratively and adaptively selects new hyperparameter settings to explore based on past results. It builds a probabilistic model of the objective function and uses it to select the most promising hyperparameters to evaluate next, making it more sample-efficient than random search. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

### Random Search

`hyperopt.rand.suggest` implements **random search**, a non-adaptive approach that samples hyperparameter configurations uniformly from the defined search space. Unlike TPE, random search does not use information from previous trials to guide future selections. It is simpler but may require more evaluations to find optimal configurations. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

## Usage in `fmin()`

The search algorithm is passed as the `algo` argument to Hyperopt's `fmin()` function: ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

```python
from hyperopt import fmin, tpe, hp, rand

# Using TPE
argmin = fmin(
    fn=objective,
    space=search_space,
    algo=tpe.suggest,
    max_evals=16
)

# Using Random Search
argmin = fmin(
    fn=objective,
    space=search_space,
    algo=rand.suggest,
    max_evals=16
)
```

## Integration with SparkTrials

When using [SparkTrials](parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md) for distributed tuning, the search algorithm works in conjunction with the parallelism strategy. `SparkTrials` distributes model evaluation across Spark workers, while the search algorithm determines which hyperparameter configurations to evaluate next. The `algo` parameter remains the same whether running single-machine or distributed tuning. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

## Considerations

- **TPE** is generally preferred for optimization problems where function evaluations are expensive (such as training machine learning models), as it converges to good solutions with fewer evaluations. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]
- **Random search** can be useful as a baseline or when the search space is small and exhaustive exploration is feasible.
- For distributed tuning with `SparkTrials`, the choice of search algorithm affects how new configurations are proposed to parallel workers, but the parallelism level is controlled separately through the `parallelism` parameter. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

## Migration Note

The open-source version of Hyperopt is no longer being maintained. Databricks recommends using [Optuna](optuna-hyperparameter-tuning-databricks.md) for single-node optimization or [RayTune](raytune-hyperparameter-tuning-databricks.md) for distributed hyperparameter tuning as alternatives. ^[parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md]

## Related Concepts

- [Hyperopt fmin()](/concepts/hyperopt-fmin.md) — The core function that orchestrates hyperparameter optimization
- [SparkTrials](/concepts/sparktrials.md) — The Trials class for distributing Hyperopt evaluations across a Spark cluster
- [Hyperparameter Search Spaces](/concepts/hyperopt-conditional-hyperparameter-spaces.md) — Defining parameter expressions with `hp` functions
- [Optuna Hyperparameter Tuning](/concepts/optuna-for-hyperparameter-tuning.md) — The recommended replacement for single-node optimization
- RayTune on Databricks — The recommended replacement for distributed hyperparameter tuning

## Sources

- parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md

# Citations

1. [parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws.md](/references/parallelize-hyperopt-hyperparameter-tuning-databricks-on-aws-b91f741c.md)
