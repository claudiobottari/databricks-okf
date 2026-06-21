---
title: Install Databricks Connect for Python | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/install
ingestedAt: "2026-06-18T08:06:17.799Z"
---

note

This article covers Databricks Connect for Databricks Runtime 13.3 LTS and above.

This article describes how to install Databricks Connect for Python. See [Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/).

## Requirements[​](#requirements "Direct link to requirements")

Before installing Databricks Connect, make sure your workspace and local environment meet the requirements. See [Databricks Connect usage requirements](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements).

## Activate a Python virtual environment[​](#activate-a-python-virtual-environment "Direct link to Activate a Python virtual environment")

Databricks strongly recommends that you have a Python _virtual environment_ activated for each Python version that you use with Databricks Connect. Python virtual environments help to make sure that you are using the correct versions of Python and Databricks Connect together. For more information about these tools and how to activate them, see [venv](https://docs.python.org/3/library/venv.html) or [Poetry](https://python-poetry.org/docs/managing-environments/).

## Install the Databricks Connect client[​](#install-the-databricks-connect-client "Direct link to install-the-databricks-connect-client")

This section describes how to install the [Databricks Connect client](https://pypi.org/project/databricks-connect/) with [venv](https://docs.python.org/3/library/venv.html) or [Poetry](https://python-poetry.org/).

### Install the Databricks Connect client with venv[​](#install-the-databricks-connect-client-with-venv "Direct link to Install the Databricks Connect client with venv")

1.  With your virtual environment activated, uninstall PySpark, if it is already installed, by running the `uninstall` command. This is required because the `databricks-connect` package conflicts with PySpark. For details, see [Conflicting PySpark installations](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/troubleshooting#conflicting-pyspark-installations). To check whether PySpark is already installed, run the `show` command.
    
    Bash
    
        # Is PySpark already installed?pip3 show pyspark# Uninstall PySparkpip3 uninstall pyspark
    
2.  With your virtual environment still activated, install the Databricks Connect client by running the `install` command. Use the `--upgrade` option to upgrade any existing client installation to the specified version.
    
    Bash
    
        pip3 install --upgrade "databricks-connect==17.3.*"  # Or X.Y.* to match your cluster version.
    
    note
    
    Databricks recommends that you append the “dot-asterisk” notation to specify `databricks-connect==X.Y.*` instead of `databricks-connect=X.Y`, to make sure that the most recent package is installed. While this is not a requirement, it helps make sure that you can use the latest supported features for that cluster.
    

### Install the Databricks Connect client with Poetry[​](#install-the-databricks-connect-client-with-poetry "Direct link to Install the Databricks Connect client with Poetry")

1.  With your virtual environment activated, uninstall PySpark, if it is already installed, by running the `remove` command. This is required because the `databricks-connect` package conflicts with PySpark. For details, see [Conflicting PySpark installations](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/troubleshooting#conflicting-pyspark-installations). To check whether PySpark is already installed, run the `show` command.
    
    Bash
    
        # Is PySpark already installed?poetry show pyspark# Uninstall PySparkpoetry remove pyspark
    
2.  With your virtual environment still activated, install the Databricks Connect client by running the `add` command.
    
    Bash
    
        poetry add databricks-connect@~17.3  # Or X.Y to match your cluster version.
    
    note
    
    Databricks recommends that you use the “at-tilde” notation to specify `databricks-connect@~17.3` instead of `databricks-connect==17.3`, to make sure that the most recent package is installed. While this is not a requirement, it helps make sure that you can use the latest supported features for that cluster.
