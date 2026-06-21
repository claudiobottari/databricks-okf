---
title: Create and connect to Ray clusters on Databricks | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ray/ray-create
ingestedAt: "2026-06-18T08:13:02.824Z"
---

Learn how to create, configure, and run Ray compute clusters on Databricks

## Requirements[​](#requirements "Direct link to Requirements")

To create a Ray cluster, you must have access to a Databricks all-purpose compute resource with the following settings:

*   Databricks Runtime 12.2 LTS ML and above.
*   Dedicated (formerly single user) or no isolation shared [access modes](https://docs.databricks.com/aws/en/compute/configure#access-modes):

note

Ray clusters are currently not supported on serverless compute.

## Install Ray[​](#install-ray "Direct link to Install Ray")

With Databricks Runtime ML 15.0 onwards, Ray is preinstalled on Databricks clusters.

For runtimes released prior to 15.0, use pip to install Ray on your cluster:

    %pip install ray[default]>=2.3.0

## Create a user-specific Ray cluster in a Databricks cluster[​](#create-a-user-specific-ray-cluster-in-a-databricks-cluster "Direct link to create-a-user-specific-ray-cluster-in-a-databricks-cluster")

To create a Ray cluster, use the [ray.util.spark.setup\_ray\_cluster](https://docs.ray.io/en/latest/cluster/vms/user-guides/community/spark.html#ray.util.spark.setup_ray_cluster) API.

note

When you create a Ray cluster in a notebook, it is only available to the current notebook user. The Ray cluster is automatically shut down after the notebook is detached from the cluster or after 30 minutes of inactivity (no tasks have been submitted to Ray). If you want to create a Ray cluster that is shared with all users and is not subject to an actively running notebook, use the `ray.util.spark.setup_global_ray_cluster` API instead.

### Fixed-size Ray cluster[​](#fixed-size-ray-cluster "Direct link to Fixed-size Ray cluster")

In any Databricks notebook that is attached to a Databricks cluster, you can run the following command to start a fixed-size Ray cluster:

Python

    import rayfrom ray.util.spark import setup_ray_cluster, shutdown_ray_clustersetup_ray_cluster(  max_worker_nodes=1,  collect_log_to_path="/dbfs/path/to/ray_collected_logs")# Pass any custom Ray configuration with ray.initray.init(ignore_reinit_error=True)

### Auto-scaling Ray cluster[​](#auto-scaling-ray-cluster "Direct link to Auto-scaling Ray cluster")

To learn how to start an auto-scaling Ray cluster, see [Scale Ray clusters on Databricks](https://docs.databricks.com/aws/en/machine-learning/ray/scale-ray).

## Starting a global mode Ray cluster[​](#starting-a-global-mode-ray-cluster "Direct link to Starting a global mode Ray cluster")

Using Ray 2.9.0 and above, you can create a global mode Ray cluster on a Databricks cluster. A global mode Ray cluster allows all users attached to the Databricks compute resource to also use the Ray cluster. This mode of running a Ray cluster doesn't have the active timeout functionality that a dedicated compute resource has when running a single user Ray cluster instance.

To start a global ray cluster that multiple users can attach to and run Ray tasks on, start by creating a Databricks notebook job and attach it to a shared mode Databricks cluster, then run the following command:

Python

    from ray.util.spark import setup_global_ray_clustersetup_global_ray_cluster(  max_worker_nodes=2,  ...  # other arguments are the same as with the `setup_global_ray` API.)

This is a blocking call that will remain active until you interrupt the call by clicking the “Interrupt” button on the notebook command cell, detaching the notebook from the Databricks cluster, or terminating the Databricks cluster. Otherwise, the global mode Ray cluster will continue to run and be available for task submission by authorized users. For more information on global mode clusters, see [Ray API Documentation](https://docs.ray.io/en/latest/ray-core/api/index.html).

Global mode clusters have the following properties:

*   In a Databricks cluster, you can only create one active global mode Ray cluster at a time.
*   In a Databricks cluster, the active global mode Ray cluster can be used by all users in any attached Databricks notebook. You can run `ray.init()` to connect to the active global mode Ray cluster. Because multiple users can access this Ray cluster, resource contention might be an issue.
*   Global mode Ray cluster is up until the `setup_ray_cluster` call is interrupted. It does not have an automatic shutdown timeout as single user Ray clusters do.

## Create a Ray GPU cluster[​](#create-a-ray-gpu-cluster "Direct link to Create a Ray GPU cluster")

For GPU clusters, these resources can be added to the Ray cluster in the following way:

Python

    from ray.util.spark import setup_ray_cluster, shutdown_ray_clustersetup_ray_cluster(  min_worker_nodes=2,  max_worker_nodes=4,  num_cpus_per_node=8,  num_gpus_per_node=1,  num_cpus_head_node=8,  num_gpus_head_node=1,  collect_log_to_path="/dbfs/path/to/ray_collected_logs")# Pass any custom Ray configuration with ray.initray.init(ignore_reinit_error=True)

## Connect to remote Ray cluster using Ray client[​](#connect-to-remote-ray-cluster-using-ray-client "Direct link to Connect to remote Ray cluster using Ray client")

In Ray version 2.3.0 and above, you can create a Ray cluster using the setup\_ray\_cluster API, and in the same notebook, you can call ray.init() API to connect to this Ray cluster. To get the remote connection string, use the following:

Python

    from ray.util.spark import setup_ray_cluster_, remote_conn_str = setup_ray_cluster(num_worker_nodes=2, ...)

Then, you can connect the remote cluster using the above remote connection string:

Python

    import rayray.init(remote_conn_str)

The Ray client does not support the Ray dataset API defined in the ray.data module. As a workaround, you can wrap your code that calls the Ray dataset API inside a remote Ray task, as shown in the following code:

Python

    import rayimport pandas as pd# Note: This must be run in the same VPC/network as the Spark cluster# so it can reach this addressray.init("ray://<ray_head_node_ip>:10001")@ray.remotedef ray_data_task():    p1 = pd.DataFrame({'a': [3,4] * 10000, 'b': [5,6] * 10000})    ds = ray.data.from_pandas(p1)    return ds.repartition(4).to_pandas()ray.get(ray_data_task.remote())

    ## Connecting the Ray Cluster to the Ray Job CLIFor many developers moving from self-managed Ray solutions to a <Databricks> solution, there is often existing infrastructure tooling built based on the Ray CLI tools. While <Databricks> currently does not support Ray Cluster CLI integration, the Ray Job CLI can be connected through the driver proxy to the Ray cluster running on <Databricks>. For example:``` shellray job submit  --headers '{"cookie" : "DATAPLANE_DOMAIN_SESSIONID=<REDACTED>"}' --address 'https://<DATABRICKS WORKSPACE URL>/driver-proxy/o/<etc>' --working-dir='.' -- python run_task.py

The values that need to be configured are the Databricks workspace URL, starting with `https://`, and then the values found after the `/driver-proxy/o/` are found in the Ray Dashboard proxy URL displayed after the Ray cluster is started.

The Ray Job CLI is used for submitting jobs to a Ray cluster from external systems but is not required for submitting jobs on Ray clusters on Databricks. It is recommended that the job be deployed using Lakeflow Jobs, a Ray cluster per application be created, and existing Databricks tooling, such as Databricks Asset Bundles or Workflow Triggers, be used to trigger the job.

## Set a log output location[​](#set-a-log-output-location "Direct link to Set a log output location")

You can set the argument `collect_log_to_path` to specify the destination path where you want to collect the Ray cluster logs. Log collection runs after the Ray cluster is shut down.

Databricks recommends setting a path starting with `/dbfs/` or Unity Catalog Volume path to preserve the logs even if you terminate the Apache Spark cluster. Otherwise, your logs are not recoverable since the local storage on the cluster is deleted when the cluster is shut down.

After creating a Ray cluster, you can run any Ray application code directly in your notebook. Click **Open Ray Cluster Dashboard in a new tab** to view the Ray dashboard for the cluster.

## Enable stack traces and flame graphs on the Ray Dashboard Actors page[​](#enable-stack-traces-and-flame-graphs-on-the-ray-dashboard-actors-page "Direct link to Enable stack traces and flame graphs on the Ray Dashboard Actors page")

On the Ray Dashboard Actors page, you can view stack traces and flame graphs for active Ray actors. To view this information, use the following command to install py-spy before you start the Ray cluster:

## Create and configure best practices[​](#create-and-configure-best-practices "Direct link to Create and configure best practices")

This section covers best practices for creating and configuring Ray clusters.

### Non-GPU workloads[​](#non-gpu-workloads "Direct link to Non-GPU workloads")

The Ray cluster runs on top of a Databricks Spark cluster. A typical scenario is to use a Spark job and Spark UDF to do simple data preprocessing tasks that do not need GPU resources. Then, use Ray to run complicated machine learning tasks that benefit from GPUs. In this case, Databricks recommends setting the Apache Spark cluster level configuration parameter spark.task.resource.gpu.amount to 0 so that all Apache Spark DataFrame transformations and Apache Spark UDF executions do not use GPU resources.

The benefits of this configuration are the following:

*   It increases Apache Spark job parallelism because the GPU instance type usually has many more CPU cores than GPU devices.
*   If the Apache Spark cluster is shared with multiple users, this configuration prevents Apache Spark jobs from competing for GPU resources with concurrently running Ray workloads.

### Disable `transformers` trainer MLflow integration if using it in Ray tasks[​](#disable-transformers-trainer-mlflow-integration-if-using-it-in-ray-tasks "Direct link to disable-transformers-trainer-mlflow-integration-if-using-it-in-ray-tasks")

The `transformers` trainer MLflow integration is enabled by default from within the `transformers` library. If you use Ray train to fine-tune a `transformers` model, Ray tasks will fail due to a credential issue. However, this issue does not apply if you directly use MLflow for training. To avoid this issue, you can set the `DISABLE_MLFLOW_INTEGRATION` environment variable to 'TRUE' from within the Databricks cluster configuration when starting your Apache Spark cluster.

### Address Ray remote function pickling error[​](#address-ray-remote-function-pickling-error "Direct link to Address Ray remote function pickling error")

To run Ray tasks, Ray pickles the task function. If you find pickling failed, you must diagnose which part of your code causes the failure. Common causes of pickling errors are the handling of external references, closures, and references to stateful objects. One of the easiest errors to verify and quickly correct can be remedied by moving import statements within the task function declaration.

For example, `datasets.load_dataset` is a widely used function that is patched in Databricks Runtime driver side, rendering the reference unpickle-able. To address it, you can simply write the task function as follows:

Python

    def ray_task_func():  from datasets import load_dataset  # import the function inside task function  ...

### Disable Ray memory monitor if the Ray task is unexpectedly killed with an out-of-memory (OOM) error[​](#disable-ray-memory-monitor-if-the-ray-task-is-unexpectedly-killed-with-an-out-of-memory-oom-error "Direct link to Disable Ray memory monitor if the Ray task is unexpectedly killed with an out-of-memory (OOM) error")

In Ray 2.9.3, Ray memory monitor has several known issues that can cause Ray tasks to be inadvertently stopped without cause. To address the issue, you can disable the Ray memory monitor by setting the environment variable `RAY_memory_monitor_refresh_ms` to `0` within the Databricks cluster configuration when starting your Apache Spark cluster.

### Applying transformation functions to batches of data[​](#applying-transformation-functions-to-batches-of-data "Direct link to Applying transformation functions to batches of data")

When processing data in batches, it is recommended to use the Ray Data API with the `map_batches` function. This approach can be more efficient and scalable, especially for large datasets or complex computations that benefit from batch processing. Any Spark DataFrame can be converted to a Ray Dataset using the `ray.data.from_spark` API. The processed output from calling this transformation API can be written out to Databricks UC tables using the API `ray.data.write_databricks_table`.

### Using MLflow in Ray tuner, Ray train or customized Ray tasks[​](#using-mlflow-in-ray-tuner-ray-train-or-customized-ray-tasks "Direct link to Using MLflow in Ray tuner, Ray train or customized Ray tasks")

Integrating Databricks MLflow and Ray requires Ray 2.41 and above.

To use MLflow with the Ray Tune, Ray Train or customized Ray tasks, set following environmental variables: `DATABRICKS_HOST` and `DATABRICKS_TOKEN`, or set the environmental variables `DATABRICKS_HOST`, `DATABRICKS_CLIENT_ID`, and `DATABRICKS_CLIENT_SECRET` before calling `ray.util.spark.setup_ray_cluster`. The following code shows how to do set these variables.

Python

    import osfrom ray.util.spark import setup_ray_clusteros.environ["DATABRICKS_HOST"] = "https://....databricks.com"os.environ["DATABRICKS_TOKEN"] = "<your PAT token"setup_ray_cluster(num_cpus_worker_node=2, num_gpus_worker_node=0, max_worker_nodes=1, min_worker_nodes=1)

### Use notebook-scoped Python libraries or cluster Python libraries in Ray tasks[​](#use-notebook-scoped-python-libraries-or-cluster-python-libraries-in-ray-tasks "Direct link to Use notebook-scoped Python libraries or cluster Python libraries in Ray tasks")

Using notebook-scoped Python libraries or cluster Python libraries in remote Ray tasks requires Ray 2.12 and above.

Ray versions 2.11 and below have a known issue where Ray tasks cannot use notebook scoped Python libraries or cluster Python libraries. For Ray versions 2.11 and below, additional dependencies must pre-install dependencies within the active session by using the `%pip` magic command prior to starting the Ray cluster.

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Start a Ray cluster on Databricks](https://docs.databricks.com/aws/en/machine-learning/ray/start-ray)
*   [Scale Ray clusters on Databricks](https://docs.databricks.com/aws/en/machine-learning/ray/scale-ray)
