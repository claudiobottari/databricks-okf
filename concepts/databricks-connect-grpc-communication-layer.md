---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 607156f900c6afa863bd59f93647313981999865aa60a4a2de13e565c1f52c95
  pageDirectory: concepts
  sources:
    - advanced-usage-of-databricks-connect-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-connect-grpc-communication-layer
    - DCGCL
  citations:
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
title: Databricks Connect gRPC Communication Layer
description: Databricks Connect communicates with Databricks clusters via gRPC over HTTP/2, enabling advanced proxy and header customization
tags:
  - databricks
  - networking
  - grpc
timestamp: "2026-06-18T10:42:32.224Z"
---

# Databricks Connect gRPC Communication Layer

**Databricks Connect** communicates with Databricks clusters via **gRPC over HTTP/2**. This communication layer is a fundamental architectural component that enables client-side development and debugging while leveraging the power of remote Spark clusters. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Overview

The gRPC communication layer in Databricks Connect is built on the [Spark Connect](/concepts/spark-connect.md) protocol, which replaces the traditional Spark driver-based connectivity model. Instead of submitting code to a remote cluster for execution, Databricks Connect establishes a gRPC channel that sends commands as protobuf-encoded operations to the Spark Connect server running on the Databricks cluster. This enables interactive development from local environments while executing computations on the remote cluster. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Connection String Configuration

The most advanced method of configuring the gRPC connection is through the **Spark Connect connection string**, which encapsulates all connection parameters in a single URI. The connection string follows the format:

```
sc://<workspace-instance-name>:443/;token=<access-token-value>;x-databricks-cluster-id=<cluster-id>
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

This string can be passed directly to the `remote()` function or set as the `SPARK_REMOTE` environment variable. When using the `remote()` function:

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

workspace_instance_name = retrieve_workspace_instance_name()
token = retrieve_token()
cluster_id = retrieve_cluster_id()

spark = [[databrickssession|DatabricksSession]].builder.remote(
    f"sc://{workspace_instance_name}:443/;token={token};x-databricks-cluster-id={cluster_id}"
).getOrCreate()
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

Alternatively, set the `SPARK_REMOTE` environment variable and then use the standard initialization:

```python
spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Proxy Support and Custom Headers

The gRPC communication layer supports HTTP/2 proxies, which may be necessary in enterprise environments where network traffic is routed through intermediary services. Advanced users can install a proxy service between the client and the Databricks cluster to gain better control over requests. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

Some proxies require custom headers in HTTP requests. The `header()` method allows adding such headers:

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.header('x-custom-header', 'value').getOrCreate()
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## SSL/TLS Certificates

When a cluster uses a **custom SSL/TLS certificate** to resolve the Databricks workspace fully qualified domain name (FQDN), the gRPC layer requires the certificate to be available on the local development machine. Set the `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` environment variable to the full path of the installed certificate:

```python
import os
os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = "/etc/ssl/certs/ca-bundle.crt"
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

This ensures that gRPC can validate the TLS connection to the Databricks cluster. The specific path depends on the operating system and certificate installation method. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Local Spark Connect Server

As an alternative to connecting to a Databricks cluster, Databricks Connect can communicate with an **open source Spark Connect server** running locally. In this configuration, the `SPARK_REMOTE` environment variable points to the local server: ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

```bash
export SPARK_REMOTE="sc://localhost"
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

However, some features available in Databricks Runtime and Databricks Connect are exclusive to Databricks or not yet released in open source Apache Spark. Code relying on these proprietary features may fail when using a local Spark Connect server. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Logging and Debugging

The gRPC communication layer produces logs through standard Python Logging mechanisms, emitted to the standard error stream (_stderr_). Logging is disabled by default. To enable debug-level logging for the gRPC channel, set the `SPARK_CONNECT_LOG_LEVEL=debug` environment variable, which prints all log messages at the `DEBUG` level and higher. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Authentication via OAuth U2M

When using [OAuth User-to-Machine (U2M)](/concepts/user-to-machine-u2m-authentication.md) authentication, the gRPC layer performs an initial OAuth token exchange. The `Client ID` is sourced from:

1. The `DATABRICKS_CLIENT_ID` environment variable
2. The connection profile's `client_id` field

The authentication flow involves a browser-based login that completes the OAuth handshake before gRPC communication can proceed.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that uses this gRPC layer
- [Spark Connect](/concepts/spark-connect.md) — The protocol underlying the gRPC communication
- [OAuth User-to-Machine (U2M)](/concepts/user-to-machine-u2m-authentication.md) — Authentication mechanism for gRPC connections
- [Databricks Session](/concepts/databrickssession.md) — The session object created through the gRPC channel
- gRPC — The remote procedure call framework used for communication

## Sources

- advanced-usage-of-databricks-connect-databricks-on-aws.md

# Citations

1. [advanced-usage-of-databricks-connect-databricks-on-aws.md](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
