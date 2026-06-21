---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 66267bb9b2cebdb8f709de50b22f672a471f6bf550205e896d89baeba4fb87f3
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-volume-file-operations-via-dbutils
    - UCVFOVD
  citations:
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
title: Unity Catalog Volume File Operations via dbutils
description: Example workflow for creating, reading, and deleting files in Unity Catalog volumes using dbutils.fs methods like put, head, and rm
tags:
  - unity-catalog
  - volumes
  - file-operations
  - dbutils
timestamp: "2026-06-19T14:55:34.600Z"
---

---
title: Unity Catalog Volume File Operations via dbutils
summary: How to create, read, write, and delete files in Unity Catalog volumes using dbutils.fs with Databricks Connect for Python
sources:
  - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T15:10:42.300Z"
updatedAt: "2026-06-19T15:10:42.300Z"
tags:
  - databricks
  - unity-catalog
  - volumes
  - file-operations
aliases:
  - unity-catalog-volume-file-operations-via-dbutils
  - UCVFOP
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Unity Catalog Volume File Operations via dbutils

**Unity Catalog Volume File Operations via dbutils** refers to using the Databricks Utilities `dbutils.fs` module to create, read, write, and delete files stored in Unity Catalog volumes from a Python application connected to a Databricks cluster via [Databricks Connect](/concepts/databricks-connect.md).

## Overview

Databricks Utilities provides a set of convenience commands for common tasks such as interacting with the Databricks File System (DBFS). When working with Unity Catalog volumes, you can use the `dbutils.fs` sub-module to perform file operations on volume paths. This capability is available through the Databricks SDK for Python, which is included in Databricks Connect for Python. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Prerequisites

- Databricks Connect for Databricks Runtime 13.3 LTS and above.
- The `WorkspaceClient` class must be initialized to authenticate the dbutils calls. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Available Databricks Utilities

When using Databricks Connect for Python, access Databricks Utilities through the `WorkspaceClient` class's `dbutils` variable. The following utilities are available: ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

- **`dbutils.fs`** – File system utility for file operations on DBFS, volumes, and external locations.
- **`dbutils.secrets`** – Secrets utility for retrieving secrets from [Databricks Secret Scopes](/concepts/databricks-secret-scopes.md).

No other Databricks Utilities functionality (such as `dbutils.widgets` or `dbutils.notebook`) is available through `dbutils` in this context. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Initializing the WorkspaceClient

To initialize `WorkspaceClient`, provide authentication information for the Databricks SDK. Supported methods include: ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

- **Configuration profile** – Create a profile with `host` and `token` fields, then initialize:
  ```python
  from databricks.sdk import WorkspaceClient
  w = WorkspaceClient(profile="<profile-name>")
  ```

- **Environment variables** – Set `DATABRICKS_HOST` and `DATABRICKS_TOKEN`, then initialize:
  ```python
  from databricks.sdk import WorkspaceClient
  w = WorkspaceClient()
  ```

- **Hard-coded values** – Provide host and token directly (not recommended, as it may expose sensitive information):
  ```python
  from databricks.sdk import WorkspaceClient
  w = WorkspaceClient(host=f"https://{retrieve_workspace_instance_name()}", token=retrieve_token())
  ```

The Databricks SDK for Python does not recognize the `SPARK_REMOTE` environment variable used by Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Working with Unity Catalog Volumes

Unity Catalog volumes are mounted under the `/Volumes/<catalog>/<schema>/<volume>/` path. You can perform file operations directly on these paths using `dbutils.fs`. The operations respect Unity Catalog's governed data permissions. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

### Example: Create, Read, and Delete a File in a Volume

The following Python example creates a text file in a volume named `my-volume`, reads its content, and then deletes it: ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

file_path = "/Volumes/main/default/my-volume/zzz_hello.txt"
file_data = "Hello, Databricks!"

fs = w.dbutils.fs

# Write a file to the volume
fs.put(
    file=file_path,
    contents=file_data,
    overwrite=True
)

# Read and print the file content
print(fs.head(file_path))

# Delete the file
fs.rm(file_path)
```

After execution, the file `zzz_hello.txt` is created, read, and then removed from the volume. The operations are performed through the Databricks SDK, which communicates with the workspace cluster where the volume resides. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- Databricks Utilities – The full set of utilities and their documentation.
- Unity Catalog Volumes – Governed file storage managed by Unity Catalog.
- [Databricks Connect](/concepts/databricks-connect.md) – Client library that enables remote execution against Databricks clusters.
- Databricks File System (DBFS) – Distributed file system used by Databricks.
- Databricks SDK for Python – The SDK that provides `WorkspaceClient` and `dbutils` access.
- Secrets Utility – How to manage and retrieve secrets with `dbutils.secrets`.

## Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
