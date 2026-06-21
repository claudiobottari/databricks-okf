---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 946c17961f27878b13f4a7bca0fb13ece28023623d44921565952645093a4d18
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-instance-profile
    - MSIP
    - Add model serving instance profile
    - IAM instance profile
    - Instance profile
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Model Serving Instance Profile
description: An AWS IAM instance profile attached to a Databricks model serving endpoint, allowing models to access AWS resources (e.g., S3, Feature Store) during inference.
tags:
  - aws
  - model-serving
  - iam
  - databricks
timestamp: "2026-06-18T10:38:53.900Z"
---

#Model Serving Instance Profile

A **Model Serving Instance Profile** is an AWS IAM instance role attached to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) that allows the endpoint to access AWS resources (such as S3 buckets or other services) permitted by that profile. By attaching an instance profile, customers can give their model serving endpoints the same credentials that the profile provides, enabling secure data access without hard‑coding secrets.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

---

## Requirements

Before you can attach an instance profile to an endpoint:

1. **Create an instance profile** in AWS (see the [AWS documentation on instance profiles](https://docs.databricks.com/aws/en/archive/storage/tutorial-s3-instance-profile)).
2. **Add the instance profile to Databricks** through the admin settings (see [Add an instance profile](https://docs.databricks.com/aws/en/archive/storage/tutorial-s3-instance-profile#add-instance-profile)).
   - If the instance profile is already configured for Serverless SQL warehouses, ensure its IAM trust policy also grants access for model serving endpoints.
3. **Configure the IAM role’s trust relationship** for serverless compute. If the role lacks the required trust relationship, you will see the error *“IAM role does not have the required trust relationship”*. Follow the setup instructions in [Confirm or set up an AWS instance profile to use with your serverless SQL warehouses](https://docs.databricks.com/aws/en/admin/sql/data-access-configuration#aws-instance-profile-setup).^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

---

## Adding an Instance Profile During Endpoint Creation

When you create a model serving endpoint, you can include the instance profile as part of the endpoint configuration.

### Using the Serving UI

1. In the Databricks workspace, navigate to the **Serving** UI.
2. Begin creating a new endpoint and expand **Advanced configurations**.
3. In the **Instance profile** field, select or enter the ARN of the instance profile you want to attach.

![Create a model serving endpoint with instance profile](https://docs.databricks.com/aws/en/assets/images/add-instance-profile-85d7ec40a687ac01fbd4cf84183f725b.png)^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

> **Note:** The endpoint creator’s permission to the instance profile is validated at creation time.

### Using the REST API

For programmatic workflows, provide the `instance_profile_arn` field inside the `served_entities` array of the `POST /api/2.0/serving-endpoints` request:

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

---

## Updating an Existing Endpoint with an Instance Profile

You can also add or change the instance profile on an already‑running endpoint using the `PUT /api/2.0/serving-endpoints/{name}/config` endpoint. The same `instance_profile_arn` field is used:

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

---

## Limitations

The following limitations apply when using instance profiles with model serving endpoints:

- **STS credentials**: Data access is authenticated using temporary security credentials from AWS Security Token Service (STS). These credentials cannot bypass any network restrictions (e.g., VPC endpoints or firewalls).^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **Role changes not propagated to running endpoints**: If you edit the instance profile’s IAM role in the Databricks UI (under **Settings**), endpoints that are already running with that profile continue to use the *old* IAM role until the endpoint is updated or redeployed.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **Deleting a profile does not impact running endpoints**: If you delete an instance profile from the Databricks admin settings while it is still in use by a running endpoint, the endpoint is not affected — it continues to use the original profile.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

For general model serving endpoint limitations, see Model Serving Limits and Regions.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

---

## Additional Resources

- Use the same instance profile attached to a serving endpoint to Look Up Features from the Feature Store.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- Learn how to Configure Access to Resources from Model Serving Endpoints using environment variables and other methods.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

---

## Related Concepts

- AWS IAM Roles and Instance Profiles
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md)
- Serverless Compute
- Feature Store Authentication
- S3 Bucket Access for Serving Endpoints

---

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
