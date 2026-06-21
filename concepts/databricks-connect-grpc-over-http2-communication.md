---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9db605be6d7cbee2433a25cf21dc7a475a1787a6058ed14b1187cc231ec84241
  pageDirectory: concepts
  sources:
    - advanced-usage-of-databricks-connect-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-grpc-over-http2-communication
    - DCGOHC
  citations:
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
title: Databricks Connect gRPC over HTTP/2 Communication
description: The underlying protocol used by Databricks Connect to communicate with Databricks clusters via gRPC over HTTP/2
tags:
  - databricks
  - networking
  - grpc
timestamp: "2026-06-19T13:55:20.541Z"
---

# Databricks Connect gRPC over HTTP/2 Communication

**Databricks Connect gRPC over HTTP/2 Communication** refers to the underlying protocol used by [Databricks Connect](/concepts/databricks-connect.md) to exchange data and commands between a local client and a remote Databricks cluster. Understanding this communication layer helps advanced users configure proxy services, custom headers, certificates, and logging for network‑sensitive or security‑hardened environments.

## Overview

Databricks Connect communicates with Databricks clusters via **gRPC over HTTP/2**. The client library (e.g., `DatabricksSession`) establishes a connection using the Spark Connect protocol, which leverages gRPC as its transport and HTTP/2 for efficient multiplexed streaming. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Connection String and Transport

The connection string for a Databricks Connect session uses the `sc://` scheme, which signals a Spark Connect client that communicates over gRPC. For example:

```
sc://<workspace-instance-name>:443/;token=<access-token-value>;x-databricks-cluster-id=<cluster-id>
```

This string can be passed directly to the `remote()` method of `DatabricksSession.builder` or set via the `SPARK_REMOTE` environment variable. The `:443` indicates the default HTTPS port, and the token and cluster ID are passed as query parameters. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Custom HTTP Headers

Because Databricks Connect uses HTTP/2 as the underlying transport, advanced users can inject **custom headers** into every gRPC request. This is useful when an intermediate proxy service requires specific headers (e.g., authentication or routing metadata). Custom headers are added using the `.header()` method on the session builder:

```python
spark = [[databrickssession|DatabricksSession]].builder.header('x-custom-header', 'value').getOrCreate()
```

Proxy services may require custom headers in HTTP requests to function correctly. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## TLS/SSL Certificates

If the cluster uses a **custom SSL/TLS certificate** to resolve the Databricks workspace fully qualified domain name (FQDN), the local development machine must trust that certificate. Set the environment variable `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` to the full path of the certificate bundle installed on the cluster:

```python
import os
os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = "/etc/ssl/certs/ca-bundle.crt"
```

This instructs the gRPC library to use the specified root certificates instead of the system defaults. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Logging and Debugging

gRPC traffic and internal Databricks Connect logs can be enabled by setting the environment variable `SPARK_CONNECT_LOG_LEVEL=debug`. Logs are emitted to the standard error stream and are turned off by default; setting this variable prints all log messages at `DEBUG` level and higher. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — the overall client‑server integration framework.
- [Spark Connect](/concepts/spark-connect.md) — the protocol that defines the gRPC service.
- gRPC — the high‑performance RPC framework used as transport.
- HTTP/2 — the network protocol enabling multiplexed streams.
- [DatabricksSession](/concepts/databrickssession.md) — the entry point for creating a Databricks Connect session.
- Proxy Configuration for Databricks Connect — advanced networking setups.

## Sources

- advanced-usage-of-databricks-connect-databricks-on-aws.md

# Citations

1. [advanced-usage-of-databricks-connect-databricks-on-aws.md](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
