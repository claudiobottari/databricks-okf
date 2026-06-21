---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 005a9642497cb5ea8e6ae9ef76ac061c81e23105330ff583a2f864846a9225a3
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - instance-profile-databricks-on-aws
    - IP(OA
    - Instance Profiles in Databricks
    - Instance profiles in Databricks
    - AWS Instance Profile Setup
    - Add an instance profile to Databricks
    - Add the instance profile to Databricks
    - Instance Profiles
    - Instance profiles
    - instance profile (IAM role)
    - instance profiles
    - instance-profile-for-databricks-model-serving
    - IPFDMS
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Instance Profile (Databricks on AWS)
description: An AWS IAM instance profile attached to a Databricks model serving endpoint to grant access to AWS resources such as S3, allowing models to read/write data during inference.
tags:
  - aws
  - iam
  - model-serving
  - security
timestamp: "2026-06-19T21:57:33.944Z"
---

# Instance Profile (Databricks on AWS)

An **instance profile** in Databricks on AWS is an IAM role that grants an AWS identity (such as an EC2 instance or a serverless compute environment) permission to access AWS resources. When attached to a [Model Serving](/concepts/model-serving.md) endpoint, the instance profile allows the endpoint to read or write to AWS resources — such as S3 buckets, DynamoDB tables, or other services — that the role’s policy allows. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Requirements

Before using an instance profile with a model serving endpoint, you must:

1. **Create an instance profile** in AWS and configure its IAM role with the necessary permissions. See the AWS documentation on creating instance profiles for S3 access. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
2. **Add the instance profile to Databricks** through the workspace settings. Instructions are available in the Databricks documentation for S3 instance profiles. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
3. **Ensure a trust relationship for serverless compute** is configured on the IAM role. Model serving endpoints run on serverless compute, so the role must trust the serverless compute service. Without this trust relationship, Databricks returns the error: “IAM role does not have the required trust relationship.” For setup instructions, refer to the serverless SQL warehouse data access configuration guide. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

If you already have an instance profile configured for serverless SQL, you may need to update its access policies so that the models have the appropriate permissions to the resources they need. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Adding an Instance Profile to a Model Serving Endpoint

### During Endpoint Creation

When creating a model serving endpoint, you can attach an instance profile by using either the Serving UI or the REST API.

- **UI:** In the **Advanced configurations** section of the endpoint creation form, select the desired instance profile. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **API:** Set the `instance_profile_arn` field inside the `served_entities` configuration of the `POST /api/2.0/serving-endpoints` request. For example: ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

```json
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

The endpoint creator’s permission to use the instance profile is validated at creation time. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Updating an Existing Endpoint

To add or change the instance profile on an already-running model serving endpoint, use the `PUT /api/2.0/serving-endpoints/{name}/config` API and include the `instance_profile_arn` field in the `served_entities` array: ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

```json
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

The following limitations apply when using an instance profile with a model serving endpoint:

- **STS temporary credentials** are used to authenticate data access. These credentials cannot bypass any network restrictions (e.g., VPC endpoints, firewall rules). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- If you **edit the instance profile IAM role** from the Databricks workspace Settings, endpoints that are already running with that instance profile continue to use the *old* IAM role until the endpoint is updated (e.g., by redeploying or modifying the configuration). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- If you **delete the instance profile** from the Databricks Settings while it is still in use by running endpoints, those endpoints are not impacted. They will continue to serve with the previously attached profile until a new configuration is applied. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

For general model serving endpoint limitations, see Model Serving Limits and Regions.

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – Deploy and manage models on Databricks.
- Serverless Compute – The compute environment used by model serving endpoints.
- AWS Instance Profiles – AWS IAM roles used for granting permissions to resources.
- [Store environment variables for model serving](/concepts/secrets-based-environment-variables-in-model-serving.md) – Alternative method for configuring resource access.
- Feature Store Lookup – Use the same instance profile to authenticate feature lookups.

## Additional Resources

- Look up features from the [Feature Store](/concepts/feature-store.md) using the same instance profile attached to the serving endpoint. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- Configure access to resources from model serving endpoints by using environment variables or instance profiles. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
