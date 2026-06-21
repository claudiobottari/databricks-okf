---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 727c7238315e76eed6bfb6bab5709255ac607bb1fc370c412d875ccc4e6aa4f7
  pageDirectory: concepts
  sources:
    - create-a-unity-catalog-metastore-databricks-on-aws.md
    - manage-unity-catalog-metastores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - metastore-level-managed-storage
    - MMS
  citations:
    - file: create-a-unity-catalog-metastore-databricks-on-aws.md
    - file: manage-unity-catalog-metastores-databricks-on-aws.md
title: Metastore-level managed storage
description: An optional S3 bucket used as the default storage location for managed tables and managed volumes in a Unity Catalog metastore, which can be overridden at catalog and schema levels.
tags:
  - unity-catalog
  - storage
  - aws-s3
  - managed-tables
timestamp: "2026-06-19T17:57:43.184Z"
---

# Metastore-Level Managed Storage

**Metastore-level managed storage** is an optional S3 bucket location that can be configured at the [Metastore](/concepts/metastore.md) level in Unity Catalog to serve as the default root storage location for managed tables and managed volumes. When enabled, this storage location provides a centralized default for all managed data in the [Metastore](/concepts/metastore.md), and it can be overridden at the [Catalog and Schema](/concepts/catalog-and-schema.md) levels. ^[create-a-unity-catalog-metastore-databricks-on-aws.md, manage-unity-catalog-metastores-databricks-on-aws.md]

## Overview

Metastore-level managed storage represents the top-level storage option in Unity Catalog's hierarchical storage model. Each [Metastore](/concepts/metastore.md) can have one S3 bucket that acts as the default storage location for managed objects created within that [Metastore](/concepts/metastore.md), sometimes referred to as the [Metastore](/concepts/metastore.md) storage root. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

This storage level is optional and is not automatically included for metastores that were created automatically (for example, when Databricks enables Unity Catalog for a workspace automatically after November 8, 2023). Administrators may choose to add metastore-level storage if they prefer a data isolation model that stores data centrally for multiple workspaces. Metastore-level storage is also required for Databricks partners who use personal staging locations. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

## When to Use Metastore-Level Storage

Metastore-level managed storage is appropriate when:

- You want a centralized storage location for all managed data across multiple workspaces attached to the same [Metastore](/concepts/metastore.md).
- You are a Databricks partner using personal staging locations (where it is required).
- You want to set a default storage location that can be inherited by catalogs and schemas unless they specify their own.

You may prefer not to use metastore-level storage if you want to force each catalog to have a dedicated storage location, enforcing stricter data isolation at the catalog level. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

## How It Works

When metastore-level storage is configured, the S3 bucket path is registered with the [Metastore](/concepts/metastore.md). When a user creates a catalog without specifying a storage location, the catalog inherits the metastore-level storage location. Similarly, schemas inherit from their parent catalog, and managed tables inherit from their parent schema. This inheritance chain can be overridden at any level by specifying a dedicated storage location. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Adding Metastore-Level Storage

To add metastore-level storage to an existing [Metastore](/concepts/metastore.md), an account admin performs three steps:

1. **Create an S3 bucket** in the same AWS region as the [Metastore](/concepts/metastore.md). The bucket must not use dot notation in its name, and it cannot have an S3 access control list attached. If KMS encryption is used, the KMS key name must be noted. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

2. **Create an external location** in Unity Catalog that represents the bucket. The AWS Quickstart method in Catalog Explorer automates the creation of the IAM role, storage credential, and external location. The user must also grant themselves the `CREATE MANAGED STORAGE` privilege on the created external location. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

3. **Set the bucket path on the metastore** via the account console's Catalog tab. Navigate to the [Metastore](/concepts/metastore.md)'s configuration, click **Set** next to **S3 bucket path**, and enter the bucket path. This path cannot be modified once set, though it can be removed and replaced. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

### Requirements

- An existing workspace must be attached to the Unity Catalog [Metastore](/concepts/metastore.md).
- To create an external location, the user needs `CREATE EXTERNAL LOCATION` and `CREATE STORAGE CREDENTIAL` privileges.
- To add the storage location to the [Metastore](/concepts/metastore.md) definition, the user must be an account admin.
- AWS permissions must allow creating S3 buckets, IAM roles, IAM policies, and cross-account trust relationships. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

## Removing Metastore-Level Storage

When metastore-level storage is removed, the following happens:

- Existing catalogs that have no storage root specified are given the [Metastore](/concepts/metastore.md) storage root's cloud storage location as their catalog-level managed storage location (the [Metastore](/concepts/metastore.md) storage root is "pushed down" to these catalogs). Data access continues without interruption.
- If no external location securable was defined for the [Metastore](/concepts/metastore.md) storage root, a new external location and associated storage credential are created automatically, named `prior_metastore_root_location` by default.
- Every time a user creates a new catalog, they must provide a dedicated storage location that is registered in Unity Catalog as an external location. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

If OpenSharing is used to share notebooks and the [Metastore](/concepts/metastore.md) root was used as shared notebook storage, the notebook must be removed from the share and re-added using a dedicated storage location before the [Metastore](/concepts/metastore.md) root can be removed. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

To remove the [Metastore](/concepts/metastore.md) storage root, an account admin navigates to the [Metastore](/concepts/metastore.md)'s configuration in the account console, clicks **Remove** next to the S3 bucket path, and confirms the action. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md)
- Managed Storage Locations in Unity Catalog
- [External Locations](/concepts/external-location.md)
- Catalog-Level Managed Storage
- Schema-Level Managed Storage
- [Managed Tables](/concepts/managed-tables-in-databricks.md)
- Managed Volumes

## Sources

- create-a-unity-catalog-metastore-databricks-on-aws.md
- manage-unity-catalog-metastores-databricks-on-aws.md

# Citations

1. [create-a-unity-catalog-metastore-databricks-on-aws.md](/references/create-a-unity-catalog-metastore-databricks-on-aws-f0a3d0e9.md)
2. [manage-unity-catalog-metastores-databricks-on-aws.md](/references/manage-unity-catalog-metastores-databricks-on-aws-6a5c164f.md)
