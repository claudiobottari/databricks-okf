---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9e0a766a87ddf2103c3b937ff114dbe63d2e9a7afe1f5dd8678fb35c3284894d
  pageDirectory: concepts
  sources:
    - advanced-usage-of-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-connection-string-configuration
    - DCCSC
  citations:
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
title: Databricks Connect Connection String Configuration
description: How to configure Databricks Connect using the Spark Connect connection string via the remote() function or the SPARK_REMOTE environment variable
tags:
  - databricks
  - connectivity
  - configuration
timestamp: "2026-06-18T10:41:29.763Z"
---

# Databricks Connect Connection String Configuration

**Databricks Connect Connection String Configuration** allows you to connect your local development environment to a Databricks cluster using a Spark Connect connection string. This approach is an alternative to the standard cluster configuration options and provides finer control over the connection parameters.

## Overview

The Spark Connect connection string is a URI-based parameter that specifies how to reach the cluster’s Spark Connect server. You can supply this string programmatically via the `remote` function in `DatabricksSession.builder`, or set it as the `SPARK_REMOTE` environment variable for use with the builder’s default `getOrCreate()` call. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Connection String Format

The connection string follows the Spark Connect URI scheme:

```
sc://<workspace-instance-name>:443/;token=<access-token-value>;x-databricks-cluster-id=<cluster-id>
```

| Component | Description |
|-----------|-------------|
| `sc://` | Scheme for Spark Connect |
| `<workspace-instance-name>` | The Databricks workspace instance name (e.g., `dbc-xxxxxxxx.cloud.databricks.com`) |
| `443` | Port for HTTPS |
| `token` | Personal access token for authentication |
| `x-databricks-cluster-id` | The ID of the target cluster |

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Configuration Methods

### Using the `remote` function

In Python, you can construct the connection string at runtime and pass it directly to the `remote` method:

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

workspace_instance_name = retrieve_workspace_instance_name()
token                   = retrieve_token()
cluster_id              = retrieve_cluster_id()

spark = [[databrickssession|DatabricksSession]].builder.remote(
   f"sc://{workspace_instance_name}:443/;token={token};x-databricks-cluster-id={cluster_id}"
).getOrCreate()
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Using the `SPARK_REMOTE` environment variable

Alternatively, export the connection string as the `SPARK_REMOTE` environment variable before starting the Python process:

```bash
export SPARK_REMOTE="sc://<workspace-instance-name>:443/;token=<access-token-value>;x-databricks-cluster-id=<cluster-id>"
```

Then initialize the session without passing any arguments:

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Using a local Spark Connect server

Advanced users can run Databricks Connect against an open source Spark Connect server. Some Databricks-specific features may not be available in open source Spark. After starting the local server (see [How to use Spark Connect](https://spark.apache.org/docs/latest/spark-connect-overview.html)), set the environment variable to point to the local URI:

```bash
export SPARK_REMOTE="sc://localhost"
```

Then initialize the session as above. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Custom Headers for Proxies

If a proxy service between the client and the Databricks cluster requires custom HTTP headers, you can add them using the `header()` method:

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.header('x-custom-header', 'value').getOrCreate()
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Certificates for Custom SSL/TLS

When the cluster uses a custom SSL/TLS certificate to resolve the workspace fully qualified domain name, set the `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` environment variable on the local machine to the full path of the certificate bundle installed on the cluster:

```python
import os
os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = "/etc/ssl/certs/ca-bundle.crt"
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Logging and Debug

Databricks Connect for Python uses the standard Python logging library. Logs are emitted to stderr and are off by default. To enable verbose output, set the environment variable `SPARK_CONNECT_LOG_LEVEL=debug` to print all log messages at the DEBUG level and above. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The overall client library for connecting local code to Databricks clusters.
- [DatabricksSession](/concepts/databrickssession.md) – The entry point for creating a Spark session via Databricks Connect.
- [Spark Connect](/concepts/spark-connect.md) – The underlying protocol that Databricks Connect uses for remote execution.
- [Cluster Configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) – Alternative ways to configure a connection (e.g., via `databricks-connect` CLI or profile).

## Sources

- advanced-usage-of-databricks-connect-databricks-on-aws.md

# Citations

1. [advanced-usage-of-databricks-connect-databricks-on-aws.md](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
