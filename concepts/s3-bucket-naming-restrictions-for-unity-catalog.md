---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 96b9a5c982e6baa8b44b8a33fadda7468cb24f4f325f2cdb2aa285c04cd8a5ed
  pageDirectory: concepts
  sources:
    - create-a-unity-catalog-metastore-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - s3-bucket-naming-restrictions-for-unity-catalog
    - SBNRFUC
    - S3 bucket naming rules (AWS documentation)
  citations:
    - file: create-a-unity-catalog-metastore-databricks-on-aws.md
title: S3 Bucket Naming Restrictions for Unity Catalog
description: The requirement that S3 buckets used with Unity Catalog must not use dot notation in their names due to compatibility issues with features like OpenSharing.
tags:
  - unity-catalog
  - aws-s3
  - naming
  - databricks
timestamp: "2026-06-18T14:49:21.540Z"
---

# S3 Bucket Naming Restrictions for Unity Catalog

**S3 Bucket Naming Restrictions for Unity Catalog** refer to the specific naming rules that must be followed when creating S3 buckets used as metastore-level storage for Unity Catalog. While AWS itself imposes general bucket naming rules, Databricks enforces an additional restriction: **bucket names must not contain dots (`.`)**. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Dot Notation Restriction

Databricks does **not** support S3 bucket names that use dot notation (for example, `incorrect.bucket.name.notation`). This restriction applies to buckets used for Unity Catalog managed storage at the [Metastore](/concepts/metastore.md), catalog, or schema level. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

### Why Dots Are Prohibited

Although AWS allows dots in S3 bucket names, buckets with dots can cause compatibility issues with features such as [OpenSharing](/concepts/opensharing.md) (Delta Sharing) due to SSL certificate validation failures. When a bucket name contains dots, SSL certificates used for secure connections may not validate correctly against the bucket’s virtual-hosted-style URL, leading to connection errors. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

### Best Practice

Use hyphens (`-`) as separators in bucket names instead of dots. For example, prefer `my-org-unity-catalog-bucket` over `my.org.unity.catalog.bucket`. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Additional Bucket Requirements for Unity Catalog

While not strictly a naming restriction, the following requirements apply to S3 buckets used for metastore-level storage in Unity Catalog:

- The bucket must not have an S3 access control list (ACL) attached. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
- If you have more than one [Metastore](/concepts/metastore.md), use a dedicated bucket for each. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
- The bucket must reside in the same AWS region as the workspaces and the [Metastore](/concepts/metastore.md). ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Impact on Other Databricks Features

The dot-notation restriction is not limited to [Metastore](/concepts/metastore.md) storage. It applies to any S3 bucket used as an external location or managed storage location in Unity Catalog, including those configured at the catalog or schema level. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) – Top-level container for data metadata in Unity Catalog.
- [Managed Storage in Unity Catalog](/concepts/managed-storage-in-unity-catalog.md) – Storage locations for managed tables and volumes.
- [OpenSharing](/concepts/opensharing.md) (Delta Sharing) – Feature affected by SSL certificate issues when dots are present.
- [Create an external location](/concepts/external-location.md) – For connecting S3 buckets to Unity Catalog.
- [S3 bucket naming rules (AWS documentation)](/concepts/s3-bucket-naming-restrictions-for-unity-catalog.md) – General AWS constraints (e.g., unique across all accounts, 3–63 characters, lowercase, no underscores).

## Sources

- create-a-unity-catalog-metastore-databricks-on-aws.md

# Citations

1. [create-a-unity-catalog-metastore-databricks-on-aws.md](/references/create-a-unity-catalog-metastore-databricks-on-aws-f0a3d0e9.md)
