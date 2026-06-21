---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1e92d7e2038f5924a91f44233e223deef4515e18832e800a1657bed01eef85c8
  pageDirectory: concepts
  sources:
    - create-a-unity-catalog-metastore-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cors-configuration-for-managed-volumes
    - CCFMV
    - cors-configuration-for-unity-catalog-managed-volumes
    - CCFUCMV
  citations:
    - file: create-a-unity-catalog-metastore-databricks-on-aws.md
title: CORS Configuration for Managed Volumes
description: Cross-origin resource sharing (CORS) configuration required on the S3 bucket to enable Databricks to upload data to managed volumes in Unity Catalog.
tags:
  - unity-catalog
  - aws-s3
  - volumes
  - configuration
timestamp: "2026-06-19T14:31:32.161Z"
---

# CORS Configuration for Managed Volumes

**CORS Configuration for Managed Volumes** refers to the cross-origin resource sharing (CORS) settings that must be applied to the S3 bucket used as the metastore-level storage location in [Unity Catalog](/concepts/unity-catalog.md). Databricks uses CORS to enable browser-based uploads to managed volumes in Unity Catalog. Without the correct CORS configuration, uploads from the Databricks web application to the underlying S3 bucket will fail. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Why CORS Is Needed

When a user uploads data to a managed volume through the Databricks UI (for example, using Catalog Explorer or the file upload feature), the request originates from a Databricks domain (e.g., `*.databricks.com`) and targets the S3 bucket that stores the volume's data. Because the bucket and the web application have different origins, the browser enforces the same-origin policy. CORS headers tell the browser that the cross-origin request is allowed. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Prerequisites

- You must have an S3 bucket configured as the metastore-level managed storage location. This bucket is created during [Metastore](/concepts/metastore.md) setup. See [Create a Unity Catalog metastore](/concepts/unity-catalog-metastore.md).
- You must have permission to edit the CORS configuration on that S3 bucket in your AWS account. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Configuration Steps

Configure CORS on the S3 bucket using the AWS Management Console, AWS CLI, or infrastructure-as-code tools. The required CORS rules are as follows:

1. Open the AWS Management Console and navigate to the S3 bucket you created for metastore-level storage.
2. Select the **Permissions** tab.
3. Under **Cross-origin resource sharing (CORS)**, click **Edit**.
4. Paste the following JSON configuration:

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

5. Save the changes. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

### Explanation of the CORS Rule

| Field | Value | Purpose |
|-------|-------|---------|
| `AllowedHeaders` | `[]` | No custom headers are required; the default headers suffice. |
| `AllowedMethods` | `["PUT"]` | The only HTTP method needed for uploads is `PUT`. |
| `AllowedOrigins` | `["https://*.databricks.com"]` | Allows requests from any Databricks workspace subdomain. This wildcard covers all workspaces in the account. |
| `ExposeHeaders` | `[]` | No additional headers need to be exposed to the client. |
| `MaxAgeSeconds` | `1800` | Caches the preflight response for 30 minutes to reduce latency on repeated uploads. |

^[create-a-unity-catalog-metastore-databricks-on-aws.md]

If you are using AWS CloudFormation, note that CloudFormation uses different property names (e.g., `AllowedMethods`, `AllowedOrigins`). Refer to the [AWS CloudFormation documentation for S3 CORS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-cors.html) for the correct syntax. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Verification

After applying the CORS configuration, test an upload to a managed volume from the Databricks UI:

- Open Catalog Explorer.
- Navigate to a managed volume.
- Use the **Upload** button to select and upload a file.

If the upload succeeds without a CORS error in the browser console, the configuration is correct.

## Important Considerations

- The CORS configuration applies **only to the S3 bucket that serves as metastore-level storage**. If you override managed storage at the catalog or schema level with a different bucket, that bucket also needs the same CORS rules. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
- The `AllowedOrigins` entry uses a wildcard for the Databricks domain. For stricter security, you could restrict this to a specific workspace URL, but that would break uploads from other workspaces linked to the same [Metastore](/concepts/metastore.md).
- CORS configuration is required **only for browser-based uploads** (or any client-side request from a Databricks domain). Direct SDK or CLI uploads to S3 do not need CORS.

## Related Concepts

- Managed Volumes — Unity Catalog volumes that store data in the metastore-managed location
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that provides managed storage and volumes
- [Metastore-level managed storage](/concepts/metastore-level-managed-storage.md) — The default S3 bucket used for all managed tables and volumes in the [Metastore](/concepts/metastore.md)
- Catalog-level managed storage — An optional override for a specific catalog
- S3 bucket CORS documentation — AWS official guide for configuring CORS on S3

## Sources

- create-a-unity-catalog-metastore-databricks-on-aws.md

# Citations

1. [create-a-unity-catalog-metastore-databricks-on-aws.md](/references/create-a-unity-catalog-metastore-databricks-on-aws-f0a3d0e9.md)
