---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2f4a91bbe7e47bf1944804efd20fefa317301c7f744fa7386ebf75c3810cb93e
  pageDirectory: concepts
  sources:
    - databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-connect
    - SPARK_REMOTE
    - Spark Connect Server
  citations:
    - file: databricks-connect-databricks-on-aws.md
title: Spark Connect
description: An open-source gRPC-based protocol within Apache Spark that enables remote connectivity to Spark clusters using the DataFrame API with a decoupled client-server architecture.
tags:
  - apache-spark
  - protocol
  - grpc
  - architecture
timestamp: "2026-06-19T18:08:38.388Z"
---

```yaml
---
title: Spark Connect
summary: An open-source gRPC-based protocol within Apache Spark that enables remote execution of Spark workloads using the DataFrame API via a decoupled client-server architecture.
sources:
  - databricks-connect-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:46:23.808Z"
updatedAt: "2026-06-19T09:46:23.808Z"
tags:
  - apache-spark
  - gRPC
  - protocol
  - remote-execution
aliases:
  - spark-connect
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Spark Connect

**Spark Connect** is an open-source gRPC-based protocol within Apache Spark that allows remote execution of Spark workloads using the DataFrame API. It introduces a decoupled client-server architecture that separates the client application from the Spark driver, enabling Spark functionality to be embedded in environments where a full Spark distribution cannot run. ^[databricks-connect-databricks-on-aws.md]

## Architecture

Spark Connect uses a client-server model where the client communicates with a Spark server over gRPC, transmitting unresolved logical plans and Apache Arrow data. The client API is designed to be thin, so that it can be embedded in application servers, IDEs, notebooks, and programming languages. ^[databricks-connect-databricks-on-aws.md]

### How Code Execution Works

- **General code runs locally**: Python and Scala code executes on the client side, enabling interactive debugging. All local code runs locally, while all Spark code continues to run on the remote cluster. ^[databricks-connect-databricks-on-aws.md]
- **DataFrame APIs are executed on the remote cluster**: All data transformations are converted to Spark plans and run on the remote cluster through the remote Spark session. Results are materialized on the local client when using commands such as `collect()`, `show()`, and `toPandas()`. ^[databricks-connect-databricks-on-aws.md]
- **UDF code runs on the remote cluster**: User-defined functions (UDFs) defined locally are serialized, transmitted to the cluster, and executed there. APIs that run user code on the cluster include UDFs, `foreach`, `foreachBatch`, and `transformWithState`. ^[databricks-connect-databricks-on-aws.md]

## Relationship with Databricks Connect

For Databricks Runtime 13.3 LTS and above, [[Databricks Connect]] is an extension of Spark Connect with additions and modifications to support working with Databricks compute modes and Unity Catalog. ^[databricks-connect-databricks-on-aws.md]

## Key Features

- **Decoupled architecture**: The client and server are separate, enabling remote connectivity to Spark clusters. ^[databricks-connect-databricks-on-aws.md]
- **Protocol**: Uses gRPC for communication, with unresolved logical plans and Apache Arrow for data transfer. ^[databricks-connect-databricks-on-aws.md]
- **Thin client API**: Designed to be lightweight and embeddable in various environments, including IDEs, notebooks, and application servers. ^[databricks-connect-databricks-on-aws.md]
- **Language support**: Supported for Python, R, and Scala through Databricks Connect. ^[databricks-connect-databricks-on-aws.md]
- **IDE integration**: Enables interactive development and debugging from IDEs such as Visual Studio Code, PyCharm, and IntelliJ IDEA. ^[databricks-connect-databricks-on-aws.md]

## Dependencies Management

Spark Connect introduces a split dependency model: ^[databricks-connect-databricks-on-aws.md]

- **Application dependencies**: Dependencies required by code that runs locally must be installed on the client machine (e.g., in a Python virtual environment). ^[databricks-connect-databricks-on-aws.md]
- **UDF dependencies**: Dependencies required by UDFs that run on the remote cluster must be installed on the cluster. ^[databricks-connect-databricks-on-aws.md]

## Related Concepts

- Apache Spark — The distributed computing framework that hosts Spark Connect
- [[Databricks Connect]] — The Databricks extension of Spark Connect
- gRPC — The underlying communication protocol
- Apache Arrow — The data format used for efficient data transfer
- DataFrame API — The primary API available through Spark Connect
- [[Unity Catalog]] — A metadata catalog supported by the Databricks extension of Spark Connect

## Sources

- databricks-connect-databricks-on-aws.md
```

# Citations

1. [databricks-connect-databricks-on-aws.md](/references/databricks-connect-databricks-on-aws-65545eb5.md)
