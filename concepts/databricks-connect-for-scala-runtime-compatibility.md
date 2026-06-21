---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7a83dcc178b1dd469530e7da9fc5ffbac8f4eaa9599e5b2bf13d5109309881bb
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-for-scala-runtime-compatibility
    - DCFSRC
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Connect for Scala Runtime Compatibility
description: The described Databricks Utilities integration works with Databricks Connect for Databricks Runtime 13.3 LTS and above.
tags:
  - databricks
  - scala
  - compatibility
  - runtime
timestamp: "2026-06-18T15:10:30.990Z"
---

# [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) Runtime Compatibility

**Databricks Connect for Scala Runtime Compatibility** refers to the supported Databricks Runtime versions and library dependencies required to use Databricks Connect with Scala projects. Databricks Connect enables you to connect popular IDEs, notebook servers, and custom applications to Databricks clusters. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Supported Runtime Versions

[Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) is supported on Databricks Runtime 13.3 LTS and above. Earlier runtime versions are not compatible with the Databricks Connect client for Scala. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Library Dependencies

### Databricks Utilities for Scala Library

[Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) already declares a dependency on the [Databricks Utilities for Scala](/concepts/databricks-utilities-for-scala-library.md) library (`com.databricks/databricks-dbutils-scala_2.12`). You do not need to explicitly declare this dependency in your Scala project's build file — whether using `build.sbt` for sbt, `pom.xml` for Maven, or `build.gradle` for Gradle. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

### Authentication

Authentication for the Databricks Utilities for Scala library is determined through initializing the `DatabricksSession` class in your Databricks Connect project for Scala. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Available Functionality

When using [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md), you can access Databricks Utilities through `DBUtils.getDBUtils`, which belongs to the Databricks Utilities for Scala library. This provides access to:

- Databricks File System (DBFS) operations
- Secrets utility (`dbutils.secrets`)

No Databricks Utilities functionality other than DBFS and secrets is available for Scala projects through Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that enables remote connection to Databricks clusters
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — The Python equivalent of this functionality
- Databricks Utilities — The broader set of utilities available in Databricks notebooks
- [Databricks Runtime 13.3 LTS](/concepts/databricks-runtime-133-lts.md) — The minimum supported runtime version

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
