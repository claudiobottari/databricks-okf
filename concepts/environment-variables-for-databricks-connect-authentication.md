---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 025383f5317458ad94b38b434cdd9b506d5fa48b9e588eae52d35b70ebc5c36a
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - environment-variables-for-databricks-connect-authentication
    - EVFDCA
    - Environment Variables for Databricks Connect
    - Environment variables for Databricks Connect
    - Environment variables for Databricks authentication
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
title: Environment variables for Databricks Connect authentication
description: Using environment variables (DATABRICKS_HOST, DATABRICKS_TOKEN, DATABRICKS_CLIENT_ID, DATABRICKS_CLIENT_SECRET, DATABRICKS_CLUSTER_ID) to configure connections without code-level config.
tags:
  - databricks
  - environment-variables
  - authentication
timestamp: "2026-06-19T09:20:45.010Z"
---

Here is the wiki page for "Environment variables for Databricks Connect authentication".

---

## Environment variables for Databricks Connect authentication

Using **environment variables** is one of the ways to configure a connection between [Databricks Connect](/concepts/databricks-connect.md) and a Databricks cluster or [serverless compute](/concepts/serverless-gpu-compute.md). Databricks Connect searches for configuration properties in a specific order and uses the first configuration it finds; environment variables are one of those supported options. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Per-property environment variables

For this option, you set the `DATABRICKS_CLUSTER_ID` environment variable and any other variables required by the [DATABRICKS Authentication Type](/concepts/databricks-authentication-type.md) you intend to use. If `DATABRICKS_CLUSTER_ID` is set, you do not need to specify `cluster_id` in your code. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

The required environment variables for each authentication type are:

| Authentication type | Required environment variables |
|---|---|
| [Personal access token authentication](/concepts/databricks-personal-access-token-pat-authentication.md) | `DATABRICKS_HOST`, `DATABRICKS_TOKEN` |
| [OAuth machine-to-machine (M2M) authentication](/concepts/machine-to-machine-m2m-authentication.md) | `DATABRICKS_HOST`, `DATABRICKS_CLIENT_ID`, `DATABRICKS_CLIENT_SECRET` |
| [OAuth user-to-machine (U2M) authentication](/concepts/user-to-machine-u2m-authentication.md) | `DATABRICKS_HOST` |

After setting the environment variables, initialize the `DatabricksSession` class:

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

### `DATABRICKS_CONFIG_PROFILE` environment variable

For this option, create or identify a Databricks [configuration profile](/concepts/databricks-configuration-profiles.md) containing the field `cluster_id` and any other fields needed for your authentication type. Then set the `DATABRICKS_CONFIG_PROFILE` environment variable to the name of this configuration profile. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

If you have already set the `DATABRICKS_CLUSTER_ID` environment variable, you do not also need to specify `cluster_id`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

The required configuration profile fields for each authentication type are:
- For [personal access token authentication](/concepts/databricks-personal-access-token-pat-authentication.md): `host` and `token`.
- For [OAuth machine-to-machine (M2M) authentication](/concepts/machine-to-machine-m2m-authentication.md): `host`, `client_id`, and `client_secret`.
- For [OAuth user-to-machine (U2M) authentication](/concepts/user-to-machine-u2m-authentication.md): `host`.

You can use the `auth login` command's `--configure-cluster` option to automatically add the `cluster_id` field to a new or existing configuration profile. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### `DATABRICKS_CLUSTER_ID` environment variable

The `DATABRICKS_CLUSTER_ID` environment variable is used across multiple configuration methods. If it is set, you do not need to specify `cluster_id` in your configuration profile, in the `DatabricksSession` class, or in the `Databricks SDK Config` object. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### `DATABRICKS_SERVERLESS_COMPUTE_ID` environment variable

For [Python](/concepts/python-wheel-task.md) connections to [serverless compute](/concepts/serverless-gpu-compute.md), set the `DATABRICKS_SERVERLESS_COMPUTE_ID` environment variable to `auto`. If this environment variable is set, Databricks Connect ignores the `cluster_id`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

You can also set `serverless_compute_id = auto` in a local Databricks configuration profile, then reference that profile from your code. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
[DEFAULT]
host = https://my-workspace.cloud.databricks.com
serverless_compute_id = auto
token = dapi123...
```

### Related concepts

- [Databricks Connect](/concepts/databricks-connect.md)
- Databricks cluster
- [Serverless compute](/concepts/serverless-gpu-compute.md)
- [Configuration profiles](/concepts/databricks-configuration-profiles.md)
- [Personal access tokens](/concepts/databricks-personal-access-token-pat-authentication.md)
- [OAuth M2M authentication](/concepts/machine-to-machine-m2m-authentication.md)
- [OAuth U2M authentication](/concepts/user-to-machine-u2m-authentication.md)

### Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
