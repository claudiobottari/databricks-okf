---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5fa5cbedb5ac84950fe96390342e262e785c500576dbd4f7786f4b61d25829e2
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-serverless-compute-connection
    - DCSCC
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
title: Databricks Connect Serverless Compute Connection
description: Configuration methods for connecting Databricks Connect to serverless compute instead of classic clusters, including environment variables, config profiles, and builder methods.
tags:
  - databricks-connect
  - serverless-compute
  - configuration
timestamp: "2026-06-19T17:48:13.346Z"
---

---

title: Databricks Connect Serverless Compute Connection
summary: Databricks Connect supports connecting to serverless compute by setting serverless_compute_id=auto in config or using builder.serverless() in code.
sources:
  - compute-configuration-for-databricks-connect-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T14:20:29.889Z"
updatedAt: "2026-06-19T14:20:29.889Z"
tags:
  - databricks
  - serverless
  - databricks-connect
aliases:
  - databricks-connect-serverless-compute-connection
  - DCSCC
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Databricks Connect Serverless Compute Connection

**Databricks Connect Serverless Compute Connection** refers to the ability of [Databricks Connect](/concepts/databricks-connect.md) to connect to a Databricks Serverless Compute resource instead of a traditional cluster, enabling local IDE and application workflows to run Spark jobs on serverless infrastructure.

## Overview

Databricks Connect for Python and Scala supports connecting to serverless compute. To use this feature, version requirements for connecting to serverless must be met (see [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md)). When a serverless compute connection is configured, Databricks Connect ignores the `cluster_id` setting, as the connection targets serverless compute instead. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Configuration Methods

You can configure a connection to serverless compute in your local environment using one of the following approaches.

### Environment Variable

Set the local environment variable `DATABRICKS_SERVERLESS_COMPUTE_ID` to `auto`. When this variable is set, Databricks Connect uses serverless compute and ignores any `cluster_id` value. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```
export DATABRICKS_SERVERLESS_COMPUTE_ID=auto
```

### Databricks Configuration Profile

In a local [Databricks configuration profile](/concepts/databricks-configuration-profiles.md) (e.g., `DEFAULT`), set `serverless_compute_id = auto` alongside other required fields such as `host` and `token`. The profile then references serverless compute automatically. When this profile is selected, Databricks Connect uses serverless compute. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

Example profile:

```
[DEFAULT]
host = https://my-workspace.cloud.databricks.com
serverless_compute_id = auto
token = dapi123...
```

### Programmatic Initialization in Python or Scala

Use the `DatabricksSession.builder` API to explicitly enable serverless compute:

- **Builder method:** `DatabricksSession.builder.serverless().getOrCreate()`
- **Remote method:** `DatabricksSession.builder.remote(serverless=True).getOrCreate()`

Both approaches are valid for Python and Scala. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

# Option 1
spark = [[databrickssession|DatabricksSession]].builder.serverless().getOrCreate()

# Option 2
spark = [[databrickssession|DatabricksSession]].builder.remote(serverless=True).getOrCreate()
```

## Validation

To validate that the connection to serverless compute is correctly configured, run the `databricks-connect test` command from the command line. This command fails with a non-zero exit code if it detects incompatibilities, such as a version mismatch between Databricks Connect and serverless compute. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

For Databricks Connect 14.3 and above, you can also validate your environment using `validateSession()`:

```python
[[databrickssession|DatabricksSession]].builder.validateSession(True).getOrCreate()
```

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The integration library for connecting local environments to Databricks compute.
- Serverless Compute – On-demand compute resources managed by Databricks without cluster setup.
- [Databricks Configuration Profiles](/concepts/databricks-configuration-profiles.md) – Local files used to store authentication and connection settings.
- Databricks Runtime versions – Version compatibility requirements for Databricks Connect and serverless compute.
- [Cluster Configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) – Traditional cluster-based connection setup.

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
