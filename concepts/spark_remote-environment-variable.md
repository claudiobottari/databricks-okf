---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2a81507d85e22648c2451ee915908076ddc8385ff75d9bb7d14cf93584e1aebe
  pageDirectory: concepts
  sources:
    - advanced-usage-of-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark_remote-environment-variable
    - SEV
    - PySpark Environment Variables
    - SPARK_REMOTE Environment Variable
    - SPARK_REMOTE environment variable
  citations:
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
title: SPARK_REMOTE Environment Variable
description: Environment variable used to point Databricks Connect or Spark Connect clients to a remote Spark server instance
tags:
  - databricks
  - spark-connect
  - environment-variables
timestamp: "2026-06-19T13:55:03.075Z"
---

```markdown
---
title: SPARK_REMOTE Environment Variable
summary: An environment variable used by Databricks Connect to specify the Spark Connect connection string for connecting to a remote Databricks cluster or an open source Spark Connect server.
sources:
  - advanced-usage-of-databricks-connect-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:00:00.000Z"
updatedAt: "2026-06-18T15:00:00.000Z"
tags:
  - databricks
  - authentication
  - configuration
  - environment-variable
aliases:
  - SPARK_REMOTE
  - spark-remote-environment-variable
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# SPARK_REMOTE Environment Variable

The `SPARK_REMOTE` environment variable allows you to specify a [[Spark Connect]] connection string that Databricks Connect uses to connect to a remote Databricks cluster or an open source Spark Connect server. Setting this variable eliminates the need to include connection details directly in code via the `remote()` method. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Usage

After setting the `SPARK_REMOTE` environment variable to a valid Spark Connect connection string, you can initialize a `DatabricksSession` using `DatabricksSession.builder.getOrCreate()`. The session automatically reads the variable and uses the provided URI for authentication and connection. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Connecting to a Databricks Cluster

Set the variable to a string that includes the workspace instance name, an access token, and the cluster ID:

```
sc://<workspace-instance-name>:443/;token=<access-token-value>;x-databricks-cluster-id=<cluster-id>
```

Then create the session:

```python
from databricks.connect import [DatabricksSession](/concepts/databrickssession.md)

spark = [DatabricksSession](/concepts/databrickssession.md).builder.getOrCreate()
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Connecting to a Local Spark Connect Server

You can also point `SPARK_REMOTE` to an open source Spark Connect server:

```bash
export SPARK_REMOTE="sc://localhost"
```

After setting the variable, use `DatabricksSession.builder.getOrCreate()` to connect. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Alternative: Using the `remote()` Function

Instead of using the environment variable, you can pass the same connection string directly to the `remote()` method on `DatabricksSession.builder`:

```python
from databricks.connect import [DatabricksSession](/concepts/databrickssession.md)

spark = [DatabricksSession](/concepts/databrickssession.md).builder.remote(
    f"sc://{workspace_instance_name}:443/;token={token};x-databricks-cluster-id={cluster_id}"
).getOrCreate()
```

This approach is equivalent but embeds the connection string in code rather than in an environment variable. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [[Databricks Connect]] — The client library that uses `SPARK_REMOTE` for remote connectivity.
- [[DatabricksSession]] — The session class that reads `SPARK_REMOTE` when `getOrCreate()` is called.
- [[Spark Connect]] — The underlying protocol that enables remote DataFrame operations.
- Authentication — How tokens and cluster IDs are passed in the connection string.
- Cluster Configuration — Setting up a Databricks cluster for remote client connections.

## Sources

- advanced-usage-of-databricks-connect-databricks-on-aws.md
```

# Citations

1. [advanced-usage-of-databricks-connect-databricks-on-aws.md](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
