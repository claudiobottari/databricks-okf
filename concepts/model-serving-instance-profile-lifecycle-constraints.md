---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 936fe4d43e561da69a85a2234c4a01c181e88dd55e0d2dd86f642264c14762e6
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-instance-profile-lifecycle-constraints
    - MSIPLC
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Model Serving Instance Profile Lifecycle Constraints
description: "Operational constraints around serving endpoint instance profiles: endpoints retain the old IAM role if the profile is edited in Databricks Settings, and deleting a profile does not affect running endpoints."
tags:
  - aws
  - model-serving
  - iam
  - databricks
timestamp: "2026-06-18T10:39:21.121Z"
---

# Model Serving Instance Profile Lifecycle Constraints

**Instance profiles** attached to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) grant the endpoint permission to access AWS resources (e.g., S3 buckets, DynamoDB tables) that the instance profile’s IAM role allows. This page describes the lifecycle behavior of instance profiles on model serving endpoints — what happens when a profile is added, updated, or removed, and the constraints that govern these operations. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Requirements

Before you can attach an instance profile to an endpoint, the profile must already exist in AWS and be registered in Databricks. The IAM role associated with the instance profile must have a trust relationship configured for Databricks serverless compute. If the trust relationship is missing, you will see the error “IAM role does not have the required trust relationship.” Setup instructions for this trust relationship follow the same process as for serverless SQL warehouses. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

The endpoint creator’s permission to the chosen instance profile is validated at endpoint creation time. If the creator lacks the necessary AWS permissions to assume the role, the creation fails. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Adding an Instance Profile During Endpoint Creation

You can attach an instance profile when creating a new model serving endpoint.

- **Using the Serving UI**: In the **Create a model serving endpoint** dialog, expand **Advanced configurations** and select the desired instance profile from the drop-down. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

- **Using the REST API**: Include the `instance_profile_arn` field inside each `served_entities` entry in the endpoint configuration. For example:

```json
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

## Updating an Existing Endpoint’s Instance Profile

You can change (or add) the instance profile on a running endpoint by calling the update config API and specifying the `instance_profile_arn` field in the request body. The new profile takes effect when the endpoint next updates its configuration.

```json
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

## Lifecycle Constraints

The following constraints govern the behavior of instance profiles once they are attached to a model serving endpoint:

- **STS temporary credentials are used for authentication.** The endpoint always authenticates to AWS resources using short-lived AWS Security Token Service (STS) credentials obtained from the instance profile’s IAM role. This mechanism cannot bypass any network restrictions (e.g., VPC endpoints, security groups). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

- **Editing the IAM role in the Databricks UI does not immediately affect running endpoints.** If you modify the instance profile’s IAM role (for example, by changing its trust policy or permissions) from the **Settings** page in the Databricks UI, endpoints that already use that instance profile continue to use the **old** role until the endpoint is updated. To force the endpoint to use the new role, you must update the endpoint configuration (for example, by re-deploying with the same profile ARN). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

- **Deleting an instance profile from the Databricks UI does not stop running endpoints.** If you remove the instance profile from the Databricks Settings page (i.e., its registration in Databricks), any endpoints that were launched with that profile will continue to run and still have access to AWS resources via the already-assumed IAM role. The profile is only required during endpoint creation and updates; after that, the endpoint holds the role’s credentials independently of the profile’s registration. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

- **Instance profile permission is validated only at endpoint creation time.** As noted in Requirements, the creator’s ability to use the profile is checked when the endpoint is first created. Subsequent updates to the endpoint do not re-validate the current user’s permissions against the profile. This means that if the IAM role’s trust policy is later changed to remove the creator’s access, an existing endpoint may continue to operate without interruption. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

For general model serving endpoint limitations (e.g., concurrency, region availability), see Model Serving Limits and Regions. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Additional Resources

- [Look up features](https://docs.databricks.com/aws/en/machine-learning/feature-store/fs-authentication) using the same instance profile attached to the serving endpoint.
- [Configure access to resources from model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/store-env-variable-model-serving) using environment variables.

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
