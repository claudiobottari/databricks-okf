---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f498ef0152205afd02e999e10de8f9443b75b4e2c19701dbc11bae4363020222
  pageDirectory: concepts
  sources:
    - databricks-connect-usage-requirements-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-local-environment-requirements
    - DCLER
  citations:
    - file: databricks-connect-usage-requirements-databricks-on-aws.md
title: Databricks Connect Local Environment Requirements
description: Local development prerequisites for Databricks Connect including Python version, authentication setup (OAuth U2M/M2M), and Scala compatibility.
tags:
  - databricks
  - development
  - authentication
timestamp: "2026-06-19T18:10:56.130Z"
---

# Databricks Connect Local Environment Requirements

**Databricks Connect Local Environment Requirements** describes the Python, authentication, and runtime version prerequisites that a local development machine must satisfy before installing and using Databricks Connect to connect to a Databricks workspace. These requirements apply to Databricks Connect for Databricks Runtime 13.3 LTS and above. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Python Requirements

Python 3 must be installed on the local machine. The minor version of Python must meet the version requirements specified in the [Databricks Connect version compatibility table](/concepts/databricks-connect-version-compatibility.md). ^[databricks-connect-usage-requirements-databricks-on-aws.md]

If you are using user-defined functions (UDFs), there is an additional constraint: the local minor version of Python must match the minor version of Python of the Databricks Runtime version running on the target cluster or serverless compute. To find the minor Python version for a specific Databricks Runtime release, refer to the *System environment* section of the corresponding release notes. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Authentication Requirements

Authentication to Databricks must be configured on the local environment. The requirements vary by authentication type: ^[databricks-connect-usage-requirements-databricks-on-aws.md]

- **OAuth user-to-machine (U2M) authentication:** You must use the Databricks CLI to authenticate before running your code. To set this up, install and configure the Databricks CLI. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- **OAuth U2M and machine-to-machine (M2M) authentication:** Both are supported on Databricks SDK for Python version 0.19.0 and above. If your project uses an older version, update it following the Databricks SDK for Python getting started guide. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Databricks Connect Version and Runtime Compatibility

The Databricks Runtime version of the target compute (cluster or serverless compute) must be greater than or equal to the Databricks Connect package version installed locally. Databricks recommends using the most recent Databricks Connect package that matches your Databricks Runtime version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

To use features available in later Databricks Runtime versions, you must upgrade the Databricks Connect package. See the Databricks Connect release notes for a list of available releases, and the Databricks Runtime release notes for version compatibility information. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## End-of-Support Versions

Databricks Connect follows the [Databricks Runtime Support Lifecycles](/concepts/databricks-runtime-support-lifecycles.md). Versions that have reached end-of-support should be upgraded to a supported version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – Overview of the connectivity tool
- [Databricks Connect cluster configuration](/concepts/databricks-connect-compute-configuration.md) – Setting up target clusters or serverless compute
- [Databricks Connect Python tutorial](/concepts/databricks-connect-for-python.md) – Step-by-step setup guide
- [Unity Catalog](/concepts/unity-catalog.md) – Required workspace feature
- [Serverless compute requirements](/concepts/serverless-compute-tracing-requirements.md) – Additional constraints for serverless targets

## Sources

- databricks-connect-usage-requirements-databricks-on-aws.md

# Citations

1. [databricks-connect-usage-requirements-databricks-on-aws.md](/references/databricks-connect-usage-requirements-databricks-on-aws-a56357da.md)
