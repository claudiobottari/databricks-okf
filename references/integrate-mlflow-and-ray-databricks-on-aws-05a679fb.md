---
title: Integrate MLflow and Ray | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ray/ray-mlflow
ingestedAt: "2026-06-18T08:13:04.549Z"
---

MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models. MLflow enables teams of all sizes to debug, evaluate, monitor, and optimize their AI applications while controlling costs and managing access to models and data. With over 30 million monthly downloads, thousands of organizations rely on MLflow each day to ship AI to production with confidence. Combining Ray with MLflow allows you to distribute workloads with Ray and track models, metrics, parameters, and metadata generated during training with MLflow.

This article covers how to integrate MLflow with the following Ray components:

*   [Ray Core](#ray-core): General-purpose distributed applications that aren't covered by Ray Tune and Ray Train
*   [Ray Train](#ray-train): Distributed model training
*   [Ray Tune](#ray-tune): Distributed hyperparameter tuning

*   [Model Serving](#model-serving): Deploying models for real-time inference

## Integrate Ray Core and MLflow[​](#integrate-ray-core-and-mlflow "Direct link to integrate-ray-core-and-mlflow")

Ray Core provides the foundational building blocks for general-purpose distributed applications. It allows you to scale Python functions and classes across multiple nodes.

This section describes the following patterns to integrate Ray Core and MLflow:

*   Log MLflow models from the Ray driver process
*   Log MLflow models from child runs

### Log MLflow from the Ray driver process[​](#log-mlflow-from-the-ray-driver-process "Direct link to Log MLflow from the Ray driver process")

It's generally best to log MLflow models from the driver process rather than from worker nodes. This is due to the added complexity of passing stateful references to the remote workers.

For instance, the following code fails because the MLflow Tracking Server isn't initialized using the `MLflow Client` from within worker nodes.

Python

    import mlflow@ray.remotedef example_logging_task(x):# ... # This method will fail mlflow.log_metric("x", x) return xwith mlflow.start_run() as run: ray.get([example_logging_task.remote(x) for x in range(10)])

Instead, return the metrics to the driver node. The metrics and metadata are generally small enough to transfer back to the driver without causing memory issues.

Take the example shown above and update it to log the returned metrics from a Ray task:

Python

    import mlflow@ray.remotedef example_logging_task(x): # ... return xwith mlflow.start_run() as run:  results = ray.get([example_logging_task.remote(x) for x in range(10)]) for x in results:   mlflow.log_metric("x", x)

For tasks that require saving large artifacts, such as a large Pandas table, images, plots, or models, Databricks recommends persisting the artifact as a file. Then, either reload the artifact within the driver context or directly log the object with MLflow by specifying the path to the saved file.

Python

    import mlflow@ray.remotedef example_logging_task(x):# ...# Create a large object that needs to be storedwith open("/dbfs/myLargeFilePath.txt", "w") as f:  f.write(myLargeObject)return xwith mlflow.start_run() as run: results = ray.get([example_logging_task.remote(x) for x in range(10)])for x in results:  mlflow.log_metric("x", x)  # Directly log the saved file by specifying the path  mlflow.log_artifact("/dbfs/myLargeFilePath.txt")

### Log Ray tasks as MLflow child runs[​](#log-ray-tasks-as-mlflow-child-runs "Direct link to Log Ray tasks as MLflow child runs")

You can integrate Ray Core with MLflow by using child runs. This involves the following steps:

1.  Create a parent run: Initialize a parent run in the driver process. This run acts as a hierarchical container for all subsequent child runs.
2.  Create child runs: Within each Ray task, initiate a child run under the parent run. Each child run can independently log its own metrics.

To implement this approach, ensure that each Ray task receives the necessary client credentials and the parent `run_id`. This setup establishes the hierarchical parent-child relationship between runs. The following code snippet demonstrates how to retrieve the credentials and pass along the parent `run_id`:

Python

    from mlflow.utils.databricks_utils import get_databricks_env_varsmlflow_db_creds = get_databricks_env_vars("databricks")username = "" # Username pathexperiment_name = f"/Users/{username}/mlflow_test"mlflow.set_experiment(experiment_name)@ray.remotedef ray_task(x, run_id):   import os  # Set the MLflow credentials within the Ray task   os.environ.update(mlflow_db_creds)  # Set the active MLflow experiment within each Ray task   mlflow.set_experiment(experiment_name)  # Create nested child runs associated with the parent run_id   with mlflow.start_run(run_id=run_id, nested=True):    # Log metrics to the child run within the Ray task       mlflow.log_metric("x", x)  return x# Start parent run on the main driver processwith mlflow.start_run() as run:  # Pass the parent run's run_id to each Ray task   results = ray.get([ray_task.remote(x, run.info.run_id) for x in range(10)])

## Ray Train and MLflow[​](#ray-train-and-mlflow "Direct link to ray-train-and-mlflow")

The simplest way to log the Ray Train models to MLflow is to use the checkpoint generated by the training run. After the training run completes, reload the model in its native deep learning framework (such as PyTorch or TensorFlow), then log it with the corresponding MLflow code.

This approach ensures the model is stored correctly and ready for evaluation or deployment.

The following code reloads a model from a Ray Train checkpoint and logs it to MLflow:

Python

    result = trainer.fit()checkpoint = result.checkpointwith checkpoint.as_directory() as checkpoint_dir:     # Change as needed for different DL frameworks    checkpoint_path = f"{checkpoint_dir}/checkpoint.ckpt"    # Load the model from the checkpoint    model = MyModel.load_from_checkpoint(checkpoint_path)with mlflow.start_run() as run:    # Change the MLflow flavor as needed    mlflow.pytorch.log_model(model, "model")

Although it's generally a best practice to send objects back to the driver node, with Ray Train, saving the final results is easier than the whole training history from the worker process.

To store multiple models from a training run, specify the number of checkpoints to keep in the `ray.train.CheckpointConfig`. The models can then be read and logged the same way as storing a single model.

note

MLflow is not responsible for handling fault tolerance during model training but rather for tracking the model's lifecycle. Fault tolerance is instead managed by Ray Train itself.

To store the training metrics specified by Ray Train, retrieve them from the result object and store them using MLflow.

Python

    result = trainer.fit()with mlflow.start_run() as run:    mlflow.log_metrics(result.metrics_dataframe.to_dict(orient='dict'))  # Change the MLflow flavor as needed    mlflow.pytorch.log_model(model, "model")

To properly configure your Spark and Ray clusters and prevent resource allocation issues, you should adjust the `resources_per_worker` setting. Specifically, set the number of CPUs for each Ray worker to be one less than the total number of CPUs available on a Ray worker node. This adjustment is crucial because if the trainer reserves all available cores for Ray actors, it can lead to resource contention errors.

## Ray Tune and MLflow[​](#ray-tune-and-mlflow "Direct link to ray-tune-and-mlflow")

Integrating Ray Tune with MLflow allows you to efficiently track and log hyperparameter tuning experiments within Databricks. This integration leverages MLflow's experiment-tracking capabilities to record metrics and results directly from Ray tasks.

### Child-run approach for logging[​](#child-run-approach-for-logging "Direct link to Child-run approach for logging")

Similar to logging from Ray Core tasks, Ray Tune applications can use a child-run approach to log metrics from each trial or tuning iteration. Use the following steps to implement a child-run approach:

1.  Create a parent run: Initialize a parent run in the driver process. This run serves as the main container for all subsequent child runs.
2.  Log child runs: Each Ray Tune task creates a child run under the parent run, maintaining a clear hierarchy of experiment results.

The following example demonstrates how to authenticate and log from Ray Tune tasks using MLflow.

Python

    import osimport tempfileimport timeimport mlflowfrom mlflow.utils.databricks_utils import get_databricks_env_varsfrom ray import train, tunefrom ray.air.integrations.mlflow import MLflowLoggerCallback, setup_mlflowmlflow_db_creds = get_databricks_env_vars("databricks")EXPERIMENT_NAME = "/Users/<WORKSPACE_USERNAME>/setup_mlflow_example"mlflow.set_experiment(EXPERIMENT_NAME)def evaluation_fn(step, width, height):   return (0.1 + width * step / 100) ** (-1) + height * 0.1def train_function_mlflow(config, run_id):   os.environ.update(mlflow_db_creds)   mlflow.set_experiment(EXPERIMENT_NAME)   # Hyperparameters   width = config["width"]   height = config["height"]   with mlflow.start_run(run_id=run_id, nested=True):       for step in range(config.get("steps", 100)):           # Iterative training function - can be any arbitrary training procedure           intermediate_score = evaluation_fn(step, width, height)           # Log the metrics to MLflow           mlflow.log_metrics({"iterations": step, "mean_loss": intermediate_score})           # Feed the score back to Tune.           train.report({"iterations": step, "mean_loss": intermediate_score})           time.sleep(0.1)def tune_with_setup(run_id, finish_fast=True):   os.environ.update(mlflow_db_creds)   # Set the experiment or create a new one if it does not exist.   mlflow.set_experiment(experiment_name=EXPERIMENT_NAME)   tuner = tune.Tuner(       tune.with_parameter(train_function_mlflow, run_id),       tune_config=tune.TuneConfig(num_samples=5),       run_config=train.RunConfig(           name="mlflow",       ),       param_space={           "width": tune.randint(10, 100),           "height": tune.randint(0, 100),           "steps": 20 if finish_fast else 100,       },   )   results = tuner.fit()with mlflow.start_run() as run:   mlflow_tracking_uri = mlflow.get_tracking_uri()   tune_with_setup(run.info.run_id)

## Model Serving[​](#model-serving "Direct link to model-serving")

Using Ray Serve on Databricks clusters for real-time inference poses challenges due to network security and connectivity limitations when interacting with external applications.

Databricks recommends using [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) to deploy machine learning models in production to a REST API endpoint. For more information, see [Custom models overview](https://docs.databricks.com/aws/en/machine-learning/model-serving/custom-models).
