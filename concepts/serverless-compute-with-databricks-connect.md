---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 62ac98b34ef8e5353260576bc8781227c5a2fd9a07f12d138b235f7f1ba24e32
  pageDirectory: concepts
  sources:
    - databricks-connect-usage-requirements-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-compute-with-databricks-connect
    - SCWDC
    - Serverless compute support for Databricks Connect
    - Serverless compute for Databricks Connect
  citations:
    - file: databricks-connect-usage-requirements-databricks-on-aws.md
title: Serverless Compute with Databricks Connect
description: Support for connecting Databricks Connect to serverless compute resources, available starting from Databricks Connect version 15.1 with specific workspace requirements.
tags:
  - databricks
  - serverless
  - compute
timestamp: "2026-06-19T18:11:08.340Z"
---

# Serverless Compute with Databricks Connect

**Serverless Compute with Databricks Connect** enables you to connect your local development environment to a Databricks serverless compute resource, allowing you to run Spark code locally while leveraging Databricks' serverless infrastructure for execution.

## Overview

Databricks Connect allows you to develop and debug Spark applications locally using your preferred IDE, then execute them remotely on Databricks compute. When using serverless compute, the workload runs on Databricks' serverless infrastructure rather than a traditional cluster, eliminating the need to manage cluster lifecycles. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Requirements

### Workspace Requirements

To use Databricks Connect with serverless compute, your workspace must meet the following requirements:

- Your Databricks account and workspace must have [Unity Catalog](/concepts/unity-catalog.md) enabled. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- The workspace must meet the [requirements for serverless compute](https://docs.databricks.com/aws/en/compute/serverless/#requirements). ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- The Databricks Runtime version of your compute must be greater than or equal to the Databricks Connect package version. Databricks recommends using the most recent Databricks Connect package that matches your Databricks Runtime version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Version Compatibility

Serverless compute is supported starting with **Databricks Connect version 15.1**. Versions of Databricks Connect that are lower than or equal to the Databricks Runtime release on serverless are fully compatible. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

To verify whether a specific Databricks Connect version is compatible with serverless compute, see the documentation on [Validating the connection to Databricks](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config#validate). ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Local Environment Requirements

Your local development environment must meet the following requirements:

- **Python 3** must be installed, with a minor version that satisfies the version compatibility requirements for your Databricks Connect version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- **Authentication** to Databricks must be configured. Supported authentication types include:
  - [OAuth user-to-machine (U2M) authentication](/concepts/user-to-machine-u2m-authentication.md) — Requires using the Databricks CLI to authenticate before running code. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
  - [OAuth machine-to-machine (M2M) authentication](/concepts/machine-to-machine-m2m-authentication.md) — Supported on Databricks SDK for Python 0.19.0 and above. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- For User-Defined Functions (UDFs), the local minor version of Python must match the minor version of Python on the serverless compute. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Key Differences from Cluster Connections

When connecting to serverless compute instead of a traditional cluster:

| Aspect | Serverless Compute | Traditional Cluster |
|--------|-------------------|-------------------|
| Required Databricks Connect version | 15.1+ | 13.3 LTS+ |
| Compute management | No cluster lifecycle management required | Must create/configure clusters |
| Access mode requirement | Workspace must meet serverless requirements | Cluster must use Assigned or Shared access mode |

^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Best Practices

- Use the most recent Databricks Connect package that matches your Databricks Runtime version on the serverless compute. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- For features available in later Databricks Runtime versions, upgrade the Databricks Connect package accordingly. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- Always validate the connection to Databricks after configuring your environment. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library for connecting local environments to Databricks compute
- Serverless Compute — Databricks' serverless compute infrastructure
- [Unity Catalog](/concepts/unity-catalog.md) — Required for using Databricks Connect
- Databricks CLI — Required for OAuth U2M authentication setup
- Databricks SDK for Python — Underlying SDK for authentication support

## Sources

- databricks-connect-usage-requirements-databricks-on-aws.md

# Citations

1. [databricks-connect-usage-requirements-databricks-on-aws.md](/references/databricks-connect-usage-requirements-databricks-on-aws-a56357da.md)
