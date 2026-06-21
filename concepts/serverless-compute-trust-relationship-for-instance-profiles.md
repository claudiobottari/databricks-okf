---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2f37971ccf4cef87779cfc8b5bd77905aa18e9f9adf7777e5d11d72bf529c84b
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-compute-trust-relationship-for-instance-profiles
    - SCTRFIP
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Serverless Compute Trust Relationship for Instance Profiles
description: The requirement that an instance profile's IAM role must have a trust relationship configured for Databricks serverless compute; otherwise the endpoint creation fails with a specific error.
tags:
  - aws
  - iam
  - serverless
  - databricks
timestamp: "2026-06-18T10:39:01.055Z"
---

# Serverless Compute Trust Relationship for Instance Profiles

**Serverless Compute Trust Relationship for Instance Profiles** is an IAM requirement that must be configured on an AWS instance profile's IAM role before it can be used with Databricks serverless compute workloads, including model serving endpoints and serverless SQL warehouses. Without this trust relationship, Databricks serverless compute cannot assume the role, and operations that depend on the instance profile will fail.

## Overview

When you attach an instance profile to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md), the endpoint runs on serverless compute. For Databricks serverless compute to assume the IAM role associated with the instance profile, the role must have a trust relationship that explicitly grants permission to the serverless compute principal. If this trust relationship is missing, operations fail with the error: "IAM role does not have the required trust relationship." ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Configuration

### Confirm or Set Up the Trust Relationship

To use an instance profile with serverless compute, you must ensure the IAM role's trust policy includes the serverless compute service principal. For detailed setup instructions, see [Confirm or set up an AWS instance profile to use with your serverless SQL warehouses](https://docs.databricks.com/aws/en/admin/sql/data-access-configuration#aws-instance-profile-setup). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Existing Instance Profiles for Serverless SQL

If you already have an instance profile configured for serverless SQL warehouses, the trust relationship is likely already in place. However, you should still verify that the access policies on that instance profile grant the correct permissions for your model's resource access requirements, as model serving endpoints may need different permissions than serverless SQL warehouses. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Validation

The permission to use an instance profile is validated at endpoint creation time. When a user creates or updates a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) with an `instance_profile_arn`, Databricks checks that the user has permission to use the instance profile. If the IAM role lacks the required serverless compute trust relationship, the endpoint creation or update fails. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) — Endpoints that use instance profiles for AWS resource access
- Instance Profile — IAM roles that grant permissions to AWS resources
- Serverless SQL Warehouses — Another serverless workload that requires this trust relationship
- AWS IAM Trust Relationships — The IAM mechanism that grants cross-account or cross-service role assumption

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
