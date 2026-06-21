---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9d533316426b8726f4cb777cd974534a2b4563cfa8d755e82fb3e6fc3d474874
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-service-disabling
    - DCSD
    - databricks-connect-cluster-disabling
    - DCCD
    - databricks-connect-service-disablement
    - DBFS disablement
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
title: Databricks Connect Service Disabling
description: How to disable the Databricks Connect (Spark Connect) service on a cluster using the spark.databricks.service.server.enabled Spark configuration property.
tags:
  - databricks-connect
  - configuration
  - spark-config
timestamp: "2026-06-19T17:48:28.148Z"
---

# Databricks Connect Service Disabling

**Databricks Connect Service Disabling** refers to the process of turning off the [Databricks Connect](/concepts/databricks-connect.md) and underlying [Spark Connect](/concepts/spark-connect.md) services on a specific cluster. When disabled, the cluster no longer accepts connections from external IDEs or applications that use Databricks Connect.

## Overview

By default, Databricks Connect is enabled on compatible clusters. Administrators or cluster creators can disable this service per cluster by applying a Spark configuration property. Disabling the service prevents any Databricks Connect client from establishing a session with that cluster, which can be useful for security or resource management purposes. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Procedure

To disable the Databricks Connect service on a cluster, set the following Spark configuration property to `false`:

```
spark.databricks.service.server.enabled false
```

This setting can be configured in the cluster’s Spark configuration section (via the cluster UI or API). Once applied and the cluster is restarted, the Databricks Connect service is deactivated for that cluster. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Effects

When Databricks Connect is disabled:

- The cluster will not respond to requests from Databricks Connect clients.
- Any attempt to connect to the cluster using Databricks Connect will fail.
- The setting applies only to the cluster on which it is set; other clusters remain unaffected.
- The service can be re‑enabled by removing the configuration property or setting it to `true`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – the framework that enables remote IDE and application connections.
- [Spark Connect](/concepts/spark-connect.md) – the underlying protocol used by Databricks Connect.
- Spark configuration – mechanisms for controlling cluster behavior.
- cluster – the compute resource that hosts the Databricks Connect service.

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
