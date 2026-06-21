---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9d7c4472098de10eaac02247eb3516b3f612cdd1e1c0e7a6f6c479b104de9fd6
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databrickssession-initialization-for-authentication
    - DIFA
    - SparkSession Initialization
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: DatabricksSession initialization for authentication
description: Authentication for the Databricks Utilities for Scala library is determined through initializing the DatabricksSession class in a Databricks Connect for Scala project.
tags:
  - databricks-connect
  - scala
  - authentication
timestamp: "2026-06-18T11:42:52.777Z"
---

# [DatabricksSession](/concepts/databrickssession.md) initialization for authentication

**DatabricksSession initialization for authentication** refers to the process by which the authentication configuration for Databricks Utilities in a [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) project is determined. The `DatabricksSession` class, when initialized in the client project, establishes the authentication context that the Databricks Utilities library subsequently uses for operations such as DBFS access and secrets management.^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Role in Authentication for Databricks Utilities

When you use [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md), the authentication for the [Databricks Utilities for Scala](/concepts/databricks-utilities-for-scala-library.md) library — specifically for `DBUtils.getDBUtils` — is not configured separately. Instead, it is derived from the `DatabricksSession` instance that you initialize in your Scala project. This means that setting up authentication correctly at session creation time is the prerequisite for all subsequent Databricks Utilities calls that interact with Databricks resources, such as writing to or reading from [Unity Catalog](/concepts/unity-catalog.md) volumes.^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

The `DatabricksSession` class is part of the Databricks Connect client library. The Databricks Utilities for Scala library declares a dependency on the Databricks Connect client library, so no explicit additional dependency is needed.^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Initialization Context

Because the authentication flow is driven entirely by `DatabricksSession`, any credentials, profiles, or environment variables that configure the session will be inherited by the Utilities library. The source material does not describe specific authentication methods (e.g., OAuth, personal access tokens, Azure AD tokens); the session initialization mechanism itself is the sole documented factor that determines authentication for Utilities.^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Example Workflow

A typical workflow in Scala involves:

1. Initializing `DatabricksSession` with appropriate authentication configuration.
2. Calling `DBUtils.getDBUtils()` to obtain the `dbutils` object.
3. Using `dbutils.fs` or `dbutils.secrets` in a manner consistent with the session’s permissions.

No explicit authentication setup for Databricks Utilities is required beyond the session initialization step.^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — The client library that provides `DatabricksSession`
- [Databricks Utilities for Scala](/concepts/databricks-utilities-for-scala-library.md) — The library that depends on the session for authentication
- [DBUtils](/concepts/dbutilsnotebookrun.md) — The entry point for accessing filesystem and secrets utilities
- [Databricks Utilities authentication](/concepts/databricks-sdk-authentication-methods.md) — Broader topic of how authentication works for various Databricks Utilities

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
