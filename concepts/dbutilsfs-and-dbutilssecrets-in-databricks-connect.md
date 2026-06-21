---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7856674ecbae4ebf8537ad4bfc468079d8aa24b07c51953fe3c9146e5de6d96a
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dbutilsfs-and-dbutilssecrets-in-databricks-connect
    - dbutils.secrets in Databricks Connect and dbutils.fs
    - DADIDC
  citations:
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
title: dbutils.fs and dbutils.secrets in Databricks Connect
description: The only two Databricks Utilities accessible through the dbutils variable in Databricks Connect for Python
tags:
  - databricks
  - utilities
  - filesystem
  - secrets
timestamp: "2026-06-19T14:54:16.197Z"
---

# dbutils.fs and dbutils.secrets in Databricks Connect

**dbutils.fs** and **dbutils.secrets** are two Databricks Utilities that can be accessed through [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) by using the `WorkspaceClient` class from the Databricks SDK for Python. These utilities enable file system operations and secret management from remote client environments such as IDEs, notebook servers, and custom applications. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

This functionality is available for Databricks Connect on Databricks Runtime 13.3 LTS and above. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Accessing dbutils.fs and dbutils.secrets

To use `dbutils.fs` and `dbutils.secrets` in Databricks Connect, you must first initialize a `WorkspaceClient` instance. This class belongs to the [Databricks SDK for Python](https://pypi.org/project/databricks-sdk) and is included with Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

Once the `WorkspaceClient` is initialized, you access the utilities through the `dbutils` variable on the client object:

- `w.dbutils.fs` — provides access to the [Databricks Utilities fs](/concepts/databricks-utilities-for-scala-library.md) (file system utility)
- `w.dbutils.secrets` — provides access to the [Databricks Utilities secrets](/concepts/databricks-secret-scopes.md) (secrets utility)

^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

No other Databricks Utilities functionality is available through `dbutils` in Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

Note that you can also use the Databricks SDK for Python to access any available Databricks REST API, not just the limited subset of Databricks Utilities. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Initializing the WorkspaceClient

To initialize `WorkspaceClient`, you must provide workspace URL and authentication credentials. The Databricks SDK for Python does **not** recognize the `SPARK_REMOTE` environment variable used for Databricks Connect authentication. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

You can authenticate in several ways:

```python
from databricks.sdk import WorkspaceClient
```

### Option 1: Hard-coded credentials (not recommended)

```python
w = WorkspaceClient(
    host=f"https://{retrieve_workspace_instance_name()}",
    token=retrieve_token()
)
```

Databricks does not recommend this approach as it can expose sensitive information such as access tokens if your code is shared or checked into version control. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

### Option 2: Configuration profile

```python
w = WorkspaceClient(profile="<profile-name>")
```

This method uses a [configuration profile](/concepts/databricks-configuration-profiles.md) that contains `host` and `token` fields. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

### Option 3: Environment variables

```python
w = WorkspaceClient()
```

This method reads the `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Example: File operations with dbutils.fs

The following example demonstrates using `dbutils.fs` through Databricks Connect to create a file in a Unity Catalog volume, read its contents, and delete it. This example assumes that `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables are already set: ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

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

## Related Concepts

- Databricks Utilities — The complete set of utility commands available in Databricks notebooks
- Databricks SDK for Python — The Python SDK that provides the `WorkspaceClient` class and REST API access
- [Databricks Connect](/concepts/databricks-connect.md) — The overall framework for connecting remote clients to Databricks clusters
- [Databricks Utilities fs](/concepts/databricks-utilities-for-scala-library.md) — The file system utility for dbutils
- [Databricks Utilities secrets](/concepts/databricks-secret-scopes.md) — The secrets utility for dbutils
- Unity Catalog volumes — Storage volumes managed by Unity Catalog

## Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
