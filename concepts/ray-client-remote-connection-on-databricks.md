---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b50b5ab4d16b6c54d61388b810094ad91c1a88d88ab6372c3dd6367c6f18321
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-client-remote-connection-on-databricks
    - RCRCOD
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
title: Ray Client Remote Connection on Databricks
description: Using the Ray client (Ray 2.3.0+) to connect to a remote Ray cluster on Databricks via a connection string, with limitations on Ray Dataset API
tags:
  - ray
  - remote-connection
  - databricks
timestamp: "2026-06-19T14:32:05.938Z"
---

# Ray Client Remote Connection on Databricks

**Ray Client Remote Connection on Databricks** refers to the ability to create a Ray cluster on a Databricks cluster and then connect to it from another process or notebook using the Ray Client API. This enables remote submission of Ray tasks without requiring the client to be running on the same cluster that hosts the Ray head node. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Requirements

To use the Ray Client remote connection on Databricks, you need:

- Databricks Runtime 12.2 LTS ML and above (Ray is preinstalled from Runtime 15.0 ML onwards; for earlier versions you must install it via `%pip install ray[default]>=2.3.0`).
- A Databricks all-purpose compute resource with **dedicated** (formerly single user) or **no isolation shared** access mode.
- Ray version 2.3.0 or above. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

Ray clusters are not supported on serverless compute. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Obtaining the Remote Connection String

When you create a Ray cluster using `ray.util.spark.setup_ray_cluster`, the function returns a remote connection string. The string typically follows the format `ray://<ray_head_node_ip>:10001`. You can capture it by assigning the return value: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
from ray.util.spark import setup_ray_cluster

_, remote_conn_str = setup_ray_cluster(num_worker_nodes=2, ...)
```

The remote connection string can then be shared with other processes that have network access to the Databricks cluster (they must be in the same VPC/network). ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Connecting with `ray.init`

Once you have the remote connection string, any Python environment that can reach the Ray head node can connect to the cluster using `ray.init()`: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
import ray
ray.init(remote_conn_str)
```

After a successful connection, you can submit Ray remote tasks as usual. The remote client can be a separate notebook or an external script.

## Limitations and Workarounds

### Ray Dataset API

The Ray Client does not support the `ray.data` API directly. Calling `ray.data` operations (such as `ray.data.from_pandas()`) on a remote client will fail. As a workaround, wrap any code that uses the Ray Dataset API inside a remote Ray task: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
@ray.remote
def ray_data_task():
    import pandas as pd
    p1 = pd.DataFrame({'a': [3,4] * 10000, 'b': [5,6] * 10000})
    ds = ray.data.from_pandas(p1)
    return ds.repartition(4).to_pandas()

ray.get(ray_data_task.remote())
```

### Network Requirements

The client must be in the same VPC or network as the Spark cluster to reach the Ray head node address. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Connecting the Ray Job CLI

For teams that have existing infrastructure tooling built on the Ray Job CLI, you can connect it through the Databricks driver proxy to the Ray cluster. The address is formed as: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```
https://<DATABRICKS_WORKSPACE_URL>/driver-proxy/o/<value>
```

The `<value>` after `/driver-proxy/o/` can be found in the Ray Dashboard proxy URL that is displayed after the Ray cluster starts. You must also provide a session cookie. An example submission: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```shell
ray job submit \
  --headers '{"cookie" : "DATAPLANE_DOMAIN_SESSIONID=<REDACTED>"}' \
  --address 'https://<workspace>/driver-proxy/o/<etc>' \
  --working-dir='.' \
  -- python run_task.py
```

The Ray Job CLI is not required for submitting jobs on Ray clusters on Databricks. Databricks recommends using [Lakeflow Jobs](/concepts/lakeflow-jobs.md) with a Ray cluster per application, and leveraging existing Databricks tooling such as Databricks Asset Bundles or Workflow Triggers to trigger the job. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Best Practices

- Obtain the remote connection string from `setup_ray_cluster` in the same notebook where the Ray cluster is created, and then share the string with other processes that need to connect.
- If you need a [Global Mode Ray Cluster](/concepts/global-mode-ray-cluster.md) (shared across users), use `setup_global_ray_cluster` instead. A global cluster remains active until interrupted and does not have an automatic shutdown timeout.
- When using [MLflow](/concepts/mlflow.md) inside Ray tasks (Ray 2.41+ required), set the environment variables `DATABRICKS_HOST` and `DATABRICKS_TOKEN` (or `DATABRICKS_CLIENT_ID` and `DATABRICKS_CLIENT_SECRET`) before calling `setup_ray_cluster`. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Ray Cluster](/concepts/global-mode-ray-cluster.md) — The Ray compute cluster running on Databricks
- Ray Client — The API for connecting to a remote Ray cluster
- Ray Dataset — Ray's distributed data API (not supported over client)
- Ray Job CLI — CLI for submitting jobs to a Ray cluster
- Driver Proxy — Databricks mechanism for reaching cluster services
- [Global Mode Ray Cluster](/concepts/global-mode-ray-cluster.md) — A Ray cluster shared by all users of a Databricks cluster
- MLflow Integration with Ray — Using MLflow tracking within Ray tasks

## Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
