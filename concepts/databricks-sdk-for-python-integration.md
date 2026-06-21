---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d863e8ba533183cdcdd9b659ef628ad5b1c1c97ce76dc54054f332610d86d136
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-sdk-for-python-integration
    - DSFPI
  citations:
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
title: Databricks SDK for Python Integration
description: The Databricks SDK for Python, included with Databricks Connect, provides not only dbutils access via WorkspaceClient but also full access to any Databricks REST API at both workspace and account levels.
tags:
  - databricks
  - python-sdk
  - api
timestamp: "2026-06-18T15:10:18.573Z"
---

---
title: Databricks SDK for Python Integration
summary: Using the Databricks SDK for Python to interact with Databricks Utilities and REST APIs, especially within Databricks Connect for Python.
sources:
  - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:00:00.000Z"
updatedAt: "2026-06-18T15:00:00.000Z"
tags:
  - databricks
  - python
  - sdk
  - databricks-connect
  - dbutils
  - authentication
aliases:
  - databricks-sdk-for-python-integration
  - DS4PI
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Databricks SDK for Python Integration

The **Databricks SDK for Python Integration** refers to using the official Python SDK (`databricks-sdk`) to interact with Databricks workspaces and [Databricks APIs](/concepts/databrickssession-api.md), particularly within the context of [Databricks Connect for Python](/concepts/databricks-connect-for-python.md). The SDK provides the `WorkspaceClient` class, which allows access to Databricks Utilities (such as `dbutils.fs` and `dbutils.secrets`) and any available [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md).^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Overview

The Databricks SDK for Python is included in Databricks Connect for Python (for Databricks Runtime 13.3 LTS and above). It enables developers to automate Databricks operations from external IDEs, notebook servers, or custom applications. The SDK's `WorkspaceClient` exposes a `dbutils` variable that mirrors the familiar `dbutils` interface used in notebooks, though only the `fs` and `secrets` utilities are available this way.^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Initializing WorkspaceClient

Authentication can be configured in several ways. The SDK does **not** use the `SPARK_REMOTE` environment variable (which is specific to Databricks Connect's Spark session). Instead, the following methods are supported:^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

- **Direct credentials (not recommended)**: Hard-code the workspace host URL and an access token. This may expose sensitive information in version control.
  ```python
  from databricks.sdk import WorkspaceClient
  
  w = WorkspaceClient(
      host=f"https://{retrieve_workspace_instance_name()}",
      token=retrieve_token()
  )
  ```
- **Configuration profile**: Use a stored profile (from `~/.databrickscfg`) that contains `host` and `token` fields:
  ```python
  w = WorkspaceClient(profile="<profile-name>")
  ```
- **Environment variables**: Set `DATABRICKS_HOST` and `DATABRICKS_TOKEN` (or other supported authentication environment variables) and then initialize without arguments:
  ```python
  w = WorkspaceClient()
  ```

For account-level operations, the SDK also provides `AccountClient`. Details on all authentication options are available in the SDK documentation.^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Available Utilities

Only `dbutils.fs` (file system utility) and `dbutils.secrets` (secrets utility) are exposed through the SDK's `WorkspaceClient.dbutils`. Other `dbutils` commands (e.g., `widgets`, `notebook`, `jobs`) are **not** currently available via the SDK.^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

### Example: Creating a File in a Volume

The following example creates a file in a Unity Catalog volume, reads its content, and then deletes it. It assumes `DATABRICKS_HOST` and `DATABRICKS_TOKEN` are set as environment variables:^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

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

The SDK also allows direct access to any [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md) through the `WorkspaceClient`'s methods (e.g., `w.clusters`, `w.jobs`). See the [SDK documentation on PyPI](https://pypi.org/project/databricks-sdk) for the full API reference.^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Relationship to Databricks Connect

Databricks Connect for Python uses the Databricks SDK internally for certain operations. While Databricks Connect primarily focuses on running Spark code on a remote cluster, the SDK extends that by providing a programmatic interface to the workspace itself. This integration allows developers to mix Spark jobs (via Databricks Connect) with workspace management tasks (via the SDK) in a single Python application.^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — The environment in which the SDK is often used.
- Databricks Utilities — The `dbutils` interface exposed through the SDK.
- Databricks REST APIs — All workspace- and account-level APIs accessible via the SDK.
- Unity Catalog Volumes — Object storage paths that can be manipulated with the SDK.
- [WorkspaceClient](/concepts/workspaceclient-and-dbutils.md) — The primary class for workspace interactions.
- AccountClient — The class for account-level API calls.
- Databricks authentication configuration profiles — Alternative authentication using `.databrickscfg`.

## Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
