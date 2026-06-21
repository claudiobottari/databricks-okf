---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 66915bbb4798236617a80c68b1dfe55c7f9402fdfd11b854ba3d29a783776f18
  pageDirectory: concepts
  sources:
    - user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - python-base-environment-for-udf-execution
    - PBEFUE
    - Python base environment
  citations:
    - file: user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md
title: Python Base Environment for UDF Execution
description: UDFs execute in the Python environment of the Databricks compute (cluster or serverless), not on the client, with specific package sets defined by the Databricks Runtime version or serverless environment version.
tags:
  - databricks-connect
  - udf
  - environment
  - runtime
timestamp: "2026-06-19T23:23:23.599Z"
---

## Python Base Environment for UDF Execution

The **Python Base Environment for UDF Execution** is the runtime environment in which [User-defined functions (UDF)](/concepts/abac-user-defined-functions-udfs.md) run when executed through [Databricks Connect for Python](/concepts/databricks-connect-for-python.md). UDFs are serialized on the client, sent to the server, and executed on the Databricks compute – they do **not** run on the client machine. The configuration of this environment depends entirely on the type of compute being used: a Databricks cluster or serverless compute. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Clusters

For cluster‑based compute, the base Python environment is the Python environment of the Databricks Runtime version running on the cluster. The exact Python version and the list of pre‑installed Python packages are documented in the Databricks Runtime release notes under the *System environment* and *Installed Python libraries* sections. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Serverless Compute

For serverless compute, the base Python environment corresponds to the serverless environment version as defined in a mapping table maintained by Databricks. Not all [Databricks Connect](/concepts/databricks-connect.md) versions support serverless compute; the version support matrix and the list of end-of-support Databricks Connect versions should be consulted to determine compatibility. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Client‑Server Python Version Match

Because UDFs are serialized on the client and deserialized on the server, the Python version used by the client **must match** the Python version on the Databricks compute. The supported version pairings are listed in the version support matrix. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Managing Dependencies on Top of the Base Environment

[Databricks Connect](/concepts/databricks-connect.md) allows users to install additional Python dependencies that are added to the base environment when UDFs run. This feature is in Public Preview and requires [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) 16.4+ and a cluster running Databricks Runtime 16.4+ with the **Enhanced Python UDFs in Unity Catalog** workspace feature enabled.

Dependencies can be specified from three sources:
- **PyPI packages** (PEP 508 format)
- **Packages in Unity Catalog volumes** (`dbfs:/Volumes/...`)
- **Local packages, folders, and Python files** (`local:<path>`)

The `withDependencies()` method of `DatabricksEnv` is used to declare dependencies, and they are installed on the compute as part of the UDF’s Python environment. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

#### Automatic Dependency Management

The `withAutoDependencies()` API (Public Preview, [Databricks Connect](/concepts/databricks-connect.md) 18.1+, Python 3.12 locally, Databricks Runtime 18.1+, same feature flag) automatically discovers and uploads local modules and public PyPI dependencies used in UDF import statements, eliminating the need for manual specification. It supports two modes:
- **`upload_local=True`** – packages and uploads local modules imported in UDFs.
- **`use_index=True`** – discovers public PyPI dependencies from the local installation and installs matching versions on the compute.

**Limitations** of automatic dependency management include:
- Dynamic imports (`importlib.import_module`) are not supported.
- Namespace packages (e.g., `azure.eventhub`, `google.cloud.aiplatform`) are not supported.
- Dependencies installed via direct‑URL references or from private package indices are not supported.
- Dependency discovery does not work in a plain Python shell; only Python scripts, IPython shell, and Jupyter Notebooks are supported. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Related Concepts

- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md)
- [User-defined functions (UDF)](/concepts/abac-user-defined-functions-udfs.md)
- Databricks Runtime release notes
- [Serverless compute](/concepts/serverless-gpu-compute.md)
- Version support matrix
- Unity Catalog volumes

### Sources

- user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md](/references/user-defined-functions-in-databricks-connect-for-python-databricks-on-aws-d446d035.md)
