---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6f125d646e496472aebb28b3d245afcfcb49e564de2c4edeaf1a3695986a62a3
  pageDirectory: concepts
  sources:
    - databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - portability-of-databricks-connect-apis
    - PODCA
    - Portability of Databricks Connect Code
  citations:
    - file: databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
title: Portability of Databricks Connect APIs
description: All Databricks Connect APIs are available in Databricks notebooks as part of the corresponding Databricks Runtime, enabling seamless code transition from local development to deployment without code changes.
tags:
  - databricks
  - portability
  - api
timestamp: "2026-06-19T14:47:44.967Z"
---

Here is the wiki page for "Portability of Databricks Connect APIs".

---

# Portability of Databricks Connect APIs

**Portability of Databricks Connect APIs** refers to the property that all Databricks Connect APIs are available in Databricks notebooks as part of the corresponding Databricks Runtime, allowing code to transition from local development to deployment without changes. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Overview

Databricks Connect enables developers to connect to Databricks compute from a local development environment outside of Databricks. Developers can then develop, debug, and test their code directly from their IDE before moving their code to a notebook or job in Databricks. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Key Principle: Seamless Transition

To make the transition from local development to deployment to Databricks seamless, all of the Databricks Connect APIs are available in Databricks notebooks as part of the corresponding Databricks Runtime. This allows you to run your code in a Databricks notebook without any changes to your code. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## [DatabricksSession](/concepts/databrickssession.md) Behavior Differences

The behavior of `DatabricksSession` differs slightly when using Databricks Connect in a local development environment and in notebooks and jobs in the Databricks workspace. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

### Local Development Environment Behavior

When running code locally within an IDE outside of Databricks:

- `DatabricksSession.builder.getOrCreate()` gets the existing Spark session for the provided configuration if it exists, or creates a new Spark session if it doesn't exist. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]
- `DatabricksSession.builder.create()` always creates a new Spark session. Connection parameters such as `host`, `token`, and `cluster_id` are populated either from the source code, environment variables, or the `.databrickscfg` configuration profiles file. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

When run using Databricks Connect, the following code creates two separate sessions: ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

```python
spark1 = [[databrickssession|DatabricksSession]].builder.create()
spark2 = [[databrickssession|DatabricksSession]].builder.create()
```

### Databricks Workspace Behavior

When running code in a notebook or job in the Databricks workspace: ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

- `DatabricksSession.builder.getOrCreate()` returns the default Spark session (also accessible through the `spark` variable) when used without any additional configuration. The `spark` variable is pre-configured to connect to the compute instance to which the notebook or job is attached. A new Spark session is created if additional connection parameters are set, for example, by using `DatabricksSession.builder.clusterId(...).getOrCreate()` or `DatabricksSession.builder.serverless().getOrCreate()`. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]
- `DatabricksSession.builder.create()` requires explicit connection parameters in a notebook, such as `DatabricksSession.builder.clusterId(...).create()`, otherwise it returns an `[UNSUPPORTED]` error. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

It is possible to use Databricks Connect to connect to Databricks compute that is not attached to the notebook or job using `remote()`, which takes a configuration _kwargs_ or the individual configuration methods, such as `host()` or `token()`. In these cases, a new session is created for the referenced compute, similar to when it is used outside of a Databricks notebook or job. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

For notebooks running on serverless compute, by default queries time out after 9000 seconds. You can customize this by setting the Spark configuration property `spark.databricks.execution.timeout`. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) - The client library for connecting to Databricks from local development environments
- [DatabricksSession](/concepts/databrickssession.md) - The session object for managing Spark connections via Databricks Connect
- Databricks Runtime - The runtime environment that includes Databricks Connect APIs
- Serverless Compute on Databricks - Compute environment with specific timeout behavior for Databricks Connect

## Sources

- databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md

# Citations

1. [databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md](/references/databricks-connect-support-in-databricks-notebooks-databricks-on-aws-dd50e122.md)
