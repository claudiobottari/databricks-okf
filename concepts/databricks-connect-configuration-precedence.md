---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6e21d91a042de147a899f45e33f46a26007620d5e74ede26e4ca1085b62742e9
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-configuration-precedence
    - DCCP
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
title: Databricks Connect Configuration Precedence
description: Databricks Connect searches for configuration properties in a defined order (remote() method, config profile, env vars, DEFAULT profile) and uses the first match.
tags:
  - databricks
  - configuration
  - databricks-connect
timestamp: "2026-06-19T14:20:15.470Z"
---

# Databricks Connect Configuration Precedence

**Databricks Connect Configuration Precedence** defines the order in which Databricks Connect searches for connection settings when establishing a link between a local IDE or application and a Databricks compute resource (cluster or serverless compute). The search uses a defined priority list, stopping at the first source that provides a complete set of required configuration properties. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Precedence Order

Databricks Connect checks configuration sources in the following order and uses the first one that is found and complete:

1. **The `DatabricksSession` class’s `remote()` method**  
   Properties can be provided directly to `remote()`, via the Databricks SDK’s `Config` class, or through a named configuration profile combined with `cluster_id`. This option applies only to personal access token authentication (legacy). ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

2. **A Databricks configuration profile**  
   A named profile (e.g., `my-profile`) that contains `cluster_id` and authentication fields (`host` and `token` for PAT; `host`, `client_id`, `client_secret` for OAuth M2M; `host` for OAuth U2M). The profile is referenced via `DatabricksSession.builder.profile("<profile-name>")` or through the SDK `Config` class with `profile=<profile-name>`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

3. **The `DATABRICKS_CONFIG_PROFILE` environment variable**  
   The variable points to the name of an existing configuration profile. When set, `DatabricksSession.builder.getOrCreate()` reads that profile automatically. The profile must contain `cluster_id` and the appropriate authentication fields. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

4. **Environment variables for each configuration property**  
   Individual environment variables such as `DATABRICKS_HOST`, `DATABRICKS_TOKEN`, `DATABRICKS_CLIENT_ID`, `DATABRICKS_CLIENT_SECRET`, and `DATABRICKS_CLUSTER_ID` are used. The variables needed depend on the authentication type. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

5. **A Databricks configuration profile named `DEFAULT`**  
   If no other configuration is found, Databricks Connect looks for a profile named `DEFAULT` in the standard Databricks configuration file. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

For steps 2–5, if the `DATABRICKS_CLUSTER_ID` environment variable is already set, the `cluster_id` field does not need to be specified again in the profile or code. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Authentication Type Requirements

Each authentication type imposes its own set of required fields in the profile or environment variables:

| Authentication Type | Required Profile Fields | Required Environment Variables |
|---------------------|------------------------|--------------------------------|
| Personal access token (PAT) | `host`, `token` | `DATABRICKS_HOST`, `DATABRICKS_TOKEN` |
| OAuth M2M | `host`, `client_id`, `client_secret` | `DATABRICKS_HOST`, `DATABRICKS_CLIENT_ID`, `DATABRICKS_CLIENT_SECRET` |
| OAuth U2M | `host` | `DATABRICKS_HOST` |

^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Serverless Compute Configuration

For serverless compute, the precedence rules still apply, but the `cluster_id` field is replaced by `serverless_compute_id = auto`. Two additional configuration methods exist specifically for serverless:

- Set the environment variable `DATABRICKS_SERVERLESS_COMPUTE_ID` to `auto`. When this variable is set, Databricks Connect ignores any `cluster_id` value. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]
- Use the programmatic methods `DatabricksSession.builder.serverless()` or `DatabricksSession.builder.remote(serverless=True)`. These bypass the cluster‑based precedence order and explicitly target serverless compute. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

Serverless configuration can also be defined in a profile (e.g., `[DEFAULT]` with `serverless_compute_id = auto`), which is then picked up through the normal precedence chain. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Validation

After configuration, run `databricks-connect test` to validate that the environment, credentials, and connection to the compute resource are correctly set up. The command fails with a non-zero exit code if any incompatibility is detected, such as a version mismatch. In Databricks Connect 14.3 and above, `validateSession()` can also be used:

```python
[[databrickssession|DatabricksSession]].builder.validateSession(True).getOrCreate()
```

^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Disabling Databricks Connect

The Databricks Connect service (and the underlying Spark Connect service) can be disabled on a cluster by setting the Spark configuration `spark.databricks.service.server.enabled` to `false`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – Overview of the client library and its capabilities.
- [Databricks Connection Profiles](/concepts/databricks-connect-configuration-profiles.md) – How to create and manage configuration profiles.
- [Databricks Authentication Types](/concepts/databricks-authentication-type.md) – PAT, OAuth M2M, and OAuth U2M.
- Serverless Compute on Databricks – Connecting to serverless compute resources.

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
