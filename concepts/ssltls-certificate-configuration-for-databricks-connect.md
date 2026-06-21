---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2cd75e6cd6d969ab9cba6ae54ea83ad7dd5d673ccc35bb4e0f34a9e59f45d727
  pageDirectory: concepts
  sources:
    - advanced-usage-of-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ssltls-certificate-configuration-for-databricks-connect
    - SCCFDC
    - SSL/TLS Certificate Trust Store
  citations:
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
title: SSL/TLS Certificate Configuration for Databricks Connect
description: Configuration of the GRPC_DEFAULT_SSL_ROOTS_FILE_PATH environment variable to support custom SSL/TLS certificates for Databricks workspace FQDN resolution.
tags:
  - databricks
  - security
  - certificates
timestamp: "2026-06-19T17:28:44.533Z"
---

# SSL/TLS Certificate Configuration for Databricks Connect

**SSL/TLS certificate configuration** is required when your Databricks cluster uses a custom SSL/TLS certificate to resolve the workspace's fully qualified domain name (FQDN). Without this configuration, the gRPC-based connection between your local development machine and the remote cluster may fail because the system’s default certificate store does not trust the custom certificate. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## When Certificate Configuration Is Needed

This configuration is necessary **only** when the cluster relies on a custom SSL/TLS certificate—typically one issued by a private Certificate Authority (CA) or a self-signed certificate—to resolve the workspace FQDN. If your cluster uses a publicly trusted certificate (for example, from Let’s Encrypt or DigiCert), no special steps are required. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Configuration Method

To configure [Databricks Connect](/concepts/databricks-connect.md) to trust a custom certificate, set the environment variable `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` on your local machine. The value must be the **full absolute path** to the certificate bundle file that the cluster trusts. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Python Example

```python
import os
os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = "/etc/ssl/certs/ca-bundle.crt"
```

The path `/etc/ssl/certs/ca-bundle.crt` is the typical location of the system CA bundle on many Linux distributions. Adjust the path to match your operating system’s certificate store. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Environment Variable Scope

The environment variable must be set **before** the gRPC channel is created (that is, before initializing the `DatabricksSession` object). The gRPC library reads the certificate bundle only once during channel setup; setting the variable afterward has no effect.

*Inference: The source does not explicitly state the timing requirement, but gRPC behavior makes this necessary.*

## How It Works

[Databricks Connect](/concepts/databricks-connect.md) communicates with a Databricks cluster using gRPC over HTTP/2, which is an encrypted transport protocol. The gRPC library loads the certificate bundle pointed to by `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` to validate the server’s certificate during the TLS handshake. If the certificate is not trusted, the connection fails with an SSL error. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that establishes a Spark Connect session.
- [Spark Connect](/concepts/spark-connect.md) — The gRPC-based protocol underlying Databricks Connect.
- gRPC — The remote procedure call framework that handles TLS security.
- SSL/TLS — The cryptographic protocol used for encrypted communication.
- Proxy configuration for Databricks Connect — Additional setup for proxies that require custom HTTP headers.

## Sources

- advanced-usage-of-databricks-connect-databricks-on-aws.md

# Citations

1. [advanced-usage-of-databricks-connect-databricks-on-aws.md](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
