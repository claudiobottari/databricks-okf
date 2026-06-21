---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aa90729cea55b7b7e950ea6b624d137c503e5f187a3cb41138f9680163ebe844
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sts-temporary-credentials-for-model-serving
    - STCFMS
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: STS Temporary Credentials for Model Serving
description: AWS Security Token Service (STS) temporary credentials are used by Databricks model serving endpoints to authenticate data access through an instance profile, but cannot bypass network restrictions.
tags:
  - aws
  - security
  - iam
  - model-serving
timestamp: "2026-06-19T21:57:53.252Z"
---

# STS Temporary Credentials for Model Serving

**STS Temporary Credentials for Model Serving** refers to the authentication mechanism used when a [Model Serving](/concepts/model-serving.md) endpoint is configured with an AWS Instance Profile. When you attach an instance profile to a serving endpoint, the endpoint uses AWS Security Token Service (STS) temporary security credentials to authenticate access to AWS resources, such as data stored in S3 buckets.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Overview

Model serving endpoints on Databricks run on Serverless Compute. To allow models to access AWS resources (e.g., model artifacts, feature tables, or other data), you can attach an IAM instance profile to the endpoint configuration. The endpoint then uses STS temporary credentials derived from that instance profile's IAM role to authenticate each request to AWS services.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

This approach avoids embedding long-term AWS credentials in model code or environment variables and enables fine-grained access control through the instance profile's IAM policy.

## How It Works

1. You configure a model serving endpoint with an `instance_profile_arn` pointing to an IAM instance profile already registered in Databricks.
2. At runtime, the serving infrastructure assumes the IAM role associated with that instance profile.
3. STS issues temporary credentials (access key, secret key, and session token) with a limited lifetime.
4. The model uses these temporary credentials to authenticate API calls to AWS services (e.g., S3, DynamoDB, Kinesis).
5. The credentials are automatically rotated by the serving infrastructure without manual intervention.

For detailed instructions on creating and configuring instance profiles, see [AWS Instance Profile Setup](/concepts/instance-profile-databricks-on-aws.md).

## Requirements

Before using STS temporary credentials with model serving endpoints, the following must be in place:

- An instance profile must be [created in AWS](https://docs.databricks.com/aws/en/archive/storage/tutorial-s3-instance-profile) and [added to Databricks](https://docs.databricks.com/aws/en/archive/storage/tutorial-s3-instance-profile#add-instance-profile).^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- The instance profile's IAM role must have a trust relationship configured for serverless compute. If you see the error "IAM role does not have the required trust relationship," follow the setup instructions for Serverless SQL Warehouses data access configuration.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- If you already have an instance profile configured for serverless SQL, ensure the access policies grant your models the right permissions to your resources.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- The endpoint creator must have permission to use the instance profile in Databricks; this is validated at endpoint creation time.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Configuration

### During Endpoint Creation

You can attach an instance profile when [creating a model serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints):

- **From the Serving UI**: Add the instance profile under **Advanced configurations**.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **Using the REST API**: Include the `instance_profile_arn` field in the `served_entities` configuration:^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

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

You can update an existing endpoint's configuration with a new instance profile using the REST API:^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

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

The following limitations apply to STS temporary credentials for model serving:

- **STS temporary credentials cannot bypass network restrictions.** If your AWS resources are behind a VPC or have IP-based access controls, the temporary credentials alone do not provide access — network connectivity must also be configured.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **Changes to the instance profile IAM role in the Databricks UI do not immediately affect running endpoints.** If you edit the instance profile's IAM role from the **Settings** page in the Databricks UI, endpoints that are already running with that instance profile continue to use the old IAM role until the endpoint is updated or restarted.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **Deleting an instance profile from Databricks does not stop running endpoints.** If you delete an instance profile from the Databricks UI and that profile is still in use by a running endpoint, the endpoint is not impacted. The existing STS credentials continue to work until they expire or the endpoint is updated.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- For general model serving endpoint limitations, see Model Serving Limits and Regions.

## Use Cases

- **Accessing feature tables**: Models can look up features stored in your [Feature Store](/concepts/feature-store.md) using the same instance profile attached to the serving endpoint.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **Reading model artifacts**: Models hosted on the endpoint can access model binaries, tokenizers, or configuration files stored in S3 buckets.
- **Accessing external data sources**: Models can read from DynamoDB, write to Kinesis, or interact with any AWS service permitted by the instance profile's IAM policy.

## Best Practices

- **Use dedicated instance profiles** for model serving endpoints rather than reusing profiles from other workloads to scope permissions precisely.
- **Review the IAM trust policy** to ensure it grants the `sts:AssumeRole` action to the serverless compute principal.
- **Monitor endpoint startup logs** for STS-related errors, which often indicate missing trust relationships or permission issues.
- **Rotate instance profiles** by updating the endpoint configuration rather than editing the profile in Databricks settings to ensure changes take effect immediately.

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — Databricks model serving infrastructure
- AWS Instance Profile — IAM role configuration for AWS resource access
- Feature Store Authentication — Using instance profiles for feature lookup
- [Model Serving Environment Variables](/concepts/model-serving-environment-variables.md) — Configuring access to resources from serving endpoints
- Serverless Compute — The compute model underlying serving endpoints
- IAM Roles for Cross-Account Access — Broader AWS IAM patterns

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
