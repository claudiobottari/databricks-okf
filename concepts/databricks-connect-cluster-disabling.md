---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1f4c416a1cbd52434a8e1eb778ed0433362271c4366d02897d6d83e175829735
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-cluster-disabling
    - DCCD
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
title: Databricks Connect Cluster Disabling
description: Databricks Connect and Spark Connect services can be disabled on a cluster by setting spark.databricks.service.server.enabled false in Spark configuration.
tags:
  - databricks
  - security
  - configuration
timestamp: "2026-06-19T14:20:32.629Z"
---

# Databricks Connect Cluster Disabling

**Databricks Connect Cluster Disabling** refers to the process of turning off the Databricks Connect (and underlying Spark Connect) service on a specific Databricks cluster. When disabled, the cluster no longer accepts remote connections from IDEs such as Visual Studio Code, PyCharm, or custom applications that use the Databricks Connect client library. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## How to Disable

You can disable the Databricks Connect service on any given cluster by setting the following Spark configuration property on the cluster:

```
spark.databricks.service.server.enabled false
```

^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

This Spark configuration is applied at the cluster level. Once set, the cluster will reject incoming connections from Databricks Connect clients, making the cluster inaccessible for remote development workflows that depend on Databricks Connect. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Effect on Spark Connect

Disabling Databricks Connect also disables the underlying [Spark Connect](/concepts/spark-connect.md) service. Both services rely on the same server-side component, so the single configuration flag controls both. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Use Cases

Disabling Databricks Connect can be useful in environments where:
- Cluster resources should be reserved exclusively for notebook or job workloads.
- Security policies require that no remote client connections are allowed.
- The cluster is in production and should not be used for ad-hoc IDE connections.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library for connecting IDEs to Databricks clusters.
- [Spark Connect](/concepts/spark-connect.md) – The underlying protocol that Databricks Connect uses.
- Spark Configuration – The mechanism for setting cluster-level properties.
- Cluster Configuration – How to configure compute resources on Databricks.

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
