---
title: "Tutorial: Run code from PyCharm on classic compute | Databricks on AWS"
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/tutorial-cluster
ingestedAt: "2026-06-18T08:06:28.353Z"
---

note

This article applies to Databricks Connect for Databricks Runtime 13.3 LTS and above.

Databricks Connect enables you to connect popular IDEs such as PyCharm, notebook servers, and other custom applications to Databricks compute. See [Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/).

This article demonstrates how to quickly get started with Databricks Connect for Python using [PyCharm](https://www.jetbrains.com/help/pycharm/installation-guide.html). You will create a project in PyCharm, install Databricks Connect for Databricks Runtime 13.3 LTS and above, and run simple code on classic compute in your Databricks workspace from PyCharm.

## Requirements[​](#requirements "Direct link to Requirements")

To complete this tutorial, you must meet the following requirements:

*   Your workspace, local environment, and compute meet the requirements for Databricks Connect for Python. See [Databricks Connect usage requirements](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements).
*   You have [PyCharm](https://www.jetbrains.com/help/pycharm/installation-guide.html) installed. This tutorial was tested with PyCharm Community Edition 2023.3.5. If you use a different version or edition of PyCharm, the following instructions might vary.
*   If you are using classic compute, you will need the cluster's ID. To get your cluster ID, in your workspace, click **Compute** on the sidebar, and then click your cluster's name. In your web browser's address bar, copy the string of characters between `clusters` and `configuration` in the URL.

## Step 1: Configure Databricks authentication[​](#step-1-configure-databricks-authentication "Direct link to step-1-configure-databricks-authentication")

This tutorial uses Databricks [OAuth user-to-machine (U2M) authentication](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-u2m) and a Databricks [configuration profile](https://docs.databricks.com/aws/en/dev-tools/auth/config-profiles) for authenticating to your Databricks workspace. To use a different authentication type, see [Configure connection properties](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config).

Configuring OAuth U2M authentication requires the Databricks CLI. For information about installing the Databricks CLI, see [Install or update the Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/install).

Initiate OAuth U2M authentication, as follows:

1.  Use the [Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/install) to initiate OAuth token management locally by running the following command for each target workspace.
    
    In the following command, replace `<workspace-url>` with your Databricks [workspace instance URL](https://docs.databricks.com/aws/en/workspace/workspace-details#workspace-url), for example `https://dbc-a1b2345c-d6e7.cloud.databricks.com`.
    
    Bash
    
        databricks auth login --configure-cluster --host <workspace-url>
    
2.  The Databricks CLI prompts you to save the information that you entered as a Databricks [configuration profile](https://docs.databricks.com/aws/en/dev-tools/auth/config-profiles). Press `Enter` to accept the suggested profile name, or enter the name of a new or existing profile. Any existing profile with the same name is overwritten with the information that you entered. You can use profiles to quickly switch your authentication context across multiple workspaces.
    
    To get a list of any existing profiles, in a separate terminal or command prompt, use the Databricks CLI to run the command `databricks auth profiles`. To view a specific profile's existing settings, run the command `databricks auth env --profile <profile-name>`.
    
3.  In your web browser, complete the on-screen instructions to log in to your Databricks workspace.
    
4.  In the list of available clusters that appears in your terminal or command prompt, use your up arrow and down arrow keys to select the target Databricks cluster in your workspace, and then press `Enter`. You can also type any part of the cluster's display name to filter the list of available clusters.
    
5.  To view a profile's current OAuth token value and the token's upcoming expiration timestamp, run one of the following commands:
    
    *   `databricks auth token --host <workspace-url>`
    *   `databricks auth token -p <profile-name>`
    *   `databricks auth token --host <workspace-url> -p <profile-name>`
    
    If you have multiple profiles with the same `--host` value, you might need to specify the `--host` and `-p` options together to help the Databricks CLI find the correct matching OAuth token information.
    

## Step 2: Create the project[​](#step-2-create-the-project "Direct link to Step 2: Create the project")

1.  Start PyCharm.
2.  On the main menu, click **File > New Project**.
3.  In the **New Project** dialog, click **Pure Python**.
4.  For **Location**, click the folder icon, and complete the on-screen directions to specify the path to your new Python project.
5.  Leave **Create a main.py welcome script** selected.
6.  For **Interpreter type**, click **Project venv**.
7.  Expand **Python version**, and use the folder icon or drop-down list to specify the path to the Python interpreter from the preceding requirements.
8.  Click **Create**.

![Create the PyCharm project](https://docs.databricks.com/aws/en/assets/images/create-project-pycharm-c030db041c7cda6dcc959ea3e550f2e9.png)

## Step 3: Add the Databricks Connect package[​](#step-3-add-the-databricks-connect-package "Direct link to step-3-add-the-databricks-connect-package")

1.  On PyCharm's main menu, click **View > Tool Windows > Python Packages**.
2.  In the search box, enter `databricks-connect`.
3.  In the **PyPI repository** list, click **databricks-connect**.
4.  In the result pane's **latest** drop-down list, select the version that matches your cluster's Databricks Runtime version. For example, if your cluster has Databricks Runtime 14.3 installed, select **14.3.1**.
5.  Click **Install package**.
6.  After the package installs, you can close the **Python Packages** window.

![Install the Databricks Connect package](https://docs.databricks.com/aws/en/assets/images/install-package-pycharm-fc617f6067dedfe12e986f2a501750d5.png)

## Step 4: Add code[​](#step-4-add-code "Direct link to step-4-add-code")

1.  In the **Project** tool window, right-click the project's root folder, and click **New > Python File**.
    
2.  Enter `main.py` and double-click **Python file**.
    
3.  Enter the following code into the file and then save the file, depending on the name of your configuration profile.
    
    If your configuration profile from Step 1 is named `DEFAULT`, enter the following code into the file, and then save the file:
    
    Python
    
        from databricks.connect import DatabricksSessionspark = DatabricksSession.builder.getOrCreate()df = spark.read.table("samples.nyctaxi.trips")df.show(5)
    
    If your configuration profile from Step 1 is not named `DEFAULT`, enter the following code into the file instead. Replace the placeholder `<profile-name>` with the name of your configuration profile from Step 1, and then save the file:
    
    Python
    
        from databricks.connect import DatabricksSessionspark = DatabricksSession.builder.profile("<profile-name>").getOrCreate()df = spark.read.table("samples.nyctaxi.trips")df.show(5)
    

## Step 5: Run the code[​](#step-5-run-the-code "Direct link to Step 5: Run the code")

1.  Start the target cluster in your remote Databricks workspace.
2.  After the cluster has started, on the main menu, click **Run > Run 'main'**.
3.  In the **Run** tool window (**View > Tool Windows > Run**), in the **Run** tab's **main** pane, the first 5 rows of the `samples.nyctaxi.trips` appear.

## Step 6: Debug the code[​](#step-6-debug-the-code "Direct link to Step 6: Debug the code")

1.  With the cluster still running, in the preceding code, click the gutter next to `df.show(5)` to set a breakpoint.
2.  On the main menu, click **Run > Debug 'main'**.
3.  In the **Debug** tool window (**View > Tool Windows > Debug**), in the **Debugger** tab's **Variables** pane, expand the **df** and **spark** variable nodes to browse information about the code's `df` and `spark` variables.
4.  In the **Debug** tool window's sidebar, click the green arrow (**Resume Program**) icon.
5.  In the **Debugger** tab's **Console** pane, the first 5 rows of the `samples.nyctaxi.trips` appear.

![Debug the PyCharm project](https://docs.databricks.com/aws/en/assets/images/debug-project-pycharm-3baa84c65702559ee79f35eb4e68325a.png)
