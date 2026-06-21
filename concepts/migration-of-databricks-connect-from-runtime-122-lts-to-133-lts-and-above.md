---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 13eda30f0b977f21d7e2323e40adfab215d92c5b4634e1e58101d785608fc0ad
  pageDirectory: concepts
  sources:
    - migrate-to-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - migration-of-databricks-connect-from-runtime-122-lts-to-133-lts-and-above
    - above and Migration of Databricks Connect from Runtime 12.2 LTS to 13.3 LTS
    - MODCFR1LT1LAA
    - Databricks Connect for Runtime 12.2 LTS and Below
  citations:
    - file: migrate-to-databricks-connect-for-python-databricks-on-aws.md
title: Migration of Databricks Connect from Runtime 12.2 LTS to 13.3 LTS and above
description: The process of upgrading a Python project or environment from Databricks Connect for Databricks Runtime 12.2 LTS and below to 13.3 LTS and above.
tags:
  - databricks
  - migration
  - python
  - version-upgrade
timestamp: "2026-06-19T19:34:44.672Z"
---

Here is the wiki page based solely on the provided source material.

---

## Migration of Databricks Connect from Runtime 12.2 LTS to 13.3 LTS and above

This page describes the process to migrate from **Databricks Connect** for **Databricks Runtime 12.2 LTS and below** to **Databricks Connect for Databricks Runtime 13.3 LTS and above** for Python. The migration involves upgrading the client, virtual environment, and code to align with the new [Databricks Connect](/concepts/databricks-connect.md) architecture for Python. ^[migrate-to-databricks-connect-for-python-databricks-on-aws.md]

### Prerequisites

Before you begin, you must set up the Databricks Connect client. See the [installation guide for Databricks Connect for Python](/concepts/databricks-connect-for-python.md). ^[migrate-to-databricks-connect-for-python-databricks-on-aws.md]

### Migration Steps

1.  **Install the correct Python version** locally to match your Databricks cluster version, as listed in the installation requirements. ^[migrate-to-databricks-connect-for-python-databricks-on-aws.md]
2.  **Upgrade your Python virtual environment** to use the correct Python version to match your cluster, if needed. ^[migrate-to-databricks-connect-for-python-databricks-on-aws.md]
3.  With your virtual environment activated:
    - **Uninstall PySpark** from your virtual environment.
    - **Uninstall Databricks Connect** for Runtime 12.2 LTS and below:
        ```bash
        pip3 uninstall databricks-connect
        ```
    - **Install Databricks Connect** for Runtime 13.3 LTS and above. Use the “dot-asterisk” notation (e.g., `==14.0.*`) to ensure the latest package for your cluster version is installed:
        ```bash
        pip3 install --upgrade "databricks-connect==14.0.*"
        ```
        ^[migrate-to-databricks-connect-for-python-databricks-on-aws.md]

4.  **Update your Python code** to initialize the `spark` variable using the `DatabricksSession` class (similar to `SparkSession` in PySpark). See [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md). ^[migrate-to-databricks-connect-for-python-databricks-on-aws.md]
5.  **Migrate your RDD APIs** to use DataFrame APIs, and migrate your `SparkContext` to use alternatives. ^[migrate-to-databricks-connect-for-python-databricks-on-aws.md]

### Setting Hadoop Configurations

On the client, you can set Hadoop configurations using the `spark.conf.set` API, which applies to SQL and DataFrame operations. However, Hadoop configurations set on the `sparkContext` must be set in the cluster configuration or using a notebook. This is because configurations set on `sparkContext` are not tied to user sessions but apply to the entire cluster. ^[migrate-to-databricks-connect-for-python-databricks-on-aws.md]

### Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md)
- Databricks Runtime
- PySpark
- SparkSession
- RDD APIs
- Hadoop configurations

### Sources

- migrate-to-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [migrate-to-databricks-connect-for-python-databricks-on-aws.md](/references/migrate-to-databricks-connect-for-python-databricks-on-aws-5b63ea6f.md)
