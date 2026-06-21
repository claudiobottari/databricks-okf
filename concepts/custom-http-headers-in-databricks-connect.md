---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 09299712e5df0b63d257dc593f4a0ad516079c48ca045223c27aecfa5bbf3764
  pageDirectory: concepts
  sources:
    - advanced-usage-of-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-http-headers-in-databricks-connect
    - CHHIDC
  citations:
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
title: Custom HTTP Headers in Databricks Connect
description: Using the `header()` method on DatabricksSession.builder to add custom HTTP headers to gRPC requests, useful when a proxy is placed between the client and the Databricks cluster.
tags:
  - databricks-connect
  - networking
  - proxy
timestamp: "2026-06-19T22:01:34.614Z"
---

```yaml
---
title: Custom HTTP Headers in Databricks Connect
summary: Adding custom headers to gRPC HTTP/2 requests in Databricks Connect to support proxy services between the client and Databricks cluster
sources:
  - advanced-usage-of-databricks-connect-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:41:36.205Z"
updatedAt: "2026-06-18T10:41:36.205Z"
tags:
  - databricks
  - proxy
  - networking
aliases:
  - custom-http-headers-in-databricks-connect
  - CHHIDC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 2
---

# Custom HTTP Headers in Databricks Connect

**Custom HTTP Headers** allow advanced users of [[Databricks Connect]] to add proprietary metadata to gRPC/HTTP/2 requests made between client code and Databricks clusters, enabling integration with proxy services or custom networking infrastructure.

## Overview

Databricks Connect communicates with Databricks clusters via gRPC over HTTP/2. When a proxy service is installed between the client and the cluster to provide additional control over request routing, that proxy may require custom headers to be present in the HTTP requests. The `header()` method on `DatabricksSession.Builder` provides a mechanism to inject those headers before the session is established. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Adding Custom Headers

Custom headers are added by chaining the `.header()` method on the builder object before calling `.getOrCreate()`. The method accepts a header name and a value as string arguments. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Python

```python
from databricks.connect import [DatabricksSession](/concepts/databrickssession.md)

spark = (
    [DatabricksSession](/concepts/databrickssession.md).builder
    .header('x-custom-header', 'value')
    .getOrCreate()
)
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Scala

```scala
import com.databricks.connect.[DatabricksSession](/concepts/databrickssession.md)

val spark = [DatabricksSession](/concepts/databrickssession.md).builder
  .header("x-custom-header", "value")
  .getOrCreate()
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Use Cases

Custom HTTP headers are typically needed when an organization deploys a proxy in the request path between the client machine running Databricks Connect and the remote Databricks cluster. Common scenarios include:

- **Authentication proxies** — Proxies that require a custom token or API key to be forwarded in a specific header field.
- **Traffic routing proxies** — Proxies that inspect a custom header to decide which backend endpoint or network path should handle the connection.
- **Audit and compliance** — Proxies that log a custom correlation ID header for tracing every request through the organization's infrastructure.

## Relationship to Connection String Configuration

Custom headers are one of several configuration parameters that can be supplied when building a session. The `.header()` method is an alternative to embedding header values directly in the [[Spark Connect connection string]] via the `remote()` function or the `SPARK_REMOTE` environment variable. Both approaches produce the same effect — the header is added to every gRPC request sent to the cluster.

## Related Concepts

- [[Databricks Connect]] — The client library that establishes the Spark Connect session
- [[Spark Connect]] — The underlying protocol layer that carries the gRPC requests
- gRPC — The remote procedure call framework used by Spark Connect
- HTTP/2 — The transport protocol on which gRPC is layered
- [[Spark Connect connection string]] — Alternative method for passing configuration to the session

## Sources

- advanced-usage-of-databricks-connect-databricks-on-aws.md
```

# Citations

1. [advanced-usage-of-databricks-connect-databricks-on-aws.md](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
