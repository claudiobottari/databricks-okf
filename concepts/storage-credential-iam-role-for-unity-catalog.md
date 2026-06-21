---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5a369aaca5055969fb49be546e2dd21c954ea24d5b5cb2cf49b98685611ee112
  pageDirectory: concepts
  sources:
    - create-a-unity-catalog-metastore-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - storage-credential-iam-role-for-unity-catalog
    - SC(RFUC
    - Storage Credential
    - Storage credential
    - Storage credentials (legacy)
    - storage credential
  citations:
    - file: create-a-unity-catalog-metastore-databricks-on-aws.md
title: Storage Credential (IAM Role) for Unity Catalog
description: An IAM role created in AWS that grants Unity Catalog access to an S3 bucket used for managed storage, requiring cross-account trust relationship policies.
tags:
  - unity-catalog
  - iam
  - aws
  - security
timestamp: "2026-06-19T09:30:36.624Z"
---

# Storage Credential (IAM Role) for Unity Catalog

A **Storage Credential** is a Unity Catalog object that encapsulates an IAM role (on AWS) used to authenticate and authorize access to cloud storage locations (e.g., S3 buckets). When you create a [Metastore](/concepts/metastore.md), catalog, or external location, the associated storage credential provides the IAM role that Unity Catalog assumes to read and write data in those buckets.

## How Storage Credentials Work

Storage credentials are created by linking an IAM role to Unity Catalog. The role must have an appropriate trust relationship policy that allows the Databricks account to assume it, and the role’s IAM policy must grant the necessary S3 bucket permissions (e.g., `s3:GetObject`, `s3:PutObject`). ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

When you set up metastore-level storage (the root S3 bucket for managed tables and volumes), you create a dedicated IAM role as a storage credential. This role is then associated with the [Metastore](/concepts/metastore.md) at creation time, although it can be attached later as well. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Creating a Storage Credential

The steps to create a storage credential for a [Metastore](/concepts/metastore.md) are described in the Databricks documentation under [Create a storage credential that accesses an AWS S3 bucket](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/s3/s3-external-location-manual#create-storage-credential). These steps include:

1. **Create an IAM role** in your AWS account with the necessary S3 permissions. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
2. **Give Databricks the IAM role details** by providing the role ARN to the account. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
3. **Update the IAM role trust relationship policy** to allow the Databricks account to assume the role. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

If you enable KMS encryption on the S3 bucket, note the name of the KMS encryption key, as it may be required during configuration. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Usage Scenarios

Storage credentials are used in multiple Unity Catalog contexts:

- **Metastore root storage**: The IAM role associated with the [Metastore](/concepts/metastore.md) is used to access the S3 bucket where managed tables and volumes are stored. This is optional—you can specify managed storage at the catalog or schema level instead. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
- **External locations**: When you register an external S3 bucket (for external tables or volumes), you must provide a storage credential that has access to that bucket.
- **Catalog-level managed storage**: You can override the [Metastore](/concepts/metastore.md) root by specifying a different storage credential for a catalog.

## Best Practices

- Use a dedicated IAM role per storage credential to follow the principle of least privilege. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
- Avoid using dot notation in S3 bucket names (`incorrect.bucket.name`); Databricks does not support dot-separated bucket names due to SSL certificate validation issues. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
- Locate the S3 bucket in the same AWS region as the [Metastore](/concepts/metastore.md) and the workspaces that will query the data. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) – The top-level container that uses storage credentials for its root storage.
- [External location](/concepts/external-location.md) – An object that references a cloud storage path and its associated storage credential.
- [Managed Storage](/concepts/managed-storage-in-unity-catalog.md) – Storage for managed tables and volumes, which can be set at [Metastore](/concepts/metastore.md), catalog, or schema level.
- IAM Role for Databricks – General guidance on IAM roles in AWS for Databricks.

## Sources

- create-a-unity-catalog-metastore-databricks-on-aws.md

# Citations

1. [create-a-unity-catalog-metastore-databricks-on-aws.md](/references/create-a-unity-catalog-metastore-databricks-on-aws-f0a3d0e9.md)
