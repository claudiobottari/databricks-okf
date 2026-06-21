---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e80247da896887056dbf826bcb4d80e8dbcad48e646203b7c63d81b412ff32c8
  pageDirectory: concepts
  sources:
    - databricks-connect-usage-requirements-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-python-environment-requirements
    - DCPER
  citations:
    - file: databricks-connect-usage-requirements-databricks-on-aws.md
title: Databricks Connect Python Environment Requirements
description: Local environment requires Python 3 with correct minor version matching the Databricks Runtime, especially for UDF compatibility.
tags:
  - databricks-connect
  - python
  - environment
timestamp: "2026-06-18T15:06:13.362Z"
---

Here is the wiki page for "Databricks Connect Python Environment Requirements", written based solely on the provided source material.

---

## Databricks Connect Python Environment Requirements

**Databricks Connect Python Environment Requirements** are the prerequisites that a local development environment must meet to install and run [Databricks Connect](/concepts/databricks-connect.md) for Python. Databricks Connect allows you to run Spark code locally while executing it on a Databricks cluster or serverless compute.

## Python Version Requirements

Python 3 must be installed on the local development machine. The specific Python minor version required depends on the target Databricks environment. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

- **General compatibility**: The minor version of Python installed locally must meet the version requirements listed in the [Databricks Connect version compatibility table](#databricks-connect-versions). ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- **User-defined functions (UDFs)**: If you use UDFs in your code, the local Python minor version must exactly match the Python minor version of the Databricks Runtime running on the cluster or serverless compute. To find the Python version of a Databricks Runtime, refer to the *System environment* section of that version's release notes. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Databricks Connect Versions

Databricks Connect version numbers correspond to Databricks Runtime version numbers. For the full list of available releases, see the [Databricks Connect release notes](https://docs.databricks.com/aws/en/release-notes/dbconnect/). ^[databricks-connect-usage-requirements-databricks-on-aws.md]

The supported Python versions for each Databricks Connect version are detailed in the version compatibility table. Databricks Connect versions that have reached end-of-support should be upgraded to a supported version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Authentication Requirements

Authentication to Databricks must be configured locally. The supported OAuth methods and their prerequisites include: ^[databricks-connect-usage-requirements-databricks-on-aws.md]

- **[OAuth user-to-machine (U2M) authentication](/concepts/user-to-machine-u2m-authentication.md)**: Requires the Databricks CLI to be installed and authenticated before running code. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- **[OAuth machine-to-machine (M2M) authentication](/concepts/machine-to-machine-m2m-authentication.md)**: Supported alongside U2M on Databricks SDK for Python version 0.19.0 and above. To use these methods, the project's Databricks SDK for Python must be at least version 0.19.0. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Package Version Compatibility

The Databricks Runtime version of the target compute must be greater than or equal to the Databricks Connect package version. Databricks recommends using the most recent Databricks Connect package that matches the Databricks Runtime version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect Local Environment Requirements](/concepts/databricks-connect-local-environment-requirements.md) — Complete list of requirements including Scala
- [Databricks Connect cluster configuration](/concepts/databricks-connect-compute-configuration.md) — Setting up a cluster for Databricks Connect
- Databricks Runtime Python versions — Python versions in each Databricks Runtime release
- Databricks SDK for Python — Required for OAuth authentication

## Sources

- databricks-connect-usage-requirements-databricks-on-aws.md

# Citations

1. [databricks-connect-usage-requirements-databricks-on-aws.md](/references/databricks-connect-usage-requirements-databricks-on-aws-a56357da.md)
