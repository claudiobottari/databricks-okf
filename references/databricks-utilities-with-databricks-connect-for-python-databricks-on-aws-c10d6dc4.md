---
title: Databricks Utilities with Databricks Connect for Python | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/databricks-utilities
ingestedAt: "2026-06-18T08:06:14.810Z"
---

note

This article covers Databricks Connect for Databricks Runtime 13.3 LTS and above.

This article describes how to use [Databricks Utilities](https://docs.databricks.com/aws/en/dev-tools/databricks-utils) with Databricks Connect for Python. Databricks Connect enables you to connect popular IDEs, notebook servers, and custom applications to Databricks clusters. See [Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/).

Before you begin to use Databricks Connect, you must [set up the Databricks Connect client](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/install).

For the Scala version of this article, see [Databricks Utilities with Databricks Connect for Scala](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/databricks-utilities).

## Available Databricks Utilities[​](#available-databricks-utilities "Direct link to Available Databricks Utilities")

You use Databricks Connect to access Databricks Utilities as follows:

*   Use the `WorkspaceClient` class's `dbutils` variable to access Databricks Utilities. The `WorkspaceClient` class belongs to the [Databricks SDK for Python](https://pypi.org/project/databricks-sdk) and is included in Databricks Connect.
*   Use `dbutils.fs` to access the Databricks Utilities [fs](https://docs.databricks.com/aws/en/dev-tools/databricks-utils#file-system-utility-dbutilsfs) utility.
*   Use `dbutils.secrets` to access the Databricks Utilities [secrets](https://docs.databricks.com/aws/en/dev-tools/databricks-utils#secrets-utility-dbutilssecrets) utility.

No Databricks Utilities functionality other than the preceding utilities are available through `dbutils`.

tip

You can also use the included Databricks SDK for Python to access any available Databricks REST API, not just the preceding Databricks Utilities APIs. See [databricks-sdk](https://pypi.org/project/databricks-sdk) on PyPI.

## Intialize the WorkspaceClient[​](#intialize-the-workspaceclient "Direct link to Intialize the WorkspaceClient")

To initialize `WorkspaceClient`, you must provide enough information to authenticate an Databricks SDK with the workspace. For example, you can:

*   Hard-code the workspace URL and your access token directly within your code, and then initialize `WorkspaceClient` as follows. Although this option is supported, Databricks **does not recommend** this option, as it can expose sensitive information, such as access tokens, if your code is checked into version control or otherwise shared:
    
    Python
    
        from databricks.sdk import WorkspaceClientw = WorkspaceClient(host  = f"https://{retrieve_workspace_instance_name()}",                    token = retrieve_token())
    
*   Create or specify a [configuration profile](https://docs.databricks.com/aws/en/dev-tools/auth/config-profiles) that contains the fields `host` and `token`, and then intialize the `WorkspaceClient` as follows:
    
    Python
    
        from databricks.sdk import WorkspaceClientw = WorkspaceClient(profile = "<profile-name>")
    
*   Set the environment variables `DATABRICKS_HOST` and `DATABRICKS_TOKEN` in the same way you set them for Databricks Connect, and then initialize `WorkspaceClient` as follows:
    
    Python
    
        from databricks.sdk import WorkspaceClientw = WorkspaceClient()
    

The Databricks SDK for Python does not recognize the `SPARK_REMOTE` environment variable for Databricks Connect.

For additional Databricks authentication options for the Databricks SDK for Python, as well as how to initialize `AccountClient` within the Databricks SDKs to access available Databricks REST APIs at the account level instead of at the workspace level, see [databricks-sdk](https://pypi.org/project/databricks-sdk) on PyPI.

## Example: Create a file in a volume[​](#example-create-a-file-in-a-volume "Direct link to Example: Create a file in a volume")

The following example shows how to use the Databricks SDK for Python to automate Databricks Utilities. This example creates a file named `zzz_hello.txt` in a Unity Catalog volume's path within the workspace, reads the data from the file, and then deletes the file. This example assumes that the environment variables `DATABRICKS_HOST` and `DATABRICKS_TOKEN` have already been set:

Python

    from databricks.sdk import WorkspaceClientw = WorkspaceClient()file_path = "/Volumes/main/default/my-volume/zzz_hello.txt"file_data = "Hello, Databricks!"fs = w.dbutils.fsfs.put(  file      = file_path,  contents  = file_data,  overwrite = True)print(fs.head(file_path))fs.rm(file_path)

See also [Interaction with dbutils](https://databricks-sdk-py.readthedocs.io/en/latest/dbutils.html) in the Databricks SDK for Python documentation.
