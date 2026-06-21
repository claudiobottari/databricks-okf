---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cbde60853dd2d7a53389de654f45860c77cedcf58b6c0ce195f773b3f64e197f
  pageDirectory: concepts
  sources:
    - create-a-unity-catalog-metastore-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - managed-storage-in-unity-catalog
    - MSIUC
    - Managed Storage Locations in Unity Catalog
    - Managed storage (Unity Catalog)
    - Managed Storage
    - Specify a managed storage location in Unity Catalog
  citations:
    - file: create-a-unity-catalog-metastore-databricks-on-aws.md
title: Managed Storage in Unity Catalog
description: The S3 bucket storage location, configurable at metastore, catalog, or schema level, where Unity Catalog stores managed tables and managed volumes.
tags:
  - unity-catalog
  - storage
  - aws
timestamp: "2026-06-19T14:31:12.471Z"
---

# Managed Storage in Unity Catalog

**Managed Storage in Unity Catalog** refers to the cloud storage location (an S3 bucket on AWS) that is designated at the [Metastore](/concepts/metastore.md) level to store the data of managed tables and managed volumes. This storage location is used by Unity Catalog to persist the underlying data files for these securable objects, and it can be overridden at finer granularity (catalog or schema level). ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Overview

Every [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) may have an associated managed storage location – an S3 bucket in the customer’s own AWS account. When a [Metastore](/concepts/metastore.md) has managed storage configured, any managed tables or managed volumes created in that [Metastore](/concepts/metastore.md) (without an explicit overriding location) store their data in that bucket. This bucket is sometimes called “metastore-level root storage.” ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

Managed storage is an optional component of [Metastore](/concepts/metastore.md) creation. Whether you need it depends on your data architecture; for guidance, see the documentation on [specifying a managed storage location](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/managed-storage). ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Requirements and Best Practices

When setting up managed storage, the following constraints must be observed:

- Each [Metastore](/concepts/metastore.md) should use a **dedicated S3 bucket**. Avoid sharing the bucket across multiple metastores. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
- The bucket must reside in the **same AWS region** as the workspaces that will access the data. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
- The bucket name **must not contain dots** (`.`). Although AWS allows dots, Databricks recommends against them because they can cause SSL certificate validation failures with features like OpenSharing. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
- The bucket **cannot have an S3 access control list (ACL)** attached. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
- Optional: You may enable KMS encryption on the bucket. If you do, note the KMS key name for later configuration. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Configuration Steps

To configure managed storage for a [Metastore](/concepts/metastore.md), you perform the following actions in your AWS account and then in Databricks:

1. **Create an S3 bucket** in AWS that will serve as the metastore-level storage location. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
2. **Create an IAM role** that grants Unity Catalog access to that bucket. The role must have appropriate permissions and a trust policy that allows Databricks to assume it. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
3. In Databricks, create the [Metastore](/concepts/metastore.md) (or update an existing one) and supply the S3 bucket path and the IAM role ARN. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
4. Optionally, configure storage credentials for more granular access.

After creation, the [Metastore](/concepts/metastore.md) will use the specified bucket and role for managed table and volume storage unless overridden.

## Override at [Catalog and Schema](/concepts/catalog-and-schema.md) Level

The managed storage location set at the [Metastore](/concepts/metastore.md) level is the default. However, you can **override** it at the catalog level or even at the schema level. This allows different parts of the data hierarchy to use different S3 buckets while still being governed by the same [Metastore](/concepts/metastore.md). ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## CORS Configuration for Managed Volumes

If you enable managed storage and plan to use managed volumes, Databricks uses cross-origin resource sharing (CORS) to upload data to the S3 bucket. You must configure a CORS policy on the bucket in AWS. An example configuration is:

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

The `AllowedOrigins` pattern should match the Databricks deployment domain. This step is required to allow browser-based uploads from the Databricks workspace to the managed volume storage. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md)
- [Managed tables](/concepts/managed-tables-in-databricks.md)
- Managed volumes
- [External locations](/concepts/external-location.md)
- Storage credentials
- [Specify a managed storage location in Unity Catalog](/concepts/managed-storage-in-unity-catalog.md) (external link)

## Sources

- create-a-unity-catalog-metastore-databricks-on-aws.md

# Citations

1. [create-a-unity-catalog-metastore-databricks-on-aws.md](/references/create-a-unity-catalog-metastore-databricks-on-aws-f0a3d0e9.md)
