---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f2593c75489b86950567a72e747b50264bbb6cb8ef7e19d3f3240063877d5644
  pageDirectory: concepts
  sources:
    - troubleshooting-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-for-scala
    - DCFS
    - Databricks Connect for Scala Setup
    - Install Databricks Connect for Scala
    - Migrate to Databricks Connect for Scala
    - Databricks SDK for Scala
    - Installing Databricks Connect for Scala
    - Limitations with Databricks Connect for Scala
    - Troubleshooting Databricks Connect for Scala
    - code examples for Databricks Connect for Scala
  citations:
    - file: databricks-connect-for-scala-databricks-on-aws.md
    - file: install-databricks-connect-for-scala-databricks-on-aws.md
    - file: tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md
    - file: code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
    - file: limitations-with-databricks-connect-for-scala-databricks-on-aws.md
    - file: tutorial-run-scala-code-on-serverless-compute-databricks-on-aws.md
    - file: testing-for-databricks-connect-for-scala-databricks-on-aws.md
    - file: troubleshooting-databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Connect for Scala
description: A tool for connecting Scala IDEs, notebook servers, and custom applications to Databricks clusters, introduced for Databricks Runtime 13.3 LTS and above.
tags:
  - databricks
  - dev-tools
  - scala
timestamp: "2026-06-19T23:14:56.572Z"
---

```yaml
---
title: [[databricks-connect|Databricks Connect]] for Scala
summary: A client library that enables connecting Scala IDEs, notebook servers, and custom applications to Databricks clusters
sources:
  - code-examples-for-databricks-connect-for-scala-databricks-on-aws.md
  - databricks-connect-for-scala-databricks-on-aws.md
  - install-databricks-connect-for-scala-databricks-on-aws.md
  - limitations-with-databricks-connect-for-scala-databricks-on-aws.md
  - testing-for-databricks-connect-for-scala-databricks-on-aws.md
  - troubleshooting-databricks-connect-for-scala-databricks-on-aws.md
  - tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md
  - tutorial-run-scala-code-on-serverless-compute-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:59:23.835Z"
updatedAt: "2026-06-19T17:45:48.607Z"
tags:
  - databricks
  - scala
  - client-library
aliases:
  - databricks-connect-for-scala
  - DCFS
confidence: 0.95
provenanceState: merged
inferredParagraphs: 2
---

# [[databricks-connect|Databricks Connect]] for Scala

**Databricks Connect for Scala** is a client library that enables connecting popular IDEs such as IntelliJ IDEA, notebook servers, and custom applications to Databricks clusters from a local Scala development environment. It allows you to run Spark code locally that executes remotely on a Databricks cluster, combining the flexibility of local development with the power of Databricks compute.^[databricks-connect-for-scala-databricks-on-aws.md]

## Overview

[[databricks-connect|Databricks Connect]] for Scala is available for [[databricks-runtime-133-lts|Databricks Runtime 13.3 LTS]] and above. It works by establishing a [[Spark Connect]] session between your local client and a remote cluster, so that DataFrame operations and Spark SQL queries run on the cluster while your code is edited and managed locally.^[databricks-connect-for-scala-databricks-on-aws.md]

## Getting Started

### Requirements

Before installing, ensure your workspace and local environment meet the requirements detailed in the [[Databricks Connect usage requirements]] documentation, including compatible versions of Scala, Java, and Databricks Runtime.^[databricks-connect-for-scala-databricks-on-aws.md]^[install-databricks-connect-for-scala-databricks-on-aws.md]

### Installation

To install the [[databricks-connect|Databricks Connect]] client, add a dependency to your Scala project’s build file. For Databricks Runtime 16.4 LTS and below, use the following in `build.sbt`:^[install-databricks-connect-for-scala-databricks-on-aws.md]

```scala
libraryDependencies += "com.databricks" % "databricks-connect" % "14.0.0"
```

For Databricks Runtime 17.0 and above:^[install-databricks-connect-for-scala-databricks-on-aws.md]

```scala
libraryDependencies += "com.databricks" %% "databricks-connect" % "17.3.+"
```

Replace the version number with the version of the [[databricks-connect|Databricks Connect]] library that matches the Databricks Runtime version on your cluster. You can find the [[databricks-connect|Databricks Connect]] library version numbers in the [Maven central repository](https://central.sonatype.com/artifact/com.databricks/databricks-connect/versions).^[install-databricks-connect-for-scala-databricks-on-aws.md]

When building with [[databricks-connect|Databricks Connect]], do not include Apache Spark artifacts such as `org.apache.spark:spark-core` in your project. Instead, compile directly against [[databricks-connect|Databricks Connect]].^[tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md]

## Authentication

[[databricks-connect|Databricks Connect]] for Scala supports multiple authentication methods, including [[User-to-Machine (U2M) Authentication|OAuth user-to-machine (U2M) authentication]] via the Databricks CLI, [[Databricks Configuration Profiles|configuration profiles]], and environment variables. The recommended approach is to use the Databricks CLI to configure OAuth U2M authentication:^[tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md]

```bash
databricks auth login --configure-cluster --host <workspace-url>
```

This creates a configuration profile that [[databricks-connect|Databricks Connect]] can use to authenticate with your workspace.^[tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md]

## Creating a Spark Session

Use `DatabricksSession` to create a Spark session that connects to your remote cluster:^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
import com.databricks.connect.[DatabricksSession](/concepts/databrickssession.md)
import org.apache.spark.sql.SparkSession

val spark = [DatabricksSession](/concepts/databrickssession.md).builder().getOrCreate()
```

