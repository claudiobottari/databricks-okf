---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 10e5e054e7c8671458ecc1e77c60d28a458d5e6eaf1fd29e54f37d94787777d2
  pageDirectory: concepts
  sources:
    - user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - udf-serialization-in-databricks-connect
    - USIDC
  citations:
    - file: user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md
title: UDF Serialization in Databricks Connect
description: User-defined functions are serialized by the Databricks Connect client and sent to the Databricks compute server for execution, requiring matching Python versions between client and server.
tags:
  - databricks-connect
  - udf
  - serialization
timestamp: "2026-06-19T23:23:00.822Z"
---

## UDF Serialization in [Databricks Connect](/concepts/databricks-connect.md)

**UDF Serialization** refers to the process by which [Databricks Connect](/concepts/databricks-connect.md) for Python serializes user-defined functions (UDFs) and sends them to the remote Databricks compute as part of a query request. When a DataFrame operation that includes UDFs is executed, the function code and its closures are serialized on the client, transmitted to the server, deserialized, and executed in the remote environment. This mechanism applies to [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) version 13.3 and above. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

Because the UDF is serialized on the client and deserialized on the server, the **Python version** of the client must match the Python version running on the Databricks compute. Databricks provides a [Databricks Connect version support matrix](/concepts/databricks-connect-version-compatibility.md) to identify compatible versions. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Defining a UDF

[Databricks Connect](/concepts/databricks-connect.md) supports all standard PySpark UDF APIs, including:
- `pyspark.sql.udf` (scalar UDF)
- `pyspark.sql.pandas_udf` (Pandas UDF)
- `pyspark.sql.udtf` (UDTF)
- DataFrame-level operations such as `mapInPandas`, `mapInArrow`, `applyInPandas`, `applyInArrow`, and `PandasCogroupedOps` methods.
- Streaming functions like `DataStreamWriter.foreach`, `foreachBatch`, and `StatefulProcessor`.

^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

The following example defines a simple scalar UDF that squares values:

```python
from pyspark.sql.functions import col, udf
from pyspark.sql.types import IntegerType
from databricks.connect import [[databrickssession|DatabricksSession]]

@udf(returnType=IntegerType())
def double(x):
    return x * x

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
df = spark.range(1, 2)
df = df.withColumn("doubled", double(col("id")))
df.show()
```

^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Managing UDF Dependencies (Preview)

In [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) 16.4 and above (with cluster Runtime 16.4+ and the **Enhanced Python UDFs in Unity Catalog** preview enabled), users can specify Python dependencies that the UDF requires. These dependencies are installed on the Databricks compute as part of the UDF’s Python environment. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

Dependencies can be sourced from:
- **PyPI packages** – specified according to PEP 508 (e.g., `dice`, `pyjokes<1`).
- **Unity Catalog volumes** – specified as `dbfs:<path>` (e.g., `dbfs:/Volumes/.../my_private_dep.whl`). The user must have `READ_FILE` permission on the file.
- **Local packages, folders, and Python files** – specified as `local:<path>` (e.g., `local:/path/to/my_private_dep.whl`). Both absolute and relative paths are supported.

^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

To include dependencies, create a `DatabricksEnv` with the `withDependencies()` method and pass it when building the Spark session:

```python
from databricks.connect import [[databrickssession|DatabricksSession]], DatabricksEnv

env = DatabricksEnv().withDependencies("dice==3.1.0")
spark = [[databrickssession|DatabricksSession]].builder.withEnvironment(env).getOrCreate()
```

^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

#### Behavior in Databricks Notebooks and Jobs

In notebooks and jobs, UDF dependencies must already be installed in the REPL environment. [Databricks Connect](/concepts/databricks-connect.md) validates that all specified dependencies are present and raises an exception if any are missing. Validation covers PyPI and [Unity Catalog](/concepts/unity-catalog.md) volume dependencies but not local dependencies. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

#### Limitations of Manual Dependency Management

