---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b6554914299d04a4133d1a4824a2ad5885616b6264e1815e8d8058a1cca1152c
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspaceclient-authentication
    - Workspace authentication
  citations:
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
title: WorkspaceClient Authentication
description: Methods for initializing the Databricks SDK WorkspaceClient including hard-coded credentials, configuration profiles, and environment variables
tags:
  - authentication
  - databricks-sdk
  - python
timestamp: "2026-06-19T14:55:23.104Z"
---

# WorkspaceClient Authentication

**WorkspaceClient Authentication** refers to the process of providing credentials to the `WorkspaceClient` class from the Databricks SDK for Python to enable access to Databricks workspace resources. The `WorkspaceClient` is available through [Databricks Connect](/concepts/databricks-connect.md) for Python and can be used to interact with Databricks Utilities as well as any [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md).

## Overview

To initialize `WorkspaceClient`, you must provide enough information to authenticate the Databricks SDK with the workspace. The SDK offers several authentication methods, each with different trade-offs between convenience and security. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Authentication Methods

### Hard-Coded Credentials (Not Recommended)

You can hard-code the workspace URL and access token directly within your code. While supported, Databricks **does not recommend** this option, as it can expose sensitive information such as access tokens if your code is checked into version control or otherwise shared. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(
    host = f"https://{retrieve_workspace_instance_name()}",
    token = retrieve_token()
)
```

### Configuration Profile

You can create or specify a [configuration profile](/concepts/databricks-configuration-profiles.md) that contains the fields `host` and `token`, and then initialize `WorkspaceClient` using the profile name. This approach keeps credentials separate from your code. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(profile = "<profile-name>")
```

### Environment Variables

You can set the environment variables `DATABRICKS_HOST` and `DATABRICKS_TOKEN` in the same way you set them for Databricks Connect, and then initialize `WorkspaceClient` without any arguments. This is a common approach for development environments. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
```

## Important Notes

- The Databricks SDK for Python does **not** recognize the `SPARK_REMOTE` environment variable used by Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]
- For additional authentication options, as well as how to initialize `AccountClient` within the Databricks SDKs to access Databricks REST APIs at the account level instead of the workspace level, see the Databricks SDK for Python documentation. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Usage

Once authenticated, `WorkspaceClient` provides access to `dbutils.fs` and `dbutils.secrets` for file system and secrets operations, respectively. No other Databricks Utilities functionality is available through `dbutils`. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- Databricks SDK for Python — The SDK that provides the `WorkspaceClient` class
- [Databricks Connect](/concepts/databricks-connect.md) — The client library that enables connection to Databricks clusters from external environments
- Databricks Utilities — The set of utilities for files, secrets, and other workspace operations
- [Configuration Profile](/concepts/databricks-configuration-profiles.md) — A named set of authentication credentials for the Databricks SDK
- AccountClient — The account-level counterpart to `WorkspaceClient`

## Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
