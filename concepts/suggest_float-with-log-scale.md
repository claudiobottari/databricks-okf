---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 43eb243c83d76a958c7c6b5d2b35a8f569590dd6508ba8cea1238696dc2fa480
  pageDirectory: concepts
  sources:
    - hyperparameter-tuning-with-optuna-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - suggest_float-with-log-scale
    - SWLS
  citations:
    - file: hyperparameter-tuning-with-optuna-databricks-on-aws.md
title: suggest_float with log scale
description: Optuna method for suggesting continuous float hyperparameters, optionally on a logarithmic scale for wide-ranging values
tags:
  - machine-learning
  - optuna
  - hyperparameter
timestamp: "2026-06-19T19:08:37.490Z"
---

# suggest_float with log scale

**suggest_float with log scale** is a hyperparameter suggestion method in [Optuna](/concepts/optuna.md) that proposes floating-point values for a trial. When used with the `log=True` parameter, it samples values on a logarithmic scale, which is particularly useful for parameters that span several orders of magnitude.

## Overview

The `suggest_float` method is invoked on a Trial object during hyperparameter optimization. It allows the user to define a search space for continuous parameters by specifying lower and upper bounds. When `log=True` is set, the sampling is performed uniformly in the log space, meaning values are drawn from a log-uniform distribution between `low` and `high`.^[hyperparameter-tuning-with-optuna-databricks-on-aws.md]

## Syntax

```python
trial.suggest_float(name, low, high, log=False)
```

- `name` (str): Name of the parameter.
- `low` (float): Lower bound of the search space.
- `high` (float): Upper bound of the search space.
- `log` (bool, default False): If `True`, the parameter is sampled on a logarithmic scale.

## Usage Example

Logarithmic scaling is commonly applied to hyperparameters such as regularization strength or learning rates, where the optimal value might exist at any scale from very small to very large. For example, the regularization parameter `C` in an SVM (Support Vector Machine) is often searched on a log scale:^[hyperparameter-tuning-with-optuna-databricks-on-aws.md]

```python
svr_c = trial.suggest_float('svr_c', 1e-10, 1e10, log=True)
```

This call suggests values for `svr_c` uniformly in the logarithmic range from 1e-10 to 1e10, covering 20 orders of magnitude. Without `log=True`, the same range would be searched linearly, making it extremely unlikely to find very small or very large optimal values.^[hyperparameter-tuning-with-optuna-databricks-on-aws.md]

## When to Use Log Scale

Use `log=True` when the hyperparameter:

- Spans multiple orders of magnitude (e.g., 1e-10 to 1e10).
- Represents a multiplicative factor or rate (e.g., learning rate, regularization coefficient).
- Is expected to have a multiplicative rather than additive effect on model performance.

## Related Concepts

- [Optuna](/concepts/optuna.md) — The hyperparameter optimization framework that provides the `suggest_float` method.
- Trial — The Optuna object that manages a single evaluation of the objective function.
- suggest_int — Similar method for integer hyperparameters, which also supports log scaling.
- suggest_categorical — Method for categorical hyperparameter selection.
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) — The broader process of optimizing model configuration parameters.

## Sources

- hyperparameter-tuning-with-optuna-databricks-on-aws.md

# Citations

1. [hyperparameter-tuning-with-optuna-databricks-on-aws.md](/references/hyperparameter-tuning-with-optuna-databricks-on-aws-acf7dc85.md)
