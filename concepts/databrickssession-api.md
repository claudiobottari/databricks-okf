---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6ef391ea5431e5f8d52c9ac2724a9a09f0be07a272d6a656084dbc3035a993d9
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-python-databricks-on-aws.md
    - tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databrickssession-api
    - Databricks Serving API
    - Databricks APIs
  citations:
    - file: code-examples-for-databricks-connect-for-python-databricks-on-aws.md
    - file: tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md
title: DatabricksSession API
description: The primary entry-point class in Databricks Connect that creates a SparkSession bound to a remote Databricks cluster.
tags:
  - api
  - python
  - databricks
timestamp: "2026-06-19T14:13:38.336Z"
---

---

title: [DatabricksSession](/concepts/databrickssession.md) API  
summary: The [DatabricksSession](/concepts/databrickssession.md) API provides a SparkSession-like entry point for using Databricks Connect from Python and Scala.  
sources:  
  - code-examples-for-databricks-connect-for-python-databricks-on-aws.md  
  - tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md  
kind: api  
createdAt: "2026-06-18T08:06:16.367Z"  
updatedAt: "2026-06-18T08:06:53.791Z"  
tags:  
  - databricks-connect  
  - spark  
  - api  
  - python  
  - scala  
aliases:  
  - databrickssession-api  
  - 5DA  
confidence: 0.95  
provenanceState: extracted  
inferredParagraphs: 0  

---

# [DatabricksSession](/concepts/databrickssession.md) API

The **DatabricksSession API** is the primary entry point for using [Databricks Connect](/concepts/databricks-connect.md) from Python and Scala. It provides a `SparkSession`-like interface that connects a local development environment (IDE, notebook server, or custom application) to a remote Databricks cluster, allowing you to run Spark code locally against data and compute in your Databricks workspace.^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]^[tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md]

## Creating a [DatabricksSession](/concepts/databrickssession.md)

### Python

In Python, import `DatabricksSession` from the `databricks.connect` package and use the builder to obtain a session:

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

`getOrCreate()` returns an existing session if one is already active, or creates a new one using the default authentication settings.^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

### Scala

In Scala, the builder methods are slightly different. Use `.builder().remote().getOrCreate()` to connect with the default authentication (for example, the `DEFAULT` configuration profile):

```scala
import com.databricks.connect.[[databrickssession|DatabricksSession]]

val spark = [[databrickssession|DatabricksSession]].builder().remote().getOrCreate()
```

To use a specific [Databricks configuration profile](/concepts/databricks-configuration-profiles.md), pass a `DatabricksConfig` object with the profile name:

```scala
import com.databricks.connect.[[databrickssession|DatabricksSession]]
import com.databricks.sdk.core.DatabricksConfig

val config = new DatabricksConfig().setProfile("<profile-name>")
val spark = [[databrickssession|DatabricksSession]].builder().sdkConfig(config).getOrCreate()
```

^[tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md]

## Authentication

[DatabricksSession](/concepts/databrickssession.md) supports the same authentication methods as the Databricks SDK for Python and Databricks SDK for Java/Scala. The recommended approach for development is [OAuth user-to-machine (U2M) authentication](/concepts/user-to-machine-u2m-authentication.md), which is configured using the Databricks CLI:

```
databricks auth login --configure-cluster --host <workspace-url>
```

The CLI prompts you to save the authentication details as a named configuration profile. The session can then be created using that profile (as shown in the Scala example above).^[tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md]

Alternatively, authentication can be configured through environment variables (such as `SPARK_REMOTE`) or other standard Databricks authentication mechanisms.^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Code Examples

### Python: Read a table and show results

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
df = spark.read.table("samples.nyctaxi.trips")
df.show(5)
```

^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

### Python: Portable pattern (fallback to SparkSession)

The following pattern allows code to work both with and without Databricks Connect installed. It attempts to use `DatabricksSession` and falls back to a standard `SparkSession` if the import fails:

```python
from pyspark.sql import SparkSession, DataFrame

def get_spark() -> SparkSession:
    try:
        from databricks.connect import [[databrickssession|DatabricksSession]]
        return [[databrickssession|DatabricksSession]].builder.getOrCreate()
    except ImportError:
        return SparkSession.builder.getOrCreate()

def get_taxis(spark: SparkSession) -> DataFrame:
    return spark.read.table("samples.nyctaxi.trips")

get_taxis(get_spark()).show(5)
```

^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

### Scala: Full example with profile

```scala
package org.example.application

import com.databricks.connect.[[databrickssession|DatabricksSession]]
import com.databricks.sdk.core.DatabricksConfig
import org.apache.spark.sql.SparkSession

object Main {
  def main(args: Array[String]): Unit = {
    val config = new DatabricksConfig().setProfile("my-profile")
    val spark = [[databrickssession|DatabricksSession]].builder().sdkConfig(config).getOrCreate()
    val df = spark.read.table("samples.nyctaxi.trips")
    df.limit(5).show()
  }
}
```

^[tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md]

## Dependencies and VM Options

### Scala (sbt)

Add the Databricks Connect library to your `build.sbt` file with a version matching your Databricks Runtime version:

```scala
libraryDependencies += "com.databricks" %% "databricks-connect" % "17.3.+"
```

Replace `17.3` with the Databricks Runtime version of your target cluster.^[tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md]

### Required JVM Options for Scala

When running from IntelliJ IDEA, add the following VM option to avoid reflection-access warnings:

```
--add-opens=java.base/java.nio=ALL-UNNAMED
```

This option can also be configured in the sbt build file using `fork := true` and `javaOptions`.^[tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The underlying connectivity framework.
- SparkSession — The standard Spark entry point that [DatabricksSession](/concepts/databrickssession.md) extends.
- [Configuration profiles for Databricks authentication](/concepts/databricks-configuration-profiles-for-authentication.md) — Storing workspace credentials.
- [OAuth user-to-machine authentication](/concepts/user-to-machine-u2m-authentication.md) — Recommended auth method for development.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — GPU-accelerated runtime that also supports [DatabricksSession](/concepts/databrickssession.md).

## Sources

- code-examples-for-databricks-connect-for-python-databricks-on-aws.md  
- tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-python-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-python-databricks-on-aws-43e94551.md)
2. [tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md](/references/tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws-da20890c.md)
