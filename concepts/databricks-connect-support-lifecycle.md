---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9e4a819f796fa6ce0f95041d47dbcc1d87a93e67dd32659018b30a865f290ac3
  pageDirectory: concepts
  sources:
    - databricks-connect-usage-requirements-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-support-lifecycle
    - DCSL
  citations:
    - file: databricks-connect-usage-requirements-databricks-on-aws.md
title: Databricks Connect Support Lifecycle
description: Databricks Connect follows the Databricks Runtime support lifecycles; end-of-support versions should be upgraded to supported versions.
tags:
  - databricks-connect
  - lifecycle
  - support
timestamp: "2026-06-18T15:05:31.497Z"
---

# Databricks Connect Support Lifecycle

**Databricks Connect** follows the same support lifecycle as the corresponding Databricks Runtime version it is based on. The Databricks Connect version number corresponds to the Databricks Runtime version number, and support for each Databricks Connect release aligns with the support timeline for that Databricks Runtime. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Support Lifecycle Policy

Databricks Connect adheres to the [Databricks Runtime Support Lifecycles](/concepts/databricks-runtime-support-lifecycles.md) policy. When a Databricks Runtime version reaches end-of-support (EOS), the corresponding Databricks Connect package also reaches end-of-support. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### End-of-Support Versions

Versions of Databricks Connect that have reached end-of-support are no longer maintained. Databricks recommends upgrading to a supported version to receive bug fixes, security updates, and compatibility with current Databricks workspace features. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

See the Databricks Connect Release Notes for a list of available Databricks Connect releases and their version history.

## Version Compatibility Requirements

### Databricks Runtime Version

The Databricks Runtime version of your target compute must be **greater than or equal to** the Databricks Connect package version. Databricks recommends using the most recent Databricks Connect package that matches your Databricks Runtime version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

For example, Databricks Connect version 15.x requires at least Databricks Runtime 15.x on the target cluster or serverless compute.

### Feature Availability

To use features available in later versions of Databricks Runtime, you must upgrade the Databricks Connect package to the corresponding version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Serverless Compute Compatibility

Serverless compute is supported starting with Databricks Connect version 15.1. Versions of Databricks Connect that are lower than or equal to the Databricks Runtime release on serverless are fully compatible. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

To verify compatibility between your Databricks Connect version and serverless compute, use the Databricks Connect Validation command to validate the connection.

## Python Version Match for UDFs

If you are using user-defined functions (UDFs), the local minor version of Python must match the minor version of Python on the target Databricks Runtime version. For example, if your cluster runs Databricks Runtime 15.4 LTS with Python 3.10, your local environment must also use Python 3.10. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

To find the Python version for a specific Databricks Runtime, refer to the **System environment** section of the Databricks Runtime Release Notes for that version, or the Serverless Compute Release Notes for serverless compute.

## Upgrading Databricks Connect

When upgrading to a newer Databricks Connect version:

1. Ensure your target compute (cluster or serverless) runs a Databricks Runtime version equal to or greater than the new Databricks Connect version.
2. Verify that your local Python version is compatible if using UDFs.
3. Validate the connection after upgrading using the validation command.

## Checking Support Status

To determine if your Databricks Connect version is supported:

- Check the [Databricks Runtime Support Lifecycles](/concepts/databricks-runtime-support-lifecycles.md) page for the support status of the corresponding Databricks Runtime version.
- Review the Databricks Connect Release Notes for version-specific announcements.
- Check the Serverless Compute Release Notes for serverless compatibility information.

## Related Concepts

- [Databricks Runtime Support Lifecycles](/concepts/databricks-runtime-support-lifecycles.md)
- [Databricks Connect](/concepts/databricks-connect.md)
- [Databricks Connect Version Requirements](/concepts/databricks-connect-requirements.md)
- Databricks Connect Validation
- Databricks Connect Release Notes
- Serverless Compute Release Notes
- [Databricks Runtime Version Compatibility](/concepts/databricks-runtime-version-compatibility.md)
- Unity Catalog Requirements

## Sources

- databricks-connect-usage-requirements-databricks-on-aws.md

# Citations

1. [databricks-connect-usage-requirements-databricks-on-aws.md](/references/databricks-connect-usage-requirements-databricks-on-aws-a56357da.md)
