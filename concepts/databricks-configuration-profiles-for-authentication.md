---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a516a2f49533353ac702f0d17d207b66aee71674f9e130ace9f8b6a5ae67067e
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-configuration-profiles-for-authentication
    - DCPFA
    - Configuration profiles for Databricks authentication
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
title: Databricks configuration profiles for authentication
description: Using profiles (in .databrickscfg) to store authentication fields (host, token, client_id, client_secret) and cluster_id for Databricks Connect connections.
tags:
  - databricks
  - authentication
  - configuration
timestamp: "2026-06-19T09:19:59.529Z"
---

# Databricks Configuration Profiles for Authentication

**Databricks configuration profiles** are named sets of authentication and connection parameters stored in a local configuration file. They allow tools like [Databricks Connect](/concepts/databricks-connect.md) and the Databricks SDK to authenticate to a Databricks workspace without hardcoding credentials in code or environment variables. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Overview

A configuration profile is a section in a `.databrickscfg` file that contains key-value pairs for authentication fields such as `host`, `token`, `client_id`, and `client_secret`. Profiles are identified by a name enclosed in square brackets, with the special name `DEFAULT` serving as the fallback when no other profile is specified. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Profile Structure

Each profile contains the fields required by the chosen [DATABRICKS Authentication Type](/concepts/databricks-authentication-type.md). The required fields vary by authentication method: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

- **Personal access token (PAT) authentication**: `host` and `token`
- **OAuth machine-to-machine (M2M) authentication**: `host`, `client_id`, and `client_secret`
- **OAuth user-to-machine (U2M) authentication**: `host`

For Databricks Connect, profiles can also include a `cluster_id` field to specify which cluster to connect to, or `serverless_compute_id = auto` to connect to [serverless compute](/concepts/serverless-gpu-compute.md). ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Example Profile

```ini
[DEFAULT]
host = https://my-workspace.cloud.databricks.com
token = dapi123...
cluster_id = 1234-567890-abcd1234
```

```ini
[my-serverless-profile]
host = https://my-workspace.cloud.databricks.com
token = dapi123...
serverless_compute_id = auto
```

## Configuration Search Order

When Databricks Connect initializes a session, it searches for configuration in the following order and uses the first match found: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

1. The `DatabricksSession` class's `remote()` method with explicit parameters
2. A named configuration profile specified via the `profile()` method
3. The profile named by the `DATABRICKS_CONFIG_PROFILE` environment variable
4. Individual environment variables for each configuration property (e.g., `DATABRICKS_HOST`, `DATABRICKS_TOKEN`)
5. A configuration profile named `DEFAULT`

## Using Profiles with Databricks Connect

### Specifying a Profile in Code

You can reference a profile directly when creating a `DatabricksSession`: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.profile("<profile-name>").getOrCreate()
```

### Using the DATABRICKS_CONFIG_PROFILE Environment Variable

Set the `DATABRICKS_CONFIG_PROFILE` environment variable to the profile name, then initialize the session without explicit parameters: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

### Using the DEFAULT Profile

If no profile is specified and no environment variables are set, Databricks Connect looks for a profile named `DEFAULT`: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

### Combining Profile with Cluster ID

You can specify a profile and override the `cluster_id` separately: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
from databricks.sdk.core import Config

config = Config(
    profile = "<profile-name>",
    cluster_id = retrieve_cluster_id()
)
spark = [[databrickssession|DatabricksSession]].builder.sdkConfig(config).getOrCreate()
```

## Using Profiles with the Databricks CLI

The `databricks auth login` command supports a `--configure-cluster` option that automatically adds the `cluster_id` field to a new or existing configuration profile. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Best Practices

- **Use profiles instead of hardcoded credentials** to keep authentication details out of source code and notebooks. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]
- **Name profiles descriptively** (e.g., `dev-workspace`, `prod-workspace`) to distinguish between different environments. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]
- **Use the DEFAULT profile** for your primary workspace to simplify code that doesn't need to switch between environments. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]
- **Store configuration files securely** and avoid committing them to version control. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks authentication types](/concepts/databricks-authentication-type.md) — The supported authentication methods for profiles
- [Databricks Connect](/concepts/databricks-connect.md) — The primary consumer of configuration profiles
- [Databricks SDK authentication](/concepts/databricks-sdk-authentication-methods.md) — How the SDK resolves credentials
- [Environment variables for Databricks authentication](/concepts/environment-variables-for-databricks-connect-authentication.md) — Alternative to configuration profiles
- [Serverless compute](/concepts/serverless-gpu-compute.md) — Compute type that uses `serverless_compute_id` instead of `cluster_id`

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
