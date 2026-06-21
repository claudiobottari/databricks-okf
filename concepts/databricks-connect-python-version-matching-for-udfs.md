---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 64ef1765b3daa811c192f4a26571de806c41dfa9b15d0fea470dbe94bea0d8b0
  pageDirectory: concepts
  sources:
    - databricks-connect-usage-requirements-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-python-version-matching-for-udfs
    - DCPVMFU
  citations:
    - file: databricks-connect-usage-requirements-databricks-on-aws.md
      start: 17
      end: 19
    - file: databricks-connect-usage-requirements-databricks-on-aws.md
      start: 21
      end: 25
title: Databricks Connect Python Version Matching for UDFs
description: When using user-defined functions (UDFs) with Databricks Connect, the local Python minor version must match the minor version on the target Databricks Runtime cluster or serverless compute.
tags:
  - databricks
  - python
  - udf
  - version-matching
timestamp: "2026-06-19T09:49:34.494Z"
---

# Databricks Connect Python Version Matching for UDFs

**Databricks Connect Python Version Matching for UDFs** refers to the requirement that when you use user-defined functions (UDFs) with [Databricks Connect](/concepts/databricks-connect.md), the minor version of Python on your local development machine must exactly match the minor version of Python running on the target Databricks Runtime cluster or [serverless compute](/concepts/serverless-gpu-compute.md). This constraint ensures that the serialized UDF code executed locally is binary‑compatible with the remote execution environment.

## Requirement

If your application includes Python UDFs, the local Python minor version must match the minor version of Python on the remote compute. For example, if the cluster runs Python 3.10.x, your local environment must also use Python 3.10.x (any patch version is acceptable). ^[databricks-connect-usage-requirements-databricks-on-aws.md:17-19]

### How to Determine the Remote Python Version

To find the minor Python version of the Databricks Runtime you are connecting to, consult the **System environment** section of the release notes for that Runtime version:

- For clusters: [Databricks Runtime release notes versions and compatibility](https://docs.databricks.com/aws/en/release-notes/runtime/)
- For serverless compute: [Serverless compute release notes](https://docs.databricks.com/aws/en/release-notes/serverless/)

^[databricks-connect-usage-requirements-databricks-on-aws.md:17-19]

## Why Matching Is Required

UDFs written in Python are serialized and sent to the remote Spark executor. If the Python versions differ, the serialized bytecode may be incompatible, causing runtime errors. Version matching guarantees that the standard library and C extensions present on the remote side match those used locally.

## Version Compatibility Table

The Databricks Connect documentation provides a table that maps each Databricks Connect version (which corresponds to a Databricks Runtime version) to the supported local Python minor version. You must use a Python version listed as compatible for your Databricks Connect version, in addition to the UDF‑specific minor‑version match. ^[databricks-connect-usage-requirements-databricks-on-aws.md:21-25]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that connects local code to a remote Spark cluster.
- User-Defined Functions (UDFs) — Custom Python functions executed on Spark workers.
- Databricks Runtime — The runtime environment on the cluster, which defines available Python versions.
- Serverless Compute — A serverless execution model for Databricks that also enforces Python version compatibility.

## Sources

- databricks-connect-usage-requirements-databricks-on-aws.md

# Citations

1. [databricks-connect-usage-requirements-databricks-on-aws.md:17-19](/references/databricks-connect-usage-requirements-databricks-on-aws-a56357da.md)
2. [databricks-connect-usage-requirements-databricks-on-aws.md:21-25](/references/databricks-connect-usage-requirements-databricks-on-aws-a56357da.md)
