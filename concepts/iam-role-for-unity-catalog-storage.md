---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 44e61686a08cc227c6317c965f1f675ed6db586086fb0313a2dea7aa66c7c519
  pageDirectory: concepts
  sources:
    - create-a-unity-catalog-metastore-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iam-role-for-unity-catalog-storage
    - IRFUCS
  citations:
    - file: create-a-unity-catalog-metastore-databricks-on-aws.md
title: IAM role for Unity Catalog storage
description: An AWS IAM role that grants Unity Catalog access to an S3 bucket used for metastore-level managed storage, requiring a cross-account trust relationship with Databricks.
tags:
  - unity-catalog
  - aws-iam
  - security
  - storage-credential
timestamp: "2026-06-19T17:57:14.989Z"
---

# IAM Role for Unity Catalog Storage

An **IAM role for Unity Catalog storage** is an AWS IAM role that grants Unity Catalog access to an S3 bucket used as the metastore-level storage location for managed tables and managed volumes. This role is required when you create a Unity Catalog [Metastore](/concepts/metastore.md) with a custom managed storage location.^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Purpose

When you create a Unity Catalog [Metastore](/concepts/metastore.md), you can optionally specify an S3 bucket for metastore-level storage of managed tables and volumes. To access this bucket, Unity Catalog needs an IAM role with the appropriate permissions. The IAM role is configured as a [storage credential](/concepts/storage-credential-iam-role-for-unity-catalog.md) that Unity Catalog assumes when reading from or writing to the S3 bucket.^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Requirements

Before creating the IAM role, ensure you meet the following requirements:

- You must have the ability to create IAM roles, IAM policies, and cross-account trust relationships in your AWS account.^[create-a-unity-catalog-metastore-databricks-on-aws.md]
- The S3 bucket used for [Metastore](/concepts/metastore.md) storage cannot have an S3 access control list attached to it.^[create-a-unity-catalog-metastore-databricks-on-aws.md]
- If you enable KMS encryption on the S3 bucket, you must note the name of the KMS encryption key for use in the IAM role policy.^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Creating the IAM Role

To create the IAM role for Unity Catalog storage, follow the instructions for creating a storage credential that accesses an AWS S3 bucket. This involves three steps:^[create-a-unity-catalog-metastore-databricks-on-aws.md]

1. **Create an IAM role** in your AWS account with a policy that grants access to the S3 bucket.
2. **Give Databricks the IAM role details** by providing the role ARN when creating the [Metastore](/concepts/metastore.md).
3. **Update the IAM role trust relationship policy** to allow Databricks to assume the role.

## Relationship to [Metastore](/concepts/metastore.md) Creation

The IAM role is specified when you create the [Metastore](/concepts/metastore.md) in the Databricks account console. During creation, you provide the S3 bucket path and the IAM role name for the bucket and role you created. The [Metastore](/concepts/metastore.md) then uses this role to access the storage location for managed tables and volumes.^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## CORS Configuration

After creating the [Metastore](/concepts/metastore.md) and linking it to workspaces, you must enable Databricks management of uploads to managed volumes by configuring cross-origin resource sharing (CORS) on the S3 bucket. The CORS configuration allows Databricks to upload data to managed volumes in Unity Catalog.^[create-a-unity-catalog-metastore-databricks-on-aws.md]

The required CORS configuration is:

```json
[
  {
    "AllowedHeaders": [],
    "AllowedMethods": ["PUT"],
    "AllowedOrigins": ["https://*.databricks.com"],
    "ExposeHeaders": [],
    "MaxAgeSeconds": 1800
  }
]
```

^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Best Practices

- Use a dedicated S3 bucket for each [Metastore](/concepts/metastore.md) if you have more than one.^[create-a-unity-catalog-metastore-databricks-on-aws.md]
- Locate the bucket in the same region as the workspaces that will access the data.^[create-a-unity-catalog-metastore-databricks-on-aws.md]
- Do not use dot notation (for example, `incorrect.bucket.name.notation`) in S3 bucket names, as Databricks does not support S3 buckets with dot notation. Dot notation can cause compatibility issues with features like OpenSharing due to SSL certificate validation failures.^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) — The top-level container for data in Unity Catalog
- [Storage Credential](/concepts/storage-credential-iam-role-for-unity-catalog.md) — The credential that grants Unity Catalog access to cloud storage
- [Managed storage location](/concepts/managed-storage-location.md) — Storage for managed tables and volumes in Unity Catalog
- S3 External Location — External storage locations for accessing data outside Unity Catalog

## Sources

- create-a-unity-catalog-metastore-databricks-on-aws.md

# Citations

1. [create-a-unity-catalog-metastore-databricks-on-aws.md](/references/create-a-unity-catalog-metastore-databricks-on-aws-f0a3d0e9.md)
