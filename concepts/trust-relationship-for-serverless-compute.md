---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c1d06de8124e352702a19d589fbe435abe64bf0cdfde87742b85cd74e16a425
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trust-relationship-for-serverless-compute
    - TRFSC
    - requirements for serverless compute
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Trust Relationship for Serverless Compute
description: The IAM role associated with an instance profile must have a trust relationship configured for Databricks serverless compute to avoid errors when attaching the profile to a serving endpoint.
tags:
  - databricks
  - aws
  - iam
  - serverless
timestamp: "2026-06-18T14:18:22.287Z"
---

## Trust Relationship for Serverless Compute

A **trust relationship** in the context of AWS IAM is a policy statement that defines which principals (such as services or accounts) are allowed to assume a given IAM role. For Databricks serverless compute, the IAM role attached to an instance profile must include a trust relationship that permits the serverless compute service to assume that role. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Purpose

When you attach an instance profile to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md), the endpoint runs on [serverless compute](/concepts/serverless-gpu-compute.md). The serverless compute infrastructure needs to be able to assume the IAM role associated with the instance profile so that it can access the AWS resources (e.g., S3 buckets, DynamoDB tables) that the role’s policies allow. Without the correct trust relationship, the role cannot be assumed, and the endpoint will fail to function. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Error Message

If the trust relationship is missing or incorrectly configured, the system returns the following error when you try to create or update a serving endpoint that uses the instance profile:

```
IAM role does not have the required trust relationship
```

^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Configuration

To configure the trust relationship for serverless compute, you must modify the IAM role’s trust policy to include the serverless compute service as a trusted entity. The same trust relationship is used for serverless SQL warehouses.

Databricks provides detailed setup instructions in the article [Confirm or set up an AWS instance profile to use with your serverless SQL warehouses](https://docs.databricks.com/aws/en/admin/sql/data-access-configuration#aws-instance-profile-setup). Follow those steps to ensure the role’s trust policy allows assumption by the serverless compute service. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Related Concepts

- [Instance profile](/concepts/model-serving-instance-profile.md) – The AWS IAM role container that is attached to the serving endpoint.
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) – The endpoint that uses the instance profile for resource access.
- [Serverless compute](/concepts/serverless-gpu-compute.md) – The compute infrastructure that runs the model serving endpoint.
- AWS IAM – The identity and access management service that governs role assumption.

### Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
