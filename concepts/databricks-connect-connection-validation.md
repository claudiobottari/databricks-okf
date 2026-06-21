---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e75bbdb3cdc96c91b9cbd77167f87cea73a471704b5df5339bce2bef950b1083
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-connection-validation
    - DCCV
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
title: Databricks Connect Connection Validation
description: Methods to validate that the environment, credentials, and compute connection are correctly configured, including the databricks-connect test command and validateSession().
tags:
  - databricks-connect
  - validation
  - troubleshooting
timestamp: "2026-06-19T17:48:39.570Z"
---

# Databricks Connect Connection Validation

**Databricks Connect Connection Validation** refers to the built‑in checks that verify your local environment, credentials, and target compute are correctly configured for [Databricks Connect](/concepts/databricks-connect.md). Validation helps detect common setup errors – such as version incompatibilities or missing authentication – before you begin running remote commands. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Validation methods

Databricks Connect provides two ways to validate the connection.

### `databricks-connect test` command

Run the following command from your terminal:

```bash
databricks-connect test
```

This command performs a full compatibility check and exits with a non‑zero exit code and an error message if it finds any issue – for example, when the installed Databricks Connect version is incompatible with the version running on the target compute. The test works for all supported Databricks Connect versions (Databricks Runtime 13.3 LTS and above). ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### `validateSession()` method (14.3+)

If you are using Databricks Connect 14.3 or later, you can also call `validateSession()` directly on the builder:

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.validateSession(True).getOrCreate()
```

Passing `True` to `validateSession()` instructs the builder to check the environment and credentials during session creation. If validation fails, the call raises an error with a descriptive message. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## What validation checks

Both methods verify:

- That the local environment has the necessary [Databricks authentication](/concepts/databricks-authentication-type.md) configuration (`host`, `token` or OAuth credentials, and either `cluster_id` or `serverless_compute_id`).
- That the target compute is reachable and supports the Databricks Connect protocol.
- That the Databricks Connect library version is compatible with the Databricks Runtime version on the cluster or serverless compute.

If a version mismatch is detected, the `databricks-connect test` command reports it explicitly, allowing you to upgrade or downgrade the client library. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Disabling validation on a cluster

Validation assumes that the Databricks Connect service is enabled on the target compute. You can disable this service on a specific cluster by setting the Spark configuration property:

```
spark.databricks.service.server.enabled false
```

When this property is set to `false`, the cluster will not accept Databricks Connect connections, and any validation attempt will fail. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Related concepts

- [Databricks Connect](/concepts/databricks-connect.md) – the overall framework for connecting IDEs to Databricks compute
- [DatabricksSession](/concepts/databrickssession.md) – the entry point for building a Spark session with Databricks Connect
- [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) – all methods for setting up a connection (profiles, environment variables, remote builder)
- [Serverless compute](/concepts/serverless-gpu-compute.md) – an alternative compute target for Databricks Connect
- Cluster – classic compute target for Databricks Connect
- [Databricks authentication](/concepts/databricks-authentication-type.md) – credential types supported by Databricks Connect

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
