---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5d3b69a40d5ecb6f8d0895317d9330ddc39d544175c5d3dd61b5bab911036037
  pageDirectory: concepts
  sources:
    - migrate-to-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-build-file-configuration
    - DCBFC
  citations:
    - file: migrate-to-databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Connect build file configuration
description: How to configure build.sbt, pom.xml, or build.gradle to add the Databricks Connect library dependency matching the target Databricks Runtime version.
tags:
  - databricks
  - build-tools
  - scala
  - configuration
timestamp: "2026-06-19T19:34:28.665Z"
---

# Databricks Connect Build File Configuration

**Databricks Connect build file configuration** refers to the steps needed to add the Databricks Connect library as a dependency in a Scala project’s build system (sbt, Maven, or Gradle). This configuration allows the project to connect to a Databricks cluster from a local IDE, notebook server, or custom application. ^[migrate-to-databricks-connect-for-scala-databricks-on-aws.md]

## Overview

[Databricks Connect](/concepts/databricks-connect.md) enables you to use familiar development tools while running Spark code on a remote Databricks cluster. For Scala projects, the client is distributed as a JAR artifact on Maven Central. To use it, you must declare a dependency on the `databricks-connect` artifact in your project’s build file. The version of the artifact must match the Databricks Runtime version running on the target cluster. ^[migrate-to-databricks-connect-for-scala-databricks-on-aws.md]

## Build File Configuration

The exact syntax depends on your build tool. After updating the dependency, your project will have access to the `DatabricksSession` class (the Scala equivalent of `SparkSession`).

### sbt (build.sbt)

```scala
libraryDependencies += "com.databricks" % "databricks-connect" % "14.0.0"
```

Replace `14.0.0` with the version matching your cluster’s Databricks Runtime version. ^[migrate-to-databricks-connect-for-scala-databricks-on-aws.md]

### Maven (pom.xml)

Add the following inside the `<dependencies>` section:

```xml
<dependency>
    <groupId>com.databricks</groupId>
    <artifactId>databricks-connect</artifactId>
    <version>14.0.0</version>
</dependency>
```

Again, adjust the version to match the target Databricks Runtime. ^[migrate-to-databricks-connect-for-scala-databricks-on-aws.md]

### Gradle (build.gradle)

```groovy
implementation 'com.databricks:databricks-connect:14.0.0'
```

Set the version appropriately. ^[migrate-to-databricks-connect-for-scala-databricks-on-aws.md]

## Version Selection

The version number corresponds to a specific Databricks Runtime release. For example, `14.0.0` maps to Databricks Runtime 14.0. You can find all available versions in the Maven Central Repository:

- For Databricks Runtime 16.4 LTS and below: [Maven central repository for `databricks-connect`](https://central.sonatype.com/artifact/com.databricks/databricks-connect/versions)
- For Databricks Runtime 17.0 and above: [Maven central repository for `databricks-connect_2.13`](https://central.sonatype.com/artifact/com.databricks/databricks-connect_2.13/versions)

^[migrate-to-databricks-connect-for-scala-databricks-on-aws.md]

## Prerequisites

Before configuring the build file, ensure that the local development environment has the correct versions of the Java Development Kit (JDK) and Scala as listed in the [Databricks Connect Requirements](/concepts/databricks-connect-requirements.md). ^[migrate-to-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md)
- Databricks Runtime
- [DatabricksSession](/concepts/databrickssession.md)
- Scala
- sbt
- Maven
- Gradle
- [Installing Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md)

## Sources

- migrate-to-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [migrate-to-databricks-connect-for-scala-databricks-on-aws.md](/references/migrate-to-databricks-connect-for-scala-databricks-on-aws-050a2949.md)
