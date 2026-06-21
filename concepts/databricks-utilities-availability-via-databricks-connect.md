---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9e5143d3c8044796f9ae7f1c6c362b31039ee68c072925abb562a1e978b68fd5
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-utilities-availability-via-databricks-connect
    - DUAVDC
  citations:
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
title: Databricks Utilities Availability via Databricks Connect
description: Only dbutils.fs (file system) and dbutils.secrets are available through WorkspaceClient.dbutils in Databricks Connect, not the full set of Databricks Utilities
tags:
  - databricks
  - dbutils
  - limitations
timestamp: "2026-06-18T11:42:13.974Z"
---

# Databricks Utilities Availability via Databricks Connect

**Databricks Utilities Availability via Databricks Connect** describes which Databricks Utilities are accessible when using [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) and how to access them through the Databricks SDK for Python. Databricks Connect enables you to connect popular IDEs, notebook servers, and custom applications to Databricks clusters. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Available Utilities

When using Databricks Connect for Python, you access Databricks Utilities through the `WorkspaceClient` class's `dbutils` variable. The `WorkspaceClient` class belongs to the Databricks SDK for Python and is included in Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

The following Databricks Utilities are available:

- **`dbutils.fs`** — Access the File System Utility (dbutils.fs) for working with files and directories. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]
- **`dbutils.secrets`** — Access the [Secrets Utility (dbutils.secrets)](/concepts/databricks-utilities-dbutils-via-connect.md) for retrieving secrets stored in Databricks secret scopes. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

No other Databricks Utilities functionality is available through `dbutils` in Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

> **Tip:** You can also use the included Databricks SDK for Python to access any available Databricks REST API, not just the Databricks Utilities APIs listed above. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Initializing the WorkspaceClient

To access Databricks Utilities, you must first initialize `WorkspaceClient` with sufficient authentication information for the Databricks SDK. The Databricks SDK for Python does not recognize the `SPARK_REMOTE` environment variable used by Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

### Authentication Methods

**Using environment variables (recommended):** Set the `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables, then initialize without arguments:

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
```

^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

**Using a configuration profile:** Create or specify a [Databricks configuration profile](/concepts/databricks-configuration-profiles.md) containing `host` and `token` fields:

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(profile="<profile-name>")
```

^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

**Using hard-coded values (not recommended):** Directly provide the workspace URL and access token. Databricks does not recommend this option as it can expose sensitive information if code is checked into version control.

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(
    host=f"https://{retrieve_workspace_instance_name()}",
    token=retrieve_token()
)
```

^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Example: Working with Files in a Volume

The following example demonstrates using `dbutils.fs` through Databricks Connect to create a file in a Unity Catalog volume, read its contents, and delete it. This example assumes `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables are already set:

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

## Requirements

This article covers Databricks Connect for Databricks Runtime 13.3 LTS and above. Before using Databricks Utilities with Databricks Connect, you must [set up the Databricks Connect client](/concepts/databricks-connect-client-setup.md). ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library for connecting IDEs and applications to Databricks clusters
- Databricks SDK for Python — The SDK providing `WorkspaceClient` and REST API access
- File System Utility (dbutils.fs) — Utility for file operations on Databricks
- [Secrets Utility (dbutils.secrets)](/concepts/databricks-utilities-dbutils-via-connect.md) — Utility for accessing secrets
- Databricks Utilities — The full set of utility commands available in Databricks notebooks
- Unity Catalog Volumes — Storage volumes in Unity Catalog for file management

## Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
