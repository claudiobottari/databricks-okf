---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ba57bff9717aed8a11ea259b9b66ba68bf72fda34bad0c84f3a098fac8a3edd6
  pageDirectory: concepts
  sources:
    - user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-udf-dependency-discovery-with-withautodependencies
    - AUDDWW
    - Automatic management of UDF dependencies with withAutoDependencies
  citations:
    - file: user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md
title: Automatic UDF Dependency Discovery with withAutoDependencies
description: Databricks Connect can automatically discover and upload local modules and public PyPI dependencies used in UDF imports, eliminating manual specification via the withAutoDependencies() API.
tags:
  - databricks-connect
  - udf
  - dependencies
  - auto-discovery
timestamp: "2026-06-19T23:23:58.887Z"
---

# Automatic UDF Dependency Discovery with withAutoDependencies

**Automatic UDF Dependency Discovery with withAutoDependencies** is a feature in the [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) API that automatically discovers and manages Python dependencies for user-defined functions (UDFs). It removes the need to manually specify dependencies, streamlining the development workflow for UDFs that rely on local modules and public PyPI packages. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

## Overview

The `withAutoDependencies()` API enables automatic discovery and upload of local modules and public PyPI dependencies used in import statements within UDFs. This eliminates manual dependency specification, simplifying the process of running UDFs on Databricks compute. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

This feature is in Public Preview and requires:
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) 18.1 or above
- Python 3.12 on your local machine
- A cluster running Databricks Runtime 18.1 or above
- The **Enhanced Python UDFs in Unity Catalog** preview enabled in your workspace ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

## Using withAutoDependencies

To enable automatic dependency management, create an environment with `withAutoDependencies()` and use it when building your Spark session: ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]], DatabricksEnv

env = DatabricksEnv().withAutoDependencies(upload_local=True, use_index=True)
spark = [[databrickssession|DatabricksSession]].builder.withEnvironment(env).getOrCreate()
```

### Parameters

The `withAutoDependencies()` method accepts two parameters: ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

- **`upload_local`**: When set to `True`, local modules imported in your UDFs are automatically discovered, packaged, and uploaded to the UDF sandbox.
- **`use_index`**: When set to `True`, public PyPI dependencies used in your UDFs are automatically discovered and installed on Databricks compute. The discovery process uses packages installed on the local machine to determine versions, ensuring consistency between local and remote execution environments.

## How It Works

When `withAutoDependencies()` is enabled, the system scans UDF import statements to identify dependencies. For local modules, it packages them into zip artifacts and uploads them to the UDF sandbox. For public PyPI packages, it detects the installed version on your local machine and installs the same version on Databricks compute. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Example Workflow

The following example demonstrates automatic dependency management with both local modules and PyPI packages. First, create local helper modules: ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

```python
# my_helper.py
def double(x):
    return 2 * x

# my_json.py
import simplejson

def loads(x):
    return simplejson.loads(x)

def dumps(x):
    return simplejson.dumps(x)
```

Then, in your main script, import these modules and use them in UDFs: ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

```python
# main.py
import dice as dc
from databricks.connect import [[databrickssession|DatabricksSession]], DatabricksEnv
from pyspark.sql.functions import col, udf
from pyspark.sql.types import IntegerType, FloatType
import my_json
from my_helper import double

env = DatabricksEnv().withAutoDependencies(upload_local=True, use_index=True)
spark = [[databrickssession|DatabricksSession]].builder.withEnvironment(env).getOrCreate()

@udf(returnType=IntegerType())
def double_and_json_parse(x):
    return my_json.loads(my_json.dumps(double(x)))

@udf(returnType=FloatType())
def sum_and_add_noise(x, y):
    return x + y + (dc.roll("d6")[0] / 6)

df = spark.range(1, 10)
df = df.withColumns({
    "doubled": double_and_json_parse(col("id")),
    "summed_with_noise": sum_and_add_noise(col("id"), col("doubled")),
})
df.show()
```

## Limitations

Automatic dependency discovery has the following limitations: ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

- **Dynamic imports** (for example, `importlib.import_module("foo")`) are not supported.
- **Namespace packages** (for example, `azure.eventhub` and `google.cloud.aiplatform`) are not supported.
- **Direct-URL reference installations** are not supported, including those from local wheel files.
- **Private package index dependencies** are not supported, as packages installed this way cannot be distinguished from public PyPI packages.
- **Dependency discovery** does not work in a Python shell. Only Python scripts, IPython shells, and Jupyter Notebooks are supported.

## Logging

To view discovered dependencies, set the `SPARK_CONNECT_LOG_LEVEL` environment variable to `info` or `debug`, or configure the Python logging framework: ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

```python
import logging
logging.basicConfig(level=logging.INFO)
```

Relevant logs are emitted by the `databricks.connect.auto_dependencies` module: ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

```
DEBUG:databricks.connect.auto_dependencies.discovery:Discovered local module: my_json
DEBUG:databricks.connect.auto_dependencies.discovery:Discovered local module: my_helper
DEBUG:databricks.connect.auto_dependencies.discovery:Discovered distribution: simplejson for module simplejson
DEBUG:databricks.connect.auto_dependencies.discovery:Discovered distribution: dice for module dice
INFO:databricks.connect.auto_dependencies.hook:Synced zip artifact for: my_json
INFO:databricks.connect.auto_dependencies.hook:Updated simplejson with auto-detected version ==3.20.2
INFO:databricks.connect.auto_dependencies.hook:Updated dice with auto-detected version ==4.0.0
```

## Related Concepts

- User-defined functions in Databricks Connect for Python — The foundation for creating and managing UDFs
- [Managing UDF dependencies with withDependencies](/concepts/manual-udf-dependency-management-with-withdependencies.md) — The manual approach for specifying UDF dependencies
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — The client library for connecting to Databricks compute
- Databricks Runtime 18.1 — The required runtime version for this feature

## Sources

- user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md](/references/user-defined-functions-in-databricks-connect-for-python-databricks-on-aws-d446d035.md)
