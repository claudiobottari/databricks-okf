---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 03931058860191feb0883da1328ab54b529b914641a325cd7a4fa1ebfe7e3eeb
  pageDirectory: concepts
  sources:
    - troubleshooting-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-memoryutil-initialization-error
    - DCMIE
  citations:
    - file: troubleshooting-databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Connect MemoryUtil initialization error
description: An error occurring when building a DatabricksSession due to Apache Arrow's reflection access to private Java methods being blocked in Java 17.
tags:
  - databricks
  - java
  - arrow
  - troubleshooting
timestamp: "2026-06-19T23:14:51.324Z"
---

# [Databricks Connect](/concepts/databricks-connect.md) MemoryUtil Initialization Error

The **Databricks Connect MemoryUtil Initialization Error** occurs when trying to build a `DatabricksSession` and the system returns the message `Failed to initialize MemoryUtil`. This error is specific to [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) when running on Java 17. ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

## Cause

Apache Arrow is a dependency of the [Databricks Connect](/concepts/databricks-connect.md) client. During initialization, Arrow attempts to access a private Java method using reflection. In Java 17, such reflective access is blocked by default for security reasons. This causes the `MemoryUtil` initialization to fail. ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

## Solution

Set the following JVM command-line argument **before JVM initialization** to open the `java.nio` module to Arrow's memory core: ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

```
--add-opens=java.base/java.nio=org.apache.arrow.memory.core,ALL-UNNAMED
```

This argument allows the reflective access that Arrow requires. For more details, see the Apache Arrow Java Compatibility documentation. ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The framework for connecting IDEs and applications to Databricks clusters.
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) – The Scala-specific client.
- Apache Arrow – An in-memory columnar data format used by the client.
- Java 17 compatibility – Security changes in Java 17 that affect reflection-based libraries.
- Troubleshooting Databricks Connect – General guide for common issues.

## Sources

- troubleshooting-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [troubleshooting-databricks-connect-for-scala-databricks-on-aws.md](/references/troubleshooting-databricks-connect-for-scala-databricks-on-aws-fde9e272.md)
