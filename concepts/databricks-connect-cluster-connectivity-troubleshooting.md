---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5a22bf6f5cfbb8f16b6c15ea4ea5ff0a3e0981985c02d6f04d48fab78478290b
  pageDirectory: concepts
  sources:
    - troubleshooting-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-cluster-connectivity-troubleshooting
    - DCCCT
  citations:
    - file: troubleshooting-databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Connect cluster connectivity troubleshooting
description: Common errors and fixes when Databricks Connect cannot reach a cluster, including checking workspace instance name, cluster ID, and cluster version compatibility.
tags:
  - databricks
  - troubleshooting
  - connectivity
timestamp: "2026-06-19T23:14:50.353Z"
---

# [Databricks Connect](/concepts/databricks-connect.md) Cluster Connectivity Troubleshooting

This page covers common connectivity issues encountered when using [Databricks Connect](/concepts/databricks-connect.md) for Scala. [Databricks Connect](/concepts/databricks-connect.md) allows you to connect IDEs, notebook servers, and custom applications to a Databricks cluster. The guidance below applies to [Databricks Runtime 13.3 LTS](/concepts/databricks-runtime-133-lts.md) and above.

## Cluster Unreachable Errors

**Issue:** Running code with [Databricks Connect](/concepts/databricks-connect.md) produces error messages containing strings such as `StatusCode.UNAVAILABLE`, `StatusCode.UNKNOWN`, `DNS resolution failed`, or `Received http2 header with status: 500`. ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

**Cause:** [Databricks Connect](/concepts/databricks-connect.md) cannot reach your cluster. ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

**Solutions:**  
- Verify that your workspace instance name is correct. If you use environment variables, ensure the related variable is available and correct on your local machine.  
- Verify that your cluster ID is correct.  
- Ensure your cluster is running a custom cluster version compatible with [Databricks Connect](/concepts/databricks-connect.md).  

^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

## Errors Connecting to an Open Source Apache Spark Server

**Issue:** Attempting to connect to an open source Apache Spark server (for example, a locally running Spark 3.5.x [Spark Connect](/concepts/spark-connect.md) server at `sc://localhost`) results in class‑not‑found errors, API behavior mismatches, or serialization failures. ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

**Cause:** [Databricks Connect](/concepts/databricks-connect.md) is built against Databricks Runtime, which has different dependencies than open source Apache Spark. Specifically, [Databricks Connect](/concepts/databricks-connect.md) 15.4 and 16.4 are incompatible with Apache Spark 3.5.x because they use a different version of the `json4s` library. ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

**Solution:** Use a Databricks cluster or serverless compute instead of an open source Apache Spark server. See [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md). ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

## Windows Path Issue

**Issue:** On Windows, the following error appears:  
`The filename, directory name, or volume label syntax is incorrect.` ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

**Cause:** [Databricks Connect](/concepts/databricks-connect.md) was installed into a directory path that contains a space. ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

**Solution:** Work around the issue by either installing into a directory path without spaces, or configuring your path using the short name form. ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

## Error: Failed to Initialize MemoryUtil

**Issue:** When building a `DatabricksSession`, the error `Failed to initialize MemoryUtil` occurs. ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

**Cause:** Apache Arrow (a dependency of the [Databricks Connect](/concepts/databricks-connect.md) client) tries to access a private Java method using reflection, which is blocked by default in Java 17 due to security restrictions. ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

**Solution:** Set the following JVM field before JVM initialization:  
`--add-opens=java.base/java.nio=org.apache.arrow.memory.core,ALL-UNNAMED` ^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

## Sources

- troubleshooting-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [troubleshooting-databricks-connect-for-scala-databricks-on-aws.md](/references/troubleshooting-databricks-connect-for-scala-databricks-on-aws-fde9e272.md)
