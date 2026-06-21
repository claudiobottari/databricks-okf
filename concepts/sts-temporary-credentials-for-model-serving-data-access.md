---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 145dac8f5565df587362f60c8d269300ab50963602905c56a2b60f6b9c18f694
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sts-temporary-credentials-for-model-serving-data-access
    - STCFMSDA
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: STS Temporary Credentials for Model Serving Data Access
description: AWS STS temporary security credentials are used to authenticate data access from model serving endpoints, but they cannot bypass network restrictions.
tags:
  - aws
  - sts
  - security
  - networking
timestamp: "2026-06-19T17:26:43.889Z"
---

```markdown
---
title: STS Temporary Credentials for Model Serving Data Access
summary: Databricks uses AWS STS temporary security credentials to authenticate data access from model serving endpoints, which cannot bypass network restrictions.
sources:
  - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T13:53:15.447Z"
updatedAt: "2026-06-19T13:53:15.447Z"
tags:
  - aws
  - security
  - authentication
  - sts
aliases:
  - sts-temporary-credentials-for-model-serving-data-access
  - STCFMSDA
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# STS Temporary Credentials for Model Serving Data Access

**STS Temporary Credentials** refers to the authentication mechanism used when attaching an AWS instance profile to a [[Model Serving Endpoint]] on Databricks. When an instance profile is associated with a serving endpoint, Databricks uses AWS Security Token Service (STS) to generate temporary security credentials that allow models to access AWS resources permitted by that instance profile's IAM role. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Overview

When you attach an instance profile to a model serving endpoint, the endpoint uses STS temporary credentials to authenticate data access to AWS resources such as S3 buckets, DynamoDB tables, or other services. These credentials are short-lived and automatically rotated, following AWS security best practices. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## How It Works

1. An instance profile with an IAM role is created in AWS and added to Databricks.
2. The instance profile is attached to a [[Model Serving Endpoint]] during endpoint creation or by updating an existing endpoint's configuration.
3. When the model serving endpoint needs to access AWS resources, Databricks uses STS to generate temporary credentials scoped to the permissions of the attached IAM role.
4. These temporary credentials are used for data access, not for bypassing network restrictions. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Adding an Instance Profile to an Endpoint

### During Endpoint Creation

When creating a model serving endpoint, you can add an instance profile through:

- **Serving UI**: Navigate to **Advanced configurations** during endpoint setup.
- **API**: Use the `instance_profile_arn` field in the endpoint creation request:

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

### Updating an Existing Endpoint

You can update an existing endpoint's configuration with a new or different instance profile using the PUT API:

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

### Permission Validation

The endpoint creator's permission to use the specified instance profile is validated at endpoint creation time. The IAM role associated with the instance profile must have a trust relationship configured for serverless compute. If you encounter the error "IAM role does not have the required trust relationship," you must configure the trust policy following the setup instructions for serverless SQL warehouses. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Limitations

The following limitations apply when using STS temporary credentials for model serving data access:

- **Network restrictions**: STS temporary credentials authenticate data access but cannot bypass any network restrictions. Network-level controls still apply.
- **Stale credentials**: If you edit the instance profile's IAM role from the Databricks UI **Settings** page, endpoints currently running with that instance profile continue to use the old IAM role until the endpoint is updated.
- **Profile deletion**: If you delete an instance profile from the Databricks UI **Settings** page and that profile is actively used in running endpoints, the running endpoints are not impacted.

^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Requirements

Before using an instance profile with a model serving endpoint:

1. **Create an instance profile** in AWS with the appropriate IAM role and policies.
2. **Add the instance profile to Databricks** following the setup documentation.
3. **Configure trust relationship**: If the instance profile is already configured for serverless SQL, update the access policies so your models have the correct access permissions.
4. **Set up serverless trust**: The IAM role must have the required trust relationship for serverless compute. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Use Cases

STS temporary credentials for model serving endpoints enable models to:

- Access training data from S3 buckets during inference
- Read reference data from DynamoDB or other AWS services
- Write inference results or logs to S3
- Call other AWS services that the instance profile's IAM role permits
- Look up features from a [[Feature Store]] using the same instance profile attached to the serving endpoint

^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Related Concepts

- Instance Profile — The AWS IAM mechanism for granting permissions to AWS resources
- [[Model Serving Endpoint]] — The Databricks endpoint that hosts models for inference
- AWS IAM Roles — The underlying permission system for STS temporary credentials
- Serverless Compute — The compute model that model serving endpoints run on
- Feature Store Authentication — Using instance profiles for feature lookups
- Model Serving Security — Overall security considerations for model serving

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
```

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
