---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 505ea2ce5731b8c1e2295d5ef27d3d63ea2b2962ba07614df7dfdf1f0d5ceaee
  pageDirectory: concepts
  sources:
    - databricks-connect-usage-requirements-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-serverless-compute-support
    - DCSCS
  citations:
    - file: databricks-connect-usage-requirements-databricks-on-aws.md
title: Databricks Connect Serverless Compute Support
description: Support for connecting Databricks Connect to serverless compute starting from version 15.1, with workspace-level prerequisites for serverless compute.
tags:
  - databricks
  - serverless
  - compute
timestamp: "2026-06-19T14:47:45.582Z"
---

# Databricks Connect Serverless Compute Support

**Databricks Connect Serverless Compute Support** refers to the ability to use [Databricks Connect](/concepts/databricks-connect.md) to connect a local development environment (e.g., PyCharm, notebook servers, custom applications) to a Databricks serverless compute resource instead of a classic cluster. This capability is available starting with Databricks Connect version 15.1.^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Requirements

### Workspace requirements

To use Databricks Connect with serverless compute:

- Your Databricks account and workspace must have [Unity Catalog](/concepts/unity-catalog.md) enabled.^[databricks-connect-usage-requirements-databricks-on-aws.md]
- The workspace must meet the [requirements for serverless compute](https://docs.databricks.com/aws/en/compute/serverless/#requirements).^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Version compatibility

Serverless compute is supported **starting with Databricks Connect version 15.1**.^[databricks-connect-usage-requirements-databricks-on-aws.md] Versions of Databricks Connect that are lower than or equal to the Databricks Runtime release running on serverless compute are fully compatible.^[databricks-connect-usage-requirements-databricks-on-aws.md] Databricks recommends using the most recent Databricks Connect package that matches your Databricks Runtime version.^[databricks-connect-usage-requirements-databricks-on-aws.md]

To verify whether your installed Databricks Connect version is compatible with serverless compute, see Validate the connection to Databricks.^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Local environment requirements

- **Python version**: If you are using user-defined functions (UDFs), the local minor version of Python must match the minor version of Python of the Databricks Runtime version running on serverless compute.^[databricks-connect-usage-requirements-databricks-on-aws.md] The Python version of the serverless Databricks Runtime is listed in the [Serverless compute release notes](https://docs.databricks.com/aws/en/release-notes/serverless/).^[databricks-connect-usage-requirements-databricks-on-aws.md]
- **Authentication**: Supported authentication types for connecting to serverless compute include OAuth user-to-machine (U2M) and OAuth machine-to-machine (M2M) authentication.^[databricks-connect-usage-requirements-databricks-on-aws.md] You must configure authentication before running your code (for example, using the Databricks CLI for U2M).^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — Overview of the tool
- [Serverless compute](/concepts/serverless-gpu-compute.md) — The compute resource type
- [Unity Catalog](/concepts/unity-catalog.md) — Required for workspace connectivity
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — Language‑specific documentation
- [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) — Detailed compute setup

## Sources

- databricks-connect-usage-requirements-databricks-on-aws.md

# Citations

1. [databricks-connect-usage-requirements-databricks-on-aws.md](/references/databricks-connect-usage-requirements-databricks-on-aws-a56357da.md)
