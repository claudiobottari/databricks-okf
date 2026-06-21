---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 210226c6385dc6457dbc30908cfa1419d5822769f533f5d9841cf5966dfe0555
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-authentication-type-requirements
    - DCATR
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
title: Databricks Connect Authentication Type Requirements
description: The specific configuration fields required for each authentication type (PAT, OAuth M2M, OAuth U2M) when connecting via Databricks Connect.
tags:
  - databricks-connect
  - authentication
  - oauth
  - pat
timestamp: "2026-06-19T17:48:32.885Z"
---

## Databricks Connect Authentication Type Requirements

**Databricks Connect Authentication Type Requirements** refers to the mandatory configuration fields that must be supplied when establishing a connection between Databricks Connect and a Databricks compute resource. The required fields depend on the chosen authentication method and whether the connection targets a classic cluster or [serverless compute](/concepts/serverless-gpu-compute.md). ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Supported Authentication Types and Required Fields

Databricks Connect supports three authentication types. Each type requires a specific set of fields, which must be provided either in a [Databricks configuration profile](/concepts/databricks-configuration-profiles.md), through environment variables, or via the `DatabricksSession.builder.remote()` method. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

| Authentication Type | Required Fields |
|---------------------|-----------------|
| [Personal Access Token Authentication](/concepts/databricks-personal-access-token-pat-authentication.md) (legacy) | `host`, `token` |
| [OAuth M2M Authentication](/concepts/machine-to-machine-m2m-authentication.md) (machine-to-machine) | `host`, `client_id`, `client_secret` |
| [OAuth U2M Authentication](/concepts/user-to-machine-u2m-authentication.md) (user-to-machine) | `host` |

For profiles and environment variables, the field names map to specific property names. For example, in a configuration profile the fields are `host`, `token`, `client_id`, `client_secret`. In environment variables they become `DATABRICKS_HOST`, `DATABRICKS_TOKEN`, `DATABRICKS_CLIENT_ID`, `DATABRICKS_CLIENT_SECRET`. OAuth U2M authentication requires only the `host` field; the token is obtained interactively via the Databricks CLI's `auth login` flow. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Connecting to a Cluster

When connecting to a classic cluster, the configuration must also include the cluster ID. The cluster ID can be supplied in the same profile, as an environment variable (`DATABRICKS_CLUSTER_ID`), or passed programmatically. If the cluster ID is already set via environment variable, it does not need to be repeated in the profile or code. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

For each authentication type, the required fields must be present in whichever configuration source is used (profile, environment variables, or the `remote()` method). The `DatabricksSession.builder` searches for configuration in a defined priority order; the first complete set of credentials found is used. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Connecting to Serverless Compute

Serverless compute connections do not use a cluster ID. Instead, the configuration must indicate serverless mode. This can be done by:

- Setting the environment variable `DATABRICKS_SERVERLESS_COMPUTE_ID` to `auto`.
- Adding `serverless_compute_id = auto` to a Databricks configuration profile.
- Using the builder methods `.serverless()` or `.remote(serverless=True)`.

When any of these serverless indicators are present, the `cluster_id` field is ignored. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Authentication Requirements by Configuration Method

The required fields for each authentication type apply uniformly across all configuration methods. The following table summarises the fields needed for each method when using PAT authentication (the most common case):

| Configuration Method | Required Fields (PAT) |
|----------------------|-----------------------|
| Profile (named or `DEFAULT`) | `host`, `token`, `cluster_id` (or `serverless_compute_id`) |
| Environment variables | `DATABRICKS_HOST`, `DATABRICKS_TOKEN`, `DATABRICKS_CLUSTER_ID` |
| `remote()` method | `host`, `token`, `cluster_id` |

For OAuth M2M, replace `token` with `client_id` and `client_secret`. For OAuth U2M, only `host` is needed. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Validation

After configuring the connection, run `databricks-connect test` or use `DatabricksSession.builder.validateSession(True)` to verify that the authentication and compute settings are correct. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md)
- [Databricks Configuration Profile](/concepts/databricks-configuration-profiles.md)
- [Personal Access Token Authentication](/concepts/databricks-personal-access-token-pat-authentication.md)
- [OAuth M2M Authentication](/concepts/machine-to-machine-m2m-authentication.md)
- [OAuth U2M Authentication](/concepts/user-to-machine-u2m-authentication.md)
- Serverless Compute
- Cluster Configuration

### Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
