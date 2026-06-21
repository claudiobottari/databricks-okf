---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a6d218c36ad4d352b7b9957bf0ab94089109d3ea8d6f963a3484052432331fe8
  pageDirectory: concepts
  sources:
    - hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hyperopt-hpchoice-index-return-behavior
    - HHIRB
  citations:
    - file: hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md
title: Hyperopt hp.choice() Index Return Behavior
description: When using hp.choice() in Hyperopt, the returned value is the index of the chosen option, not the option itself; hyperopt.space_eval() is needed to retrieve actual parameter values.
tags:
  - hyperparameter-optimization
  - python
  - mlflow
timestamp: "2026-06-19T19:07:45.552Z"
---

# Hyperopt hp.choice() Index Return Behavior

When using Hyperopt's `hp.choice()` function to define a hyperparameter search space, the function returns the **index** of the chosen item from the provided list, not the item value itself. This means that when Hyperopt logs the selected parameter to MLflow, the logged value is the integer index rather than the actual parameter value from the choice list. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## How hp.choice() Works

`hp.choice()` is a Hyperopt function that defines a categorical search space over a list of options. When Hyperopt evaluates a trial configuration, it selects one of the options and records the selection as an integer index. For example, if you provide `hp.choice('optimizer', ['sgd', 'adam', 'rmsprop'])` and Hyperopt selects 'adam', it will log the value `1` (the index) rather than the string `'adam'`. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Retrieving Actual Parameter Values

To retrieve the actual parameter values instead of the index, use `hyperopt.space_eval()`. This function evaluates the search space and returns the real values corresponding to the indices selected by Hyperopt. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

### Example Usage

```python
from hyperopt import hp, space_eval, fmin, tpe, Trials

# Define search space
space = {
    'algorithm': hp.choice('algorithm', ['sgd', 'adam', 'rmsprop']),
    'learning_rate': hp.uniform('learning_rate', 0.001, 0.1),
    'batch_size': hp.choice('batch_size', [32, 64, 128])
}

# Run optimization
best = fmin(fn=objective_function, space=space, algo=tpe.suggest, max_evals=100)

# Retrieve actual values
best_params = space_eval(space, best)

# best_params['algorithm'] will return the string value, not the index
```

## Implications for MLflow Logging

Because Hyperopt logs the index value, MLflow experiment records will show integer values for parameters defined with `hp.choice()`. This can be confusing when reviewing experiment results, as the logged values do not directly correspond to the meaningful parameter choices. Use `hyperopt.space_eval()` to decode the indices when analyzing results or when passing parameters to downstream functions. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]

## Best Practices

- Always use `hyperopt.space_eval()` to convert indices back to actual values when interpreting results or using optimized parameters. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]
- Consider using other search space functions like `hp.uniform()`, `hp.quniform()`, or `hp.loguniform()` for numeric parameters that do not have this indexing behavior. ^[hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md]
- For categorical parameters, explicitly map the index back to the original choice using a dictionary or list lookup after optimization.

## Related Concepts

- Hyperopt search space definition
- [Tree of Parzen Estimators (TPE) algorithm](/concepts/hyperopt-tree-of-parzen-estimators-tpe-algorithm.md)
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md)
- Hyperparameter tuning best practices

## Sources

- hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md

# Citations

1. [hyperopt-best-practices-and-troubleshooting-databricks-on-aws.md](/references/hyperopt-best-practices-and-troubleshooting-databricks-on-aws-838e4655.md)
