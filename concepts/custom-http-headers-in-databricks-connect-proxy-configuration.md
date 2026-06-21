---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5b804172b5a6b17bac7d502a192f2b82f94a7d6632978784134bc87a9b7ef64e
  pageDirectory: concepts
  sources:
    - advanced-usage-of-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-http-headers-in-databricks-connect-proxy-configuration
    - CHHIDCPC
  citations:
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
title: Custom HTTP Headers in Databricks Connect Proxy Configuration
description: Using the header() method to add custom HTTP headers for proxy servers when using Databricks Connect with gRPC over HTTP/2.
tags:
  - databricks
  - networking
  - proxy
timestamp: "2026-06-19T17:28:27.446Z"
---

## Custom HTTP Headers in Databricks Connect Proxy Configuration

**Custom HTTP Headers in Databricks Connect Proxy Configuration** refers to the ability to add custom key-value pairs to HTTP requests sent by Databricks Connect, typically required when a proxy service sits between the client and the Databricks cluster and needs specific headers for authentication, routing, or policy enforcement.

### Overview

Databricks Connect communicates with Databricks Clusters via gRPC over HTTP/2. Advanced users may choose to install a proxy service between the client and the Databricks cluster to gain better control over incoming requests. In such setups, the proxy may require custom headers to be present in the HTTP requests — for example, to pass authentication tokens or routing hints. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Adding Custom Headers

Databricks Connect provides a `header()` method on the `DatabricksSession.builder` to attach custom headers to all HTTP requests. The method takes a header name and a header value as strings.

**Python example:**

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder \
    .header('x-custom-header', 'value') \
    .getOrCreate()
```

The same pattern is available for Scala. Multiple calls to `.header()` can be chained to add several headers. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Intended Use Case

The primary scenario for custom headers is when an intermediate proxy service inspects or modifies the traffic between the Databricks Connect client and the Databricks cluster. The proxy may mandate certain headers — such as an API key, a session identifier, or a tenant ID — before forwarding the request. By using the `header()` method, the client ensures every gRPC-over-HTTP/2 request carries those required headers. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library for connecting local IDEs to Databricks clusters.
- [Spark Connect](/concepts/spark-connect.md) – The underlying protocol (gRPC over HTTP/2) used by Databricks Connect.
- Proxy Server Configuration – General guidance on placing a proxy between client and cluster.
- [Spark Connect Connection String](/concepts/spark-connect-connection-string.md) – Alternative way to configure the connection endpoint and authentication.

### Sources

- advanced-usage-of-databricks-connect-databricks-on-aws.md

# Citations

1. [advanced-usage-of-databricks-connect-databricks-on-aws.md](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
