---
title: Create a Unity Catalog metastore | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/create-metastore
ingestedAt: "2026-06-18T08:03:57.747Z"
---

This page shows how to create a Unity Catalog metastore and link it to workspaces.

important

For workspaces that were enabled for Unity Catalog automatically, the instructions in this page are unnecessary. Databricks began to enable new workspaces for Unity Catalog automatically on November 8, 2023, with a rollout proceeding gradually across accounts. You must follow the instructions in this page only if you have a workspace and don't already have a metastore in your workspace region. To determine whether a metastore already exists in your region, see [Get started with Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/get-started).

A metastore is the top-level container for data in Unity Catalog. Unity Catalog metastores register metadata about securable objects (such as tables, volumes, external locations, and shares) and the permissions that govern access to them. Each metastore exposes a three-level namespace (`catalog`.`schema`.`table`) by which data can be organized. You must have one metastore for each region in which your organization operates. To work with Unity Catalog, users must be on a workspace that is attached to a metastore in their region.

To create a metastore, you do the following:

1.  In your AWS account, optionally create a storage location for metastore-level storage of managed tables and volumes.
    
    For information to help you decide whether you need metastore-level storage, see [Specify a managed storage location in Unity Catalog](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/managed-storage) and [Specify a managed storage location in Unity Catalog](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/managed-storage).
    
2.  In your AWS account, create an IAM role that gives access to that storage location.
    
3.  In Databricks, create the metastore, attaching the storage location, and assign workspaces to the metastore.
    

## Before you begin[​](#before-you-begin "Direct link to Before you begin")

Before you begin, you should familiarize yourself with the basic Unity Catalog concepts, including metastores and managed storage. See [What is Unity Catalog?](https://docs.databricks.com/aws/en/data-governance/unity-catalog/).

You should also confirm that you meet the following requirements for all setup steps:

*   You must be a Databricks account admin.
*   Your Databricks account must be on the [Premium plan or above](https://databricks.com/product/pricing/platform-addons).
*   If you want to set up metastore-level root storage, you must have the ability to create S3 buckets, IAM roles, IAM policies, and cross-account trust relationships in your AWS account.

In this step, which is optional, you create the S3 bucket required by Unity Catalog to store managed table and volume data at the metastore level. You create the S3 bucket in your own AWS account. To determine whether you need metastore-level storage, see [Specify a managed storage location in Unity Catalog](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/managed-storage).

1.  In AWS, create an S3 bucket.
    
    This S3 bucket will be the metastore-level storage location for managed tables and managed volumes in Unity Catalog. This storage location can be overridden at the catalog and schema levels. See [Specify a managed storage location in Unity Catalog](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/managed-storage)
    
    Requirements:
    
    *   If you have more than one metastore, you should use a dedicated S3 bucket for each one.
    *   Locate the bucket in the same region as the workspaces you want to access the data from.
    *   Do not use dot notation (for example, `incorrect.bucket.name.notation`) in S3 bucket names. Although AWS allows dots in bucket names, Databricks does not support S3 buckets with dot notation. Buckets containing dots can cause compatibility issues with features like OpenSharing due to SSL certificate validation failures. For more information, see the [AWS bucket naming best practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html#automatically-created-buckets).
    *   The bucket cannot have an S3 access control list attached to it.
2.  Make a note of the S3 bucket path, which starts with `s3://`.
    
3.  If you enable KMS encryption on the S3 bucket, make a note of the name of the KMS encryption key.
    

## Step 2 (Optional): Create an IAM role to access the storage location[​](#step-2-optional-create-an-iam-role-to-access-the-storage-location "Direct link to step-2-optional-create-an-iam-role-to-access-the-storage-location")

In this step, which is required only if you completed step 1, you create the IAM role required by Unity Catalog to access the S3 bucket that you created in the previous step. Follow these instructions in [Create a storage credential that accesses an AWS S3 bucket](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/s3/s3-external-location-manual#create-storage-credential):

*   [Step 1: Create an IAM role](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/s3/s3-external-location-manual#create-storage-credentials-1)
*   [Step 2: Give Databricks the IAM role details](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/s3/s3-external-location-manual#create-storage-credentials-2)
*   [Step 3: Update the IAM role trust relationship policy](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/s3/s3-external-location-manual#create-storage-credentials-3)

Each Databricks region requires its own Unity Catalog metastore.

You create a metastore for each region in which your organization operates. You can link each of these regional metastores to any number of workspaces in that region. Each linked workspace has the same view of the data in the metastore, and data access control can be managed across workspaces. You can access data in other metastores using [OpenSharing](https://docs.databricks.com/aws/en/delta-sharing/).

If you chose to create metastore-level storage, the metastore will use the the S3 bucket and IAM role that you created in the previous steps.

To create a metastore:

1.  Log in to the Databricks [account console](https://accounts.cloud.databricks.com/).
    
2.  Click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
    
3.  Click **Create metastore**.
    
4.  Enter the following:
    
    *   A name for the metastore.
        
    *   The region where you want to deploy the metastore.
        
        This must be in the same region as the workspaces you want to use to access the data. Make sure that this matches the region of the storage bucket you created earlier.
        
    *   (Optional) The S3 bucket path (you can omit `s3://`) and IAM role name for the bucket and role you created in the previous steps.
        
5.  Click **Create**.
    
6.  When prompted, select workspaces to link to the metastore.
    
    For details, see [Enable a workspace for Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/enable-workspaces).
    
7.  Transfer the metastore admin role to a group.
    
    The user who creates a metastore is its owner, also called the metastore admin. The metastore admin can create top-level objects in the metastore such as catalogs and can manage access to tables and other objects. Databricks recommends that you reassign the metastore admin role to a group. See [Assign a metastore admin](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/admin-privileges#assign-metastore-admin).
    
8.  Enable Databricks management of uploads to managed volumes.
    
    Databricks uses cross-origin resource sharing (CORS) to upload data to [managed volumes](https://docs.databricks.com/aws/en/volumes/) in Unity Catalog.
    
    If, instead of using the instructions that follow, you want to use an AWS CloudFormation template, be aware that CloudFormation uses some property names that differ from those listed in these instructions. Use the [CORS configuration instructions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-cors.html) in the AWS CloudFormation reference to get the correct property names.
    
    1.  Use the AWS console to select your bucket from the buckets list.
        
    2.  Select **Permissions**.
        
    3.  Select **Edit** under **Cross-origin resource sharing (CORS)**.
        
    4.  Copy the following JSON configuration into the text box:
        
        JSON
        
            [  {    "AllowedHeaders": [],    "AllowedMethods": ["PUT"],    "AllowedOrigins": ["https://*.databricks.com"],    "ExposeHeaders": [],    "MaxAgeSeconds": 1800  }]
        
    5.  Select **Save changes**.
        

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Create catalogs](https://docs.databricks.com/aws/en/catalogs/create-catalog)
*   [Create schemas](https://docs.databricks.com/aws/en/schemas/create-schema)
*   [Databricks tables](https://docs.databricks.com/aws/en/tables/)
*   [Manage Unity Catalog metastores](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-metastore)
*   [Learn more about Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/)
