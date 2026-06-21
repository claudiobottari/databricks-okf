---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 05b7a4691482bff7b69c084fd5dfcbda2998e5a1424b14e992970b82a0a9da38
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - instance-profile-lifecycle-and-running-endpoints
    - Running Endpoints and Instance Profile Lifecycle
    - IPLARE
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Instance Profile Lifecycle and Running Endpoints
description: Running endpoints continue to use the originally attached instance profile IAM role even if the profile is edited or deleted from the Databricks UI; changes only take effect upon endpoint update.
tags:
  - databricks
  - aws
  - iam
  - lifecycle
timestamp: "2026-06-18T14:19:49.641Z"
---

Here is the wiki page for "Instance Profile Lifecycle and Running Endpoints", written solely from the provided source material.

---

## Instance Profile Lifecycle and Running Endpoints

An **instance profile** attached to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) allows the model to access AWS resources, such as S3 buckets, that the instance profile's IAM role permits. The lifecycle of this profile—creation, update, and deletion—has specific behaviors that impact running endpoints. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Adding an Instance Profile

An instance profile can be added to a model serving endpoint during endpoint creation or by updating an existing endpoint's configuration. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

#### During Endpoint Creation

When creating a model serving endpoint, you can add an instance profile to the endpoint configuration. The endpoint creator's permission to the instance profile is validated at creation time. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

- **UI:** In the Serving UI, add an instance profile under **Advanced configurations**. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **API:** Use the `instance_profile_arn` field in the `served_entities` configuration when creating an endpoint via the `POST /api/2.0/serving-endpoints` endpoint. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

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

#### Updating an Existing Endpoint

You can update an existing model serving endpoint configuration with an instance profile by including the `instance_profile_arn` field in the `PUT /api/2.0/serving-endpoints/{name}/config` request. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

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

### Lifecycle Behaviors and Limitations

The following behaviors govern how changes to an instance profile affect running endpoints: ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

- **IAM role edits in the UI are not applied immediately.** If you edit the instance profile's IAM role from the **Settings** of the Databricks UI, endpoints running with that profile continue to use the old IAM role until the endpoint updates. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **Deleting an instance profile from the UI does not impact running endpoints.** If you delete an instance profile from the **Settings** of the Databricks UI and that profile is used in running endpoints, the running endpoint is not impacted. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **STS temporary security credentials are used.** These temporary credentials authenticate data access but cannot bypass any network restrictions. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Requirements

- You must first create an instance profile and then add it to Databricks. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- If you have an instance profile already configured for serverless SQL, ensure its access policies are updated to grant the model the correct access to your resources. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- Model serving endpoints run on serverless compute, so the instance profile's IAM role must have a trust relationship configured for serverless compute. If you see the error "IAM role does not have the required trust relationship," follow the setup instructions for serverless SQL warehouses. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Related Concepts

- [Model Serving Endpoint](/concepts/model-serving-endpoint.md)
- [Instance Profiles](/concepts/instance-profile-databricks-on-aws.md)
- AWS IAM Roles for Model Serving
- Serverless Compute

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
