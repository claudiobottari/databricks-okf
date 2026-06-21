---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ae8764b7b22d6e95516d8415841ae238df7bbcb08a337f9686b320974b2f4a3f
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - programmatic-endpoint-configuration-with-instance-profile-arn
    - PECWIPA
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Programmatic Endpoint Configuration with Instance Profile ARN
description: Using the REST API to attach an instance profile to a model serving endpoint by specifying the instance_profile_arn field in the served_entities configuration during endpoint creation or update.
tags:
  - databricks
  - api
  - model-serving
  - configuration
timestamp: "2026-06-18T14:18:26.143Z"
---

# Programmatic Endpoint Configuration with Instance Profile ARN

**Programmatic Endpoint Configuration with Instance Profile ARN** refers to the process of attaching an AWS instance profile to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) during endpoint creation or by updating an existing endpoint configuration using the Databricks REST API. This configuration allows the model serving endpoint to access AWS resources that are permissible under the specified instance profile's IAM role.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Overview

When you configure a model serving endpoint programmatically, you can include the `instance_profile_arn` field in the endpoint configuration to specify which AWS instance profile the endpoint should use for accessing external resources. The instance profile's IAM role must have a trust relationship configured for serverless compute, as model serving endpoints run on serverless compute.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Adding an Instance Profile During Endpoint Creation

You can add an instance profile to a model serving endpoint at creation time by including the `instance_profile_arn` field in the `served_entities` configuration. The endpoint creator's permission to the instance profile is validated at endpoint creation time.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Programmatic Example

The following example shows how to create an endpoint with an instance profile using the Databricks REST API:^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

```bash
POST /api/2.0/serving-endpoints
{
  "name": "feed-ads",
  "config": {
    "served_entities": [{
      "entity_name": "ads",
      "entity_version": "1",
      "workload_size": "Small",
      "scale_to_zero_enabled": true,
      "instance_profile_arn": "arn:aws:iam::<aws-account-id>:instance-profile/<instance-profile-name-1>"
    }]
  }
}
```

## Updating an Existing Endpoint with an Instance Profile

You can update an existing model serving endpoint configuration with the `instance_profile_arn` field using the `PUT` endpoint:^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

```bash
PUT /api/2.0/serving-endpoints/{name}/config
{
  "served_entities": [{
    "entity_name": "ads",
    "entity_version": "2",
    "workload_size": "Small",
    "scale_to_zero_enabled": true,
    "instance_profile_arn": "arn:aws:iam::<aws-account-id>:instance-profile/<instance-profile-name-2>"
  }]
}
```

## Requirements

Before configuring an instance profile on a model serving endpoint, you must:^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

- Create an instance profile in AWS.
- [Add an instance profile to Databricks](/concepts/instance-profile-databricks-on-aws.md).
- Ensure the instance profile's IAM role has a trust relationship configured for serverless compute. If you see the error "IAM role does not have the required trust relationship," follow the setup instructions for serverless SQL warehouse instance profile configuration.

## Limitations

The following limitations apply when using instance profiles with model serving endpoints:^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

- [STS temporary security credentials](/concepts/sts-temporary-credentials-for-data-access.md) are used to authenticate data access and cannot bypass network restrictions.
- If you edit the instance profile IAM role from the Databricks UI Settings, endpoints running with the instance profile continue to use the old IAM role until the endpoint is updated.
- If you delete an instance profile from the Databricks UI Settings that is used in running endpoints, the running endpoint is not impacted.

For general model serving endpoint limitations, see Model Serving limits and regions.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Related Concepts

- Instance Profile — AWS IAM roles that grant permissions to EC2 instances and other AWS services
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) — The serving infrastructure that hosts machine learning models for inference
- Serverless Compute — The compute model used by Databricks for model serving
- AWS Resources Access — Using instance profiles to access S3, DynamoDB, and other AWS services
- Feature Store Authentication — Looking up features using the same instance profile

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
