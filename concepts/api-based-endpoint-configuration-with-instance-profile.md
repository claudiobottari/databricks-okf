---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 406a586b044472192c7cc473aa0ad1b1a822a1cf5adc864440c348bbb54e9ecd
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - api-based-endpoint-configuration-with-instance-profile
    - AECWIP
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: API-Based Endpoint Configuration with Instance Profile
description: Using the Databricks Serving Endpoints API (POST/PUT /api/2.0/serving-endpoints) with the instance_profile_arn field to assign an instance profile during creation or update.
tags:
  - api
  - model-serving
  - configuration
timestamp: "2026-06-19T13:53:21.700Z"
---

# API-Based Endpoint Configuration with Instance Profile

**API-Based Endpoint Configuration with Instance Profile** refers to the process of attaching an AWS Instance Profile to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) using the Databricks REST API, either during endpoint creation or by updating an existing endpoint. This configuration allows models deployed on the endpoint to access AWS resources (such as S3 buckets) that are permissible under the instance profile’s IAM role. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Requirements

Before attaching an instance profile to a model serving endpoint via the API, the following prerequisites must be met:

1. **Create an instance profile** in AWS with the necessary IAM role and policies. See the Databricks documentation on [creating an instance profile](https://docs.databricks.com/aws/en/archive/storage/tutorial-s3-instance-profile). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
2. **Add the instance profile to Databricks** through the workspace’s settings. If the instance profile is already used for serverless SQL, ensure that the access policies are updated so that models have the correct permissions to the required resources. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
3. **Configure a trust relationship** for serverless compute. Because model serving endpoints run on serverless compute, the instance profile’s IAM role must have a trust policy that allows the serverless compute service to assume the role. If the error “IAM role does not have the required trust relationship” appears, follow the setup instructions provided in the serverless SQL warehouse configuration guide. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Adding an Instance Profile During Endpoint Creation

When creating a new model serving endpoint via the API, the `instance_profile_arn` field can be included in the request body’s `served_entities` array to attach the instance profile. The endpoint creator’s permission to use the specified instance profile is validated at creation time. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

**Example API call (POST /api/2.0/serving-endpoints):**

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

This can also be done from the Serving UI under **Advanced configurations** during endpoint creation. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Updating an Existing Endpoint with an Instance Profile

To attach a new instance profile to an existing endpoint (or change the one currently attached), use the `PUT /api/2.0/serving-endpoints/{name}/config` endpoint with the `instance_profile_arn` field in the updated `served_entities` configuration. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

**Example API call (PUT /api/2.0/serving-endpoints/{name}/config):**

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

## Limitations

The following limitations apply when using instance profiles with model serving endpoints:

- **STS temporary credentials** are used to authenticate data access. This method cannot bypass any network restrictions that the endpoint may be subject to. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **IAM role changes in the Databricks UI** are not immediately reflected. If the instance profile’s IAM role is edited from the **Settings** page of the workspace, endpoints that are already running with that instance profile continue to use the old IAM role until the endpoint is updated (e.g., by redeploying the configuration). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **Deleting an instance profile** from the **Settings** page does not impact running endpoints that still reference that profile. The endpoint continues to operate with the previously attached profile. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

For general model serving endpoint limits and regional availability, refer to the [Model Serving limits and regions](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits) documentation. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Additional Use Cases

Once an instance profile is attached to an endpoint, the same profile can be used to look up features from the [Feature Store](/concepts/feature-store.md). See the documentation on [authenticating feature lookups](https://docs.databricks.com/aws/en/machine-learning/feature-store/fs-authentication). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

For broader configuration of access to resources from model serving endpoints (including environment variables), see [Configure access to resources from model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/store-env-variable-model-serving). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoint](/concepts/model-serving-endpoint.md)
- Instance Profile
- IAM Role
- Serverless Compute
- [Feature Store](/concepts/feature-store.md)
- S3 Data Access
- Service Principal

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
