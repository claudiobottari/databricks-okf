---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 68319506a4aabd23d8f13903b914ea0f6b2fa54eff98ef5d902e2ceb049af64c
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspaceclient-authentication-methods
    - WAM
  citations:
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
title: WorkspaceClient Authentication Methods
description: "Three supported authentication approaches for initializing the Databricks SDK WorkspaceClient: hard-coded credentials, configuration profiles, and environment variables (DATABRICKS_HOST and DATABRICKS_TOKEN)."
tags:
  - databricks
  - authentication
  - python-sdk
timestamp: "2026-06-18T15:10:04.316Z"
---

Here is the wiki page for "WorkspaceClient Authentication Methods".

---

## WorkspaceClient Authentication Methods

**WorkspaceClient Authentication Methods** refers to the various techniques available to authenticate a `WorkspaceClient` object from the Databricks SDK for Python, enabling it to connect securely to a Databricks workspace for automation tasks.

### Overview

When using the `WorkspaceClient` class—which is part of the Databricks SDK for Python and included with [Databricks Connect](/concepts/databricks-connect.md)—you must provide sufficient authentication information to establish a connection with the target workspace. The SDK supports several methods to supply these credentials, and it does **not** recognize the `SPARK_REMOTE` environment variable for Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

### Authentication Methods

#### Hard-Coded Credentials (Not Recommended)

You can explicitly pass the workspace host URL and an access token as arguments to the `WorkspaceClient` constructor. While supported, Databricks **does not recommend** this approach, as it can expose sensitive information—such as access tokens—if your code is checked into version control or otherwise shared. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(
    host=f"https://<workspace-instance-name>",
    token="<your-access-token>"
)
```

#### Configuration Profile

You can create or specify a [configuration profile](/concepts/databricks-configuration-profiles.md) that contains the `host` and `token` fields, and then initialize `WorkspaceClient` by passing the profile name. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
w = WorkspaceClient(profile="<profile-name>")
```

Configuration profiles are a secure way to store credentials outside your code, reducing the risk of accidental exposure. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

#### Environment Variables

You can set the environment variables `DATABRICKS_HOST` and `DATABRICKS_TOKEN` (in the same manner as for Databricks Connect), and then instantiate `WorkspaceClient` with no arguments, which causes the SDK to automatically read these variables. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
w = WorkspaceClient()
```

The Databricks SDK for Python does **not** recognize the `SPARK_REMOTE` environment variable for Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

#### Default Authentication (No Arguments)

When no explicit host or token is provided, `WorkspaceClient()` relies on the SDK’s default authentication chain, which can include environment variables, configuration files, or other configured providers. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

### Additional Options

For more authentication options—including how to initialize the `AccountClient` class to access Databricks REST APIs at the account level (rather than the workspace level)—see the databricks-sdk package on PyPI. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

### Related Concepts

- Databricks SDK for Python – The underlying SDK that provides `WorkspaceClient` and `AccountClient`.
- [Databricks Connect](/concepts/databricks-connect.md) – The framework that enables remote connection to Databricks clusters.
- [Configuration Profiles](/concepts/databricks-configuration-profiles.md) – Secure files for storing authentication credentials.
- Databricks Utilities – The workspace utilities accessed via `dbutils` from a `WorkspaceClient` instance.

### Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
