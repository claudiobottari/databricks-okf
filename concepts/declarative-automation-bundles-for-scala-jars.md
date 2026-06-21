---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f4aa3fe868c6c6b1f6f90c64617634cad9fdfd6936cb9d3d935dca9473962a8f
  pageDirectory: concepts
  sources:
    - create-and-run-jars-on-serverless-compute-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - declarative-automation-bundles-for-scala-jars
    - DABFSJ
  citations:
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Declarative Automation Bundles for Scala JARs
description: Databricks recommends Declarative Automation Bundles over manual JAR building; bundles handle correct version configuration, templating, and easy deployment to the workspace.
tags:
  - databricks
  - bundles
  - automation
  - deployment
timestamp: "2026-06-19T18:00:17.810Z"
---

Here is the wiki page for "Declarative Automation Bundles for Scala JARs", based solely on the provided source material.

---

# Declarative Automation Bundles for Scala JARs

**Declarative Automation Bundles** is Databricks' recommended approach for building and deploying Scala JARs for serverless compute. Instead of manually configuring build files, dependency versions, and deployment steps, Declarative Automation Bundles provides a project template with the correct Scala, JDK, and Databricks Connect versions already configured, and enables simple deployment of the JAR to the Databricks workspace. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Overview

Building and deploying JARs manually requires careful management of dependency versions, build configurations, and deployment workflows. Declarative Automation Bundles simplifies this process by providing a standardized project structure that eliminates many common configuration errors. The template ensures compatibility with [serverless compute](/concepts/serverless-gpu-compute.md) environments by pre-configuring the correct versions of Scala, JDK, and Databricks Connect. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Benefits Over Manual JAR Building

When building JARs manually, developers must:

1.  Ensure Scala and JDK versions exactly match the serverless runtime environment.
2.  Manually configure build files (e.g., `build.sbt` or `pom.xml`) with correct dependency versions.
3.  Manage deployment of the JAR to the workspace.
4.  Handle dependency management, ensuring libraries are either included in the JAR, declared as provided, or attached as environment libraries.

Declarative Automation Bundles addresses all of these concerns through a template-based approach. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Creating a Project

To create a new Scala JAR project using Declarative Automation Bundles, use the project template that automatically configures:

- **Scala version** matching the serverless runtime (e.g., Scala 2.13).
- **JDK version** matching the serverless runtime (e.g., JDK 17, class file version 61).
- **Databricks Connect version** matching the serverless compute API surface (e.g., Databricks Connect 17.3).
- **Build tool configuration** for `sbt` or `Maven` with correct library dependencies.

The template also handles the creation of the assembly JAR and provides commands for deploying the JAR to the workspace. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Supported Build Tools

Declarative Automation Bundles supports both sbt (Scala Build Tool) and Maven for building Scala JARs:

- **sbt 1.11.7 or higher** for Scala JARs
- **Maven 3.9.0 or higher** for Java JARs

The template generates a properly configured build file for the selected tool. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Deploying the JAR

Once the project is created and the JAR is built, Declarative Automation Bundles provides a simple deployment mechanism to upload the JAR to the Databricks workspace. This eliminates the manual steps of dragging and dropping files or using the UI to select JAR files from Unity Catalog volumes or workspace locations. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Requirements

To use Declarative Automation Bundles for Scala JARs, your local development environment must have sbt 1.11.7 or higher installed. The template handles version compatibility automatically. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- Serverless Compute — The execution environment for JAR tasks
- [JAR Tasks for Jobs](/concepts/jar-task-in-lakeflow-jobs.md) — How to configure a job to run a JAR
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) — The job orchestration framework
- [Spark Connect](/concepts/spark-connect.md) — The API surface for serverless compute
- Databricks Connect Versions — Version compatibility requirements
- [Serverless Environment Versions](/concepts/serverless-environment-versioning.md) — Runtime environment configurations

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md

# Citations

1. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
