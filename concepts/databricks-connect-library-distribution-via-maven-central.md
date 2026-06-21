---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a508e57d6c4ff3b277ef89cfcd76c3870d2f46411f59024d0251240c0c6ca7fd
  pageDirectory: concepts
  sources:
    - install-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-library-distribution-via-maven-central
    - DCLDVMC
  citations:
    - file: install-databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Connect library distribution via Maven Central
description: The Databricks Connect client library is distributed through Maven Central repository, with separate artifact coordinates for different Databricks Runtime versions.
tags:
  - databricks
  - maven
  - package-management
timestamp: "2026-06-19T19:10:13.644Z"
---

# Databricks Connect Library Distribution via Maven Central

**Databricks Connect library distribution via Maven Central** refers to the process of making the Databricks Connect client library available for Scala projects through the Maven Central Repository, enabling developers to add it as a dependency using standard build tools like `sbt`, Maven, or Gradle.

## Overview

The Databricks Connect client library is distributed through [Maven Central](https://central.sonatype.com/), the industry-standard repository for Java and Scala artifacts. This distribution method allows developers to integrate Databricks Connect into their local development environments by adding a simple dependency reference to their project build files. ^[install-databricks-connect-for-scala-databricks-on-aws.md]

## Version Availability

The library versions available on Maven Central correspond to specific Databricks Runtime versions. There are two distinct artifact coordinates depending on the Databricks Runtime version:

- For **Databricks Runtime 16.4 LTS and below**, the artifact is available at: `https://central.sonatype.com/artifact/com.databricks/databricks-connect/versions` ^[install-databricks-connect-for-scala-databricks-on-aws.md]
- For **Databricks Runtime 17.0 and above**, the artifact is available at: `https://central.sonatype.com/artifact/com.databricks/databricks-connect_2.13/versions` ^[install-databricks-connect-for-scala-databricks-on-aws.md]

## Build Tool Integration

### sbt

For sbt projects, add the following to your `build.sbt` file:

```scala
libraryDependencies += "com.databricks" % "databricks-connect" % "14.0.0"
```

For Databricks Connect 17.0 and above, use the Scala-versioned artifact:

```scala
libraryDependencies += "com.databricks" %% "databricks-connect" % "17.3.+"
```

^[install-databricks-connect-for-scala-databricks-on-aws.md]

### Maven

For Maven projects, add the dependency to your `pom.xml` file using the same group and artifact coordinates with the appropriate version matching your cluster's Databricks Runtime version. ^[install-databricks-connect-for-scala-databricks-on-aws.md]

### Gradle

For Gradle projects, add the dependency to your `build.gradle` file using Maven Central as a repository source. ^[install-databricks-connect-for-scala-databricks-on-aws.md]

## Version Compatibility

When selecting a version, replace the version number with the version of the Databricks Connect library that matches the Databricks Runtime version on your cluster. Using an incompatible version may cause connection or functionality issues. ^[install-databricks-connect-for-scala-databricks-on-aws.md]

## Requirements

Before installing Databricks Connect, ensure your workspace and local environment meet the [Databricks Connect usage requirements](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements). ^[install-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — The client library that enables local development against Databricks clusters
- Databricks Runtime — The runtime environment that determines which library version to use
- Maven Central Repository — The standard distribution platform for Java/Scala artifacts
- Databricks Cluster Configuration — How to configure compute resources for Databricks Connect

## Sources

- install-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [install-databricks-connect-for-scala-databricks-on-aws.md](/references/install-databricks-connect-for-scala-databricks-on-aws-9a592761.md)
