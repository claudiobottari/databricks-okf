---
title: When to use Spark vs. Ray | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ray/spark-ray-overview
ingestedAt: "2026-06-18T08:13:08.412Z"
---

With Databricks, you can run Ray and Spark operations in the same execution environment. Having both engines available provides a powerful solution to distribute nearly any type of Python application.

In general, Spark and Ray have their unique advantages for specific tasks types.

Ray excels at **task parallelism** - Run a set of independent tasks concurrently.

Spark excels at **data parallelism** - Apply the same operation to each element of a large dataset.

## When to use Spark[​](#when-to-use-spark "Direct link to When to use Spark")

*   **Large-scale data processing**: For most use cases involving extensive data processing, Spark is highly recommended due to its optimization for tasks like table joins, filtering, and aggregation.
*   **Data parallelism**: Spark excels at data parallelism, which involves applying the same operation to each element of a large dataset. It's ideal for ETL, analytics reporting, feature engineering, and data preprocessing.
*   **Machine learning**: Spark's MLlib and SparkML libraries are optimized for large-scale machine learning algorithms and statistical modeling.

## When to use Ray[​](#when-to-use-ray "Direct link to When to use Ray")

*   **Task parallelism**: Ray is designed for task parallelism, where multiple tasks run concurrently and independently. It's particularly efficient for computation-focused tasks.
*   **Specific workloads**: Use Ray for workloads where Spark is less optimized, such as reinforcement learning, hierarchical time series forecasting, simulation modeling, hyperparameter search, deep learning training, and high-performance computing (HPC).

## When to use both Ray and Spark[​](#when-to-use-both-ray-and-spark "Direct link to When to use both Ray and Spark")

*   **Shared mode execution**: You can run a Ray cluster within the same environment as Spark, allowing you to leverage both frameworks in a single application. Use Spark for data-intensive tasks and switch to Ray for stages that require heavy computation.
*   **Efficient data retrieval**: In some cases, Spark can be used solely for efficient data retrieval, while Ray handles the complex computational tasks.

## Workflow architecture patterns[​](#workflow-architecture-patterns "Direct link to Workflow architecture patterns")

The following are recommended patterns for integrating Spark and Ray pipelines within the same workflow.

### Isolate ETL in a subtask[​](#isolate-etl-in-a-subtask "Direct link to Isolate ETL in a subtask")

You can isolate and separate the main data extract-transform-load (ETL) portion into its own subtask within a Databricks Workflow. This lets you match the cluster type to the type of ETL workload and avoid resource sharing issues between Ray and Spark.

### Combine Ray and Spark in a single task[​](#combine-ray-and-spark-in-a-single-task "Direct link to Combine Ray and Spark in a single task")

To combine Ray and Spark in a single task, Databricks recommends one of the following patterns:

*   **Spark for data handling, Ray for computation**
    
    Use Spark to manage input and output data operations. For example, use `databricks.ray.data.from_spark` to pass training data from Spark to Ray Data. Save the output model to MLflow or a data set to Unity Catalog tables.
    
*   **Ray inside a Spark functions (advanced)**
    
    Run Ray within Spark functions like UDFs or Structured Streaming `foreachBatch` operations.
    
*   **Concurrent Spark and Ray operations (advanced)**
    
    Run Spark operations alongside Ray functions. For example, use Spark to query data within Ray tasks or to write output data while Ray is still running.
    

To learn more about combining Ray and Spark in a single task, see [Combine Ray and Spark in the same environment on Databricks](https://docs.databricks.com/aws/en/machine-learning/ray/connect-spark-ray)

### Resource management while combining Ray and Spark in a single task[​](#resource-management-while-combining-ray-and-spark-in-a-single-task "Direct link to Resource management while combining Ray and Spark in a single task")

Resource conflicts are rare due to task scheduling but can be managed by configuring resource allocation to ensure that both frameworks have sufficient memory, CPU, and/or GPU availability.

The following example shows how to use the setup configuration arguments when starting your Ray cluster to split resources between Ray and Spark. Adjust the cluster size or the number of CPUs allocated to Ray worker nodes as needed to prevent contention.

Python

    from ray.util.spark import setup_ray_cluster, shutdown_ray_cluster# For a Databricks cluster configured with autoscaling enabled,# The minimum worker nodes of 4 and maximum of 6 nodes.# 2 Spark-only nodes will launch when needed.# The Ray cluster will have 4 nodes allocated for its use.setup_ray_cluster(  min_worker_nodes=4,  max_worker_nodes=4,)# Pass any custom Ray configuration with ray.initray.init()

## Next steps[​](#next-steps "Direct link to Next steps")

Learn how to [connect Spark and Ray](https://docs.databricks.com/aws/en/machine-learning/ray/connect-spark-ray) to pass data between them for shared workloads.
