---
title: User-defined functions in Databricks Connect for Python | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/udf
ingestedAt: "2026-06-18T08:06:31.754Z"
---

note

This article covers Databricks Connect for Databricks Runtime 13.3 and above.

Databricks Connect for Python supports [user-defined functions (UDF)](https://docs.databricks.com/aws/en/udf/). When a DataFrame operation that includes UDFs is executed, the UDFs are serialized by Databricks Connect and sent to the server as part of the request.

For information about UDFs for Databricks Connect for Scala, see [User-defined functions in Databricks Connect for Scala](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/udf).

note

Because the user-defined function is serialized and deserialized, the Python version of the client must match the Python version on the Databricks compute. For supported versions, see the [version support matrix](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements#versions).

## Define a UDF[​](#define-a-udf "Direct link to Define a UDF")

To create a UDF in Databricks Connect for Python, use one of the following supported functions:

*   PySpark user-defined functions
    *   [pyspark.sql.udf](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.udf.html)
    *   [pyspark.sql.pandas\_udf](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.pandas_udf.html)
    *   [pyspark.sql.udtf](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.udtf.html)
    *   [pyspark.sql.DataFrame.mapInPandas](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.mapInPandas.html)
    *   [pyspark.sql.DataFrame.mapInArrow](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.mapInArrow.html)
    *   [pyspark.sql.GroupedData.applyInPandas](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.GroupedData.applyInPandas.html)
    *   [pyspark.sql.GroupedData.applyInArrow](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.GroupedData.applyInArrow.html)
    *   [pyspark.sql.PandasCogroupedOps.applyInPandas](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.PandasCogroupedOps.applyInPandas.html)
    *   [pyspark.sql.PandasCogroupedOps.applyInArrow](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.PandasCogroupedOps.applyInArrow.html)
*   PySpark streaming functions
    *   [pyspark.sql.streaming.DataStreamWriter.foreach](https://spark.apache.org/docs/latest/api/python/reference/pyspark.ss/api/pyspark.sql.streaming.DataStreamWriter.foreach.html)
    *   [pyspark.sql.streaming.DataStreamWriter.foreachBatch](https://spark.apache.org/docs/latest/api/python/reference/pyspark.ss/api/pyspark.sql.streaming.DataStreamWriter.foreachBatch.html)
    *   [pyspark.sql.streaming.StatefulProcessor](https://docs.databricks.com/aws/en/stateful-applications)

For example, the following Python sets up a simple UDF that squares the values in a column.

Python

    from pyspark.sql.functions import col, udffrom pyspark.sql.types import IntegerTypefrom databricks.connect import DatabricksSession@udf(returnType=IntegerType())def double(x):    return x * xspark = DatabricksSession.builder.getOrCreate()df = spark.range(1, 2)df = df.withColumn("doubled", double(col("id")))df.show()

## Manage UDF dependencies[​](#manage-udf-dependencies "Direct link to manage-udf-dependencies")

Preview

This feature is in [Public Preview](https://docs.databricks.com/aws/en/release-notes/release-types) and requires Databricks Connect for Python 16.4 or above, and a cluster running Databricks Runtime 16.4 or above. To use this feature, enable the preview **Enhanced Python UDFs in Unity Catalog** in your workspace.

Databricks Connect supports specifying Python dependencies that are required for UDFs. These dependencies are installed on Databricks compute as part of the UDF's Python environment.

This feature allows users to specify dependencies that the UDF needs in addition to the packages provided in the base environment. It can also be used to install a different version of the package from what is provided in the [base environment](#base-env).

Dependencies can be installed from the following sources:

*   PyPI packages
    *   PyPI packages can be specified according to [PEP 508](https://peps.python.org/pep-0508/), for example, `dice`, `pyjokes<1` or `simplejson==3.19.*`.
*   Packages stored in Unity Catalog volumes
    *   Both built distributions (`.whl`) and source distributions (`.tar.gz`) are supported.
    *   Unity Catalog volumes packages can be specified as `dbfs:<path>`, for example, `dbfs:/Volumes/users/someone@example.com/wheels/my_private_dep-3.20.2-py3-none-any.whl` or `dbfs:/Volumes/users/someone@example.com/tars/my_private_dep-4.0.0.tar.gz`.
    *   The user must be granted `READ_FILE` permission on the file in the re:\[UC\] volume. Granting this permission to all account users automatically enables this for new users.
*   Local packages, folders, and Python files
    *   Local built distributions (`.whl`), source distributions (`.tar.gz`), folders and Python files can be specified as `local:<path>`, for example: `local:/path/to/my_private_dep-3.20.2-py3-none-any.whl`, `local:/path/to/my_private_dep-4.0.0.tar.gz`, `local:/path/to/my_folder`, `local:/path/to/my_file.py`.
    *   Both absolute and relative paths are supported, for example: `local:/path/to/my_file.py` or `local:./path/to/my_file.py`.

To include custom dependencies in your UDF, specify them in an environment using `withDependencies`, then use that environment to create a Spark session. The dependencies are installed on your Databricks compute and will be available in all UDFs that use this Spark session.

The following code declares the PyPI package `dice` as a dependency:

Python

    from databricks.connect import DatabricksSession, DatabricksEnvenv = DatabricksEnv().withDependencies("dice==3.1.0")spark = DatabricksSession.builder.withEnvironment(env).getOrCreate()

Or, to specify a dependency of a wheel in a volume:

Python

    from databricks.connect import DatabricksSession, DatabricksEnvenv = DatabricksEnv().withDependencies("dbfs:/Volumes/users/someone@example.com/wheels/my_private_dep-3.20.2-py3-none-any.whl")spark = DatabricksSession.builder.withEnvironment(env).getOrCreate()

### Behavior in Databricks notebooks and jobs[​](#behavior-in-databricks-notebooks-and-jobs "Direct link to Behavior in Databricks notebooks and jobs")

In notebooks and jobs, UDF dependencies need to be installed directly in the REPL. Databricks Connect validates the REPL Python environment by verifying that all specified dependencies are already installed and throws an exception if any are not installed. Notebook environment validation runs for both PyPI and Unity Catalog volume dependencies, but not for local dependencies.

### Limitations[​](#limitations "Direct link to Limitations")

*   UDF dependencies support for `pyspark.sql.streaming.DataStreamWriter.foreach` requires Databricks Connect for Python 18.0 or above, and a cluster running Databricks Runtime 18.0 or above.
*   UDF dependencies support for `pyspark.sql.streaming.DataStreamWriter.foreachBatch` requires Databricks Connect for Python 18.0 or above, and a cluster running Databricks Runtime 18.0 or above. The feature is not supported on serverless.
*   UDF dependencies support for local packages, folders, and Python files requires Databricks Connect for Python 18.1 or above, and a cluster running Databricks Runtime 18.1 or above.
*   UDF dependencies are not supported for pandas aggregation UDFs over window functions.
*   Unity Catalog volumes packages and local packages must be packaged following the standard Python packaging specifications from [PEP-427](https://peps.python.org/pep-0427/) or later for wheel built distributions and [PEP-241](https://peps.python.org/pep-0241/) or later for tar source distributions. For more information on Python packaging standards, see the [PyPA documentation](https://packaging.python.org/en/latest/specifications/).

### Examples[​](#examples "Direct link to Examples")

The following example defines PyPI and volumes dependencies in an environment, creates a session with that environment, then defines and calls UDFs that use those dependencies:

Python

    from databricks.connect import DatabricksSession, DatabricksEnvfrom pyspark.sql.functions import udf, col, pandas_udffrom pyspark.sql.types import IntegerType, LongType, StringTypeimport pandas as pdpypi_deps = ["pyjokes>=0.8,<1"]volumes_deps = [    # Example library from: https://pypi.org/project/dice/#files    "dbfs:/Volumes/main/someone@example.com/test/dice-4.0.0.tar.gz",]local_deps = [    # Example library from: https://pypi.org/project/simplejson/#files    "local:./test/simplejson-3.20.2-py3-none-any.whl",]env = DatabricksEnv().withDependencies(pypi_deps).withDependencies(volumes_deps).withDependencies(local_deps)spark = DatabricksSession.builder.withEnvironment(env).getOrCreate()# UDFs@udf(returnType=StringType())def get_joke():    from pyjokes import get_joke    return get_joke()@udf(returnType=IntegerType())def double_and_json_parse(x):    import simplejson    return simplejson.loads(simplejson.dumps(x * 2))@pandas_udf(returnType=LongType())def multiply_and_add_roll(a: pd.Series, b: pd.Series) -> pd.Series:    import dice    return a * b + dice.roll(f"1d10")[0]df = spark.range(1, 10)df = df.withColumns({    "joke": get_joke(),    "doubled": double_and_json_parse(col("id")),    "mutliplied_with_roll": multiply_and_add_roll(col("id"), col("doubled"))})df.show()

## Automatic management of UDF dependencies[​](#automatic-management-of-udf-dependencies "Direct link to automatic-management-of-udf-dependencies")

Preview

This feature is in [Public Preview](https://docs.databricks.com/aws/en/release-notes/release-types) and requires Databricks Connect for Python 18.1 or above, Python 3.12 on your local machine, and a cluster running Databricks Runtime 18.1 or above. To use this feature, enable the preview **Enhanced Python UDFs in Unity Catalog** in your workspace.

The Databricks Connect `withAutoDependencies()` API enables automatic discovery and upload of local modules and public PyPI dependencies used in the import statements in your UDFs. It removes the need to manually specify dependencies.

The following code enables automatic dependency management:

Python

    from databricks.connect import DatabricksSession, DatabricksEnvenv = DatabricksEnv().withAutoDependencies(upload_local=True, use_index=True)spark = DatabricksSession.builder.withEnvironment(env).getOrCreate()

The `withAutoDependencies()` method accepts the following parameters:

*   `upload_local`: When set to `True`, local modules imported in your UDFs are automatically discovered, packaged, and uploaded to UDF sandbox.
*   `use_index`: When set to `True`, public PyPI dependencies used in your UDFs are automatically discovered and installed on Databricks compute. The discovery process uses the installed packages on your local machine to determine versions, ensuring consistency between your local environment and the remote execution environment.

### Limitations[​](#limitations-1 "Direct link to Limitations")

*   Dynamic imports (for example, `importlib.import_module("foo")`) are not supported.
*   Namespace packages (for example, `azure.eventhub` and `google.cloud.aiplatform`) are not supported.
*   Dependencies installed using direct-URL references are not supported. This includes those installed from local wheel files.
*   Dependencies installed from private package indices are not supported. Packages installed this way can't be distinguished from packages installed from the public PyPI.
*   Dependency discovery doesn't work in a Python shell. Only Python scripts, IPython shell and Jupyter Notebooks are supported.

### Examples[​](#examples-1 "Direct link to Examples")

The following example demonstrates automatic dependency management with both local modules and PyPI packages. This example requires that you have installed `simplejson` and `dice` (using `pip install simplejson dice`).

First, create local helper modules:

Python

    # my_helper.pydef double(x):    return 2 * x

Python

    # my_json.pyimport simplejsondef loads(x):    return simplejson.loads(x)def dumps(x):    return simplejson.dumps(x)

Then, in your main script, import these modules and use them in UDFs:

Python

    # main.pyimport dice as dcfrom databricks.connect import DatabricksSession, DatabricksEnvfrom pyspark.sql.functions import col, udffrom pyspark.sql.types import IntegerType, FloatTypeimport my_jsonfrom my_helper import doubleenv = DatabricksEnv().withAutoDependencies(upload_local=True, use_index=True)spark = DatabricksSession.builder.withEnvironment(env).getOrCreate()@udf(returnType=IntegerType())def double_and_json_parse(x):    return my_json.loads(my_json.dumps(double(x)))@udf(returnType=FloatType())def sum_and_add_noise(x, y):    return x + y + (dc.roll("d6")[0] / 6)df = spark.range(1, 10)df = df.withColumns({    "doubled": double_and_json_parse(col("id")),    "summed_with_noise": sum_and_add_noise(col("id"), col("doubled")),})df.show()

### Logging[​](#logging "Direct link to Logging")

To output discovered dependencies, set the `SPARK_CONNECT_LOG_LEVEL` environment variable to `info` or `debug`. Alternatively, configure the Python logging framework:

Python

    import logginglogging.basicConfig(level=logging.INFO)

The relevant logs are emitted by the `databricks.connect.auto_dependencies` module, for example:

    DEBUG:databricks.connect.auto_dependencies.discovery:Discovered local module: my_jsonDEBUG:databricks.connect.auto_dependencies.discovery:Discovered local module: my_helperDEBUG:databricks.connect.auto_dependencies.discovery:Discovered distribution: simplejson for module simplejsonDEBUG:databricks.connect.auto_dependencies.discovery:Discovered distribution: dice for module diceINFO:databricks.connect.auto_dependencies.hook:Synced zip artifact for: my_jsonINFO:databricks.connect.auto_dependencies.hook:Synced zip artifact for: my_helperINFO:databricks.connect.auto_dependencies.hook:Updated simplejson with auto-detected version ==3.20.2INFO:databricks.connect.auto_dependencies.hook:Updated dice with auto-detected version ==4.0.0

## Python base environment[​](#python-base-environment "Direct link to python-base-environment")

UDFs are executed on the Databricks compute and not on the client. The base Python environment in which UDFs are executed depends on the Databricks compute.

For clusters, the base Python environment is the Python environment of the Databricks Runtime version running on the cluster. The Python version and the list of packages in this base environment are found under the _System environment_ and _Installed Python libraries_ sections of the [Databricks Runtime release notes](https://docs.databricks.com/aws/en/release-notes/runtime/).

For serverless compute, the base Python environment corresponds to the [serverless environment version](https://docs.databricks.com/aws/en/release-notes/serverless/#environment-version) according to the following table. Databricks Connect versions not listed in this table either do not support serverless yet or have reached end-of-support. See [version support matrix](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements#versions) and [end-of-support Databricks Connect versions](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements#end-of-support-versions).
