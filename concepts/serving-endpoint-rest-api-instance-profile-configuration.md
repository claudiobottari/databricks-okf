---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 57052610e0f4b6e3511bd750796959ca6435067dee33019fa59235f3999566cd
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serving-endpoint-rest-api-instance-profile-configuration
    - SERAIPC
    - AWS Instance Profile Configuration
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Serving Endpoint REST API Instance Profile Configuration
description: The instance_profile_arn field in the Databricks Serving Endpoint REST API (POST/PUT /api/2.0/serving-endpoints) used to attach an AWS instance profile during endpoint creation or update.
tags:
  - api
  - model-serving
  - aws
  - databricks
timestamp: "2026-06-18T10:39:08.203Z"
---

# Serving Endpoint REST API Instance Profile Configuration

This page explains how to configure an AWS **instance profile** for a model serving endpoint using the Databricks Serving REST API. Attaching an instance profile to an endpoint allows the model to access any AWS resources that the instance profile’s IAM role permits, such as S3 buckets or databases. You can assign an instance profile both when creating an endpoint and when updating an existing endpoint. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Requirements

Before you can attach an instance profile to a serving endpoint, you must:

- **Create an AWS instance profile** in your AWS account with the necessary IAM policies. See the [instance profile setup guide](https://docs.databricks.com/aws/en/archive/storage/tutorial-s3-instance-profile). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **Add the instance profile to Databricks** using the Databricks account or workspace console (Settings > Cloud resources > Instance profiles). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **Configure a trust relationship** for serverless compute. Model serving endpoints run on serverless compute, so the instance profile’s IAM role must trust the Databricks serverless compute principal. If you see the error “IAM role does not have the required trust relationship”, follow the [serverless SQL warehouse instance profile setup instructions](https://docs.databricks.com/aws/en/admin/sql/data-access-configuration#aws-instance-profile-setup). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

If an instance profile is already configured for serverless SQL warehouses, you may need to adjust its IAM policies to grant the model access to the required resources. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Add an Instance Profile During Endpoint Creation

You can specify an instance profile when you create a model serving endpoint, either through the Databricks Serving UI or via the REST API.

### Using the Serving UI

1. Navigate to the **Serving** UI.
2. Click **Create serving endpoint**.
3. Under **Advanced configurations**, locate the **Instance profile** field.
4. Select the desired instance profile from the list.
5. Complete the remaining endpoint fields and create the endpoint.

> The endpoint creator’s permission to use the instance profile is validated at endpoint creation time. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Using the REST API

Use the `POST /api/2.0/serving-endpoints` endpoint and include the `instance_profile_arn` field inside each `served_entity` configuration. The following example creates an endpoint named `feed-ads` serving a model entity with an instance profile: ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

```bash
POST /api/2.0/serving-endpoints
{
  "name": "feed-ads",
  "config": {
    "served_entities": [
      {
        "entity_name": "ads1",
        "entity_version": "1",
        "workload_size": "Small",
        "scale_to_zero_enabled": true,
        "instance_profile_arn": "arn:aws:iam::<aws-account-id>:instance-profile/<instance-profile-name-1>"
      }
    ]
  }
}
```

## Update an Existing Endpoint with an Instance Profile

You can also add or change the instance profile on an existing endpoint using the `PUT /api/2.0/serving-endpoints/{name}/config` endpoint. Supply the updated `served_entities` array with the new `instance_profile_arn`: ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

```bash
PUT /api/2.0/serving-endpoints/{name}/config
{
  "served_entities": [
    {
      "entity_name": "ads1",
      "entity_version": "2",
      "workload_size": "Small",
      "scale_to_zero_enabled": true,
      "instance_profile_arn": "arn:aws:iam::<aws-account-id>:instance-profile/<instance-profile-name-2>"
    }
  ]
}
```

After the update, the endpoint will use the new instance profile for subsequent inference requests.

## Limitations

The following limitations apply when using instance profiles with model serving endpoints:

- **STS temporary credentials** are used to authenticate data access. Network restrictions (e.g., VPC endpoints) cannot be bypassed through the instance profile. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- If you **edit the IAM role** attached to the instance profile from the Databricks Settings UI, endpoints already running with that profile **continue to use the old IAM role** until the endpoint is updated (e.g., by re-deploying or changing the configuration). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- If you **delete an instance profile** from the Databricks Settings UI, any running endpoints that are using that profile **are not immediately impacted**. The endpoint continues to operate until it is redeployed or updated. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

For general model serving endpoint limits (e.g., concurrency, payload size, regional availability), see [Model Serving limits and regions](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Additional Resources

- [Look up features](https://docs.databricks.com/aws/en/machine-learning/feature-store/fs-authentication) using the same instance profile attached to the serving endpoint to authenticate to the Feature Store. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- [Configure access to resources from model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/store-env-variable-model-serving) using environment variables or secrets. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Related Concepts

- Serving Endpoint — Manage model serving endpoints with the REST API
- AWS Instance Profile — IAM role-based credentials for AWS resource access
- Serverless Compute — Compute infrastructure used by model serving
- Feature Store Authentication — Using instance profiles for feature lookup
- Model Serving Limits — Quotas and constraints for serving endpoints

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
