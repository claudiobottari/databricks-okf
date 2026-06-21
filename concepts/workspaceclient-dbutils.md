---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: af1dac697a2b8e9fc11ec9f749c94bcf6197e2ebd2c00bd079a33ee67ec2b42e
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspaceclient-dbutils
    - Workspace Client
title: WorkspaceClient dbutils
description: The WorkspaceClient class from the Databricks SDK for Python exposes a dbutils variable that provides access to limited Databricks Utilities through Databricks Connect
tags:
  - databricks
  - sdk
  - dbutils
timestamp: "2026-06-18T11:42:22.531Z"
---

# WorkspaceClient dbutils

**WorkspaceClient dbutils** refers to the `dbutils` attribute on the `WorkspaceClient` class from the Databricks SDK for Python. When used with [Databricks Connect](/concepts/databricks-connect.md) for Python, this attribute provides access to a limited subset of Databricks Utilities — specifically the file system utility (`fs`) and the secrets utility (`secrets`). No other Databricks Utilities functionality is available through this interface.[^source]

## Available Utilities

Through `w.dbutils` (where `w` is a `WorkspaceClient` instance), you can call:

- `w.dbutils.fs` – provides file system operations (e.g., `put`, `head`, `rm`, `ls`, `cp`, `mv`).  
- `w.dbutils.secrets` – provides secret management operations (e.g., `get`, `list`, `listScopes`).

All other Databricks Utilities (such as `dbutils.widgets`, `dbutils.notebook`, `dbutils.jobs`, etc.) are **not** exposed through the `WorkspaceClient.dbutils` object.[^source]

## Initializing WorkspaceClient

To use `WorkspaceClient.dbutils`, you must first create a `WorkspaceClient` instance with valid authentication to your Databricks workspace. The Databricks SDK for Python supports several initialization methods:[^source]

### Hard‑coded credentials (not recommended)

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(
    host=f"https://{retrieve_workspace_instance_name()}",
    token=retrieve_token()
)
```

### Configuration profile

```python
w = WorkspaceClient(profile="<profile-name>")
```

### Environment variables (`DATABRICKS_HOST` and `DATABRICKS_TOKEN`)

```python
w = WorkspaceClient()   # reads DATABRICKS_HOST and DATABRICKS_TOKEN
```

The Databricks SDK for Python does **not** recognise the `SPARK_REMOTE` environment variable used by Databricks Connect.[^source]

## Example: File operations in a Unity Catalog volume

The following example initialises `WorkspaceClient`, writes a file to a Unity Catalog volume, reads its contents, and deletes it. The example assumes `DATABRICKS_HOST` and `DATABRICKS_TOKEN` are set as environment variables.[^source]

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

## Limitations

- Only `dbutils.fs` and `dbutils.secrets` are accessible through `WorkspaceClient.dbutils`. Other dbutils utilities are not available.
- The `SPARK_REMOTE` environment variable is not recognised; authentication must be provided via the SDK’s own configuration mechanisms.[^source]

For any Databricks REST API functionality beyond the two available utilities, you can use the underlying Databricks SDK for Python directly (for example, `w.serving_endpoints`, `w.jobs`, etc.).[^source]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – How to connect IDEs and custom applications to Databricks clusters.
- Databricks SDK for Python – The SDK that provides `WorkspaceClient` and other API wrappers.
- dbutils – The full set of Databricks Utilities available in notebooks and on clusters.
- Unity Catalog volumes – Storage volumes that can be accessed via `dbutils.fs`.
- [Workspace authentication](/concepts/workspaceclient-authentication.md) – Methods for authenticating with a Databricks workspace.

## Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
