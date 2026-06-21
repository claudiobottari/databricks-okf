---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fcfb8c0086159d063f5a41756ee05e071425d08ad97fc7602d0b33f0596ed7b7
  pageDirectory: concepts
  sources:
    - advanced-usage-of-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-custom-proxy-headers
    - DCCPH
  citations:
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
title: Databricks Connect Custom Proxy Headers
description: Using the header() method to add custom HTTP headers to gRPC requests when a proxy service sits between the client and the Databricks cluster
tags:
  - databricks
  - networking
  - proxies
timestamp: "2026-06-19T08:54:41.952Z"
---

Here is the wiki page for “Databricks Connect Custom Proxy Headers,” written solely from the provided source material.

---

## Databricks Connect Custom Proxy Headers

**Databricks Connect Custom Proxy Headers** allow advanced users to inject custom HTTP headers into the gRPC requests that Databricks Connect sends to Databricks clusters. This is useful when a proxy service is installed between the client and the cluster and that proxy requires specific headers to be present in the gRPC over HTTP/2 requests. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Overview

Databricks Connect communicates with Databricks clusters via gRPC over HTTP/2. In some network architectures, an intermediate proxy server may require custom headers — such as authentication tokens, tracing IDs, or routing information — before it forwards the request to the target cluster. By setting custom headers on the [DatabricksSession](/concepts/databrickssession.md), you can satisfy these proxy requirements without modifying the underlying Spark Connect protocol. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Usage

Use the `.header()` method when building a `DatabricksSession` to add custom headers. Multiple headers can be added by chaining calls. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

#### Python

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder \
    .header('x-custom-header', 'value') \
    .getOrCreate()
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

#### Scala

```scala
import com.databricks.connect.[[databrickssession|DatabricksSession]]

val spark = [[databrickssession|DatabricksSession]].builder()
  .header("x-custom-header", "value")
  .getOrCreate()
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### When to Use Custom Headers

Custom headers are intended for **advanced users** who have installed a proxy service between their client and the Databricks cluster. Common use cases include: ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

- Passing a proxy authentication token.
- Adding a correlation or tracing header for observability.
- Inserting a header that routes requests to a specific backend.

Do **not** use custom headers to override the standard Databricks authentication header — the SDK manages authentication (token) separately via the `remote()` function or `SPARK_REMOTE` environment variable. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Related Concepts

- Advanced Usage of Databricks Connect – Configuration of Spark Connect connection strings and certificates.
- [DatabricksSession](/concepts/databrickssession.md) – The main entry point for building a Spark session in Databricks Connect.
- [Spark Connect](/concepts/spark-connect.md) – The underlying protocol for client-server communication.
- Proxy Configuration – General guidance on network proxies in Databricks.

### Sources

- advanced-usage-of-databricks-connect-databricks-on-aws.md

# Citations

1. [advanced-usage-of-databricks-connect-databricks-on-aws.md](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
