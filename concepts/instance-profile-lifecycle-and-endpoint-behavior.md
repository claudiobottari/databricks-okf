---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 36d1f8bca2c0ca7940ac58cac04223cf5ee56b7b71941bbc1ef3370b036b49fe
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - instance-profile-lifecycle-and-endpoint-behavior
    - Endpoint Behavior and Instance Profile Lifecycle
    - IPLAEB
    - instance-profile-lifecycle-and-running-endpoints
    - Running Endpoints and Instance Profile Lifecycle
    - IPLARE
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Instance Profile Lifecycle and Endpoint Behavior
description: Modifying or deleting an instance profile in Databricks settings does not affect running endpoints until they are updated or restarted.
tags:
  - aws
  - iam
  - lifecycle
  - databricks
timestamp: "2026-06-19T17:26:49.250Z"
---

```yaml
---
title: Instance Profile Lifecycle and Endpoint Behavior
summary: Editing or deleting an instance profile in Databricks settings does not immediately affect running model serving endpoints; old credentials persist until the endpoint is updated.
sources:
  - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T13:53:12.489Z"
updatedAt: "2026-06-19T13:53:12.489Z"
tags:
  - aws
  - model-serving
  - limitations
  - lifecycle
aliases:
  - instance-profile-lifecycle-and-endpoint-behavior
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# Instance Profile Lifecycle and Endpoint Behavior

**Instance Profile Lifecycle and Endpoint Behavior** describes how [[Instance Profile (Databricks on AWS)|instance profiles]] are associated with [[Model Serving Endpoint|model serving endpoints]] on Databricks and what happens when those instance profiles are modified or deleted after an endpoint is running. Understanding this lifecycle is essential for managing data access from serving endpoints without unintended service disruptions.

## Associating an Instance Profile with an Endpoint

Instance profiles can be attached to a model serving endpoint either during creation or through a subsequent configuration update. This association allows the endpoint to access AWS resources (such as S3 buckets) that the instance profile's IAM role permits. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### At Endpoint Creation

When creating a model serving endpoint, you can specify an instance profile in the endpoint configuration. The endpoint creator's permission to use the instance profile is validated at creation time. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

In the Serving UI, you can add an instance profile under **Advanced configurations**. For programmatic workflows, use the `instance_profile_arn` field in the [Create Serving Endpoint API](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

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

You can update an existing model serving endpoint's configuration with a new instance profile using the `instance_profile_arn` field in the [Update Serving Endpoint API](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints). This is done via a `PUT` request to `/api/2.0/serving-endpoints/{name}/config`. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Lifecycle Behavior During Modifications

### Editing the Instance Profile IAM Role

If an administrator edits the instance profile's IAM role from the **Settings** page of the Databricks UI, endpoints that are already running with that instance profile **continue to use the old IAM role** until the endpoint is updated. This means that changes to the IAM role's permissions do not take effect on existing endpoints until those endpoints are refreshed or reconfigured. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Deleting an Instance Profile from Databricks

If an instance profile is deleted from the **Settings** page of the Databricks UI and that profile is currently in use by running endpoints, the **running endpoint is not impacted**. The endpoint continues functioning with the previously configured IAM role, even though the profile reference has been removed from the Databricks configuration. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Authentication Mechanism

Model serving endpoints run on [[Serverless GPU Compute|serverless compute]] infrastructure. The endpoint uses AWS [[STS Token Sharing|STS (Security Token Service)]] temporary security credentials to authenticate data access. These credentials are bound by the access policies of the assigned instance profile's IAM role. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Trust Relationship Requirement

For an instance profile to work with model serving endpoints, the IAM role must have a trust relationship configured for serverless compute. If the trust relationship is not set up, the endpoint creation or update may fail with the error: "IAM role does not have the required trust relationship." Instructions for configuring this trust relationship are available in the documentation for serverless SQL warehouse data access configuration. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Limitations

- STS temporary credentials are used for data access authentication. This mechanism cannot bypass any network restrictions. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- Endpoints that were created with an instance profile will retain the old IAM role until the endpoint itself is updated, even if the IAM role's permissions are modified in the AWS console or Databricks UI. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- Deleting an instance profile from Databricks settings does not affect running endpoints that reference it. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Related Concepts

- [[Instance Profile (Databricks on AWS)|Instance profiles]] — IAM roles that grant AWS resource access
- [[Model Serving Endpoint|Model serving endpoints]] — The serverless infrastructure that hosts models
- [[Serverless GPU Compute|Serverless compute]] — The compute layer that model serving endpoints run on
- STS temporary credentials — Short-lived credentials used for data access
- [[Secrets-Based Environment Variables for Model Serving|Environment variables for model serving]] — Alternative method for configuring resource access
- Feature store authentication — Accessing feature store with the same instance profile

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
```

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
