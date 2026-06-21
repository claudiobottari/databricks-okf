---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 12850eee8a580da7526f2ee9eebb2ab21e3d4ea7861568bc43de9512c35d9d20
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-serverless-compute
    - DCSC
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
title: Databricks Connect Serverless Compute
description: Feature allowing Databricks Connect to connect to serverless compute resources instead of classic clusters
tags:
  - serverless
  - connectivity
  - databricks
timestamp: "2026-06-18T11:04:39.017Z"
---

# Databricks Connect Serverless Compute

**Databricks Connect Serverless Compute** is a connection mode that allows Databricks Connect clients to connect to Databricks [serverless compute] instead of a traditional cluster. This mode eliminates the need to manage cluster infrastructure while still enabling remote execution of Spark workloads from local IDEs, notebook servers, and custom applications. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Overview

Databricks Connect enables you to connect popular IDEs such as Visual Studio Code, PyCharm, RStudio Desktop, IntelliJ IDEA, notebook servers, and other custom applications to Databricks compute resources. Serverless compute provides an alternative to classic cluster-based connections, offering automatic scaling and management without requiring a running cluster. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

Both Python and Scala versions of Databricks Connect support connections to serverless compute, provided the version requirements are met. See [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md) for supported version details. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Prerequisites

Before configuring a connection to serverless compute, you need:

- Databricks Connect installed. For installation requirements, see [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md).
- The Databricks workspace instance name (Server Hostname for your compute resource). See [Get connection details for a Databricks compute resource](/concepts/remote-connections-from-databricks-notebooks.md).
- A workspace that has serverless compute enabled.

Unlike classic compute connections, you do not need a cluster ID when using serverless compute. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Configuration Methods

There are multiple ways to configure a connection to serverless compute. Databricks Connect searches for configuration properties in the following order and uses the first configuration it finds: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

1. The `DatabricksSession` class's `.serverless()` or `.remote(serverless=True)` method
2. A Databricks configuration profile with `serverless_compute_id = auto`
3. The `DATABRICKS_SERVERLESS_COMPUTE_ID` environment variable set to `auto`

When the serverless compute id is set to `auto`, Databricks Connect ignores any configured `cluster_id`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### Using the `.serverless()` Builder Method

The simplest way to connect to serverless compute is to call the `.serverless()` method on the `DatabricksSession` builder: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.serverless().getOrCreate()
```

### Using the `.remote(serverless=True)` Method

Alternatively, you can use the `.remote()` method with `serverless=True`: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.remote(serverless=True).getOrCreate()
```

### Using a Configuration Profile

Create or modify a local Databricks [configuration profile] and set `serverless_compute_id = auto`. For example, in the `DEFAULT` profile: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```
[DEFAULT]
host = https://my-workspace.cloud.databricks.com
serverless_compute_id = auto
token = dapi123...
```

Then reference that profile from your code: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.profile("<profile-name>").getOrCreate()
```

### Using Environment Variables

Python users can also set the `DATABRICKS_SERVERLESS_COMPUTE_ID` environment variable to `auto`. When this environment variable is set, Databricks Connect ignores any `cluster_id` configuration. Then use the standard builder initialization: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

## Validation

To validate that your environment, default credentials, and connection to serverless compute are correctly configured, run the `databricks-connect test` command: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```bash
databricks-connect test
```

This command fails with a non-zero exit code and a corresponding error message when it detects any incompatibility, such as when the Databricks Connect version is incompatible with the serverless compute version. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

In Databricks Connect 14.3 and above, you can also validate your environment using `validateSession()`: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
[[databrickssession|DatabricksSession]].builder.validateSession(True).getOrCreate()
```

## Differences from Classic Compute

| Aspect | Serverless Compute | Classic Cluster |
|--------|-------------------|-----------------|
| Infrastructure management | Fully managed by Databricks | User manages cluster lifecycle |
| Cluster ID requirement | Not required (`serverless_compute_id = auto`) | Required (`cluster_id` must be specified) |
| Scaling | Automatic | Manual or auto-scaling configuration |
| Startup time | Near-instant | Varies based on cluster state and size |
| Configuration | Uses `serverless_compute_id` or `.serverless()` method | Uses `cluster_id` or `.remote()` method |

When `DATABRICKS_SERVERLESS_COMPUTE_ID` is set to `auto`, Databricks Connect ignores the `cluster_id` setting if one is also present. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Known Limitations

- Serverless compute connection requires specific version compatibility between Databricks Connect and the serverless compute runtime. See [Databricks Connect versions](/concepts/databricks-connect.md) for supported version pairs.
- Some features available on classic clusters may not be supported in the serverless compute environment.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The overall framework for connecting local environments to Databricks compute
- [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md) — Version and environment requirements
- [Databricks Configuration Profiles](/concepts/databricks-configuration-profiles.md) — Authentication and connection configuration files
- Serverless compute (Databricks) — The serverless compute infrastructure
- Databricks cluster — Traditional cluster-based compute for comparison
- Compute resource URL and ID — How to find workspace instance names and cluster IDs

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
