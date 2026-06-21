---
title: Hyperopt concepts | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/hyperopt-concepts
ingestedAt: "2026-06-18T08:09:45.529Z"
---

note

The open-source version of [Hyperopt](https://github.com/hyperopt/hyperopt) is no longer being maintained.

Hyperopt is not included in Databricks Runtime for Machine Learning after 16.4 LTS ML. Databricks recommends using either [Optuna](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/optuna) for single-node optimization or [RayTune](https://docs.ray.io/en/latest/tune/index.html) for a similar experience to the deprecated Hyperopt distributed hyperparameter tuning functionality. Learn more about using [RayTune](https://docs.databricks.com/aws/en/machine-learning/ray/ray-mlflow) on Databricks.

This article describes some of the concepts you need to know to use distributed Hyperopt.

**In this section:**

*   [`fmin()`](#fmin)
*   [The `SparkTrials` class](#the-sparktrials-class)
*   [`SparkTrials` and MLflow](#sparktrials-and-mlflow)

For examples illustrating how to use Hyperopt in Databricks, see [Hyperopt](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/#hyperopt-overview).

## `fmin()`[​](#fmin "Direct link to fmin")

You use `fmin()` to execute a Hyperopt run. The arguments for `fmin()` are shown in the table; see [the Hyperopt documentation](https://github.com/hyperopt/hyperopt/wiki/FMin) for more information. For examples of how to use each argument, see [the example notebooks](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/#hyperopt-overview).

## The `SparkTrials` class[​](#the-sparktrials-class "Direct link to the-sparktrials-class")

`SparkTrials` is an API developed by Databricks that allows you to distribute a Hyperopt run without making other changes to your Hyperopt code. `SparkTrials` accelerates single-machine tuning by distributing trials to Spark workers.

note

`SparkTrials` is designed to parallelize computations for single-machine ML models such as scikit-learn. For models created with distributed ML algorithms such as MLlib or Horovod, do not use `SparkTrials`. In this case the model building process is automatically parallelized on the cluster and you should use the default Hyperopt class `Trials`.

This section describes how to configure the arguments you pass to `SparkTrials` and implementation aspects of `SparkTrials`.

### Arguments[​](#arguments "Direct link to Arguments")

`SparkTrials` takes two optional arguments:

*   `parallelism`: Maximum number of trials to evaluate concurrently. A higher number lets you scale-out testing of more hyperparameter settings. Because Hyperopt proposes new trials based on past results, there is a trade-off between parallelism and adaptivity. For a fixed `max_evals`, greater parallelism speeds up calculations, but lower parallelism may lead to better results since each iteration has access to more past results.
    
    Default: Number of Spark executors available. Maximum: 128. If the value is greater than the number of concurrent tasks allowed by the cluster configuration, `SparkTrials` reduces parallelism to this value.
    
*   `timeout`: Maximum number of seconds an `fmin()` call can take. When this number is exceeded, all runs are terminated and `fmin()` exits. Information about completed runs is saved.
    

### Implementation[​](#implementation "Direct link to Implementation")

When defining the objective function `fn` passed to `fmin()`, and when selecting a cluster setup, it is helpful to understand how `SparkTrials` distributes tuning tasks.

In Hyperopt, a trial generally corresponds to fitting one model on one setting of hyperparameters. Hyperopt iteratively generates trials, evaluates them, and repeats.

With `SparkTrials`, the driver node of your cluster generates new trials, and worker nodes evaluate those trials. Each trial is generated with a Spark job which has one task, and is evaluated in the task on a worker machine. If your cluster is set up to run multiple tasks per worker, then multiple trials may be evaluated at once on that worker.

## `SparkTrials` and MLflow[​](#sparktrials-and-mlflow "Direct link to sparktrials-and-mlflow")

Databricks Runtime ML supports logging to MLflow from workers. You can add custom logging code in the objective function you pass to Hyperopt.

`SparkTrials` logs tuning results as nested MLflow runs as follows:

*   Main or parent run: The call to `fmin()` is logged as the main run. If there is an active run, `SparkTrials` logs to this active run and does not end the run when `fmin()` returns. If there is no active run, `SparkTrials` creates a new run, logs to it, and ends the run before `fmin()` returns.
*   Child runs: Each hyperparameter setting tested (a “trial”) is logged as a child run under the main run. MLflow log records from workers are also stored under the corresponding child runs.

When calling `fmin()`, Databricks recommends active MLflow run management; that is, wrap the call to `fmin()` inside a `with mlflow.start_run():` statement. This ensures that each `fmin()` call is logged to a separate MLflow main run, and makes it easier to log extra tags, parameters, or metrics to that run.

note

When you call `fmin()` multiple times within the same active MLflow run, MLflow logs those calls to the same main run. To resolve name conflicts for logged parameters and tags, MLflow appends a UUID to names with conflicts.

When logging from workers, you do not need to manage runs explicitly in the objective function. Call `mlflow.log_param("param_from_worker", x)` in the objective function to log a parameter to the child run. You can log parameters, metrics, tags, and artifacts in the objective function.
