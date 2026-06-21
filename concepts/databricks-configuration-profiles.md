---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f19ee0ac8853ccdf9c36347d9d06acee97f5b7258ea6048ee5c33d0ad66cc90e
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
    - tutorial-develop-a-databricks-app-locally-with-databricks-connect-databricks-on-aws.md
    - tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md
    - tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-configuration-profiles
    - DCP
    - .databrickscfg configuration file
    - .databrickscfg configuration profiles
    - Databricks CLI configuration profiles
    - Databricks Configuration Profile
    - Databricks configuration profile
    - Configuration Profile
    - Configuration Profiles
    - Configuration profiles
    - Databricks CLI Configuration
    - configuration profile
    - configuration profiles
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
    - file: tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md
    - file: tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md
    - file: tutorial-develop-a-databricks-app-locally-with-databricks-connect-databricks-on-aws.md
title: Databricks Configuration Profiles
description: Named configuration files used to store connection properties (host, token, cluster_id, etc.) for Databricks authentication and compute targeting
tags:
  - configuration
  - authentication
  - databricks
timestamp: "2026-06-18T11:04:24.293Z"
---

# Databricks Configuration Profiles

**Databricks configuration profiles** are local, INI‑style configuration files that store authentication and compute‑connection settings for Databricks tools such as the CLI, SDK, and Databricks Connect. They allow you to quickly switch between workspaces, authentication methods, and compute resources without hard‑coding sensitive values in application code. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md, tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md]

## File Location and Format

The configuration file is named `.databrickscfg`. On Linux or macOS it resides in the user’s home directory (`~/.databrickscfg`); on Windows it is in the `%USERPROFILE%` folder (`C:\Users\<username>\.databrickscfg`). ^[tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md]

The file uses a standard INI format. Each section (called a profile) begins with a section header in square brackets and contains key‑value pairs. The `DEFAULT` profile is special: the Databricks SDK and Databricks Connect use it when no explicit profile name is provided. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

Example profile for serverless compute:

```ini
[DEFAULT]
host                  = https://my-workspace.cloud.databricks.com
auth_type             = databricks-cli
serverless_compute_id = auto
```

^[tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md]

## Creating and Managing Profiles

Profiles are typically created using the Databricks CLI’s `auth login` command. The command can be combined with flags that automatically add compute‑specific fields, making it easier to configure Databricks Connect:

- `--configure-cluster` – adds `cluster_id` to the profile after you select a classic cluster from the list. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md, tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md]
- `--configure-serverless` – adds `serverless_compute_id = auto` to enable serverless compute. ^[tutorial-develop-a-databricks-app-locally-with-databricks-connect-databricks-on-aws.md]

To initiate OAuth user‑to‑machine (U2M) authentication and create a new profile, run:

```bash
databricks auth login --host <workspace-url>
```

The CLI prompts you to name the profile; pressing `Enter` accepts the suggested name (often `DEFAULT`). Existing profiles with the same name are overwritten. ^[tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md]

You can also edit the `.databrickscfg` file directly with any text editor to add, modify, or remove profiles. ^[tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md]

## Common Profile Fields

| Field | Description | Example |
|-------|-------------|---------|
| `host` | Databricks workspace instance URL | `https://dbc-a1b2345c-d6e7.cloud.databricks.com` |
| `token` | Databricks personal access token (legacy) | `dapi123...` |
| `auth_type` | Authentication method | `databricks-cli`, `oauth-m2m`, `pat` |
| `client_id` | OAuth client ID (M2M or U2M) | – |
| `client_secret` | OAuth client secret (M2M) | – |
| `cluster_id` | ID of a classic cluster | `0810-123456-abcd1234` |
| `serverless_compute_id` | Set to `auto` to use serverless compute | `auto` |

^[compute-configuration-for-databricks-connect-databricks-on-aws.md, tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md]

## Using Profiles with Databricks Connect

Databricks Connect (for Python and Scala) can be configured through a profile in several ways. The SDK searches for configuration properties in a defined order and uses the first match: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

1. **Explicit profile in code** – Pass the profile name to a `DatabricksSession` builder or SDK `Config` object:
   ```python
   from databricks.connect import [[databrickssession|DatabricksSession]]
   spark = [[databrickssession|DatabricksSession]].builder.profile("my-profile").getOrCreate()
   ```
   ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

2. **`DATABRICKS_CONFIG_PROFILE` environment variable** – Set the variable to the profile name, then call `DatabricksSession.builder.getOrCreate()` without arguments. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

3. **DEFAULT profile** – When no profile is specified anywhere, the SDK falls back to the `DEFAULT` section in `.databrickscfg`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md, tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md]

Profiles can also be combined with individual environment variables (e.g., `DATABRICKS_HOST`, `DATABRICKS_CLUSTER_ID`, `DATABRICKS_SERVERLESS_COMPUTE_ID`) for ad‑hoc overrides. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Example: Classic Cluster

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
spark = [[databrickssession|DatabricksSession]].builder.profile("my-classic-profile").getOrCreate()
```

Where the profile includes:
```ini
[my-classic-profile]
host = https://my-workspace.cloud.databricks.com
token = dapi...
cluster_id = 0810-123456-abcd1234
```

^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Example: Serverless Compute

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
spark = [[databrickssession|DatabricksSession]].builder.profile("my-serverless-profile").getOrCreate()
```

Where the profile sets `serverless_compute_id = auto`. When this field is present, Databricks Connect ignores any `cluster_id` value. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Best Practices

- **Use the `DEFAULT` profile** for your primary workspace to minimize boilerplate in code, especially for production‑ready applications. ^[tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md]
- **Create separate profiles** for different workspaces or authentication modes (e.g., one for development, one for production). ^[tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md]
- **Avoid hard‑coding credentials** in source code. Instead, store tokens and secrets in the configuration file or use OAuth flows that manage tokens automatically. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]
- **Protect the `.databrickscfg` file** with appropriate file permissions, as it contains sensitive authentication material.
- **Use the CLI to manage profiles** rather than manual editing, to ensure correct syntax and reduce errors.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – embeds Databricks configuration profiles to establish remote Spark sessions.
- Databricks CLI – creates and manages profiles through the `auth login` command.
- [Databricks authentication](/concepts/databricks-authentication-type.md) – overview of supported authentication types (PAT, OAuth M2M, OAuth U2M).
- Databricks SDK – uses the same profile resolution logic as Databricks Connect.
- Databricks personal access tokens – legacy authentication method stored in profiles.
- [OAuth machine-to-machine authentication](/concepts/machine-to-machine-m2m-authentication.md) – M2M OAuth fields (`client_id`, `client_secret`).
- [OAuth user-to-machine authentication](/concepts/user-to-machine-u2m-authentication.md) – U2M OAuth profiles created by `databricks auth login`.
- [Serverless compute](/concepts/serverless-gpu-compute.md) – compute mode enabled via `serverless_compute_id = auto`.

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md
- tutorial-develop-a-databricks-app-locally-with-databricks-connect-databricks-on-aws.md
- tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md
- tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
2. [tutorial-run-python-code-on-serverless-compute-databricks-on-aws.md](/references/tutorial-run-python-code-on-serverless-compute-databricks-on-aws-39a4e270.md)
3. [tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws.md](/references/tutorial-run-code-from-intellij-idea-on-classic-compute-databricks-on-aws-da20890c.md)
4. [tutorial-develop-a-databricks-app-locally-with-databricks-connect-databricks-on-aws.md](/references/tutorial-develop-a-databricks-app-locally-with-databricks-connect-databricks-on-aws-00e28271.md)
