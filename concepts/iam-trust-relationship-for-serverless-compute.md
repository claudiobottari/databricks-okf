---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5873e8ff740eedd97319f5b28f3cb854fd4d99ac719070cc73cd7acb41350576
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iam-trust-relationship-for-serverless-compute
    - ITRFSC
    - IAM Role Trust Policy for Serverless
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: IAM Trust Relationship for Serverless Compute
description: Requirement that the instance profile's IAM role must have a trust relationship configured for Databricks serverless compute, or the endpoint creation fails.
tags:
  - aws
  - iam
  - serverless
  - model-serving
timestamp: "2026-06-19T13:53:05.431Z"
---

Here is the wiki page for "IAM Trust Relationship for Serverless Compute", written solely based on the provided source material.

---

## IAM Trust Relationship for Serverless Compute

**IAM Trust Relationship for Serverless Compute** refers to the required configuration of an AWS Identity and Access Management (IAM) role that allows Databricks [serverless compute](/concepts/serverless-gpu-compute.md) to assume that role. This trust relationship is a prerequisite for using an instance profile with Databricks model serving endpoints and other serverless workloads.

### Purpose

When you attach an instance profile to a model serving endpoint, the endpoint uses the IAM role associated with that profile to access AWS resources such as S3 buckets or DynamoDB tables. For the serverless compute that powers the endpoint to successfully assume this IAM role, the role must have a trust relationship explicitly configured for Databricks serverless compute. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Error Condition

If the IAM role does not have the required trust relationship, Databricks returns the following error:

```
IAM role does not have the required trust relationship
```

^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Setup Instructions

To resolve this error and configure the trust relationship, see the documentation on confirming or setting up an AWS instance profile for use with serverless SQL warehouses. The setup process for model serving endpoints follows the same trust relationship requirements as serverless SQL warehouses. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Related Concepts

- [Add an instance profile to a model serving endpoint](/concepts/instance-profile-for-model-serving-endpoints.md) — The workflow that triggers the trust relationship validation
- [Instance profile](/concepts/model-serving-instance-profile.md) — The AWS construct that contains the IAM role and its permissions
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) — The serverless endpoint that uses the instance profile for resource access
- Serverless SQL Warehouses — Another Databricks workload type that shares the same trust relationship requirements
- [STS temporary security credentials](/concepts/sts-temporary-credentials-for-data-access.md) — The mechanism used by model serving endpoints to authenticate data access

### Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
