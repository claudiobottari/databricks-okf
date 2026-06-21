---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6a286cfdb33bc6c4ff3bcaede1e0e28e2ea80d198fbd1777c08599bdfb863d92
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - environment-variable-configuration-for-databricks-connect
    - EVCFDC
    - Environment Variables for Databricks Connect
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
title: Environment Variable Configuration for Databricks Connect
description: Using environment variables such as DATABRICKS_CLUSTER_ID, DATABRICKS_HOST, DATABRICKS_TOKEN, etc. to configure Databricks Connect without code changes.
tags:
  - configuration
  - environment-variables
  - databricks-connect
timestamp: "2026-06-18T14:41:02.009Z"
---

# Environment Variable Configuration for Databricks Connect

**Environment Variable Configuration for Databricks Connect** refers to the method of configuring a connection between [Databricks Connect](/concepts/databricks-connect.md) and a Databricks cluster or [serverless compute](/concepts/serverless-gpu-compute.md) by setting environment variables. This approach is one of several configuration options, and Databricks Connect searches for configuration properties in a specific order, using the first configuration it finds. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Overview

When connecting Databricks Connect to a cluster or serverless compute, environment variables provide a way to configure the connection without hardcoding credentials or cluster IDs in application code. Databricks Connect searches for configuration properties in the following order, using the first configuration it finds:

1. The `DatabricksSession` class's `remote()` method
2. A [Databricks configuration profile](/concepts/databricks-configuration-profiles.md)
3. The `DATABRICKS_CONFIG_PROFILE` environment variable
4. An environment variable for each configuration property
5. A Databricks configuration profile named `DEFAULT`

^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Configuring with Individual Environment Variables

To configure a connection using individual environment variables, set the `DATABRICKS_CLUSTER_ID` environment variable along with any other environment variables required for the chosen [DATABRICKS Authentication Type](/concepts/databricks-authentication-type.md). ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Required Environment Variables by Authentication Type

The required environment variables vary depending on the authentication method: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

- **[Personal access token authentication](/concepts/databricks-personal-access-token-pat-authentication.md) (legacy)**: `DATABRICKS_HOST` and `DATABRICKS_TOKEN`
- **[OAuth machine-to-machine (M2M) authentication](/concepts/machine-to-machine-m2m-authentication.md)**: `DATABRICKS_HOST`, `DATABRICKS_CLIENT_ID`, and `DATABRICKS_CLIENT_SECRET`
- **[OAuth user-to-machine (U2M) authentication](/concepts/user-to-machine-u2m-authentication.md)**: `DATABRICKS_HOST`

After setting these environment variables, initialize the `DatabricksSession` class without passing any parameters: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

### Serverless Compute Configuration

To connect to serverless compute using environment variables, set the `DATABRICKS_SERVERLESS_COMPUTE_ID` environment variable to `auto`. When this environment variable is set, Databricks Connect ignores the `cluster_id` setting. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Configuring with `DATABRICKS_CONFIG_PROFILE`

As an alternative to setting individual environment variables, you can set the `DATABRICKS_CONFIG_PROFILE` environment variable to the name of a [Databricks configuration profile](/concepts/databricks-configuration-profiles.md). This profile must contain the `cluster_id` field and any other fields required for the chosen authentication type. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

If you have already set the `DATABRICKS_CLUSTER_ID` environment variable, you do not also need to specify `cluster_id` in the profile. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

When `DATABRICKS_CONFIG_PROFILE` is set, you can initialize `DatabricksSession` without parameters: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

## Using the `auth login` Command

The `databricks auth login` command's `--configure-cluster` option can automatically add the `cluster_id` field to a new or existing configuration profile, simplifying the setup process. For more information, run `databricks auth login -h`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Configuration Profile for Serverless

For serverless compute connections via a configuration profile, set `serverless_compute_id = auto` in the profile alongside the `host` and `token` fields: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```ini
[DEFAULT]
host = https://my-workspace.cloud.databricks.com
serverless_compute_id = auto
token = dapi123...
```

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library for connecting IDEs and applications to Databricks compute
- [Databricks configuration profile](/concepts/databricks-configuration-profiles.md) — File-based configuration for Databricks tools
- [Databricks authentication types](/concepts/databricks-authentication-type.md) — Available methods for authenticating to Databricks
- [Serverless compute](/concepts/serverless-gpu-compute.md) — On-demand compute for Databricks workloads
- [DatabricksSession](/concepts/databrickssession.md) — The main entry point for using Databricks Connect
- [Databricks personal access token authentication](/concepts/databricks-personal-access-token-pat-authentication.md) — Legacy authentication method
- [OAuth machine-to-machine authentication](/concepts/machine-to-machine-m2m-authentication.md) — OAuth M2M authentication for Databricks
- [OAuth user-to-machine authentication](/concepts/user-to-machine-u2m-authentication.md) — OAuth U2M authentication for Databricks

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
