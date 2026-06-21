---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7786956b1dca686e6f0700249d9d82a74f7bb653ba8cd7fe2d69891b60303d8e
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-databricks
    - MSE(
    - Deploy a model serving endpoint with Databricks SDK
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Model Serving Endpoint (Databricks)
description: A serverless endpoint that hosts one or more ML models for inference, configurable with instance profiles, workload sizes, and scale-to-zero settings.
tags:
  - machine-learning
  - model-serving
  - databricks
timestamp: "2026-06-19T21:57:39.238Z"
---

---

title: Model Serving Endpoint (Databricks)
sources:
  - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T10:00:00Z"
updatedAt: "2026-06-20T10:00:00Z"
tags:
  - databricks
  - model-serving
  - endpoint
  - instance-profile
aliases:
  - Model Serving Endpoint
confidence: 0.9
provenanceState: inferred
inferredParagraphs: 0

---

# Model Serving Endpoint (Databricks)

A **Model Serving Endpoint** on Databricks provides a managed, serverless compute environment for deploying machine learning models as REST APIs. Endpoints run on Serverless Compute and can be configured with an Instance Profile (AWS IAM role) to grant access to AWS resources such as S3 buckets, DynamoDB tables, or other services required by the model during inference. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Requirements for Using an Instance Profile

To attach an instance profile to a model serving endpoint, you must first meet the following prerequisites:

- Create an instance profile in AWS (an IAM role with a trust policy that allows EC2 and serverless compute to assume it). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- Add the instance profile to Databricks via the admin settings. If the instance profile is already configured for serverless SQL warehouses, you may need to adjust its access policies so that your model has the correct permissions for its resources. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- The IAM role must have a trust relationship configured for Databricks serverless compute. If you see the error "IAM role does not have the required trust relationship," follow the setup instructions for AWS instance profile trust with serverless SQL warehouses. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Attaching an Instance Profile

You can attach an instance profile during endpoint creation or update an existing endpoint’s configuration.

### During Endpoint Creation

When creating a serving endpoint from the UI, navigate to **Advanced configurations** and select the instance profile. For programmatic workflows, use the `instance_profile_arn` field in the `POST /api/2.0/serving-endpoints` request. The endpoint creator must have permission to use the instance profile at creation time. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

Example API request snippet:

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

Use the `PUT /api/2.0/serving-endpoints/{name}/config` endpoint to update the configuration of a running endpoint, including changing the instance profile ARN. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

Example:

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

- **STS temporary credentials**: The endpoint uses AWS Security Token Service (STS) temporary credentials to authenticate data access. These credentials cannot bypass network restrictions such as VPC or firewall rules. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **IAM role updates via UI**: If you edit the instance profile’s IAM role from the Databricks **Settings** page, endpoints that are already running with that instance profile continue to use the old role until the endpoint is updated (e.g., through a config update or redeployment). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **Deletion of instance profile**: If you delete an instance profile from the Databricks **Settings** page, running endpoints that use that profile are not impacted; they continue to function with the previously assigned role. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

For general model serving endpoint limits and regional availability, see Model Serving Limits and Regions.

## Additional Resources

- Use the same instance profile attached to a serving endpoint to Look Up Features in the Databricks Feature Store for online inference. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- Configure Access to Resources from Model Serving Endpoints covers storing environment variables and secrets required by models. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Related Concepts

- Instance Profile
- Serverless Compute
- [Model Serving](/concepts/model-serving.md)
- IAM Roles for AWS Resources
- Feature Store Authentication
- Model Serving Limits and Regions

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
