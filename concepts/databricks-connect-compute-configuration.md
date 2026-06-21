---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4a52fa227e36116ee7b064df058c070a0551b1d0128a77b9b32f72a63cd57123
  pageDirectory: concepts
  sources:
    - databricks-connect-for-python-databricks-on-aws.md
    - databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.7
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-connect-compute-configuration
    - DCCC
    - Databricks Connect cluster configuration
    - Databricks clusters|Compute configuration
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
    - file: databricks-connect-for-python-databricks-on-aws.md
    - file: databricks-connect-for-scala-databricks-on-aws.md
title: Databricks Connect compute configuration
description: Configuration options for classic compute and serverless compute when using Databricks Connect.
tags:
  - databricks
  - compute
  - configuration
timestamp: "2026-06-19T18:09:58.353Z"
---

# Databricks Connect Compute Configuration

**Databricks Connect Compute Configuration** refers to the settings and requirements for connecting a local development environment—such as an IDE, notebook server, or custom application—to a Databricks compute resource for executing Spark code. Proper compute configuration is a prerequisite for using [Databricks Connect](/concepts/databricks-connect.md). ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Overview

Databricks Connect works by sending Spark commands from a local client to a remote Databricks compute target. The compute must be a Databricks-managed resource—either a classic cluster or a serverless compute endpoint. Configuration details, including how to specify the workspace instance name, cluster ID, and authentication, are documented on the official configuration page. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Prerequisites

Before you begin, you need the following:

- **Databricks Connect installed**. For installation requirements, see the Databricks Connect usage requirements documentation. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]
- **Workspace instance name** (Server Hostname). This is the URL of your Databricks workspace. See the documentation on getting connection details for a Databricks compute resource. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]
- **Cluster ID** (for classic compute). You can retrieve the cluster ID from the URL of the cluster in the Databricks workspace UI. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Configuration Methods

Databricks Connect searches for configuration properties in the following order, and uses the first configuration it finds: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

1. **The `DatabricksSession` class's `remote()` method** — Applies to personal access token (PAT) authentication only. You can specify `host`, `token`, and `cluster_id` directly in code. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]
2. **A Databricks configuration profile** — Create a profile with `cluster_id` and other fields needed for your authentication type (PAT, OAuth M2M, or OAuth U2M). ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]
3. **The `DATABRICKS_CONFIG_PROFILE` environment variable** — Set this variable to the name of a configuration profile, then initialize `DatabricksSession`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]
4. **An environment variable for each configuration property** — Set `DATABRICKS_CLUSTER_ID` and other variables (e.g., `DATABRICKS_HOST`, `DATABRICKS_TOKEN`) for your authentication type. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]
5. **A Databricks configuration profile named `DEFAULT`** — Create a profile named `DEFAULT` with `cluster_id` and other required fields. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Configuration Profile Requirements

The required fields in a Databricks configuration profile depend on the authentication type:

- **Personal access token (PAT)**: `host` and `token` ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]
- **OAuth machine-to-machine (M2M)**: `host`, `client_id`, and `client_secret` ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]
- **OAuth user-to-machine (U2M)**: `host` ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

Note: You can use the `auth login` command's `--configure-cluster` option to automatically add the `cluster_id` field to a new or existing configuration profile. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Serverless Compute Configuration

For connecting to [serverless compute](/concepts/serverless-gpu-compute.md):

- **Python**: Set the environment variable `DATABRICKS_SERVERLESS_COMPUTE_ID` to `auto`, or set `serverless_compute_id = auto` in a configuration profile. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]
- **Python or Scala**: Use `DatabricksSession.builder.serverless().getOrCreate()` or `DatabricksSession.builder.remote(serverless=True).getOrCreate()`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

Note: When `DATABRICKS_SERVERLESS_COMPUTE_ID` is set, Databricks Connect ignores the `cluster_id` setting. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Connection Validation

To validate that your environment, default credentials, and connection to compute are correctly set up, run the `databricks-connect test` command. This command fails with a non-zero exit code and a corresponding error message when it detects any incompatibility. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

In Databricks Connect 14.3 and above, you can also validate your environment using `validateSession()`:

```python
[[databrickssession|DatabricksSession]].builder.validateSession(True).getOrCreate()
```

^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Disabling Databricks Connect

Databricks Connect (and the underlying Spark Connect) services can be disabled on any given cluster by setting the following Spark configuration:

```
spark.databricks.service.server.enabled false
```

^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Related Documentation

- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — Get-started guide with platform-specific setup. ^[databricks-connect-for-python-databricks-on-aws.md]
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — Get-started guide for Scala and JVM-based development. ^[databricks-connect-for-scala-databricks-on-aws.md]
- [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md) — Version compatibility and environment requirements. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Related Concepts

- Databricks Clusters — Classic compute resource for running Spark workloads.
- Serverless Compute on Databricks — On-demand compute without cluster management.
- [Databricks authentication types](/concepts/databricks-authentication-type.md) — PAT, OAuth M2M, and OAuth U2M authentication methods.

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md
- databricks-connect-for-python-databricks-on-aws.md
- databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
2. [databricks-connect-for-python-databricks-on-aws.md](/references/databricks-connect-for-python-databricks-on-aws-669513ea.md)
3. [databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-connect-for-scala-databricks-on-aws-9156fcdc.md)
