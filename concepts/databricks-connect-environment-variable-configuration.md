---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c530fe45c555ab0ba7ed651093946ef9563e6317a3092b5986c642a9c7788ee1
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-connect-environment-variable-configuration
    - DCEVC
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
    - file: databricks-connect-for-r-databricks-on-aws.md
title: Databricks Connect Environment Variable Configuration
description: Environment variables such as DATABRICKS_CONFIG_PROFILE, DATABRICKS_CLUSTER_ID, DATABRICKS_HOST, DATABRICKS_TOKEN can configure the connection without hardcoding values.
tags:
  - databricks
  - environment-variables
  - configuration
timestamp: "2026-06-19T14:21:49.710Z"
---

# Databricks Connect Environment Variable Configuration

**Databricks Connect Environment Variable Configuration** refers to the method of configuring a connection between [Databricks Connect](/concepts/databricks-connect.md) and a Databricks cluster or serverless compute by setting environment variables. Databricks Connect searches for configuration properties in a specific order, and environment variables are one of the supported configuration methods. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Overview

Databricks Connect enables you to connect popular IDEs such as Visual Studio Code, PyCharm, RStudio Desktop, IntelliJ IDEA, notebook servers, and other custom applications to Databricks clusters. You can configure the connection using environment variables for each configuration property, which Databricks recommends over hard-coding credentials in code. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md, databricks-connect-for-r-databricks-on-aws.md]

## Configuration Search Order

Databricks Connect searches for configuration properties in the following order and uses the first configuration it finds. Environment variables are checked at position 4 in the search order. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

1. The [DatabricksSession](/concepts/databrickssession.md) class's `remote()` method
2. A Databricks configuration profile
3. The `DATABRICKS_CONFIG_PROFILE` environment variable
4. **An environment variable for each configuration property**
5. A Databricks configuration profile named `DEFAULT`

## Required Environment Variables

### For Cluster Connections

The required environment variables for each [Databricks authentication](/concepts/databricks-authentication-type.md) type are as follows: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

**Personal access token authentication:**
- `DATABRICKS_HOST` — The workspace instance URL
- `DATABRICKS_TOKEN` — A Databricks personal access token
- `DATABRICKS_CLUSTER_ID` — The ID of the cluster to connect to

**OAuth machine-to-machine (M2M) authentication (where supported):**
- `DATABRICKS_HOST` — The workspace instance URL
- `DATABRICKS_CLIENT_ID` — The OAuth client ID
- `DATABRICKS_CLIENT_SECRET` — The OAuth client secret
- `DATABRICKS_CLUSTER_ID` — The ID of the cluster to connect to

**OAuth user-to-machine (U2M) authentication (where supported):**
- `DATABRICKS_HOST` — The workspace instance URL
- `DATABRICKS_CLUSTER_ID` — The ID of the cluster to connect to

### For Serverless Compute Connections

To connect to serverless compute instead of a cluster, set: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

- `DATABRICKS_SERVERLESS_COMPUTE_ID` to `auto` — When this environment variable is set, Databricks Connect ignores the `cluster_id` setting.

All other authentication-related environment variables (`DATABRICKS_HOST`, `DATABRICKS_TOKEN`, etc.) remain the same as for cluster connections.

## Usage

After setting the required environment variables, initialize the `DatabricksSession` class: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

The `getOrCreate()` method automatically reads the environment variables you have set.

## Environment Variables for R (Databricks Connect for R)

For [Databricks Connect for R](/concepts/databricks-connect-for-r.md) using `sparklyr`, authentication currently only supports Databricks personal access tokens. Set the following environment variables in an `.Renviron` file: ^[databricks-connect-for-r-databricks-on-aws.md]

```
DATABRICKS_HOST=<workspace-url>
DATABRICKS_TOKEN=<personal-access-token>
DATABRICKS_CLUSTER_ID=<cluster-id>
```

To load these environment variables in RStudio Desktop, restart R by clicking **Session > Restart R**. ^[databricks-connect-for-r-databricks-on-aws.md]

## Best Practices

Databricks recommends configuring connection properties through environment variables or configuration files rather than hard-coding them in your code. This approach keeps sensitive values such as tokens and credentials separate from source code and makes it easier to change connection parameters without modifying your application code. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Validation

To validate that your environment variables and connection are correctly set up, run the `databricks-connect test` command. In Databricks Connect 14.3 and above, you can also use `validateSession()`: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
[[databrickssession|DatabricksSession]].builder.validateSession(True).getOrCreate()
```

The validation fails with a non-zero exit code and an error message when it detects any incompatibility, such as a version mismatch between Databricks Connect and the compute resource.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The overall tool for connecting IDEs to Databricks
- [Databricks configuration profile](/concepts/databricks-configuration-profiles.md) — An alternative to environment variables for storing connection settings
- [Databricks authentication](/concepts/databricks-authentication-type.md) — The various authentication methods supported by Databricks
- [DatabricksSession](/concepts/databrickssession.md) — The main class for establishing a Databricks Connect session
- [Databricks Connect for R](/concepts/databricks-connect-for-r.md) — R-specific implementation using `sparklyr`

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md
- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
2. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
