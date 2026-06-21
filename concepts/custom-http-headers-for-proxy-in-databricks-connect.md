---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: db72f7a95e074faf60cdff19fe935713bdf88aa23e34c6a4b3d476b4a679dae6
  pageDirectory: concepts
  sources:
    - advanced-usage-of-databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-http-headers-for-proxy-in-databricks-connect
    - CHHFPIDC
  citations:
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
title: Custom HTTP Headers for Proxy in Databricks Connect
description: Using the `header()` method on DatabricksSession.builder to add custom HTTP headers for proxy services that sit between the client and the Databricks cluster.
tags:
  - databricks-connect
  - networking
  - proxy
  - configuration
timestamp: "2026-06-18T14:20:37.132Z"
---

Here is the wiki page for "Custom HTTP Headers for Proxy in Databricks Connect".

---

## Custom HTTP Headers for Proxy in Databricks Connect

**Custom HTTP Headers for Proxy in Databricks Connect** allows advanced users to add custom headers to HTTP requests made by the Databricks Connect client when communicating with a Databricks cluster through an intermediary proxy service.

### Overview

Databricks Connect communicates with Databricks clusters via gRPC over HTTP/2. Advanced users may choose to install a proxy service between the client and the Databricks cluster to have better control over incoming client requests. In some cases, these proxies require custom headers in the HTTP requests.^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Adding Custom Headers

Use the `header()` method on the `DatabricksSession.builder` to add custom headers to HTTP requests. The method takes a header name and value as arguments and is called before `getOrCreate()`. Multiple headers can be added by chaining multiple `header()` calls.^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

The following example demonstrates adding a custom header:

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.header('x-custom-header', 'value').getOrCreate()
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that connects local code to Databricks clusters
- Configure Spark Connect Connection String — Alternative method for specifying cluster connection parameters
- [Spark Connect Server](/concepts/spark-connect.md) — The open source server that Databricks Connect can optionally target

### Sources

- advanced-usage-of-databricks-connect-databricks-on-aws.md

# Citations

1. [advanced-usage-of-databricks-connect-databricks-on-aws.md](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
