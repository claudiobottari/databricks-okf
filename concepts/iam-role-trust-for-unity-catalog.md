---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f4be4e73008d83469e5fd76baf5f265dfda7d4657e71d011e943a496260a87e6
  pageDirectory: concepts
  sources:
    - create-a-unity-catalog-metastore-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iam-role-trust-for-unity-catalog
    - IRTFUC
    - IAM Role Trust Policy
  citations:
    - file: create-a-unity-catalog-metastore-databricks-on-aws.md
title: IAM Role Trust for Unity Catalog
description: The cross-account IAM role and trust relationship that must be established in AWS to allow Unity Catalog to access an S3 bucket for managed storage.
tags:
  - unity-catalog
  - aws-iam
  - security
  - databricks
timestamp: "2026-06-18T14:49:24.102Z"
---

---

title: IAM Role Trust for Unity Catalog
summary: Unity Catalog uses IAM roles to access S3 buckets for managed storage; a trust relationship policy must be configured to allow Databricks to assume the role.
sources:
  - create-a-unity-catalog-metastore-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:45:52.790Z"
updatedAt: "2026-06-18T14:45:52.790Z"
tags:
  - unity-catalog
  - aws
  - iam
  - security
aliases:
  - iam-role-trust-for-unity-catalog
  - IRTUC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# IAM Role Trust for Unity Catalog

**IAM Role Trust for Unity Catalog** refers to the AWS IAM trust relationship that allows Databricks to assume a role in your account to access an S3 bucket used for Unity Catalog managed storage. This trust policy is a required component of the [storage credential](/concepts/storage-credential-iam-role-for-unity-catalog.md) that grants Unity Catalog permission to read and write metastore-level stored data.

## Overview

When you create a Unity Catalog [Metastore](/concepts/metastore.md), you have the option to specify a storage location for managed tables and managed volumes. That location is an S3 bucket in your AWS account. To access the bucket, Unity Catalog needs an IAM role that it can assume. The role must have a trust relationship that enables the Databricks AWS account (specifically, the Unity Catalog service principal) to assume it. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

Configuring the trust relationship is part of the three-step process documented in Create a storage credential that accesses an AWS S3 bucket:

1. **Create an IAM role** that grants permissions to the S3 bucket.
2. **Give Databricks the IAM role details** (the role ARN and external ID).
3. **Update the IAM role trust relationship policy** to allow Databricks to assume the role. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Trust Policy Details

The IAM role’s trust policy must include a statement that allows the Databricks AWS account (the Unity Catalog service principal) to call `sts:AssumeRole`. The policy typically includes:
- The Databricks AWS account ID as the `Principal`.
- A condition that checks the `sts:ExternalId` to prevent confused deputy attacks.
- The `Action: sts:AssumeRole`.

The exact policy structure is shown in the referenced documentation. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## When Is This Required?

This trust configuration is required only if you choose to set up metastore-level storage (the S3 bucket and IAM role). If you skip metastore-level storage, Unity Catalog uses the default storage in the Databricks account. For guidance, see [Specify a managed storage location in Unity Catalog](/concepts/managed-storage-in-unity-catalog.md). ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) — The top-level container for metadata and permissions.
- [Managed storage (Unity Catalog)](/concepts/managed-storage-in-unity-catalog.md) — The S3 location where managed tables and volumes store data.
- [Storage credential](/concepts/storage-credential-iam-role-for-unity-catalog.md) — The object that holds the IAM role ARN and trust policy configuration.
- Cross-account IAM role trust — General AWS concept underpinning this configuration.
- Create a storage credential that accesses an AWS S3 bucket — The detailed setup guide.

## Sources

- create-a-unity-catalog-metastore-databricks-on-aws.md

# Citations

1. [create-a-unity-catalog-metastore-databricks-on-aws.md](/references/create-a-unity-catalog-metastore-databricks-on-aws-f0a3d0e9.md)
