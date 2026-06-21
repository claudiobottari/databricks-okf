---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7fde8fb9235ea4ab8ec23b14c36007435be413bdcc71febd8298cf650c93d98d
  pageDirectory: concepts
  sources:
    - create-a-unity-catalog-metastore-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - regional-metastore-deployment
    - RMD
  citations:
    - file: create-a-unity-catalog-metastore-databricks-on-aws.md
title: Regional metastore deployment
description: The requirement that each Databricks region must have its own Unity Catalog metastore, which can be linked to multiple workspaces within that same region.
tags:
  - unity-catalog
  - deployment
  - multi-region
  - architecture
timestamp: "2026-06-19T17:57:27.327Z"
---

---
title: Regional [Metastore](/concepts/metastore.md) Deployment
summary: The requirement that each Databricks region must have its own Unity Catalog [Metastore](/concepts/metastore.md), and workspaces can only be linked to a [Metastore](/concepts/metastore.md) in the same region.
sources:
  - create-a-unity-catalog-metastore-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:15:57.659Z"
updatedAt: "2026-06-18T11:15:57.659Z"
tags:
  - unity-catalog
  - deployment
  - aws
aliases:
  - regional-metastore-deployment
  - RMD
confidence: 1
provenanceState: extracted
inferredParagraphs: 1
---

# Regional [Metastore](/concepts/metastore.md) Deployment

**Regional [Metastore](/concepts/metastore.md) Deployment** refers to the practice of creating a distinct [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) for each AWS region in which an organization operates. Because each Databricks region requires its own Unity Catalog [Metastore](/concepts/metastore.md), organizations must deploy one [Metastore](/concepts/metastore.md) per region and link it to the workspaces in that region. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Why Regional Deployment Is Necessary

A [Metastore](/concepts/metastore.md) is the top-level container for data in Unity Catalog. It registers metadata about securable objects (such as tables, volumes, external locations, and shares) and the permissions that govern access to them. Each [Metastore](/concepts/metastore.md) exposes a three-level namespace (`catalog.schema.table`). To work with Unity Catalog, users must be on a workspace that is attached to a [Metastore](/concepts/metastore.md) in their region. Therefore, if your organization operates in multiple AWS regions, you must create a separate [Metastore](/concepts/metastore.md) for each region. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Prerequisites

- You must be a Databricks account admin.
- Your Databricks account must be on the Premium plan or above.
- If you set up metastore-level root storage, you must have the ability to create S3 buckets, IAM roles, IAM policies, and cross-account trust relationships in your AWS account.

^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Deployment Process

### 1. Create an S3 Bucket (Optional)

If you decide to use metastore-level storage for managed tables and volumes, create an S3 bucket in your own AWS account. This bucket will serve as the root storage location for the [Metastore](/concepts/metastore.md), though it can be overridden at the [Catalog and Schema](/concepts/catalog-and-schema.md) levels. Requirements include:

- Use a dedicated S3 bucket for each [Metastore](/concepts/metastore.md).
- Locate the bucket in the same region as the workspaces that will access the data.
- Avoid dot notation in bucket names (e.g., `incorrect.bucket.name.notation`) because Databricks does not support S3 buckets with dots.
- The bucket cannot have an S3 access control list (ACL) attached.
- If you enable KMS encryption, note the name of the KMS key.

^[create-a-unity-catalog-metastore-databricks-on-aws.md]

### 2. Create an IAM Role (Optional, Required Only If You Created a Bucket)

Create an IAM role that Unity Catalog will use to access the S3 bucket. Follow the standard instructions for creating a storage credential for an AWS S3 bucket, which include:

- Create an IAM role.
- Give Databricks the IAM role details.
- Update the IAM role trust relationship policy.

^[create-a-unity-catalog-metastore-databricks-on-aws.md]

### 3. Create the [Metastore](/concepts/metastore.md)

1. Log in to the Databricks [account console](https://accounts.cloud.databricks.com/).
2. Click **Catalog**.
3. Click **Create metastore**.
4. Enter a name for the [Metastore](/concepts/metastore.md).
5. Select the region where the [Metastore](/concepts/metastore.md) will be deployed — this must match the region of your S3 bucket and the workspaces that will use the [Metastore](/concepts/metastore.md).
6. Optionally, enter the S3 bucket path (omitting `s3://`) and IAM role name.
7. Click **Create**.
8. When prompted, select the workspaces to link to the [Metastore](/concepts/metastore.md).
9. Transfer the [Metastore](/concepts/metastore.md) admin role to a group (recommended). The user who creates the [Metastore](/concepts/metastore.md) is its owner; reassigning ownership to a group simplifies administration.
10. Enable CORS on the S3 bucket to allow Databricks to upload data to managed volumes. In the AWS console, add the following CORS configuration:

```json
[  {    "AllowedHeaders": [],    "AllowedMethods": ["PUT"],    "AllowedOrigins": ["https://*.databricks.com"],    "ExposeHeaders": [],    "MaxAgeSeconds": 1800  }]
```

^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Automatic Enablement for New Workspaces

For workspaces enabled for Unity Catalog automatically after November 8, 2023, the instructions above are unnecessary. Databricks began to enable new workspaces for Unity Catalog automatically, with a gradual rollout across accounts. You only need to follow the manual deployment steps if your workspace does not already have a [Metastore](/concepts/metastore.md) in its region. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Best Practices

- Use a dedicated S3 bucket for each [Metastore](/concepts/metastore.md) to avoid cross-region contamination.
- Assign the [Metastore](/concepts/metastore.md) admin role to a group rather than an individual user.
- Configure CORS on the S3 bucket to support managed volume uploads.
- After deployment, create catalogs, schemas, and tables to begin organizing data.

^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Metastore](/concepts/metastore.md)
- [Specify a managed storage location in Unity Catalog](/concepts/managed-storage-location.md)
- Workspace
- [Storage Credential](/concepts/storage-credential-iam-role-for-unity-catalog.md)
- [OpenSharing](/concepts/opensharing.md)

## Sources

- create-a-unity-catalog-metastore-databricks-on-aws.md

# Citations

1. [create-a-unity-catalog-metastore-databricks-on-aws.md](/references/create-a-unity-catalog-metastore-databricks-on-aws-f0a3d0e9.md)
