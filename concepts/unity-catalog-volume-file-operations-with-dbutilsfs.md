---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4fe5655cd847c31c0c17cec0c14359215475cc6986427ae408023d739e02d1c3
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-volume-file-operations-with-dbutilsfs
    - UCVFOWD
  citations:
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
title: Unity Catalog Volume File Operations with dbutils.fs
description: Through Databricks Connect, dbutils.fs can perform file operations like put, head, and rm on Unity Catalog volume paths
tags:
  - databricks
  - unity-catalog
  - file-operations
timestamp: "2026-06-18T11:42:39.079Z"
---

# Unity Catalog Volume File Operations with `dbutils.fs`

**Unity Catalog Volume File Operations with `dbutils.fs`** describes how to use the Databricks Utilities file system module (`dbutils.fs`) through the `WorkspaceClient` in the Databricks SDK for Python to read, write, and delete files stored in Unity Catalog volumes. This approach is available when using [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) (Databricks Runtime 13.3 LTS and above) as well as in regular Databricks notebooks.

## Prerequisites

Before you can perform volume file operations with `dbutils.fs`, you must:

- Have a Unity Catalog volume created and accessible in your workspace.
- Initialize a `WorkspaceClient` instance with valid Databricks authentication (see [Initializing WorkspaceClient](/concepts/workspaceclient-dbutils.md)).
- Use Databricks Connect (for remote IDE or custom application usage) or run the code directly in a Databricks notebook.

## Available dbutils.fs Operations

Within `w.dbutils.fs` (where `w` is a `WorkspaceClient` instance), the following operations are commonly used for volume file management: ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

| Method | Description |
|--------|-------------|
| `put(file, contents, overwrite)` | Writes contents to a file at the given path. Set `overwrite=True` to replace an existing file. |
| `head(file)` | Reads and returns the first portion (default 65,536 bytes) of a file’s contents as a string. |
| `rm(file)` | Deletes the file at the given path. |

The path to a Unity Catalog volume follows the pattern:

```
/Volumes/<catalog>/<schema>/<volume>/<path-to-file>
```

^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Example: Create, Read, and Delete a File in a Volume

The following example demonstrates the full lifecycle of a file in a Unity Catalog volume using `dbutils.fs`: ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

# Initialize the WorkspaceClient (assumes DATABRICKS_HOST and DATABRICKS_TOKEN are set)
w = WorkspaceClient()

file_path = "/Volumes/main/default/my-volume/zzz_hello.txt"
file_data = "Hello, Databricks!"

fs = w.dbutils.fs

# Write the file (overwrite if it exists)
fs.put(file=file_path, contents=file_data, overwrite=True)

# Read the file content
print(fs.head(file_path))

# Delete the file
fs.rm(file_path)
```

## Important Notes

- `dbutils.fs` and `dbutils.secrets` are the only Databricks Utilities modules exposed through the `WorkspaceClient.dbutils` property in Databricks Connect. Other utilities (like `dbutils.widgets`) are not available. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]
- You can use the full Databricks SDK for Python to call any Databricks REST API, not just the utilities shown here. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]
- The Databricks SDK for Python does **not** use the `SPARK_REMOTE` environment variable for Databricks Connect; authentication must be configured via `host`/`token` parameters, a config profile, or environment variables (`DATABRICKS_HOST`, `DATABRICKS_TOKEN`). ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- dbutils.fs – The file system utility reference
- [WorkspaceClient](/concepts/workspaceclient-dbutils.md) – The SDK client that provides access to `dbutils`
- Unity Catalog volumes – The storage abstraction for non-tabular data
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) – The framework for remote execution
- Databricks SDK for Python – The underlying library for REST API access

## Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
