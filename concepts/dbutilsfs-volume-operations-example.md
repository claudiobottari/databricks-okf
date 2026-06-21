---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 86311deffcc3d746f6569306263e2dde24d28a9eb9e83701e6d3e20cca2d5c6e
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dbutilsfs-volume-operations-example
    - DVOE
  citations:
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
title: dbutils.fs Volume Operations Example
description: A concrete Python example demonstrating file operations (put, head, rm) on Unity Catalog volumes using dbutils.fs via Databricks Connect's WorkspaceClient.
tags:
  - databricks
  - python
  - file-operations
  - unity-catalog
timestamp: "2026-06-18T15:10:08.797Z"
---

# dbutils.fs Volume Operations Example

**dbutils.fs Volume Operations Example** demonstrates how to use the Databricks Utilities file system utility (`dbutils.fs`) with [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) to create, read, and delete files in a Unity Catalog Volume.

## Overview

When using Databricks Connect for Python, the `dbutils` object is accessed through the `WorkspaceClient` class from the Databricks SDK for Python. Only two Databricks Utilities are available through this interface: `dbutils.fs` (file system utility) and `dbutils.secrets` (secrets utility). No other Databricks Utilities functionality is available via `dbutils` in this context. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

The `dbutils.fs` object supports standard file operations such as `put` (write), `head` (read), and `rm` (delete), which can be used to interact with files in Unity Catalog volumes or other accessible paths.

## Prerequisites

- Databricks Connect for Python (Databricks Runtime 13.3 LTS and above).
- The Databricks SDK for Python (included with Databricks Connect).
- A configured Databricks workspace with authentication credentials (host and token).
- An existing Unity Catalog volume (e.g., `/Volumes/main/default/my-volume/`).

## Initializing the Workspace Client

Before using `dbutils.fs`, initialize a `WorkspaceClient` instance with appropriate authentication. Three common approaches are: ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

1. **Using environment variables** `DATABRICKS_HOST` and `DATABRICKS_TOKEN` (recommended):

   ```python
   from databricks.sdk import WorkspaceClient
   w = WorkspaceClient()
   ```

2. **Using a configuration profile**:

   ```python
   w = WorkspaceClient(profile="<profile-name>")
   ```

3. **Hard-coding host and token** (not recommended due to security risks):

   ```python
   w = WorkspaceClient(host="https://<workspace-url>", token="<token>")
   ```

Note that the Databricks SDK for Python does not recognize the `SPARK_REMOTE` environment variable. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Example: Create, Read, and Delete a File in a Volume

The following example demonstrates a complete volume file operation cycle using `dbutils.fs`: ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

file_path = "/Volumes/main/default/my-volume/zzz_hello.txt"
file_data = "Hello, Databricks!"

fs = w.dbutils.fs

# Write the file to the volume
fs.put(
    file     = file_path,
    contents = file_data,
    overwrite = True
)

# Read the file content
print(fs.head(file_path))

# Delete the file
fs.rm(file_path)
```

The `put()` method writes the specified contents to the given file path, with the `overwrite` parameter controlling whether existing files are replaced. The `head()` method returns the first portion of the file (default size limit). The `rm()` method removes the file from the volume.

## Related Concepts

- Databricks Utilities – Overview of all available dbutils features.
- Unity Catalog Volumes – Managed storage locations for files in Unity Catalog.
- [Databricks Connect](/concepts/databricks-connect.md) – How to connect external applications to Databricks clusters.
- [WorkspaceClient](/concepts/workspaceclient-and-dbutils.md) – The SDK class that provides access to Databricks APIs.
- Databricks SDK for Python – Low-level client for Databricks REST APIs.

## Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
