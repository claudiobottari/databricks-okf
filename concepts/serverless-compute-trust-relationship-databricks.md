---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aa26b02464dabd005fb5e03471ca70f5206c3fb1c1b42056bca5bb571287b4ea
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-compute-trust-relationship-databricks
    - SCTR(
    - Serverless Compute Trust Relationship
    - Serverless Compute Trust Policy
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Serverless Compute Trust Relationship (Databricks)
description: A required trust policy configuration on an AWS IAM role that allows Databricks serverless compute to assume the role when running model serving endpoints.
tags:
  - aws
  - iam
  - serverless
  - security
timestamp: "2026-06-19T21:57:38.921Z"
---

# Serverless Compute Trust Relationship (Databricks)

**Serverless Compute Trust Relationship** refers to the requirement that an AWS instance profile’s IAM role must include a trust policy that allows Databricks serverless compute to assume the role. This relationship is required when an instance profile is attached to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md), which runs on serverless compute infrastructure. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Error When Trust Relationship is Missing

If the instance profile’s IAM role does not have the required trust relationship configured for serverless compute, the following error occurs when attempting to use the instance profile with a model serving endpoint:

> **IAM role does not have the required trust relationship**

^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Setup Instructions

To resolve the error, the trust relationship must be added to the IAM role. The Databricks documentation for Serverless SQL warehouse setup provides the necessary steps. See [Confirm or set up an AWS instance profile to use with your serverless SQL warehouses](https://docs.databricks.com/aws/en/admin/sql/data-access-configuration#aws-instance-profile-setup). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Related Concepts

- Instance Profile – An AWS IAM role that can be attached to Databricks compute resources.
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) – The endpoint that hosts machine learning models on serverless compute.
- [IAM Role Trust Policy](/concepts/iam-role-trust-for-unity-catalog.md) – The AWS policy that defines which principals can assume the role.
- Serverless SQL Warehouse – Another Databricks workload that uses serverless compute and may require a similar trust relationship.

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
