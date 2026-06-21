---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0f550cb324021465d0dcf20cac40e8015461c29e251f57b2e7c130cf953b011b
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-for-python-volume-file-operations
    - DCFPVFO
  citations:
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
    - file: |-
        databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

        ## Related Concepts

        - [[Databricks Connect for Python
title: Databricks Connect for Python Volume File Operations
description: Example pattern demonstrating how to use Databricks SDK's WorkspaceClient and dbutils.fs to create, read, and delete files in Unity Catalog volumes.
tags:
  - databricks
  - file-operations
  - volumes
  - python
timestamp: "2026-06-19T09:55:26.815Z"
---

# Databricks Connect for Python Volume File Operations

**Databricks Connect for Python Volume File Operations** refers to the ability to programmatically interact with [Unity Catalog](/concepts/unity-catalog.md) volumes — specifically creating, reading, and deleting files — using the `dbutils.fs` interface exposed through the `WorkspaceClient` class in the Databricks SDK for Python. This functionality is available in Databricks Connect for Databricks Runtime 13.3 LTS and above. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Overview

Databricks Connect enables you to connect popular IDEs, notebook servers, and custom applications to Databricks clusters. Before using volume file operations, you must [set up the Databricks Connect client](/concepts/databricks-connect-client-setup.md). ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Accessing Databricks Utilities

You access Databricks Utilities through the `WorkspaceClient` class's `dbutils` variable. The `WorkspaceClient` class is part of the Databricks SDK for Python and is included in Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

The following utilities are available through `dbutils`:

- `dbutils.fs` – For Databricks Utilities filesystem operations
- `dbutils.secrets` – For Databricks Utilities secrets operations

No other Databricks Utilities functionality is exposed through `dbutils` in this context. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Initializing the WorkspaceClient

To initialize `WorkspaceClient`, you must provide authentication information. Three approaches are supported: ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

**Hard-coded credentials (not recommended):** You can hard-code the workspace URL and access token directly. Databricks does not recommend this approach because it can expose sensitive information if your code is checked into version control. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient(host=f"https://{retrieve_workspace_instance_name()}", token=retrieve_token())
```

**Configuration profile:** Create or specify a [configuration profile](/concepts/databricks-configuration-profiles.md) containing `host` and `token` fields: ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient(profile="<profile-name>")
```

**Environment variables:** Set `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables: ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()
```

Note: The Databricks SDK for Python does not recognize the `SPARK_REMOTE` environment variable for Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Example: Volume File Operations

The following example demonstrates creating a file in a Unity Catalog volume, reading its contents, and deleting it. This assumes `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables are already set: ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
file_path = "/Volumes/main/default/my-volume/zzz_hello.txt"
file_data = "Hello, Databricks!"
fs = w.dbutils.fs

fs.put(
    file      = file_path,
    contents  = file_data,
    overwrite = True
)

print(fs.head(file_path))
fs.rm(file_path)
```

The `fs.put()` method writes the file with an optional `overwrite` parameter. The `fs.head()` method reads the first bytes of the file. The `fs.rm()` method deletes the file. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

## Related Concepts

- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) – General setup and usage guide
- Databricks Utilities – Full reference of available utilities
- Databricks SDK for Python – The SDK providing `WorkspaceClient` and `dbutils`
- Unity Catalog volumes – The storage abstraction used in file paths
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) – Scala equivalent of this functionality

## Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
2. databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

## Related Concepts

- [[Databricks Connect for Python
