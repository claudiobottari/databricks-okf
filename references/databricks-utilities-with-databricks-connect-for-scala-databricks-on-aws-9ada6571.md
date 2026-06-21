---
title: Databricks Utilities with Databricks Connect for Scala | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/databricks-utilities
ingestedAt: "2026-06-18T08:06:40.019Z"
---

note

This article covers Databricks Connect for Databricks Runtime 13.3 LTS and above.

This article describes how to use [Databricks Utilities](https://docs.databricks.com/aws/en/dev-tools/databricks-utils) with Databricks Connect for Scala. Databricks Connect enables you to connect popular IDEs, notebook servers, and custom applications to Databricks clusters. See [Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/).

Before you begin to use Databricks Connect, you must [set up the Databricks Connect client](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/install).

For the Python version of this article, see [Databricks Utilities with Databricks Connect for Python](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/databricks-utilities).

## Available Databricks Utilities[​](#available-databricks-utilities "Direct link to Available Databricks Utilities")

You use Databricks Connect to access Databricks Utilities as follows:

*   Use `DBUtils.getDBUtils` to access the [Databricks File System (DBFS)](https://docs.databricks.com/aws/en/dbfs/) and [secrets](https://docs.databricks.com/aws/en/dev-tools/databricks-utils#secrets-utility-dbutilssecrets) through Databricks Utilities. `DBUtils.getDBUtils` belongs to the [Databricks Utilities for Scala](https://central.sonatype.com/artifact/com.databricks/databricks-dbutils-scala_2.12/versions) library.
*   No Databricks Utilities functionality other than the preceding utilities are available for Scala projects.
*   Databricks Connect for Scala already declares a dependency on the Databricks Utilities for Scala library, so you do not need to explicitly declare this dependency in your Scala project's build file such as `build.sbt` for `sbt`, `pom.xml` for Maven, or `build.gradle` for Gradle.
*   Authentication for the Databricks Utilities for Scala library is determined through initializing the `DatabricksSession` class in your Databricks Connect project for Scala.

## Example: Create a file in a volume[​](#example-create-a-file-in-a-volume "Direct link to Example: Create a file in a volume")

The following example shows how to use the Databricks Utilities for Scala library to automate a Unity Catalog volume. This example creates a file named `zzz_hello.txt` in the volume's path within the workspace, reads the data from the file, and then deletes the file.

Scala

    import com.databricks.sdk.scala.dbutils.DBUtilsobject Main {  def main(args: Array[String]): Unit = {    val filePath = "/Volumes/main/default/my-volume/zzz_hello.txt"    val fileData = "Hello, Databricks!"    val dbutils = DBUtils.getDBUtils()    dbutils.fs.put(      file = filePath,      contents = fileData,      overwrite = true    )    println(dbutils.fs.head(filePath))    dbutils.fs.rm(filePath)  }}
