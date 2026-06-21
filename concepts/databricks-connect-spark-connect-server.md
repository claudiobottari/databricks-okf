---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4d78242b1e38e9457c0971a7b79be1053a2d5a557ba66ce50b7a760ee82493f6
  pageDirectory: concepts
  sources:
    - advanced-usage-of-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-spark-connect-server
    - DCSCS
    - databricks-connect-with-open-source-spark-connect-server
    - DCWOSSCS
  citations:
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
title: Databricks Connect Spark Connect Server
description: Running Databricks Connect against an open source Spark Connect server instead of a Databricks cluster, with caveats about exclusive features
tags:
  - databricks
  - spark
  - open-source
timestamp: "2026-06-19T08:54:42.034Z"
---

# Databricks Connect Spark Connect Server

**Databricks Connect Spark Connect Server** refers to the ability to use [Databricks Connect](/concepts/databricks-connect.md) against either a Databricks-managed cluster or an open source [Spark Connect](/concepts/spark-connect.md) server. Databricks Connect communicates with clusters via gRPC over HTTP/2, and the Spark Connect server is the endpoint that handles client requests. This page covers advanced configuration options such as custom connection strings, running against a local Spark Connect server, adding custom headers, handling certificates, and enabling debug logging. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

> **Note:** This article covers Databricks Connect for Databricks Runtime 14.0 and above. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Configure the Spark Connect Connection String

Besides the standard cluster configuration methods, you can connect using a Spark Connect connection string directly. Pass the string to the `remote()` function or set the `SPARK_REMOTE` environment variable. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Using the `remote()` function (Python)

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

workspace_instance_name = retrieve_workspace_instance_name()
token                   = retrieve_token()
cluster_id              = retrieve_cluster_id()

spark = [[databrickssession|DatabricksSession]].builder.remote(
    f"sc://{workspace_instance_name}:443/;token={token};x-databricks-cluster-id={cluster_id}"
).getOrCreate()
```

### Using the `SPARK_REMOTE` environment variable

Set the environment variable to a connection string of the form:

```
sc://<workspace-instance-name>:443/;token=<access-token-value>;x-databricks-cluster-id=<cluster-id>
```

Then initialize the session:

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Use Spark Connect Server with Databricks Connect

You can optionally run Databricks Connect against an open source Spark Connect server instead of a Databricks cluster. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

> **Important:** Some features available in Databricks Runtime and Databricks Connect are exclusive to Databricks or not yet released in open source Apache Spark. If your code relies on these features, the following steps may fail with errors. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Steps

1. Start a local Spark Connect server. See the Apache Spark documentation on [how to use Spark Connect](https://spark.apache.org/docs/latest/spark-connect-overview.html). ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]
2. Configure Databricks Connect by setting the `SPARK_REMOTE` environment variable to point to your local server. For example:  
   `export SPARK_REMOTE="sc://localhost"` ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]
3. Initialize the Databricks session as usual:  
   ```python
   from databricks.connect import [[databrickssession|DatabricksSession]]
   spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
   ```  
   ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Custom Headers for Proxy Support

If you use a proxy between the client and the Databricks cluster, you may need to add custom headers to HTTP requests. Use the `header()` method on the builder:

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
spark = [[databrickssession|DatabricksSession]].builder.header('x-custom-header', 'value').getOrCreate()
```

This is useful for proxies that require custom authentication or routing headers. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Certificates

If your cluster relies on a custom SSL/TLS certificate to resolve a Databricks workspace fully qualified domain name, you must set the environment variable `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` on your local development machine. This variable should point to the full path of the installed certificate on the cluster. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

Example (Python):

```python
import os
os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = "/etc/ssl/certs/ca-bundle.crt"
```

For other ways to set environment variables, see your operating system's documentation. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Logging and Debug Logs

Databricks Connect for Python uses standard Python logging, emitting messages to stderr. By default, logging is turned off. To enable debug-level logging, set the environment variable `SPARK_CONNECT_LOG_LEVEL=debug`. This will print all log messages at the `DEBUG` level and higher. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library for remote Spark execution.
- [Spark Connect](/concepts/spark-connect.md) – The protocol used for communication.
- Databricks Runtime – The runtime version requirements.
- gRPC – The underlying transport protocol.
- SSL/TLS Certificates – Handling custom certificates with gRPC.

## Sources

- advanced-usage-of-databricks-connect-databricks-on-aws.md

# Citations

1. [advanced-usage-of-databricks-connect-databricks-on-aws.md](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
