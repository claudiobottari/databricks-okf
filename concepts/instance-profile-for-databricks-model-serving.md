---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6ee2ac2f20b843e673578cd19b25e3afcc1e318fe1996ecd3940c56356f4685b
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - instance-profile-for-databricks-model-serving
    - IPFDMS
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Instance Profile for Databricks Model Serving
description: An AWS IAM instance profile attached to a model serving endpoint to grant access to AWS resources (e.g., S3, feature stores) from a deployed model.
tags:
  - aws
  - model-serving
  - iam
  - databricks
timestamp: "2026-06-19T08:51:18.694Z"
---

# Instance Profile for Databricks Model Serving

**Instance Profile for Databricks Model Serving** refers to an AWS IAM instance profile that is attached to a model serving endpoint to grant the endpoint permissions to access AWS resources, such as S3 buckets, DynamoDB tables, or other services required by the model during inference.

## Overview

An instance profile is an AWS IAM role that can be associated with a Databricks model serving endpoint. When attached, the endpoint uses the permissions defined in the instance profile's IAM role to access any AWS resources that the model needs during serving. This enables models to read feature data, access lookup tables, or write results to AWS services. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Requirements

Before adding an instance profile to a model serving endpoint, the following prerequisites must be met:

1. **Create an instance profile** in AWS following the standard AWS IAM instance profile setup process. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
2. **Add the instance profile to Databricks** through the Databricks workspace settings. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
3. **Configure trust relationship for serverless compute** — Model serving endpoints run on serverless compute. The instance profile's IAM role must have a trust relationship configured for serverless compute. If you encounter the error "IAM role does not have the required trust relationship," follow the setup instructions for serverless SQL warehouses to configure the trust relationship. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
4. **Adjust access policies** — If you have an instance profile already configured for serverless SQL, ensure the access policies are updated so that your models have the appropriate access to your resources. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Adding an Instance Profile

### During Endpoint Creation

When creating a model serving endpoint, you can add an instance profile to the endpoint configuration. The endpoint creator's permission to use the instance profile is validated at creation time. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

**From the Serving UI:**
- Navigate to the **Serving** UI in Databricks.
- During endpoint creation, expand **Advanced configurations**.
- Select the desired instance profile from the available options.

**Using the API:**
Use the `instance_profile_arn` field in the endpoint creation request: ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

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

### Updating an Existing Endpoint

You can update an existing model serving endpoint to add or change its instance profile using the `instance_profile_arn` field in the endpoint configuration update API: ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

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

The following limitations apply when using instance profiles with model serving endpoints: ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

- **STS temporary credentials** — AWS Security Token Service (STS) temporary security credentials are used to authenticate data access. These credentials cannot bypass any network restrictions.
- **IAM role changes** — If you edit the instance profile's IAM role from the Databricks workspace **Settings**, endpoints currently running with that instance profile continue to use the old IAM role until the endpoint is updated.
- **Instance profile deletion** — If you delete an instance profile from the Databricks workspace **Settings** and that profile is in use by running endpoints, the running endpoints are not impacted.

For general model serving endpoint limitations, see Model Serving Limits and Regions.

## Use Cases

- **Feature lookup** — Models can look up features from the [Feature Store](/concepts/feature-store.md) using the same instance profile attached to the serving endpoint. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **Resource access** — Models can access S3 buckets, DynamoDB tables, or other AWS resources required for inference.
- **Cross-service integration** — Enable models to read from or write to other AWS services during prediction.

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The serving infrastructure that hosts models for real-time inference.
- AWS Instance Profiles — IAM roles that grant permissions to AWS resources.
- Feature Store Authentication — Using instance profiles for feature lookup during model serving.
- [Serverless Compute Trust Relationship](/concepts/serverless-compute-trust-relationship-databricks.md) — Required IAM trust policy for serverless workloads.
- Model Serving Limits and Regions — General limitations and regional availability for model serving.

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
