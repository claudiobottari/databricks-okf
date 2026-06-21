---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3208413fba0c84f4edfc5d1de0dadbcce63341ff3516f367a5c9ca42d3909daf
  pageDirectory: concepts
  sources:
    - install-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-for-scala-installation-methods
    - DCFSIM
  citations:
    - file: install-databricks-connect-for-scala-databricks-on-aws.md
      start: 1
      end: 3
    - file: install-databricks-connect-for-scala-databricks-on-aws.md
      start: 8
      end: 10
    - file: install-databricks-connect-for-scala-databricks-on-aws.md
      start: 13
      end: 15
    - file: install-databricks-connect-for-scala-databricks-on-aws.md
      start: 17
      end: 22
    - file: install-databricks-connect-for-scala-databricks-on-aws.md
      start: 24
      end: 33
    - file: install-databricks-connect-for-scala-databricks-on-aws.md
      start: 19
      end: 22
    - file: 24-28
    - file: install-databricks-connect-for-scala-databricks-on-aws.md
      start: 24
      end: 28
    - file: 30-33
    - file: install-databricks-connect-for-scala-databricks-on-aws.md
      start: 45
      end: 46
title: Databricks Connect for Scala installation methods
description: The procedures for adding Databricks Connect as a dependency in Scala projects using sbt, Maven, or Gradle build tools.
tags:
  - databricks
  - scala
  - installation
  - build-tools
timestamp: "2026-06-19T19:10:27.004Z"
---

# [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) installation methods

**Databricks Connect for Scala** allows you to connect your local Scala IDE, notebook server, or custom application to an Apache Spark cluster on Databricks. This page describes how to install the Databricks Connect client for Scala for Databricks Runtime 13.3 LTS and above. ^[install-databricks-connect-for-scala-databricks-on-aws.md:1-3]

## Requirements

Before installing Databricks Connect, ensure that your Databricks workspace and local development environment meet the required prerequisites. See [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md) for details. ^[install-databricks-connect-for-scala-databricks-on-aws.md:8-10]

## Install the Databricks Connect client

The installation consists of adding a reference to the Databricks Connect library in your Scala project’s build configuration. Three build tools are supported: `sbt`, Maven, and Gradle. ^[install-databricks-connect-for-scala-databricks-on-aws.md:13-15]

### Add a reference to the Databricks Connect client

In your project’s build file — `build.sbt` for sbt, `pom.xml` for Maven, or `build.gradle` for Gradle — add the following dependency. Replace the version number with the version of the Databricks Connect library that matches the Databricks Runtime version on your cluster. The correct version numbers can be found in the Maven central repository:

- For Databricks Runtime 16.4 LTS and below: [Maven Central](https://central.sonatype.com/artifact/com.databricks/databricks-connect/versions)
- For Databricks Runtime 17.0 and above: [Maven Central](https://central.sonatype.com/artifact/com.databricks/databricks-connect_2.13/versions)

^[install-databricks-connect-for-scala-databricks-on-aws.md:17-22]

#### sbt

For Databricks Runtime versions 16.4 LTS and below:

```scala
libraryDependencies += "com.databricks" % "databricks-connect" % "14.0.0"
```

For Databricks Runtime 17.0 and above:

```scala
libraryDependencies += "com.databricks" %% "databricks-connect" % "17.3.+"
```

^[install-databricks-connect-for-scala-databricks-on-aws.md:24-33]

#### Maven

The Maven coordinates for the artifact are `com.databricks:databricks-connect:VERSION` (for Databricks Runtime 16.4 LTS and below) or `com.databricks:databricks-connect_2.13:VERSION` (for Databricks Runtime 17.0 and above). Add the appropriate dependency to your `pom.xml`.

^[install-databricks-connect-for-scala-databricks-on-aws.md:19-22, 24-28]

#### Gradle

The Gradle dependency declaration follows the same artifact coordinates as Maven. Add the following to your `build.gradle` (for Databricks Runtime 16.4 LTS and below):

```groovy
implementation 'com.databricks:databricks-connect:14.0.0'
```

For Databricks Runtime 17.0 and above:

```groovy
implementation 'com.databricks:databricks-connect_2.13:17.3.+'
```

^[install-databricks-connect-for-scala-databricks-on-aws.md:24-28, 30-33]

## Next steps

After installing the Databricks Connect client, you must configure a connection to your Databricks workspace. See [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) for instructions. ^[install-databricks-connect-for-scala-databricks-on-aws.md:45-46]

## Related concepts

- [Databricks Connect](/concepts/databricks-connect.md) – Overview of the remote connectivity tool.
- [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md) – Detailed prerequisites.
- Databricks Runtime – The runtime version that determines the compatible Databricks Connect version.
- sbt (Scala Build Tool) – Alternative build tool details.
- Maven – Build lifecycle and dependency management.
- Gradle – Build tool featuring incremental builds.

## Sources

- install-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [install-databricks-connect-for-scala-databricks-on-aws.md:1-3](/references/install-databricks-connect-for-scala-databricks-on-aws-9a592761.md)
2. [install-databricks-connect-for-scala-databricks-on-aws.md:8-10](/references/install-databricks-connect-for-scala-databricks-on-aws-9a592761.md)
3. [install-databricks-connect-for-scala-databricks-on-aws.md:13-15](/references/install-databricks-connect-for-scala-databricks-on-aws-9a592761.md)
4. [install-databricks-connect-for-scala-databricks-on-aws.md:17-22](/references/install-databricks-connect-for-scala-databricks-on-aws-9a592761.md)
5. [install-databricks-connect-for-scala-databricks-on-aws.md:24-33](/references/install-databricks-connect-for-scala-databricks-on-aws-9a592761.md)
6. [install-databricks-connect-for-scala-databricks-on-aws.md:19-22](/references/install-databricks-connect-for-scala-databricks-on-aws-9a592761.md)
7. 24-28
8. [install-databricks-connect-for-scala-databricks-on-aws.md:24-28](/references/install-databricks-connect-for-scala-databricks-on-aws-9a592761.md)
9. 30-33
10. [install-databricks-connect-for-scala-databricks-on-aws.md:45-46](/references/install-databricks-connect-for-scala-databricks-on-aws-9a592761.md)
