---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2440bccb8116fc57f514b6f402490e737a944030c5fba348e53acbcefb5cabab
  pageDirectory: concepts
  sources:
    - user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - udf-dependency-sources
    - UDS
    - UDFs
    - Managed UDF Dependencies
    - Managing UDF Dependencies
    - UDF Dependencies
  citations:
    - file: user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md
title: UDF Dependency Sources
description: "Dependencies for Databricks Connect UDFs can come from three sources: PyPI packages (PEP 508), Unity Catalog volumes (dbfs: paths), and local files (local: paths including .whl, .tar.gz, folders, and .py files)."
tags:
  - databricks-connect
  - udf
  - dependencies
  - packaging
timestamp: "2026-06-19T23:23:11.141Z"
---

## UDF Dependency Sources

**UDF Dependency Sources** are the origins from which Python packages and modules can be installed for use inside user-defined functions (UDFs) when using [Databricks Connect for Python](/concepts/databricks-connect-for-python.md). This feature is in Public Preview and allows users to specify dependencies that a UDF requires beyond the base environment provided by the cluster or serverless compute. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

Dependencies can be specified via the `DatabricksEnv.withDependencies()` method, which accepts one or more dependency strings. The dependencies are installed on Databricks compute as part of the UDF's Python environment and become available to all UDFs that use that Spark session. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Supported Sources

Three categories of dependency sources are supported:

1. **PyPI packages** – Specified according to PEP 508 dependency specification syntax. Examples include `dice`, `pyjokes<1`, or `simplejson==3.19.*`. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

2. **Unity Catalog volumes packages** – Both built distributions (`.whl`) and source distributions (`.tar.gz`) stored in a [Unity Catalog](/concepts/unity-catalog.md) volume. These are specified using the `dbfs:` scheme, for example `dbfs:/Volumes/users/someone@example.com/wheels/my_private_dep-3.20.2-py3-none-any.whl`. The user must have the `READ_FILE` permission on the file in the [Unity Catalog](/concepts/unity-catalog.md) volume. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

3. **Local packages, folders, and Python files** – Local built distributions (`.whl`), source distributions (`.tar.gz`), folders, or Python files. These are specified using the `local:` scheme, for example `local:/path/to/my_private_dep-3.20.2-py3-none-any.whl` or `local:./path/to/my_file.py`. Both absolute and relative paths are supported. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

All local and volume dependencies must comply with standard Python packaging specifications (PEP 427 for wheels, PEP 241 for source distributions). ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Automatic Dependency Management

In addition to manual specification, [Databricks Connect](/concepts/databricks-connect.md) provides a `withAutoDependencies()` API that automatically discovers and uploads local modules and public PyPI dependencies used in UDF import statements. This feature is in Public Preview and requires [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) 18.1 or above, Python 3.12 locally, and a cluster running Databricks Runtime 18.1 or above. The workspace preview **Enhanced Python UDFs in Unity Catalog** must be enabled. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

The method accepts two parameters:
- `upload_local`: When `True`, local modules imported in UDFs are automatically packaged as zip artifacts and uploaded to the UDF sandbox.
- `use_index`: When `True`, public PyPI dependencies are automatically discovered and installed on Databricks compute, using the locally installed package versions to ensure consistency. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

Automatic discovery does not support dynamic imports (`importlib.import_module`), namespace packages (e.g., `azure.eventhub`), dependencies installed via direct-URL references, or packages from private indices. Dependency discovery works only in Python scripts, IPython Shell, and Jupyter Notebooks; it does not work in a plain Python shell. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Behavior in Databricks Notebooks and Jobs

When running in notebooks or jobs, UDF dependencies must be installed directly in the REPL. [Databricks Connect](/concepts/databricks-connect.md) validates the REPL environment by checking that all specified dependencies are already installed and throws an exception if they are missing. This validation runs for PyPI and [Unity Catalog](/concepts/unity-catalog.md) volume dependencies but not for local dependencies. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Limitations

- UDF dependency support for `foreach` requires [Databricks Connect](/concepts/databricks-connect.md) 18.0+ and Databricks Runtime 18.0+.
- Support for `foreachBatch` requires the same versions but is not available on serverless compute.
- Local package support requires [Databricks Connect](/concepts/databricks-connect.md) 18.1+ and Databricks Runtime 18.1+.
- Dependencies are not supported for pandas aggregation UDFs over window functions.
- Volume and local packages must follow standard Python packaging specifications. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Related Concepts

- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md)
- [User-defined functions (UDFs)](/concepts/abac-user-defined-functions-udfs.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- PyPI
- Python packaging

### Sources

- user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md](/references/user-defined-functions-in-databricks-connect-for-python-databricks-on-aws-d446d035.md)
