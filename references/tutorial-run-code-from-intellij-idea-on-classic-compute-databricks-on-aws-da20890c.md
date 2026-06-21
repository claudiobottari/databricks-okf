---
title: "Tutorial: Run code from IntelliJ IDEA on classic compute | Databricks on AWS"
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/tutorial
ingestedAt: "2026-06-18T08:06:53.791Z"
---

This tutorial demonstrates how to get started with Databricks Connect for Scala using [IntelliJ IDEA](https://www.jetbrains.com/help/idea/installation-guide.html) and the [Scala plugin](https://www.jetbrains.com/help/idea/discover-intellij-idea-for-scala.html).

In this tutorial you create a project in IntelliJ IDEA, install Databricks Connect for Databricks Runtime 13.3 LTS and above, and run simple code on compute in your Databricks workspace from IntelliJ IDEA.

## Requirements[​](#requirements "Direct link to Requirements")

To complete this tutorial, you must meet the following requirements:

*   Your workspace, local environment, and compute meet the requirements for Databricks Connect for Scala. See [Databricks Connect usage requirements](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements).
    
*   You must have your cluster ID available. To get your cluster ID, in your workspace, click **Compute** on the sidebar, and then click your cluster's name. In your web browser's address bar, copy the string of characters between `clusters` and `configuration` in the URL.
    
*   You have the Java Development Kit (JDK) installed on your development machine. For information about the version to install, see [version support matrix](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements#versions).
    
    note
    
    If you do not have a JDK installed, or if you have multiple JDK installs on your development machine, you can install or choose a specific JDK later in Step 1. Choosing a JDK install that is below or above the JDK version on your cluster might produce unexpected results, or your code might not run at all.
    
*   You have [IntelliJ IDEA](https://www.jetbrains.com/help/idea/installation-guide.html) installed. This tutorial was tested with IntelliJ IDEA Community Edition 2023.3.6. If you use a different version or edition of IntelliJ IDEA, the following instructions might vary.
    
*   You have the [Scala plugin](https://www.jetbrains.com/help/idea/discover-intellij-idea-for-scala.html) for IntelliJ IDEA installed.
    

## Step 1: Configure Databricks authentication[​](#step-1-configure-databricks-authentication "Direct link to step-1-configure-databricks-authentication")

This tutorial uses Databricks [OAuth user-to-machine (U2M) authentication](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-u2m) and a Databricks [configuration profile](https://docs.databricks.com/aws/en/dev-tools/auth/config-profiles) for authenticating with your Databricks workspace. To use a different authentication type instead, see [Configure connection properties](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config).

Configuring OAuth U2M authentication requires the Databricks CLI, as follows:

1.  Install the [Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/install):
    
    *   Linux, macOS
    *   Windows
    
    Use [Homebrew](https://brew.sh/) to install the Databricks CLI by running the following commands:
    
    Bash
    
        brew tap databricks/tapbrew trust databricks/tapbrew install databricks
    
    The `brew trust` command is required as of [Homebrew 6.0.0](https://docs.brew.sh/Tap-Trust).
    
2.  Confirm that the Databricks CLI is installed by running the following command, which displays the current version of the installed Databricks CLI. This version should be 0.205.0 or above:
    

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

1.  Start IntelliJ IDEA.
    
2.  On the main menu, click **File > New > Project**.
    
3.  Give your project some meaningful **Name**.
    
4.  For **Location**, click the folder icon, and complete the on-screen directions to specify the path to your new Scala project.
    
5.  For **Language**, click **Scala**.
    
6.  For **Build system**, click **sbt**.
    
7.  In the **JDK** drop-down list, select an existing installation of the JDK on your development machine that matches the JDK version on your cluster, or select **Download JDK** and follow the on-screen instructions to download a JDK that matches the JDK version on your cluster. See [Requirements](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/install#requirements).
    
    note
    
    Choosing a JDK install that is above or below the JDK version on your cluster might produce unexpected results, or your code might not run at all.
    
8.  In the **sbt** drop-down list, select the latest version.
    
9.  In the **Scala** drop-down list, select the version of Scala that matches the Scala version on your cluster. See [Requirements](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/install#requirements).
    
    note
    
    Choosing a Scala version that is below or above the Scala version on your cluster might produce unexpected results, or your code might not run at all.
    
10.  Make sure the **Download sources** box next to **Scala** is checked.
     
11.  For **Package prefix**, enter some package prefix value for your project's sources, for example `org.example.application`.
     
12.  Make sure the **Add sample code** box is checked.
     
13.  Click **Create**.
     

![Create the IntelliJ IDEA project](https://docs.databricks.com/aws/en/assets/images/create-project-intellij-idea-a91ec29fe7cf255fac2b530c6f893741.png)

## Step 3: Add the Databricks Connect package[​](#step-3-add-the-databricks-connect-package "Direct link to Step 3: Add the Databricks Connect package")

1.  With your new Scala project open, in your **Project** tool window (**View > Tool Windows > Project**), open the file named `build.sbt`, in **_project-name_ > target**.
    
2.  Add the following code to the end of the `build.sbt` file, which declares your project's dependency on a specific version of the Databricks Connect library for Scala, compatible with the Databricks Runtime version of your cluster:
    
        libraryDependencies += "com.databricks" %% "databricks-connect" % "17.3.+"
    
    Replace `17.3` with the version of the Databricks Connect library that matches the Databricks Runtime version on your cluster. For example, Databricks Connect 17.3.+ matches Databricks Runtime 17.3 LTS. You can find the Databricks Connect library version numbers in the [Maven central repository (for Databricks Runtime 16.4 LTS and below)](https://central.sonatype.com/artifact/com.databricks/databricks-connect/versions) or the [Maven central repository (for Databricks Runtime 17.0 and above)](https://central.sonatype.com/artifact/com.databricks/databricks-connect_2.13/versions).
    
    note
    
    When building with Databricks Connect, do not include Apache Spark artifacts such as `org.apache.spark:spark-core` in your project. Instead, compile directly against Databricks Connect.
    
3.  Click the **Load sbt changes** notification icon to update your Scala project with the new library location and dependency.
    
    ![Install the Databricks Connect package](https://docs.databricks.com/aws/en/assets/images/install-package-intellij-idea-8be9adc402504f2d5d69099572d31693.png)
    
4.  Wait until the `sbt` progress indicator at the bottom of the IDE disappears. The `sbt` load process might take a few minutes to complete.
    

## Step 4: Add code[​](#step-4-add-code "Direct link to Step 4: Add code")

1.  In your **Project** tool window, open the file named `Main.scala`, in **_project-name_ > src > main > scala**.
    
2.  Replace any existing code in the file with the following code and then save the file, depending on the name of your configuration profile.
    
    If your configuration profile from Step 1 is named `DEFAULT`, replace any existing code in the file with the following code, and then save the file:
    
    Scala
    
        package org.example.applicationimport com.databricks.connect.DatabricksSessionimport org.apache.spark.sql.SparkSessionobject Main {  def main(args: Array[String]): Unit = {    val spark = DatabricksSession.builder().remote().getOrCreate()    val df = spark.read.table("samples.nyctaxi.trips")    df.limit(5).show()  }}
    
    If your configuration profile from Step 1 is not named `DEFAULT`, replace any existing code in the file with the following code instead. Replace the placeholder `<profile-name>` with the name of your configuration profile from Step 1, and then save the file:
    
    Scala
    
        package org.example.applicationimport com.databricks.connect.DatabricksSessionimport com.databricks.sdk.core.DatabricksConfigimport org.apache.spark.sql.SparkSessionobject Main {  def main(args: Array[String]): Unit = {    val config = new DatabricksConfig().setProfile("<profile-name>")    val spark = DatabricksSession.builder().sdkConfig(config).getOrCreate()    val df = spark.read.table("samples.nyctaxi.trips")    df.limit(5).show()  }}
    

## Step 5: Configure the VM options[​](#step-5-configure-the-vm-options "Direct link to Step 5: Configure the VM options")

1.  Import the current directory in your IntelliJ where `build.sbt` is located.
    
2.  Choose Java 17 in IntelliJ. Go to **File** > **Project Structure** > **SDKs**.
    
3.  Open `src/main/scala/com/examples/Main.scala`.
    
4.  Navigate to the configuration for Main to add VM options:
    
    ![Edit Main](https://docs.databricks.com/aws/en/assets/images/intellij-edit-main-a9dc8082bb05ddd6a445803bb8ecbf61.png)
    
    ![Add VM options](https://docs.databricks.com/aws/en/assets/images/intellij-add-vm-options-dbac1d0679b4d0e91bd7c7f385948202.png)
    
5.  Add the following to your VM options:
    
        --add-opens=java.base/java.nio=ALL-UNNAMED
    

tip

Alternatively, or if you are using Visual Studio Code, add the following to your sbt build file:

    fork := truejavaOptions += "--add-opens=java.base/java.nio=ALL-UNNAMED"

Then run your application from the terminal:

## Step 6: Run the code[​](#step-6-run-the-code "Direct link to Step 6: Run the code")

1.  Start the target cluster in your remote Databricks workspace.
2.  After the cluster has started, on the main menu, click **Run > Run 'Main'**.
3.  In the **Run** tool window (**View > Tool Windows > Run**), on the **Main** tab, the first 5 rows of the `samples.nyctaxi.trips` table appear.

## Step 7: Debug the code[​](#step-7-debug-the-code "Direct link to Step 7: Debug the code")

1.  With the target cluster still running, in the preceding code, click the gutter next to `df.limit(5).show()` to set a breakpoint.
    
2.  On the main menu, click **Run > Debug 'Main'**. In the **Debug** tool window (**View > Tool Windows > Debug**), on the **Console** tab, click the calculator (**Evaluate Expression**) icon.
    
3.  Enter the expression `df.schema`.
    
4.  Click **Evaluate** to show the DataFrame's schema.
    
5.  In the **Debug** tool window's sidebar, click the green arrow (**Resume Program**) icon. The first 5 rows of the `samples.nyctaxi.trips` table appear in the **Console** pane.
    
    ![Debug the IntelliJ IDEA project](https://docs.databricks.com/aws/en/assets/images/debug-project-intellij-idea-ce552e63b64c361c7113e9b84eb9c2ba.png)
