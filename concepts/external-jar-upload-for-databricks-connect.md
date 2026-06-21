---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0c191b9d2d34f18183014068e773cbd8d1ca08833ddcd35fdd7ae49edf6ff750
  pageDirectory: concepts
  sources:
    - user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-jar-upload-for-databricks-connect
    - EJUFDC
  citations:
    - file: user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md
title: External JAR Upload for Databricks Connect
description: Uploading private or third-party JARs from local directories (e.g., a lib/ folder) to Databricks clusters using the addCompiledArtifacts() API to resolve ClassNotFoundException during UDF execution.
tags:
  - databricks-connect
  - scala
  - jar-management
  - udf
timestamp: "2026-06-19T23:24:39.114Z"
---

# External JAR Upload for [Databricks Connect](/concepts/databricks-connect.md)

**External JAR Upload for Databricks Connect** refers to the process of uploading compiled JAR files and third-party dependencies from a local development environment to a Databricks cluster when using [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md). This mechanism enables the execution of user-defined functions (UDFs) and typed dataset operations that depend on external libraries not already present on the cluster.

## Overview

When running Scala code locally with [Databricks Connect](/concepts/databricks-connect.md), compiled classes and JARs must be explicitly uploaded to the remote cluster for UDFs to execute correctly. The `addCompiledArtifacts()` API from `DatabricksSession.builder()` handles this upload, ensuring that all necessary classes are available on the cluster at runtime. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Uploading Compiled Classes and JARs

To upload compiled artifacts when creating a Spark session:

```scala
import com.databricks.connect.[[databrickssession|DatabricksSession]]
import org.apache.spark.sql.SparkSession

def getSession(): SparkSession = {
  if (sys.env.contains("DATABRICKS_RUNTIME_VERSION")) {
    // On a Databricks cluster — reuse the active session
    SparkSession.active
  } else {
    // Locally with [[databricks-connect|Databricks Connect]] — upload local JARs and classes
    [[databrickssession|DatabricksSession]]
      .builder()
      .addCompiledArtifacts(
        Main.getClass.getProtectionDomain.getCodeSource.getLocation.toURI
      )
      .getOrCreate()
  }
}
```

`Main.getClass.getProtectionDomain.getCodeSource.getLocation.toURI` points to the project's compiled output directory (e.g., `target/classes` or the built JAR). All compiled classes in that location are uploaded to Databricks, not just the `Main` class. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

### Adding Artifacts After Session Creation

When the Spark session is already initialized, further compiled classes and JARs can be uploaded using the `spark.addArtifact()` API. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## UDFs with Third-Party Dependencies

If a UDF uses a Maven dependency that is not available on the Databricks cluster, the `ClassNotFoundException` will occur during server-side execution. Use `spark.addArtifact()` with the `ivy://` scheme to download dependencies from Maven Central. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

### Process

1. Add the dependency to `build.sbt` with the `Provided` scope:
   ```scala
   libraryDependencies ++= Seq(
     "org.apache.commons" % "commons-text" % "1.10.0" % Provided,
     "oro" % "oro" % "2.0.8"  // Required for ivy:// to work
   )
   ```
   ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

2. After creating the session, add the artifact using the `addArtifact()` API:
   ```scala
   val spark = [[databrickssession|DatabricksSession]].builder()
     .addCompiledArtifacts(Main.getClass.getProtectionDomain.getCodeSource.getLocation.toURI)
     .getOrCreate()
   spark.addArtifact("ivy://org.apache.commons:commons-text:1.10.0")
   ```
   ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## External JAR Dependencies

For private or third-party libraries stored in a local `lib/` folder, upload all JARs when creating the session:

```scala
def getSession(): SparkSession = {
  if (sys.env.contains("DATABRICKS_RUNTIME_VERSION")) {
    SparkSession.active
  } else {
    val builder = [[databrickssession|DatabricksSession]].builder()
      .addCompiledArtifacts(
        Main.getClass.getProtectionDomain.getCodeSource.getLocation.toURI
      )
    val libFolder = new java.io.File("lib")
    builder.addCompiledArtifacts(libFolder.toURI)
    builder.getOrCreate()
  }
}
```

This automatically uploads all JARs in the `lib/` directory to Databricks when running locally. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Projects with Multiple Modules

In a multi-module SBT project, `getClass.getProtectionDomain.getCodeSource.getLocation.toURI` only returns the current module's location. If a UDF uses classes from other modules, `ClassNotFoundException` will occur. Use `getClass` from a class in each module to get their locations and upload them separately:

```scala
// In module-a/src/main/scala/Main.scala
import com.company.moduleb.DataProcessor  // From module-b

def getSession(): SparkSession = {
  if (sys.env.contains("DATABRICKS_RUNTIME_VERSION")) {
    SparkSession.active
  } else {
    val moduleALocation = Main.getClass
      .getProtectionDomain.getCodeSource.getLocation.toURI
    val moduleBLocation = DataProcessor.getClass
      .getProtectionDomain.getCodeSource.getLocation.toURI
    [[databrickssession|DatabricksSession]].builder()
      .addCompiledArtifacts(moduleALocation)  // Upload module-a
      .addCompiledArtifacts(moduleBLocation)  // Upload module-b
      .getOrCreate()
  }
}
```

^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Important Considerations

- **Transitive dependencies**: When uploading JARs, all transitive dependency JARs must be included. The APIs do not perform automatic detection of transitive dependencies. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]
- **Server-side vs. client-side**: Code must behave differently depending on where it runs. When deployed on a Databricks cluster, no upload is needed because classes are already available. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]
- **Typed Dataset APIs**: The `addCompiledArtifacts()` API also applies to typed dataset operations like `map()`, `filter()`, `mapPartitions()`, and aggregations. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- User-defined functions in Databricks Connect
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md)
- SparkSession with SPARK_REMOTE|SparkSession management
- [Ivy dependency resolution](/concepts/ivy-dependency-resolution-for-databricks-connect-udfs.md)
- Multi-module SBT projects

## Sources

- user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md](/references/user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws-38ccefae.md)