- `foreach` and `foreachBatch` support require [Databricks Connect](/concepts/databricks-connect.md) 18.0+ and Runtime 18.0+; `foreachBatch` is not supported on serverless.
- Local packages, folders, and files require [Databricks Connect](/concepts/databricks-connect.md) 18.1+ and Runtime 18.1+.
- Dependencies are not supported for pandas aggregation UDFs over window functions.
- Local and UC volume packages must follow Python packaging standards (PEP 427/.whl or PEP 241/.tar.gz).

^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

#### Examples

The following shows a session with dependencies from PyPI, a UC volume, and a local wheel, all used in UDFs:

```python
from databricks.connect import [[databrickssession|DatabricksSession]], DatabricksEnv
from pyspark.sql.functions import udf, col, pandas_udf
from pyspark.sql.types import IntegerType, LongType, StringType
import pandas as pd

pypi_deps = ["pyjokes>=0.8,<1"]
volumes_deps = ["dbfs:/Volumes/main/someone@example.com/test/dice-4.0.0.tar.gz"]
local_deps = ["local:./test/simplejson-3.20.2-py3-none-any.whl"]

env = (DatabricksEnv()
       .withDependencies(pypi_deps)
       .withDependencies(volumes_deps)
       .withDependencies(local_deps))
spark = [[databrickssession|DatabricksSession]].builder.withEnvironment(env).getOrCreate()

# UDFs use those dependencies ...
```

^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Automatic Management of UDF Dependencies (Preview)

[Databricks Connect](/concepts/databricks-connect.md) 18.1+ (with Python 3.12 on the local machine, Runtime 18.1+, and the same preview feature enabled) provides the `withAutoDependencies()` API. This feature automatically discovers local modules and public PyPI dependencies imported by your UDFs and uploads/packages them for remote execution. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

Usage:

```python
env = DatabricksEnv().withAutoDependencies(upload_local=True, use_index=True)
spark = [[databrickssession|DatabricksSession]].builder.withEnvironment(env).getOrCreate()
```

- `upload_local=True`: automatically packages and uploads local modules imported in UDFs.
- `use_index=True`: automatically discovers public PyPI dependencies and installs them on the compute using the same versions as on the local machine.

^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

#### Limitations of Automatic Dependency Management

- Dynamic imports (`importlib.import_module`) are not supported.
- Namespace packages (e.g., `azure.eventhub`) are not supported.
- Dependencies installed via direct-URL references or from private indices are not supported.
- Dependency discovery does not work in a plain Python shell; it requires a Python script, IPython shell, or Jupyter Notebook.

^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

#### Example

After installing `simplejson` and `dice` locally, create helper modules and use them in UDFs:

```python
# my_helper.py
def double(x): return 2 * x

# my_json.py
import simplejson
def loads(x): return simplejson.loads(x)
def dumps(x): return simplejson.dumps(x)
```

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

# use UDFs ...
```

^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

#### Logging

To see which dependencies were discovered, set the environment variable `SPARK_CONNECT_LOG_LEVEL` to `info` or `debug`, or configure Python logging. The module `databricks.connect.auto_dependencies` emits logs like:

    DEBUG:databricks.connect.auto_dependencies.discovery:Discovered local module: my_json
    INFO:databricks.connect.auto_dependencies.hook:Synced zip artifact for: my_json

^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Python Base Environment

UDFs execute on the Databricks compute, not on the client. For **clusters**, the base Python environment is the environment of the Databricks Runtime version running on the cluster. The Python version and preinstalled packages are listed in the Databricks Runtime Release Notes under "System environment" and "Installed Python libraries". ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

For **serverless compute**, the base Python environment corresponds to the Serverless Environment Version as documented in the serverless release notes. [Databricks Connect](/concepts/databricks-connect.md) versions not listed in the compatibility tables either do not support serverless yet or have reached end-of-support. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

## Sources

- user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md](/references/user-defined-functions-in-databricks-connect-for-python-databricks-on-aws-d446d035.md)
