---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 210f14611d3b542d77c8180d34d739ed2e7e17720b46427ddd572752931232c6
  pageDirectory: concepts
  sources:
    - migrate-to-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-public-preview
    - DCPP
  citations:
    - file: migrate-to-databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Connect public preview
description: The Public Preview status of Databricks Connect for Scala on Databricks Runtime 13.3 LTS and above.
tags:
  - databricks
  - release-notes
  - preview
timestamp: "2026-06-19T19:34:34.932Z"
---

## Databricks Connect Public Preview

**Databricks Connect Public Preview** refers to the publicly available, pre‑release version of the Databricks Connect client for Scala, introduced for Databricks Runtime 13.3 LTS and above. This client lets users connect popular IDEs, notebook servers, and custom applications to Databricks clusters, enabling remote code execution against a cluster’s Spark engine. The public preview status indicates that the feature is ready for early testing and feedback but may not yet be fully supported in production environments.^[migrate-to-databricks-connect-for-scala-databricks-on-aws.md]

### Overview

The public preview is specific to the Scala client library (`databricks-connect`) for Databricks Runtime 13.3 LTS and later. Users migrating from older versions (12.2 LTS and below) must update their project dependencies, JDK, and Scala versions, and adjust their `spark` variable initialization to use the `DatabricksSession` class. The migration guide provides step‑by‑step instructions for updating build files (e.g., `build.sbt`, `pom.xml`, `build.gradle`) and code.^[migrate-to-databricks-connect-for-scala-databricks-on-aws.md]

### Key Details

- **Scope**: Scala only. A separate migration guide exists for Python.
- **Supported Runtime**: Databricks Runtime 13.3 LTS and above.
- **Status**: Public Preview (not yet General Availability).
- **Library Coordinates**: `com.databricks:databricks-connect:<version>` where the version matches the cluster’s Databricks Runtime version. Versions up to 16.4 LTS are listed in the Maven Central repository for the `databricks-connect` artifact; for Runtime 17.0 and later, the artifact is `databricks-connect_2.13`.^[migrate-to-databricks-connect-for-scala-databricks-on-aws.md]

### Migration Steps

1. Install the correct JDK and Scala versions matching the cluster’s Databricks Runtime.
2. Update the build file to reference the new `databricks-connect` library version.
3. Update code to initialize the `spark` variable using `DatabricksSession` instead of earlier APIs.

For full examples, see the [Code examples for [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md)](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/examples).

### Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md)
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md)
- Databricks Runtime
- Scala client library
- [DatabricksSession](/concepts/databrickssession.md)

### Sources

- migrate-to-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [migrate-to-databricks-connect-for-scala-databricks-on-aws.md](/references/migrate-to-databricks-connect-for-scala-databricks-on-aws-050a2949.md)
