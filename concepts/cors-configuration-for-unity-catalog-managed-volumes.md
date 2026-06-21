---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 368535ef8402bfad9dd98fa7c622e4432973c7d6b1f46961eca468a2d346abca
  pageDirectory: concepts
  sources:
    - create-a-unity-catalog-metastore-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cors-configuration-for-unity-catalog-managed-volumes
    - CCFUCMV
  citations:
    - file: create-a-unity-catalog-metastore-databricks-on-aws.md
title: CORS configuration for Unity Catalog managed volumes
description: Cross-origin resource sharing (CORS) settings that must be applied to the S3 bucket to enable Databricks to upload data to managed volumes in Unity Catalog.
tags:
  - unity-catalog
  - aws-s3
  - cors
  - managed-volumes
timestamp: "2026-06-19T17:57:45.015Z"
---

---
title: CORS Configuration for Unity Catalog Managed Volumes
summary: Cross-origin resource sharing (CORS) settings required on the S3 bucket to enable Databricks to upload data to managed volumes in Unity Catalog.
sources:
  - create-a-unity-catalog-metastore-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:49:20.539Z"
updatedAt: "2026-06-19T09:30:49.463Z"
tags:
  - unity-catalog
  - aws-s3
  - cors
  - managed-volumes
aliases:
  - cors-configuration-for-unity-catalog-managed-volumes
  - CCFUCMV
confidence: 1
provenanceState: extracted
inferredParagraphs: 1
---

# CORS Configuration for Unity Catalog Managed Volumes

**CORS Configuration for Unity Catalog Managed Volumes** refers to the cross-origin resource sharing (CORS) settings required on the S3 bucket used as the managed storage location for a [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md). Without this configuration, Databricks cannot upload data to Managed Volumes in Unity Catalog. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Overview

Databricks uses cross-origin resource sharing (CORS) to upload data to managed volumes in Unity Catalog. When you create a Unity Catalog [Metastore](/concepts/metastore.md) with an S3 bucket as the managed storage location, you must configure CORS rules on that bucket to allow Databricks to perform upload operations. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Required CORS Configuration

To enable uploads to managed volumes, you must add the following CORS configuration to your S3 bucket: ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

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

Key elements of this configuration: ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

- **AllowedMethods**: Only `PUT` is required, as uploads use HTTP PUT requests.
- **AllowedOrigins**: Must include `https://*.databricks.com` to allow requests from any Databricks workspace.
- **AllowedHeaders**: Empty array, as no custom headers are needed for the upload operation.
- **ExposeHeaders**: Empty array, as no response headers need to be exposed to the client.
- **MaxAgeSeconds**: Set to 1800 seconds (30 minutes) to cache preflight responses.

## How to Apply the Configuration

If you are not using an AWS CloudFormation template, apply the CORS configuration manually through the AWS console: ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

1. In the AWS console, select your S3 bucket from the buckets list.
2. Select the **Permissions** tab.
3. Under **Cross-origin resource sharing (CORS)**, select **Edit**.
4. Copy the JSON configuration into the text box.
5. Select **Save changes**.

### CloudFormation Note

If you are using an AWS CloudFormation template, be aware that CloudFormation uses some property names that differ from those listed in the manual instructions. Refer to the [AWS CloudFormation CORS configuration documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-cors.html) for the correct property names. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Prerequisites

Before applying the CORS configuration, ensure the S3 bucket meets these requirements: ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

- The bucket must not have an S3 access control list attached to it.
- Bucket names must not use dot notation (for example, `incorrect.bucket.name.notation`), as this can cause compatibility issues with features like OpenSharing due to SSL certificate validation failures.

## Related Concepts

- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) — The top-level container for data in Unity Catalog that requires this CORS configuration.
- Managed Volumes — The Unity Catalog feature that enables file uploads, requiring CORS support.
- Create a Unity Catalog Metastore — The setup process that includes this CORS configuration step.
- S3 Bucket Configuration for Unity Catalog — Additional bucket settings needed for Unity Catalog, such as IAM role setup.
- [Managed storage location](/concepts/managed-storage-location.md) — The storage location that the CORS rules protect.

## Sources

- create-a-unity-catalog-metastore-databricks-on-aws.md

# Citations

1. [create-a-unity-catalog-metastore-databricks-on-aws.md](/references/create-a-unity-catalog-metastore-databricks-on-aws-f0a3d0e9.md)
