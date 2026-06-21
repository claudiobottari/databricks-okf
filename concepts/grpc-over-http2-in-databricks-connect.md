---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9a739e6f60c456140a2989cd4c45d6ec77cb7a20db67ad8d692425489732ba88
  pageDirectory: concepts
  sources:
    - advanced-usage-of-databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grpc-over-http2-in-databricks-connect
    - GOHIDC
  citations:
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
title: gRPC over HTTP/2 in Databricks Connect
description: Databricks Connect communicates with Databricks clusters via gRPC over HTTP/2, which is the underlying transport protocol for Spark Connect.
tags:
  - databricks-connect
  - networking
  - grpc
  - protocol
timestamp: "2026-06-18T14:20:53.285Z"
---

# gRPC over HTTP/2 in Databricks Connect

**gRPC over HTTP/2** is the underlying communication protocol used by [Databricks Connect](/concepts/databricks-connect.md) to transmit requests and data between a client development environment and a Databricks cluster. This protocol provides efficient, bidirectional streaming communication for Spark operations executed remotely.

## Overview

Databricks Connect communicates with Databricks clusters using gRPC (gRPC Remote Procedure Calls) transported over HTTP/2. This protocol choice enables low-latency, high-performance communication between the client application and the Spark Connect server running on the cluster. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

The gRPC over HTTP/2 transport provides several advantages for distributed data processing workloads, including multiplexed streams, header compression, and bidirectional streaming capabilities that are well-suited for Spark's computational patterns. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Client Configuration

### Connection String Format

When connecting to a Databricks cluster via gRPC, the connection string uses the Spark Connect URI scheme. The format follows the pattern `sc://<workspace-instance>:443/` with authentication and cluster identification parameters appended: ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

```
sc://<workspace-instance-name>:443/;token=<access-token-value>;x-databricks-cluster-id=<cluster-id>
```

This connection string can be passed to the `remote` function or set as the `SPARK_REMOTE` environment variable. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Custom HTTP Headers

Advanced users can add custom headers to gRPC over HTTP/2 requests. This capability is useful when a proxy service is installed between the client and the Databricks cluster and requires specific headers: ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.header('x-custom-header', 'value').getOrCreate()
```

## Certificate Requirements

When a Databricks workspace uses a custom SSL/TLS certificate for its fully qualified domain name (FQDN), the client must trust that certificate for the gRPC over HTTP/2 connection to succeed. The `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` environment variable must point to the certificate bundle on the local development machine: ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

```python
import os
os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = "/etc/ssl/certs/ca-bundle.crt"
```

## Proxy Services

For environments requiring additional control over client requests, advanced users can install a proxy service between the client and the Databricks cluster. When proxies require custom headers in HTTP requests, the `header()` method on the session builder can inject these headers into the gRPC over HTTP/2 stream. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Logging and Debugging

Debug logging for the gRPC connection can be enabled by setting the `SPARK_CONNECT_LOG_LEVEL` environment variable to `debug`. This setting prints all log messages at the `DEBUG` level and above to the standard error stream. By default, logging is turned off. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that uses gRPC over HTTP/2 for remote Spark execution
- [Spark Connect](/concepts/spark-connect.md) — The server-side component that accepts gRPC connections
- [DatabricksSession](/concepts/databrickssession.md) — The Python class for establishing gRPC connections to clusters
- gRPC — The remote procedure call framework underlying the protocol
- HTTP/2 — The transport layer protocol providing multiplexed streams
- SSL/TLS Certificates — Security certificates required for encrypted gRPC connections

## Sources

- advanced-usage-of-databricks-connect-databricks-on-aws.md

# Citations

1. [advanced-usage-of-databricks-connect-databricks-on-aws.md](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
