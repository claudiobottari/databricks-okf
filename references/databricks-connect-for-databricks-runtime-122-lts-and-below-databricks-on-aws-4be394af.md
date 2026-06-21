---
title: Databricks Connect for Databricks Runtime 12.2 LTS and below | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect-legacy
ingestedAt: "2026-06-18T08:06:57.586Z"
---

Databricks Connect allows you to connect popular IDEs such as Visual Studio Code and PyCharm, notebook servers, and other custom applications to Databricks clusters.

This article explains how Databricks Connect works, walks you through the steps to get started with Databricks Connect, explains how to troubleshoot issues that may arise when using Databricks Connect, and differences between running using Databricks Connect versus running in a Databricks notebook.

## Overview[​](#overview "Direct link to Overview")

Databricks Connect is a client library for the Databricks Runtime. It allows you to write jobs using Spark APIs and run them remotely on a Databricks cluster instead of in the local Spark session.

For example, when you run the DataFrame command `spark.read.format(...).load(...).groupBy(...).agg(...).show()` using Databricks Connect, the logical representation of the command is sent to the Spark server running in Databricks for execution on the remote cluster.

With Databricks Connect, you can:

*   Run large-scale Spark jobs from any Python, R, Scala, or Java application. Anywhere you can `import pyspark`, `require(SparkR)` or `import org.apache.spark`, you can now run Spark jobs directly from your application, without needing to install any IDE plugins or use Spark submission scripts.
*   Step through and debug code in your IDE even when working with a remote cluster.
*   Iterate quickly when developing libraries. You do not need to restart the cluster after changing Python or Java library dependencies in Databricks Connect, because each client session is isolated from each other in the cluster.
*   Shut down idle clusters without losing work. Because the client application is decoupled from the cluster, it is unaffected by cluster restarts or upgrades, which would normally cause you to lose all the variables, RDDs, and DataFrame objects defined in a notebook.

note

