---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: adc6c0f37bbfd02454fe828b26876c784a8210c8cd4d88ed7e9de3141628ef59
  pageDirectory: concepts
  sources:
    - hyperparameter-tuning-with-optuna-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - optuna-trial-object
    - OTO
    - Trial object
  citations:
    - file: hyperparameter-tuning-with-optuna-databricks-on-aws.md
      start: 3
      end: 8
    - file: hyperparameter-tuning-with-optuna-databricks-on-aws.md
      start: 4
      end: 4
    - file: hyperparameter-tuning-with-optuna-databricks-on-aws.md
      start: 5
      end: 5
    - file: hyperparameter-tuning-with-optuna-databricks-on-aws.md
      start: 7
      end: 7
    - file: hyperparameter-tuning-with-optuna-databricks-on-aws.md
      start: 10
      end: 14
    - file: hyperparameter-tuning-with-optuna-databricks-on-aws.md
      start: 1
      end: 15
title: Optuna Trial object
description: Core abstraction in Optuna that provides suggest methods to generate hyperparameter values during optimization
tags:
  - machine-learning
  - optuna
  - api
timestamp: "2026-06-19T19:08:37.963Z"
---

Here is the wiki page for "Optuna Trial object", written solely from the provided source material.

---

## Optuna Trial object

An **Optuna Trial object** is the core interface through which a hyperparameter optimization study interacts with a machine learning model's training code. During each invocation of an objective function, Optuna creates a `Trial` object that manages the state for that single evaluation and provides methods for sampling hyperparameters.

### Generating Hyperparameters

The primary role of the `Trial` object is to generate hyperparameter suggestions. Within an objective function, you call the `suggest_*` methods of the `Trial` object to declare the search space for each hyperparameter. These methods dynamically choose values based on the underlying sampling algorithm (e.g., [Tree‑structured Parzen Estimator](/concepts/hyperopt-tree-of-parzen-estimators-tpe-algorithm.md)). ^[hyperparameter-tuning-with-optuna-databricks-on-aws.md#L3-L8]

Commonly used suggest methods include:

- **`trial.suggest_categorical(name, choices)`** – suggests a value from a discrete set of categories. ^[hyperparameter-tuning-with-optuna-databricks-on-aws.md#L4]
- **`trial.suggest_float(name, low, high, log=False)`** – suggests a floating‑point value within a range; when `log=True`, the sampling is performed on a logarithmic scale. ^[hyperparameter-tuning-with-optuna-databricks-on-aws.md#L5]
- **`trial.suggest_int(name, low, high)`** – suggests an integer value within a specified inclusive range. ^[hyperparameter-tuning-with-optuna-databricks-on-aws.md#L7]

### Linking an Objective Value to a Trial

After training a model with the suggested hyperparameters, the objective function computes a scalar error metric (for example, mean squared error) and returns it. This return value is automatically associated with the `Trial` object by Optuna, allowing the study to record the performance of that particular hyperparameter configuration. ^[hyperparameter-tuning-with-optuna-databricks-on-aws.md#L10-L14]

### Example

The following example shows a complete objective function that uses a `Trial` object:

```python
import sklearn

def objective(trial):
    # Invoke suggest methods of a Trial object to generate hyperparameters.
    regressor_name = trial.suggest_categorical('classifier', ['SVR', 'RandomForest'])
    if regressor_name == 'SVR':
        svr_c = trial.suggest_float('svr_c', 1e-10, 1e10, log=True)
        regressor_obj = sklearn.svm.SVR(C=svr_c)
    else:
        rf_max_depth = trial.suggest_int('rf_max_depth', 2, 32)
        regressor_obj = sklearn.ensemble.RandomForestRegressor(max_depth=rf_max_depth)

    X, y = sklearn.datasets.fetch_california_housing(return_X_y=True)
    X_train, X_val, y_train, y_val = sklearn.model_selection.train_test_split(X, y, random_state=0)
    regressor_obj.fit(X_train, y_train)
    y_pred = regressor_obj.predict(X_val)
    error = sklearn.metrics.mean_squared_error(y_val, y_pred)

    return error  # An objective value linked with the Trial object
```

^[hyperparameter-tuning-with-optuna-databricks-on-aws.md#L1-L15]

### Related Concepts

- Hyperparameter optimization – The broader process of searching for optimal model configuration.
- Optuna Study – The container that manages a collection of trials.
- Objective function – The function that receives a `Trial` object and returns a metric to minimize or maximize.
- [Tree-structured Parzen Estimator (TPE)](/concepts/hyperopt-tree-of-parzen-estimators-tpe-algorithm.md) – A default sampling algorithm that uses trial history to guide suggestions.

### Sources

- hyperparameter-tuning-with-optuna-databricks-on-aws.md

# Citations

1. [hyperparameter-tuning-with-optuna-databricks-on-aws.md:3-8](/references/hyperparameter-tuning-with-optuna-databricks-on-aws-acf7dc85.md)
2. [hyperparameter-tuning-with-optuna-databricks-on-aws.md:4-4](/references/hyperparameter-tuning-with-optuna-databricks-on-aws-acf7dc85.md)
3. [hyperparameter-tuning-with-optuna-databricks-on-aws.md:5-5](/references/hyperparameter-tuning-with-optuna-databricks-on-aws-acf7dc85.md)
4. [hyperparameter-tuning-with-optuna-databricks-on-aws.md:7-7](/references/hyperparameter-tuning-with-optuna-databricks-on-aws-acf7dc85.md)
5. [hyperparameter-tuning-with-optuna-databricks-on-aws.md:10-14](/references/hyperparameter-tuning-with-optuna-databricks-on-aws-acf7dc85.md)
6. [hyperparameter-tuning-with-optuna-databricks-on-aws.md:1-15](/references/hyperparameter-tuning-with-optuna-databricks-on-aws-acf7dc85.md)
