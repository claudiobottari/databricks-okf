---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b8fc761cf2652b008ea7326398b4fbb39ffdd00c0aebd69d248bc12ad8bda85a
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cluster-id-configuration-in-databricks-connect
    - CICIDC
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
title: Cluster ID configuration in Databricks Connect
description: Methods for specifying cluster_id when connecting to classic compute, including inline, in config profiles, or via DATABRICKS_CLUSTER_ID environment variable.
tags:
  - databricks
  - configuration
  - cluster
timestamp: "2026-06-19T09:21:04.937Z"
---

# Cluster ID Configuration in Databricks Connect

**Cluster ID configuration in Databricks Connect** refers to the methods and requirements for specifying which Databricks cluster a local IDE or custom application connects to via [Databricks Connect](/concepts/databricks-connect.md). The cluster ID (`cluster_id`) tells Databricks Connect which remote compute resource should execute Spark workloads sent from the local environment.

## Overview

When using Databricks Connect with classic clusters (as opposed to [serverless compute](/concepts/serverless-gpu-compute.md)), the `cluster_id` must be provided as part of the connection configuration. Databricks Connect searches for configuration properties in a specific order — methods earlier in the search order take precedence.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

Databricks recommends configuring connection properties through environment variables or configuration files rather than hardcoding credentials in source code.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Providing the Cluster ID

### Via the `DatabricksSession.remote()` Method

You can pass the `cluster_id` directly in code using `DatabricksSession.builder.remote()`. The cluster ID must be provided explicitly unless the `DATABRICKS_CLUSTER_ID` environment variable is already set. This method supports only [Databricks personal access token authentication](/concepts/databricks-personal-access-token-pat-authentication.md).^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.remote(
    host       = "https://<workspace-instance-name>",
    token      = "<personal-access-token>",
    cluster_id = "<cluster-id>"
).getOrCreate()
```

### Via a Databricks Configuration Profile

A [Databricks configuration profile](/concepts/databricks-configuration-profiles.md) can include the `cluster_id` field alongside authentication fields. The profile name is then passed to `DatabricksSession.builder.profile()`. The `cluster_id` can be embedded in the profile or specified separately.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

The `databricks auth login` command's `--configure-cluster` option automatically adds the `cluster_id` field to a new or existing configuration profile.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

# When cluster_id is in the profile:
spark = [[databrickssession|DatabricksSession]].builder.profile("<profile-name>").getOrCreate()

# When cluster_id is provided separately:
from databricks.sdk.core import Config

config = Config(profile="<profile-name>", cluster_id="<cluster-id>")
spark = [[databrickssession|DatabricksSession]].builder.sdkConfig(config).getOrCreate()
```

### Via Environment Variables

Set the `DATABRICKS_CLUSTER_ID` environment variable along with authentication-related environment variables. Databricks Connect reads these variables automatically. The required authentication environment variables depend on the [DATABRICKS Authentication Type](/concepts/databricks-authentication-type.md).^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

# Requires DATABRICKS_CLUSTER_ID, DATABRICKS_HOST, and DATABRICKS_TOKEN
# (or other auth variables) to be set in the environment.
spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

### Via the `DEFAULT` Configuration Profile

A configuration profile named `DEFAULT` that includes the `cluster_id` field is automatically discovered by Databricks Connect. No explicit profile name needs to be specified in code.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Serverless Compute (No Cluster ID)

When connecting to [serverless compute](/concepts/serverless-gpu-compute.md), the `cluster_id` is **not** used. Instead, set `serverless_compute_id = auto` in a configuration profile or the environment variable `DATABRICKS_SERVERLESS_COMPUTE_ID = auto`. You can also use `DatabricksSession.builder.serverless()` or `DatabricksSession.builder.remote(serverless=True)`. If `DATABRICKS_SERVERLESS_COMPUTE_ID` is set, Databricks Connect ignores the `cluster_id`.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Configuration Search Order

Databricks Connect applies configuration from the first source it finds, in this order:

1. The `DatabricksSession` class's `remote()` method
2. A Databricks configuration profile specified by name in code
3. The `DATABRICKS_CONFIG_PROFILE` environment variable
4. Individual environment variables for each property
5. A Databricks configuration profile named `DEFAULT`

If `DATABRICKS_CLUSTER_ID` is already set as an environment variable, it can be used as a fallback even when other configuration methods are employed.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Retrieving the Cluster ID

The cluster ID can be found in the Databricks workspace UI from the cluster's URL. See Compute resource URL and ID for details.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks authentication types](/concepts/databricks-authentication-type.md) — Required alongside `cluster_id` for connection
- [Databricks Configuration Profiles](/concepts/databricks-configuration-profiles.md) — Centralized credential management
- [Serverless compute in Databricks](/concepts/serverless-gpu-compute-on-databricks.md) — Alternative compute that does not require a cluster ID
- [Databricks Connect versions](/concepts/databricks-connect.md) — Compatibility requirements
- [DatabricksSession API](/concepts/databrickssession.md) — Core entry point for Databricks Connect

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
