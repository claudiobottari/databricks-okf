---
title: Databricks Connect support in Databricks notebooks | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/notebooks
ingestedAt: "2026-06-18T08:06:11.922Z"
---

note

This article covers Databricks Connect for Databricks Runtime 13.3 LTS and above.

Databricks Connect allows you to connect to Databricks compute from a local development environment outside of Databricks. You can then develop, debug, and test your code directly from your IDE before moving your code to a notebook or job in Databricks. See [Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/).

## Portability[​](#portability "Direct link to Portability")

To make the transition from local development to deployment to Databricks seamless, all of the Databricks Connect APIs are available in Databricks notebooks as part of the corresponding Databricks Runtime. This allows you to run your code in a Databricks notebook without any changes to your code.

## DatabricksSession behavior[​](#databrickssession-behavior "Direct link to DatabricksSession behavior")

The behavior of `DatabricksSession` differs slightly when using Databricks Connect in a local development environment and in notebooks and jobs in the Databricks workspace.

### Local development environment behavior[​](#local-development-environment-behavior "Direct link to Local development environment behavior")

When running code locally within an IDE outside of Databricks, `DatabricksSession.builder.getOrCreate()` gets the existing Spark session for the provided configuration if it exists, or creates a new Spark session if it doesn't exist. `DatabricksSession.builder.create()` always creates a new Spark session. Connection parameters such as `host`, `token`, and `cluster_id` are populated either from the source code, environment variables, or the `.databrickscfg` configuration profiles file.

In other words, when run using Databricks Connect, the following code creates two separate sessions:

    spark1 = DatabricksSession.builder.create()spark2 = DatabricksSession.builder.create()

### Databricks workspace behavior[​](#databricks-workspace-behavior "Direct link to databricks-workspace-behavior")

When running code in a notebook or job in the Databricks workspace, `DatabricksSession.builder.getOrCreate()` returns the default Spark session (also accessible through the `spark` variable) when used without any additional configuration. The `spark` variable is pre-configured to connect to the compute instance to which the notebook or job is attached. A new Spark session is created if additional connection parameters are set, for example, by using `DatabricksSession.builder.clusterId(...).getOrCreate()` or `DatabricksSession.builder.serverless().getOrCreate()`.

`DatabricksSession.builder.create()` requires explicit connection parameters in a notebook, such as `DatabricksSession.builder.clusterId(...).create()`, otherwise it returns an `[UNSUPPORTED]` error.

It is possible to use Databricks Connect to connect to Databricks compute that is not attached to the notebook or job using `remote()`, which takes a configuration _kwargs_ or the individual configuration methods, such as `host()` or `token()`. In these cases, a new session is created for the referenced compute, similar to when it is used outside of a Databricks notebook or job.

note

For notebooks running on serverless compute, by default queries time out after 9000 seconds. You can customize this by setting the Spark configuration property `spark.databricks.execution.timeout`. See [Set Spark configuration properties on Databricks](https://docs.databricks.com/aws/en/spark/conf).
