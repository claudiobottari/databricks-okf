---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 596f6a888954d26ed376ebb98dd40a625a799e66d67fd17d1100e6bf59bd76be
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - instance-profile-attachment-to-model-serving-endpoints
    - IPATMSE
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Instance Profile Attachment to Model Serving Endpoints
description: The process and configuration of attaching an AWS IAM instance profile to a Databricks model serving endpoint to grant access to AWS resources.
tags:
  - aws
  - model-serving
  - security
  - iam
timestamp: "2026-06-19T13:53:11.649Z"
---

# Instance Profile Attachment to Model Serving Endpoints

**Instance Profile Attachment to Model Serving Endpoints** refers to the ability to associate an AWS IAM instance profile with a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) on Databricks. This allows the endpoint to access AWS resources (such as S3 buckets, DynamoDB tables, or other services) that the instance profile’s IAM role permits. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Overview

By attaching an instance profile to a model serving endpoint, any code running on that endpoint can make authenticated calls to AWS resources. The endpoint uses [STS temporary security credentials](/concepts/sts-temporary-credentials-for-data-access.md) derived from the instance profile role, though these credentials cannot bypass network restrictions. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Requirements

Before attaching an instance profile, you must:

1. **Create an instance profile** in AWS and configure its IAM role with the necessary permissions. See the [AWS instance profile documentation](https://docs.databricks.com/aws/en/archive/storage/tutorial-s3-instance-profile).
2. **Add the instance profile to Databricks** via the workspace settings. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
3. **Configure a trust relationship** between the instance profile’s IAM role and Databricks [serverless compute](/concepts/serverless-gpu-compute.md). If this trust relationship is missing, you will see the error: “IAM role does not have the required trust relationship.” For setup instructions, refer to [Confirm or set up an AWS instance profile to use with your serverless SQL warehouses](https://docs.databricks.com/aws/en/admin/sql/data-access-configuration#aws-instance-profile-setup). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

If you already have an instance profile configured for serverless SQL warehouses, ensure its access policies are updated to grant the correct permissions to your models. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Adding an Instance Profile During Endpoint Creation

When you [create a model serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints), you can attach an instance profile as part of the configuration.

- **In the Serving UI:** Navigate to the **Advanced configurations** section when creating the endpoint and select or enter the instance profile ARN.
- **Via the API:** Use the `instance_profile_arn` field in the `served_entities` block of the `POST /api/2.0/serving-endpoints` request.

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

The endpoint creator’s permission to the instance profile is validated at creation time. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Updating an Existing Endpoint

You can update an already running model serving endpoint to use an instance profile by calling `PUT /api/2.0/serving-endpoints/{name}/config` and including the `instance_profile_arn` in the request body.

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

- **STS credentials cannot bypass network restrictions.** The temporary security credentials obtained from the instance profile are subject to any VPC or network-level controls. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **Editing the instance profile IAM role** in Databricks Settings does not affect running endpoints until the endpoint is updated or restarted. Endpoints continue to use the old IAM role. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **Deleting an instance profile** from Databricks Settings does not impact endpoints that are already running with that profile. They continue to operate unchanged. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

For general model serving endpoint limitations, see the [Model Serving limits and regions](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits) documentation. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Additional Resources

- Use the attached instance profile to look up features from the Feature Store by following the [authentication guide](https://docs.databricks.com/aws/en/machine-learning/feature-store/fs-authentication).
- Configure access to resources from model serving endpoints using environment variables to complement instance profile permissions. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Related Concepts

- Instance Profile – AWS IAM roles attached to EC2 instances or serverless compute.
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) – The serving infrastructure that hosts ML models.
- Serverless Compute – The underlying compute layer for model serving.
- IAM Role – AWS identity with permission policies.
- [Feature Store](/concepts/feature-store.md) – Databricks feature store accessed via the same instance profile.
- AWS STS – Service that issues temporary credentials for the instance profile.

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
