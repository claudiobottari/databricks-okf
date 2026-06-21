---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cf38f59204491978f888ed3f62b50b573e61578ce1692abc6ac2a2504d6d9456
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-configuration-api
    - MSECA
    - Model Serving Endpoint Configuration
    - Serving endpoint configuration
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Model Serving Endpoint Configuration API
description: The REST API endpoints and payload format for creating (POST /api/2.0/serving-endpoints) and updating (PUT /api/2.0/serving-endpoints/{name}/config) model serving endpoints with an instance_profile_arn field.
tags:
  - api
  - model-serving
  - configuration
timestamp: "2026-06-19T08:51:24.431Z"
---

# Model Serving Endpoint Configuration API

The **Model Serving Endpoint Configuration API** provides REST endpoints to create and update [model serving endpoints](/concepts/model-serving-endpoint.md) on Databricks. The configuration allows you to attach an Instance Profile to an endpoint so that the model can access AWS resources (such as S3 buckets, databases, or other services) that the instance profile has permission to access. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## API Endpoints

### Create an endpoint

Use `POST /api/2.0/serving-endpoints` to create a new serving endpoint. The request body includes a `config` object with a list of `served_entities`. Each entity can specify an `instance_profile_arn` to associate an AWS instance profile with that served model. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

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

### Update an existing endpoint

Use `PUT /api/2.0/serving-endpoints/{name}/config` to update the configuration of an existing endpoint. The same `instance_profile_arn` field can be used to change or add an instance profile. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

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

## Instance Profile Attachment

Instance profiles can be attached during endpoint creation via the API or through the [Serving UI](/concepts/serving-ui.md) under **Advanced configurations**. The endpoint creator’s permission to use the instance profile is validated at creation time. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Prerequisites

- The instance profile must already be [added to Databricks](https://docs.databricks.com/aws/en/archive/storage/tutorial-s3-instance-profile#add-instance-profile). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- The IAM role associated with the instance profile must have a trust relationship configured for Serverless Compute. If this is missing, the error “IAM role does not have the required trust relationship” will appear. See [Confirm or set up an AWS instance profile to use with your serverless SQL warehouses](https://docs.databricks.com/aws/en/admin/sql/data-access-configuration#aws-instance-profile-setup) for setup instructions. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Limitations

The following limitations apply when using instance profiles with serving endpoints: ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

- **STS temporary credentials** are used to authenticate data access. The instance profile cannot bypass any network restrictions.
- If you edit the instance profile IAM role from the Databricks **Settings** page, endpoints that are already running with the old instance profile continue to use the old IAM role until the endpoint is updated.
- If you delete an instance profile from Databricks **Settings**, endpoints that are currently using that profile are not immediately impacted.

For general serving endpoint limitations, see Model Serving Limits and Regions.

## Additional Resources

- [Look up features|Look up features](/concepts/featurelookup.md) using the same instance profile attached to the serving endpoint in the [Feature Store](/concepts/feature-store.md). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- Configure access to resources from model serving endpoints for more details on environment variables and data access. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
