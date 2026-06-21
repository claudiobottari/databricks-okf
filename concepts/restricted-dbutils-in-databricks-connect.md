---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d50239f442107e7a207df05c3784423726d44e20b8b93780b13e416a1a89b1a9
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - restricted-dbutils-in-databricks-connect
    - RDIDC
    - limitations-of-dbutils-in-databricks-connect
    - LODIDC
    - Limitations of Databricks Connect
  citations:
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
title: Restricted dbutils in Databricks Connect
description: Only 'fs' (file system) and 'secrets' Databricks Utilities are available through dbutils in Databricks Connect for Python; all other utilities are unavailable.
tags:
  - databricks
  - utilities
  - limitations
timestamp: "2026-06-19T09:54:50.304Z"
---

# Restricted dbutils in Databricks Connect

**Restricted dbutils in Databricks Connect** refers to the limited subset of Databricks Utilities functionality available when using [Databricks Connect for Python](/concepts/databricks-connect-for-python.md). When connecting to a Databricks cluster from an IDE, notebook server, or custom application via Databricks Connect, only two of the standard dbutils utilities are accessible through the `WorkspaceClient` class. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Available Utilities

When using Databricks Connect with Python, the following Databricks Utilities are available through the `WorkspaceClient` object's `dbutils` variable: ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

- **`dbutils.fs`** — The file system utility (dbutils.fs) for working with files and directories.
- **`dbutils.secrets`** — The secrets utility (dbutils.secrets) for accessing secrets stored in Databricks.

No other Databricks Utilities functionality is available through `dbutils` in Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Access Pattern

To access the restricted dbutils, you must initialize a `WorkspaceClient` instance from the Databricks SDK for Python: ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
fs = w.dbutils.fs
secrets = w.dbutils.secrets
```

The `WorkspaceClient` class is included with Databricks Connect and provides the `dbutils` variable for accessing these utilities. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Authentication

To initialize `WorkspaceClient`, you must provide authentication credentials for the Databricks workspace. The Databricks SDK for Python supports several authentication methods: ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

- **Environment variables**: Set `DATABRICKS_HOST` and `DATABRICKS_TOKEN` (the same variables used for Databricks Connect), then initialize without arguments: `WorkspaceClient()`.
- **Configuration profile**: Create a [Databricks configuration profile](/concepts/databricks-configuration-profiles.md) with `host` and `token` fields, then initialize with: `WorkspaceClient(profile="<profile-name>")`.
- **Hard-coded values**: Pass `host` and `token` directly (not recommended due to security concerns).

The Databricks SDK for Python does **not** recognize the `SPARK_REMOTE` environment variable used by Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Example Usage

The following example demonstrates creating a file in a Unity Catalog volume, reading its contents, and deleting it using the restricted dbutils: ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

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

## Alternative: Using the Databricks SDK Directly

Since the Databricks SDK for Python is included with Databricks Connect, you can also use it to access any available [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md), not just the limited dbutils utilities. This provides a broader range of functionality for automating Databricks operations from your client code. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — The client library for connecting to Databricks clusters
- Databricks SDK for Python — The underlying SDK that provides `WorkspaceClient`
- Databricks Utilities — The full set of utilities available in Databricks notebooks
- File system utility (dbutils.fs) — Available through restricted dbutils
- Secrets utility (dbutils.secrets) — Available through restricted dbutils
- Unity Catalog volumes — Storage locations accessible via dbutils.fs

## Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
