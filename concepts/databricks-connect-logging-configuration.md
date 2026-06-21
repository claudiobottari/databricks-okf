---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3a9e09deb75c83f81760dc954e05d57b4f879794f0cbe0ee2f2eb80ce4c4f240
  pageDirectory: concepts
  sources:
    - advanced-usage-of-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-logging-configuration
    - DCLC
  citations:
    - file: advanced-usage-of-databricks-connect-databricks-on-aws.md
title: Databricks Connect Logging Configuration
description: Enabling debug logs in Databricks Connect for Python by setting the `SPARK_CONNECT_LOG_LEVEL=debug` environment variable, which sends logs to stderr using standard Python logging.
tags:
  - databricks-connect
  - debugging
  - logging
timestamp: "2026-06-19T22:00:42.364Z"
---

# Databricks Connect Logging Configuration

**Databricks Connect Logging Configuration** refers to the mechanism for controlling and viewing log output from the [Databricks Connect](/concepts/databricks-connect.md) Python client library. The client uses the standard Python logging framework to emit diagnostic messages to the standard error stream (*stderr*). ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

## Enabling Debug Logs

By default, logging in Databricks Connect for Python is completely turned off. To enable debug‑level output, set the environment variable `SPARK_CONNECT_LOG_LEVEL` to `debug`. When this variable is set, all log messages at the `DEBUG` level and higher are printed to stderr. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

### Example

```bash
export SPARK_CONNECT_LOG_LEVEL=debug
```

After setting this environment variable, the next time a [DatabricksSession](/concepts/databrickssession.md) is created or a Spark Connect operation is performed, detailed logs appear on stderr.

## Configuration Details

- **Log framework:** Python’s built-in `logging` module.
- **Output destination:** Standard error stream (stderr).
- **Default state:** Off (no logs are emitted).
- **Control:** Environment variable `SPARK_CONNECT_LOG_LEVEL` set to `debug` enables logging at DEBUG level and above. ^[advanced-usage-of-databricks-connect-databricks-on-aws.md]

The logging behavior is entirely driven by this single environment variable; no other logging configuration files or programmatic calls are required.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library connecting to Databricks clusters.
- Python logging – The standard logging framework used by Databricks Connect.
- [Environment variables](/concepts/model-serving-environment-variables.md) – Mechanism for passing configuration to the client.
- Debugging – Common debugging techniques for Databricks Connect.
- [Spark Connect Connection String](/concepts/spark-connect-connection-string.md) – An advanced connection method that may benefit from logging.

## Sources

- advanced-usage-of-databricks-connect-databricks-on-aws.md

# Citations

1. [advanced-usage-of-databricks-connect-databricks-on-aws.md](/references/advanced-usage-of-databricks-connect-databricks-on-aws-e72df911.md)
