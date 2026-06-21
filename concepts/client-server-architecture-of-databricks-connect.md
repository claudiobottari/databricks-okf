---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6366bb68528bdc1dfdd601846f35fad51d4ee0bb71283175e052b57f450a7373
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - client-server-architecture-of-databricks-connect
    - CAODC
  citations:
    - file: databricks-connect-databricks-on-aws.md
title: Client-Server Architecture of Databricks Connect
description: The architectural pattern where Databricks Connect separates code execution into local (general code), remote cluster (DataFrame APIs), and cluster-side (UDFs), enabling interactive debugging on the client while leveraging Spark on Databricks for data transformations.
tags:
  - architecture
  - client-server
  - remote-execution
timestamp: "2026-06-18T15:02:45.913Z"
---

---
title: Client-Server Architecture of Databricks Connect
summary: Databricks Connect uses a decoupled client-server architecture based on Spark Connect, where general code and DataFrame APIs run locally while Spark transformations execute remotely on Databricks compute.
sources:
  - databricks-connect-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:06:07.370Z"
tags:
  - databricks-connect
  - architecture
  - spark-connect
aliases:
  - client-server-architecture-of-databricks-connect
  - csadc
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Client-Server Architecture of Databricks Connect

Databricks Connect is a client library for the Databricks Runtime that enables remote connectivity to Databricks compute from IDEs, notebooks, and custom applications. It is built on an open-source gRPC-based protocol called [Spark Connect](/concepts/spark-connect.md), which has a decoupled client-server architecture for Apache Spark.^[databricks-connect-databricks-on-aws.md]

## How It Works

The client-server architecture of Databricks Connect is based on three key patterns for how code is executed across the local client and remote Databricks cluster:^[databricks-connect-databricks-on-aws.md]

### General Code Runs Locally

Python, Scala, and R code runs on the client side, enabling interactive debugging. All non-Spark code is executed locally on the developer's machine.^[databricks-connect-databricks-on-aws.md]

### DataFrame APIs Are Executed on Databricks Compute

All data transformations using the DataFrame API are converted to unresolved Spark logical plans and executed on the Databricks compute through the remote Spark session. The underlying protocol uses Apache Arrow on top of gRPC. Results are materialized locally when using commands such as `collect()`, `show()`, and `toPandas()`.^[databricks-connect-databricks-on-aws.md]

### UDF Code Runs on Databricks Compute

User-defined functions (UDFs) defined locally are serialized and transmitted to the Databricks cluster where they execute. Other APIs that run user code on Databricks include `foreach`, `foreachBatch`, and `transformWithState`.^[databricks-connect-databricks-on-aws.md]

## Client vs. Server Responsibilities

The architecture separates responsibility between client and server:^[databricks-connect-databricks-on-aws.md]

- **Client (local machine):** Runs general application code, manages Python virtual environments, and installs application dependencies that execute locally.
- **Server (Databricks cluster):** Executes all Spark code, including DataFrame transformations and UDFs. For UDFs, dependencies must be installed on the Databricks cluster separately.

## Dependencies Management

Because code runs across two environments, dependencies are managed separately:^[databricks-connect-databricks-on-aws.md]

- **Application dependencies** are installed on the local machine as part of the Python virtual environment or project setup.
- **UDF dependencies** must be installed on Databricks separately. See Manage UDF Dependencies.

## Protocol Details

Spark Connect is built on an open-source gRPC-based protocol that:
- Uses unresolved logical plans for query representation
- Uses Apache Arrow for data serialization
- Enables thin client APIs that can be embedded in application servers, IDEs, notebooks, and programming languages^[databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) – Python-specific setup and usage
- [Databricks Connect for R](/concepts/databricks-connect-for-r.md) – R-specific setup and usage
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) – Scala-specific setup and usage
- [Spark Connect](/concepts/spark-connect.md) – The open-source protocol underlying Databricks Connect
- Databricks Runtime – The compute environment where Spark code executes
- Manage UDF Dependencies – How to install UDF dependencies on Databricks

## Sources

- databricks-connect-databricks-on-aws.md

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)
