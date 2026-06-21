---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9ee89a72c6f315c77292d7deb9f8ed8f7b288b32d9e321d4890128cdbcb41fb4
  pageDirectory: concepts
  sources:
    - advanced-usage-of-databricks-connect-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-connect-connection-string
    - SCCS
    - Configure Spark Connect Connection String
    - Configure a connection to a cluster
  citations:
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
title: Spark Connect Connection String
description: Advanced method to configure Databricks Connect by passing a Spark Connect connection string via the `remote` function or the `SPARK_REMOTE` environment variable.
tags:
  - databricks-connect
  - configuration
  - spark-connect
timestamp: "2026-06-19T22:00:31.041Z"
---

# Spark Connect Connection String

The **Spark Connect connection string** is a client-side configuration string that tells a [Databricks Connect](/concepts/databricks-connect.md) client how to reach a Spark Connect server — either a Databricks cluster or a local open source Spark Connect server. It encodes the endpoint, authentication token, and, when connecting to a Databricks cluster, the target cluster ID.

## Connection String Format

When connecting to a Databricks cluster, the connection string follows this pattern:

```
sc://<workspace-instance-name>:443/;token=<access-token-value>;x-databricks-cluster-id=<cluster-id>
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

- `sc://` – Scheme for Spark Connect protocol (gRPC over HTTP/2).
- `<workspace-instance-name>` – The Databricks workspace instance name (e.g., `dbc-XXXXXXXX.cloud.databricks.com`).
- `:443` – Standard HTTPS port.
- `;token=<access-token-value>` – The personal access token or service principal token.
- `;x-databricks-cluster-id=<cluster-id>` – The ID of the Databricks cluster to connect to.

## Passing the Connection String

You can supply the connection string in one of two ways.

### Using the `remote()` Function

When constructing a [DatabricksSession](/concepts/databrickssession.md), call the `remote()` method with the full connection string:

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

### Using the `SPARK_REMOTE` Environment Variable

Set the `SPARK_REMOTE` environment variable to the same string. After it is set, you can create a session without explicitly passing a remote string:

```bash
export SPARK_REMOTE="sc://<workspace-instance-name>:443/;token=<access-token-value>;x-databricks-cluster-id=<cluster-id>"
```

Then, in your Python or Scala code:

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Connecting to an Open Source Spark Connect Server

You can also target a local (non‑Databricks) Spark Connect server. In that case the connection string is simply `sc://localhost` (or `sc://hostname:port`). Some Databricks‑exclusive features may not be available.

```bash
export SPARK_REMOTE="sc://localhost"
```

After setting the environment variable, initialize the session as shown above.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library that uses this connection string.
- [DatabricksSession](/concepts/databrickssession.md) – The entry point for creating a Spark session with Databricks Connect.
- [Configure a connection to a cluster](/concepts/spark-connect-connection-string.md) – Alternative setup methods for Databricks Connect.

## Sources

- advanced-usage-of-databricks-connect-databricks-on-aws.md

# Citations

1. [advanced-usage-of-databricks-connect-databricks-on-aws.md](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
