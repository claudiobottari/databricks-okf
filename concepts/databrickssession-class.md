---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2dad1831b22f7419d407a8e98887fe09aaefaf1562ae9db1b391a5756a3a6c1d
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databrickssession-class
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: DatabricksSession class
description: The class used to initialize authentication for Databricks Connect projects in Scala, which also determines authentication for the Databricks Utilities for Scala library.
tags:
  - databricks
  - scala
  - authentication
timestamp: "2026-06-19T09:55:13.388Z"
---

## [DatabricksSession](/concepts/databrickssession.md) class

The **DatabricksSession** class is a core authentication component used in [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) projects. When initializing a Databricks Connect client, the `DatabricksSession` class determines the authentication context for the [Databricks Utilities (DBUtils) for Scala](/concepts/databricks-utilities-for-scala-library.md) library. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

Authentication for the Databricks Utilities for Scala library is determined by initializing the `DatabricksSession` class in a Databricks Connect project for Scala. Without this initialization, the utilities library may not have the necessary credentials to interact with the Databricks workspace. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

The `DatabricksSession` class belongs to the broader [Databricks Connect](/concepts/databricks-connect.md) framework and is distinct from the utilities library itself (which is provided by `com.databricks/databricks-dbutils-scala_2.12`). [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) already declares a dependency on the Databricks Utilities library, but the session initialization step remains necessary to establish authentication. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library that enables connecting external IDEs and applications to Databricks clusters.
- [DBUtils](/concepts/dbutilsnotebookrun.md) – The Databricks Utilities object used for filesystem and secrets operations.
- Authentication on Databricks – How credentials are managed across SDKs and tools.
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) – The Scala-specific variant of the Databricks Connect client.

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
