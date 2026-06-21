---
title: Troubleshooting Databricks Connect for Scala | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/troubleshooting
ingestedAt: "2026-06-18T08:06:51.949Z"
---

note

This article covers Databricks Connect for Databricks Runtime 13.3 LTS and above.

This article provides troubleshooting information for Databricks Connect for Scala. Databricks Connect enables you to connect popular IDEs, notebook servers, and custom applications to Databricks clusters. See [Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/). For the Python version of this article, see [Troubleshooting Databricks Connect for Python](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/troubleshooting).

**Issue**: When you try to run code with Databricks Connect, you get an error messages that contains strings such as `StatusCode.UNAVAILABLE`, `StatusCode.UNKNOWN`, `DNS resolution failed`, or `Received http2 header with status: 500`.

**Cause**: Databricks Connect cannot reach your cluster.

**Solutions**:

*   Check to make sure that your workspace instance name is correct. If you use environment variables, check to make sure the related environment variable is available and correct on your local development machine.
*   Check to make sure that your cluster ID is correct. If you use environment variables, check to make sure the related environment variable is available and correct on your local development machine.
*   Check to make sure that your cluster has the correct custom cluster version that is compatible with Databricks Connect.

## Errors connecting to Apache Spark server[​](#errors-connecting-to-apache-spark-server "Direct link to errors-connecting-to-apache-spark-server")

**Issue**:

Attempting to connect to an open source Apache Spark server (for example, a locally running Apache Spark 3.5.x Spark Connect server at `sc://localhost`), results in errors such as class not found, API behavior mismatches, or serialization failures.

**Cause**:

Databricks Connect is built against Databricks Runtime, which has different dependencies than open source Apache Spark. In particular, Databricks Connect 15.4 and 16.4 are incompatible with Apache Spark 3.5.x because they use a different version of the `json4s` library.

**Solution**:

Use a Databricks cluster or serverless compute instead of an open source Apache Spark server. See [Compute configuration for Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config).

## The filename, directory name, or volume label syntax is incorrect on Windows[​](#the-filename-directory-name-or-volume-label-syntax-is-incorrect-on-windows "Direct link to The filename, directory name, or volume label syntax is incorrect on Windows")

**Issue**: You are using Databricks Connect on Windows and see:

    The filename, directory name, or volume label syntax is incorrect.

**Cause**: Databricks Connect was installed into a directory with a [space in your path](https://stackoverflow.com/questions/47028892/why-does-spark-shell-fail-with-the-filename-directory-name-or-volume-label-sy).

**Solution**: You can work around this by either installing into a directory path without spaces, or configuring your path using the [short name form](https://stackoverflow.com/questions/892555/how-do-i-specify-c-program-files-without-a-space-in-it-for-programs-that-cant).

## Error: Failed to initialize MemoryUtil[​](#error-failed-to-initialize-memoryutil "Direct link to Error: Failed to initialize MemoryUtil")

**Issue**: When you try to build a `DatabricksSession`, it returns an error `Failed to initialize MemoryUtil`.

**Cause**: Apache Arrow is a dependency of the Databricks Connect client, and it is trying to access a private Java method using reflection, which is by default blocked in Java 17 because of security considerations.

**Solution**:

Set the following JVM field prior to JVM initialization:

    --add-opens=java.base/java.nio=org.apache.arrow.memory.core,ALL-UNNAMED

For more information, see [Apache Arrow Java Compatibility](https://arrow.apache.org/java/current/install.html#java-compatibility).
