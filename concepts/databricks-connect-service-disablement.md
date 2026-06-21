---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c11f6fbfb73505e9c2fff3a58a9d01ddf98dc0b1fe22a56fe1ce59573d1a9309
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-service-disablement
    - DCSD
    - DBFS disablement
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
title: Databricks Connect service disablement
description: Method to disable Databricks Connect (Spark Connect) on a cluster by setting spark.databricks.service.server.enabled false in Spark configuration.
tags:
  - databricks
  - configuration
  - security
timestamp: "2026-06-19T09:20:21.636Z"
---

# Databricks Connect Service Disablement

**Databricks Connect service disablement** refers to the process of turning off the Spark Connect service on a Databricks cluster to prevent connections from Databricks Connect clients such as IDEs, notebook servers, and custom applications.

## Overview

Databricks Connect and the underlying Spark Connect service can be disabled on any given cluster. When disabled, the cluster will no longer accept incoming connections from [Databricks Connect](/concepts/databricks-connect.md) clients. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Configuration

To disable the Databricks Connect service on a cluster, set the following Spark configuration property: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```
spark.databricks.service.server.enabled false
```

This Spark configuration must be applied to the cluster before it starts. Once set, the service will not be available for the lifetime of the cluster.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client-side tool for connecting IDEs and applications to Databricks compute
- [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) — Full guide on configuring connections between clients and compute
- Spark configuration — General mechanism for setting cluster-level properties
- [Serverless compute for Databricks Connect](/concepts/serverless-compute-with-databricks-connect.md) — Alternative compute target for Databricks Connect connections

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
