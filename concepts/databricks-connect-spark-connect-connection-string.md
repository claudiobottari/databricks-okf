---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c22539d79b3051efd6b55030c7e3271e4d4f73bab6e4d405eefcca0a6646b581
  pageDirectory: concepts
  sources:
    - advanced-usage-of-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-spark-connect-connection-string
    - DCSCCS
  citations:
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
title: Databricks Connect Spark Connect Connection String
description: Advanced method to connect Databricks Connect to a cluster using a Spark Connect connection string, either via the remote() function or the SPARK_REMOTE environment variable.
tags:
  - databricks
  - connectivity
  - spark-connect
timestamp: "2026-06-19T17:29:31.345Z"
---

Based on the provided source material, here is the wiki page for "Databricks Connect Spark Connect Connection String".

---
title: Databricks Connect Spark Connect Connection String
summary: How to configure Databricks Connect using the Spark Connect connection string via the remote() function or SPARK_REMOTE environment variable
sources:
  - advanced-usage-of-databricks-connect-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T08:55:22.471Z"
updatedAt: "2026-06-19T13:54:52.207Z"
tags:
  - databricks
  - spark-connect
  - configuration
aliases:
  - databricks-connect-spark-connect-connection-string
  - DCSCCS
  - DCC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# Databricks Connect Spark Connect Connection String

**Databricks Connect Spark Connect Connection String** refers to the URI-based connection format used to establish a direct gRPC connection between a local development environment and a Databricks cluster via the Spark Connect protocol. This approach is an advanced alternative to the standard configuration methods for [Databricks Connect](/concepts/databricks-connect.md).^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Overview

The Spark Connect connection string allows you to programmatically specify the connection parameters for a Databricks cluster when initializing a [DatabricksSession](/concepts/databrickssession.md). The string contains the workspace endpoint, authentication token, and cluster identifier, and can be passed directly to the `remote()` function or set as an environment variable.^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Connection String Format

The standard Spark Connect connection string for Databricks follows this format:^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

```
sc://<workspace-instance-name>:443/;token=<access-token-value>;x-databricks-cluster-id=<cluster-id>
```

The components are:
- `sc://` — The Spark Connect protocol prefix
- `<workspace-instance-name>` — Your Databricks workspace instance name (e.g., `dbc-XXXXXXXX.cloud.databricks.com`)
- `:443/` — The standard HTTPS port for secure communication
- `;token=<access-token-value>` — Your Databricks personal access token for authentication
- `;x-databricks-cluster-id=<cluster-id>` — The ID of the target cluster for executing Spark operations

## Usage Methods

### Using the `remote()` Function

You can construct the connection string dynamically and pass it to the `remote()` builder method:^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

workspace_instance_name = retrieve_workspace_instance_name()
token = retrieve_token()
cluster_id = retrieve_cluster_id()

spark = [[databrickssession|DatabricksSession]].builder.remote(
    f"sc://{workspace_instance_name}:443/;token={token};x-databricks-cluster-id={cluster_id}"
).getOrCreate()
```

### Using the `SPARK_REMOTE` Environment Variable

Alternatively, set the `SPARK_REMOTE` environment variable with the connection string, then initialize the session without arguments:^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

```bash
export SPARK_REMOTE="sc://<workspace-instance-name>:443/;token=<access-token-value>;x-databricks-cluster-id=<cluster-id>"
```

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

## Using Spark Connect Server with Databricks Connect

You can optionally run Databricks Connect against an open source [Spark Connect](/concepts/spark-connect.md) server rather than a Databricks cluster.^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

1. Start a local Spark Connect server (see [Apache Spark documentation](https://spark.apache.org/docs/latest/spark-connect-overview.html) for instructions).
2. Set `SPARK_REMOTE` to point to your local server:
   ```bash
   export SPARK_REMOTE="sc://localhost"
   ```
3. Initialize the Databricks session:
   ```python
   from databricks.connect import [[databrickssession|DatabricksSession]]
   spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
   ```

**Important:** Some features available in Databricks Runtime and Databricks Connect are exclusive to Databricks or not yet released in open source Apache Spark. Code relying on these features may fail when connecting to an open source Spark Connect server.^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Communication Protocol

Databricks Connect communicates with Databricks clusters via **gRPC over HTTP/2**. The connection string establishes this secure, efficient communication channel between the client and the cluster.^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Custom HTTP Headers

Advanced users who install a proxy service between the client and the Databricks cluster may need to add custom headers to HTTP requests. Use the `header()` method to add custom headers:^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.header('x-custom-header', 'value').getOrCreate()
```

## SSL/TLS Certificates

If your cluster relies on a **custom SSL/TLS certificate** to resolve the Databricks workspace fully qualified domain name (FQDN), you must set the `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` environment variable on your local development machine to the full path of the installed certificate on the cluster:^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

```python
import os
os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = "/etc/ssl/certs/ca-bundle.crt"
```

## Related Concepts

- [DatabricksSession](/concepts/databrickssession.md) — The main entry point for Databricks Connect
- [Spark Connect](/concepts/spark-connect.md) — The gRPC-based protocol underlying the connection
- Databricks Personal Access Token — Authentication mechanism for the connection string
- [Cluster Configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) — Standard configuration alternatives
- gRPC and HTTP/2 — The underlying transport protocol

## Sources

- advanced-usage-of-databricks-connect-databricks-on-aws.md

# Citations

1. [advanced-usage-of-databricks-connect-databricks-on-aws.md](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
