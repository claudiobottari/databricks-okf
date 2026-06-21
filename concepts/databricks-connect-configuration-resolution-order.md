---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3a24997bedc3e4f7f793ca2c7f5ce17686fd86ad940e3bdc54c2c72ee0308564
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-configuration-resolution-order
    - DCCRO
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
title: Databricks Connect Configuration Resolution Order
description: The ordered sequence (5 levels) in which Databricks Connect searches for connection configuration properties, using the first match found.
tags:
  - databricks-connect
  - configuration
  - resolution-order
timestamp: "2026-06-19T17:48:21.086Z"
---

# Databricks Connect Configuration Resolution Order

**Databricks Connect Configuration Resolution Order** defines the sequence in which [Databricks Connect](/concepts/databricks-connect.md) searches for configuration properties when establishing a connection to a Databricks cluster or [serverless compute](/concepts/serverless-gpu-compute.md). The system uses the first configuration it finds in this ordered list, allowing flexible configuration through multiple methods.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Resolution Order

Databricks Connect searches for configuration properties in the following order, using the first configuration it finds:^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

1. **The `DatabricksSession` class's `remote()` method** – Specify the workspace instance name, token, and cluster ID directly in code.
2. **A Databricks configuration profile** – Use a named profile containing `cluster_id` and authentication fields.
3. **The `DATABRICKS_CONFIG_PROFILE` environment variable** – Set an environment variable pointing to a named profile.
4. **An environment variable for each configuration property** – Set individual environment variables like `DATABRICKS_HOST`, `DATABRICKS_TOKEN`, `DATABRICKS_CLUSTER_ID`.
5. **A Databricks configuration profile named `DEFAULT`** – Fall back to the default profile when no other configuration is found.

## Configuration Methods

### 1. The `DatabricksSession` class's `remote()` method

This applies to [personal access token authentication](/concepts/databricks-personal-access-token-pat-authentication.md) only. You initialize by setting `host`, `token`, and `cluster_id` in `DatabricksSession.builder.remote()`. You can also use the Databricks SDK's `Config` class or specify a configuration profile along with `cluster_id`.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

Databricks recommends configuring properties through environment variables or configuration files rather than specifying them in code.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### 2. A Databricks configuration profile

Create or identify a [Databricks configuration profile](/concepts/databricks-configuration-profiles.md) containing `cluster_id` and authentication fields for your authentication type. Required fields vary by authentication type:^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

- **Personal access token**: `host` and `token`
- **OAuth M2M**: `host`, `client_id`, `client_secret`
- **OAuth U2M**: `host`

You can specify `cluster_id` either within the profile or separately alongside the profile name.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### 3. The `DATABRICKS_CONFIG_PROFILE` environment variable

Set the `DATABRICKS_CONFIG_PROFILE` environment variable to the name of a configuration profile containing `cluster_id` and authentication fields. Then initialize `DatabricksSession` without additional parameters.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### 4. An environment variable for each configuration property

Set individual environment variables like `DATABRICKS_HOST`, `DATABRICKS_TOKEN`, and `DATABRICKS_CLUSTER_ID` corresponding to your authentication type's requirements. Then initialize `DatabricksSession` without additional parameters.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### 5. A Databricks configuration profile named `DEFAULT`

Name a configuration profile `DEFAULT` containing `cluster_id` and authentication fields. This serves as the fallback configuration when no other method is specified. You can use the `auth login` command's `--configure-cluster` option to automatically add `cluster_id` to this profile.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Serverless Compute Configuration

For [serverless compute](/concepts/serverless-gpu-compute.md) connections, you can:^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

- Set `DATABRICKS_SERVERLESS_COMPUTE_ID` to `auto` – this overrides `cluster_id`
- Set `serverless_compute_id = auto` in a configuration profile
- Use `DatabricksSession.builder.serverless()` or `DatabricksSession.builder.remote(serverless=True)`

## Validation

To validate your configuration, run `databricks-connect test`. This command fails with a non-zero exit code and error message when detecting incompatibility. In Databricks Connect 14.3+, you can also use `validateSession()`.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Disabling Databricks Connect

Databricks Connect can be disabled on any cluster by setting `spark.databricks.service.server.enabled` to `false` in the Spark configuration.^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library for remote Spark execution
- [Databricks configuration profile](/concepts/databricks-configuration-profiles.md) – Stored authentication and connection settings
- [Personal access token authentication](/concepts/databricks-personal-access-token-pat-authentication.md) – Legacy authentication method
- [OAuth M2M authentication](/concepts/machine-to-machine-m2m-authentication.md) – Machine-to-machine authentication
- [OAuth U2M authentication](/concepts/user-to-machine-u2m-authentication.md) – User-to-machine authentication
- [Serverless compute](/concepts/serverless-gpu-compute.md) – Databricks' serverless compute offering
- Spark configuration – Cluster-level configuration settings

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
