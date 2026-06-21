---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cf394f285b4a16b0a508d0234e219160eb86a231b7cc9bae878dd80b556f2852
  pageDirectory: concepts
  sources:
    - manage-unity-catalog-metastores-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-location-creation-via-aws-quickstart
    - ELCVAQ
  citations:
    - file: manage-unity-catalog-metastores-databricks-on-aws.md
title: External Location Creation via AWS Quickstart
description: A streamlined method using AWS CloudFormation Quickstart templates to create external locations and storage credentials in Unity Catalog for S3 bucket access, involving token-based authentication between Databricks and AWS.
tags:
  - unity-catalog
  - aws
  - external-location
  - cloudformation
timestamp: "2026-06-19T19:29:11.046Z"
---

# External Location Creation via AWS Quickstart

**External Location Creation via AWS Quickstart** is a recommended method within Unity Catalog for creating an [External location](/concepts/external-location.md) and its associated [storage credential](/concepts/storage-credential-iam-role-for-unity-catalog.md) in a single step, using an AWS CloudFormation template. This approach automates the IAM role and policy setup required to grant Databricks access to an S3 bucket, reducing manual configuration. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

## Overview

When you need to add an external location in Catalog Explorer, the **AWS Quickstart** option is presented alongside a **Manual** option. Quickstart configures the external location and creates a storage credential for you. If you choose the Manual option, you must create an IAM role that gives access to the S3 bucket and create the storage credential in Databricks yourself. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

## Prerequisites

- You must have the `CREATE EXTERNAL LOCATION` and `CREATE STORAGE CREDENTIAL` privileges. ^[manage-unity-catalog-metastores-databricks-on-aws.md]
- You must have permission to create S3 buckets, IAM roles, IAM policies, and cross-account trust relationships in your AWS account.
- You should have an S3 bucket already created in the same region as your [Metastore](/concepts/metastore.md) (see [Step 1: Create the storage location](#step-1-create-the-storage-location) below).

## Step-by-Step Procedure

1. Open a workspace that is attached to the [Metastore](/concepts/metastore.md) and open **Catalog Explorer** by clicking the **Catalog** icon.
2. Click the **+ Add** button and select **Add an external location**.
3. On the **Create a new external location** dialog, click **AWS Quickstart (Recommended)** and then click **Next**. ^[manage-unity-catalog-metastores-databricks-on-aws.md]
4. Enter the S3 bucket path in the **Bucket Name** field.
5. Click **Generate new token** to generate a personal access token that will be used to authenticate between Databricks and your AWS account. Copy this token. ^[manage-unity-catalog-metastores-databricks-on-aws.md]
6. Click **Launch in Quickstart**. This opens the AWS CloudFormation console with a **Quick create stack** form.
7. Paste the copied token into the **Databricks Account Credentials** field.
8. Accept the terms by checking the box **I acknowledge that AWS CloudFormation might create IAM resources with custom names**.
9. Click **Create stack**. It may take a few minutes for CloudFormation to complete and create the external location object in Databricks. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

## Verification

After the stack finishes, return to your Databricks workspace and go to the **External locations** pane in Catalog Explorer. Click the **Connect** icon (plug icon) and then **External locations**. You should see a new external location with a naming syntax `db_s3_external_databricks-S3-ingest-<id>`. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

## Post-Creation: Grant Privileges

If you are using this external location for metastore-level managed storage, you must grant yourself the `CREATE MANAGED STORAGE` privilege on the external location:

1. Click the external location name to open the details pane.
2. On the **Permissions** tab, click **Grant**.
3. Select yourself as the principal, choose the privilege `CREATE MANAGED STORAGE`, and click **Grant**. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

This privilege is required when you later set the S3 bucket path on the [Metastore](/concepts/metastore.md) as the managed storage root.

## Related Concepts

- [External location](/concepts/external-location.md) – A Unity Catalog securable that represents a cloud storage path.
- [Storage credential](/concepts/storage-credential-iam-role-for-unity-catalog.md) – The authentication secret used to access cloud storage.
- AWS CloudFormation – The infrastructure-as-code service used by Quickstart.
- [Catalog Explorer](/concepts/catalog-explorer.md) – The Databricks UI for managing Unity Catalog objects.
- [Metastore-level managed storage](/concepts/metastore-level-managed-storage.md) – Optional centralized storage for managed tables and volumes.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer for Databricks data and AI assets.

## Sources

- manage-unity-catalog-metastores-databricks-on-aws.md

# Citations

1. [manage-unity-catalog-metastores-databricks-on-aws.md](/references/manage-unity-catalog-metastores-databricks-on-aws-6a5c164f.md)
