---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 91df8e1a32d3562b98a7fc66bd43ba4a309c146b699948be88ac94952256844e
  pageDirectory: concepts
  sources:
    - databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - limitations-of-dbutils-in-databricks-connect
    - LODIDC
    - Limitations of Databricks Connect
  citations:
    - file: databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md
title: Limitations of dbutils in Databricks Connect
description: Only the fs and secrets Databricks Utilities are available through dbutils in Databricks Connect; all other dbutils utilities are not accessible
tags:
  - databricks
  - limitations
  - utilities
timestamp: "2026-06-19T14:54:31.202Z"
---

## Limitations of dbutils in Databricks Connect

**Databricks Utilities (dbutils)** provide a set of convenient commands for working with files, secrets, widgets, notebooks, and more within Databricks notebooks. However, when using **Databricks Connect** for Python (Databricks Runtime 13.3 LTS and above), only a subset of these utilities is available. This page describes which dbutils commands work with Databricks Connect and which do not, along with the recommended workaround.

### Overview

Databricks Connect enables you to connect popular IDEs, notebook servers, and custom applications to Databricks clusters. Within a Databricks Connect Python session, you access dbutils through the `WorkspaceClient.dbutils` variable. The `WorkspaceClient` class is part of the Databricks SDK for Python. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

Importantly, **no Databricks Utilities functionality other than `dbutils.fs` and `dbutils.secrets` is available through `dbutils`** in Databricks Connect. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

### Available Utilities

The following utilities are directly callable via `w.dbutils.fs` and `w.dbutils.secrets`:

| Utility | Description |
|---------|-------------|
| `dbutils.fs` | File system operations (e.g., put, head, rm, cp, mv, ls, mkdirs, mount, refreshMounts) |
| `dbutils.secrets` | Secret access (e.g., get, getBytes, list, listScopes) |

^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

These correspond to the [fs](https://docs.databricks.com/aws/en/dev-tools/databricks-utils#file-system-utility-dbutilsfs) and [secrets](https://docs.databricks.com/aws/en/dev-tools/databricks-utils#secrets-utility-dbutilssecrets) utilities described in the Databricks Utilities documentation. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

### Unavailable Utilities

All other built-in dbutils utilities are **not available** through `dbutils` when using Databricks Connect. These include but are not limited to:

- `dbutils.widgets` – creating and managing widgets
- `dbutils.notebook` – running notebooks, exit commands
- `dbutils.jobs` – job-related operations
- `dbutils.library` – library management
- `dbutils.credentials` – credential pass-through
- `dbutils.data` – data skew hints

The Databricks documentation explicitly states: "No Databricks Utilities functionality other than the preceding utilities are available through `dbutils`." ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

### Workaround: Using the Databricks SDK for Python

Although the missing utilities are not exposed through `dbutils`, you can access any available Databricks REST API using the included Databricks SDK for Python. The SDK is part of the `WorkspaceClient` and provides methods that correspond to many of the same operations that dbutils would perform (e.g., job management, notebook execution). ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

For details on all available methods, refer to the [Databricks SDK for Python documentation](https://pypi.org/project/databricks-sdk) and the [Databricks SDK for Python dbutils reference](https://databricks-sdk-py.readthedocs.io/en/latest/dbutils.html). ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

### Additional Notes on Authentication

When initializing `WorkspaceClient`, the Databricks SDK for Python does **not** recognize the `SPARK_REMOTE` environment variable that is used by Databricks Connect for client-server communication. Instead, you must authenticate using one of the supported SDK methods, such as hard‑coding host and token, using a configuration profile, or setting the `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables. ^[databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md]

### Related Concepts

- Databricks Utilities – Full list of dbutils commands available in notebook environments.
- [Databricks Connect](/concepts/databricks-connect.md) – Overview of connecting external tools to Databricks clusters.
- [WorkspaceClient](/concepts/workspaceclient-and-dbutils.md) – The Python SDK client used to access dbutils and other APIs.
- Databricks SDK for Python – Programmatic access to Databricks REST APIs.
- [Secrets Utility (dbutils.secrets)](/concepts/databricks-utilities-dbutils-via-connect.md) – Manage secrets in Databricks Connect.
- File System Utility (dbutils.fs) – Manage files in Databricks Connect.

### Sources

- databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-utilities-with-databricks-connect-for-python-databricks-on-aws.md](/references/databricks-utilities-with-databricks-connect-for-python-databricks-on-aws-c10d6dc4.md)
