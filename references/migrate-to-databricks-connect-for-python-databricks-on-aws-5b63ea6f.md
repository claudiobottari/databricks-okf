---
title: Migrate to Databricks Connect for Python | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/migrate
ingestedAt: "2026-06-18T08:06:20.949Z"
---

This article describes how to migrate from Databricks Connect for Databricks Runtime 12.2 LTS and below to Databricks Connect for Databricks Runtime 13.3 LTS and above for Python. Databricks Connect enables you to connect popular IDEs, notebook servers, and custom applications to Databricks clusters. See [Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/).

Before you begin to use Databricks Connect, you must [set up the Databricks Connect client](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/install).

For the Scala version of this article, see [Migrate to Databricks Connect for Scala](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/migrate).

## Migrate your Python project[​](#migrate-your-python-project "Direct link to Migrate your Python project")

To migrate your existing Python code project or coding environment from Databricks Connect for Databricks Runtime 12.2 LTS and below to Databricks Connect for Databricks Runtime 13.3 LTS and above:

1.  Install the correct version of Python as listed in the [installation requirements](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/install) to match your Databricks cluster, if it is not already installed locally.
    
2.  Upgrade your Python virtual environment to use the correct version of Python to match your cluster, if needed. For instructions, see your virtual environment provider's documentation.
    
3.  With your virtual environment activated, uninstall PySpark from your virtual environment:
    
4.  With your virtual environment still activated, uninstall Databricks Connect for Databricks Runtime 12.2 LTS and below:
    
    Bash
    
        pip3 uninstall databricks-connect
    
5.  With your virtual environment still activated, install Databricks Connect for Databricks Runtime 13.3 LTS and above:
    
    Bash
    
        pip3 install --upgrade "databricks-connect==14.0.*"  # Or X.Y.* to match your cluster version.
    
    note
    
    Databricks recommends that you append the “dot-asterisk” notation to specify `databricks-connect==X.Y.*` instead of `databricks-connect=X.Y`, to make sure that the most recent package is installed. While this is not a requirement, it helps make sure that you can use the latest supported features for that cluster.
    
6.  Update your Python code to initialize the `spark` variable (which represents an instantiation of the `DatabricksSession` class, similar to `SparkSession` in PySpark). See [Compute configuration for Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config).
    
7.  Migrate your RDD APIs to use DataFrame APIs, and migrate your `SparkContext` to use alternatives.
    

## Set Hadoop configurations[​](#set-hadoop-configurations "Direct link to Set Hadoop configurations")

On the client you can set Hadoop configurations using the `spark.conf.set` API, which applies to SQL and DataFrame operations. Hadoop configurations set on the `sparkContext` must be set in the cluster configuration or using a notebook. This is because configurations set on `sparkContext` are not tied to user sessions but apply to the entire cluster.
