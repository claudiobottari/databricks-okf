---
title: Troubleshooting Databricks Connect for Python | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/troubleshooting
ingestedAt: "2026-06-18T08:06:25.286Z"
---

note

This article covers Databricks Connect for Databricks Runtime 13.3 LTS and above.

This article provides troubleshooting information for Databricks Connect for Python. Databricks Connect enables you to connect popular IDEs, notebook servers, and custom applications to Databricks clusters. See [Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/). For the Scala version of this article, see [Troubleshooting Databricks Connect for Scala](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/troubleshooting).

**Issue**: When you try to run code with Databricks Connect, you get an error messages that contains strings such as `StatusCode.UNAVAILABLE`, `StatusCode.UNKNOWN`, `DNS resolution failed`, or `Received http2 header with status: 500`.

**Possible cause**: Databricks Connect cannot reach your cluster.

**Recommended solutions**:

*   Check to make sure that your workspace instance name is correct. If you use environment variables, check to make sure the related environment variable is available and correct on your local development machine.
*   Check to make sure that your cluster ID is correct. If you use environment variables, check to make sure the related environment variable is available and correct on your local development machine.
*   Check to make sure that your cluster has the correct custom cluster version that is compatible with Databricks Connect.

## Python version mismatch[​](#python-version-mismatch "Direct link to Python version mismatch")

Check the Python version you are using locally has at least the same minor release as the version on the cluster (for example, `3.10.11` versus `3.10.10` is OK, `3.10` versus `3.9` is not). For supported versions, see the [version support matrix](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements#versions).

If you have multiple Python versions installed locally, ensure that Databricks Connect is using the right one by setting the `PYSPARK_PYTHON` environment variable (for example, `PYSPARK_PYTHON=python3`).

## Conflicting PySpark installations[​](#conflicting-pyspark-installations "Direct link to conflicting-pyspark-installations")

The `databricks-connect` package conflicts with PySpark. Having both installed will cause errors when initializing the Spark context in Python. This can manifest in several ways, including “stream corrupted” or “class not found” errors. If you have `pyspark` installed in your Python environment, ensure it is uninstalled before installing `databricks-connect`. After uninstalling PySpark, make sure to fully re-install the Databricks Connect package:

Bash

    pip3 uninstall pysparkpip3 uninstall databricks-connectpip3 install --upgrade "databricks-connect==14.0.*"  # or X.Y.* to match your specific cluster version.

Databricks Connect and PySpark are mutually exclusive, but it is possible to use Python virtual environments to do remote development with `databricks-connect` in your IDE and local testing with `pyspark` in a terminal. However, Databricks recommends that you use Databricks Connect for Python with [serverless compute](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config#serverless) for all testing, for the following reasons:

*   Databricks Runtime, and hence `databricks-connect`, contains features that are not available in the OSS `pyspark`.
*   Testing with `databricks-connect` and serverless is faster than testing using `pyspark` locally.
*   Unity Catalog integrations are not available in `pyspark`, so there will be no permissions enforced when you test using `pyspark` locally.
*   For testing end-to-end with an external dependency such as Databricks compute, integration tests, as opposed to unit tests, are best.

If you still choose to connect to a local Spark cluster, you can specify a [connection string](https://github.com/apache/spark/blob/master/sql/connect/docs/client-connection-string.md) using the following:

Python

    connection_string = "sc://localhost"DatabricksSession.builder.remote(connection_string).getOrCreate()

## Errors connecting to Apache Spark server[​](#errors-connecting-to-apache-spark-server "Direct link to errors-connecting-to-apache-spark-server")

Databricks Connect is built against Databricks Runtime, which has different dependencies than open source Apache Spark. Attempting to connect to an open source Apache Spark server (for example, a locally running Apache Spark 3.5.x Spark Connect server at `sc://localhost`), results in errors such as class not found, API behavior mismatches, or serialization failures. In particular, Databricks Connect 15.4 and 16.4 are incompatible with Apache Spark 3.5.x because they use a different version of the `json4s` library.

Use a Databricks cluster or serverless compute instead of an open source Apache Spark server. See [Compute configuration for Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config).

## Conflicting or Missing `PATH` entry for binaries[​](#conflicting-or-missing-path-entry-for-binaries "Direct link to conflicting-or-missing-path-entry-for-binaries")

It is possible your PATH is configured so that commands like `spark-shell` will be running some other previously installed binary instead of the one provided with Databricks Connect. You should make sure either the Databricks Connect binaries take precedence, or remove the previously installed ones.

If you can't run commands like `spark-shell`, it is also possible your PATH was not automatically set up by `pip3 install` and you'll need to add the installation `bin` dir to your PATH manually. It's possible to use Databricks Connect with IDEs even if this isn't set up.

## The filename, directory name, or volume label syntax is incorrect on Windows[​](#the-filename-directory-name-or-volume-label-syntax-is-incorrect-on-windows "Direct link to The filename, directory name, or volume label syntax is incorrect on Windows")

If you are using Databricks Connect on Windows and see:

    The filename, directory name, or volume label syntax is incorrect.

Databricks Connect was installed into a directory with a [space in your path](https://stackoverflow.com/questions/47028892/why-does-spark-shell-fail-with-the-filename-directory-name-or-volume-label-sy). You can work around this by either installing into a directory path without spaces, or configuring your path using the [short name form](https://stackoverflow.com/questions/892555/how-do-i-specify-c-program-files-without-a-space-in-it-for-programs-that-cant).
