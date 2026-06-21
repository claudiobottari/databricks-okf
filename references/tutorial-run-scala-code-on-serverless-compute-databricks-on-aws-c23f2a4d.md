---
title: "Tutorial: Run Scala code on serverless compute | Databricks on AWS"
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/jar-compile
ingestedAt: "2026-06-18T08:06:44.483Z"
---

This tutorial provides an overview of how to get started with Databricks Connect for Scala using serverless compute. It walks through building a Unity Catalog\-enabled compute (either classic compute in standard access mode or serverless compute) compatible Scala JAR file.

## Requirements[​](#requirements "Direct link to Requirements")

Your local development environment must meet the requirements for Databricks Connect for Scala. See [Databricks Connect usage requirements](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements), which includes the following:

*   Java Development Kit (JDK)
    
*   sbt
    
*   Databricks CLI, configured for serverless compute:
    
        databricks auth login --configure-serverless --host <workspace-url>
    

## Step 1: Create a Scala project[​](#step-1-create-a-scala-project "Direct link to Step 1: Create a Scala project")

First create a Scala project. When prompted, enter a project name, for example, `my-spark-app`.

Bash

    sbt new scala/scala-seed.g8

## Step 2: Update the Scala and JDK versions[​](#step-2-update-the-scala-and-jdk-versions "Direct link to Step 2: Update the Scala and JDK versions")

Before building your JAR, ensure the version of the Java Development Kit (JDK) and Scala that you use to compile your code are supported for serverless compute. For details on this requirement, see [Set JDK and Scala versions](https://docs.databricks.com/aws/en/jobs/jar-create#set-versions).

For compatible versions, see the [version support matrix](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements#versions).

The following configuration is for Scala 2.13 and JDK 17, which is compatible with dedicated or standard access compute with Databricks Runtime version 17 and [serverless environment version 4](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/four).

    scalaVersion := "2.13.16"javacOptions ++= Seq("-source", "17", "-target", "17")scalacOptions ++= Seq("-release", "17")

## Step 3: Add Databricks Connect as a dependency[​](#step-3-add-databricks-connect-as-a-dependency "Direct link to step-3-add-databricks-connect-as-a-dependency")

Add Databricks Connect as a dependency to build Scala JARs. For more information, see [Spark dependencies](https://docs.databricks.com/aws/en/jobs/jar-create#dependencies).

In your Scala project's `build.sbt` build file, add the following reference to Databricks Connect.

    scalaVersion := "2.13.16"libraryDependencies += "com.databricks" %% "databricks-connect" % "17.3.+"// To run with new JVM options, a fork is required, otherwise it uses the same options as the sbt process.fork := truejavaOptions += "--add-opens=java.base/java.nio=ALL-UNNAMED"

## Step 4: Add other dependencies[​](#step-4-add-other-dependencies "Direct link to Step 4: Add other dependencies")

Databricks recommends packaging your application and all dependent libraries into a single JAR file, also known as an _über_ or _fat JAR_. Alternatively, you can install dependent libraries as [compute-scoped libraries](https://docs.databricks.com/aws/en/libraries/#compatibility) or in your serverless environment. For more information, see [Application dependencies](https://docs.databricks.com/aws/en/jobs/jar-create#application-dependencies).

important

Remove any dependency on Spark. Spark APIs are provided by Databricks Connect. For more information, see [Spark dependencies](https://docs.databricks.com/aws/en/jobs/jar-create#spark).

## Step 5: Add Spark code[​](#step-5-add-spark-code "Direct link to Step 5: Add Spark code")

Create your main class in `src/main/scala/example/DatabricksExample.scala`. For details about using Spark session in your Scala code, see [Use the Databricks Spark session](https://docs.databricks.com/aws/en/jobs/jar-create#spark-session).

Scala

    package com.examplesimport com.databricks.connect.DatabricksSessionimport org.apache.spark.sql.{SparkSession}object SparkJar {  def main(args: Array[String]): Unit = {    val spark: SparkSession = DatabricksSession.builder()      .validateSession(false)      .addCompiledArtifacts(SparkJar.getClass.getProtectionDomain.getCodeSource.getLocation.toURI)      .getOrCreate()    println(spark.version)    println(spark.range(10).limit(3).collect().mkString(" "))  }}

## Step 6: Run and build your code[​](#step-6-run-and-build-your-code "Direct link to Step 6: Run and build your code")

Next, run your code:

Now create a `project/assembly.sbt` file with the following line, then build the project:

    addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "2.3.1")

## Step 7: Deploy your JAR[​](#step-7-deploy-your-jar "Direct link to Step 7: Deploy your JAR")

Now deploy your JAR file using a JAR task from the UI or using Declarative Automation Bundles:

*   [JAR task for jobs](https://docs.databricks.com/aws/en/jobs/jar)
*   [JAR task](https://docs.databricks.com/aws/en/dev-tools/bundles/job-task-types#jar).
