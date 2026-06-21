---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1118ec3f3463cfe7a5b32cbd65e1d4528a733df901e02186695d68a759a032f9
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
    - tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databrickssession-builder-api
    - DBA
    - DatabricksSession builder
    - DatabricksSession.builder
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
    - file: tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md
title: DatabricksSession Builder API
description: The programmatic API (remote(), profile(), serverless(), sdkConfig(), getOrCreate()) for configuring and initializing a Databricks Connect session.
tags:
  - databricks-connect
  - api
  - session-management
  - python-scala
timestamp: "2026-06-19T17:48:19.959Z"
---

---
title: [DatabricksSession](/concepts/databrickssession.md) Builder API
summary: The primary Python/Scala builder for configuring a Databricks Connect session, providing methods to specify host, token, cluster ID, serverless mode, authentication profiles, and SDK configuration.
sources:
  - compute-configuration-for-databricks-connect-databricks-on-aws.md
  - tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md
kind: concept
tags:
  - databricks
  - api
  - spark-session
  - databricks-connect
aliases:
  - databrickssession-builder-api
  - DBA
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

## [DatabricksSession](/concepts/databrickssession.md) Builder API

The **DatabricksSession Builder API** is the primary Python/Scala interface for configuring a connection between Databricks Connect and Databricks compute resources, including classic clusters and serverless compute. It is the standard way to establish a connection from a local development environment or IDE to Databricks compute. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Overview

The `DatabricksSession.builder` object exposes methods to specify connection details — such as host, authentication token, cluster ID, or serverless mode — and then creates the session with `getOrCreate()`. It supports multiple authentication mechanisms including Databricks personal access tokens (PAT), OAuth machine-to-machine (M2M), and OAuth user-to-machine (U2M). ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

Databricks Connect searches for configuration properties in a defined order and uses the first one it finds, allowing you to mix code-based configuration with environment variables and configuration profiles. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Builder Methods

### `.remote()`

Sets connection properties explicitly: `host`, `token`, and optionally `cluster_id`. This method applies only to personal access token authentication. You can also pass `serverless=True` to connect to serverless compute instead of a cluster. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
spark = [[databrickssession|DatabricksSession]].builder.remote(
    host="https://<workspace-url>",
    token="<token>",
    cluster_id="<cluster-id>"
).getOrCreate()
```

### `.profile()`

Specifies a Databricks [configuration profile](/concepts/databricks-configuration-profiles.md) name to use. The profile must contain the necessary fields for the chosen authentication type (e.g., `host` and `token` for PAT). If the profile already includes `cluster_id`, you do not need to provide it separately. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
spark = [[databrickssession|DatabricksSession]].builder.profile("<profile-name>").getOrCreate()
```

### `.sdkConfig()`

Accepts a `databricks.sdk.core.Config` object. This is useful when you already have a configuration object from the Databricks SDK. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.sdk.core import Config
config = Config(host="...", token="...", cluster_id="...")
spark = [[databrickssession|DatabricksSession]].builder.sdkConfig(config).getOrCreate()
```

### `.serverless()`

Configures the session to connect to serverless compute. Equivalent to using `.remote(serverless=True)`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md, tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md]

```python
spark = [[databrickssession|DatabricksSession]].builder.serverless().getOrCreate()
```

### `.getOrCreate()`

Creates a new `DatabricksSession` (or returns an existing one if it matches the configuration). It must be called last in the builder chain. If no configuration is explicitly provided via builder methods, it falls back to environment variables and configuration profiles. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### `.validateSession()`

Available from Databricks Connect 14.3 and above. Validates the environment, default credentials, and connection to compute. It should be called before `getOrCreate()`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
spark = [[databrickssession|DatabricksSession]].builder.validateSession(True).getOrCreate()
```

## Configuration Search Order

When `getOrCreate()` is called, Databricks Connect searches for configuration properties in the following order, using the first one found: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

1. **`.remote()` method** — explicit host, token, cluster_id/serverless.
2. **`.profile()` method** — named configuration profile.
3. **`DATABRICKS_CONFIG_PROFILE` environment variable** — points to a named profile.
4. **Individual environment variables** — one per configuration property (e.g., `DATABRICKS_HOST`, `DATABRICKS_TOKEN`, `DATABRICKS_CLUSTER_ID`, `DATABRICKS_SERVERLESS_COMPUTE_ID`).
5. **A configuration profile named `DEFAULT`** — the last resort.

## Connecting to a Cluster

To connect to a classic cluster, you must provide a `cluster_id`. This can be done: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

- In the `.remote()` method.
- In a configuration profile (as a `cluster_id` field) and then using `.profile()`.
- Via the environment variable `DATABRICKS_CLUSTER_ID`.

If `DATABRICKS_CLUSTER_ID` is set and you use `.profile()` or `.sdkConfig()` without also specifying `cluster_id`, the environment variable is used. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

You can specify `cluster_id` alongside a profile or SDK config without modifying the profile itself. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Connecting to Serverless Compute

To connect to serverless compute, you have several options: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md, tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md]

- Use `.serverless()` in the builder chain.
- Use `.remote(serverless=True)`.
- Set the environment variable `DATABRICKS_SERVERLESS_COMPUTE_ID=auto`.
- Add `serverless_compute_id = auto` to a configuration profile and reference it.

When any of these are used, Databricks Connect ignores the `cluster_id` setting. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Production-Ready Configuration

For production scenarios, it is recommended to avoid specifying compute details in the builder code. Instead, rely on a `DEFAULT` configuration profile or environment variables. This makes the code portable across environments (e.g., local IDE, CI/CD, deployment to a Databricks cluster). ^[tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md]

The recommended pattern is:

```python
spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

Then configure the connection through a `.databrickscfg` file (typically `~/.databrickscfg`) or environment variables. For serverless, add `serverless_compute_id = auto` to the `DEFAULT` profile. For a classic cluster, add `cluster_id = <cluster-id>`. ^[tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md]

## Validation

You can validate your environment and connection by running the `databricks-connect test` command from the terminal, or by calling `validateSession(True)` on the builder. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The overall mechanism for connecting IDEs to Databricks compute.
- Databricks Authentication — Methods for authenticating to Databricks (PAT, OAuth U2M, OAuth M2M).
- [Configuration Profiles](/concepts/databricks-configuration-profiles.md) — Files that store workspace and authentication settings.
- Serverless Compute — On-demand compute that requires no cluster configuration.
- Compute Configuration — How to set up clusters for Databricks Connect.

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md
- tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
2. [tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md](/references/tutorial-run-python-code-on-serverless-compute-databricks-on-aws-39a4e270.md)
