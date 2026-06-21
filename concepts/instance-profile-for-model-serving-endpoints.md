---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c41476c2cbb9b3a85ec6e66d991f18bd9b5fec837db35580306db28b4c528f34
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - instance-profile-for-model-serving-endpoints
    - IPFMSE
    - Add an Instance Profile to a Model Serving Endpoint
    - Add an instance profile to a model serving endpoint
    - Instance Profile for Model Serving
    - adding an instance profile to a model serving endpoint
    - instance profile on a served model
    - instance-profile-attachment-to-model-serving-endpoints
    - IPATMSE
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Instance Profile for Model Serving Endpoints
description: Attaching AWS IAM instance profiles to Databricks model serving endpoints to grant access to AWS resources such as S3 buckets and feature stores.
tags:
  - aws
  - model-serving
  - iam
  - databricks
timestamp: "2026-06-19T17:26:43.440Z"
---

# Instance Profile for Model Serving Endpoints

**Instance Profile for Model Serving Endpoints** allows you to attach an AWS instance profile to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md). This grants the endpoint access to AWS resources—such as S3 buckets, DynamoDB tables, or other services—that the instance profile’s IAM role permits. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Requirements

Before attaching an instance profile to a model serving endpoint, you must:

- Create an instance profile in AWS.
- [Add an instance profile to Databricks](/concepts/instance-profile-databricks-on-aws.md) via the workspace settings. If the instance profile is already configured for serverless SQL, update its access policies so that your models have the appropriate permissions to your resources. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

Model serving endpoints run on [serverless compute](/concepts/serverless-gpu-compute.md). The instance profile's IAM role must have a trust relationship configured for serverless compute. If you encounter the error "IAM role does not have the required trust relationship," see the setup instructions for configuring an AWS instance profile for serverless SQL warehouses. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Adding an Instance Profile During Endpoint Creation

When you create a model serving endpoint, you can attach an instance profile as part of the endpoint configuration. The endpoint creator's permission to use the instance profile is validated at creation time. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Using the Serving UI

In the **Create model serving endpoint** form, expand **Advanced configurations** and specify the instance profile. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Using the REST API

Set the `instance_profile_arn` field in the `served_entities` array when calling `POST /api/2.0/serving-endpoints`. For example:

```bash
POST /api/2.0/serving-endpoints
{
  "name": "feed-ads",
  "config": {
    "served_entities": [{
      "entity_name": "ads1",
      "entity_version": "1",
      "workload_size": "Small",
      "scale_to_zero_enabled": true,
      "instance_profile_arn": "arn:aws:iam::<aws-account-id>:instance-profile/<instance-profile-name-1>"
    }]
  }
}
```

^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Updating an Existing Endpoint with an Instance Profile

You can update the configuration of an existing model serving endpoint to add or change an instance profile using the `PUT /api/2.0/serving-endpoints/{name}/config` endpoint. The `instance_profile_arn` field in the `served_entities` array specifies the new profile. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

```bash
PUT /api/2.0/serving-endpoints/{name}/config
{
  "served_entities": [{
    "entity_name": "ads1",
    "entity_version": "2",
    "workload_size": "Small",
    "scale_to_zero_enabled": true,
    "instance_profile_arn": "arn:aws:iam::<aws-account-id>:instance-profile/<instance-profile-name-2>"
  }]
}
```

## Limitations

The following limitations apply when using instance profiles with model serving endpoints:

- [STS temporary security credentials](/concepts/sts-temporary-credentials-for-data-access.md) are used to authenticate data access. They cannot bypass any network restriction (for example, VPC restrictions). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- If you edit the instance profile's IAM role from the **Settings** page of the Databricks UI, endpoints that are already running with that profile continue to use the old IAM role until the endpoint is updated (for example, by redeploying the endpoint configuration). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- If you delete an instance profile from the **Settings** page, running endpoints that use that profile are not impacted. The endpoint continues to operate with the credentials it already holds. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

For general endpoint limitations, see Model Serving limits and regions. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Additional Resources

- Use the same instance profile to look up features from a feature store during model serving. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- Configure access to resources from model serving endpoints using environment variables instead of instance profiles. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
