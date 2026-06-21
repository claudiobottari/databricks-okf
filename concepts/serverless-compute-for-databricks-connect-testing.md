---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3831041fb72a12a7fee2bc5f019ab7aa39975c1be6f49125deece1ad9bbfb74c
  pageDirectory: concepts
  sources:
    - troubleshooting-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-compute-for-databricks-connect-testing
    - SCFDCT
    - Serverless compute for Databricks Connect
  citations:
    - file: troubleshooting-databricks-connect-for-python-databricks-on-aws.md
title: Serverless Compute for Databricks Connect Testing
description: Databricks recommends using serverless compute with Databricks Connect for all testing because it provides Databricks Runtime features, Unity Catalog integration, faster execution, and better end-to-end validation than local OSS PySpark testing.
tags:
  - databricks-connect
  - serverless
  - testing
  - best-practices
timestamp: "2026-06-19T23:14:41.100Z"
---

# Serverless Compute for [Databricks Connect](/concepts/databricks-connect.md) Testing

**Serverless Compute** is a [Databricks Connect](/concepts/databricks-connect.md) compute mode that provisions on-demand infrastructure for running Spark jobs submitted from a local development environment. It is the recommended compute option for testing Python workloads with [Databricks Connect](/concepts/databricks-connect.md), replacing the need for a classic interactive cluster or a local open-source Apache Spark server. ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

## Benefits

Databricks recommends using serverless compute for all [Databricks Connect](/concepts/databricks-connect.md) testing for the following reasons: ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

- **Full feature parity with Databricks Runtime** — Serverless compute runs the same Databricks Runtime as a cluster, including features (e.g., [Delta Lake](/concepts/delta-lake.md), Photon) that are not available in open-source PySpark. This eliminates discrepancies between local testing and production. ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]
- **Faster testing** — Serverless compute eliminates cluster startup time and auto‑scales resources, making test cycles faster than using a local PySpark environment. ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]
- **Unity Catalog enforcement** — When testing with serverless compute, [Unity Catalog](/concepts/unity-catalog.md) permissions and policies are enforced, which is not the case when testing locally with PySpark. This ensures that access‑control issues are caught early. ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]
- **Integration testing readiness** — Serverless compute provides a true production‑like environment, making it suitable for integration tests rather than relying on unit tests with stubs. ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

## Configuration

To use serverless compute with [Databricks Connect](/concepts/databricks-connect.md), set up the compute configuration as described in the official documentation on [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md). The `serverless` option is available within the cluster‑configuration workflow. ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

## Avoiding open-source Apache Spark incompatibility

[Databricks Connect](/concepts/databricks-connect.md) is built against Databricks Runtime and is not compatible with an open‑source Apache [Spark Connect](/concepts/spark-connect.md) server (e.g., a local instance at `sc://localhost`). Attempting to connect to such a server results in class‑not‑found errors, serialization failures, or API mismatches. Serverless compute ensures a fully compatible runtime environment. ^[troubleshooting-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client used to connect IDEs and notebooks to Databricks compute.
- Serverless Compute – The general on‑demand compute model on Databricks.
- Databricks Runtime – The execution environment that serverless compute provides.
- [Unity Catalog](/concepts/unity-catalog.md) – Databricks’ unified governance solution enforced on serverless compute.
- PySpark – Open‑source Spark Python API, not recommended for [Databricks Connect](/concepts/databricks-connect.md) testing.

## Sources

- troubleshooting-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [troubleshooting-databricks-connect-for-python-databricks-on-aws.md](/references/troubleshooting-databricks-connect-for-python-databricks-on-aws-bb4d5efd.md)
