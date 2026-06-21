---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d144f2fd4fab9c8f94fd18aadd8829e525116aafdb8b695ad328336ef0ae3ac7
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sts-temporary-credentials-for-data-access
    - STCFDA
    - STS temporary security credentials
    - sts-temporary-credentials-for-model-serving
    - STCFMS
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: STS Temporary Credentials for Data Access
description: Model serving endpoints use AWS STS temporary security credentials to authenticate data access through the instance profile; these credentials cannot bypass network restrictions.
tags:
  - databricks
  - aws
  - sts
  - security
timestamp: "2026-06-18T14:18:31.347Z"
---

# STS Temporary Credentials for Data Access

**STS Temporary Credentials for Data Access** refers to the use of short-lived security tokens issued by the AWS Security Token Service (STS) to authenticate and authorize data access from [model serving endpoints](/concepts/model-serving-endpoint.md). These credentials are obtained through the IAM role associated with an instance profile attached to the endpoint, allowing the model to interact with AWS resources without embedding long-term access keys.

## Overview

When a model serving endpoint is configured with an instance profile, Databricks uses STS temporary security credentials to authenticate all data access made by that endpoint. The credentials inherit the permissions defined in the instance profile's IAM role, providing fine-grained control over which AWS resources the model can read or write. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Usage with Model Serving Endpoints

To enable STS-based data access, you attach an instance profile to a model serving endpoint at creation time or update an existing endpoint's configuration. The endpoint creator's permission to use the instance profile is validated at endpoint creation time. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

When the endpoint makes a request to an AWS resource (for example, reading data from Amazon S3 or invoking a Lambda function), AWS STS generates temporary credentials scoped to the permissions of the instance profile's IAM role. The model serving endpoint uses these credentials transparently. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Limitations

- STS temporary credentials **cannot bypass any network restriction**. If a VPC or firewall blocks access to the target resource, the temporary credentials will not override that control. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- If you edit the instance profile's IAM role from the Databricks UI **Settings**, endpoints that are already running with that instance profile continue to use the **old** IAM role until the endpoint configuration is updated. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- If you delete an instance profile from Databricks Settings while it is still in use by running endpoints, those endpoints are **not impacted**; they continue to operate with the previously associated IAM role. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Related Concepts

- Instance Profile — The configuration that links an IAM role to a model serving endpoint
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) — The serving infrastructure that uses STS credentials for data access
- IAM Role — The role whose permissions define what resources can be accessed
- Serverless Compute — The runtime environment that assumes the IAM role for STS token generation
- Data Access — The broader topic of securing data access from serving endpoints
- AWS Security Token Service — The AWS service that issues temporary security credentials

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
