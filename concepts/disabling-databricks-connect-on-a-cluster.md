---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cece30b69c6689af4d6054ace762aca7e2714c079deadd060762867115eda532
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - disabling-databricks-connect-on-a-cluster
    - DDCOAC
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
title: Disabling Databricks Connect on a Cluster
description: Disabling the Databricks Connect and Spark Connect services on a cluster by setting spark.databricks.service.server.enabled to false.
tags:
  - configuration
  - clusters
  - security
timestamp: "2026-06-18T14:41:04.907Z"
---

# Disabling Databricks Connect on a Cluster

**Disabling Databricks Connect on a cluster** refers to the process of turning off the Databricks Connect service (and the underlying Spark Connect service) for a specific cluster. When disabled, the cluster no longer accepts connections from Databricks Connect clients such as Visual Studio Code, PyCharm, RStudio Desktop, IntelliJ IDEA, or custom applications. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## How to disable

To disable the Databricks Connect service on a cluster, set the following Spark configuration property:

```
spark.databricks.service.server.enabled false
```

This configuration can be applied when creating a new cluster or by editing the Spark configuration settings of an existing cluster. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Effect of disabling

Once `spark.databricks.service.server.enabled` is set to `false`, the cluster will not run the Databricks Connect service. Any attempt to connect to the cluster using Databricks Connect fails. The cluster continues to operate normally for all other workloads, including notebooks, jobs, and standard Databricks operations. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Related concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that connects IDEs and custom applications to Databricks clusters
- Spark configuration — Cluster-level settings that control Spark and Databricks behavior
- [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) — Full details on configuring connections between Databricks Connect and clusters or serverless compute
- Cluster — The compute resource that Databricks Connect connects to

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
