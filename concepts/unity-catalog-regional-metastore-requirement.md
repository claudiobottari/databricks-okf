---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d8f7991050490d7a534cf397410e6d9073bc8902ff2b7c7eb251c5d9c08690e1
  pageDirectory: concepts
  sources:
    - create-a-unity-catalog-metastore-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-regional-metastore-requirement
    - UCRMR
  citations:
    - file: create-a-unity-catalog-metastore-databricks-on-aws.md
title: Unity Catalog Regional Metastore Requirement
description: The architectural requirement that each AWS region must have its own Unity Catalog metastore, with workspaces linked only to metastores in their same region.
tags:
  - unity-catalog
  - architecture
  - aws
  - databricks
timestamp: "2026-06-18T14:49:11.207Z"
---

# Unity Catalog Regional [Metastore](/concepts/metastore.md) Requirement

**Unity Catalog Regional [Metastore](/concepts/metastore.md) Requirement** refers to the architectural constraint in [Unity Catalog](/concepts/unity-catalog.md) that a separate [Metastore](/concepts/metastore.md) must be created for each AWS region where an organization operates. A [Metastore](/concepts/metastore.md) is the top-level container for data in Unity Catalog, registering metadata about securable objects such as tables, volumes, external locations, and shares, along with the permissions that govern access to them.^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Overview

Each Databricks region requires its own Unity Catalog [Metastore](/concepts/metastore.md). This means organizations must create a dedicated [Metastore](/concepts/metastore.md) for every region in which they operate. These regional metastores can then be linked to any number of workspaces within that same region.^[create-a-unity-catalog-metastore-databricks-on-aws.md]

The [Metastore](/concepts/metastore.md) must be deployed in the same region as the workspaces that will access the data. When creating a [Metastore](/concepts/metastore.md), the specified region must match the region of the storage bucket used for metastore-level storage.^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## How Regional Metastores Work

Each linked workspace has the same view of the data in the [Metastore](/concepts/metastore.md), and data access control can be managed across workspaces. Data in other metastores in different regions can be accessed using [OpenSharing](/concepts/opensharing.md) (Delta Sharing).^[create-a-unity-catalog-metastore-databricks-on-aws.md]

The [Metastore](/concepts/metastore.md) exposes a three-level namespace (`catalog.schema.table`) by which data can be organized. To work with Unity Catalog, users must be on a workspace that is attached to a [Metastore](/concepts/metastore.md) in their region.^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Automatic [Metastore](/concepts/metastore.md) Setup

For workspaces that were enabled for Unity Catalog automatically (starting November 8, 2023), the manual creation instructions on this page are unnecessary. Databricks began automatically enabling new workspaces for Unity Catalog with a gradual rollout across accounts. Users should only follow manual [Metastore](/concepts/metastore.md) creation steps if their workspace does not already have a [Metastore](/concepts/metastore.md) in its region.^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Prerequisites for Creating a [Metastore](/concepts/metastore.md)

Before creating a [Metastore](/concepts/metastore.md), users must meet the following requirements:^[create-a-unity-catalog-metastore-databricks-on-aws.md]

- Be a Databricks account admin
- Have a Databricks account on the Premium plan or above
- Have the ability to create S3 buckets, IAM roles, IAM policies, and cross-account trust relationships in the AWS account (if setting up metastore-level root storage)

## Steps to Create a Regional [Metastore](/concepts/metastore.md)

Creating a [Metastore](/concepts/metastore.md) involves the following steps:^[create-a-unity-catalog-metastore-databricks-on-aws.md]

1. **(Optional)** Create an S3 bucket for metastore-level storage of managed tables and volumes in the AWS account
2. **(Optional)** Create an IAM role to access the storage location
3. In Databricks, create the [Metastore](/concepts/metastore.md), attaching the storage location, and assign workspaces to the [Metastore](/concepts/metastore.md)

### S3 Bucket Requirements

If using metastore-level storage:^[create-a-unity-catalog-metastore-databricks-on-aws.md]

- Use a dedicated S3 bucket for each [Metastore](/concepts/metastore.md) if you have more than one
- Locate the bucket in the same region as the workspaces
- Do not use dot notation (e.g., `incorrect.bucket.name.notation`) in S3 bucket names
- The bucket cannot have an S3 access control list attached

## Best Practices

After creating a [Metastore](/concepts/metastore.md), Databricks recommends:^[create-a-unity-catalog-metastore-databricks-on-aws.md]

- Transferring the [Metastore](/concepts/metastore.md) admin role to a group rather than an individual user
- Enabling cross-origin resource sharing (CORS) on the S3 bucket to allow Databricks management of uploads to managed volumes

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that metastores are part of
- [Metastore](/concepts/metastore.md) — The top-level container for Unity Catalog metadata
- Unity Catalog Managed Storage — Options for metastore-level, catalog-level, and schema-level storage
- [OpenSharing (Delta Sharing)](/concepts/opensharing-delta-sharing.md) — Mechanism for accessing data across different metastores and regions
- Workspace Attachment — The process of linking workspaces to a regional [Metastore](/concepts/metastore.md)

## Sources

- create-a-unity-catalog-metastore-databricks-on-aws.md

# Citations

1. [create-a-unity-catalog-metastore-databricks-on-aws.md](/references/create-a-unity-catalog-metastore-databricks-on-aws-f0a3d0e9.md)
