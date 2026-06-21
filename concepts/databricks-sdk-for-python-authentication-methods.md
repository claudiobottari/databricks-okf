---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0052e2751bb58b1dd77b6ae8caf89368ec1fbf1a3afe2703be12836cf9bcbebd
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-sdk-for-python-authentication-methods
    - DSFPAM
  citations:
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
title: Databricks SDK for Python Authentication Methods
description: "Three ways to authenticate the WorkspaceClient: hard-coded host/token, configuration profiles, or environment variables (DATABRICKS_HOST and DATABRICKS_TOKEN). The SPARK_REMOTE environment variable is not supported."
tags:
  - databricks
  - authentication
  - python
  - sdk
timestamp: "2026-06-19T09:54:58.869Z"
---

# Databricks SDK for Python Authentication Methods

**Databricks SDK for Python Authentication Methods** refers to the ways in which the Databricks SDK for Python (used by `WorkspaceClient` and `AccountClient`) authenticates with a Databricks workspace or account. The SDK supports multiple authentication strategies, including hard-coded credentials, configuration profiles, and environment variables, allowing flexible integration into different development and production environments. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Overview

The Databricks SDK for Python provides a unified client that can authenticate to a workspace or account using several mechanisms. The choice of method depends on security requirements, deployment context, and developer workflow. While the SDK includes many authentication options beyond those exposed by the Databricks Connect for Python client, the core principles remain similar. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Supported Authentication Methods

The source material outlines three specific methods that can be used to initialize a `WorkspaceClient`:

### 1. Hard-coded Credentials (Not Recommended)

You can pass the workspace URL and an access token directly as parameters when creating the `WorkspaceClient`. This approach is supported but **not recommended** because it can expose sensitive information if the code is committed to version control or shared. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(
    host=f"https://{retrieve_workspace_instance_name()}",
    token=retrieve_token()
)
```

### 2. Configuration Profile

You can create or specify a [Databricks configuration profile](/concepts/databricks-configuration-profiles.md) that contains the fields `host` and `token`. The client then authenticates using that profile. Profiles are stored locally and can be managed with the Databricks CLI. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(profile="<profile-name>")
```

### 3. Environment Variables

The SDK reads the `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables when no explicit parameters or profile are provided. This method is commonly used in automated pipelines and containerized environments. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
```

> **Note:** The Databricks SDK for Python does **not** recognize the `SPARK_REMOTE` environment variable used by older Databricks Connect versions. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Additional Authentication Options

The Databricks SDK for Python includes many other authentication methods not covered in the source material, such as OAuth, Azure Managed Identity, Service Principal authentication, and more. For a complete list, refer to the [Databricks SDK for Python documentation](https://databricks-sdk-py.readthedocs.io/). The `AccountClient` within the SDK can also be initialized with similar authentication options to access account-level REST APIs. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- Databricks SDK for Python – The underlying SDK that provides authentication and API access.
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) – A companion tool that uses the SDK and supports its authentication methods.
- [Databricks configuration profile](/concepts/databricks-configuration-profiles.md) – A local file storing connection and authentication details.
- [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md) – The API surface accessed after successful authentication.
- OAuth with Databricks – An alternative authentication flow for service principals and end users.

## Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
