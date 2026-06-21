---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 51395eaba3a4e1c6bf6912e7b7cd8230a4ffa8de8f83cab941a304e640d38a84
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-cluster-log-collection-on-databricks
    - RCLCOD
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
title: Ray cluster log collection on Databricks
description: Configuring log output destinations for Ray clusters using the collect_log_to_path argument, with recommendations for /dbfs/ or Unity Catalog Volume paths to preserve logs after cluster termination
tags:
  - ray
  - databricks
  - logging
timestamp: "2026-06-18T14:49:57.143Z"
---

# Ray Cluster Log Collection on Databricks

**Ray cluster log collection on Databricks** refers to the process of collecting and persisting logs from a [Ray cluster](/concepts/global-mode-ray-cluster.md) running on a Databricks Spark cluster. By default, logs exist only on the local storage of the cluster's nodes and are lost when the cluster terminates. Proper configuration ensures logs are saved to durable storage for debugging and auditing.

## Overview

When a Ray cluster is created via `ray.util.spark.setup_ray_cluster`, the `collect_log_to_path` argument specifies a destination directory where Ray cluster logs are collected. Log collection occurs automatically after the Ray cluster shuts down, not continuously during runtime. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Configuration

Set the `collect_log_to_path` parameter when calling `setup_ray_cluster`:

```python
from ray.util.spark import setup_ray_cluster

setup_ray_cluster(
    max_worker_nodes=1,
    collect_log_to_path="/dbfs/path/to/ray_collected_logs"
)
```

Databricks recommends using a path starting with `/dbfs/` or a Unity Catalog Volume path. These provide durable storage that persists even after the Apache Spark cluster is terminated. If a non-persistent path is used (e.g., a local node directory), the logs are not recoverable once the cluster shuts down. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Log Collection Timing

Logs are gathered only after the Ray cluster is shut down. The collection process runs as part of the shutdown lifecycle. This means logs are not available in real-time during a Ray task; they must be retrieved from the output path after the Ray cluster has stopped. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Best Practices

- **Always set `collect_log_to_path`** with a durable storage location to avoid losing diagnostic information.
- **Use `/dbfs/` or a Unity Catalog Volume** to ensure logs survive cluster termination.
- **Verify the path** is writable by the Spark driver process that hosts the Ray cluster.

## Related Concepts

- [Ray Cluster on Databricks](/concepts/ray-cluster-on-databricks.md)
- Ray dashboard
- Unity Catalog Volumes
- Spark cluster logging

## Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
