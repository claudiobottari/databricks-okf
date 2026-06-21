---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7973308e1d1f490ce349bcacfd32a5a9e878b8d059830399c9a0ead4c2f93606
  pageDirectory: concepts
  sources:
    - databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-compatibility
    - DRC
    - Databricks Runtime ML Compatibility Matrix
    - Databricks Runtime ML compatibility
  citations:
    - file: databricks-connect-for-python-databricks-on-aws.md
title: Databricks Runtime Compatibility
description: Version compatibility requirements between Databricks Runtime and Databricks Connect client packages.
tags:
  - databricks
  - versioning
  - compatibility
timestamp: "2026-06-19T09:48:01.201Z"
---

# Databricks Runtime Compatibility

**Databricks Runtime Compatibility** refers to the set of requirements and constraints governing which version of [Databricks Connect](/concepts/databricks-connect.md) works with a given Databricks Runtime version. Understanding compatibility is essential for successfully connecting local development environments to Databricks compute.

## Overview

Databricks Connect enables you to connect popular IDEs such as PyCharm, notebook servers, and other custom applications to Databricks compute. The Python version of Databricks Connect is supported for Databricks Runtime 13.3 LTS and above. ^[databricks-connect-for-python-databricks-on-aws.md]

## Version Requirements

When setting up Databricks Connect for Python, you must confirm that your workspace and local development environment meet the Databricks Connect requirements and choose a Databricks Connect package version that is compatible with your specific Databricks Runtime configuration. ^[databricks-connect-for-python-databricks-on-aws.md]

### Runtime Support

- **Databricks Runtime 13.3 LTS and above**: Supported by Databricks Connect for Python
- **Databricks Runtime 12.2 LTS and below**: Requires migration to the newer Databricks Connect version (see [Migrate to Databricks Connect for Python](/concepts/databricks-connect-for-python.md)) ^[databricks-connect-for-python-databricks-on-aws.md]

## Compute Types

Databricks Connect for Python supports both classic compute and serverless compute configurations. Separate tutorials are available for each:
- Tutorial: Run code from PyCharm on classic compute
- Tutorial: Run Python code on serverless compute ^[databricks-connect-for-python-databricks-on-aws.md]

## Language Variants

Databricks Connect is available for multiple programming languages, each with its own compatibility considerations:

- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) – Supported for Databricks Runtime 13.3 LTS and above
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) – Separate documentation and version requirements
- [Databricks Connect for R](/concepts/databricks-connect-for-r.md) – Separate documentation and version requirements ^[databricks-connect-for-python-databricks-on-aws.md]

## Configuration Resources

To learn more about compatibility and configuration:

- [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md) – Detailed workspace and environment requirements
- [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) – How to configure compute for Databricks Connect
- Troubleshooting Databricks Connect – Common compatibility issues and solutions
- [Databricks Connect Limitations](/concepts/databricks-connect-limitations.md) – Known limitations and workarounds ^[databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- Databricks Runtime
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- Serverless Compute on Databricks
- Classic Compute on Databricks

## Sources

- databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-connect-for-python-databricks-on-aws.md](/references/databricks-connect-for-python-databricks-on-aws-669513ea.md)
