---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9ea2f109469533eed44e34fbda36fff4aba36ca2246a66ee9ee0456d98ef15f8
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-configuration-profiles
    - DCCP
    - Databricks Connect configuration files
    - Databricks Connection Profiles
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
title: Databricks Connect Configuration Profiles
description: Using .databrickscfg configuration profiles (including DEFAULT) to store connection properties like host, token, cluster_id, and serverless_compute_id.
tags:
  - databricks-connect
  - configuration
  - profiles
  - authentication
timestamp: "2026-06-19T17:48:19.860Z"
---

# Databricks Connect Configuration Profiles

**Databricks Connect Configuration Profiles** are named sets of connection properties stored in a local configuration file that allow [Databricks Connect](/concepts/databricks-connect.md) to authenticate and connect to a Databricks cluster or serverless compute resource. They provide a reusable, secure way to manage connection settings without hardcoding credentials in code.

## Overview

Databricks Connect enables you to connect popular IDEs such as Visual Studio Code, PyCharm, RStudio Desktop, IntelliJ IDEA, notebook servers, and other custom applications to Databricks clusters. Configuration profiles simplify the setup by storing connection parameters in a single location. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Configuration Profile Fields

A configuration profile must contain the `cluster_id` field (for classic compute connections) or `serverless_compute_id` field (for serverless compute connections), along with authentication-specific fields. The required fields depend on the authentication type: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

- **Personal access token authentication**: `host` and `token`
- **OAuth machine-to-machine (M2M) authentication**: `host`, `client_id`, and `client_secret`
- **OAuth user-to-machine (U2M) authentication**: `host`

## Configuration Search Order

Databricks Connect searches for configuration properties in the following order and uses the first configuration it finds: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

1. The `DatabricksSession` class's `remote()` method
2. A Databricks configuration profile specified in code
3. The `DATABRICKS_CONFIG_PROFILE` environment variable
4. Individual environment variables for each configuration property
5. A Databricks configuration profile named `DEFAULT`

## Using Configuration Profiles

### Specifying a Profile in Code

You can reference a configuration profile directly when creating a `DatabricksSession`: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.profile("<profile-name>").getOrCreate()
```

### Using the `DATABRICKS_CONFIG_PROFILE` Environment Variable

Set the `DATABRICKS_CONFIG_PROFILE` environment variable to the name of your configuration profile, then initialize the session without specifying the profile in code: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

### Using the `DEFAULT` Profile

If you name your configuration profile `DEFAULT`, Databricks Connect automatically uses it without any additional configuration: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

## Serverless Compute Configuration

For serverless compute connections, you can configure a profile with `serverless_compute_id = auto`: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```ini
[DEFAULT]
host = https://my-workspace.cloud.databricks.com
serverless_compute_id = auto
token = dapi123...
```

Alternatively, you can use the `serverless()` method or set `serverless=True` in the `remote()` method: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

# Using serverless() method
spark = [[databrickssession|DatabricksSession]].builder.serverless().getOrCreate()

# Using remote() with serverless=True
spark = [[databrickssession|DatabricksSession]].builder.remote(serverless=True).getOrCreate()
```

## Automatic Cluster ID Configuration

You can use the `databricks auth login` command with the `--configure-cluster` option to automatically add the `cluster_id` field to a new or existing configuration profile. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Environment Variable Override

If the `DATABRICKS_CLUSTER_ID` environment variable is set, it overrides the `cluster_id` field in configuration profiles. This allows you to use the same profile with different clusters without modifying the profile file. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that uses these configuration profiles
- Databricks Authentication — Authentication types supported by configuration profiles
- [DatabricksSession](/concepts/databrickssession.md) — The main entry point for Databricks Connect
- Serverless Compute — Compute resource type that can be configured via profiles
- Cluster Configuration — Classic compute resource configuration

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
