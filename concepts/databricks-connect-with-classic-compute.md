---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 30fd854f6e5ed255e9fe2102aeb8eba50c105b874be3b4368eede53d8e93ef07
  pageDirectory: concepts
  sources:
    - databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-with-classic-compute
    - DCWCC
    - Databricks Compute|classic compute
    - Databricks Connect for Python classic compute tutorial
  citations:
    - file: databricks-connect-for-python-databricks-on-aws.md
title: Databricks Connect with Classic Compute
description: Support for running code from IDEs like PyCharm on classic (non-serverless) Databricks compute clusters
tags:
  - databricks
  - ide-integration
  - compute
timestamp: "2026-06-18T11:34:14.774Z"
---

# Databricks Connect with Classic Compute

**Databricks Connect** enables you to connect popular IDEs such as PyCharm, notebook servers, and other custom applications to Databricks compute — specifically, to classic compute (interactive clusters). This page focuses on using Databricks Connect with classic compute clusters; for serverless compute, see [Databricks Connect with Serverless Compute](/concepts/databricks-connect-with-serverless-compute.md).^[databricks-connect-for-python-databricks-on-aws.md]

## What is Databricks Connect with Classic Compute?

Databricks Connect with classic compute allows you to run PySpark code from a local development environment (e.g., a Python script in PyCharm or a Jupyter notebook running on your local machine) on a Databricks classic compute cluster rather than on a serverless compute resource. The client sends Spark jobs to the remote cluster, which executes them and returns results. This approach is suitable when you have an existing Databricks classic compute cluster or when your workload requires the full set of libraries and configurations available on a cluster.^[databricks-connect-for-python-databricks-on-aws.md]

## Requirements

To use Databricks Connect with classic compute, you need:
- **A Databricks workspace.** You must have a workspace on AWS that is enabled for classic compute (not serverless-only).
- **A classic compute cluster.** The cluster must be running a Databricks Runtime version that is compatible with your Databricks Connect package version. See [Databricks Connect Version Compatibility](/concepts/databricks-connect-version-compatibility.md) for exact mappings.
- **A local Python environment.** The local machine must have a compatible Python version — see [Databricks Connect Requirements](/concepts/databricks-connect-requirements.md) for details.
- **The `databricks-connect` package installed.** Run `pip install databricks-connect` in your local Python environment. The package version must match the cluster's Databricks Runtime version; see Install Databricks Connect for instructions.

## How to Connect

After installing the package, you configure the connection by providing your Databricks workspace URL, an access token (or personal access token), and the cluster ID of the target classic compute cluster. You set these values using the `databricks-connect` CLI command:

```bash
databricks-connect configure
```

This command prompts for the workspace URL, the token, and the cluster ID. Once configured, any `from databricks.connect import DatabricksSession` call in your local Python code creates a Spark session that runs on the specified classic compute cluster.^[databricks-connect-for-python-databricks-on-aws.md]

## Tutorials

For step-by-step walkthroughs, see:

- Tutorial: Run code from PyCharm on classic compute — a detailed guide for PyCharm users.
- Tutorial: Run Python code on serverless compute — this tutorial covers the serverless path; the classic compute equivalent is covered in the PyCharm tutorial.

## Supported IDEs and Applications

Databricks Connect with classic compute supports:
- **PyCharm** (see the tutorial above).
- **Jupyter Notebooks** running locally.
- **VS Code** (via Python extension).
- **Custom Python scripts** executed from the command line or from CI/CD pipelines.
- **The Spark shell** — you can start a local Spark shell that connects to the remote cluster using `databricks-connect shell`.^[databricks-connect-for-python-databricks-on-aws.md]

## Limitations

- **No support for serverless endpoints.** When you target a classic compute cluster, you cannot connect to serverless compute resources. If you need serverless, use the [Databricks Connect with Serverless Compute](/concepts/databricks-connect-with-serverless-compute.md) path.
- **Cluster must be running.** The classic compute cluster must be in the "Running" state for your local code to connect. If the cluster is stopped, the connection fails.
- **No Databricks Runtime version downgrade.** The client-version compatibility is fixed — see the version compatibility matrix for allowed combinations.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — the general parent concept
- [Databricks Connect with Serverless Compute](/concepts/databricks-connect-with-serverless-compute.md) — the alternative for serverless workspaces
- [Databricks Connect Requirements](/concepts/databricks-connect-requirements.md) — detailed system requirements
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — the Scala variant
- [Databricks Connect for R](/concepts/databricks-connect-for-r.md) — the R variant
- [Troubleshoot Databricks Connect](/concepts/databricks-connect.md) — common connection issues

## Sources

- databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-connect-for-python-databricks-on-aws.md](/references/databricks-connect-for-python-databricks-on-aws-669513ea.md)
