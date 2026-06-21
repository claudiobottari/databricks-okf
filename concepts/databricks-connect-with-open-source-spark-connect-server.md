---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6a2f2ac86599ffc1ff7180ec5f0e3e9b42907c2944dca47afb5d8d0c2473491a
  pageDirectory: concepts
  sources:
    - advanced-usage-of-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-with-open-source-spark-connect-server
    - DCWOSSCS
  citations:
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
title: Databricks Connect with Open Source Spark Connect Server
description: Running Databricks Connect against a local open source Spark Connect server instead of a Databricks cluster, with the caveat that some Databricks-exclusive features may fail.
tags:
  - databricks-connect
  - spark-connect
  - open-source
timestamp: "2026-06-19T22:01:52.289Z"
---

# Databricks Connect with Open Source Spark Connect Server

**Databricks Connect with Open Source Spark Connect Server** refers to the practice of using the [Databricks Connect](/concepts/databricks-connect.md) client library to connect to an open source Apache Spark Connect server, rather than a Databricks cluster. This approach is useful for testing, development, or environments where a Databricks cluster is not available.^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Important Caveat

Some features available in Databricks Runtime and Databricks Connect are exclusive to Databricks or have not yet been released in open source Apache Spark. If your code relies on these proprietary features, connecting to an open source Spark Connect server may fail with errors.^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Setup Steps

1. **Start a local Spark Connect server** by following the official Apache Spark guide: [How to use Spark Connect](https://spark.apache.org/docs/latest/spark-connect-overview.html).^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

2. **Configure the environment variable** `SPARK_REMOTE` to point to your Spark Connect server. For example:
   ```bash
   export SPARK_REMOTE="sc://localhost"
   ```
   ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

3. **Initialize a Databricks session** using `DatabricksSession.builder.getOrCreate()`. The `DatabricksSession` class automatically reads the `SPARK_REMOTE` variable and connects to the specified server.^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Python Example

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Scala Example

```scala
import com.databricks.connect.[[databrickssession|DatabricksSession]]

val spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## How It Works

[Databricks Connect](/concepts/databricks-connect.md) communicates with the cluster (or Spark Connect server) via **gRPC over HTTP/2**. When using an open source server, the same protocol is used. For advanced users who need to route requests through a proxy, custom HTTP headers can be added using the `header()` method during session creation.^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Spark Connect](/concepts/spark-connect.md) – The protocol used for remote Spark execution.
- [Databricks Connect](/concepts/databricks-connect.md) – The main client library for remote Spark operations.
- [DatabricksSession](/concepts/databrickssession.md) – The entry point for creating a Spark session via Databricks Connect.
- [SPARK_REMOTE](/concepts/spark-connect.md) – The environment variable that defines the connection string to a Spark Connect server.
- gRPC – The transport protocol underlying Spark Connect communication.

## Sources

- advanced-usage-of-databricks-connect-databricks-on-aws.md

# Citations

1. [advanced-usage-of-databricks-connect-databricks-on-aws.md](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
