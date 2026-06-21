---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ca2dd5de8178452d4e430ce15b7f68f1b87744209ab7575dbf3f714628fd7472
  pageDirectory: concepts
  sources:
    - user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - typed-dataset-apis-in-databricks-connect
    - TDAIDC
    - Typed Dataset API limitations
  citations:
    - file: user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md
title: Typed Dataset APIs in Databricks Connect
description: Support for running typed transformations like map(), filter(), mapPartitions() and aggregations via Databricks Connect for Scala, requiring compiled artifacts to be uploaded to the remote cluster.
tags:
  - databricks-connect
  - scala
  - dataset-api
  - udf
timestamp: "2026-06-19T23:24:01.073Z"
---

# Typed Dataset APIs in [Databricks Connect](/concepts/databricks-connect.md)

**Typed Dataset APIs** in [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) provide a strongly-typed interface for running distributed data transformations — such as `map()`, `filter()`, `mapPartitions()`, and aggregations — on Apache Spark Datasets. They allow developers to write type-safe code against structured data while executing the workload on a remote Databricks cluster.

## How They Work

Typed Dataset APIs operate on `Dataset[T]` objects, where `T` is a Scala case class or a built-in type (such as `Long`, `String`, or a custom domain object). Because the function logic (for example, the body of a `map()` block) runs on the remote worker nodes, the compiled `.class` files and any associated JARs must be available on the cluster’s classpath at runtime. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

When you use [Databricks Connect](/concepts/databricks-connect.md) from a local development environment, the cluster does **not** automatically have your local project’s compiled classes. You must explicitly upload them. If the same code is later deployed directly on a Databricks cluster (where you are already inside a running Databricks Runtime), no upload is needed because the classes are already present on the cluster. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Uploading Compiled Classes and JARs

For typed Dataset APIs to work, you must call `addCompiledArtifacts()` during session creation. This tells the [DatabricksSession](/concepts/databrickssession.md) builder which local artifacts to ship to the remote cluster. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

The following example uses `map()` to turn a numeric row into a prefixed string:

```scala
import com.databricks.connect.[[databrickssession|DatabricksSession]]
import org.apache.spark.sql.SparkSession

object Main {
  def main(args: Array[String]): Unit = {
    val sourceLocation = getClass.getProtectionDomain.getCodeSource.getLocation.toURI
    val spark = [[databrickssession|DatabricksSession]].builder()
      .addCompiledArtifacts(sourceLocation)
      .getOrCreate()

    spark.range(3).map(f => s"row-$f").show()
  }
}
```

^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Classpath and Transitive Dependencies

When uploading JARs, all transitive dependency JARs must be included for upload. The APIs do not perform any automatic detection of transitive dependencies. If a UDF or typed Dataset transformation uses a library from an external Maven dependency (for example, `org.apache.commons:commons-text:1.10.0`) that is not already on the cluster, use `spark.addArtifact()` with an `ivy://` URL to fetch that dependency from Maven. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

Example: adding a Maven dependency at runtime after the session is created:

```scala
val spark = [[databrickssession|DatabricksSession]].builder()
  .addCompiledArtifacts(Main.getClass.getProtectionDomain.getCodeSource.getLocation.toURI)
  .getOrCreate()

spark.addArtifact("ivy://org.apache.commons:commons-text:1.10.0")
```

^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Multi-Module Projects

In a multi-module SBT project, `getClass.getProtectionDomain.getCodeSource.getLocation.toURI` only returns the location of the class you called it on. If your typed Dataset transformation uses classes from another module, you must upload each module’s location separately by calling `addCompiledArtifacts()` for each module’s compiled output. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

Example: uploading both `module-a` and `module-b`:

```scala
val moduleALocation = Main.getClass
  .getProtectionDomain.getCodeSource.getLocation.toURI
val moduleBLocation = DataProcessor.getClass
  .getProtectionDomain.getCodeSource.getLocation.toURI

[[databrickssession|DatabricksSession]].builder()
  .addCompiledArtifacts(moduleALocation)   // Upload module-a
  .addCompiledArtifacts(moduleBLocation)   // Upload module-b
  .getOrCreate()
```

^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [User-defined functions (UDFs) in Databricks Connect](/concepts/udf-execution-in-databricks-connect.md) — The broader mechanism for running custom code on remote clusters.
- [DatabricksSession](/concepts/databrickssession.md) — The session builder that manages artifact upload.
- External JAR dependencies — Handling private or third-party libraries not on the cluster.
- [Typed Dataset API limitations](/concepts/typed-dataset-apis-in-databricks-connect.md) — Version compatibility and serverless compute restrictions.

## Sources

- user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md](/references/user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws-38ccefae.md)
