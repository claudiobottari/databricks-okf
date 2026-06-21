---
title: "Tutorial: Run Python code on serverless compute | Databricks on AWS"
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/tutorial-serverless
ingestedAt: "2026-06-18T08:06:30.081Z"
---

note

This article applies to Databricks Connect 15.4 LTS and above.

This article describes how to create a project in your IDE, setup your virtual environment, install Databricks Connect for Python, and run code on serverless compute in your Databricks workspace.

This tutorial uses Python 3.12 and Databricks Connect 17.3 LTS. To use other versions of Python of Databricks Connect, they must be compatible. See the [version support matrix](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements#versions).

## Requirements[​](#requirements "Direct link to Requirements")

To complete this tutorial, the following requirements must be met:

*   Your workspace, local environment, and compute meet the requirements for Databricks Connect for Python. See [Databricks Connect usage requirements](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements).
*   Serverless compute is enabled in your workspace. See [Connect to serverless compute](https://docs.databricks.com/aws/en/compute/serverless/).
*   You have Python 3.12 is installed.
*   You have an IDE installed, such as Visual Studio Code.
*   You have the Databricks CLI installed in your local machine. See [Install or update the Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/install).

## Step 1: Configure Databricks authentication[​](#step-1-configure-databricks-authentication "Direct link to step-1-configure-databricks-authentication")

This tutorial uses Databricks [OAuth user-to-machine (U2M) authentication](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-u2m) and a Databricks [configuration profile](https://docs.databricks.com/aws/en/dev-tools/auth/config-profiles) for authenticating to your Databricks workspace.

1.  Use the [Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/install) to initiate OAuth token management locally by running the following command for each target workspace. In the following command, replace `<workspace-url>` with your Databricks [workspace instance URL](https://docs.databricks.com/aws/en/workspace/workspace-details#workspace-url), for example `https://dbc-a1b2345c-d6e7.cloud.databricks.com`.
    
    Bash
    
        databricks auth login --host <workspace-url>
    
2.  The Databricks CLI prompts you to save the information that you entered as a Databricks [configuration profile](https://docs.databricks.com/aws/en/dev-tools/auth/config-profiles). Press `Enter` to accept the suggested profile name, or enter the name of a new or existing profile. Databricks recommends using `DEFAULT` as your profile name.
    
3.  In your web browser, complete the on-screen instructions to log in to your Databricks workspace.
    

## Step 2: Create a new Python virtual environment[​](#step-2-create-a-new-python-virtual-environment "Direct link to Step 2: Create a new Python virtual environment")

1.  Create your project folder and open it in your IDE. For example, in the Visual Studio Code main menu, click **File** > **Open Folder** > **Open**
    
2.  Open a terminal window at the project folder root. For example, in the Visual Studio Code main menu, click **View** > **Terminal**.
    
3.  Create a virtual environment for the project called `venv` at the root of the project folder by running the following command in the terminal:
    
4.  Activate your virtual environment:
    
    Bash
    
        # Linux/Macsource .venv/bin/activate
    
    Bash
    
        # Windows.venv\Scripts\activate
    

## Step 3: Install Databricks Connect[​](#step-3-install-databricks-connect "Direct link to Step 3: Install Databricks Connect")

Install Databricks Connect. For information about the latest released versions of Databricks Connect, see [Databricks Connect release notes](https://docs.databricks.com/aws/en/release-notes/dbconnect/).

    pip install "databricks-connect==17.3.*"

## Step 4: Add code and run[​](#step-4-add-code-and-run "Direct link to Step 4: Add code and run")

1.  Add a new Python file `main.py` to your project
    
2.  Enter the following code into the file, replacing the placeholder `<profile-name>` with the name of your configuration profile from Step 1, then save the file. The default configuration profile name is `DEFAULT`.
    
    Python
    
        from databricks.connect import DatabricksSessionspark = DatabricksSession.builder.serverless().profile("<profile-name>").getOrCreate()df = spark.read.table("samples.nyctaxi.trips")df.show(5)
    
3.  Run the code using the following command:
    
    Five rows of the table are returned:
    
    Output
    
        +--------------------+---------------------+-------------+-----------+---------+-----------+|tpep_pickup_datetime|tpep_dropoff_datetime|trip_distance|fare_amount|pickup_zip|dropoff_zip|+--------------------+---------------------+-------------+-----------+----------+-----------+| 2016-02-16 22:40:45|  2016-02-16 22:59:25|         5.35|       18.5|     10003|      11238|| 2016-02-05 16:06:44|  2016-02-05 16:26:03|          6.5|       21.5|     10282|      10001|| 2016-02-08 07:39:25|  2016-02-08 07:44:14|          0.9|        5.5|     10119|      10003|| 2016-02-29 22:25:33|  2016-02-29 22:38:09|          3.5|       13.5|     10001|      11222|| 2016-02-03 17:21:02|  2016-02-03 17:23:24|          0.3|        3.5|     10028|      10028|+--------------------+---------------------+-------------+-----------+----------+-----------+
    

You have run successfully your first query on Databricks serverless compute using Databricks Connect from your IDE.

## Step 5: Make your code production-ready[​](#step-5-make-your-code-production-ready "Direct link to Step 5: Make your code production-ready")

For production scenarios, it is important to avoid using compute specifications in the Spark session builder. For example, if you deploy your code to a classic cluster: `Standard` or `Dedicated` using the `.` `serverless()` API in your Spark session builder, a new serverless Spark session is created using the classic cluster as client.

To make your code flexible and ready for production, the Spark session should not contain any parameters.

Python

    spark = DatabricksSession.builder.getOrCreate()

However, when this code is run on Databricks, the default global Spark session of the Databricks compute is used.

To enable serverless compute in your IDE, use the DEFAULT configuration profile, which is selected by the `DatabricksSession.builder` when no parameters are specified:

1.  Create a configuration profile named `DEFAULT` using the instructions from [step 1](#configure-auth).
    
2.  Use a text editor to open the `.databrickscfg` file, which is found in:
    
    *   Your `$HOME` user home folder on Unix, Linux, or macOS: `~/.databrickscfg`, or
        
    *   Your `%USERPROFILE%` (your user home) folder on Windows. For example, for macOS:
        
3.  Add `serverless_compute_id = auto` to the `DEFAULT` profile:
    
        [DEFAULT]host                  = https://my-workspace.cloud.databricks.comauth_type             = databricks-cliserverless_compute_id = auto
    
4.  Save the changes and exit your editor.
    
5.  Modify your code to use a general Spark session and run it:
    
    Python
    
        from databricks.connect import DatabricksSessionspark = DatabricksSession.builder.getOrCreate()df = spark.read.table("samples.nyctaxi.trips")df.show(5)
    

You have run your production-ready code successfully on Databricks serverless compute using Databricks Connect from your IDE using the DEFAULT configuration profile.

tip

You can also use environment variables to set the connection to a specific Databricks compute:

*   Serverless: `DATABRICKS_SERVERLESS_COMPUTE_ID=auto`
*   Classic: `DATABRICKS_CLUSTER_ID=<your_cluster_id>`
