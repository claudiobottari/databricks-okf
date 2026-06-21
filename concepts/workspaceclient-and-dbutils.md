---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a4f92536124daab30a75bacd13839f2de0a544741628014b0bc0946038f7ce73
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspaceclient-and-dbutils
    - dbutils and WorkspaceClient
    - WAD
    - Initializing WorkspaceClient
    - WorkspaceClient
  citations:
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
title: WorkspaceClient and dbutils
description: The WorkspaceClient class from the Databricks SDK for Python exposes a 'dbutils' variable that provides access to Databricks Utilities (fs and secrets) in Databricks Connect.
tags:
  - databricks
  - sdk
  - python
timestamp: "2026-06-19T09:54:55.935Z"
---

# WorkspaceClient and dbutils

**WorkspaceClient** is a class from the [Databricks SDK for Python](https://pypi.org/project/databricks-sdk) that provides a programmatic interface to Databricks workspaces. Within Databricks Connect for Python (Databricks Runtime 13.3 LTS and above), a `WorkspaceClient` instance exposes a `dbutils` variable that grants access to a subset of Databricks Utilities — specifically the `fs` (file system) and `secrets` utilities. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Initializing WorkspaceClient

Before using `WorkspaceClient`, you must authenticate it with your workspace. The Databricks SDK for Python supports several authentication methods; the source material documents three common approaches:

1. **Hard-code host and token** (not recommended) — Pass the workspace URL and an access token directly to the constructor. This risks exposing sensitive information if the code is shared or version-controlled. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

   ```python
   from databricks.sdk import WorkspaceClient

   w = WorkspaceClient(
       host  = f"https://{retrieve_workspace_instance_name()}",
       token = retrieve_token()
   )
   ```

2. **Use a configuration profile** — Create a [configuration profile](https://docs.databricks.com/aws/en/dev-tools/auth/config-profiles) containing `host` and `token` fields, then pass the profile name. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

   ```python
   w = WorkspaceClient(profile = "<profile-name>")
   ```

3. **Use environment variables** — Set `DATABRICKS_HOST` and `DATABRICKS_TOKEN` (the same variables used for Databricks Connect), then call `WorkspaceClient()` with no arguments. Note that the Databricks SDK for Python does **not** read the `SPARK_REMOTE` environment variable. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

   ```python
   w = WorkspaceClient()
   ```

For additional authentication options (including account‑level access via `AccountClient`), see the Databricks SDK for Python documentation. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Available dbutils Utilities

When using Databricks Connect, `WorkspaceClient.dbutils` exposes only two utilities:

| Utility | Purpose |
|---------|---------|
| `dbutils.fs` | File system operations (e.g., `put`, `head`, `rm`). ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md] |
| `dbutils.secrets` | Secret management. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md] |

No other Databricks Utilities (such as `dbutils.widgets` or `dbutils.notebook`) are available through `WorkspaceClient` in this environment.

Because the Databricks SDK for Python is bundled with Databricks Connect, you can also call any Databricks REST API directly — not just the two utilities above. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Example: File Operations in a Volume

The following example creates a file in a Unity Catalog volume, reads its contents, then deletes it. It assumes `DATABRICKS_HOST` and `DATABRICKS_TOKEN` have been set as environment variables: ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

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

The `head()` method returns the first portion of the file; `rm()` deletes it.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The framework that enables remote execution and provides `WorkspaceClient`.
- Databricks Utilities – Full list of utilities; only `fs` and `secrets` are accessible via `WorkspaceClient` in Databricks Connect.
- Databricks SDK for Python – The broader SDK that includes `WorkspaceClient` and `AccountClient`.
- Authentication for Databricks SDK – Configuration profiles, environment variables, and other authentication methods.
- Unity Catalog Volumes – The storage path used in the example.

## Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
