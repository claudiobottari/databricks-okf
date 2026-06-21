---
title: Create and run JARs on serverless compute | Databricks on AWS
source: https://docs.databricks.com/aws/en/jobs/how-to/use-jars-in-workflows
ingestedAt: "2026-06-18T08:07:54.120Z"
---

important

Databricks strongly recommends Declarative Automation Bundles instead of building and deploying JARs manually as described on this page. Declarative Automation Bundles makes it easy to create a project from a template that has the correct Scala, JDK, and Databricks Connect versions already configured for serverless, and also enables simple deployment of the JAR to the Databricks workspace. See [Build a Scala JAR with Declarative Automation Bundles](https://docs.databricks.com/aws/en/dev-tools/bundles/scala-jar).

A [Java archive](https://en.wikipedia.org/wiki/JAR_\(file_format\)) (JAR) packages Java or Scala code into a single file. Create a JAR with Spark code and deploy it as a JAR task on [serverless compute](https://docs.databricks.com/aws/en/jobs/run-serverless-jobs) in a Lakeflow Job.

## Requirements[​](#requirements "Direct link to requirements")

To build a JAR, your local development environment must have the following installed:

*   [sbt](https://www.scala-sbt.org/download/) 1.11.7 or higher for Scala JARs
*   [Maven](https://maven.apache.org/install.html) 3.9.0 or higher for Java JARs
*   JDK, Scala, and Databricks Connect versions that match your [serverless environment](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/). See [Dependency versions](#dependency-versions).

### Dependency versions[​](#dependency-versions "Direct link to dependency-versions")

important

To run on serverless compute without failures, your JAR Scala and JDK versions must exactly match the runtime Scala and JDK versions. See [Databricks Connect versions](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements#versions).

The example on this page uses [serverless environment version 4](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/), so this page creates a JAR that:

*   Is compiled against Scala 2.13; every dependency uses the `_2.13` suffix.
*   Is compiled against JDK 17, class file version 61.
*   Is compiled against Databricks Connect 17.3, the Spark API surface for serverless compute.
*   Uses only public Spark APIs. It uses no RDDs and no Spark internals. See [Limitations](#limitations).
*   Includes every dependency in the JAR or attached as a serverless environment library. See [Managing dependencies](#dependencies).

#### Limitations[​](#limitations "Direct link to limitations")

Serverless compute uses [Spark Connect](https://docs.databricks.com/aws/en/compute/lakeguard#lakeguard-architecture). Your JAR runs against a thin client library that exposes the public Spark APIs, while the Spark engine itself runs server-side. Code that bypasses the public API can't benefit from Catalyst optimization or [Photon](https://docs.databricks.com/aws/en/compute/photon) acceleration, even on classic compute. RDD-based and internals-dependent code is generally slower than the equivalent DataFrame or SQL code.

The following aren't available:

*   RDD API (`org.apache.spark.rdd.*`) and `SparkContext` / `JavaSparkContext`. Use `SparkSession.builder().getOrCreate()` and DataFrame/Dataset operations instead.
*   Spark internal APIs (`org.apache.spark.catalyst.*`, `org.apache.spark.util.*`, `org.apache.spark.sql.util.*`, `org.apache.spark.sql.internal.*`). Code that imports these APIs fail with `NoClassDefFoundError`. Refactor to the public Spark API. If a third-party library uses internals, check whether it publishes a Spark Connect-compatible release.
*   Native libraries (`.so`, `.dll`, JNI). Serverless compute does not permit writing native libraries to the file system. Libraries that unpack native binaries at startup fail with `UnsatisfiedLinkError`. Init scripts are not a workaround. Use a Java equivalent if one is available.

If your workload requires any of the above, run it on [standard or dedicated compute](https://docs.databricks.com/aws/en/compute/) instead.

## Step 1: Build a JAR[​](#step-1-build-a-jar "Direct link to step-1-build-a-jar")

*   Scala
*   Java

1.  Run the following command to create a Scala project:
    
    Bash
    
        sbt new scala/scala-seed.g8
    
    When prompted, enter a project name, for example, `my-spark-app`.
    
2.  Next, delete the seed's stub files and create the directory for your source:
    
    Bash
    
        cd my-spark-apprm src/main/scala/example/Hello.scalarm src/test/scala/example/HelloSpec.scalarm project/Dependencies.scalamkdir -p src/main/scala/com/examples
    
3.  Replace the contents of your `build.sbt` file with the following:
    
    Scala
    
        name := "my-spark-app"// Set the dependency versionsscalaVersion := "2.13.16"javacOptions ++= Seq("--release", "17")scalacOptions ++= Seq("-release", "17")libraryDependencies += "com.databricks" %% "databricks-connect" % "17.3.2" % "provided"// Your other dependencies go here. Use %% for Scala libraries so sbt picks the _2.13 artifact.// Fork a new JVM on run so our javaOptions are applied.fork := truejavaOptions += "--add-opens=java.base/java.nio=ALL-UNNAMED"
    
4.  Edit or create a `project/plugins.sbt` file, and add this line:
    
    Scala
    
        addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "2.3.1")
    
5.  Create your main class in `src/main/scala/com/examples/SparkJar.scala`:
    
    Scala
    
        package com.examplesimport org.apache.spark.sql.SparkSessionobject SparkJar {  def main(args: Array[String]): Unit = {    val spark = SparkSession.builder().getOrCreate()    // Prints the arguments to the class, which    // are job parameters when run as a job:    println(args.mkString(", "))    // Shows using spark:    println(spark.version)    println(spark.range(10).limit(3).collect().mkString(" "))  }}
    
6.  To build your JAR file, run the following command:
    
    The compiled JAR is created in the `target/` folder as `my-spark-app-assembly-0.1.0-SNAPSHOT.jar`.
    

### Manage dependencies[​](#manage-dependencies "Direct link to manage-dependencies")

To make a library available to your JAR on serverless compute:

*   **Use a [provided library](#provided-libraries)**: Serverless compute includes Databricks Connect and a curated set of common libraries. If your version is compatible, declare it `provided` in your build and don't include it in your JAR.
*   **Attach as an environment library**: Add a library to your [serverless environment](https://docs.databricks.com/aws/en/compute/serverless/dependencies#libraries) if it isn't already provided. Use this for runtime-only libraries you don't want to include.
*   **Connect to an external database**: For JDBC sources, use a [JDBC connection](https://docs.databricks.com/aws/en/connect/jdbc-connection) instead of including a driver. JDBC connections are Unity Catalog\-managed. Credentials, lineage, and governance are handled for you.

#### Provided libraries[​](#provided-libraries "Direct link to provided-libraries")

The following libraries are required dependencies and are available by default on serverless compute. Declare them `provided` in your build. Bundling your own versions of these libraries triggers a `NoSuchMethodError` at runtime.

note

The library versions listed below are for **serverless environment version 4**. For installed libraries for other environment versions, see the [serverless environment version notes](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/) reference.

*   `com.databricks:databricks-connect_2.13`, version 17.3.2
*   `org.scala-lang:scala-library_2.13`, version 2.13.16
*   `org.scala-lang:scala-reflect_2.13`, version 2.13.16
*   `org.slf4j:slf4j-api`, version 2.0.10
*   `org.apache.logging.log4j:log4j-api`, version 2.20.0
*   `org.apache.logging.log4j:log4j-core`, version 2.20.0
*   `org.apache.httpcomponents:httpclient`, version 4.5.14
*   `org.apache.httpcomponents:httpcore`, version 4.4.16
*   `com.fasterxml.jackson.core:jackson-databind`, version 2.15.2
*   `com.fasterxml.jackson.core:jackson-core`, version 2.15.2
*   `com.fasterxml.jackson.core:jackson-annotations`, version 2.15.2
*   `com.fasterxml.jackson.datatype:jackson-datatype-jsr310`, version 2.15.2
*   `com.google.guava:guava`, version 32.0.1-jre
*   `commons-io:commons-io`, version 2.14.0
*   `org.json4s:json4s-jackson_2.13`, version 4.0.7
*   `org.apache.commons:commons-lang3`, version 3.14.0
*   `org.apache.commons:commons-configuration2`, version 2.11.0
*   `org.apache.commons:commons-text`, version 1.12.0
*   `com.databricks:databricks-sdk-java`, version 0.52.0
*   `com.databricks:databricks-dbutils-scala_2.13`, version 0.1.4

## Step 2: Create a job to run the JAR[​](#step-2-create-a-job-to-run-the-jar "Direct link to step-2-create-a-job-to-run-the-jar")

1.  In your workspace, click ![Workflows icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0zLjc1IDRDNC40NDAzNiA0IDUgMy40NDAzNiA1IDIuNzVDNSAyLjA1OTY0IDQuNDQwMzYgMS41IDMuNzUgMS41QzMuMDU5NjQgMS41IDIuNSAyLjA1OTY0IDIuNSAyLjc1QzIuNSAzLjQ0MDM2IDMuMDU5NjQgNCAzLjc1IDRaTTYuMzk2NDggMy41QzYuMDcwMDIgNC42NTQyNSA1LjAwODc4IDUuNSAzLjc1IDUuNUMyLjIzMTIyIDUuNSAxIDQuMjY4NzggMSAyLjc1QzEgMS4yMzEyMiAyLjIzMTIyIDAgMy43NSAwQzUuMDA4NzggMCA2LjA3MDAyIDAuODQ1NzQ4IDYuMzk2NDggMkgxMS42MjVDMTMuNDg5IDIgMTUgMy41MTEwNCAxNSA1LjM3NUMxNSA3LjE5OTQgMTMuNTUyNCA4LjY4NTY5IDExLjc0MzIgOC43NDc5N0w4LjQzNTk0IDExLjExMDNDOC4xNzUxNiAxMS4yOTY2IDcuODI0ODUgMTEuMjk2NiA3LjU2NDA4IDExLjExMDNMNC4yNjQxNiA4Ljc1MzIyQzMuMjgwMjIgOC44MTA1OCAyLjUgOS42MjY2OCAyLjUgMTAuNjI1QzIuNSAxMS42NjA1IDMuMzM5NDcgMTIuNSA0LjM3NSAxMi41SDkuNjAzNTJDOS45Mjk5OCAxMS4zNDU3IDEwLjk5MTIgMTAuNSAxMi4yNSAxMC41QzEzLjc2ODggMTAuNSAxNSAxMS43MzEyIDE1IDEzLjI1QzE1IDE0Ljc2ODggMTMuNzY4OCAxNiAxMi4yNSAxNkMxMC45OTEyIDE2IDkuOTI5OTggMTUuMTU0MyA5LjYwMzUyIDE0SDQuMzc1QzIuNTExMDQgMTQgMSAxMi40ODkgMSAxMC42MjVDMSA4LjgwMDYgMi40NDc1OCA3LjMxNDMgNC4yNTY4MSA3LjI1MjAzTDcuNTY0MDggNC44ODk2OUM3LjgyNDg1IDQuNzAzNDMgOC4xNzUxNiA0LjcwMzQzIDguNDM1OTQgNC44ODk2OUwxMS43MzU5IDcuMjQ2NzhDMTIuNzE5OCA3LjE4OTQxIDEzLjUgNi4zNzMzMiAxMy41IDUuMzc1QzEzLjUgNC4zMzk0NyAxMi42NjA1IDMuNSAxMS42MjUgMy41SDYuMzk2NDhaTTEzLjUgMTMuMjVDMTMuNSAxMy45NDA0IDEyLjk0MDQgMTQuNSAxMi4yNSAxNC41QzExLjU1OTYgMTQuNSAxMSAxMy45NDA0IDExIDEzLjI1QzExIDEyLjU1OTYgMTEuNTU5NiAxMiAxMi4yNSAxMkMxMi45NDA0IDEyIDEzLjUgMTIuNTU5NiAxMy41IDEzLjI1Wk04LjAwMDAxIDYuNDIxNjdMNS43OTAzNSA4TDguMDAwMDEgOS41NzgzM0wxMC4yMDk3IDhMOC4wMDAwMSA2LjQyMTY3WiIgZmlsbD0iIzZGNkY2RiIvPgo8L3N2Zz4K) **Jobs & Pipelines** in the sidebar.
    
2.  Click **Create**, then **Job**.
    
3.  Click the **JAR** tile to configure the first task. If the **JAR** tile is not available, click **Add another task type** and search for **JAR**.
    
4.  Optionally, replace the name of the job, which defaults to **`New Job <date-time>`**, with your job name.
    
5.  In **Task name**, enter a name for the task, for example `JAR_example`.
    
6.  If necessary, select **JAR** from the **Type** drop-down menu.
    
7.  For **Main class**, enter the package and class of your JAR. If you followed the example earlier, enter `com.examples.SparkJar`.
    
8.  For **Compute**, select **Serverless**.
    
9.  Configure the serverless environment:
    
    1.  Select an environment, then click ![Pencil icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xMy40ODc0IDEuNTEyNTZDMTIuODA0IDAuODI5MTQ2IDExLjY5NiAwLjgyOTE0NSAxMS4wMTI2IDEuNTEyNTZMMS4yMTk2NyAxMS4zMDU1QzEuMDc5MDIgMTEuNDQ2MSAxIDExLjYzNjkgMSAxMS44MzU4VjE0LjMzNThDMSAxNC43NSAxLjMzNTc5IDE1LjA4NTggMS43NSAxNS4wODU4SDQuMjVDNC40NDg5MSAxNS4wODU4IDQuNjM5NjggMTUuMDA2OCA0Ljc4MDMzIDE0Ljg2NjFMMTQuNTczMiA1LjA3MzIyQzE1LjI1NjYgNC4zODk4MSAxNS4yNTY2IDMuMjgxNzcgMTQuNTczMiAyLjU5ODM1TDEzLjQ4NzQgMS41MTI1NlpNMTIuMDczMiAyLjU3MzIyQzEyLjE3MDkgMi40NzU1OSAxMi4zMjkxIDIuNDc1NTkgMTIuNDI2OCAyLjU3MzIyTDEzLjUxMjYgMy42NTkwMUMxMy42MTAyIDMuNzU2NjQgMTMuNjEwMiAzLjkxNDkzIDEzLjUxMjYgNC4wMTI1NkwxMiA1LjUyNTEzTDEwLjU2MDcgNC4wODU3OUwxMi4wNzMyIDIuNTczMjJaTTkuNSA1LjE0NjQ1TDIuNSAxMi4xNDY0VjEzLjU4NThIMy45MzkzNEwxMC45MzkzIDYuNTg1NzlMOS41IDUuMTQ2NDVaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Edit** to configure it.
    2.  Select **4** or higher for the **Environment version**.
    3.  Add your JAR file by dragging and dropping it into the file selector, or browse to select it from a Unity Catalog volume or workspace location.
10.  For **Parameters**, for this example, enter `["Hello", "World!"]`.
     
11.  Click **Create task**.
     

## Step 3: Run the job and view the job run details[​](#step-3-run-the-job-and-view-the-job-run-details "Direct link to step-3-run-the-job-and-view-the-job-run-details")

Click ![Run Now Button](data:image/png;base64,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) to run the workflow. To view [details for the run](https://docs.databricks.com/aws/en/jobs/monitor#job-run-details), click **View run** in the **Triggered run** pop-up or click the link in the **Start time** column for the run in the [job runs](https://docs.databricks.com/aws/en/jobs/monitor#view-job-run-list) view.

When the run completes, the output appears in the **Output** pane, including the arguments you passed to the task.

## Troubleshooting[​](#troubleshooting "Direct link to troubleshooting")

The following table provides troubleshooting information for common exceptions.

## Next steps[​](#next-steps "Direct link to next-steps")

*   To learn more about JAR tasks, see [JAR task for jobs](https://docs.databricks.com/aws/en/jobs/jar).
*   To learn more about creating a compatible JAR, see [Create a Databricks compatible JAR](https://docs.databricks.com/aws/en/jobs/jar-create).
*   To learn more about creating and running jobs, see [Lakeflow Jobs](https://docs.databricks.com/aws/en/jobs/).
