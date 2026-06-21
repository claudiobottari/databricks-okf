---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 80c36595da7f279285ccc8ab9aa2c28a296751c80408df529d68539892f2e220
  pageDirectory: concepts
  sources:
    - limitations-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scalar-udfs-on-dedicated-access-mode
    - SUODAM
  citations:
    - file: limitations-with-databricks-connect-for-scala-databricks-on-aws.md
title: Scalar UDFs on Dedicated Access Mode
description: Scalar UDFs are unavailable on compute resources using dedicated access mode (formerly single user) in Databricks Connect for Scala.
tags:
  - databricks-connect
  - udf
  - access-mode
  - limitations
timestamp: "2026-06-19T19:12:34.538Z"
---

# Scalar UDFs on Dedicated Access Mode

**Scalar UDFs on Dedicated Access Mode** refers to a known limitation in [Databricks Connect](/concepts/databricks-connect.md) for Scala when connecting to compute resources configured with dedicated access mode (formerly called single‑user mode). Under this configuration, scalar user‑defined functions (UDFs) are **not available** for use through Databricks Connect. ^[limitations-with-databricks-connect-for-scala-databricks-on-aws.md]

## Scope of the Limitation

This limitation applies to:

- Databricks Connect for **Scala** (not Python).
- Databricks Runtime **13.3 LTS and below**.
- Compute resources that use **dedicated access mode** (formerly single‑user mode).

The restriction means that any code or notebook using [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) that attempts to define or call a scalar UDF against a dedicated‑mode cluster will fail or produce an error. ^[limitations-with-databricks-connect-for-scala-databricks-on-aws.md]

## Workarounds

To work around this limitation, consider one of the following approaches:

1. **Switch to shared access mode** – If possible, configure the compute resource to use Shared Access Mode instead of dedicated access mode. Scalar UDFs may then be supported (depending on the Runtime version).
2. **Upgrade Databricks Runtime** – If the limitation is specifically tied to Runtime 13.3 LTS and below, upgrading to a newer Runtime version may resolve the issue. Check the [Databricks Connect](/concepts/databricks-connect.md) release notes for updated compatibility.
3. **Avoid scalar UDFs** – Rewrite logic to use built‑in Spark SQL functions or other transformations that do not require scalar UDFs.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library that enables remote connection to Databricks compute.
- Scalar UDF – A user‑defined function that operates on a single row and returns a single value.
- [Dedicated Access Mode](/concepts/dedicated-access-mode-for-ml-compute.md) – A cluster security mode that restricts access to a single user.
- Shared Access Mode – A cluster security mode that supports multiple users and broader UDF compatibility.
- [Limitations with Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) – The full list of restrictions for the Scala client.

## Sources

- limitations-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [limitations-with-databricks-connect-for-scala-databricks-on-aws.md](/references/limitations-with-databricks-connect-for-scala-databricks-on-aws-8e97ac24.md)
