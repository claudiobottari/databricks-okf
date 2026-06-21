---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 530bd5fc7b2ae6bd6aeb2f3c8a4467be01374e677d6c4e8648fca8dd79dc5305
  pageDirectory: concepts
  sources:
    - databricks-connect-usage-requirements-databricks-on-aws.md
    - install-databricks-connect-for-scala-databricks-on-aws.md
    - migrate-to-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-connect-version-compatibility
    - DCVC
    - Databricks Connect version compatibility table
    - Databricks Connect version support matrix
  citations:
    - file: databricks-connect-usage-requirements-databricks-on-aws.md
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
    - file: install-databricks-connect-for-scala-databricks-on-aws.md
    - file: migrate-to-databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Connect Version Compatibility
description: The version alignment rules between Databricks Connect packages and Databricks Runtime versions, including support lifecycles and end-of-support policies.
tags:
  - databricks
  - versioning
  - compatibility
timestamp: "2026-06-19T18:11:00.494Z"
---

# Databricks Connect Version Compatibility

**Databricks Connect Version Compatibility** establishes the relationship between the Databricks Connect client library version and the Databricks Runtime (DBR) version on the target compute resource. Compliance with this compatibility rule is required for a successful connection.

## Version Relationship

Databricks Connect version numbers correspond to Databricks Runtime version numbers. For example, Databricks Connect 14.x is designed to work with Databricks Runtime 14.x. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### For Databricks Runtime 13.3 LTS and Above

The Databricks Runtime version of your compute must be **greater than or equal to** the Databricks Connect package version. Databricks recommends using the most recent Databricks Connect package that matches your Databricks Runtime version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

- If you upgrade your Databricks Runtime version, you must also upgrade your Databricks Connect client to a compatible version.
- To use features available in later Databricks Runtime versions, you must upgrade the Databricks Connect package accordingly. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### For Databricks Runtime 12.2 LTS and Below

The Databricks Connect major and minor package version must exactly match your Databricks Runtime version. For example, when using Databricks Runtime 12.2 LTS, you must install `databricks-connect==12.2.*`. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Supported Versions

Databricks Connect releases are aligned with Databricks Runtime releases. See the Databricks Connect release notes for a list of available releases. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Python

For Databricks Connect 13.3 LTS and above, Python 3 must be installed locally and the minor version of Python must meet the version requirements shown in the version compatibility table. If you are using user-defined functions (UDFs), the local minor Python version must match the minor Python version on the target cluster or serverless compute. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Scala

For Scala clients, the correct version of the Java Development Kit (JDK) and Scala must be installed locally to match your Databricks cluster. The Databricks Connect library version numbers can be found in the Maven central repository. ^[install-databricks-connect-for-scala-databricks-on-aws.md, migrate-to-databricks-connect-for-scala-databricks-on-aws.md]

### Legacy Versions (12.2 LTS and Below)

For Databricks Runtime 12.2 LTS and below, the minor Python version on the client must be the same as the minor Python version on the cluster. Additionally, Java Runtime Environment (JRE) 8 is required. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Serverless Compute Compatibility

Serverless compute is supported starting with Databricks Connect version 15.1. Versions lower than or equal to the Databricks Runtime release on serverless are fully compatible. ^[databricks-connect-usage-requirements-databricks-on-aws.md] To verify compatibility, use the Validate command or refer to the Serverless compute release notes. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## End-of-Support Versions

Databricks Connect follows the Databricks Runtime [support lifecycles](/concepts/databricks-runtime-support-lifecycles.md). The following versions have reached end-of-support and are no longer recommended for new development. If you are using an end-of-support version, upgrade to a supported version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

- **Python and Scala:** Databricks Connect 13.x and 14.x (final versions) have reached end-of-support. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- Databricks Runtime 12.2 LTS and below are considered legacy and are no longer supported for new development. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Prerequisites for Connection

### Workspace Requirements

- [Unity Catalog](/concepts/unity-catalog.md) must be enabled.
- Compute must use **Assigned** or **Shared** access mode.
- For serverless compute, the workspace must meet serverless compute requirements. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Local Environment Requirements

- Python 3 installed with the appropriate minor version (for Python clients).
- For Scala clients: the correct JDK and Scala versions matching the target cluster. ^[install-databricks-connect-for-scala-databricks-on-aws.md]
- For OAuth authentication: Databricks CLI installed and configured, and Databricks SDK for Python 0.19.0+ for OAuth user-to-machine (U2M) and machine-to-machine (M2M) authentication. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- For legacy clients (12.2 LTS and below): Java Runtime Environment (JRE) 8. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library for local development.
- Databricks Runtime — The compute engine version.
- Databricks Connect release notes — Version-specific release information.
- [Serverless compute](/concepts/serverless-gpu-compute.md) — Supported from Databricks Connect 15.1+.
- [OAuth authentication](/concepts/user-to-machine-u2m-authentication.md) — Supported from Databricks SDK for Python 0.19.0+.
- [Unity Catalog](/concepts/unity-catalog.md) — Required for connection.
- [Support lifecycles](/concepts/databricks-runtime-support-lifecycles.md) — Databricks Runtime version support policies.

## Sources

- databricks-connect-usage-requirements-databricks-on-aws.md
- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
- install-databricks-connect-for-scala-databricks-on-aws.md
- migrate-to-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-connect-usage-requirements-databricks-on-aws.md](/references/databricks-connect-usage-requirements-databricks-on-aws-a56357da.md)
2. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)
3. [install-databricks-connect-for-scala-databricks-on-aws.md](/references/install-databricks-connect-for-scala-databricks-on-aws-9a592761.md)
4. [migrate-to-databricks-connect-for-scala-databricks-on-aws.md](/references/migrate-to-databricks-connect-for-scala-databricks-on-aws-050a2949.md)
