---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e933749c4a6f28c606946a510317e484392c1817db7dd9b43b22c62eb889a286
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-client-remote-connection
    - RCRC
    - ray-client-remote-connection-on-databricks
    - RCRCOD
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
title: Ray Client Remote Connection
description: Connecting to a remote Ray cluster from a Databricks notebook using the Ray client with a connection string obtained from setup_ray_cluster
tags:
  - ray
  - networking
  - databricks
timestamp: "2026-06-19T17:57:55.061Z"
---

# Ray Client Remote Connection

**Ray Client Remote Connection** refers to the ability to connect to a [Ray cluster](/concepts/global-mode-ray-cluster.md) running on a Databricks compute resource from a different notebook or application using the Ray client API. This is supported in Ray version 2.3.0 and above, and it allows users to submit Ray tasks to a remote cluster without needing to run the Ray driver process on the same machine as the cluster.

## Obtaining the Remote Connection String

When creating a Ray cluster with the `setup_ray_cluster` API, you can capture the remote connection string by using the underscore variant `setup_ray_cluster_`. This variant returns a tuple where the second element is the connection string: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
from ray.util.spark import setup_ray_cluster_

_, remote_conn_str = setup_ray_cluster(
    num_worker_nodes=2,
    ...
)
```

The returned `remote_conn_str` is a URL of the form `ray://<ray_head_node_ip>:10001`. You can then connect to the cluster from another process or notebook by calling `ray.init()` with this string: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
import ray
ray.init(remote_conn_str)
```

> **Note:** The connecting client must reside within the same VPC or network as the Spark cluster so that it can reach the Ray head node address.

## Limitations with the Ray Dataset API

The Ray client does not support the Ray Dataset API defined in the `ray.data` module when called directly through the client. As a workaround, you can wrap code that uses the Ray Dataset API inside a remote Ray task: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
import ray
import pandas as pd

ray.init("ray://<ray_head_node_ip>:10001")

@ray.remote
def ray_data_task():
    p1 = pd.DataFrame({'a': [3,4] * 10000, 'b': [5,6] * 10000})
    ds = ray.data.from_pandas(p1)
    return ds.repartition(4).to_pandas()

ray.get(ray_data_task.remote())
```

This approach executes the dataset operations on the remote Ray cluster and returns the result to the client.

## Connecting the Ray Job CLI

For users migrating from self-managed Ray solutions, the Ray Job CLI can be connected to a Ray cluster running on Databricks using the driver proxy URL. The command takes the form: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```shell
ray job submit \
  --headers '{"cookie" : "DATAPLANE_DOMAIN_SESSIONID=<REDACTED>"}' \
  --address 'https://<DATABRICKS WORKSPACE URL>/driver-proxy/o/<etc>' \
  --working-dir='.' \
  -- python run_task.py
```

The `<DATABRICKS WORKSPACE URL>` and the path segments after `/driver-proxy/o/` are taken from the Ray Dashboard proxy URL displayed after the Ray cluster is started.

While the Ray Job CLI is available, Databricks recommends deploying jobs using [Lakeflow Jobs](/concepts/lakeflow-jobs.md), creating a Ray cluster per application, and using existing Databricks tooling such as Databricks Asset Bundles or Workflow Triggers to trigger the job.

## Best Practices for Remote Connections

When using MLflow within Ray remote tasks (Ray Tune, Ray Train, or custom Ray tasks – supported from Ray 2.41 and above), set the environment variables `DATABRICKS_HOST` and `DATABRICKS_TOKEN` (or the OAuth equivalents) **before** calling `setup_ray_cluster` to ensure the Ray workers can authenticate with Databricks MLflow: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
import os
from ray.util.spark import setup_ray_cluster

os.environ["DATABRICKS_HOST"] = "https://....databricks.com"
os.environ["DATABRICKS_TOKEN"] = "<your PAT token>"

setup_ray_cluster(
    num_cpus_worker_node=2,
    num_gpus_worker_node=0,
    max_worker_nodes=1,
    min_worker_nodes=1,
)
```

## Related Concepts

- [Ray Cluster on Databricks](/concepts/ray-cluster-on-databricks.md) – Overview of creating and managing Ray clusters.
- setup_ray_cluster – The primary API for starting a Ray cluster on Databricks.
- Ray Client – The general Ray client library for remote execution.
- Ray Job CLI – Command-line tool for submitting jobs to a Ray cluster.
- MLflow Integration with Ray – Using MLflow tracking in distributed Ray workloads.

## Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
