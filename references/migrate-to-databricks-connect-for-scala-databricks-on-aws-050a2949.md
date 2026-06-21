---
title: Migrate to Databricks Connect for Scala | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/migrate
ingestedAt: "2026-06-18T08:06:47.844Z"
---

note

Databricks Connect for Databricks Runtime 13.3 LTS and above for Scala is in [Public Preview](https://docs.databricks.com/aws/en/release-notes/release-types).

This article describes how to migrate from Databricks Connect for Databricks Runtime 12.2 LTS and below to Databricks Connect for Databricks Runtime 13.3 LTS and above for Scala. Databricks Connect enables you to connect popular IDEs, notebook servers, and custom applications to Databricks clusters. See [Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/).

Before you begin to use Databricks Connect, you must [set up the Databricks Connect client](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/install).

For the Python version of this article, see [Migrate to Databricks Connect for Python](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/migrate).

## Migrate your Scala project[​](#migrate-your-scala-project "Direct link to Migrate your Scala project")

1.  Install the correct version of the Java Development Kit (JDK) and Scala as listed in the [installation requirements](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements#versions) to match your Databricks cluster, if it is not already installed locally.
    
2.  In your Scala project's build file such as `build.sbt` for `sbt`, `pom.xml` for Maven, or `build.gradle` for Gradle, update the following reference to the Databricks Connect client:
    
    *   Sbt
    *   Maven
    *   Gradle
    
        libraryDependencies += "com.databricks" % "databricks-connect" % "14.0.0"
    
    Replace `14.0.0` with the version of the Databricks Connect library that matches the Databricks Runtime version on your cluster. You can find the Databricks Connect library version numbers in the [Maven central repository (for Databricks Runtime 16.4 LTS and below)](https://central.sonatype.com/artifact/com.databricks/databricks-connect/versions) or the [Maven central repository (for Databricks Runtime 17.0 and above)](https://central.sonatype.com/artifact/com.databricks/databricks-connect_2.13/versions).
    
3.  Update your Scala code to initialize the `spark` variable (which represents an instantiation of the `DatabricksSession` class, similar to `SparkSession` in Spark). For code examples, see [Code examples for Databricks Connect for Scala](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/examples).
