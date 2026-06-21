---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e62d4b6033f3f7cc14f6e47fb1197b801e66dc835f4e2a1a4025315c45dadefe
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - programmatic-instance-profile-assignment-via-serving-endpoints-api
    - PIPAVSEA
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Programmatic Instance Profile Assignment via Serving Endpoints API
description: The Databricks Serving Endpoints API supports the instance_profile_arn field for attaching instance profiles during both endpoint creation and updates using REST API calls.
tags:
  - api
  - model-serving
  - aws
  - databricks
timestamp: "2026-06-19T17:26:48.760Z"
---

# Programmatic Instance Profile Assignment via Serving Endpoints API

**Programmatic Instance Profile Assignment via Serving Endpoints API** allows users to attach an AWS instance profile to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) using the Databricks REST API. This enables the endpoint to access AWS resources (such as S3 buckets) that the instance profile’s IAM role permits. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Requirements

Before assigning an instance profile programmatically, you must:

1. **Create an instance profile** in AWS and **add it to Databricks** using the account or workspace settings. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
2. **Configure a trust relationship** between the instance profile’s IAM role and the Databricks serverless compute. Model serving endpoints run on serverless compute; without this trust relationship, the API returns a `"IAM role does not have the required trust relationship"` error. Setup instructions are available in the serverless SQL warehouse documentation. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
3. If you already use an instance profile for serverless SQL, ensure its policies grant the necessary access for your model workload. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Assigning an Instance Profile When Creating an Endpoint

When creating a model serving endpoint via the [`POST /api/2.0/serving-endpoints`](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints) API, include the `instance_profile_arn` field inside the `served_entities` configuration object. The endpoint creator’s permission to the instance profile is validated at creation time. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

**Example request:**

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

In this example, the endpoint `feed-ads` will use the specified instance profile for all data access. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Updating an Existing Endpoint with an Instance Profile

To add or change the instance profile on an existing endpoint, use the [`PUT /api/2.0/serving-endpoints/{name}/config`](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints) API. Provide the `instance_profile_arn` field in the updated `served_entities` array. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

**Example request:**

```bash
PUT /api/2.0/serving-endpoints/feed-ads/config
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

This operation replaces the entire endpoint configuration; all previous served entities must be included. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Limitations

The following restrictions apply when using programmatic instance profile assignment:

- **Temporary credentials:** STS temporary security credentials are used to authenticate data access. These credentials cannot bypass any network restrictions (e.g., VPC endpoints). ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **Stale IAM role:** If the instance profile’s IAM role is edited in the Databricks UI (**Settings** → **Instance Profiles**), endpoints already running with that profile continue to use the old IAM role until the endpoint is updated or recreated. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **Deletion impact:** If an instance profile is deleted from the Databricks UI, running endpoints that reference it are **not** impacted. The endpoint continues to function with the previously associated credentials. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

For general model serving endpoint quotas and regional availability, see Model Serving limits and regions. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Related Concepts

- AWS Instance Profile – How to create and manage instance profiles in AWS.
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) – Overview of serving endpoints on Databricks.
- Serverless Compute – The compute layer that model serving endpoints use.
- [IAM Role Trust Policy for Serverless](/concepts/trust-relationship-for-serverless-compute.md) – Configuring trust relationships for serverless workloads.
- Lookup Features with Instance Profile – Using the same instance profile for feature store authentication.

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
