---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0e134ffe0cdbd271760869c6735f9b585f5921f8f5f443c7049f1244a4622d41
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-configuration-profiles-for-connect
    - DCPFC
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
title: Databricks Configuration Profiles for Connect
description: Named configuration profiles (including DEFAULT) store connection fields like host, token, cluster_id, client_id, and client_secret for Databricks Connect authentication.
tags:
  - databricks
  - authentication
  - configuration
timestamp: "2026-06-19T14:20:56.353Z"
---

---
title: Databricks Configuration Profiles for Connect
summary: Using .databrickscfg configuration profiles (named or DEFAULT) with cluster_id and authentication fields to configure Databricks Connect.
sources:
  - compute-configuration-for-databricks-connect-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:40:56.687Z"
updatedAt: "2026-06-18T14:40:56.687Z"
tags:
  - configuration
  - profiles
  - authentication
aliases:
  - databricks-configuration-profiles-for-connect
  - DCPFC
confidence: 1
provenanceState: extracted
inferredParagraphs: 1
---

# Databricks Configuration Profiles for Connect

**Databricks Configuration Profiles for Connect** are named sections in a configuration file (typically `~/.databrickscfg`) that store connection and authentication parameters for [Databricks Connect](/concepts/databricks-connect.md). They allow developers to avoid hardcoding credentials and cluster identifiers in code, and to switch between different environments or compute targets by changing the profile name. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Overview

When initializing a `DatabricksSession` for [Databricks Connect](/concepts/databricks-connect.md), the library searches for configuration properties in a defined order and uses the first configuration it finds. A configuration profile is one of the supported methods. Databricks recommends configuring properties through environment variables or configuration files rather than embedding them in code. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Prerequisites

Before using a configuration profile for Databricks Connect, ensure the following are available:

- Databricks Connect installed. See [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md).
- The Databricks [workspace instance name](https://docs.databricks.com/aws/en/workspace/workspace-details#workspace-url) (the **Server Hostname** for the compute resource).
- If connecting to classic compute, the cluster ID (obtainable from the cluster URL). ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Creating a Configuration Profile for Cluster Connections

A configuration profile for connecting to a classic cluster must include the `cluster_id` field and the fields required by the chosen [Databricks authentication types|authentication type](/concepts/databricks-authentication-type.md). ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

The required fields per authentication type are:

- **[Personal access tokens](/concepts/databricks-personal-access-token-pat-authentication.md)**: `host` and `token`.
- **[OAuth M2M authentication](/concepts/machine-to-machine-m2m-authentication.md)** (where supported): `host`, `client_id`, and `client_secret`.
- **[OAuth U2M authentication](/concepts/user-to-machine-u2m-authentication.md)** (where supported): `host`.

The `auth login` command’s `--configure-cluster` option can automatically add the `cluster_id` field to a new or existing profile. Run `databricks auth login -h` for details. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Using a Configuration Profile

Databricks Connect can reference a profile in several ways, each described below. If the `DATABRICKS_CLUSTER_ID` environment variable is already set, the `cluster_id` field can be omitted from the profile. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Specifying the Profile Name in Code

Pass the profile name to `DatabricksSession.builder.profile("<profile-name>")`:

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
spark = [[databrickssession|DatabricksSession]].builder.profile("<profile-name>").getOrCreate()
```

The profile must include the `cluster_id` field. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Specifying Profile Name Together with `cluster_id`

If the profile does not contain `cluster_id`, use the Databricks SDK `Config` class to supply it separately:

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
from databricks.sdk.core import Config
config = Config(profile="<profile-name>", cluster_id="<cluster-id>")
spark = [[databrickssession|DatabricksSession]].builder.sdkConfig(config).getOrCreate()
```

The `cluster_id` can come from a custom retrieve function. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Using the `DATABRICKS_CONFIG_PROFILE` Environment Variable

Set the environment variable `DATABRICKS_CONFIG_PROFILE` to the profile name. Then call `DatabricksSession.builder.getOrCreate()` without arguments. The profile must contain `cluster_id` and the necessary auth fields. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Using the `DEFAULT` Profile

If no profile is specified explicitly and `DATABRICKS_CONFIG_PROFILE` is not set, Databricks Connect looks for a profile named `DEFAULT` in the configuration file. The `DEFAULT` profile must contain `cluster_id` and the required auth fields. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Configuration Profile for Serverless Compute

Databricks Connect for Python and Scala also supports connecting to [serverless compute](/concepts/serverless-gpu-compute.md). To use a configuration profile with serverless compute, set `serverless_compute_id = auto` in the profile instead of `cluster_id` ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]:

```
[DEFAULT]
host = https://my-workspace.cloud.databricks.com
serverless_compute_id = auto
token = dapi123...
```

Then reference the profile by name or use the `DEFAULT` profile. Alternatively, set the `DATABRICKS_SERVERLESS_COMPUTE_ID` environment variable to `auto`. If this variable is set, Databricks Connect ignores `cluster_id`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

In code, a serverless connection can also be created without a profile by calling `DatabricksSession.builder.serverless()` or `DatabricksSession.builder.remote(serverless=True)`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Validating the Connection

To verify that the environment, credentials, and compute configuration are correct, run `databricks-connect test`. This command fails with a non-zero exit code and a message when incompatibilities are detected (e.g., version mismatch). ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

In Databricks Connect 14.3 and later, `validateSession(True)` can be called on the builder:

```python
[[databrickssession|DatabricksSession]].builder.validateSession(True).getOrCreate()
```

^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks authentication types](/concepts/databricks-authentication-type.md)
- [Personal access tokens](/concepts/databricks-personal-access-token-pat-authentication.md)
- [OAuth M2M authentication](/concepts/machine-to-machine-m2m-authentication.md)
- [OAuth U2M authentication](/concepts/user-to-machine-u2m-authentication.md)
- [Databricks Connect](/concepts/databricks-connect.md)
- [Serverless compute](/concepts/serverless-gpu-compute.md)
- Databricks cluster configuration
- [Environment Variable Configuration for Databricks Connect](/concepts/environment-variable-configuration-for-databricks-connect.md)

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
