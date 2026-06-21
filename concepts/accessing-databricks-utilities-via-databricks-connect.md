---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6f7c7a806bf26c7b2abc5b64cfeb8a7db2f478d027b6efe450b1dc0a18a01b06
  pageDirectory: concepts
  sources:
    - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - accessing-databricks-utilities-via-databricks-connect
    - ADUVDC
  citations:
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
title: Accessing Databricks Utilities via Databricks Connect
description: How to use dbutils.fs and dbutils.secrets utilities through Databricks Connect, including file copy operations between local and remote filesystems and accessing secrets.
tags:
  - dbutils
  - utilities
  - filesystem
timestamp: "2026-06-19T18:09:36.889Z"
---

# Accessing Databricks Utilities via Databricks Connect

**Databricks Connect** allows you to access a subset of Databricks Utilities (`dbutils`) from your local development environment when connected to a remote Databricks cluster. This enables you to use familiar utility commands for file system operations and secret management while working from an IDE, notebook server, or custom application.

## Supported Utilities

When using Databricks Connect, you can access commands from two `dbutils` modules:

- **`dbutils.fs`** — File system utility commands for working with DBFS and other filesystems.
- **`dbutils.secrets`** — Secrets utility commands for managing and retrieving secrets.

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Supported `dbutils.fs` Commands

The following file system commands are supported:

- `dbutils.fs.cp`
- `dbutils.fs.head`
- `dbutils.fs.ls`
- `dbutils.fs.mkdirs`
- `dbutils.fs.mv`
- `dbutils.fs.put`
- `dbutils.fs.rm`

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Supported `dbutils.secrets` Commands

The following secrets commands are supported:

- `dbutils.secrets.get`
- `dbutils.secrets.getBytes`
- `dbutils.secrets.list`
- `dbutils.secrets.listScopes`

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Usage Patterns

### Basic Usage in Python

To use `dbutils` with Databricks Connect, import `DBUtils` from `pyspark.dbutils` and instantiate it with your Spark session:

```python
from pyspark.sql import SparkSession
from pyspark.dbutils import DBUtils

spark = SparkSession.builder.getOrCreate()
dbutils = DBUtils(spark)

print(dbutils.fs.ls("dbfs:/"))
print(dbutils.secrets.listScopes())
```

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Cross-Environment Compatibility

When using Databricks Runtime 7.3 LTS or above, you can define a helper function that works both locally (via Databricks Connect) and on Databricks clusters:

```python
def get_dbutils(spark):
    from pyspark.dbutils import DBUtils
    return DBUtils(spark)
```

For older Databricks Runtime versions, use an alternative pattern that checks the cluster environment:

```python
def get_dbutils(spark):
    if spark.conf.get("spark.databricks.service.client.enabled") == "true":
        from pyspark.dbutils import DBUtils
        return DBUtils(spark)
    else:
        import IPython
        return IPython.get_ipython().user_ns["dbutils"]
```

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Copying Files Between Local and Remote Filesystems

You can use `dbutils.fs` to copy files between your local machine and remote filesystems. The `file:/` scheme refers to the local filesystem on the client:

```python
from pyspark.dbutils import DBUtils

dbutils = DBUtils(spark)
dbutils.fs.cp('file:/home/user/data.csv', 'dbfs:/uploads')
dbutils.fs.cp('dbfs:/output/results.csv', 'file:/home/user/downloads/')
```

The maximum file size that can be transferred this way is **250 MB**.

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Enabling `dbutils.secrets.get`

Due to security restrictions, the ability to call `dbutils.secrets.get` is **disabled by default**. To enable this feature for your workspace, you must contact Databricks support and request that it be enabled.

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Unsupported Utilities

The following Databricks Utilities modules are **not supported** when using Databricks Connect:

- `dbutils.credentials`
- `dbutils.library`
- `dbutils.notebook.workflow`
- `dbutils.widgets`

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that enables remote Spark execution.
- Databricks Utilities (dbutils) — The full reference for all available utilities.
- DBUtils File System Commands — Details on `dbutils.fs` operations.
- [DBUtils Secrets Commands](/concepts/dbutilssecrets-via-databricks-connect.md) — Details on `dbutils.secrets` operations.
- Databricks Secrets — Managing secrets in Databricks.

## Sources

- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md

# Citations

1. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)
