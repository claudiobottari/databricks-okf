---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 858ebf4568c63b332037567b1d6a8c605993679d1d1beeaaebfe5768c04837a2
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sts-temporary-credentials-for-model-data-access
    - STCFMDA
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: STS Temporary Credentials for Model Data Access
description: AWS STS temporary security credentials are used to authenticate data access from model serving endpoints, but they cannot bypass network restrictions.
tags:
  - aws
  - sts
  - security
  - data-access
timestamp: "2026-06-19T08:51:37.967Z"
---

# STS Temporary Credentials for Model Data Access

**STS Temporary Credentials for Model Data Access** refers to the authentication mechanism used by [model serving endpoints](/concepts/model-serving-endpoint.md) to access AWS resources. When an instance profile is attached to a model serving endpoint, Databricks uses AWS Security Token Service (STS) temporary security credentials to authenticate data access to AWS resources such as S3 buckets, DynamoDB tables, or other services permissible by the instance profile's IAM role. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Overview

When you attach an instance profile to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md), the endpoint uses STS temporary credentials to authenticate requests to AWS resources. This approach provides secure, time-limited access without requiring long-term AWS credentials to be stored or managed manually. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## How It Works

1. **Instance Profile Attachment**: An IAM instance profile is attached to the model serving endpoint configuration, either during endpoint creation or by updating an existing endpoint. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
2. **STS Credential Generation**: Databricks generates temporary security credentials via AWS STS on behalf of the endpoint.
3. **Authenticated Access**: The endpoint uses these temporary credentials to access AWS resources defined in the instance profile's IAM role policies.

## Limitations and Considerations

### Network Restrictions

STS temporary security credentials **cannot bypass any network restriction**. The credentials authenticate data access but do not override network-level controls such as VPC configurations, security groups, or network ACLs. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### IAM Role Changes

If you edit the instance profile's IAM role from the Databricks **Settings** UI, endpoints that are already running with that instance profile continue to use the **old IAM role** until the endpoint is updated. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Instance Profile Deletion

If you delete an instance profile from the Databricks **Settings** UI and that profile is actively used by running endpoints, the running endpoint is **not impacted**. The deletion only prevents the profile from being used for new endpoint configurations or updates. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Requirements

To use STS temporary credentials with model serving endpoints:

- You must create an instance profile in AWS with the appropriate IAM role and policies.
- You must add the instance profile to Databricks.
- The instance profile's IAM role must have a trust relationship configured for [serverless compute](/concepts/serverless-gpu-compute.md). If you see the error "IAM role does not have the required trust relationship," see the documentation on setting up AWS instance profiles for serverless SQL warehouses. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Use Cases

### Feature Store Access

You can use the same instance profile to look up features from the [Feature Store](/concepts/feature-store.md) when serving models, ensuring consistent authentication for both model inference and feature retrieval. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Resource Access Configuration

For detailed guidance on configuring access to AWS resources from model serving endpoints, see Configure access to resources from model serving endpoints. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) – The compute infrastructure that serves ML models for inference.
- [Instance Profiles](/concepts/instance-profile-databricks-on-aws.md) – IAM roles that grant permissions to AWS resources.
- AWS Security Token Service (STS) – The AWS service that issues temporary security credentials.
- Serverless Compute – The compute layer that model serving endpoints run on.
- Feature Store Authentication – Authenticating feature store lookups from serving endpoints.

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
