---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 21278866dece82731cffa7c1f77384768d066a8fb019d675f85d3308a30c54cb
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-sdk-for-python-rest-api-access
    - DSFPRAA
  citations:
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
title: Databricks SDK for Python REST API Access
description: The included Databricks SDK for Python can be used to access any available Databricks REST API, beyond just the dbutils utilities
tags:
  - databricks-sdk
  - rest-api
  - python
timestamp: "2026-06-19T14:55:03.588Z"
---

# Databricks SDK for Python REST API Access

**Databricks SDK for Python REST API Access** refers to using the included `databricks-sdk` Python package to call any available Databricks REST API programmatically. The SDK provides a comprehensive client interface for both workspace-level and account-level API operations, extending beyond the limited set of commands available through Databricks Utilities. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Overview

The Databricks SDK for Python is automatically included with [Databricks Connect](/concepts/databricks-connect.md) for Python. Through the `WorkspaceClient` class, developers can access the full range of Databricks REST APIs, not just those exposed by `dbutils`. This enables automation of workflows, resource management, and integration with external applications. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Initialization

To initialize `WorkspaceClient`, you must provide authentication credentials. The Databricks SDK for Python supports multiple authentication methods:

### Hard-coded credentials (not recommended)

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(
    host=f"https://{retrieve_workspace_instance_name()}",
    token=retrieve_token()
)
```

This approach is supported but **not recommended** because it can expose sensitive information like access tokens if the code is checked into version control. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

### Configuration profile

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(profile="<profile-name>")
```

This method uses a [Databricks Configuration Profile](/concepts/databricks-configuration-profiles.md) containing `host` and `token` fields. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

### Environment variables

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
```

This works when the `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables are set. Note that the Databricks SDK for Python does **not** recognize the `SPARK_REMOTE` environment variable used by Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Account-Level Access

For account-level operations, developers can use `AccountClient` instead of `WorkspaceClient`. This provides access to Databricks REST APIs at the account level rather than at the workspace level. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Available Functionality

Through the SDK, you can access:

- All Databricks REST APIs available in your deployment
- `dbutils.fs` for Filesystem Operations
- `dbutils.secrets` for Secrets Management

No Databricks Utilities functionality other than `fs` and `secrets` is available through `dbutils` in the SDK context, but the SDK itself provides direct REST API access for any operation not covered by these utilities. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Example: Filesystem Operations

The following example demonstrates using the SDK to create, read, and delete a file in a Unity Catalog volume:

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

file_path = "/Volumes/main/default/my-volume/zzz_hello.txt"
file_data = "Hello, Databricks!"

fs = w.dbutils.fs
fs.put(
    file=file_path,
    contents=file_data,
    overwrite=True
)

print(fs.head(file_path))
fs.rm(file_path)
```

^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The framework that includes the SDK for remote cluster interaction
- Databricks SDK for Python — The broader SDK package available on PyPI
- [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md) — The full set of API endpoints accessible through the SDK
- Databricks Utilities — The limited subset of utilities exposed through `dbutils`
- Databricks Authentication — Various methods for authenticating SDK requests
- [Databricks Configuration Profile](/concepts/databricks-configuration-profiles.md) — Profile-based authentication configuration
- Unity Catalog Volumes — Storage locations for files accessed in SDK examples

## Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
