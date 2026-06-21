---
title: Scale Ray clusters on Databricks | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ray/scale-ray
ingestedAt: "2026-06-18T08:13:06.475Z"
---

Learn how to tune the size of your Ray cluster for optimal performance, including autoscaling, head node configuration, heterogeneous clusters, and resource allocation.

## Create a Ray cluster in autoscaling mode[​](#create-a-ray-cluster-in-autoscaling-mode "Direct link to Create a Ray cluster in autoscaling mode")

In Ray 2.8.0 and above, Ray clusters started on Databricks support integration with Databricks autoscaling. This autoscaling integration triggers Databricks cluster autoscaling internally within the Databricks environment.

To enable autoscaling, run the following command:

For Ray version below 2.10:

Python

    from ray.util.spark import setup_ray_clustersetup_ray_cluster(  num_worker_nodes=8,  autoscale=True,)

For Ray version 2.10 and onwards:

Python

    from ray.util.spark import setup_ray_cluster, shutdown_ray_clustersetup_ray_cluster(  min_worker_nodes=2,  max_worker_nodes=4,  num_cpus_per_node=4,  collect_log_to_path="/dbfs/path/to/ray_collected_logs")# Pass any custom Ray configuration with ray.initray.init(ignore_reinit_error=True)

The `ray.util.spark.setup_ray_cluster` API creates a Ray cluster on Apache Spark. Internally, it creates a background Apache Spark job. Each Apache Spark task in the job creates a Ray worker node, and the Ray head node is created on the driver. The arguments `min_worker_nodes` and `max_worker_nodes` represent the range of Ray worker nodes to create and utilize for Ray workloads. If the argument `min_worker_nodes` is left undefined, a fixed-size Ray cluster will be started with `max_worker_nodes` number of workers available. To specify the number of CPU or GPU cores assigned to each Ray worker node, set the argument `num_cpus_worker_node` (default value: 1) or `num_gpus_worker_node` (default value: 0).

For Ray version below 2.10, if autoscaling is enabled, `num_worker_nodes` indicates the maximum number of Ray worker nodes. The default minimum number of Ray worker nodes is zero. This default setting means that when the Ray cluster is idle, it scales down to zero Ray worker nodes. This might not be ideal for fast responsiveness in all scenarios, but it can significantly reduce costs when enabled.

In autoscaling mode, num\_worker\_nodes cannot be set to `ray.util.spark.MAX_NUM_WORKER_NODES`.

The following arguments configure the upscaling and downscaling speed:

*   `autoscale_upscaling_speed` represents the number of nodes allowed to be pending as a multiple of the current number of nodes. The higher the value, the more aggressive the upscaling. For example, if this is set to 1.0, the cluster can grow in size by at most 100% at any time.
*   `autoscale_idle_timeout_minutes` represents the number of minutes that need to pass before the autoscaler removes an idle worker node. The smaller the value, the more aggressive the downscaling.

With Ray 2.9.0 and above, you can also set `autoscale_min_worker_nodes` to prevent the Ray cluster from scaling down to zero workers when the Ray cluster is idle, which would cause the cluster to terminate.

## Configure resources used by the Ray head node[​](#configure-resources-used-by-the-ray-head-node "Direct link to Configure resources used by the Ray head node")

By default, for the Ray on Spark configuration, Databricks restricts resources allocated to the Ray head node to:

*   0 CPU cores
*   0 GPUs
*   128 MB heap memory
*   128 MB object store memory

This is because the Ray head node is usually used only for global coordination, not for running Ray tasks. The Apache Spark driver node resources are shared with multiple users, so the default setting saves resources on the Apache Spark driver side. With Ray 2.8.0 and above, you can configure resources used by the Ray head node. Use the following arguments in the setup\_ray\_cluster API:

*   `num_cpus_head_node`: setting CPU cores used by Ray head node
*   `num_gpus_head_node`: setting GPU used by Ray head node
*   `object_store_memory_head_node`: setting object store memory size by Ray head node

## Support for heterogeneous clusters[​](#support-for-heterogeneous-clusters "Direct link to Support for heterogeneous clusters")

You can create a Ray on Spark cluster for more efficient and cost-effective training runs and set different configurations between the Ray head node and Ray worker nodes. However, all Ray worker nodes must have the same configuration. Databricks clusters do not fully support heterogeneous clusters, but you can create a Databricks cluster with different driver and worker instance types by setting a cluster policy. For example:

    {  "node_type_id": {    "type": "fixed",    "value": "i3.xlarge"  },  "driver_node_type_id": {    "type": "fixed",    "value": "g4dn.xlarge"  },  "spark_version": {    "type": "fixed",    "value": "13.x-snapshot-gpu-ml-scala2.12"  }}

## Tune the Ray cluster configuration[​](#tune-the-ray-cluster-configuration "Direct link to Tune the Ray cluster configuration")

