---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 32cdc9736a22db844df7b90c796c5a96e0323e4cf3ca5ab7f264346e049d4974
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serving-endpoint-rest-api-databricks
    - SERA(
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Serving Endpoint REST API (Databricks)
description: The Databricks REST API (endpoints /api/2.0/serving-endpoints) for creating and updating model serving endpoint configurations, including fields like instance_profile_arn.
tags:
  - api
  - model-serving
  - databricks
  - rest
timestamp: "2026-06-19T21:57:49.944Z"
---

# Serving Endpoint REST API (Databricks)

The **Serving Endpoint REST API** allows you to programmatically create, manage, and update [Model Serving Endpoints](/concepts/model-serving-endpoint.md) on Databricks. This API enables automated workflows for deploying and maintaining models in production, including the configuration of [Instance Profiles](/concepts/instance-profile-databricks-on-aws.md) for accessing AWS resources.

## Creating an Endpoint with an Instance Profile

When creating a model serving endpoint via the API, you can attach an Instance Profile to enable the endpoint to access AWS resources. The endpoint creator's permission to the instance profile is validated at creation time. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

To create an endpoint with an instance profile, use the `POST /api/2.0/serving-endpoints` endpoint with the `instance_profile_arn` field in the `served_entities` configuration:

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

## Updating an Existing Endpoint

You can update an existing model serving endpoint's configuration, including adding or changing the instance profile, using the `PUT /api/2.0/serving-endpoints/{name}/config` endpoint: ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

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

## Using the Serving UI

As an alternative to the REST API, instance profiles can also be added during endpoint creation through the Serving UI under **Advanced configurations**. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Prerequisites

Before using the Serving Endpoint REST API with instance profiles:

1. **Create an instance profile** following the AWS documentation.
2. **Add the instance profile to Databricks** through the admin settings.
3. **Configure the IAM role trust relationship** for serverless compute. If you see the error "IAM role does not have the required trust relationship," follow setup instructions for serverless SQL warehouse instance profiles.
4. If using an instance profile already configured for Serverless SQL, update the access policies so models have appropriate resource access. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Limitations

The following limitations apply when using the Serving Endpoint REST API with instance profiles: ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

- **STS credentials**: AWS Security Token Service (STS) temporary security credentials are used to authenticate data access. This cannot bypass any network restrictions.
- **Stale IAM roles**: If you edit the instance profile IAM role from the Databricks UI **Settings**, endpoints running with that instance profile continue to use the old IAM role until the endpoint is updated.
- **Deleted profiles**: If you delete an instance profile from the Databricks UI **Settings** that is used in running endpoints, the running endpoint is not impacted.

For general model serving endpoint limitations, see Model Serving limits and regions.

## Additional Resources

- Use the same instance profile attached to a serving endpoint to [Look up features](/concepts/featurespec.md) from the [Feature Store](/concepts/feature-store.md).
- Configure access to resources from model serving endpoints for more configuration options.

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md)
- [Instance Profiles](/concepts/instance-profile-databricks-on-aws.md)
- AWS IAM Roles
- Serverless Compute
- [Feature Store](/concepts/feature-store.md)
- [Serving UI](/concepts/serving-ui.md)

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
