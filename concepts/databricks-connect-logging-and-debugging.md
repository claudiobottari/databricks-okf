---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2ffd59e6aee14b530afb321e1bac6b886149850c4c3f703626eb5b94487de64f
  pageDirectory: concepts
  sources:
    - advanced-usage-of-databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-logging-and-debugging
    - Debugging and Databricks Connect Logging
    - DCLAD
    - databricks-connect-logging-and-debug-logs
    - Debug Logs and Databricks Connect Logging
    - DCLADL
    - databricks-connect-logging-configuration
    - DCLC
  citations:
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
title: Databricks Connect Logging and Debugging
description: Enabling debug logging in Databricks Connect for Python via the SPARK_CONNECT_LOG_LEVEL environment variable
tags:
  - databricks
  - debugging
  - logging
timestamp: "2026-06-19T08:54:42.168Z"
---

# Databricks Connect Logging and Debugging

**Databricks Connect Logging and Debugging** covers the mechanisms to capture diagnostic information from [Databricks Connect](/concepts/databricks-connect.md) client applications, including log output, custom HTTP headers for proxy environments, and SSL/TLS certificate configuration. These tools help developers troubleshoot connection issues, query execution problems, and other runtime behaviors.

## Python Logging

Databricks Connect for Python uses standard [Python logging](https://docs.python.org/3/library/logging.html) to produce log messages. Logs are emitted to the standard error stream (stderr), and by default logging is turned off—no log messages are produced. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Enabling Debug Logging

To enable logging, set the environment variable `SPARK_CONNECT_LOG_LEVEL=debug`. This modifies the default log level and prints all log messages at the `DEBUG` level and higher to stderr. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

Set the environment variable before launching your Python application:

```bash
export SPARK_CONNECT_LOG_LEVEL=debug
python my_connect_app.py
```

Or set it programmatically (must be done before initializing the session):

```python
import os
os.environ["SPARK_CONNECT_LOG_LEVEL"] = "debug"
from databricks.connect import [[databrickssession|DatabricksSession]]
spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

### What Debug Logs Contain

When debug logging is enabled, the logs include detailed information about the gRPC communication between the client and the Spark Connect server on the Databricks cluster. This covers connection establishment, gRPC request and response metadata, execution plan serialization/deserialization, and error/exception details from the remote server. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md] (Log content is inferred from the nature of Spark Connect; the source states that logs are emitted at DEBUG level and higher.)

## Custom HTTP Headers for Proxy Environments

If a proxy service sits between the Databricks Connect client and the Databricks cluster and requires custom HTTP headers, use the `header()` method to add them:

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
spark = [[databrickssession|DatabricksSession]].builder.header('x-custom-header', 'value').getOrCreate()
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## SSL/TLS Certificate Configuration

If your cluster relies on a custom SSL/TLS certificate to resolve a Databricks workspace fully qualified domain name (FQDN), set the `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` environment variable on your local development machine to the full path to the certificate file installed on the cluster:

```python
import os
os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = "/etc/ssl/certs/ca-bundle.crt"
```

^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

This configuration is essential for secure gRPC connections when the workspace uses a non-default certificate authority.

## Spark Connect Connection String

For advanced debugging or alternative connection setups, you can configure the Spark Connect connection string using the `remote` function or the `SPARK_REMOTE` environment variable. This is useful when testing against a local Spark Connect server or when you need full control over the connection parameters. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

Example using the `remote` function:

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
spark = [[databrickssession|DatabricksSession]].builder.remote(
    "sc://<workspace-instance-name>:443/;token=<token>;x-databricks-cluster-id=<cluster-id>"
).getOrCreate()
```

Or via environment variable:

```bash
export SPARK_REMOTE="sc://<workspace-instance-name>:443/;token=<token>;x-databricks-cluster-id=<cluster-id>"
```

Then initialize `DatabricksSession.builder.getOrCreate()`. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — Client library for connecting to Databricks clusters
- [Spark Connect](/concepts/spark-connect.md) — Underlying protocol for Databricks Connect connections
- gRPC — Communication protocol used by Spark Connect
- Databricks Runtime — Server-side environment for cluster execution

## Sources

- advanced-usage-of-databricks-connect-databricks-on-aws.md

# Citations

1. [advanced-usage-of-databricks-connect-databricks-on-aws.md](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
