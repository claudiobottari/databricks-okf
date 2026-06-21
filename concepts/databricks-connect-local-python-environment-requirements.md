---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 549b11c4ae324adbff4be1acdd8cbe5a9758495f462a9e866171dbb6b5788e0b
  pageDirectory: concepts
  sources:
    - databricks-connect-usage-requirements-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-local-python-environment-requirements
    - DCLPER
  citations:
    - file: databricks-connect-usage-requirements-databricks-on-aws.md
title: Databricks Connect Local Python Environment Requirements
description: Python 3 must be installed locally, and the minor version must satisfy the version compatibility table; the document references both Python and Scala APIs.
tags:
  - databricks
  - python
  - environment
timestamp: "2026-06-19T09:50:11.021Z"
---

# Databricks Connect Local Python Environment Requirements

**Databricks Connect Local Python Environment Requirements** describes the Python and authentication prerequisites that a local development environment must satisfy to install and run [Databricks Connect](/concepts/databricks-connect.md) against a Databricks workspace (Databricks Runtime 13.3 LTS and above). Meeting these requirements ensures that code written locally can interact with cluster or [serverless compute](/concepts/serverless-gpu-compute.md) resources without version mismatches or connection failures.

## Overview

To use Databricks Connect, the local development machine must have Python 3 installed, a compatible minor version (see the version compatibility table), and proper authentication configured. If the workload involves User-Defined Functions (UDFs), the local Python minor version must exactly match the minor version running on the target compute. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Python Version Requirements

The local environment must have **Python 3** installed. The minor version (e.g., 3.8, 3.9, 3.10) must meet the requirements listed in the Databricks Connect version compatibility table, which maps Databricks Connect versions to supported Python minor versions. Databricks Connect version numbers correspond to Databricks Runtime version numbers; therefore, upgrading Databricks Connect may require a corresponding Python upgrade. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

The Databricks Connect release notes and Databricks Runtime release notes provide the authoritative version matrix. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## UDF Version Matching

When using user-defined functions (UDFs), the **local minor version of Python must match the minor version of Python** on the Databricks Runtime version of the cluster or serverless compute. For example, if the cluster runs Databricks Runtime 13.3 LTS with Python 3.9, the local environment must also use Python 3.9. The minor Python version for each Databricks Runtime release is documented in the _System environment_ section of the Databricks Runtime release notes. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

This requirement ensures binary compatibility of the UDF serialization and execution.

## Authentication Setup

Although not strictly a Python version requirement, authentication must be configured locally before Databricks Connect can connect to the workspace. The recommended method is **OAuth user-to-machine (U2M) authentication** using the Databricks CLI. The Databricks CLI must be installed and authenticated before running Databricks Connect code. OAuth U2M and OAuth machine-to-machine (M2M) authentication are supported on Databricks SDK for Python 0.19.0 and above. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Workspace Prerequisites

While the workspace must have [Unity Catalog](/concepts/unity-catalog.md) enabled and the compute (cluster or serverless) must meet its own access mode requirements, those are not local environment concerns. However, the local environment must be configured to point to a workspace that satisfies these prerequisites for Databricks Connect to function. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Databricks Runtime
- User-Defined Functions (UDFs)
- [OAuth authentication](/concepts/user-to-machine-u2m-authentication.md)
- Databricks CLI
- [Serverless compute](/concepts/serverless-gpu-compute.md)

## Sources

- databricks-connect-usage-requirements-databricks-on-aws.md

# Citations

1. [databricks-connect-usage-requirements-databricks-on-aws.md](/references/databricks-connect-usage-requirements-databricks-on-aws-a56357da.md)
