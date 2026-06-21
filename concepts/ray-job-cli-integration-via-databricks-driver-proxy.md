---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5f1a070da6060e33d7ece970ca13a0b892e3345332e31b529bbcbe626a5c0527
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-job-cli-integration-via-databricks-driver-proxy
    - RJCIVDDP
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
title: Ray Job CLI Integration via Databricks Driver Proxy
description: Connecting Ray Job CLI to a Databricks-hosted Ray cluster through the driver proxy endpoint
tags:
  - ray
  - cli
  - databricks
timestamp: "2026-06-19T09:31:50.039Z"
---

# Ray Job CLI Integration via Databricks Driver Proxy

**Ray Job CLI Integration via Databricks Driver Proxy** describes how to connect the Ray Job CLI (a command-line tool for submitting jobs to a Ray cluster) to a [Ray cluster](/concepts/global-mode-ray-cluster.md) running on Databricks by routing the job submission through the [Databricks driver proxy](/concepts/ray-job-cli-with-databricks-driver-proxy.md). This approach is intended for developers migrating from self-managed Ray infrastructure who have existing tooling built around the Ray CLI. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Overview

While Databricks does not support direct Ray Cluster CLI integration, you can connect the Ray Job CLI to a Ray cluster on Databricks through the Databricks driver proxy. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md] The connection is established by specifying the Databricks workspace URL and the proxy path found in the Ray Dashboard URL that appears after the Ray cluster is started. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Command Structure

A typical Ray Job CLI submission through the Databricks driver proxy uses the following command pattern: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```shell
ray job submit \
  --headers '{"cookie" : "DATAPLANE_DOMAIN_SESSIONID=<REDACTED>"}' \
  --address 'https://<DATABRICKS WORKSPACE URL>/driver-proxy/o/<etc>' \
  --working-dir='.' \
  -- python run_task.py
```

The key components that require configuration are:

- **Databricks workspace URL**: Begins with `https://`, and is the base URL for your Databricks workspace. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]
- **Driver proxy path**: The values after `/driver-proxy/o/` are found in the Ray Dashboard proxy URL that is displayed after the Ray cluster is started. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]
- **Session cookie header**: Required for authentication, using the `DATAPLANE_DOMAIN_SESSIONID` cookie value. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## When to Use This Integration

The Ray Job CLI is used for submitting jobs to a Ray cluster from external systems. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md] This integration is primarily relevant for teams with existing Ray CLI-based tooling who are migrating to Databricks and want to reuse their automation scripts. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Recommended Alternative

For most use cases, Databricks recommends deploying jobs using [Lakeflow Jobs](/concepts/lakeflow-jobs.md) rather than the Ray Job CLI. The recommended approach is to create one [Ray cluster](/concepts/global-mode-ray-cluster.md) per application and use existing Databricks tooling such as Databricks Asset Bundles or Workflow Triggers to trigger the job. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Prerequisites

Before connecting the Ray Job CLI to a Databricks-hosted Ray cluster, ensure the following:

- The Ray cluster is created using `ray.util.spark.setup_ray_cluster` API or `setup_global_ray_cluster` API. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]
- The Ray cluster is running on a Databricks all-purpose compute resource with Databricks Runtime 12.2 LTS ML or above and dedicated or no isolation shared access modes. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]
- The Ray Dashboard proxy URL is visible and can be used to extract the driver proxy path. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Related Concepts

- Ray Cluster CLI
- Ray Job CLI
- [Databricks Driver Proxy](/concepts/ray-job-cli-with-databricks-driver-proxy.md)
- [Ray Cluster on Databricks](/concepts/ray-cluster-on-databricks.md)
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md)
- Databricks Asset Bundles
- Workflow Triggers
- Ray Dashboard

## Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
