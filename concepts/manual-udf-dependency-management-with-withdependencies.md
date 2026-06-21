---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 78a6e4d24f01a5b8db2531a595033693f80d8994c851efea771d49cd85b4746d
  pageDirectory: concepts
  sources:
    - user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - manual-udf-dependency-management-with-withdependencies
    - MUDMWW
    - Managing UDF dependencies with withDependencies
  citations:
    - file: user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md
    - file: |-
        user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md

        ## Behavior in Databricks Notebooks and Jobs

        In notebooks and jobs
    - file: UDF dependencies need to be installed directly in the REPL. Databricks Connect validates the REPL Python environment by verifying that all specified dependencies are already installed and throws an exception if any are not installed. Notebook environment validation runs for both PyPI and Unity Catalog volume dependencies
    - file: but not for local dependencies. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md
title: Manual UDF Dependency Management with withDependencies
description: Databricks Connect allows explicit specification of Python dependencies for UDFs via the withDependencies() API, supporting PyPI packages, Unity Catalog volumes, and local packages.
tags:
  - databricks-connect
  - udf
  - dependencies
timestamp: "2026-06-19T23:23:54.714Z"
---

# Manual UDF Dependency Management with withDependencies

**Manual UDF Dependency Management with withDependencies** is a feature in [Databricks Connect](/concepts/databricks-connect.md) for Python that allows users to explicitly specify Python dependencies required by user-defined functions (UDFs). Dependencies are installed on Databricks compute as part of the UDF's Python environment. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

## Overview

When using [Databricks Connect](/concepts/databricks-connect.md), UDFs are serialized and sent to the server for execution. The `withDependencies()` method on `DatabricksEnv` enables users to declare dependencies that the UDF needs in addition to the packages provided in the [Python base environment](/concepts/python-base-environment-for-udf-execution.md). This can also be used to install a different version of a package than what is provided in the base environment. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

## Supported Dependency Sources

Dependencies can be installed from the following sources: ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

- **PyPI packages**: Specified according to [PEP 508](https://peps.python.org/pep-0508/), for example, `dice`, `pyjokes<1`, or `simplejson==3.19.*`.
- **Packages stored in [Unity Catalog](/concepts/unity-catalog.md) volumes**: Both built distributions (`.whl`) and source distributions (`.tar.gz`) are supported. These are specified as `dbfs:<path>`, for example, `dbfs:/Volumes/users/someone@example.com/wheels/my_private_dep-3.20.2-py3-none-any.whl`. The user must be granted `READ_FILE` permission on the file in the [Unity Catalog](/concepts/unity-catalog.md) volume.
- **Local packages, folders, and Python files**: Local built distributions (`.whl`), source distributions (`.tar.gz`), folders, and Python files can be specified as `local:<path>`, for example, `local:/path/to/my_private_dep-3.20.2-py3-none-any.whl`. Both absolute and relative paths are supported.

## Usage

To include custom dependencies in UDFs, specify them in an environment using `withDependencies`, then use that environment to create a Spark session. Dependencies are installed on Databricks compute and are available in all UDFs that use that Spark session. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Basic Example: PyPI Package

```python
from databricks.connect import [[databrickssession|DatabricksSession]], DatabricksEnv

env = DatabricksEnv().withDependencies("dice==3.1.0")
spark = [[databrickssession|DatabricksSession]].builder.withEnvironment(env).getOrCreate()
```
^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Example: [Unity Catalog](/concepts/unity-catalog.md) Volume Package

```python
from databricks.connect import [[databrickssession|DatabricksSession]], DatabricksEnv

env = DatabricksEnv().withDependencies(
    "dbfs:/Volumes/users/someone@example.com/wheels/my_private_dep-3.20.2-py3-none-any.whl"
)
spark = [[databrickssession|DatabricksSession]].builder.withEnvironment(env).getOrCreate()
```
^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Example: Multiple Dependency Sources

```python
from databricks.connect import [[databrickssession|DatabricksSession]], DatabricksEnv

pypi_deps = ["pyjokes>=0.8,<1"]
volumes_deps = [
    "dbfs:/Volumes/main/someone@example.com/test/dice-4.0.0.tar.gz",
]
local_deps = [
    "local:./test/simplejson-3.20.2-py3-none-any.whl",
]

env = (
    DatabricksEnv()
    .withDependencies(pypi_deps)
    .withDependencies(volumes_deps)
    .withDependencies(local_deps)
)
spark = [[databrickssession|DatabricksSession]].builder.withEnvironment(env).getOrCreate()
```
^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md

## Behavior in Databricks Notebooks and Jobs

In notebooks and jobs, UDF dependencies need to be installed directly in the REPL. Databricks Connect validates the REPL Python environment by verifying that all specified dependencies are already installed and throws an exception if any are not installed. Notebook environment validation runs for both PyPI and Unity Catalog volume dependencies, but not for local dependencies. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

## Limitations

- UDF dependencies support for `pyspark.sql.streaming.DataStreamWriter.foreach` requires [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) 18.0 or above, and a cluster running Databricks Runtime 18.0 or above. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]
- UDF dependencies support for `pyspark.sql.streaming.DataStreamWriter.foreachBatch` requires [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) 18.0 or above, and a cluster running Databricks Runtime 18.0 or above. This feature is not supported on serverless. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]
- UDF dependencies support for local packages, folders, and Python files requires [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) 18.1 or above, and a cluster running Databricks Runtime 18.1 or above. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]
- UDF dependencies are not supported for pandas aggregation UDFs over window functions. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]
- [Unity Catalog](/concepts/unity-catalog.md) volumes packages and local packages must be packaged following standard Python packaging specifications from [PEP-427](https://peps.python.org/pep-0427/) (for wheel built distributions) or [PEP-241](https://peps.python.org/pep-0241/) (for tar source distributions). ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- User-defined functions in Databricks Connect for Python
- [Automatic management of UDF dependencies with withAutoDependencies](/concepts/automatic-udf-dependency-discovery-with-withautodependencies.md)
- [DatabricksSession](/concepts/databrickssession.md)
- [Python base environment](/concepts/python-base-environment-for-udf-execution.md)
- Unity Catalog volumes

## Requirements

This feature is in Public Preview and requires: ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) 16.4 or above
- A cluster running Databricks Runtime 16.4 or above
- The workspace preview **Enhanced Python UDFs in Unity Catalog** enabled

## Sources

- user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md](/references/user-defined-functions-in-databricks-connect-for-python-databricks-on-aws-d446d035.md)
2. user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md

## Behavior in Databricks Notebooks and Jobs

In notebooks and jobs
3. UDF dependencies need to be installed directly in the REPL. Databricks Connect validates the REPL Python environment by verifying that all specified dependencies are already installed and throws an exception if any are not installed. Notebook environment validation runs for both PyPI and Unity Catalog volume dependencies
4. but not for local dependencies. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md
