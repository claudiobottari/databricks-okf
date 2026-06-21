---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 66d0fc220698b9332e2b005d719abf04853f93ed02f471c9d8b4c34396d5fb12
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serving-ui-advanced-configuration-for-instance-profiles
    - SUACFIP
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Serving UI Advanced Configuration for Instance Profiles
description: Instance profiles can be added to model serving endpoints through the Databricks Serving UI under Advanced configurations, with the endpoint creator's permission validated at creation time.
tags:
  - databricks
  - ui
  - model-serving
  - configuration
timestamp: "2026-06-18T14:18:29.097Z"
---

# Serving UI Advanced Configuration for Instance Profiles

**Serving UI Advanced Configuration for Instance Profiles** refers to the process of attaching an AWS Instance Profile to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) using the Databricks Serving UI. This configuration allows model serving endpoints to access AWS resources — such as S3 buckets, DynamoDB tables, or other AWS services — that are permissible by the attached instance profile's IAM role. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Overview

Instance profiles provide a secure way to grant model serving endpoints access to AWS resources without embedding long-term credentials in your code or configuration. When you attach an instance profile to a serving endpoint, the endpoint uses AWS STS temporary security credentials to authenticate data access. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Adding an Instance Profile During Endpoint Creation

When you create a model serving endpoint, you can add an instance profile through the Serving UI's **Advanced configurations** section. The endpoint creator's permission to the instance profile is validated at endpoint creation time. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

To add an instance profile via the UI:

1. Navigate to the **Serving** UI in your Databricks workspace.
2. Begin creating a new model serving endpoint.
3. In the configuration form, locate **Advanced configurations**.
4. Specify the instance profile you want to attach.

For programmatic workflows, use the `instance_profile_arn` field in the endpoint creation API:

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

You can update an existing model serving endpoint to add or change its instance profile using the API:

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

^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Requirements

Before attaching an instance profile to a serving endpoint, ensure the following prerequisites are met: ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

- **Create an instance profile** in AWS with the appropriate IAM role and policies.
- **Add the instance profile to Databricks** through the workspace settings.
  - If you have an instance profile already configured for Serverless SQL, update its access policies so that your models have the correct permissions for your resources.
- **Configure trust relationship for serverless compute.** Model serving endpoints run on serverless compute. The instance profile's IAM role must have a trust relationship configured for serverless compute. If you encounter the error "IAM role does not have the required trust relationship," follow the setup instructions for AWS instance profile setup for serverless SQL warehouses.

## Limitations

The following limitations apply when using instance profiles with model serving endpoints: ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

- **STS temporary security credentials** are used to authenticate data access. These credentials cannot bypass any network restrictions.
- **Editing the instance profile IAM role** from the Databricks UI **Settings** does not affect running endpoints. Endpoints continue to use the old IAM role until the endpoint is updated.
- **Deleting an instance profile** from the Databricks UI **Settings** does not impact running endpoints that are currently using that profile.

For general model serving endpoint limitations, see Model Serving limits and regions.

## Additional Resources

- Use the same instance profile attached to a serving endpoint to look up features from the [Feature Store](/concepts/feature-store.md).
- See Configure access to resources from model serving endpoints for alternative methods of granting resource access.

## Related Concepts

- [Model Serving Endpoint](/concepts/model-serving-endpoint.md)
- Instance Profile
- AWS STS
- Serverless SQL
- [Feature Store](/concepts/feature-store.md)
- Model Serving limits and regions

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
