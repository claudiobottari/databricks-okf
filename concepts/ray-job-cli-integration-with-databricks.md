---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0b855a8a1bd752fe1f8c920c6941533824bb9a8fdfdfde7a172a04ff61bad858
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-job-cli-integration-with-databricks
    - RJCIWD
    - Power BI Integration with Databricks
    - Tableau Integration with Databricks
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
title: Ray Job CLI integration with Databricks
description: Using the Ray Job CLI to submit jobs to Ray clusters running on Databricks via the driver proxy, alongside recommendations for using Lakeflow Jobs instead
tags:
  - ray
  - databricks
  - cli
  - job-submission
timestamp: "2026-06-18T14:50:09.574Z"
---

# Ray Job CLI Integration with Databricks

**Ray Job CLI integration with Databricks** refers to the ability to submit jobs to a Ray cluster running on Databricks using the Ray Job CLI tool. While Databricks does not support native Ray Cluster CLI integration, the Ray Job CLI can connect through the Databricks driver proxy to submit and manage jobs on Ray clusters. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Overview

The Ray Job CLI provides a command-line interface for submitting jobs to Ray clusters from external systems. For teams migrating from self-managed Ray solutions to Databricks, this integration allows them to leverage existing infrastructure tooling built around the Ray CLI tools. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Connecting to a Ray Cluster

To use the Ray Job CLI with a Databricks Ray cluster, you submit jobs using the `ray job submit` command with specific connection parameters. The connection requires two key pieces of information: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

1. **Databricks workspace URL** — The full HTTPS URL of your Databricks workspace.
2. **Driver proxy path** — The path segment after `/driver-proxy/o/`, which is found in the Ray Dashboard proxy URL displayed after the Ray cluster is started.

### Example Command

```shell
ray job submit \
  --headers '{"cookie" : "DATAPLANE_DOMAIN_SESSIONID=<REDACTED>"}' \
  --address 'https://<DATABRICKS WORKSPACE URL>/driver-proxy/o/<etc>' \
  --working-dir='.' \
  -- python run_task.py
```

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Required Parameters

- `--address`: The full proxy URL combining the Databricks workspace URL with the driver proxy path.
- `--headers`: Authentication cookie header with a valid session ID.
- `--working-dir`: The directory containing the job files.
- The Python script and its arguments to execute as the Ray job.

## Alternative Approach: Ray Client API

As an alternative to the Ray Job CLI, you can connect to the same Ray cluster using the Ray Client API programmatically: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
import ray

# Get the remote connection string when creating the Ray cluster
from ray.util.spark import setup_ray_cluster
_, remote_conn_str = setup_ray_cluster(num_worker_nodes=2, ...)

# Connect to the remote cluster
ray.init(remote_conn_str)
```

## Note: Not Required for On-Cluster Job Submission

The Ray Job CLI is specifically designed for submitting jobs to a Ray cluster from external systems. It is **not required** for submitting jobs on Ray clusters that are already running within Databricks. For jobs running directly on Databricks Ray clusters, Databricks recommends: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

- Deploying jobs using [Lakeflow Jobs](/concepts/lakeflow-jobs.md).
- Creating a Ray cluster per application.
- Using existing Databricks tooling such as Databricks Asset Bundles or Workflow Triggers to trigger the job.

## Limitations

- The Ray Job CLI does not support the Ray Dataset API (defined in the `ray.data` module) when connecting via the Ray client. To work around this limitation, wrap code that calls the Ray Dataset API inside a remote Ray task. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Ray Clusters on Databricks](/concepts/ray-cluster-on-databricks.md) — How to create and configure Ray clusters within Databricks.
- Ray Client API — Alternative programmatic connection method for Ray clusters.
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) — Recommended deployment approach for Ray applications on Databricks.
- Databricks Asset Bundles — Tool for managing Databricks resource deployments.
- Ray Dashboard — Web UI for monitoring Ray cluster activity and finding driver proxy URLs.

## Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