The recommended configuration for each Ray worker node is as follows: Minimum 4 CPU cores per Ray worker node. Minimum 10GB heap memory for each Ray worker node.

So, when calling `ray.util.spark.setup_ray_cluster`, Databricks recommends setting `num_cpus_per_node` to a value greater than or equal to 4.

See the next section for details about tuning heap memory for each Ray worker node.

### Memory allocation for Ray worker nodes[​](#memory-allocation-for-ray-worker-nodes "Direct link to Memory allocation for Ray worker nodes")

Each Ray worker node uses two types of memory: heap memory and object store memory.

The allocated memory size for each type is determined as described below.

The total memory allocated to each Ray worker node is: `RAY_WORKER_NODE_TOTAL_MEMORY = (SPARK_WORKER_NODE_PHYSICAL_MEMORY / MAX_NUMBER_OF_LOCAL_RAY_WORKER_NODES * 0.8)`

`MAX_NUMBER_OF_LOCAL_RAY_WORKER_NODES` is the maximum number of Ray worker nodes that can be launched on the Apache Spark worker node. This is determined by the argument `num_cpus_per_node` or `num_gpus_per_node`.

If you do not set the argument `object_store_memory_per_node`, then the heap memory size and object store memory size allocated to each Ray worker node are: `RAY_WORKER_NODE_HEAP_MEMORY = RAY_WORKER_NODE_TOTAL_MEMORY * 0.7` `OBJECT_STORE_MEMORY_PER_NODE = RAY_WORKER_NODE_TOTAL_MEMORY * 0.3`

If you do set the argument `object_store_memory_per_node`: `RAY_WORKER_NODE_HEAP_MEMORY = RAY_WORKER_NODE_TOTAL_MEMORY - argument_object_store_memory_per_node`

In addition, the object store memory size per Ray worker node is limited by the shared memory of the operating system. The maximum value is: `OBJECT_STORE_MEMORY_PER_NODE_CAP = (SPARK_WORKER_NODE_OS_SHARED_MEMORY / MAX_NUMBER_OF_LOCAL_RAY_WORKER_NODES * 0.8)`

`SPARK_WORKER_NODE_OS_SHARED_MEMORY` is the `/dev/shm` disk size configured for the Apache Spark worker node.

## Scaling best practice[​](#scaling-best-practice "Direct link to Scaling best practice")

### Set the CPU and GPU number for each Ray worker node[​](#set-the-cpu-and-gpu-number-for-each-ray-worker-node "Direct link to Set the CPU and GPU number for each Ray worker node")

We recommend setting the argument `num_cpus_worker_node` to the number of CPU cores per Apache Spark worker node. Similarly, setting `num_gpus_worker_node` to the number of GPUs per Apache Spark worker node is optimal. With this configuration, each Apache Spark worker node launches one Ray worker node that will fully utilize the resources of each Apache Spark worker node.

Set the environment variable `RAY_memory_monitor_refresh_ms` to `0` within the Databricks cluster configuration when starting your Apache Spark cluster.

### Memory resource configuration for Apache Spark and Ray hybrid workloads[​](#memory-resource-configuration-for-apache-spark-and-ray-hybrid-workloads "Direct link to memory-resource-configuration-for-apache-spark-and-ray-hybrid-workloads")

If you run hybrid Spark and Ray workloads in a Databricks cluster, Databricks recommends you reduce the Spark executor memory to a small value. For example, set `spark.executor.memory 4g` in the Databricks cluster config.

The Apache Spark executor is a Java process that triggers GC lazily, and the Apache Spark dataset cache uses a lot of Apache Spark executor memory. This reduces the available memory that Ray can use. To avoid potential out-of-memory errors, reduce the `spark.executor.memory` config.

### Computation resource configuration for Apache Spark and Ray hybrid workloads[​](#computation-resource-configuration-for-apache-spark-and-ray-hybrid-workloads "Direct link to computation-resource-configuration-for-apache-spark-and-ray-hybrid-workloads")

If you run hybrid Spark and Ray workloads in a Databricks cluster, we recommend that you make either cluster nodes or Ray worker nodes auto-scalable. For example:

If you have a fixed number of worker nodes available to start a Databricks cluster, we recommend that you enable Ray-on-Spark autoscaling. When no Ray workloads are running, the Ray cluster will scale down, allowing resources to be freed for use by Apache Spark tasks. When Apache Spark tasks are finished, and Ray is used again, the Ray-on-Spark cluster will again scale up to meet the demand.

Furthermore, you can make the Databricks and Ray-on-spark clusters auto-scalable. For example, if you configure the Databricks cluster's auto-scalable nodes to a maximum of 10 nodes, configure the Ray-on-Spark worker nodes to a maximum of four nodes, and configure each Ray worker node to fully utilize the resources of each Apache Spark worker, Ray workloads can use at most four nodes resources on such a cluster configuration. In comparison, Apache Spark jobs can allocate at most six nodes worth of resources.
