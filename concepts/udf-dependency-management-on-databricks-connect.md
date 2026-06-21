---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 51534881c93fcef9cf98e8560cb54779abdddb8cb8da96e9dfccf1e48eb260c4
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - udf-dependency-management-on-databricks-connect
    - UDMODC
  citations:
    - file: databricks-connect-databricks-on-aws.md
title: UDF Dependency Management on Databricks Connect
description: The pattern where application dependencies are installed locally while UDF dependencies must be separately managed and installed on the Databricks cluster for remote execution.
tags:
  - dependency-management
  - udf
  - databricks
timestamp: "2026-06-19T18:08:47.726Z"
---

# UDF Dependency Management on Databricks Connect

**UDF Dependency Management on Databricks Connect** refers to the process of installing and managing software dependencies required by user-defined functions (UDFs) that execute on the Databricks cluster when using Databricks Connect. Because UDF code runs on Databricks compute rather than the local client, its dependencies must be installed separately from the application dependencies used for local code execution. ^[databricks-connect-databricks-on-aws.md]

## Overview

Databricks Connect uses a decoupled architecture where code runs in two distinct environments. General Python and Scala code executes on the local client machine, enabling interactive debugging. DataFrame API operations execute on the remote Databricks cluster. UDF code, including functions used with `foreach`, `foreachBatch`, and `transformWithState`, also runs on the Databricks compute side. ^[databricks-connect-databricks-on-aws.md]

This architectural separation creates two distinct dependency management concerns:
- **Local dependencies**: Application dependencies that run on the local machine must be installed as part of the local project, such as within a Python virtual environment.
- **UDF dependencies**: Dependencies required by UDFs that execute on the Databricks cluster must be installed on Databricks compute.

## Managing UDF Dependencies

UDF dependencies must be installed on the Databricks cluster because the serialized UDF code is transmitted from the local client and executed remotely. If a UDF imports a library that is not available on the cluster, it will fail at runtime. ^[databricks-connect-databricks-on-aws.md]

The recommended approach is to install UDF dependencies on the Databricks cluster using the cluster's library management features. This includes:
- Cluster Libraries – Installing Python packages, JARs, or other dependencies on the cluster via the Databricks UI, API, or cluster configuration.
- Databricks Runtime – Ensuring the cluster runs a compatible Databricks Runtime version (13.3 LTS and above for Databricks Connect support).

## Separation of Concerns

The dependency management model for Databricks Connect follows a clear separation:

| Dependency Type | Where It Runs | Where to Install |
|-----------------|---------------|------------------|
| Application dependencies | Local client machine | Local environment (e.g., Python virtual environment, Conda) |
| UDF dependencies | Databricks cluster | Cluster libraries or cluster configuration |

This separation allows developers to maintain different sets of dependencies for their development environment versus the execution environment, avoiding conflicts and ensuring that only necessary libraries are deployed to the cluster. ^[databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library that enables remote connectivity to Databricks compute.
- User-Defined Functions (UDFs) – Functions that run user code on Databricks compute.
- [Spark Connect](/concepts/spark-connect.md) – The open-source gRPC protocol underlying Databricks Connect.
- Cluster Libraries – Mechanism for installing dependencies on Databricks clusters.
- [Databricks Visual Studio Code Extension](/concepts/databricks-visual-studio-code-extension.md) – Uses Databricks Connect for debugging.

## Sources

- databricks-connect-databricks-on-aws.md

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)
