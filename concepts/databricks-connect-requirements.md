---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4fabdbbf93983df9e86f991941f4bf96cbd627524fbd53ad408982c647fc78b2
  pageDirectory: concepts
  sources:
    - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-requirements
    - DCR
    - Databricks Connect Version Requirements
    - Databricks Connect for Python requirements
    - Databricks Connect versions|supported version
  citations:
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
title: Databricks Connect Requirements
description: Supported Databricks Runtime versions (7.3 LTS through 12.2 LTS), matching Python minor versions, matching databricks-connect package versions, and JRE 8.
tags:
  - configuration
  - requirements
  - compatibility
timestamp: "2026-06-19T09:47:47.765Z"
---

# Databricks Connect Requirements

**Databricks Connect** is a client library that allows you to connect popular IDEs (such as Visual Studio Code and PyCharm), notebook servers, and other custom applications to Databricks clusters. It enables you to write jobs using Spark APIs and run them remotely on a Databricks cluster instead of in a local Spark session. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Supported Databricks Runtime Versions

Databricks Connect supports only the following Databricks Runtime versions:

- Databricks Runtime 12.2 LTS ML, Databricks Runtime 12.2 LTS
- Databricks Runtime 11.3 LTS ML, Databricks Runtime 11.3 LTS
- Databricks Runtime 10.4 LTS ML, Databricks Runtime 10.4 LTS
- Databricks Runtime 9.1 LTS ML, Databricks Runtime 9.1 LTS
- Databricks Runtime 7.3 LTS

## Python Version Requirements

You must install Python 3 on your development machine, and the **minor version** of your client Python installation must match the minor Python version of your Databricks cluster. For example, if your cluster runs Python 3.9, your local environment must also use Python 3.9. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

Databricks strongly recommends using a Python **virtual environment** activated for each Python version used with Databricks Connect. This helps ensure you are using the correct versions of Python and Databricks Connect together and reduces time spent resolving technical issues. Supported virtual environment tools include [venv](https://docs.python.org/3/library/venv.html) and [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Package Version Requirements

The Databricks Connect major and minor package version **must always match** your Databricks Runtime version. Databricks recommends using the most recent package of Databricks Connect that matches your Databricks Runtime version. For example, when using a Databricks Runtime 12.2 LTS cluster, you must use the `databricks-connect==12.2.*` package. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Java Requirements

A Java Runtime Environment (JRE) 8 is required. The client has been tested with the OpenJDK 8 JRE. The client **does not** support Java 11. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## PySpark Conflict Warning

The `databricks-connect` package conflicts with PySpark. If PySpark is already installed in your Python environment, you must uninstall it before installing Databricks Connect. Having both installed will cause errors when initializing the Spark context in Python, which can manifest as "stream corrupted" or "class not found" errors. After uninstalling PySpark, fully re-install the Databricks Connect package. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Configuration Requirements

To connect to a Databricks cluster, you need the following configuration properties:

- The Databricks workspace URL
- A Databricks [personal access token](/concepts/databricks-personal-access-token-pat-authentication.md)
- The cluster ID (obtainable from the cluster URL)
- The port for the connection (default is `15001`)

These can be configured via the CLI, SQL configs, or environment variables. The precedence of configuration methods from highest to lowest is: SQL config keys, CLI, and environment variables. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Cluster Configuration Requirements

The cluster must have the Spark server enabled with `spark.databricks.service.server.enabled true`. This is enabled by default on supported cluster versions. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect Overview](/concepts/databricks-connect.md)
- [Databricks Connect Troubleshooting](/concepts/databricks-connect-troubleshooting.md)
- [Databricks Connect Limitations](/concepts/databricks-connect-limitations.md)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- [Personal Access Tokens](/concepts/databricks-personal-access-token-pat-authentication.md)

## Sources

- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md

# Citations

1. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)
