---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a89a245fb3917d4cfda79bccb6d1e1c72e5c187dede6d35213173ac6cc68da96
  pageDirectory: concepts
  sources:
    - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-utilities-dbutils-via-databricks-connect
    - DU(VDC
  citations:
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
title: Databricks Utilities (dbutils) via Databricks Connect
description: The supported subset of Databricks Utilities commands accessible through Databricks Connect, including dbutils.fs for file operations and dbutils.secrets for secrets management.
tags:
  - utilities
  - dbutils
  - filesystem
  - secrets
timestamp: "2026-06-19T14:46:35.728Z"
---

# Databricks Utilities (dbutils) via Databricks Connect

**Databricks Utilities (dbutils) via Databricks Connect** refers to the ability to use a subset of the dbutils module when working with [Databricks Connect](/concepts/databricks-connect.md), the client library that allows you to run Spark jobs remotely on a Databricks cluster from local IDEs, notebook servers, or custom applications. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Supported Utilities

When using Databricks Connect, you can access commands from two dbutils modules: ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

- **dbutils.fs** — The file system utility, with support for: `cp`, `head`, `ls`, `mkdirs`, `mv`, `put`, `rm`.
- **[dbutils.secrets](/concepts/databricks-secret-scopes.md)** — The secrets utility, with support for: `get`, `getBytes`, `list`, `listScopes`.

## Usage in Python

### Importing DBUtils

To access dbutils from a Python client, import `DBUtils` from `pyspark.dbutils` after creating a SparkSession: ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

```python
from pyspark.sql import SparkSession
from pyspark.dbutils import DBUtils

spark = SparkSession.builder.getOrCreate()
dbutils = DBUtils(spark)
```

### Checking dbutils Availability

For Databricks Runtime 7.3 LTS and above, you can define a helper function that works both locally and on Databricks clusters: ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

```python
def get_dbutils(spark):
    from pyspark.dbutils import DBUtils
    return DBUtils(spark)
```

For older versions of Databricks Runtime, use the following fallback function that checks whether the client is running locally or on a cluster: ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

```python
def get_dbutils(spark):
    if spark.conf.get("spark.databricks.service.client.enabled") == "true":
        from pyspark.dbutils import DBUtils
        return DBUtils(spark)
    else:
        import IPython
        return IPython.get_ipython().user_ns["dbutils"]
```

### Usage in Scala

Scala users can access dbutils in Databricks Connect through the `dbutils` variable available in the Spark shell, or by importing the appropriate libraries. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Copying Files Between Local and Remote Filesystems

Using `dbutils.fs`, you can copy files between your local development machine and remote filesystems. The `file:/` scheme refers to the local filesystem on the client: ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

```python
from pyspark.dbutils import DBUtils
dbutils = DBUtils(spark)

# Copy from local to remote
dbutils.fs.cp('file:/home/user/data.csv', 'dbfs:/uploads')

# Copy from remote to local
dbutils.fs.cp('dbfs:/output/results.csv', 'file:/home/user/downloads/')
```

The maximum file size that can be transferred this way is 250 MB. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Enabling dbutils.secrets.get

Due to security restrictions, the ability to call `dbutils.secrets.get` is disabled by default in Databricks Connect. To enable this feature for your workspace, you must contact Databricks support. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Unsupported dbutils Utilities

The following dbutils utilities are **not supported** when using Databricks Connect: ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

- **dbutils.credentials** — Credentials utility
- **[dbutils.library](/concepts/databricks-utilities-for-scala-library.md)** — Library utility
- **dbutils.widgets** — Widgets utility
- **dbutils.notebook** — Notebook workflow utility

## Example: Listing Files and Secrets

The following example demonstrates listing files in DBFS root and listing available secret scopes: ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

```python
from pyspark.sql import SparkSession
from pyspark.dbutils import DBUtils

spark = SparkSession.builder.getOrCreate()
dbutils = DBUtils(spark)

# List files in DBFS root
print(dbutils.fs.ls("dbfs:/"))

# List available secret scopes
print(dbutils.secrets.listScopes())
```

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library for connecting to remote Databricks clusters
- dbutils — The comprehensive Databricks Utilities module reference
- dbutils.fs — File system utility commands
- [dbutils.secrets](/concepts/databricks-secret-scopes.md) — Secrets management utility
- Databricks SQL Connector for Python — An alternative for Python development with SQL queries
- Databricks Runtime — The runtime environment on the cluster

## Sources

- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md

# Citations

1. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)
