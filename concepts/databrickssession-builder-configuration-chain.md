---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d60537ab45c4507eff7f92d3387feb0f7f643d99029e2888510bc482645796f9
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databrickssession-builder-configuration-chain
    - DBCC
    - DatabricksSession configuration
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
title: DatabricksSession builder configuration chain
description: "The ordered precedence of configuration methods for DatabricksSession: remote() method, config profile, DATABRICKS_CONFIG_PROFILE env var, individual env vars, and DEFAULT profile."
tags:
  - databricks
  - api
  - configuration-pattern
timestamp: "2026-06-19T09:19:43.448Z"
---

# [DatabricksSession](/concepts/databrickssession.md) Builder Configuration Chain

**DatabricksSession builder configuration chain** refers to the ordered sequence of configuration sources that [Databricks Connect](/concepts/databricks-connect.md) searches when establishing a connection to a Databricks cluster or serverless compute. The builder uses the first configuration it finds, following a well-defined precedence. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Overview

Databricks Connect enables popular IDEs (Visual Studio Code, PyCharm, IntelliJ IDEA, etc.) and custom applications to run Spark code on a remote Databricks compute resource. The `DatabricksSession.builder` object provides a fluent API to supply connection parameters. Understanding the configuration chain helps you choose the most appropriate method for your environment and ensures that settings are picked up correctly. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Configuration Search Order

Databricks Connect searches for configuration properties in the following order and uses the **first** configuration it finds: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

1. **`DatabricksSession.builder.remote()` method** – Explicitly set `host`, `token`, and `cluster_id` (or `serverless=True`) in code.
2. **A Databricks configuration profile** – Specify a profile by name using `.profile("<name>")` or via `Config` with `profile="..."`.
3. **`DATABRICKS_CONFIG_PROFILE` environment variable** – Set the variable to the name of a profile containing `cluster_id` (if connecting to a cluster) and authentication fields.
4. **Environment variables for each property** – Set individual variables such as `DATABRICKS_HOST`, `DATABRICKS_TOKEN`, `DATABRICKS_CLUSTER_ID`.
5. **A Databricks configuration profile named `DEFAULT`** – If no other source is found, the builder falls back to a profile named `DEFAULT` in the standard credentials file.

### 1. The `remote()` Method

You can pass connection details directly to `DatabricksSession.builder.remote()`. This method accepts `host`, `token`, `cluster_id`, and a `serverless` flag. It is also possible to use the Databricks SDK’s `Config` class together with `.sdkConfig(config)` to supply a profile or explicit credentials along with `cluster_id`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.remote(
    host="https://<workspace-url>",
    token="<pat>",
    cluster_id="<cluster-id>"
).getOrCreate()
```

If you have already set the `DATABRICKS_CLUSTER_ID` environment variable, you do not need to specify `cluster_id` in the `remote()` call. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### 2. A Databricks Configuration Profile

A Databricks [configuration profile](/concepts/databricks-configuration-profiles.md) is a section in the credentials file (typically `~/.databrickscfg`) that contains authentication fields and optionally `cluster_id`. You can reference it using `.profile("<profile-name>")` or by constructing a `Config` object with the profile name. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
# Using .profile()
spark = [[databrickssession|DatabricksSession]].builder.profile("my-profile").getOrCreate()

# Using Config
config = Config(profile="my-profile", cluster_id="<cluster-id>")
spark = [[databrickssession|DatabricksSession]].builder.sdkConfig(config).getOrCreate()
```

### 3. `DATABRICKS_CONFIG_PROFILE` Environment Variable

Set the environment variable `DATABRICKS_CONFIG_PROFILE` to the name of a profile. The builder then reads all required fields from that profile (including `cluster_id` if applicable). ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```bash
export DATABRICKS_CONFIG_PROFILE=my-profile
```

Then in code:

```python
spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

### 4. Per-Property Environment Variables

You can set individual environment variables for each authentication type. For example, for PAT authentication: `DATABRICKS_HOST`, `DATABRICKS_TOKEN`, and `DATABRICKS_CLUSTER_ID`. For OAuth M2M: `DATABRICKS_HOST`, `DATABRICKS_CLIENT_ID`, `DATABRICKS_CLIENT_SECRET`, and `DATABRICKS_CLUSTER_ID`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
# After setting environment variables
spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

### 5. Default Configuration Profile

If none of the above sources are present, the builder looks for a profile named `DEFAULT` in the credentials file. This profile must contain a `cluster_id` (or be combined with the `DATABRICKS_CLUSTER_ID` environment variable) and appropriate authentication fields. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Configuration for Serverless Compute

To connect to serverless compute instead of a classic cluster, you have several options: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

- Set the environment variable `DATABRICKS_SERVERLESS_COMPUTE_ID` to `auto`. When set, Databricks Connect ignores `cluster_id`.
- In a configuration profile, set `serverless_compute_id = auto`.
- Use the `.serverless()` builder method, which is equivalent to `.remote(serverless=True)`.

```python
# Option A: builder.serverless()
spark = [[databrickssession|DatabricksSession]].builder.serverless().getOrCreate()

# Option B: builder.remote(serverless=True)
spark = [[databrickssession|DatabricksSession]].builder.remote(serverless=True).getOrCreate()
```

## Validation

After configuration, you can validate your environment with the command `databricks-connect test`, or in code (Databricks Connect 14.3+) by calling `DatabricksSession.builder.validateSession(True).getOrCreate()`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Disabling Databricks Connect

Databricks Connect (and the underlying Spark Connect) can be disabled on a cluster by setting the Spark configuration `spark.databricks.service.server.enabled false`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — Overview of the remote Spark client.
- [Databricks authentication profiles](/concepts/databricks-authentication-type.md) — How to create and manage profiles.
- [Personal access token authentication](/concepts/databricks-personal-access-token-pat-authentication.md)
- [OAuth machine-to-machine authentication](/concepts/machine-to-machine-m2m-authentication.md)
- [Serverless compute on Databricks](/concepts/serverless-gpu-compute-on-databricks.md)

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
