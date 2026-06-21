---
title: Databricks Connect for R | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/r/
ingestedAt: "2026-06-18T08:06:34.985Z"
---

note

This article covers `sparklyr` integration with Databricks Connect for Databricks Runtime 13.0 and above. This integration is neither provided by Databricks nor directly supported by Databricks.

For questions, go to the [Posit Community](https://community.rstudio.com/).

To report issues, go to the [Issues](https://github.com/sparklyr/sparklyr/issues) section of the `sparklyr` repository in GitHub.

For more information, see [Databricks Connect v2](https://spark.rstudio.com/deployment/databricks-connect.html) in the `sparklyr` documentation.

Databricks Connect enables you to connect popular IDEs such as RStudio Desktop, notebook servers, and other custom applications to Databricks clusters. See [Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/).

note

Databricks Connect has limited compatibility with [Apache Spark MLlib](https://spark.apache.org/mllib/), because Spark MLlib uses RDDs, while Databricks Connect only supports the DataFrame API. To use all of sparklyr's Spark MLlib functions, use Databricks notebooks or the `db_repl` function of the [brickster package](https://databrickslabs.github.io/brickster/).

This article demonstrates how to quickly get started with Databricks Connect for R using `sparklyr` and [RStudio Desktop](https://posit.co/download/rstudio-desktop/).

*   For Databricks Connect for Python, see [Databricks Connect for Python](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/).
*   For Databricks Connect for Scala, see [Databricks Connect for Scala](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/).

## Tutorial[​](#tutorial "Direct link to Tutorial")

In the following tutorial you create a project in RStudio, install and configure Databricks Connect for Databricks Runtime 13.3 LTS and above, and run simple code on compute in your Databricks workspace from RStudio. For supplemental information about this tutorial, see the “Databricks Connect” section of [Spark Connect, and Databricks Connect v2](https://spark.rstudio.com/deployment/databricks-spark-connect) on the `sparklyr` website.

This tutorial uses RStudio Desktop and Python 3.10. If you don't have them already installed, [install R and RStudio Desktop](https://posit.co/download/rstudio-desktop/) and Python 3.10.

## Requirements[​](#requirements "Direct link to Requirements")

To complete this tutorial, you must meet the following requirements:

*   Your target Databricks workspace and cluster must meet the requirements for [Compute configuration for Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config).
*   You must have your cluster ID available. To get your cluster ID, in your workspace, click **Compute** on the sidebar, and then click your cluster's name. In your web browser's address bar, copy the string of characters between `clusters` and `configuration` in the URL.

## Step 1: Create a personal access token[​](#step-1-create-a-personal-access-token "Direct link to step-1-create-a-personal-access-token")

note

Databricks Connect for R authentication currently only supports Databricks personal access tokens.

This tutorial uses Databricks [personal access token authentication](https://docs.databricks.com/aws/en/dev-tools/auth/pat) for authenticating with your Databricks workspace.

If you already have a Databricks personal access token, skip to Step 2. If you are not sure whether you already have a Databricks personal access token, you can follow this step without affecting any other Databricks personal access tokens in your user account.

To create a personal access token, follow the steps in [Create personal access tokens for workspace users](https://docs.databricks.com/aws/en/dev-tools/auth/pat#pat-user).

## Step 2: Create the project[​](#step-2-create-the-project "Direct link to step-2-create-the-project")

1.  Start RStudio Desktop.
2.  On the main menu, click **File > New Project**.
3.  Select **New Directory**.
4.  Select **New Project**.
5.  For **Directory name** and **Create project as subdirectory of**, enter the new project directory's name and where to create this new project directory.
6.  Select **Use renv with this project**. If prompted to install an updated version of the `renv` package, click **Yes**.
7.  Click **Create Project**.

![Create the RStudio Desktop project](https://docs.databricks.com/aws/en/assets/images/create-project-rstudio-cb2270663722e06336243fdd7847b3d0.png)

## Step 3: Add the Databricks Connect package and other dependencies[​](#step-3-add-the-databricks-connect-package-and-other-dependencies "Direct link to step-3-add-the-databricks-connect-package-and-other-dependencies")

1.  On the RStudio Desktop main menu, click **Tools > Install Packages**.
    
2.  Leave **Install from** set to **Repository (CRAN)**.
    
3.  For **Packages**, enter the following list of packages that are prerequisites for the Databricks Connect package and this tutorial:
    
        sparklyr,pysparklyr,reticulate,usethis,dplyr,dbplyr
    
4.  Leave **Install to Library** set to your R virtual environment.
    
5.  Make sure that **Install dependencies** is selected.
    
6.  Click **Install**.
    

![Install the Databricks Connect package dependencies](https://docs.databricks.com/aws/en/assets/images/add-pkg-deps-rstudio-6b929d34a13ea8a498b49b08de4d8253.png)

1.  When you are prompted in the **Console** view (**View > Move Focus to Console**) to proceed with the installation, enter `Y`. The `sparklyr` and `pysparklyr` packages and their dependencies are installed in your R virtual environment.
    
2.  In the **Console** pane, use `reticulate` to install Python by running the following command. (Databricks Connect for R requires `reticulate` and Python to be installed first.) In the following command, replace `3.10` with the major and minor version of the Python version that is installed on your Databricks cluster. To find this major and minor version, see the “System environment” section of the release notes for your cluster's Databricks Runtime version in [Databricks Runtime release notes versions and compatibility](https://docs.databricks.com/aws/en/release-notes/runtime/).
    
        reticulate::install_python(version = "3.10")
    
3.  In the **Console** pane, install the Databricks Connect package by running the following command. In the following command, replace `13.3` with the Databricks Runtime version that is installed on your Databricks cluster. To find this version, on your cluster's details page in your Databricks workspace, on the **Configuration** tab, see the **Databricks Runtime Version** box.
    
        pysparklyr::install_databricks(version = "13.3")
    
    If you do not know the Databricks Runtime version for your cluster or you do not want to look it up, you can run the following command instead, and `pysparklyr` will query the cluster to determine the correct Databricks Runtime version to use:
    
        pysparklyr::install_databricks(cluster_id = "<cluster-id>")
    
    If you want your project to connect later to a different cluster that has the same Databricks Runtime version than the one that you just specified, `pysparklyr` will use the same Python environment. If the new cluster has a different Databricks Runtime version, you should run the `pysparklyr::install_databricks` command again with the new Databricks Runtime version or cluster ID.
    

## Step 4: Set environment variables for the workspace URL, access token, and cluster ID[​](#step-4-set-environment-variables-for-the-workspace-url-access-token-and-cluster-id "Direct link to step-4-set-environment-variables-for-the-workspace-url-access-token-and-cluster-id")

Databricks does not recommend that you hard-code sensitive or changing values such as your Databricks workspace URL, Databricks personal access token, or Databricks cluster ID into your R scripts. Instead, store these values separately, for example in local environment variables. This tutorial uses RStudio Desktop's built-in support for storing environment variables in a `.Renviron` file.

1.  Create an `.Renviron` file to store the environment variables, if this file does not already exist, and then open this file for editing: in the RStudio Desktop **Console**, run the following command:
    
        usethis::edit_r_environ()
    
2.  In the `.Renviron` file that appears (**View > Move Focus to Source**), enter the following content. In this content, replace the following placeholders:
    
    *   Replace `<workspace-url>` with your [workspace instance URL](https://docs.databricks.com/aws/en/workspace/workspace-details#workspace-url), for example `https://dbc-a1b2345c-d6e7.cloud.databricks.com`.
    *   Replace `<personal-access-token>` with your Databricks personal access token from Step 1.
    *   Replace `<cluster-id>` with your cluster ID from this tutorial's requirements.
    
        DATABRICKS_HOST=<workspace-url>DATABRICKS_TOKEN=<personal-access-token>DATABRICKS_CLUSTER_ID=<cluster-id>
    
3.  Save the `.Renviron` file.
    
4.  Load the environment variables into R: on the main menu, click **Session > Restart R**.
    

![Set the environment variables for Databricks Connect](https://docs.databricks.com/aws/en/assets/images/set-env-vars-rstudio-10cd0d330209f879e5ea5735f18329d2.png)

## Step 5: Add code[​](#step-5-add-code "Direct link to step-5-add-code")

1.  On the RStudio Desktop main menu, click **File > New File > R Script**.
    
2.  Enter the following code into the file and then save the file (**File > Save**) as `demo.R`:
    
    R
    
        library(sparklyr)library(dplyr)library(dbplyr)sc <- sparklyr::spark_connect(  master     = Sys.getenv("DATABRICKS_HOST"),  cluster_id = Sys.getenv("DATABRICKS_CLUSTER_ID"),  token      = Sys.getenv("DATABRICKS_TOKEN"),  method     = "databricks_connect",  envname    = "r-reticulate")trips <- dplyr::tbl(  sc,  dbplyr::in_catalog("samples", "nyctaxi", "trips"))print(trips, n = 5)
    

## Step 6: Run the code[​](#step-6-run-the-code "Direct link to Step 6: Run the code")

1.  On the RStudio Desktop, in the toolbar for the `demo.R` file, click **Source**.
    
    ![Run the RStudio Desktop project](https://docs.databricks.com/aws/en/assets/images/run-file-rstudio-d2d919f799bdbcf658c9692fe0483d50.png)
    
2.  In the **Console**, the first five rows of the `trips` table appear.
    
3.  In the **Connections** view (**View > Show Connections**), you can explore available catalogs, schemas, tables, and views.
    
    ![The Connections view for the project](https://docs.databricks.com/aws/en/assets/images/connections-view-rstudio-accf8e4c09c5c46a695d63033d4fb515.png)
    

## Step 7: Debug the code[​](#step-7-debug-the-code "Direct link to Step 7: Debug the code")

1.  In the `demo.R` file, click the gutter next to `print(trips, n = 5)` to set a breakpoint.
2.  In the toolbar for the `demo.R` file, click **Source**.
3.  When the code pauses running at the breakpoint, you can inspect variable in the **Environment** view (**View > Show Environment**).
4.  On the main menu, click **Debug > Continue**.
5.  In the **Console**, the first five rows of the `trips` table appear.

![Debug the RStudio Desktop project](https://docs.databricks.com/aws/en/assets/images/debug-project-rstudio-80040085277ea83850c52bbfd1a1927a.png)
