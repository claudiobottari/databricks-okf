---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8489623bc5e882fe9a189b60bff87549885bf3f550562835d625494c54ee0a83
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dbutilsfs-via-databricks-connect
    - DVDC
  citations:
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
title: dbutils.fs via Databricks Connect
description: The file system utility from Databricks Utilities accessible through WorkspaceClient.dbutils.fs for file operations on Databricks volumes.
tags:
  - databricks
  - file-system
  - dbutils
timestamp: "2026-06-19T18:15:30.134Z"
---

# dbutils.fs via Databricks Connect

**dbutils.fs via Databricks Connect** refers to using the [Databricks Utilities](/databricks-utilities) file system utility (`dbutils.fs`) from a local development environment through [Databricks Connect](/databricks-connect). This method allows you to read, write, and manage files on Databricks (including in Unity Catalog volumes) without running code inside a notebook or cluster.

## Overview

Databricks Connect enables popular IDEs, notebook servers, and custom applications to connect to a Databricks cluster. When using the Python client, the `WorkspaceClient` class (from the [Databricks SDK for Python](/databricks-sdk-for-python), included in Databricks Connect) provides a `dbutils` variable. Through this variable you can access `dbutils.fs` (file system utility) and `dbutils.secrets` (secrets utility). No other Databricks Utilities are available through `dbutils`. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## How to Access `dbutils.fs`

1. Initialize a `WorkspaceClient` instance with appropriate authentication.
2. Access the file system utility via `w.dbutils.fs`.

The methods available mirror those of the standard [Databricks Utilities fs](/databricks-utilities#file-system-utility-dbutilsfs). The example below demonstrates `put`, `head`, and `rm` operations on a Unity Catalog volume. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Authentication

The `WorkspaceClient` must authenticate with the workspace. Several methods are supported:

- **Hard-coded credentials** (not recommended): provide `host` and `token` directly.
- **Configuration profile**: create a profile with `host` and `token` fields (see [configuration profiles](/databricks-authentication-profiles)).
- **Environment variables**: set `DATABRICKS_HOST` and `DATABRICKS_TOKEN` (same variables used for Databricks Connect). The `WorkspaceClient()` constructor picks them up automatically.

The Databricks SDK for Python does **not** recognize the `SPARK_REMOTE` environment variable for Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Example: Create a File in a Volume

The following snippet creates a file named `zzz_hello.txt` in a Unity Catalog volume, reads its content, and deletes it. It assumes `DATABRICKS_HOST` and `DATABRICKS_TOKEN` are already set.

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

## Limitations

- Only `dbutils.fs` and `dbutils.secrets` are exposed through `WorkspaceClient.dbutils`. Other Databricks Utilities (e.g., `widgets`, `notebook`, `exit`) are not available. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]
- The `SPARK_REMOTE` environment variable is not recognized; use `DATABRICKS_HOST`/`DATABRICKS_TOKEN` or a profile. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The framework underlying this capability.
- Databricks Utilities – Overview of all utility commands.
- Databricks SDK for Python – The SDK providing `WorkspaceClient`.
- Unity Catalog volumes – Target storage for file operations.
- [dbutils.secrets via Databricks Connect](/concepts/dbutilssecrets-via-databricks-connect.md) – The secrets counterpart.

## Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
