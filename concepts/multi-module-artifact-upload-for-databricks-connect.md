---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a340dbc605e13115f3126011b1b9712dc0609e0f92cdb847d19fcb00bc931183
  pageDirectory: concepts
  sources:
    - user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-module-artifact-upload-for-databricks-connect
    - MAUFDC
    - Compiled Artifact Upload for Databricks Connect
  citations:
    - file: user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md
title: Multi-Module Artifact Upload for Databricks Connect
description: Strategy for handling UDFs in multi-module SBT projects where each module's classes must be uploaded separately using addCompiledArtifacts() with getClass references from each module.
tags:
  - databricks-connect
  - scala
  - multi-module
  - artifact-management
timestamp: "2026-06-19T23:23:50.043Z"
---

# Multi-Module Artifact Upload for [Databricks Connect](/concepts/databricks-connect.md)

**Multi-Module Artifact Upload for Databricks Connect** refers to the technique of uploading compiled class files and JARs from multiple modules of a multi-module project to a Databricks cluster when using [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md). This is necessary to ensure that user-defined functions (UDFs) and typed dataset operations can access classes defined in dependent modules at runtime.

## Problem Description

In a multi-module SBT project, the standard approach of using `getClass.getProtectionDomain.getCodeSource.getLocation.toURI` only returns the location of the current module's compiled output. If a UDF or typed Dataset API transformation uses classes from another module, the cluster will throw a `ClassNotFoundException` during execution because those classes were not uploaded. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

For example, consider a project with two modules:

```
my-project/
├── module-a/  (main application)
├── module-b/  (utilities — module-a depends on this)
```

If a UDF in `module-a` uses a class from `module-b`, only uploading `module-a`'s compiled artifacts will cause the UDF to fail on the remote cluster. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Solution: Separate Upload Per Module

To resolve this, you must obtain the compiled artifact location for each module using a class defined within that module, then upload each location using separate calls to `addCompiledArtifacts()`. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

The following Scala code demonstrates the correct approach:

```scala
// In module-a/src/main/scala/Main.scala
import com.company.moduleb.DataProcessor  // From module-b

def getSession(): SparkSession = {
  if (sys.env.contains("DATABRICKS_RUNTIME_VERSION")) {
    SparkSession.active
  } else {
    // Get location using a class FROM module-a
    val moduleALocation = Main.getClass
      .getProtectionDomain.getCodeSource.getLocation.toURI
    // Get location using a class FROM module-b
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

## Key Considerations

- The `addCompiledArtifacts()` API is called during session creation with `DatabricksSession.builder()`. After the session is already initialized, use `spark.addArtifact()` for further uploads. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]
- When uploading JARs, all transitive dependency JARs must be included for upload; the APIs do not perform automatic detection of transitive dependencies. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]
- For deployments running directly on a Databricks cluster (where `DATABRICKS_RUNTIME_VERSION` is set), no upload is needed because the classes are already present on the cluster. ^[user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — The development framework enabling local code execution against Databricks clusters
- User-defined functions in Databricks Connect for Scala — Overview of UDF execution in [Databricks Connect](/concepts/databricks-connect.md)
- Compiled Artifact Upload for Databricks Connect — General pattern for uploading compiled classes and JARs
- Third-Party Dependency Handling in Databricks Connect — How to manage external JAR and Maven dependencies

## Sources

- user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws.md](/references/user-defined-functions-in-databricks-connect-for-scala-databricks-on-aws-38ccefae.md)
