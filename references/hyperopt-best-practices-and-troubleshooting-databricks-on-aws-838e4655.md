---
title: Hyperopt best practices and troubleshooting | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/hyperopt-best-practices
ingestedAt: "2026-06-18T08:09:43.969Z"
---

*   [](https://docs.databricks.com/aws/en/)
*   [Machine learning](https://docs.databricks.com/aws/en/machine-learning/)
*   [Train models](https://docs.databricks.com/aws/en/machine-learning/train-model/)
*   [Databricks Runtime ML](https://docs.databricks.com/aws/en/machine-learning/databricks-runtime-ml)
*   [Model training examples](https://docs.databricks.com/aws/en/machine-learning/train-model/training-examples)
*   [Hyperparameter tuning](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/)
*   Hyperopt best practices and troubleshooting

Last updated on **May 6, 2026**

note

The open-source version of [Hyperopt](https://github.com/hyperopt/hyperopt) is no longer being maintained.

Hyperopt is not included in Databricks Runtime for Machine Learning after 16.4 LTS ML. Databricks recommends using either [Optuna](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/optuna) for single-node optimization or [RayTune](https://docs.ray.io/en/latest/tune/index.html) for a similar experience to the deprecated Hyperopt distributed hyperparameter tuning functionality. Learn more about using [RayTune](https://docs.databricks.com/aws/en/machine-learning/ray/ray-mlflow) on Databricks.

## Best practices[​](#best-practices "Direct link to Best practices")

*   Bayesian approaches can be much more efficient than grid search and random search. Hence, with the Hyperopt Tree of Parzen Estimators (TPE) algorithm, you can explore more hyperparameters and larger ranges. Using domain knowledge to restrict the search domain can optimize tuning and produce better results.
*   When you use `hp.choice()`, Hyperopt returns the index of the choice list. Therefore the parameter logged in MLflow is also the index. Use `hyperopt.space_eval()` to retrieve the parameter values.
*   For models with long training times, start experimenting with small datasets and many hyperparameters. Use MLflow to identify the best performing models and determine which hyperparameters can be fixed. In this way, you can reduce the parameter space as you prepare to tune at scale.
*   Take advantage of Hyperopt support for conditional dimensions and hyperparameters. For example, when you evaluate multiple flavors of gradient descent, instead of limiting the hyperparameter space to just the common hyperparameters, you can have Hyperopt include conditional hyperparameters—the ones that are only appropriate for a subset of the flavors. For more information about using conditional parameters, see [Defining a search space](http://hyperopt.github.io/hyperopt/getting-started/search_spaces/).
*   When using `SparkTrials`, configure parallelism appropriately for CPU-only versus GPU-enabled clusters. In Databricks, CPU and GPU clusters use different numbers of executor threads per worker node. CPU clusters use multiple executor threads per node. GPU clusters use only one executor thread per node to avoid conflicts among multiple Spark tasks trying to use the same GPU. While this is generally optimal for libraries written for GPUs, it means that maximum parallelism is reduced on GPU clusters, so be aware of how many GPUs each trial can use when selecting GPU instance types. See [GPU-enabled Clusters](https://docs.databricks.com/aws/en/compute/gpu) for details.
*   Do not use `SparkTrials` on autoscaling clusters. Hyperopt selects the parallelism value when execution begins. If the cluster later autoscales, Hyperopt will not be able to take advantage of the new cluster size.

## Troubleshooting[​](#troubleshooting "Direct link to troubleshooting")

*   A reported loss of NaN (not a number) usually means the objective function passed to `fmin()` returned NaN. This does not affect other runs and you can safely ignore it. To prevent this result, try adjusting the hyperparameter space or modifying the objective function.
*   Because Hyperopt uses stochastic search algorithms, the loss usually does not decrease monotonically with each run. However, these methods often find the best hyperparameters more quickly than other methods.
*   Both Hyperopt and Spark incur overhead that can dominate the trial duration for short trial runs (low tens of seconds). The speedup you observe may be small or even zero.

## Example notebook: Best practices for datasets of different sizes[​](#example-notebook-best-practices-for-datasets-of-different-sizes "Direct link to Example notebook: Best practices for datasets of different sizes")

`SparkTrials` runs the trials on Spark worker nodes. This notebook provides guidelines on how to move datasets of different orders of magnitude to worker nodes when using `SparkTrials`.

#### Handle datasets of different orders of magnitude notebook
