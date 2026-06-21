---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 880a84bcc570cb2019641f1691791e1153a6143865b3a8f824feb5fe26f3c0f7
  pageDirectory: concepts
  sources:
    - user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - addcompiledartifacts-api
    - addCompiledArtifacts
  citations:
    - file: user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md
title: addCompiledArtifacts API
description: API in Databricks Connect for Scala that uploads compiled classes and JARs from local development to a remote Databricks cluster so that UDFs and typed Dataset operations can execute on the server side.
tags:
  - databricks-connect
  - scala
  - udf
  - artifact-management
timestamp: "2026-06-19T23:23:58.110Z"
---

# addCompiledArtifacts API

The **`addCompiledArtifacts()` API** is a method on the `DatabricksSession.Builder` class used in [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) to upload compiled classes and JARs from a local development environment to a remote Databricks cluster. This upload is required for user-defined functions (UDFs) and typed Dataset APIs to execute correctly on the cluster side. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Purpose

When running Scala code locally with [Databricks Connect](/concepts/databricks-connect.md), UDFs and typed Dataset operations (such as `map()`, `filter()`, and `mapPartitions()`) need access to compiled bytecode on the remote cluster. The `addCompiledArtifacts()` API uploads the necessary classes and JARs so the cluster can deserialize and execute the user code. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Usage

The API is called during session creation on the `DatabricksSession.builder()`. When running on a Databricks cluster directly (not through [Databricks Connect](/concepts/databricks-connect.md)), the upload is unnecessary because the classes are already available. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

### Basic Example

The following pattern shows how to conditionally use `addCompiledArtifacts()` only when running locally with [Databricks Connect](/concepts/databricks-connect.md):

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

^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

### Parameter

The method accepts a `java.net.URI` pointing to the compiled output location. This is typically obtained via `getClass.getProtectionDomain.getCodeSource.getLocation.toURI`, which resolves to the project's compiled output directory (for example, `target/classes` or the built JAR location). All compiled classes under that location are uploaded to Databricks, not just the calling class. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Multiple Calls

`addCompiledArtifacts()` can be called multiple times on the same builder to upload artifacts from different locations. This is particularly useful for:

- **Multi-module projects**: Each module's compiled output must be uploaded separately using a class from that module to obtain its location. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]
- **External JAR dependencies**: All JARs from a `lib/` directory can be uploaded by passing the directory URI to a separate call. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

### Multi-Module Example

```scala
// In module-a, which depends on module-b
val moduleALocation = Main.getClass
  .getProtectionDomain.getCodeSource.getLocation.toURI
val moduleBLocation = DataProcessor.getClass
  .getProtectionDomain.getCodeSource.getLocation.toURI

[[databrickssession|DatabricksSession]].builder()
  .addCompiledArtifacts(moduleALocation)  // Upload module-a
  .addCompiledArtifacts(moduleBLocation)  // Upload module-b
  .getOrCreate()
```

^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

### External JARs Example

```scala
val builder = [[databrickssession|DatabricksSession]].builder()
  .addCompiledArtifacts(Main.getClass.getProtectionDomain.getCodeSource.getLocation.toURI)

// Add all JARs from lib/ folder
val libFolder = new java.io.File("lib")
builder.addCompiledArtifacts(libFolder.toURI)
builder.getOrCreate()
```

^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Related Methods

After the session is created, additional artifacts can be uploaded using the `spark.addArtifact()` API. This is used, for example, to resolve third-party Maven dependencies via `ivy://` URIs that are not available on the cluster but are needed for UDF execution. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Limitations

- When uploading JARs, all transitive dependency JARs must be included for upload. The APIs do not perform any automatic detection of transitive dependencies. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]
- UDF support on serverless compute always follows the initial corresponding minor release of [Databricks Connect](/concepts/databricks-connect.md). ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — The development tool that enables local-to-cluster execution
- [User-defined functions (UDFs) in Databricks Connect](/concepts/udf-execution-in-databricks-connect.md) — Overview of UDF support in [Databricks Connect](/concepts/databricks-connect.md)
- [DatabricksSession](/concepts/databrickssession.md) — The session builder class that provides `addCompiledArtifacts()`
- spark.addArtifact() — The runtime API for adding additional artifacts after session creation

## Sources

- user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md](/references/user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws-38ccefae.md)
