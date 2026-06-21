---
title: Manage Unity Catalog metastores | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-metastore
ingestedAt: "2026-06-18T08:04:39.872Z"
---

This article shows how to update, delete, and manage the behavior of Unity Catalog metastores in your Databricks account.

To learn about Unity Catalog metastores and how to create them, see [Create a Unity Catalog metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/create-metastore).

To assign an existing Unity Catalog metastore automatically to new workspaces in that metastore's region, an account admin can enable workspace auto-assignment for the metastore. If this setting is not selected, the admin who creates a workspace in the same region as the metastore must manually enable the workspace for Unity Catalog and select the metastore from a drop-down.

Before an account admin enables this option, they should be sure to understand the following impacts on new workspaces:

*   A _workspace catalog_ will be created, and all workspace users will have the privileges required to create objects in it. See [Get started with Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/get-started).
*   Workspace admins will have the permissions required to create metastore-level securable objects, like catalogs and external locations. See [Workspace admin privileges when workspaces are enabled for Unity Catalog automatically](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/admin-privileges#workspace-admins-auto).
*   If metastore-level storage is already enabled for the metastore, the workspace will be able to use that storage. See [Specify a managed storage location in Unity Catalog](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/managed-storage).
*   If a metastore admin is defined for the metastore, they will be able to manage access to all securable objects in all workspaces attached to the metastore. See [Metastore admins](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/admin-privileges#metastore-admins).
*   The OpenSharing setting (enabled or disabled) for the metastore will apply to all workspaces attached to the metastore. See [Set up OpenSharing for your account (for providers)](https://docs.databricks.com/aws/en/delta-sharing/set-up).

To enable automatic assignment:

1.  As an account admin, go to the Databricks account console.
2.  Click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
3.  Select your metastore.
4.  On the **Configuration** tab, under **Workspace assignment**, select **Automatically assign new workspaces in `<region>` to this metastore**.
5.  On the confirmation dialog, click **Enable auto-assignment**.

Metastore-level managed storage is optional, and it is not included for metastores that were created automatically. You might want to add metastore-level storage to your metastore if you prefer a data isolation model that stores data centrally for multiple workspaces. You need metastore-level storage if you are a Databricks partner who uses personal staging locations.

See also [Specify a managed storage location in Unity Catalog](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/managed-storage).

### Requirements[​](#requirements "Direct link to Requirements")

*   You must have at least one workspace attached to the Unity Catalog metastore.
*   Databricks permissions required:
    *   To create an external location, you must have the `CREATE EXTERNAL LOCATION` and `CREATE STORAGE CREDENTIAL` privileges.
    *   To add the storage location to the metastore definition, you must be an account admin.
*   AWS permissions required: the ability to create S3 buckets, IAM roles, IAM policies, and cross-account trust relationships.

### Step 1: Create the storage location[​](#step-1-create-the-storage-location "Direct link to step-1-create-the-storage-location")

Follow the instructions in [Step 1 (Optional): Create an S3 bucket for metastore-level managed storage in AWS](https://docs.databricks.com/aws/en/data-governance/unity-catalog/create-metastore#cloud-tenant-setup-aws) to create a dedicated S3 bucket in an AWS account in the same region as your metastore.

### Step 2: Create an external location in Unity Catalog[​](#step-2-create-an-external-location-in-unity-catalog "Direct link to step-2-create-an-external-location-in-unity-catalog")

In this step, you create an external location in Unity Catalog that represents the bucket that you just created.

1.  Open a workspace that is attached to the metastore.
    
2.  Click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog** to open Catalog Explorer.
    
3.  Click the **\+ Add** button and select **Add an external location**.
    
4.  On the **Create a new external location** dialog, click **AWS Quickstart (Recommended)** and click **Next**.
    
    The AWS Quickstart configures the external location and creates a storage credential for you. If you choose to use the **Manual** option, you must manually create an IAM role that gives access to the S3 bucket and create the storage credential in Databricks yourself.
    
5.  On the **Create external location with Quickstart** dialog, enter the path to the S3 bucket in the **Bucket Name** field.
    
6.  Click **Generate new token** to generate the personal access token that you will use to authenticate between Databricks and your AWS account.
    
7.  Copy the token and click **Launch in Quickstart**.
    
8.  In the AWS CloudFormation template that launches (labeled **Quick create stack**), paste the token into the **Databricks Account Credentials** field.
    
9.  Accept the terms at the bottom of the page (**I acknowledge that AWS CloudFormation might create IAM resources with custom names**).
    
10.  Click **Create stack**.
     
     It may take a few minutes for the CloudFormation template to finish creating the external location object in Databricks.
     
11.  Return to your Databricks workspace and go to the **External locations** pane in **Catalog Explorer**.
     
     In the left pane of Catalog Explorer, scroll down and click ![Plug icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xNC4xNjc5IDIuOTUzNDZMMTUuMDYwNyAyLjA2MDY2TDE0IDFMMTMuMTA3MiAxLjg5Mjc5QzExLjU1MDQgMC44MzI0MTYgOS40MTExNiAwLjk5MjY0NCA4LjAzMDMyIDIuMzczNDhMNy4xNDY0NCAzLjI1NzM2QzcuMDA1NzkgMy4zOTgwMSA2LjkyNjc3IDMuNTg4NzggNi45MjY3NyAzLjc4NzY5QzYuOTI2NzcgMy45ODY2MSA3LjAwNTc5IDQuMTc3MzcgNy4xNDY0NCA0LjMxODAyTDExLjc0MjYgOC45MTQyMkMxMi4wMzU1IDkuMjA3MTEgMTIuNTEwNCA5LjIwNzExIDEyLjgwMzMgOC45MTQyMkwxMy42ODcyIDguMDMwMzNDMTUuMDY4IDYuNjQ5NSAxNS4yMjgyIDQuNTEwMjkgMTQuMTY3OSAyLjk1MzQ2Wk0xMi42MjY1IDYuOTY5NjdMMTIuMjczIDcuMzIzMjNMOC43Mzc0MyAzLjc4NzY5TDkuMDkwOTggMy40MzQxNEMxMC4wNjczIDIuNDU3ODMgMTEuNjUwMiAyLjQ1NzgzIDEyLjYyNjUgMy40MzQxNEMxMy42MDI4IDQuNDEwNDUgMTMuNjAyOCA1Ljk5MzM2IDEyLjYyNjUgNi45Njk2N1oiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik03LjMyMzIzIDEwLjE1MTZMNS45MDkwMSA4LjczNzQxTDcuMzIzMjMgNy4zMjMyTDYuMjYyNTcgNi4yNjI1NEw0Ljg0ODM1IDcuNjc2NzVMNC4zMTgwMiA3LjE0NjQyQzQuMDI1MTMgNi44NTM1MyAzLjU1MDI2IDYuODUzNTMgMy4yNTczNiA3LjE0NjQyTDIuMzczNDggOC4wMzAzMUMwLjk5MjY0NiA5LjQxMTE0IDAuODMyNDE2IDExLjU1MDQgMS44OTI3OSAxMy4xMDcyTDEgMTRMMi4wNjA2NiAxNS4wNjA2TDIuOTUzNDUgMTQuMTY3OUM0LjUxMDI4IDE1LjIyODIgNi42NDk1IDE1LjA2OCA4LjAzMDMzIDEzLjY4NzJMOC45MTQyMiAxMi44MDMzQzkuMjA3MTEgMTIuNTEwNCA5LjIwNzExIDEyLjAzNTUgOC45MTQyMiAxMS43NDI2TDguMzgzODkgMTEuMjEyM0w5Ljc5ODEgOS43OTgwN0w4LjczNzQ0IDguNzM3NDFMNy4zMjMyMyAxMC4xNTE2Wk0zLjQzNDE0IDEyLjYyNjVDNC40MTA0NSAxMy42MDI4IDUuOTkzMzYgMTMuNjAyOCA2Ljk2OTY3IDEyLjYyNjVMNy4zMjMyMyAxMi4yNzI5TDMuNzg3NjkgOC43Mzc0MUwzLjQzNDE0IDkuMDkwOTdDMi40NTc4MyAxMC4wNjczIDIuNDU3ODMgMTEuNjUwMiAzLjQzNDE0IDEyLjYyNjVaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Connect**, then click **External locations**.
     
12.  Confirm that a new external location has been created.
     
     Automatically-generated external locations use the naming syntax `db_s3_external_databricks-S3-ingest-<id>`.
     
13.  Grant yourself the `CREATE MANAGED STORAGE` privilege on the external location.
     
     1.  Click the external location name to open the details pane.
     2.  On the **Permissions** tab, click **Grant**.
     3.  On the **Grant on `<external location>`** dialog, select yourself in the **Principals** field and select `CREATE MANAGED STORAGE`.
     4.  Click **Grant**.

### Step 3: Add the storage location to the metastore[​](#step-3-add-the-storage-location-to-the-metastore "Direct link to Step 3: Add the storage location to the metastore")

After you have created an external location that represents the metastore storage bucket, you can add it to the metastore.

1.  As an account admin, log in to the [account console](https://accounts.cloud.databricks.com/).
    
2.  Click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
    
3.  Click the metastore name.
    
4.  Confirm that you are the **Metastore Admin**.
    
    If you are not, click **Edit** and assign yourself as the metastore admin. You can unassign yourself when you are done with this procedure.
    
5.  On the **Configuration** tab, next to **S3 bucket path**, click **Set**.
    
6.  On the **Set metastore root** dialog, enter the S3 bucket path that you used to create the external location, and click **Update**.
    
    You cannot modify this path once you set it, but you can remove it and add a new path if necessary.
    

If you have metastore-level storage for managed tables and volumes (also known as the metastore storage root), but you want to enforce data storage isolation at the catalog or schema level, you can remove the metastore-level storage option for the metastore. When you do, the following happens:

*   Existing catalogs that have no storage root specified are given the metastore storage root's cloud storage location as their catalog-level managed storage location. In other words, the metastore storage root is “pushed down” to these catalogs. Access to data in these catalogs continues to function without interruption.
*   Depending on how your metastore was created, there might not be an external location securable defined in Unity Catalog for the metastore storage root. In that case, a new external location and associated storage credential are created for it. The new external location is named `prior_metastore_root_location` by default.
*   Every time a user creates a catalog, they must provide a dedicated storage location that is registered in Unity Catalog as an external location.

note

If you use OpenSharing to share notebooks and you used the metastore root as shared notebook storage, you must do the following before you can remove the metastore root:

1.  Remove your notebook from the share.
2.  Re-add the notebook using a dedicated storage location.

See [Add notebook files to a share](https://docs.databricks.com/aws/en/delta-sharing/create-share#add-remove-notebook-files).

To remove the metastore storage root:

1.  As an account admin, log in to the [account console](https://accounts.cloud.databricks.com/).
2.  Click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
3.  Click the metastore name.
4.  On the **Configuration** tab, under **S3 bucket path**, click the **Remove** button.
5.  On the confirmation dialog, click **Remove**.

Metastore admins are optional, but there are situations where you might want one for your metastore. See [Assign a metastore admin](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/admin-privileges#assign-metastore-admin).

If you are closing your Databricks account or have another reason to delete access to data managed by your Unity Catalog metastore, you can delete the metastore.

warning

All objects managed by the metastore will become inaccessible using Databricks workspaces. This action cannot be undone.

[Managed table](https://docs.databricks.com/aws/en/tables/managed) data and metadata will be auto-deleted after 30 days. External table data in your cloud storage is not affected by metastore deletion.

To delete a metastore:

1.  As a metastore admin, log in to the [account console](https://accounts.cloud.databricks.com/).
2.  Click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
3.  Click the metastore name.
4.  On the **Configuration** tab, click the three-button menu at the far upper right and select **Delete**.
5.  On the confirmation dialog, enter the name of the metastore and click **Delete**.
