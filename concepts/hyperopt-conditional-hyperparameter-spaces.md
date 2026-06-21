---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 55d3148138d6d6ce93345bc968f102fbfa7fdd94262ca36a2b317d6c83c4e741
  pageDirectory: concepts
  sources:
    - hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hyperopt-conditional-hyperparameter-spaces
    - HCHS
    - Hyperparameter Search Spaces
  citations:
    - file: hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md
title: Hyperopt Conditional Hyperparameter Spaces
description: Hyperopt supports conditional search spaces where certain hyperparameters are only explored for specific model flavors or algorithms, enabling more targeted optimization.
tags:
  - hyperparameter-optimization
  - search-spaces
timestamp: "2026-06-19T19:07:55.519Z"
---

# Hyperopt Conditional Hyperparameter Spaces

**Hyperopt Conditional Hyperparameter Spaces** refer to a feature of the [Hyperopt] library that allows the search space to include hyperparameters that are only relevant for a subset of configuration choices. Rather than restricting the entire space to a fixed set of common hyperparameters, conditional dimensions let the optimizer sample different parameter sets depending on which algorithmic flavor or model variant is being evaluated.

## Overview

Conditional hyperparameter spaces are supported through Hyperopt’s search space definition, particularly using `hp.choice()` to select among discrete alternatives (e.g., optimizers, activation functions, model backbones). When `hp.choice()` is used, a nested dictionary or list can define parameters that apply only to a specific choice, creating a branching space. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

Because Hyperopt uses the Tree of Parzen Estimators (TPE) algorithm, it can efficiently explore non‑uniform spaces. Conditional dimensions enable the optimizer to search over more hyperparameters and larger ranges without wasting trials on irrelevant parameters. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Motivation

When tuning multiple flavors of an algorithm (for example, different gradient‑descent variants such as SGD, Adam, and AdaGrad), each flavor has its own set of hyperparameters (e.g., momentum for SGD, β₁/β₂ for Adam). A standard flat search space would force all parameters to exist for all trials, creating an unnecessarily large space and wasting trials on parameters that are meaningless for a given flavor. Conditional spaces solve this by letting Hyperopt sample only the parameters that apply to the chosen flavor. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Usage with `hp.choice()` and `space_eval()`

When using `hp.choice(key, [option1, option2, ...])`, Hyperopt returns the **index** of the chosen option, not the option’s value. Consequently, if a conditional hyperparameter’s value is logged directly to [MLflow] (or recorded for analysis), it will be recorded as an integer index rather than the original string or object. To retrieve the actual parameter value, use `hyperopt.space_eval()`. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

A common pattern is to define the space as a dictionary:

```python
space = hp.choice('optimizer', [
    {
        'type': 'sgd',
        'lr': hp.loguniform('lr_sgd', ...),
        'momentum': hp.uniform('momentum', ...)
    },
    {
        'type': 'adam',
        'lr': hp.loguniform('lr_adam', ...),
        'beta1': hp.uniform('beta1', ...),
        'beta2': hp.uniform('beta2', ...)
    }
])
```

In this example, when `hp.choice` selects SGD, only `lr_sgd` and `momentum` are sampled; when Adam is selected, only `lr_adam`, `beta1`, and `beta2` are sampled. After `fmin()` completes, `hyperopt.space_eval(space, best_params)` converts the integer indices back to the meaningful choice values. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Best Practices

- Use conditional dimensions to reduce the effective search space when tuning across families of algorithms or models. This allows the TPE algorithm to focus on relevant hyperparameters. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]
- Always call `hyperopt.space_eval()` before logging results or comparing trials, because `hp.choice()` stores integer indices. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]
- For very large spaces, start with a small dataset to identify which hyperparameters are important, then fix the conditional choices that perform poorly. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Deprecation Note

Hyperopt is no longer being maintained, and it is not included in Databricks Runtime ML after version 16.4 LTS ML. Databricks recommends using [Optuna] for single‑node optimization or [RayTune] for distributed hyperparameter tuning that provides a similar experience to the deprecated `SparkTrials` functionality. However, the concept of conditional search spaces is supported by both alternatives (e.g., Optuna’s `suggest_categorical` and Ray Tune’s conditional spaces). ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Related Concepts

- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md)
- [Tree of Parzen Estimators (TPE)](/concepts/hyperopt-tree-of-parzen-estimators-tpe-algorithm.md)
- [MLflow](/concepts/mlflow.md)
- [SparkTrials](/concepts/sparktrials.md)
- [Optuna](/concepts/optuna.md)
- [RayTune](/concepts/raytune.md)

## Sources

- hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md

# Citations

1. [hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md](/references/hyperopt-best-practices-and-troubleshooting-databricks-on-aws-838e4655.md)
