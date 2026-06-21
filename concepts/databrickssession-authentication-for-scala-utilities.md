---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: be9839f1d5ba312e17759c825253f82723e50ebb2c48fb101e279565a9a2f56f
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databrickssession-authentication-for-scala-utilities
    - DAFSU
  citations:
    - file: databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md
title: DatabricksSession authentication for Scala Utilities
description: Authentication for the Databricks Utilities for Scala library is determined through initializing the DatabricksSession class in the Databricks Connect project for Scala.
tags:
  - databricks
  - scala
  - authentication
timestamp: "2026-06-19T14:55:16.690Z"
---

# [DatabricksSession](/concepts/databrickssession.md) Authentication for Scala Utilities

**DatabricksSession authentication for Scala Utilities** refers to the mechanism by which the [Databricks Utilities for Scala](/concepts/databricks-utilities-for-scala-library.md) library authenticates API calls when used through [Databricks Connect](/concepts/databricks-connect.md). The authentication is determined by how the `DatabricksSession` class is initialized in the Scala project.

## Overview

When using Databricks Utilities with [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md), authentication for the Scala Utilities library is controlled entirely through the initialization of the `DatabricksSession` class. The `DBUtils.getDBUtils` method, which provides access to DBFS and [Secrets Utility (dbutils.secrets)](/concepts/databricks-utilities-dbutils-via-connect.md) functionality, inherits its authentication configuration from the session. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Authentication Flow

The authentication for Scala Utilities follows a chain of configuration that originates from the `DatabricksSession` setup. This means that the same authentication method used to connect Databricks Connect to a Databricks workspace is automatically used for utility operations such as reading from Unity Catalog Volumes or managing secrets. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Supported Authentication Methods

Because `DatabricksSession` authentication determines utility authentication, all authentication methods supported by [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) are available, including:

- [OAuth (machine-to-machine)](/concepts/machine-to-machine-m2m-authentication.md)
- Databricks Personal Access Token
- Azure Service Principal
- Azure Active Directory Token
- Databricks CLI Profile

The specific method is configured during the `DatabricksSession` initialization in the Scala project's application code or configuration files. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Example: Initializing [DatabricksSession](/concepts/databrickssession.md) with Authentication

The following example demonstrates initializing `DatabricksSession` with Databricks Connect, which then determines authentication for subsequent utility calls:

```scala
import com.databricks.sdk.[[databrickssession|DatabricksSession]]

// Authentication is configured via [[databrickssession|DatabricksSession]] initialization
val session = [[databrickssession|DatabricksSession]].builder()
  .host("https://your-workspace.cloud.databricks.com")
  .token("your-personal-access-token")
  .build()
```

After the session is initialized, `DBUtils.getDBUtils()` uses the same authentication context for file system and secrets operations. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Configuration Options

Authentication configuration can be provided through several mechanisms that are resolved during `DatabricksSession` initialization:

| Method | Description |
|--------|-------------|
| Environment variables | `DATABRICKS_HOST`, `DATABRICKS_TOKEN` |
| Configuration files | `.databrickscfg` profile-based authentication |
| Direct API | Builder methods providing host, token, or other credentials |
| OAuth | Machine-to-machine OAuth with client ID and secret |

The resolution order follows the standard Databricks SDK chain of configuration sources. ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Security Considerations

- Authentication credentials are managed through the `DatabricksSession` instance and are not exposed directly through utility APIs.
- The utility library does not define its own authentication; it relies entirely on the session's configuration.
- [Secrets Utility (dbutils.secrets)](/concepts/databricks-utilities-dbutils-via-connect.md) operations are authenticated through this same mechanism, providing secure access to [Databricks Secret Scopes](/concepts/databricks-secret-scopes.md). ^[databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) – The framework that enables remote cluster connectivity.
- [Databricks Session](/concepts/databrickssession.md) – The session object that manages authentication and configuration.
- [DBUtils.getDBUtils](/concepts/dbutilsgetdbutils.md) – The entry point for accessing Databricks Utilities in Scala.
- [Databricks Utilities for Scala library](/concepts/databricks-utilities-for-scala-library.md) – The library providing utility access methods.
- [Databricks SDK Authentication](/concepts/databricks-sdk-authentication-methods.md) – The underlying authentication framework.

## Sources

- databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-scala-databricks-on-aws-9ada6571.md)
