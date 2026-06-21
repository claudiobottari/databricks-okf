---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5d728df5a874c320eb2530f90f47e2df451b9acaa5fbead9c39e4b6ffe12fbe0
  pageDirectory: concepts
  sources:
    - advanced-usage-of-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ssltls-certificates-for-databricks-connect
    - SCFDC
  citations:
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
title: SSL/TLS Certificates for Databricks Connect
description: Configuring custom SSL/TLS certificates for Databricks Connect by setting the `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` environment variable to the certificate path on the local development machine.
tags:
  - databricks-connect
  - security
  - certificates
timestamp: "2026-06-19T22:00:40.942Z"
---

# SSL/TLS Certificates for Databricks Connect

**SSL/TLS Certificates for Databricks Connect** refers to the configuration required when a Databricks cluster uses a custom SSL/TLS certificate to resolve the workspace’s fully qualified domain name (FQDN). In such cases, the local Databricks Connect client must be told to trust that custom certificate in order to establish a secure gRPC connection to the cluster.

## Overview

Databricks Connect communicates with Databricks clusters via gRPC over HTTP/2. gRPC uses SSL/TLS to encrypt the connection. If the cluster is configured with a custom (non-public) SSL/TLS certificate — for example, a certificate issued by an internal CA — the default system trust store on the developer’s machine may not contain the necessary root certificate. As a result, the gRPC handshake will fail unless the custom certificate is explicitly provided. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Configuration

To enable Databricks Connect to trust a custom SSL/TLS certificate, set the environment variable `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` on the local development machine. This variable must point to the full file path of the certificate bundle that contains the custom root certificate. The path should correspond to the certificate file that is already installed on the Databricks cluster. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Example (Python)

```python
import os
os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = "/etc/ssl/certs/ca-bundle.crt"
```

The example above sets the environment variable to a typical location on Linux systems. The exact path depends on where the custom certificate is stored on the cluster. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Other Languages

The same environment variable applies regardless of the language client (Python or Scala). Users of other supported languages should set `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` in their shell or application environment before initializing the Databricks session. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Notes

- This configuration is only necessary when a custom SSL/TLS certificate is used on the cluster. If the cluster uses a publicly trusted certificate (e.g., from a well-known CA), the standard trust store is sufficient.
- The environment variable must be set *before* creating the `DatabricksSession`; setting it after the connection is established has no effect.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library for connecting remote IDEs to Databricks clusters.
- [Spark Connect](/concepts/spark-connect.md) — The underlying protocol used by Databricks Connect for client-to-cluster communication.
- gRPC — The transport layer used by Spark Connect.
- Cluster Configuration — How to set up custom SSL/TLS certificates on a Databricks cluster.

## Sources

- advanced-usage-of-databricks-connect-databricks-on-aws.md

# Citations

1. [advanced-usage-of-databricks-connect-databricks-on-aws.md](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
