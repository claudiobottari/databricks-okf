---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 94dc0a5d0d72eb68571735f914f161e554c26fcb105c2e14b2b284cc9aa0392b
  pageDirectory: concepts
  sources:
    - advanced-usage-of-databricks-connect-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-grpc-communication
    - DCGC
  citations:
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
title: Databricks Connect gRPC Communication
description: Databricks Connect communicates with Databricks Clusters via gRPC over HTTP/2, which is the underlying protocol for Spark Connect connections.
tags:
  - databricks-connect
  - networking
  - protocol
timestamp: "2026-06-19T22:00:50.730Z"
---

# Databricks Connect gRPC Communication

**Databricks Connect gRPC Communication** refers to the underlying transport protocol that Databricks Connect uses to send requests and receive responses from Databricks clusters. The protocol is gRPC over HTTP/2, and advanced users can configure connection strings, custom headers, TLS certificates, and logging to control this communication layer.

## Overview

Databricks Connect communicates with Databricks clusters via gRPC over HTTP/2. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md] All Spark operations (e.g., DataFrame transformations, SQL queries) are sent as gRPC requests to the cluster using the Spark Connect protocol.

## Connection String

The connection to a cluster is defined using a Spark Connect connection string with the scheme `sc://`. This string can be passed directly to the `DatabricksSession.builder.remote()` function or set via the `SPARK_REMOTE` environment variable. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md] For example:

```text
sc://<workspace-instance-name>:443/;token=<access-token-value>;x-databricks-cluster-id=<cluster-id>
```

When the `SPARK_REMOTE` environment variable is set, `DatabricksSession.builder.getOrCreate()` reads it automatically. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Proxy and Custom Headers

Because gRPC runs over HTTP/2, advanced users can install a proxy service between the client and the Databricks cluster. Some proxies require custom HTTP headers. To add such headers to every gRPC request, use the `header()` method on the builder: ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
spark = [[databrickssession|DatabricksSession]].builder.header('x-custom-header', 'value').getOrCreate()
```

## Certificates

If the cluster uses a custom SSL/TLS certificate to resolve the Databricks workspace fully qualified domain name (FQDN), the client must trust that certificate. Set the environment variable `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` on the local development machine to the full path of the certificate bundle installed on the cluster. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

Example:

```python
import os
os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = "/etc/ssl/certs/ca-bundle.crt"
```

## Logging and Debugging

By default, Databricks Connect gRPC logs are turned off. To enable debug-level logging for the gRPC layer, set the environment variable `SPARK_CONNECT_LOG_LEVEL=debug`. All log messages at the `DEBUG` level and higher are printed to the standard error stream. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The overall client library that uses gRPC communication.
- [Spark Connect](/concepts/spark-connect.md) – The protocol definition that provides the gRPC service.
- [Cluster Configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) – How to specify cluster endpoints.
- gRPC – The underlying RPC framework (not Databricks‑specific).
- HTTP/2 – The transport protocol used by gRPC.

## Sources

- advanced-usage-of-databricks-connect-databricks-on-aws.md

# Citations

1. [advanced-usage-of-databricks-connect-databricks-on-aws.md](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
