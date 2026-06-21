---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4d98a6622d8a49a2f2d8e32b51d472708b60ec0603dc3ed25610588b813c892d
  pageDirectory: concepts
  sources:
    - user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-serverless-udf-limitations
    - DCSUL
  citations:
    - file: user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Connect Serverless UDF Limitations
description: UDF support on serverless compute always follows the initial corresponding minor release of Databricks Connect, with version compatibility defined in the official compatibility table.
tags:
  - databricks-connect
  - scala
  - udf
  - limitations
timestamp: "2026-06-19T23:24:00.288Z"
---

# [Databricks Connect](/concepts/databricks-connect.md) Serverless UDF Limitations

**Databricks Connect Serverless UDF Limitations** describes the version‑support constraints for running User‑Defined Functions (UDFs) with [Databricks Connect](/concepts/databricks-connect.md) on Serverless Compute. The limitations apply to both Scala and – by extrapolation from the cross‑referenced Python article – Python UDFs when using serverless compute targets.

## Version Compatibility Constraint

Support for UDFs on serverless compute follows the **initial corresponding minor release** of [Databricks Connect](/concepts/databricks-connect.md). This means that UDF functionality on serverless compute is tied to the very first minor version of [Databricks Connect](/concepts/databricks-connect.md) that introduced it; later minor versions within the same major release line may not automatically include serverless UDF support. Users must consult the official [Databricks Connect version compatibility table](/concepts/databricks-connect-version-compatibility.md) to confirm whether their specific Databricks Runtime version and serverless compute combination is supported. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

The limitation is documented in the “Limitations” section of the [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) user‑defined functions article. The same restrictions likely apply to Python UDFs on serverless compute, as the platform’s UDF documentation cross‑references the Python version of the article. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library that allows local code to execute on Databricks clusters.
- User-Defined Functions (UDFs) – Custom functions registered with Spark SQL.
- Serverless Compute – On‑demand compute that scales automatically without cluster management.
- [Databricks Connect Version Compatibility](/concepts/databricks-connect-version-compatibility.md) – Table that lists supported Databricks Runtime versions and compute types.
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) – The Scala API for [Databricks Connect](/concepts/databricks-connect.md).

## Sources

- user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md](/references/user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws-38ccefae.md)