For Python development with SQL queries, Databricks recommends that you use the [Databricks SQL Connector for Python](https://docs.databricks.com/aws/en/dev-tools/python-sql-connector) instead of Databricks Connect. the Databricks SQL Connector for Python is easier to set up than Databricks Connect. Also, Databricks Connect parses and plans jobs runs on your local machine, while jobs run on remote compute resources. This can make it especially difficult to debug runtime errors. The Databricks SQL Connector for Python submits SQL queries directly to remote compute resources and fetches results.

## Requirements[​](#requirements "Direct link to requirements")

This section lists the requirements for Databricks Connect.

*   Only the following Databricks Runtime versions are supported:
    
    *   Databricks Runtime 12.2 LTS ML, Databricks Runtime 12.2 LTS
    *   Databricks Runtime 11.3 LTS ML, Databricks Runtime 11.3 LTS
    *   Databricks Runtime 10.4 LTS ML, Databricks Runtime 10.4 LTS
    *   Databricks Runtime 9.1 LTS ML, Databricks Runtime 9.1 LTS
    *   Databricks Runtime 7.3 LTS
*   You must install Python 3 on your development machine, and the minor version of your client Python installation must be the same as the minor Python version of your Databricks cluster. The following table shows the Python version installed with each Databricks Runtime.
    
    Databricks strongly recommends that you have a Python _virtual environment_ activated for each Python version that you use with Databricks Connect. Python virtual environments help to make sure that you are using the correct versions of Python and Databricks Connect together. This can help to reduce the time spent resolving related technical issues.
    
    For example, if you're using [venv](https://docs.python.org/3/library/venv.html) on your development machine and your cluster is running Python 3.9, you must create a `venv` environment with that version. The following example command generates the scripts to activate a `venv` environment with Python 3.9, and this command then places those scripts within a hidden folder named `.venv` within the current working directory:
    
    Bash
    
        # Linux and macOSpython3.9 -m venv ./.venv# Windowspython3.9 -m venv .\.venv
    
    To use these scripts to activate this `venv` environment, see [How venvs work](https://docs.python.org/3/library/venv.html#how-venvs-work).
    
    As another example, if you're using [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) on your development machine and your cluster is running Python 3.9, you must create a Conda environment with that version, for example:
    
    Bash
    
        conda create --name dbconnect python=3.9
    
    To activate the Conda environment with this environment name, run `conda activate dbconnect`.
    
*   The Databricks Connect major and minor package version must always match your Databricks Runtime version. Databricks recommends that you always use the most recent package of Databricks Connect that matches your Databricks Runtime version. For example, when you use a Databricks Runtime 12.2 LTS cluster, you must also use the `databricks-connect==12.2.*` package.
    
*   Java Runtime Environment (JRE) 8. The client has been tested with the OpenJDK 8 JRE. The client does not support Java 11.
    

note

On Windows, if you see an error that Databricks Connect cannot find `winutils.exe`, see [Cannot find `winutils.exe` on Windows](#cannot-find-winutilsexe-on-windows-legacy).

## Set up the client[​](#set-up-the-client "Direct link to set-up-the-client")

Complete the following steps to set up the local client for Databricks Connect.

note

Before you begin to set up the local Databricks Connect client, you must [meet the requirements](#requirements-legacy) for Databricks Connect.

### Step 1: Install the Databricks Connect client[​](#step-1-install-the-databricks-connect-client "Direct link to Step 1: Install the Databricks Connect client")

1.  With your virtual environment activated, uninstall PySpark, if it is already installed, by running the `uninstall` command. This is required because the `databricks-connect` package conflicts with PySpark. For details, see [Conflicting PySpark installations](#conflicting-pyspark-installations-legacy). To check whether PySpark is already installed, run the `show` command.
    
    Bash
    
        # Is PySpark already installed?pip3 show pyspark# Uninstall PySparkpip3 uninstall pyspark
    
2.  With your virtual environment still activated, install the Databricks Connect client by running the `install` command. Use the `--upgrade` option to upgrade any existing client installation to the specified version.
    
    Bash
    
        pip3 install --upgrade "databricks-connect==12.2.*"  # Or X.Y.* to match your cluster version.
    
    note
    
    Databricks recommends that you append the “dot-asterisk” notation to specify `databricks-connect==X.Y.*` instead of `databricks-connect=X.Y`, to make sure that the most recent package is installed.
    

### Step 2: Configure connection properties[​](#step-2-configure-connection-properties "Direct link to Step 2: Configure connection properties")

1.  Collect the following configuration properties.
    
    *   The Databricks [workspace URL](https://docs.databricks.com/aws/en/workspace/workspace-details#workspace-url).
        
    *   Your Databricks [personal access token](https://docs.databricks.com/aws/en/dev-tools/auth/pat).
        
    *   The ID of your cluster. You can obtain the cluster ID from the URL. Here the cluster ID is `0304-201045-hoary804`.
        
        ![Cluster ID 2](https://docs.databricks.com/aws/en/assets/images/cluster-id-aws-9700c96b7d99a12223758a763026f03b.png)
        
    *   The port that Databricks Connect connects to on your cluster. The default port is `15001`.
        
2.  Configure the connection as follows.
    
    You can use the CLI, SQL configs, or environment variables. The precedence of configuration methods from highest to lowest is: SQL config keys, CLI, and environment variables.
    
    *   CLI
        
        1.  Run `databricks-connect`.
            
            Bash
            
                databricks-connect configure
            
            The license displays:
            
                Copyright (2018) Databricks, Inc.This library (the "Software") may not be used except in connection with theLicensee's use of the Databricks Platform Services pursuant to an Agreement  ...
            
        2.  Accept the license and supply configuration values. For **Databricks Host** and **Databricks Token**, enter the workspace URL and the personal access token you noted in Step 1.
            
                Do you accept the above agreement? [y/N] ySet new config values (leave input empty to accept default):Databricks Host [no current value, must start with https://]: <databricks-url>Databricks Token [no current value]: <databricks-token>Cluster ID (e.g., 0921-001415-jelly628) [no current value]: <cluster-id>Org ID (Azure-only, see ?o=orgId in URL) [0]: <org-id>Port [15001]: <port>
            
    *   SQL configs or environment variables. The following table shows the SQL config keys and the environment variables that correspond to the configuration properties you noted in Step 1. To set a SQL config key, use `sql("set config=value")`. For example: `sql("set spark.databricks.service.clusterId=0304-201045-abcdefgh")`.
        
3.  With your virtual environment still activated, test connectivity to Databricks as follows.
    
    If the cluster you configured is not running, the test starts the cluster which will remain running until its configured autotermination time. The output should look similar to the following:
    
        * PySpark is installed at /.../.../pyspark* Checking java versionjava version "1.8..."Java(TM) SE Runtime Environment (build 1.8...)Java HotSpot(TM) 64-Bit Server VM (build 25..., mixed mode)* Testing scala command../../.. ..:..:.. WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicableUsing Spark's default log4j profile: org/apache/spark/log4j-defaults.propertiesSetting default log level to "WARN".To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).../../.. ..:..:.. WARN MetricsSystem: Using default name SparkStatusTracker for source because neither spark.metrics.namespace nor spark.app.id is set.../../.. ..:..:.. WARN SparkServiceRPCClient: Now tracking server state for 5ab..., invalidating prev state../../.. ..:..:.. WARN SparkServiceRPCClient: Syncing 129 files (176036 bytes) took 3003 msWelcome to      ____              __     / __/__  ___ _____/ /__    _\ \/ _ \/ _ `/ __/  '_/   /___/ .__/\_,_/_/ /_/\_\   version 2...      /_/Using Scala version 2.... (Java HotSpot(TM) 64-Bit Server VM, Java 1.8...)Type in expressions to have them evaluated.Type :help for more information.scala> spark.range(100).reduce(_ + _)Spark context Web UI available at https://...Spark context available as 'sc' (master = local[*], app id = local-...).Spark session available as 'spark'.View job details at <databricks-url>/?o=0#/setting/clusters/<cluster-id>/sparkUiView job details at <databricks-url>?o=0#/setting/clusters/<cluster-id>/sparkUires0: Long = 4950scala> :quit* Testing python command../../.. ..:..:.. WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicableUsing Spark's default log4j profile: org/apache/spark/log4j-defaults.propertiesSetting default log level to "WARN".To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).../../.. ..:..:.. WARN MetricsSystem: Using default name SparkStatusTracker for source because neither spark.metrics.namespace nor spark.app.id is set.../../.. ..:..:.. WARN SparkServiceRPCClient: Now tracking server state for 5ab.., invalidating prev stateView job details at <databricks-url>/?o=0#/setting/clusters/<cluster-id>/sparkUi
    
4.  If no connection-related errors are shown (`WARN` messages are okay), then you have successfully connected.
    

## Use Databricks Connect[​](#use-databricks-connect "Direct link to use-databricks-connect")

The section describes how to configure your preferred IDE or notebook server to use the client for Databricks Connect.

**In this section:**

*   [JupyterLab](#jupyterlab)
*   [Classic Jupyter Notebook](#classic-jupyter-notebook)
*   [PyCharm](#pycharm)
*   [SparkR and RStudio Desktop](#sparkr-and-rstudio-desktop)
*   [sparklyr and RStudio Desktop](#sparklyr-and-rstudio-desktop)
*   [IntelliJ (Scala or Java)](#intellij-scala-or-java)
*   [PyDev with Eclipse](#pydev-with-eclipse)
*   [Eclipse](#eclipse)
*   [SBT](#sbt)
*   [Spark shell](#spark-shell)

### JupyterLab[​](#jupyterlab "Direct link to jupyterlab")

note

Before you begin to use Databricks Connect, you must [meet the requirements](#requirements-legacy) and [set up the client](#set-up-legacy) for Databricks Connect.

To use Databricks Connect with [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) and Python, follow these instructions.

1.  To install JupyterLab, with your Python virtual environment activated, run the following command from your terminal or Command Prompt:
    
2.  To start JupyterLab in your web browser, run the following command from your activated Python virtual environment:
    
    If JupyterLab does not appear in your web browser, copy the URL that starts with `localhost` or `127.0.0.1` from your virtual environment, and enter it in your web browser's address bar.
    
3.  Create a new notebook: in JupyterLab, click **File > New > Notebook** on the main menu, select **Python 3 (ipykernel)** and click **Select**.
    
4.  In the notebook's first cell, enter either the [example code](#example-code-legacy) or your own code. If you use your own code, at minimum you must instantiate an instance of `SparkSession.builder.getOrCreate()`, as shown in the [example code](#example-code-legacy).
    
5.  To run the notebook, click **Run > Run All Cells**.
    
6.  To debug the notebook, click the bug (**Enable Debugger**) icon next to **Python 3 (ipykernel)** in the notebook's toolbar. Set one or more breakpoints, and then click **Run > Run All Cells**.
    
7.  To shut down JupyterLab, click **File > Shut Down**. If the JupyterLab process is still running in your terminal or Command Prompt, stop this process by pressing `Ctrl + c` and then entering `y` to confirm.
    

For more specific debug instructions, see [Debugger](https://jupyterlab.readthedocs.io/en/stable/user/debugger.html).

### Classic Jupyter Notebook[​](#classic-jupyter-notebook "Direct link to classic-jupyter-notebook")

note

Before you begin to use Databricks Connect, you must [meet the requirements](#requirements-legacy) and [set up the client](#set-up-legacy) for Databricks Connect.

The configuration script for Databricks Connect automatically adds the package to your project configuration. To get started in a Python kernel, run:

Python

    from pyspark.sql import SparkSessionspark = SparkSession.builder.getOrCreate()

To enable the `%sql` shorthand for running and visualizing SQL queries, use the following snippet:

Python

    from IPython.core.magic import line_magic, line_cell_magic, Magics, magics_class@magics_classclass DatabricksConnectMagics(Magics):   @line_cell_magic   def sql(self, line, cell=None):       if cell and line:           raise ValueError("Line must be empty for cell magic", line)       try:           from autovizwidget.widget.utils import display_dataframe       except ImportError:           print("Please run `pip install autovizwidget` to enable the visualization widget.")           display_dataframe = lambda x: x       return display_dataframe(self.get_spark().sql(cell or line).toPandas())   def get_spark(self):       user_ns = get_ipython().user_ns       if "spark" in user_ns:           return user_ns["spark"]       else:           from pyspark.sql import SparkSession           user_ns["spark"] = SparkSession.builder.getOrCreate()           return user_ns["spark"]ip = get_ipython()ip.register_magics(DatabricksConnectMagics)

#### Visual Studio Code[​](#visual-studio-code "Direct link to Visual Studio Code")

note

Before you begin to use Databricks Connect, you must [meet the requirements](#requirements-legacy) and [set up the client](#set-up-legacy) for Databricks Connect.

To use Databricks Connect with Visual Studio Code, do the following:

1.  Verify that the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) is installed.
    
2.  Open the Command Palette (**Command+Shift+P** on macOS and **Ctrl+Shift+P** on Windows/Linux).
    
3.  Select a Python interpreter. Go to **Code > Preferences > Settings**, and choose **python settings**.
    
4.  Run `databricks-connect get-jar-dir`.
    
5.  Add the directory returned from the command to the User Settings JSON under `python.venvPath`. This should be added to the Python Configuration.
    
6.  Disable the linter. Click the **…** on the right side and **edit json settings**. The modified settings are as follows:
    
    ![VS Code configuration](https://docs.databricks.com/aws/en/assets/images/vscode-149a300aa6a15a060873b9778b3c14c4.png)
    
7.  If running with a virtual environment, which is the recommended way to develop for Python in VS Code, in the Command Palette type `select python interpreter` and point to your environment that _matches_ your cluster Python version.
    
    ![Select Python interpreter](https://docs.databricks.com/aws/en/assets/images/select-intepreter-107c56dd463264488906cb69f7226633.png)
    
    For example, if your cluster is Python 3.9, your development environment should be Python 3.9.
    
    ![Python version](https://docs.databricks.com/aws/en/assets/images/python35-4cb2ea1e4bba8f2aa3e5b81a3aa9e6a3.png)
    

### PyCharm[​](#pycharm "Direct link to PyCharm")

note

Before you begin to use Databricks Connect, you must [meet the requirements](#requirements-legacy) and [set up the client](#set-up-legacy) for Databricks Connect.

The configuration script for Databricks Connect automatically adds the package to your project configuration.

#### Python 3 clusters[​](#python-3-clusters "Direct link to Python 3 clusters")

1.  When you create a PyCharm project, select **Existing Interpreter**. From the drop-down menu, select the Conda environment you created (see [Requirements](#requirements)).
    
    ![Select interpreter](https://docs.databricks.com/aws/en/assets/images/interpreter-feadbfd61bb21cedf97b26e66d082480.png)
    
2.  Go to **Run > Edit Configurations**.
    
3.  Add `PYSPARK_PYTHON=python3` as an environment variable.
    
    ![Python 3 cluster configuration](https://docs.databricks.com/aws/en/assets/images/python3-env-ab75ecc349cb7c4b2d9a495ff506f80e.png)
    

### SparkR and RStudio Desktop[​](#sparkr-and-rstudio-desktop "Direct link to sparkr-and-rstudio-desktop")

note

Before you begin to use Databricks Connect, you must [meet the requirements](#requirements-legacy) and [set up the client](#set-up-legacy) for Databricks Connect.

To use Databricks Connect with SparkR and RStudio Desktop, do the following:

1.  Download and unpack the [open source Spark](https://spark.apache.org/downloads.html) distribution onto your development machine. Choose the same version as in your Databricks cluster (Hadoop 2.7).
    
2.  Run `databricks-connect get-jar-dir`. This command returns a path like `/usr/local/lib/python3.5/dist-packages/pyspark/jars`. Copy the file path of _one directory above_ the JAR directory file path, for example, `/usr/local/lib/python3.5/dist-packages/pyspark`, which is the `SPARK_HOME` directory.
    
3.  Configure the Spark lib path and Spark home by adding them to the top of your R script. Set `<spark-lib-path>` to the directory where you unpacked the open source Spark package in step 1. Set `<spark-home-path>` to the Databricks Connect directory from step 2.
    
    R
    
        # Point to the OSS package path, e.g., /path/to/.../spark-2.4.0-bin-hadoop2.7library(SparkR, lib.loc = .libPaths(c(file.path('<spark-lib-path>', 'R', 'lib'), .libPaths())))# Point to the Databricks Connect PySpark installation, e.g., /path/to/.../pysparkSys.setenv(SPARK_HOME = "<spark-home-path>")
    
4.  Initiate a Spark session and start running SparkR commands.
    
    R
    
        sparkR.session()df <- as.DataFrame(faithful)head(df)df1 <- dapply(df, function(x) { x }, schema(df))collect(df1)
    

### sparklyr and RStudio Desktop[​](#sparklyr-and-rstudio-desktop "Direct link to sparklyr-and-rstudio-desktop")

note

Before you begin to use Databricks Connect, you must [meet the requirements](#requirements-legacy) and [set up the client](#set-up-legacy) for Databricks Connect.

You can copy sparklyr-dependent code that you've developed locally using Databricks Connect and run it in a Databricks notebook or hosted RStudio Server in your Databricks workspace with minimal or no code changes.

**In this section:**

*   [Requirements](#requirements)
*   [Install, configure, and use sparklyr](#install-configure-and-use-sparklyr)
*   [Resources](#resources)
*   [sparklyr and RStudio Desktop limitations](#sparklyr-and-rstudio-desktop-limitations)

#### Requirements[​](#requirements-1 "Direct link to Requirements")

*   sparklyr 1.2 or above.
*   Databricks Runtime 7.3 LTS or above with the matching version of Databricks Connect.

#### Install, configure, and use sparklyr[​](#install-configure-and-use-sparklyr "Direct link to Install, configure, and use sparklyr")

1.  In RStudio Desktop, install sparklyr 1.2 or above from CRAN or install the latest master version from GitHub.
    
    R
    
        # Install from CRANinstall.packages("sparklyr")# Or install the latest master version from GitHubinstall.packages("devtools")devtools::install_github("sparklyr/sparklyr")
    
2.  Activate the Python environment with the correct version of Databricks Connect installed and run the following command in the terminal to get the `<spark-home-path>`:
    
    Bash
    
        databricks-connect get-spark-home
    
3.  Initiate a Spark session and start running sparklyr commands.
    
    R
    
        library(sparklyr)sc <- spark_connect(method = "databricks", spark_home = "<spark-home-path>")iris_tbl <- copy_to(sc, iris, overwrite = TRUE)library(dplyr)src_tbls(sc)iris_tbl %>% count
    
4.  Close the connection.
    

#### Resources[​](#resources "Direct link to Resources")

For more information, see the sparklyr GitHub [README](https://github.com/sparklyr/sparklyr#connecting-through-databricks-connect).

For code examples, see [sparklyr](https://docs.databricks.com/aws/en/sparkr/sparklyr).

#### sparklyr and RStudio Desktop limitations[​](#sparklyr-and-rstudio-desktop-limitations "Direct link to sparklyr and RStudio Desktop limitations")

The following features are unsupported:

*   sparklyr streaming APIs
*   sparklyr ML APIs
*   broom APIs
*   csv\_file serialization mode
*   spark submit

### IntelliJ (Scala or Java)[​](#intellij-scala-or-java "Direct link to IntelliJ (Scala or Java)")

note

Before you begin to use Databricks Connect, you must [meet the requirements](#requirements-legacy) and [set up the client](#set-up-legacy) for Databricks Connect.

To use Databricks Connect with IntelliJ (Scala or Java), do the following:

1.  Run `databricks-connect get-jar-dir`.
    
2.  Point the dependencies to the directory returned from the command. Go to **File > Project Structure > Modules > Dependencies > '+' sign > JARs or Directories**.
    
    ![IntelliJ JARs](https://docs.databricks.com/aws/en/assets/images/intelli-j-jars-816f44b2987ad149e0cb44596b51f3a2.png)
    
    To avoid conflicts, we strongly recommend removing any other Spark installations from your classpath. If this is not possible, make sure that the JARs you add are at the front of the classpath. In particular, they must be ahead of any other installed version of Spark (otherwise you will either use one of those other Spark versions and run locally or throw a `ClassDefNotFoundError`).
    
3.  Check the setting of the breakout option in IntelliJ. The default is **All** and will cause network timeouts if you set breakpoints for debugging. Set it to **Thread** to avoid stopping the background network threads.
    
    ![IntelliJ Thread](data:image/png;base64,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)
    

### PyDev with Eclipse[​](#pydev-with-eclipse "Direct link to pydev-with-eclipse")

note

Before you begin to use Databricks Connect, you must [meet the requirements](#requirements-legacy) and [set up the client](#set-up-legacy) for Databricks Connect.

To use Databricks Connect and [PyDev](https://www.pydev.org/manual_101_install.html) with [Eclipse](https://www.eclipse.org/downloads), follow these instructions.

1.  Start Eclipse.
2.  Create a project: click **File > New > Project > PyDev > PyDev Project**, and then click **Next**.
3.  Specify a **Project name**.
4.  For **Project contents**, specify the path to your Python virtual environment.
5.  Click **Please configure an interpreter before proceeding**.
6.  Click **Manual config**.
7.  Click **New > Browse for python/pypy exe**.
8.  Browse to and select select the full path to the Python interpreter that is referenced from the virtual environment, and then click **Open**.
9.  In the **Select interpreter** dialog, click **OK**.
10.  In the **Selection needed** dialog, click **OK**.
11.  In the **Preferences** dialog, click **Apply and Close**.
12.  In the **PyDev Project** dialog, click **Finish**.
13.  Click **Open Perspective**.
14.  Add to the project a Python code (`.py`) file that contains either the [example code](#example-code-legacy) or your own code. If you use your own code, at minimum you must instantiate an instance of `SparkSession.builder.getOrCreate()`, as shown in the [example code](#example-code-legacy).
15.  With the Python code file open, set any breakpoints where you want your code to pause while running.
16.  Click **Run > Run** or **Run > Debug**.

For more specific run and debug instructions, see [Running a Program](https://www.pydev.org/manual_101_run.html).

### Eclipse[​](#eclipse "Direct link to Eclipse")

note

Before you begin to use Databricks Connect, you must [meet the requirements](#requirements-legacy) and [set up the client](#set-up-legacy) for Databricks Connect.

To use Databricks Connect and Eclipse, do the following:

1.  Run `databricks-connect get-jar-dir`.
    
2.  Point the external JARs configuration to the directory returned from the command. Go to **Project menu > Properties > Java Build Path > Libraries > Add External Jars**.
    
    ![Eclipse external JAR configuration](https://docs.databricks.com/aws/en/assets/images/eclipse-f082144851973c385f9f1785c932c370.png)
    
    To avoid conflicts, we strongly recommend removing any other Spark installations from your classpath. If this is not possible, make sure that the JARs you add are at the front of the classpath. In particular, they must be ahead of any other installed version of Spark (otherwise you will either use one of those other Spark versions and run locally or throw a `ClassDefNotFoundError`).
    
    ![Eclipse Spark configuration](https://docs.databricks.com/aws/en/assets/images/eclipse2-097f471ea1ff51d06a9236dd1ed6b570.png)
    

### SBT[​](#sbt "Direct link to SBT")

note

Before you begin to use Databricks Connect, you must [meet the requirements](#requirements-legacy) and [set up the client](#set-up-legacy) for Databricks Connect.

To use Databricks Connect with SBT, you must configure your `build.sbt` file to link against the Databricks Connect JARs instead of the usual Spark library dependency. You do this with the `unmanagedBase` directive in the following example build file, which assumes a Scala app that has a `com.example.Test` main object:

#### `build.sbt`[​](#buildsbt "Direct link to buildsbt")

    name := "hello-world"version := "1.0"scalaVersion := "2.11.6"// this should be set to the path returned by ``databricks-connect get-jar-dir``unmanagedBase := new java.io.File("/usr/local/lib/python2.7/dist-packages/pyspark/jars")mainClass := Some("com.example.Test")

### Spark shell[​](#spark-shell "Direct link to Spark shell")

note

Before you begin to use Databricks Connect, you must [meet the requirements](#requirements-legacy) and [set up the client](#set-up-legacy) for Databricks Connect.

To use Databricks Connect with the Spark shell and Python or Scala, follow these instructions.

1.  With your virtual environment activated, make sure that the `databricks-connect test` command ran successfully in [Set up the client](#set-up-legacy).
    
2.  With your virtual environment activated, start the Spark shell. For Python, run the `pyspark` command. For Scala, run the `spark-shell` command.
    
3.  The Spark shell appears, for example for Python:
    
        Python 3... (v3...)[Clang 6... (clang-6...)] on darwinType "help", "copyright", "credits" or "license" for more information.Setting default log level to "WARN".To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).../../.. ..:..:.. WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicableWelcome to       ____              __     / __/__  ___ _____/ /__    _\ \/ _ \/ _ `/ __/  '_/   /__ / .__/\_,_/_/ /_/\_\   version 3....      /_/Using Python version 3... (v3...)Spark context Web UI available at http://...:...Spark context available as 'sc' (master = local[*], app id = local-...).SparkSession available as 'spark'.>>>
    
    For Scala:
    
        Setting default log level to "WARN".To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).../../.. ..:..:.. WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicableSpark context Web UI available at http://...Spark context available as 'sc' (master = local[*], app id = local-...).Spark session available as 'spark'.Welcome to      ____              __     / __/__  ___ _____/ /__    _\ \/ _ \/ _ `/ __/  '_/   /___/ .__/\_,_/_/ /_/\_\   version 3...      /_/Using Scala version 2... (OpenJDK 64-Bit Server VM, Java 1.8...)Type in expressions to have them evaluated.Type :help for more information.scala>
    
4.  Refer to [Interactive Analysis with the Spark Shell](https://spark.apache.org/docs/latest/quick-start.html#interactive-analysis-with-the-spark-shell) for information about how to use the Spark shell with Python or Scala to run commands on your cluster.
    
    Use the built-in `spark` variable to represent the `SparkSession` on your running cluster, for example for Python:
    
        >>> df = spark.read.table("samples.nyctaxi.trips")>>> df.show(5)+--------------------+---------------------+-------------+-----------+----------+-----------+|tpep_pickup_datetime|tpep_dropoff_datetime|trip_distance|fare_amount|pickup_zip|dropoff_zip|+--------------------+---------------------+-------------+-----------+----------+-----------+| 2016-02-14 16:52:13|  2016-02-14 17:16:04|         4.94|       19.0|     10282|      10171|| 2016-02-04 18:44:19|  2016-02-04 18:46:00|         0.28|        3.5|     10110|      10110|| 2016-02-17 17:13:57|  2016-02-17 17:17:55|          0.7|        5.0|     10103|      10023|| 2016-02-18 10:36:07|  2016-02-18 10:41:45|          0.8|        6.0|     10022|      10017|| 2016-02-22 14:14:41|  2016-02-22 14:31:52|         4.51|       17.0|     10110|      10282|+--------------------+---------------------+-------------+-----------+----------+-----------+only showing top 5 rows
    
    For Scala:
    
        >>> val df = spark.read.table("samples.nyctaxi.trips")>>> df.show(5)+--------------------+---------------------+-------------+-----------+----------+-----------+|tpep_pickup_datetime|tpep_dropoff_datetime|trip_distance|fare_amount|pickup_zip|dropoff_zip|+--------------------+---------------------+-------------+-----------+----------+-----------+| 2016-02-14 16:52:13|  2016-02-14 17:16:04|         4.94|       19.0|     10282|      10171|| 2016-02-04 18:44:19|  2016-02-04 18:46:00|         0.28|        3.5|     10110|      10110|| 2016-02-17 17:13:57|  2016-02-17 17:17:55|          0.7|        5.0|     10103|      10023|| 2016-02-18 10:36:07|  2016-02-18 10:41:45|          0.8|        6.0|     10022|      10017|| 2016-02-22 14:14:41|  2016-02-22 14:31:52|         4.51|       17.0|     10110|      10282|+--------------------+---------------------+-------------+-----------+----------+-----------+only showing top 5 rows
    
5.  To stop the Spark shell, press `Ctrl + d` or `Ctrl + z`, or run the command `quit()` or `exit()` for Python or `:q` or `:quit` for Scala.
    

## Code examples[​](#code-examples "Direct link to code-examples")

This simple code example queries the specified table and then shows the specified table's first 5 rows. To use a different table, adjust the call to `spark.read.table`.

Python

    from pyspark.sql.session import SparkSessionspark = SparkSession.builder.getOrCreate()df = spark.read.table("samples.nyctaxi.trips")df.show(5)

This longer code example does the following:

1.  Creates an in-memory DataFrame.
2.  Creates a table with the name `zzz_demo_temps_table` within the `default` schema. If the table with this name already exists, the table is deleted first. To use a different schema or table, adjust the calls to `spark.sql`, `temps.write.saveAsTable`, or both.
3.  Saves the DataFrame's contents to the table.
4.  Runs a `SELECT` query on the table's contents.
5.  Shows the query's result.
6.  Deletes the table.

*   Python
*   Scala
*   Java

Python

    from pyspark.sql import SparkSessionfrom pyspark.sql.types import *from datetime import datespark = SparkSession.builder.appName('temps-demo').getOrCreate()# Create a Spark DataFrame consisting of high and low temperatures# by airport code and date.schema = StructType([    StructField('AirportCode', StringType(), False),    StructField('Date', DateType(), False),    StructField('TempHighF', IntegerType(), False),    StructField('TempLowF', IntegerType(), False)])data = [    [ 'BLI', date(2021, 4, 3), 52, 43],    [ 'BLI', date(2021, 4, 2), 50, 38],    [ 'BLI', date(2021, 4, 1), 52, 41],    [ 'PDX', date(2021, 4, 3), 64, 45],    [ 'PDX', date(2021, 4, 2), 61, 41],    [ 'PDX', date(2021, 4, 1), 66, 39],    [ 'SEA', date(2021, 4, 3), 57, 43],    [ 'SEA', date(2021, 4, 2), 54, 39],    [ 'SEA', date(2021, 4, 1), 56, 41]]temps = spark.createDataFrame(data, schema)# Create a table on the Databricks cluster and then fill# the table with the DataFrame's contents.# If the table already exists from a previous run,# delete it first.spark.sql('USE default')spark.sql('DROP TABLE IF EXISTS zzz_demo_temps_table')temps.write.saveAsTable('zzz_demo_temps_table')# Query the table on the Databricks cluster, returning rows# where the airport code is not BLI and the date is later# than 2021-04-01. Group the results and order by high# temperature in descending order.df_temps = spark.sql("SELECT * FROM zzz_demo_temps_table " \    "WHERE AirportCode != 'BLI' AND Date > '2021-04-01' " \    "GROUP BY AirportCode, Date, TempHighF, TempLowF " \    "ORDER BY TempHighF DESC")df_temps.show()# Results:## +-----------+----------+---------+--------+# |AirportCode|      Date|TempHighF|TempLowF|# +-----------+----------+---------+--------+# |        PDX|2021-04-03|       64|      45|# |        PDX|2021-04-02|       61|      41|# |        SEA|2021-04-03|       57|      43|# |        SEA|2021-04-02|       54|      39|# +-----------+----------+---------+--------+# Clean up by deleting the table from the Databricks cluster.spark.sql('DROP TABLE zzz_demo_temps_table')

## Work with dependencies[​](#work-with-dependencies "Direct link to Work with dependencies")

Typically your main class or Python file will have other dependency JARs and files. You can add such dependency JARs and files by calling `sparkContext.addJar("path-to-the-jar")` or `sparkContext.addPyFile("path-to-the-file")`. You can also add Egg files and zip files with the `addPyFile()` interface. Every time you run the code in your IDE, the dependency JARs and files are installed on the cluster.

*   Python
*   Scala

Python

    from lib import Foofrom pyspark.sql import SparkSessionspark = SparkSession.builder.getOrCreate()sc = spark.sparkContext#sc.setLogLevel("INFO")print("Testing simple count")print(spark.range(100).count())print("Testing addPyFile isolation")sc.addPyFile("lib.py")print(sc.parallelize(range(10)).map(lambda i: Foo(2)).collect())class Foo(object):  def __init__(self, x):    self.x = x

**Python + Java UDFs**

Python

    from pyspark.sql import SparkSessionfrom pyspark.sql.column import _to_java_column, _to_seq, Column## In this example, udf.jar contains compiled Java / Scala UDFs:#package com.example##import org.apache.spark.sql._#import org.apache.spark.sql.expressions._#import org.apache.spark.sql.functions.udf##object Test {#  val plusOne: UserDefinedFunction = udf((i: Long) => i + 1)#}spark = SparkSession.builder \  .config("spark.jars", "/path/to/udf.jar") \  .getOrCreate()sc = spark.sparkContextdef plus_one_udf(col):  f = sc._jvm.com.example.Test.plusOne()  return Column(f.apply(_to_seq(sc, [col], _to_java_column)))sc._jsc.addJar("/path/to/udf.jar")spark.range(100).withColumn("plusOne", plus_one_udf("id")).show()

## Access Databricks Utilities[​](#access-databricks-utilities "Direct link to access-databricks-utilities")

This section describes how to use Databricks Connect to access [Databricks Utilities](https://docs.databricks.com/aws/en/dev-tools/databricks-utils).

You can use `dbutils.fs` and `dbutils.secrets` utilities of the [Databricks Utilities (`dbutils`) reference](https://docs.databricks.com/aws/en/dev-tools/databricks-utils) module. Supported commands are `dbutils.fs.cp`, `dbutils.fs.head`, `dbutils.fs.ls`, `dbutils.fs.mkdirs`, `dbutils.fs.mv`, `dbutils.fs.put`, `dbutils.fs.rm`, `dbutils.secrets.get`, `dbutils.secrets.getBytes`, `dbutils.secrets.list`, `dbutils.secrets.listScopes`. See [File system utility (dbutils.fs)](https://docs.databricks.com/aws/en/dev-tools/databricks-utils#dbutils-fs) or run `dbutils.fs.help()` and [Secrets utility (dbutils.secrets)](https://docs.databricks.com/aws/en/dev-tools/databricks-utils#dbutils-secrets) or run `dbutils.secrets.help()`.

*   Python
*   Scala

Python

    from pyspark.sql import SparkSessionfrom pyspark.dbutils import DBUtilsspark = SparkSession.builder.getOrCreate()dbutils = DBUtils(spark)print(dbutils.fs.ls("dbfs:/"))print(dbutils.secrets.listScopes())

When using Databricks Runtime 7.3 LTS or above, to access the DBUtils module in a way that works both locally and in Databricks clusters, use the following `get_dbutils()`:

Python

    def get_dbutils(spark):  from pyspark.dbutils import DBUtils  return DBUtils(spark)

Otherwise, use the following `get_dbutils()`:

Python

    def get_dbutils(spark):  if spark.conf.get("spark.databricks.service.client.enabled") == "true":    from pyspark.dbutils import DBUtils    return DBUtils(spark)  else:    import IPython    return IPython.get_ipython().user_ns["dbutils"]

### Copying files between local and remote filesystems[​](#copying-files-between-local-and-remote-filesystems "Direct link to Copying files between local and remote filesystems")

You can use `dbutils.fs` to copy files between your client and remote filesystems. Scheme `file:/` refers to the local filesystem on the client.

Python

    from pyspark.dbutils import DBUtilsdbutils = DBUtils(spark)dbutils.fs.cp('file:/home/user/data.csv', 'dbfs:/uploads')dbutils.fs.cp('dbfs:/output/results.csv', 'file:/home/user/downloads/')

The maximum file size that can be transferred that way is 250 MB.

### Enable `dbutils.secrets.get`[​](#enable-dbutilssecretsget "Direct link to enable-dbutilssecretsget")

Because of security restrictions, the ability to call `dbutils.secrets.get` is disabled by default. Contact Databricks support to enable this feature for your workspace.

## Set Hadoop configurations[​](#set-hadoop-configurations "Direct link to Set Hadoop configurations")

On the client you can set Hadoop configurations using the `spark.conf.set` API, which applies to SQL and DataFrame operations. Hadoop configurations set on the `sparkContext` must be set in the cluster configuration or using a notebook. This is because configurations set on `sparkContext` are not tied to user sessions but apply to the entire cluster.

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

Run `databricks-connect test` to check for connectivity issues. This section describes some common issues you may encounter with Databricks Connect and how to resolve them.

**In this section:**

*   [Python version mismatch](#python-version-mismatch)
*   [Server not enabled](#server-not-enabled)
*   [Conflicting PySpark installations](#conflicting-pyspark-installations)
*   [Conflicting `SPARK_HOME`](#conflicting-spark_home)
*   [Conflicting or Missing `PATH` entry for binaries](#conflicting-or-missing-path-entry-for-binaries)
*   [Conflicting serialization settings on the cluster](#conflicting-serialization-settings-on-the-cluster)
*   [Cannot find `winutils.exe` on Windows](#cannot-find-winutilsexe-on-windows)
*   [The filename, directory name, or volume label syntax is incorrect on Windows](#the-filename-directory-name-or-volume-label-syntax-is-incorrect-on-windows)

### Python version mismatch[​](#python-version-mismatch "Direct link to Python version mismatch")

Check the Python version you are using locally has at least the same minor release as the version on the cluster (for example, `3.9.16` versus `3.9.15` is OK, `3.9` versus `3.8` is not).

If you have multiple Python versions installed locally, ensure that Databricks Connect is using the right one by setting the `PYSPARK_PYTHON` environment variable (for example, `PYSPARK_PYTHON=python3`).

### Server not enabled[​](#server-not-enabled "Direct link to Server not enabled")

Ensure the cluster has the Spark server enabled with `spark.databricks.service.server.enabled true`. You should see the following lines in the driver log if it is:

    ../../.. ..:..:.. INFO SparkConfUtils$: Set spark config:spark.databricks.service.server.enabled -> true...../../.. ..:..:.. INFO SparkContext: Loading Spark Service RPC Server../../.. ..:..:.. INFO SparkServiceRPCServer:Starting Spark Service RPC Server../../.. ..:..:.. INFO Server: jetty-9...../../.. ..:..:.. INFO AbstractConnector: Started ServerConnector@6a6c7f42{HTTP/1.1,[http/1.1]}{0.0.0.0:15001}../../.. ..:..:.. INFO Server: Started @5879ms

### Conflicting PySpark installations[​](#conflicting-pyspark-installations "Direct link to conflicting-pyspark-installations")

The `databricks-connect` package conflicts with PySpark. Having both installed will cause errors when initializing the Spark context in Python. This can manifest in several ways, including “stream corrupted” or “class not found” errors. If you have PySpark installed in your Python environment, ensure it is uninstalled before installing databricks-connect. After uninstalling PySpark, make sure to fully re-install the Databricks Connect package:

Bash

    pip3 uninstall pysparkpip3 uninstall databricks-connectpip3 install --upgrade "databricks-connect==12.2.*"  # or X.Y.* to match your specific cluster version.

### Conflicting `SPARK_HOME`[​](#conflicting-spark_home "Direct link to conflicting-spark_home")

If you have previously used Spark on your machine, your IDE may be configured to use one of those other versions of Spark rather than the Databricks Connect Spark. This can manifest in several ways, including “stream corrupted” or “class not found” errors. You can see which version of Spark is being used by checking the value of the `SPARK_HOME` environment variable:

*   Python
*   Scala
*   Java

Python

    import osprint(os.environ['SPARK_HOME'])

#### Resolution[​](#resolution "Direct link to Resolution")

If `SPARK_HOME` is set to a version of Spark other than the one in the client, you should unset the `SPARK_HOME` variable and try again.

Check your IDE environment variable settings, your `.bashrc`, `.zshrc`, or `.bash_profile` file, and anywhere else environment variables might be set. You will most likely have to quit and restart your IDE to purge the old state, and you may even need to create a new project if the problem persists.

You should not need to set `SPARK_HOME` to a new value; unsetting it should be sufficient.

### Conflicting or Missing `PATH` entry for binaries[​](#conflicting-or-missing-path-entry-for-binaries "Direct link to conflicting-or-missing-path-entry-for-binaries")

It is possible your PATH is configured so that commands like `spark-shell` will be running some other previously installed binary instead of the one provided with Databricks Connect. This can cause `databricks-connect test` to fail. You should make sure either the Databricks Connect binaries take precedence, or remove the previously installed ones.

If you can't run commands like `spark-shell`, it is also possible your PATH was not automatically set up by `pip3 install` and you'll need to add the installation `bin` dir to your PATH manually. It's possible to use Databricks Connect with IDEs even if this isn't set up. However, the `databricks-connect test` command will not work.

### Conflicting serialization settings on the cluster[​](#conflicting-serialization-settings-on-the-cluster "Direct link to Conflicting serialization settings on the cluster")

If you see “stream corrupted” errors when running `databricks-connect test`, this may be due to incompatible cluster serialization configs. For example, setting the `spark.io.compression.codec` config can cause this issue. To resolve this issue, consider removing these configs from the cluster settings, or setting the configuration in the Databricks Connect client.

### Cannot find `winutils.exe` on Windows[​](#cannot-find-winutilsexe-on-windows "Direct link to cannot-find-winutilsexe-on-windows")

If you are using Databricks Connect on Windows and see:

    ERROR Shell: Failed to locate the winutils binary in the hadoop binary pathjava.io.IOException: Could not locate executable null\bin\winutils.exe in the Hadoop binaries.

Follow the instructions to [configure the Hadoop path on Windows](https://cwiki.apache.org/confluence/display/HADOOP2/Hadoop2OnWindows).

### The filename, directory name, or volume label syntax is incorrect on Windows[​](#the-filename-directory-name-or-volume-label-syntax-is-incorrect-on-windows "Direct link to The filename, directory name, or volume label syntax is incorrect on Windows")

If you are using Windows and Databricks Connect and see:

    The filename, directory name, or volume label syntax is incorrect.

Either Java or Databricks Connect was installed into a directory with a [space in your path](https://stackoverflow.com/questions/47028892/why-does-spark-shell-fail-with-the-filename-directory-name-or-volume-label-sy). You can work around this by either installing into a directory path without spaces, or configuring your path using the [short name form](https://stackoverflow.com/questions/892555/how-do-i-specify-c-program-files-without-a-space-in-it-for-programs-that-cant).

## Limitations[​](#limitations "Direct link to Limitations")

*   [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/).

*   Structured Streaming.
*   Running arbitrary code that is not a part of a Spark job on the remote cluster.
*   Native Scala, Python, and R APIs for Delta table operations (for example, `DeltaTable.forPath`) are not supported. However, the SQL API (`spark.sql(...)`) with Delta Lake operations and the Spark API (for example, `spark.read.load`) on Delta tables are both supported.
*   Copy into.
*   Using SQL functions, Python or Scala UDFs which are part of the server's catalog. However, locally introduced Scala and Python UDFs work.
*   [Apache Zeppelin](https://zeppelin.apache.org/) 0.7.x and below.
*   Connecting to clusters with [table access control](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/table-acl).
*   Connecting to clusters with process isolation enabled (in other words, where `spark.databricks.pyspark.enableProcessIsolation` is set to `true`).
*   Delta `CLONE` SQL command.
*   Global temporary views.
*   [Koalas](https://docs.databricks.com/aws/en/archive/legacy/koalas) and `pyspark.pandas`.
*   `CREATE TABLE table AS SELECT ...` SQL commands do not always work. Instead, use `spark.sql("SELECT ...").write.saveAsTable("table")`.

*   The following [Databricks Utilities (`dbutils`) reference](https://docs.databricks.com/aws/en/dev-tools/databricks-utils):
    *   [credentials](https://docs.databricks.com/aws/en/dev-tools/databricks-utils#dbutils-credentials)
    *   [library](https://docs.databricks.com/aws/en/archive/dev-tools/dbutils-library)
    *   [notebook workflow](https://docs.databricks.com/aws/en/dev-tools/databricks-utils#dbutils-workflow)
    *   [widgets](https://docs.databricks.com/aws/en/dev-tools/databricks-utils#dbutils-widgets)
*   [AWS Glue catalog](https://docs.databricks.com/aws/en/archive/external-metastores/aws-glue-metastore)
