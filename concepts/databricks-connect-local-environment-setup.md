---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1a3a9752e8326c44bd25f319cab1284bf85d58a8a9959c9a07957cc6e2641b48
  pageDirectory: concepts
  sources:
    - databricks-connect-usage-requirements-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-local-environment-setup
    - DCLES
  citations:
    - file: databricks-connect-usage-requirements-databricks-on-aws.md
title: Databricks Connect Local Environment Setup
description: Local development environment prerequisites including Python 3 installation, Python version matching for UDFs, and Scala requirements
tags:
  - databricks
  - setup
  - python
  - scala
timestamp: "2026-06-18T11:35:55.949Z"
---

# Databricks Connect Local Environment Setup

**Databricks Connect** is a client library that allows you to run Spark code and work with Databricks resources from your local development environment. It connects to a Databricks cluster or serverless compute to execute code remotely, making it useful for development and testing without needing to be in the Databricks workspace directly. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Overview

Databricks Connect enables you to develop Spark applications locally using your preferred IDE and tools, then submit them to run on a Databricks cluster or [serverless compute](/concepts/serverless-gpu-compute.md) endpoint. This setup requires careful configuration of your local environment to ensure compatibility with the target Databricks Runtime version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Prerequisites

### Databricks Workspace Requirements

Before setting up Databricks Connect locally, your Databricks workspace must meet the following requirements:

- **Unity Catalog must be enabled** for the workspace. See Get started with Unity Catalog and Enable a workspace for Unity Catalog. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- **The Databricks Runtime version of your compute must be greater than or equal to the Databricks Connect package version**. Databricks recommends using the most recent Databricks Connect package that matches your Databricks Runtime version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- **For serverless compute**: Your workspace must meet the [serverless compute requirements](/concepts/serverless-compute-tracing-requirements.md). Serverless compute is supported starting with Databricks Connect version 15.1. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- **For cluster connections**: The target cluster must use an access mode of **Assigned** or **Shared**. See [Access modes](/concepts/standard-access-mode.md). ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Local Development Environment Requirements

Your local machine must meet the following requirements to install and use Databricks Connect:

#### Python Environment
- **Python 3** must be installed, with the minor version matching the requirements in the version compatibility table. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- **For user-defined functions (UDFs)**: The local minor version of Python must match the minor version of Python of the Databricks Runtime version of the target cluster or serverless compute. To find the minor Python version, refer to the *System environment* section of the Databricks Runtime release notes or the Serverless compute release notes. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

#### Authentication
- **Authentication to Databricks must be configured**. Depending on the authentication type, there may be additional requirements: ^[databricks-connect-usage-requirements-databricks-on-aws.md]
  - **OAuth user-to-machine (U2M)**: Requires the Databricks CLI to authenticate before running code. See Install or update the Databricks CLI. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
  - **OAuth machine-to-machine (M2M)**: Supported on the Databricks SDK for Python 0.19.0 and above. See Get started with the Databricks SDK for Python. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Version Compatibility

Databricks Connect version numbers correspond to Databricks Runtime version numbers. The following table shows supported versions and compatible language versions: ^[databricks-connect-usage-requirements-databricks-on-aws.md]

| Databricks Connect Version | Python Version | Notes |
|---------------------------|----------------|-------|
| 13.3 LTS and above | See release notes | Match minor version for UDF compatibility |
| 15.1+ | See release notes | Supports serverless compute |

#### End-of-Support Versions

Databricks Connect follows the Databricks Runtime [support lifecycles](/concepts/databricks-runtime-support-lifecycles.md). If you are using a version that has reached end-of-support, upgrade to a supported version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Installation Steps

### Option 1: Python (pip)

Install Databricks Connect using pip:

```bash
pip install databricks-connect
```

Ensure the installed version matches or is compatible with your target Databricks Runtime version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Option 2: Scala / SBT

For Scala projects, add the Databricks Connect dependency to your `build.sbt` file:

```scala
libraryDependencies += "com.databricks" %% "databricks-connect" % "<version>"
```

Replace `<version>` with the appropriate Databricks Connect version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Configuration and Validation

### Configure Connection

After installation, configure the connection to your Databricks workspace:

```bash
databricks-connect configure
```

This command prompts for workspace URL, authentication token, and cluster ID. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Validate Connection

To verify the connection works:

```bash
databricks-connect test
```

For serverless compute compatibility validation, see Validate the connection to Databricks. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Best Practices

- **Use matching versions**: Keep your local Databricks Connect package version aligned with the target Databricks Runtime version to avoid compatibility issues. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- **Upgrade packages**: To use features available in later Databricks Runtime versions, upgrade the Databricks Connect package accordingly. See Databricks Connect release notes. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- **Version compatibility** for UDFs: Ensure the local Python minor version matches the remote environment when using user-defined functions. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Related Concepts

- Databricks Runtime versions — The runtime version that defines available features
- [Serverless compute](/concepts/serverless-gpu-compute.md) — A compute option for Databricks Connect
- [Unity Catalog](/concepts/unity-catalog.md) — Required for workspace connectivity
- [OAuth authentication](/concepts/user-to-machine-u2m-authentication.md) — Supported authentication methods
- Databricks SDK for Python — Required for M2M authentication
- [Cluster access modes](/concepts/databricks-connect-cluster-access-modes.md) — Supported modes for Databricks Connect
- [User-defined functions (UDFs)](/concepts/abac-user-defined-functions-udfs.md) — Functions that require Python version matching

## Sources

- databricks-connect-usage-requirements-databricks-on-aws.md

# Citations

1. [databricks-connect-usage-requirements-databricks-on-aws.md](/references/databricks-connect-usage-requirements-databricks-on-aws-a56357da.md)
