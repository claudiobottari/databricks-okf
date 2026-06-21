---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a99759842b8d9721fa3c34355ea37deb404c16bf134565ae6b7f956c9fbc63be
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-compute-trust-relationship-for-iam-roles
    - SCTRFIR
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Serverless Compute Trust Relationship for IAM Roles
description: IAM roles used with Databricks model serving endpoints must have a trust relationship configured for serverless compute, or endpoints will fail with a specific error.
tags:
  - aws
  - iam
  - serverless
  - databricks
timestamp: "2026-06-19T17:26:32.991Z"
---

```yaml
---
title: Serverless Compute Trust Relationship for IAM Roles
summary: An IAM role trust policy that allows Databricks serverless compute (e.g., model serving endpoints, serverless SQL warehouses) to assume the role for accessing AWS resources.
sources:
  - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:11:43.889Z"
updatedAt: "2026-06-18T08:11:43.889Z"
tags:
  - iam
  - serverless
  - aws
  - model-serving
  - security
aliases:
  - serverless-compute-trust-relationship-for-iam-roles
  - SCTRIR
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Serverless Compute Trust Relationship for IAM Roles

The **Serverless Compute Trust Relationship for IAM Roles** is an AWS IAM trust policy that must be attached to an instance profile's IAM role when the role is used with Databricks serverless compute. This policy grants the Databricks serverless compute service permission to assume the IAM role, allowing workloads running on serverless infrastructure to access AWS resources (such as S3 buckets) that the role permits. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Overview

When you attach an instance profile to a [[model serving endpoint]] or a serverless SQL warehouse, the endpoint’s serverless compute needs to assume the IAM role associated with that instance profile. Without the correct trust relationship, the assume‑role call fails and the endpoint cannot access the protected resources. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

The trust relationship is configured in the IAM role’s trust policy. The source document does not provide the exact policy structure; instead, it directs users to the setup guide for serverless SQL warehouses for instructions. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Error Scenario

If the IAM role does not have the required trust relationship, you will see the following error when creating or updating a model serving endpoint that uses the instance profile:

```
IAM role does not have the required trust relationship.
```

^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Configuration

To resolve the error, follow the instructions in Confirm or set up an AWS instance profile to use with your serverless SQL warehouses. Although that guide is written for serverless SQL, the same trust policy is required for model serving endpoints because both use the same serverless compute plane. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

The general steps are:

1. Locate the IAM role associated with your instance profile in the AWS IAM console.
2. Edit the trust relationship and add a policy that allows the Databricks serverless compute principal to assume the role.
3. Save the trust policy and retry the endpoint creation or update.

For the exact trust policy document, refer to the serverless SQL warehouse setup guide linked above. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Important Notes

- Serverless compute uses AWS STS temporary security credentials (temporary credentials) to authenticate data access. The trust relationship enables STS to generate credentials for the role. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- If you edit the instance profile’s IAM role after it has been attached to a running endpoint, the endpoint continues to use the original role until the endpoint is updated. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- Deleting an instance profile from the Databricks UI does not affect endpoints that are already running with that profile. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Related Concepts

- Instance Profile
- [[Model Serving Endpoint]]
- Serverless SQL Warehouse
- IAM Role
- AWS STS
- Serverless Compute

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
```

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
