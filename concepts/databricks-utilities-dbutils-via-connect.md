---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 759328275b474bbeb7c2d22054ae36ea11ba072981d6ea8b929a52eb90fda08a
  pageDirectory: concepts
  sources:
    - databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-utilities-dbutils-via-connect
    - DU(VC
    - Databricks Utilities (DBUtils)
    - Secrets Utility (dbutils.secrets)
  citations:
    - file: databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md
title: Databricks Utilities (dbutils) via Connect
description: Accessing dbutils.fs and dbutils.secrets through Databricks Connect, including file copying between local and remote filesystems and secret management.
tags:
  - dbutils
  - filesystem
  - secrets
  - utilities
timestamp: "2026-06-19T09:47:58.074Z"
---

# Databricks Utilities (`dbutils`) via Connect

**Databricks Utilities (`dbutils`) via Connect** refers to the subset of [Databricks Utilities (`dbutils`)](https://docs.databricks.com/aws/en/dev-tools/databricks-utils) that can be accessed from a local development environment through [Databricks Connect](./databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md). Databricks Connect allows you to run Spark jobs remotely on a Databricks cluster, and a limited set of `dbutils` commands are available to perform file system and secrets operations from your client machine.

## Supported Utilities

The `dbutils.fs` and `dbutils.secrets` modules are the only utilities currently exposed through Databricks Connect. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### File System Utility (`dbutils.fs`)

The following `dbutils.fs` commands are supported:

- `cp` – Copy files or directories.
- `head` – Display the first few lines of a file.
- `ls` – List files or directories.
- `mkdirs` – Create a directory (and any parent directories).
- `mv` – Move files or directories.
- `put` – Write content to a file.
- `rm` – Remove files or directories.

For full usage details, refer to the [File system utility (`dbutils.fs`)](https://docs.databricks.com/aws/en/dev-tools/databricks-utils#dbutils-fs) documentation or run `dbutils.fs.help()` in your code. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

### Secrets Utility (`dbutils.secrets`)

The following `dbutils.secrets` commands are supported:

- `get` – Retrieve a secret value.
- `getBytes` – Retrieve a secret as bytes.
- `list` – List secret keys within a scope.
- `listScopes` – List available secret scopes.

See the [Secrets utility (`dbutils.secrets`)](https://docs.databricks.com/aws/en/dev-tools/databricks-utils#dbutils-secrets) documentation or run `dbutils.secrets.help()`. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Accessing `dbutils` in Your Code

### Python

The recommended way to create a `dbutils` object from a `SparkSession` is to use the `pyspark.dbutils.DBUtils` class:

```python
from pyspark.sql import SparkSession
from pyspark.dbutils import DBUtils

spark = SparkSession.builder.getOrCreate()
dbutils = DBUtils(spark)

# Example usage
print(dbutils.fs.ls("dbfs:/"))
print(dbutils.secrets.listScopes())
```

^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

#### Compatibility Helper Functions

To write code that works both in Databricks notebooks and via Databricks Connect, use one of the following `get_dbutils()` patterns.

**For Databricks Runtime 7.3 LTS and above:**

```python
def get_dbutils(spark):
    from pyspark.dbutils import DBUtils
    return DBUtils(spark)
```

**For earlier Databricks Runtime versions:**

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

### Scala

Scala support follows the same pattern, using the `DBUtils` class from `com.databricks.dbutils_v1` (or similar depending on the runtime version). The source material shows a Python example only, but the same `dbutils` object is available through the Spark session.

## Copying Files Between Local and Remote Filesystems

You can use `dbutils.fs.cp` to transfer files between your local client and remote Databricks storage. The local filesystem is referenced with the `file:/` scheme.

```python
from pyspark.dbutils import DBUtils
dbutils = DBUtils(spark)

# Copy from local to DBFS
dbutils.fs.cp('file:/home/user/data.csv', 'dbfs:/uploads')

# Copy from DBFS to local
dbutils.fs.cp('dbfs:/output/results.csv', 'file:/home/user/downloads/')
```

The maximum file size that can be transferred this way is **250 MB**. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Secrets Utility Considerations

The ability to call `dbutils.secrets.get` is **disabled by default** due to security restrictions. To enable it for your workspace, you must contact Databricks support. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Limitations

The following `dbutils` modules are **not supported** when using Databricks Connect:

- **Credentials utility** (`dbutils.credentials`)
- **Library utility** (`dbutils.library`)
- **Notebook workflow utility** (`dbutils.notebook` / `dbutils.workflow`)
- **Widgets utility** (`dbutils.widgets`)

These modules require notebook-specific execution contexts that are not available through the remote Spark connection. ^[databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library used to run Spark jobs remotely.
- dbutils.fs – File system utility for managing files on Databricks.
- [dbutils.secrets](/concepts/databricks-secret-scopes.md) – Secrets utility for accessing sensitive credentials.
- Databricks Utilities (dbutils) reference – Full documentation of all available utilities.

## Sources

- databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md

# Citations

1. [databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws.md](/references/databricks-connect-for-databricks-runtime-122-lts-and-below-databricks-on-aws-4be394af.md)
