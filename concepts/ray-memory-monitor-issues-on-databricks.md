---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 79ca3eda49922cb2ee228469a94c16502e36627d76907c27492aae4ad87feeff
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-memory-monitor-issues-on-databricks
    - RMMIOD
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
title: Ray Memory Monitor Issues on Databricks
description: Known issues in Ray 2.9.3 where the memory monitor can inadvertently kill Ray tasks, with workaround of disabling the monitor via RAY_memory_monitor_refresh_ms environment variable
tags:
  - ray
  - memory
  - troubleshooting
  - databricks
timestamp: "2026-06-19T14:32:22.922Z"
---

# Ray Memory Monitor Issues on Databricks

**Ray Memory Monitor Issues on Databricks** refers to a known problem in Ray 2.9.3 where the built‑in memory monitor can incorrectly kill Ray tasks that are not actually out of memory, even when sufficient memory is available. The issue manifests as unexpected task termination without a genuine out‑of‑memory (OOM) condition, leading to unreliable training or inference workloads. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Cause

In Ray 2.9.3, the memory monitor component has several known bugs that cause it to erroneously detect memory pressure and stop tasks pre‑emptively. When this occurs, the affected Ray tasks are killed even though the system has not exceeded its memory limits. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Workaround

Until a fixed version of Ray is deployed, the recommended workaround is to disable the Ray memory monitor entirely. This is done by setting the environment variable `RAY_memory_monitor_refresh_ms` to `0` within the Databricks cluster configuration **before starting the Apache Spark cluster** (i.e., before calling `setup_ray_cluster`). Once set to zero, the memory monitor stops refreshing and will no longer kill tasks based on its faulty checks. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### How to set the environment variable

1. In the Databricks cluster configuration UI, add the environment variable `RAY_memory_monitor_refresh_ms = 0` under the **Advanced options** → **Spark** → **Environment variables** section (or equivalent for your cluster version).
2. Restart the cluster so that the variable is available when the Ray cluster is started.

Alternatively, if you are starting the Ray cluster from a notebook, you can set the environment variable in the notebook before running `setup_ray_cluster`:

```python
import os
os.environ["RAY_memory_monitor_refresh_ms"] = "0"

from ray.util.spark import setup_ray_cluster
setup_ray_cluster(...)
```

Note that disabling the memory monitor means you lose the ability to automatically catch genuine OOM conditions. Monitor memory usage manually via Ray Dashboard or external tools when using this workaround.

## Scope

This issue is specific to **Ray 2.9.3**. Users on older or newer versions of Ray may not be affected. Databricks recommends using the latest supported Ray version and checking the release notes for bug fixes related to the memory monitor.

## Related Concepts

- Ray OOM Errors – True out‑of‑memory situations that the monitor is intended to detect.
- Databricks Cluster Configuration – How to set environment variables in the cluster setup.
- Ray 2.9.3 – The specific Ray version affected.
- [Ray Cluster Setup on Databricks](/concepts/ray-cluster-on-databricks.md) – Guidelines for creating Ray clusters.

## Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
