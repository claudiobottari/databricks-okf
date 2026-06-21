---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f7f0f7e8621e825e85f105849e5767c0c8e3be9201b8bb188495c1d89f40c482
  pageDirectory: concepts
  sources:
    - advanced-usage-of-databricks-connect-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-connect-grpc-communication-protocol
    - DCGCP
  citations:
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
title: Databricks Connect gRPC Communication Protocol
description: Databricks Connect communicates with Databricks Clusters via gRPC over HTTP/2, which underlies the need for proxy configuration and certificate management.
tags:
  - databricks
  - networking
  - grpc
timestamp: "2026-06-19T17:28:37.080Z"
---

# Databricks Connect gRPC Communication Protocol

The **Databricks Connect gRPC Communication Protocol** is the underlying transport mechanism that enables communication between Databricks Connect clients and Databricks clusters. It uses gRPC over HTTP/2 to facilitate remote execution of Spark operations from local development environments.

## Overview

Databricks Connect communicates with Databricks clusters via gRPC (gRPC Remote Procedure Calls) over HTTP/2. This protocol provides efficient, high-performance communication between the client and the cluster, enabling developers to run Spark code locally while executing operations remotely on a Databricks cluster. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Connection String Format

The gRPC connection is established using a Spark Connect connection string. The connection string follows this format:

```
sc://<workspace-instance-name>:443/;token=<access-token-value>;x-databricks-cluster-id=<cluster-id>
```

This string can be passed directly to the `remote` function or set as the `SPARK_REMOTE` environment variable. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Proxy Support

Advanced users may install a proxy service between the client and the Databricks cluster to gain better control over incoming requests. Some proxies require custom headers in HTTP requests. Databricks Connect supports adding custom headers using the `header()` method:

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
spark = [[databrickssession|DatabricksSession]].builder.header('x-custom-header', 'value').getOrCreate()
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## SSL/TLS Certificates

When a cluster relies on a custom SSL/TLS certificate to resolve a Databricks workspace fully qualified domain name (FQDN), the local development machine must be configured to trust that certificate. This is done by setting the `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` environment variable to the full path of the installed certificate on the cluster:

```python
import os
os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = "/etc/ssl/certs/ca-bundle.crt"
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Debug Logging

Databricks Connect for Python produces logs using standard Python logging, emitted to the standard error stream (stderr). Logging is turned off by default. To enable debug-level logging, set the `SPARK_CONNECT_LOG_LEVEL=debug` environment variable, which prints all log messages at the `DEBUG` level and higher. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that uses this protocol for remote Spark execution.
- [Spark Connect](/concepts/spark-connect.md) — The underlying open source protocol that Databricks Connect builds upon.
- [Databricks Session](/concepts/databrickssession.md) — The session object that manages the gRPC connection to the cluster.
- [Cluster Configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) — How to configure cluster connections.
- gRPC — The high-performance RPC framework used for communication.

## Sources

- advanced-usage-of-databricks-connect-databricks-on-aws.md

# Citations

1. [advanced-usage-of-databricks-connect-databricks-on-aws.md](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
