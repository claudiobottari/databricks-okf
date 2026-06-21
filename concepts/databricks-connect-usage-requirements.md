---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e1ed1531acce55363ec53b3f7897b36e1b44a156db4d9e07ceca9ca1d0c77cef
  pageDirectory: concepts
  sources:
    - databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-usage-requirements
    - DCUR
  citations:
    - file: databricks-connect-for-python-databricks-on-aws.md
      start: 2
      end: 2
    - file: databricks-connect-for-python-databricks-on-aws.md
      start: 4
      end: 4
    - file: databricks-connect-for-python-databricks-on-aws.md
      start: 8
      end: 9
    - file: databricks-connect-for-python-databricks-on-aws.md
      start: 7
      end: 7
    - file: databricks-connect-for-python-databricks-on-aws.md
      start: 10
      end: 11
    - file: databricks-connect-for-python-databricks-on-aws.md
      start: 22
      end: 22
    - file: databricks-connect-for-python-databricks-on-aws.md
      start: 13
      end: 14
title: Databricks Connect usage requirements
description: Prerequisites and compatibility requirements for workspace and local development environment to use Databricks Connect.
tags:
  - databricks
  - requirements
  - setup
timestamp: "2026-06-19T18:09:28.357Z"
---

# Databricks Connect Usage Requirements

**Databricks Connect Usage Requirements** describes the prerequisites that your Databricks workspace and local development environment must meet before you can use [Databricks Connect](/concepts/databricks-connect.md). These requirements apply to Databricks Runtime 13.3 LTS and above, which is the minimum runtime version supported by Databricks Connect. ^[databricks-connect-for-python-databricks-on-aws.md:2]

## Overview

Databricks Connect enables you to connect popular IDEs such as PyCharm and IntelliJ IDEA, notebook servers, and other custom applications to Databricks compute. Before installing and configuring Databricks Connect, you must confirm that your workspace and local development environment satisfy the necessary requirements. You also need to choose a Databricks Connect package version that is compatible with your configuration. ^[databricks-connect-for-python-databricks-on-aws.md:4]

## Workspace Requirements

Your Databricks workspace must be running a supported version of Databricks Runtime. Databricks Connect for Databricks Runtime 13.3 LTS and above is supported. ^[databricks-connect-for-python-databricks-on-aws.md:2]

## Local Development Environment Requirements

The specific requirements for your local environment depend on the language you use (Python, Scala, or R) and the Databricks Connect package version you choose. Consult the language-specific documentation for detailed version compatibility:

- For Python: see [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) ^[databricks-connect-for-python-databricks-on-aws.md:8-9]
- For Scala: see [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) ^[databricks-connect-for-python-databricks-on-aws.md:7]
- For R: see [Databricks Connect for R](/concepts/databricks-connect-for-r.md) ^[databricks-connect-for-python-databricks-on-aws.md:10-11]

## Compute Requirements

You must have access to a Databricks compute resource (classic cluster or serverless compute) that your Databricks Connect client can connect to. The compute resource must be running a compatible Databricks Runtime version. For detailed compute configuration guidance, see [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md). ^[databricks-connect-for-python-databricks-on-aws.md:22]

## Choosing a Compatible Package Version

Select a Databricks Connect package version that matches the Databricks Runtime version on your cluster. See [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md) for guidance on selecting a compatible version for your configuration. ^[databricks-connect-for-python-databricks-on-aws.md:13-14]

## Next Steps

After confirming that your environment meets the requirements:

1. Install Databricks Connect. See [Install Databricks Connect for Python](/concepts/databricks-connect-for-python.md) or the corresponding guide for your language.
2. Configure compute. See [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md).
3. Walk through a tutorial:
   - Tutorial: Run code from PyCharm on classic compute
   - Tutorial: Run Python code on serverless compute

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The overarching client library for connecting IDEs to Databricks compute.
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) – Python‑specific usage and installation.
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) – Scala‑specific usage and installation.
- [Databricks Connect for R](/concepts/databricks-connect-for-r.md) – R‑specific usage and installation.
- [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) – Detailed cluster setup guidance.
- Databricks Runtime – The compute environment running on Databricks clusters.

## Sources

- databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-connect-for-python-databricks-on-aws.md:2-2](/references/databricks-connect-for-python-databricks-on-aws-669513ea.md)
2. [databricks-connect-for-python-databricks-on-aws.md:4-4](/references/databricks-connect-for-python-databricks-on-aws-669513ea.md)
3. [databricks-connect-for-python-databricks-on-aws.md:8-9](/references/databricks-connect-for-python-databricks-on-aws-669513ea.md)
4. [databricks-connect-for-python-databricks-on-aws.md:7-7](/references/databricks-connect-for-python-databricks-on-aws-669513ea.md)
5. [databricks-connect-for-python-databricks-on-aws.md:10-11](/references/databricks-connect-for-python-databricks-on-aws-669513ea.md)
6. [databricks-connect-for-python-databricks-on-aws.md:22-22](/references/databricks-connect-for-python-databricks-on-aws-669513ea.md)
7. [databricks-connect-for-python-databricks-on-aws.md:13-14](/references/databricks-connect-for-python-databricks-on-aws-669513ea.md)