For non-default configuration profiles, specify the profile name:^[tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md]

```scala
val config = new DatabricksConfig().setProfile("<profile-name>")
val spark = [DatabricksSession](/concepts/databrickssession.md).builder().sdkConfig(config).getOrCreate()
```

## Core Operations

### Reading Tables

Query a table and display results:^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
val df = spark.read.table("samples.nyctaxi.trips")
df.limit(5).show()
```

### Creating DataFrames and Writing Tables

Create an in-memory DataFrame and save it as a table:^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
val schema = StructType(Seq(
  StructField("AirportCode", StringType, false),
  StructField("Date", DateType, false),
  StructField("TempHighF", IntegerType, false),
  StructField("TempLowF", IntegerType, false)
))

val data = Seq(
  ("BLI", LocalDate.of(2021, 4, 3), 52, 43),
  ("PDX", LocalDate.of(2021, 4, 3), 64, 45),
  ("SEA", LocalDate.of(2021, 4, 3), 57, 43)
)

val temps = spark.createDataFrame(data).toDF(schema.fieldNames: _*)
spark.sql("DROP TABLE IF EXISTS zzz_demo_temps_table")
temps.write.saveAsTable("zzz_demo_temps_table")
```

Note that `CREATE TABLE <table-name> AS SELECT` is not available; instead, use `spark.sql("SELECT ...").write.saveAsTable("table")`.^[limitations-with-databricks-connect-for-scala-databricks-on-aws.md]

### Running SQL Queries

