---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 00550da7985dc071bfc334c42344a257f575b46f2cb3a02fee6beb4f07fbf069
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databrickssession-builder-configuration-methods
    - DBCM
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
title: DatabricksSession Builder Configuration Methods
description: The DatabricksSession class provides builder methods (remote(), profile(), sdkConfig(), serverless(), getOrCreate()) to configure connections to Databricks compute.
tags:
  - databricks
  - api
  - databricks-connect
timestamp: "2026-06-19T14:20:26.664Z"
---

# [DatabricksSession](/concepts/databrickssession.md) Builder Configuration Methods

**DatabricksSession Builder Configuration Methods** describes the various ways to configure a connection between [Databricks Connect](/concepts/databricks-connect.md) and a Databricks compute resource — either a cluster or [serverless compute](/concepts/serverless-gpu-compute.md) — using the `DatabricksSession.builder` API. This page covers the supported configuration options, their priority order, and best practices for each approach.

## Overview

Databricks Connect enables connection from popular IDEs (Visual Studio Code, PyCharm, RStudio Desktop, IntelliJ IDEA), notebook servers, and custom applications to Databricks clusters or serverless compute. The `DatabricksSession.builder` API provides the primary interface for establishing this connection programmatically.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

The builder searches for configuration properties in a defined priority order, using the first configuration it finds. This allows flexible setup through code, environment variables, or configuration files.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Configuration Priority Order

Databricks Connect resolves configuration properties in the following order:^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

1. The `DatabricksSession` class's `remote()` method
2. A [Databricks configuration profile](/concepts/databricks-configuration-profiles.md)
3. The `DATABRICKS_CONFIG_PROFILE` environment variable
4. An environment variable for each configuration property
5. A Databricks configuration profile named `DEFAULT`

## Connecting to a Cluster

### Using the `remote()` Method

The `remote()` method supports [personal access token (PAT) authentication](/concepts/databricks-personal-access-token-pat-authentication.md) only. You specify the workspace instance name, token, and cluster ID directly:^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.remote(
    host       = f"https://{workspace_instance_name}",
    token      = pat_token,
    cluster_id = cluster_id
).getOrCreate()
```

You can also pass a Databricks SDK Config object using `.sdkConfig()`:^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
from databricks.sdk.core import Config

config = Config(
    host       = f"https://{workspace_instance_name}",
    token      = pat_token,
    cluster_id = cluster_id
)
spark = [[databrickssession|DatabricksSession]].builder.sdkConfig(config).getOrCreate()
```

### Using a Configuration Profile

Create or identify a [configuration profile](/concepts/databricks-configuration-profiles.md) containing the `cluster_id` field along with any authentication-required fields. Then reference the profile by name:^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.profile("<profile-name>").getOrCreate()
```

Required fields per authentication type:^[compute-configuration-for-databricks-connect-databricks-on-aws.md]
- **PAT authentication**: `host`, `token`
- **[OAuth M2M authentication](/concepts/machine-to-machine-m2m-authentication.md)**: `host`, `client_id`, `client_secret`
- **[OAuth U2M authentication](/concepts/user-to-machine-u2m-authentication.md)**: `host`

You can also combine a profile with a separate `cluster_id`:^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
config = Config(profile="<profile-name>", cluster_id=retrieve_cluster_id())
spark = [[databrickssession|DatabricksSession]].builder.sdkConfig(config).getOrCreate()
```

### Using the `DATABRICKS_CONFIG_PROFILE` Environment Variable

Set the `DATABRICKS_CONFIG_PROFILE` environment variable to a profile name that includes the `cluster_id` field. Then initialize without arguments:^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

### Using Individual Environment Variables

Set environment variables for each required property (e.g., `DATABRICKS_HOST`, `DATABRICKS_TOKEN`, `DATABRICKS_CLUSTER_ID`) and use the no-argument builder:^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

### Using the `DEFAULT` Configuration Profile

A profile named `DEFAULT` in the configuration file is used as a fallback when no other configuration is specified:^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

## Connecting to Serverless Compute

Databricks Connect for Python and Scala supports connecting to serverless compute when version requirements are met.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Using the `.serverless()` Method

The most straightforward approach is to call `.serverless()` on the builder:^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.serverless().getOrCreate()
```

### Using `remote()` with `serverless=True`

You can also pass the `serverless` parameter to `remote()`:^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.remote(serverless=True).getOrCreate()
```

### Using Environment or Profile Configuration

Set the `DATABRICKS_SERVERLESS_COMPUTE_ID` environment variable to `auto` — this causes Databricks Connect to ignore any `cluster_id` setting:^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```
export DATABRICKS_SERVERLESS_COMPUTE_ID=auto
```

Alternatively, add `serverless_compute_id = auto` to a configuration profile:^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```
[DEFAULT]
host = https://my-workspace.cloud.databricks.com
serverless_compute_id = auto
token = dapi123...
```

## Validation Methods

### `databricks-connect test`

Run the `databricks-connect test` command to validate environment, default credentials, and compute connection. The command fails with a non-zero exit code when it detects incompatibility.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### `validateSession()`

In Databricks Connect 14.3 and above, call `validateSession()` on the builder:^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
[[databrickssession|DatabricksSession]].builder.validateSession(True).getOrCreate()
```

## Disabling Databricks Connect

The Databricks Connect service (and underlying [Spark Connect](/concepts/spark-connect.md)) can be disabled on any cluster by setting the following Spark configuration:^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```
spark.databricks.service.server.enabled false
```

## Best Practices

- **Use environment variables or configuration profiles** for connection properties rather than hardcoding them in code. This enables different configurations for different environments without code changes.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]
- **Avoid mixing `cluster_id` and `serverless_compute_id` settings** — if `DATABRICKS_SERVERLESS_COMPUTE_ID` is set to `auto`, the `cluster_id` is ignored.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]
- **Use the `auth login` command's `--configure-cluster` option** to automatically add the `cluster_id` field to a configuration profile. See `databricks auth login -h` for details.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md)
- [Databricks Session](/concepts/databrickssession.md)
- [Configuration profiles](/concepts/databricks-configuration-profiles.md)
- [Authentication types](/concepts/databricks-authentication-type.md)
- [Serverless compute](/concepts/serverless-gpu-compute.md)
- [Spark Connect](/concepts/spark-connect.md)
- Workspace instance name

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
