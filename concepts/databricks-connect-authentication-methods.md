---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 51c8aa8fc6334969553f45f6d14161cc5f1c3700d6da434d1757085994722561
  pageDirectory: concepts
  sources:
    - databricks-connect-usage-requirements-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-authentication-methods
    - DCAM
  citations:
    - file: databricks-connect-usage-requirements-databricks-on-aws.md
title: Databricks Connect Authentication Methods
description: Supported authentication mechanisms for Databricks Connect including OAuth user-to-machine (U2M) and machine-to-machine (M2M) authentication via the Databricks SDK for Python.
tags:
  - databricks
  - authentication
  - oauth
  - security
timestamp: "2026-06-19T18:11:01.307Z"
---

# Databricks Connect Authentication Methods

**Databricks Connect Authentication Methods** refer to the supported ways a local development environment can authenticate with a Databricks workspace when using the Databricks Connect client library. Proper authentication is required to establish a connection between your local IDE or script and a Databricks cluster or serverless compute resource.

## Supported Authentication Types

Databricks Connect supports multiple authentication mechanisms, depending on the context of the connection and the environment configuration. The following authentication types are available:

### OAuth User-to-Machine (U2M) Authentication

OAuth U2M authentication authenticates a human user to the Databricks workspace. This method is supported on the Databricks SDK for Python version 0.19.0 and above. To use OAuth U2M with Databricks Connect, you must first authenticate using the Databricks CLI before running your code. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### OAuth Machine-to-Machine (M2M) Authentication

OAuth M2M authentication allows service principals and automated workflows to authenticate without interactive user input. Like U2M, M2M authentication is supported on Databricks SDK for Python version 0.19.0 and above. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Other Authentication Types

The Databricks Connect client leverages the broader Databricks authentication SDK to resolve credentials. Depending on your configuration, additional authentication types may be available, including personal access tokens (PAT), Azure Active Directory tokens, or other methods supported by the Databricks SDK. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Requirements

### Databricks SDK Version

For OAuth U2M and OAuth M2M authentication, your project must use the Databricks SDK for Python version 0.19.0 or above. To update the installed version of the SDK in your project, see the documentation on getting started with the Databricks SDK for Python. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Environment Prerequisites

- Python 3 must be installed, with a minor version matching the requirements in the version compatibility table for your Databricks Connect version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- If you are using user-defined functions (UDFs), the local minor version of Python must match the minor version of Python on the Databricks Runtime version of your target cluster or serverless compute. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Workspace Requirements

- The Databricks account and workspace must have [Unity Catalog](/concepts/unity-catalog.md) enabled. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- The Databricks Runtime version of your compute resource must be greater than or equal to the Databricks Connect package version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- If connecting to [serverless compute](/concepts/serverless-gpu-compute.md), the workspace must meet the serverless compute requirements, and serverless compute support begins with Databricks Connect version 15.1. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- If connecting to a cluster, the cluster must use an access mode of **Assigned** or **Shared**. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Configuration

Authentication configuration is typically handled through environment variables, the Databricks CLI, or the Databricks SDK's default credential chain. For OAuth U2M, you must authenticate with the Databricks CLI before executing your Databricks Connect code. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library for connecting local code to Databricks compute.
- [Databricks authentication types](/concepts/databricks-authentication-type.md) — Complete list of supported authentication mechanisms.
- Databricks CLI — Command-line tool used to configure OAuth U2M authentication.
- Databricks SDK for Python — Software development kit that provides the underlying authentication layer.
- [OAuth U2M authentication](/concepts/user-to-machine-u2m-authentication.md) — Interactive, user-based OAuth flow.
- [OAuth M2M authentication](/concepts/machine-to-machine-m2m-authentication.md) — Non-interactive, service principal–based OAuth flow.

## Sources

- databricks-connect-usage-requirements-databricks-on-aws.md

# Citations

1. [databricks-connect-usage-requirements-databricks-on-aws.md](/references/databricks-connect-usage-requirements-databricks-on-aws-a56357da.md)
