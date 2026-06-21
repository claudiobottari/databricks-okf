---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 69e584163ff0d343efdad958a43ceb474d6f54f30048040788501deb0462cc7c
  pageDirectory: concepts
  sources:
    - databricks-connect-for-python-databricks-on-aws.md
    - migrate-to-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-connect-migration
    - DCM
  citations:
    - file: migrate-to-databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Connect migration
description: Process for migrating from Databricks Connect for Databricks Runtime 12.2 LTS and below to Databricks Connect for Databricks Runtime 13.3 LTS and above.
tags:
  - databricks
  - migration
  - version-upgrade
timestamp: "2026-06-19T18:09:54.111Z"
---

# Databricks Connect migration

**Databricks Connect migration** describes the process of upgrading client-side applications from Databricks Connect for Databricks Runtime 12.2 LTS and below to Databricks Connect for Databricks Runtime 13.3 LTS and above. The migration instructions differ for Python and Scala clients. This page covers the Scala migration; the Python version is documented in a separate article. ^[migrate-to-databricks-connect-for-scala-databricks-on-aws.md]

Databricks Connect for Databricks Runtime 13.3 LTS and above for Scala is in Public Preview. Before beginning migration, you must complete the [Databricks Connect Client Setup](/concepts/databricks-connect-client-setup.md) for the new version. ^[migrate-to-databricks-connect-for-scala-databricks-on-aws.md]

## Prerequisites

Ensure that your local development environment has the correct versions of the Java Development Kit (JDK) and Scala as listed in the [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md). These must match the Databricks Runtime version running on your target cluster. ^[migrate-to-databricks-connect-for-scala-databricks-on-aws.md]

## Migrate your Scala project

1. **Update the build dependency** – In your project's build file (`build.sbt` for sbt, `pom.xml` for Maven, or `build.gradle` for Gradle), change the Databricks Connect artifact reference to the version that matches your target Databricks Runtime version. For example:

   ```scala
   libraryDependencies += "com.databricks" % "databricks-connect" % "14.0.0"
   ```

   Replace `14.0.0` with the correct version number. Available versions can be found in the Maven Central Repository (for Databricks Runtime 16.4 LTS and below) or the Maven Central Repository for Scala 2.13 (for Databricks Runtime 17.0 and above). ^[migrate-to-databricks-connect-for-scala-databricks-on-aws.md]

2. **Update the initialization code** – Modify your Scala code to initialize the `spark` variable as an instance of `DatabricksSession` (analogous to `SparkSession` in standard Spark). See the [code examples for Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) for the correct usage pattern. ^[migrate-to-databricks-connect-for-scala-databricks-on-aws.md]

## Python migration

This article does not cover the Python client migration. For the equivalent Python instructions, refer to [Migrate to Databricks Connect for Python](/concepts/databricks-connect-for-python.md).

## Related concepts

- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md)
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md)
- [Databricks Runtime 13.3 LTS](/concepts/databricks-runtime-133-lts.md)
- Public Preview
- [Databricks Connect Client Setup](/concepts/databricks-connect-client-setup.md)
- [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md)

## Sources

- migrate-to-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [migrate-to-databricks-connect-for-scala-databricks-on-aws.md](/references/migrate-to-databricks-connect-for-scala-databricks-on-aws-050a2949.md)
