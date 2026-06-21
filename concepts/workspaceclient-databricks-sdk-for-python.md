---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5fb49e293519da37549df47a21a50ccfd16cd28275cf62deb097ef46b1218a3f
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspaceclient-databricks-sdk-for-python
    - W(SFP
  citations:
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
title: WorkspaceClient (Databricks SDK for Python)
description: The class used to access Databricks Utilities (dbutils) from external Python environments via the Databricks SDK.
tags:
  - databricks
  - sdk
  - python
timestamp: "2026-06-19T18:15:59.540Z"
---

# WorkspaceClient (Databricks SDK for Python)

**WorkspaceClient** is a class from the [Databricks SDK for Python](https://pypi.org/project/databricks-sdk) that provides a unified interface for interacting with Databricks workspaces. It is included in Databricks Connect for Python and serves as the primary entry point for accessing Databricks REST APIs and utilities programmatically. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Overview

The `WorkspaceClient` class belongs to the `databricks-sdk` package and is designed to simplify authentication and API access to Databricks workspaces. It is the recommended way to access Databricks Utilities when using Databricks Connect for Python (Databricks Runtime 13.3 LTS and above). ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Key Capabilities

Through `WorkspaceClient`, you can:

- Access Databricks Utilities via the `dbutils` variable, providing access to `fs` (file system utility) and `secrets` (secrets utility) — no other Databricks Utilities are available through `dbutils`. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]
- Use the included Databricks SDK for Python to access any available Databricks REST API, not just the utilities APIs. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Initialization

To initialize `WorkspaceClient`, you must provide authentication information. The SDK supports multiple methods:

### Hard-Coded Credentials (Not Recommended)
```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(
    host=f"https://{retrieve_workspace_instance_name()}",
    token=retrieve_token()
)
```
Databricks does not recommend this approach as it can expose sensitive information like access tokens if code is shared or checked into version control. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

### Configuration Profile
```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(profile="<profile-name>")
```
This method uses a [configuration profile](/concepts/databricks-configuration-profiles.md) containing `host` and `token` fields. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

### Environment Variables
```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
```
This method relies on the `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables. The SDK does not recognize `SPARK_REMOTE` for Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Example Usage

The following example demonstrates using `WorkspaceClient` with Databricks utilities to create, read, and delete a file in a Unity Catalog volume:

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
file_path = "/Volumes/main/default/my-volume/zzz_hello.txt"
file_data = "Hello, Databricks!"

fs = w.dbutils.fs
fs.put(file=file_path, contents=file_data, overwrite=True)
print(fs.head(file_path))
fs.rm(file_path)
```
^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Additional Resources

- The Databricks SDK for Python can also initialize `AccountClient` for account-level REST API access.
- For further details, see the [interaction with dbutils](https://databricks-sdk-py.readthedocs.io/en/latest/dbutils.html) documentation.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The framework that integrates IDEs and custom applications with Databricks clusters
- Databricks Utilities — The `dbutils` family of utilities for file system and secrets management
- [Configuration Profile](/concepts/databricks-configuration-profiles.md) — Authentication method using a profile file
- [WorkspaceClient](/concepts/workspaceclient-dbutils.md) (this page) — Core SDK class for workspace-level operations

## Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
