---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 19be31e99037f509151011736655cb517b11d882a2d835694bfd29d5a32b3b24
  pageDirectory: concepts
  sources:
    - databricks-connect-usage-requirements-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-cluster-requirements
    - DCCR
  citations:
    - file: databricks-connect-usage-requirements-databricks-on-aws.md
title: Databricks Connect Cluster Requirements
description: Requirements for target compute resources including cluster access modes (Assigned or Shared) and serverless compute support (starting from Databricks Connect 15.1)
tags:
  - databricks
  - clusters
  - serverless
timestamp: "2026-06-18T11:35:48.843Z"
---

# Databricks Connect Cluster Requirements

**Databricks Connect** allows you to connect your local development environment to a Databricks cluster or serverless compute to run Spark jobs remotely. This page covers the compute-side requirements that must be met before you can establish a connection.

## Workspace Requirements

Your Databricks account and workspace must have [Unity Catalog](/concepts/unity-catalog.md) enabled. See [Get started with Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/get-started) and [Enable a workspace for Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/enable-workspaces). ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Cluster Requirements

### Access Mode

If you are connecting to a cluster (as opposed to serverless compute), the target cluster must use a cluster access mode of **Assigned** or **Shared**. See [Cluster access modes](/concepts/databricks-connect-cluster-access-modes.md) for details. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Databricks Runtime Version

The Databricks Runtime version of your compute must be **greater than or equal to** the Databricks Connect package version. Databricks recommends using the most recent Databricks Connect package that matches your Databricks Runtime version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

To use features available in later versions of Databricks Runtime, you must upgrade the Databricks Connect package. See the Databricks Connect release notes and Databricks Runtime release notes for version information. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Serverless Compute Requirements

If you are connecting to serverless compute, the following additional requirements apply:

- Your workspace must meet the general [requirements for serverless compute](/concepts/trust-relationship-for-serverless-compute.md).
- Serverless compute is supported starting with **Databricks Connect version 15.1**.
- Versions of Databricks Connect that are lower than or equal to the Databricks Runtime release on serverless are fully compatible. See the Serverless compute release notes.
- To verify if your Databricks Connect version is compatible with serverless compute, see Validate the connection to Databricks.

^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Local Environment Requirements

### Python Version

Python 3 must be installed locally, and the minor version must meet the requirements specified in the version compatibility table. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

#### UDFs and Python Version Matching

If you are using user-defined functions (UDFs), the **local minor version of Python must match the minor version of Python** on the Databricks Runtime version of your cluster or serverless compute. To find the minor Python version of a specific Databricks Runtime version, refer to the **System environment** section of the Databricks Runtime release notes for that version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Authentication

Authentication to Databricks must be configured. Depending on the authentication type, there may be specific requirements:

- **OAuth user-to-machine (U2M) authentication**: You must use the Databricks CLI to authenticate before running your code. See the Databricks Connect for Python tutorial.
- **OAuth U2M and OAuth machine-to-machine (M2M) authentication**: Supported on Databricks SDK for Python 0.19.0 and above.

^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Language Support

Databricks Connect supports both Python and Scala. The version compatibility table shows which Databricks Connect versions correspond to which language and Databricks Runtime versions. Databricks Connect version numbers correspond to Databricks Runtime version numbers. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## End-of-Support Versions

Databricks Connect follows the [Databricks Runtime Support Lifecycles](/concepts/databricks-connect-support-lifecycle.md). Versions that have reached end-of-support should be upgraded to a supported version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — Overview of the Databricks Connect client
- [Cluster access modes](/concepts/databricks-connect-cluster-access-modes.md) — Access mode options for Databricks clusters
- [Serverless compute](/concepts/serverless-gpu-compute.md) — Databricks serverless compute for Spark workloads
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance and cataloging requirements
- Databricks SDK for Python — Authentication and SDK requirements
- [User-defined functions (UDFs)](/concepts/abac-user-defined-functions-udfs.md) — Requirements for running UDFs with Databricks Connect

## Sources

- databricks-connect-usage-requirements-databricks-on-aws.md

# Citations

1. [databricks-connect-usage-requirements-databricks-on-aws.md](/references/databricks-connect-usage-requirements-databricks-on-aws-a56357da.md)
