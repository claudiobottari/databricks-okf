---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5b94616ecb06156f9cbc227021c4fb3f16d3dfdbe18cdfee605b2bee1a5a50cd
  pageDirectory: concepts
  sources:
    - troubleshooting-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-connect-java-17-compatibility
    - DCJ1C
  citations:
    - file: troubleshooting-databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Connect Java 17 compatibility
description: Java 17's security restrictions block Apache Arrow reflection access needed by Databricks Connect; the fix requires setting --add-opens JVM flag.
tags:
  - databricks
  - java
  - compatibility
timestamp: "2026-06-19T23:14:57.174Z"
---

# [Databricks Connect](/concepts/databricks-connect.md) Java 17 Compatibility

**Databricks Connect Java 17 compatibility** refers to the issues and solutions encountered when using the [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) client with Java 17 as the runtime environment. Because [Databricks Connect](/concepts/databricks-connect.md) depends on Apache Arrow, which uses Java reflection to access private methods, Java 17’s stricter reflection restrictions can prevent initialization.

## Error: Failed to initialize MemoryUtil

When building a `DatabricksSession` using the Scala client on Java 17, you may encounter the following error:

```
Failed to initialize MemoryUtil
```

### Cause

The Apache Arrow library, a dependency of the [Databricks Connect](/concepts/databricks-connect.md) client, attempts to access a private Java method using reflection. Java 17 blocks such reflective access by default for security reasons, causing the initialization to fail. ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

### Solution

Before the JVM initialization, set the following `--add-opens` JVM argument to allow the reflective access:

```
--add-opens=java.base/java.nio=org.apache.arrow.memory.core,ALL-UNNAMED
```

This option opens the `java.nio` module in `java.base` to the Arrow memory core module (and all unnamed modules), enabling the reflection call. For further details, see the [Apache Arrow Java Compatibility](https://arrow.apache.org/java/current/install.html#java-compatibility) documentation. ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

## Applicability

This compatibility issue applies to [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) on [Databricks Runtime 13.3 LTS](/concepts/databricks-runtime-133-lts.md) and above. The Python client may have different troubleshooting steps; refer to the Python-specific troubleshooting guide for that variant. ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – Overview of the client used to connect IDEs and applications to Databricks clusters.
- Apache Arrow Java Compatibility – Official documentation for Arrow’s Java requirements, including the `--add-opens` workaround.
- [Troubleshooting Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) – Full troubleshooting guide for Scala client issues.
- Troubleshooting Databricks Connect for Python – Python-specific troubleshooting counterpart.
- Java 17 Reflection Restrictions – General information on Java 17’s stronger encapsulation of internal APIs.

## Sources

- troubleshooting-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [troubleshooting-databricks-connect-for-scala-databricks-on-aws.md](/references/troubleshooting-databricks-connect-for-scala-databricks-on-aws-fde9e272.md)
