---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0cad18e310f4140d79899192f50126e7decbb1fbfc89e430112a0db86ef19f54
  pageDirectory: concepts
  sources:
    - advanced-usage-of-databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-ssltls-certificate-configuration
    - DCSCC
  citations:
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
title: Databricks Connect SSL/TLS Certificate Configuration
description: Configuring custom SSL/TLS certificates for Databricks Connect by setting the GRPC_DEFAULT_SSL_ROOTS_FILE_PATH environment variable
tags:
  - databricks
  - security
  - configuration
timestamp: "2026-06-19T08:54:33.589Z"
---

# Databricks Connect SSL/TLS Certificate Configuration

**Databricks Connect SSL/TLS Certificate Configuration** refers to the setup required on a local development machine when a Databricks cluster uses a custom SSL/TLS certificate to resolve the workspace fully qualified domain name (FQDN). Without this configuration, Databricks Connect cannot establish a secure gRPC connection to the cluster.

## When to Configure

If your cluster relies on a custom SSL/TLS certificate (not one signed by a public certificate authority that the operating system already trusts) to present the Databricks workspace FQDN, you must set the environment variable `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` on your local machine. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

The custom certificate must be installed on the cluster. The environment variable points to the full path of that certificate file on the cluster. Databricks Connect uses this path to locate the certificate bundle when verifying the server’s identity during the TLS handshake.

## Configuration Steps

### Set the Environment Variable

Set `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` to the full path of the custom certificate bundle file. The exact path depends on your cluster's operating system and certificate placement.

**Python example:**

```python
import os
os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = "/etc/ssl/certs/ca-bundle.crt"
```

You can also set the variable outside of code, using your operating system’s standard methods (e.g., shell export, `.bashrc`, or system environment settings). ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

> **Important:** The value must match the certificate location on the **cluster**, not on the local machine. If you are using a cluster with a custom certificate, obtain the correct path from the cluster administrator.

### Verify the Connection

After setting the environment variable, restart your development session and test a simple Spark operation (e.g., `spark.sql("SELECT 1").show()`) to confirm the TLS handshake succeeds.

## How Databricks Connect Uses This Variable

Databricks Connect communicates with a cluster via gRPC over HTTP/2. The gRPC library (underlying Spark Connect) reads `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` to obtain the set of root certificates used for TLS verification. If this variable is not set or points to an incorrect file, the connection will fail with an SSL/TLS error. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library for connecting local code to Databricks clusters.
- [Spark Connect](/concepts/spark-connect.md) – The underlying protocol (gRPC-based) used by Databricks Connect.
- [Advanced Databricks Connect Configuration](/concepts/databricks-connect-configuration.md) – Other advanced topics such as custom headers and proxy setup.
- [SSL/TLS Certificate Trust Store](/concepts/ssltls-certificates-for-databricks-connect.md) – General concept of certificate trust paths on Linux systems.
- [Environment Variables for Databricks Connect](/concepts/environment-variable-configuration-for-databricks-connect.md) – Other environment variables like `SPARK_REMOTE` and `SPARK_CONNECT_LOG_LEVEL`.

## Sources

- advanced-usage-of-databricks-connect-databricks-on-aws.md

# Citations

1. [advanced-usage-of-databricks-connect-databricks-on-aws.md](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