Execute SQL queries directly on the remote cluster:^[code-examples-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
val df_temps = spark.sql("SELECT * FROM zzz_demo_temps_table " +
  "WHERE AirportCode != 'BLI' AND Date > '2021-04-01' " +
  "GROUP BY AirportCode, Date, TempHighF, TempLowF " +
  "ORDER BY TempHighF DESC")
df_temps.show()
```

## Building JARs for Serverless Compute

[[databricks-connect|Databricks Connect]] can be used to build Scala JAR files compatible with [[Unity Catalog]]-enabled compute and [[Serverless GPU Compute|serverless compute]]. Configure your `build.sbt` with compatible versions:^[tutorial-run-scala-code-on-serverless-compute-databricks-on-aws.md]

```scala
scalaVersion := "2.13.16"
libraryDependencies += "com.databricks" %% "databricks-connect" % "17.3.+"
fork := true
javaOptions += "--add-opens=java.base/java.nio=ALL-UNNAMED"
```

When building for serverless compute, use `validateSession(false)` and `addCompiledArtifacts()` in your session creation:^[tutorial-run-scala-code-on-serverless-compute-databricks-on-aws.md]

```scala
val spark: SparkSession = [DatabricksSession](/concepts/databrickssession.md).builder()
  .validateSession(false)
  .addCompiledArtifacts(SparkJar.getClass.getProtectionDomain.getCodeSource.getLocation.toURI)
  .getOrCreate()
```

## Testing with ScalaTest

[[databricks-connect|Databricks Connect]] for Scala can be used with ScalaTest for local testing. The following example shows a test that verifies a `SparkSession` is returned and that a DataFrame contains at least one row:^[testing-for-databricks-connect-for-scala-databricks-on-aws.md]

```scala
// In src/test/scala/NYCTaxiFunctionsTest.scala
package org.example.application

import org.apache.spark.sql.SparkSession
import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers

class SparkSessionTypeTest extends AnyFlatSpec with Matchers {
  "The session" should "be of type SparkSession" in {
    val nycTaxiFunctions = new NYCTaxiFunctions()
    val spark = nycTaxiFunctions.getSpark
    spark shouldBe a [SparkSession]
  }
}

class GetTaxisRowCountTest extends AnyFlatSpec with Matchers {
  "The DataFrame" should "have at least one row" in {
    val nycTaxiFunctions = new NYCTaxiFunctions()
    val df = nycTaxiFunctions.getTaxis
    df.count() should be > (0L)
  }
}
```

The `NYCTaxiFunctions` class must instantiate `DatabricksSession` to connect to the remote cluster.^[testing-for-databricks-connect-for-scala-databricks-on-aws.md]

## Limitations

The following features are **not available** on [Databricks Connect](/concepts/databricks-connect.md) for [Databricks Runtime 13.3 LTS](/concepts/databricks-runtime-133-lts.md) and below:

- Streaming `foreachBatch`
- Creating DataFrames with an unresolved logical plan larger than 128 MB
- Long queries over 3600 seconds
- Scalar UDFs on compute resources that use dedicated access mode

The following features are **not available** on any version:

- Databricks Utilities: `credentials`, `library`, `notebook workflow`, `widgets`
- RDDs and Spark Context
- `CREATE TABLE <table-name> AS SELECT`
- Changing the `log4j` log level through `SparkContext`
- Distributed ML training
- Synchronizing the local development environment with the remote compute resource

^[limitations-with-databricks-connect-for-scala-databricks-on-aws.md]

## Troubleshooting

The following issues and solutions apply to [Databricks Connect](/concepts/databricks-connect.md) for [Databricks Runtime 13.3 LTS](/concepts/databricks-runtime-133-lts.md) and above.^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

### Connection Failures

**Issue**: When you try to run code with [Databricks Connect](/concepts/databricks-connect.md), you get error messages containing strings such as `StatusCode.UNAVAILABLE`, `StatusCode.UNKNOWN`, `DNS resolution failed`, or `Received http2 header with status: 500`.

**Cause**: [Databricks Connect](/concepts/databricks-connect.md) cannot reach your cluster.^[troubleshooting-databricks-connect-for-scala-databricks-on-aws.md]

**Solutions**:^[troubleshooting-databricks-connect-for-scala

# Citations

1. [databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-connect-for-scala-databricks-on-aws-9156fcdc.md)
2. [install-databricks-connect-for-scala-databricks-on-aws.md](/references/install-databricks-connect-for-scala-databricks-on-aws-9a592761.md)
3. [tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md](/references/tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws-da20890c.md)
4. [code-examples-for-databricks-connect-for-scala-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-scala-databricks-on-aws-383843cd.md)
5. [limitations-with-databricks-connect-for-scala-databricks-on-aws.md](/references/limitations-with-databricks-connect-for-scala-databricks-on-aws-8e97ac24.md)
6. [tutorial-run-scala-code-on-serverless-compute-databricks-on-aws.md](/references/tutorial-run-scala-code-on-serverless-compute-databricks-on-aws-c23f2a4d.md)
7. [testing-for-databricks-connect-for-scala-databricks-on-aws.md](/references/testing-for-databricks-connect-for-scala-databricks-on-aws-dea6ce36.md)
8. [troubleshooting-databricks-connect-for-scala-databricks-on-aws.md](/references/troubleshooting-databricks-connect-for-scala-databricks-on-aws-fde9e272.md)
