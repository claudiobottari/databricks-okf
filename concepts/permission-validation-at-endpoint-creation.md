---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b5a0cc263c2f83df65d304117e33621c3bda0965fc14860e7e3242b28ab95cc4
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - permission-validation-at-endpoint-creation
    - PVAEC
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Permission Validation at Endpoint Creation
description: The endpoint creator's permission to the specified instance profile is validated at endpoint creation time, not at update time.
tags:
  - model-serving
  - security
  - permissions
timestamp: "2026-06-19T13:53:14.744Z"
---

Here is the wiki page for "Permission Validation at Endpoint Creation".

---

## Permission Validation at Endpoint Creation

**Permission Validation at Endpoint Creation** refers to the check that occurs when a user creates a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) on Databricks, specifically when an instance profile is attached to the endpoint configuration. At the moment of creation, the system validates that the endpoint creator has the necessary permissions to use the specified AWS Instance Profile.

### Overview

When a user creates a model serving endpoint and includes an instance profile in the configuration, Databricks validates the creator's permission to that instance profile at endpoint creation time.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md] This validation ensures that only authorized users can associate instance profiles with endpoints, preventing unauthorized access to AWS resources.

### When Validation Occurs

The permission check is performed during endpoint creation rather than at runtime. This applies both when creating endpoints through:

- **The Serving UI:** In the **Advanced configurations** section when setting up a new endpoint.
- **The API:** Using the `instance_profile_arn` field in the `POST /api/2.0/serving-endpoints` request body.

^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Requirements for Successful Validation

For the permission validation to succeed, two conditions must be met:

1. The user must have permission to use the specified instance profile within Databricks.
2. The instance profile's IAM role must have a trust relationship configured for serverless compute. If this trust relationship is missing, the endpoint creation will fail with the error: "IAM role does not have the required trust relationship."^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Related Limitations

Several limitations apply to instance profiles on model serving endpoints that relate to permission management:

- **STStemporary security credentials** are used to authenticate data access and cannot bypass network restrictions.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **Editing the instance profile** IAM role from the Databricks UI does not affect running endpoints — they continue to use the old IAM role until the endpoint is updated.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]
- **Deleting an instance profile** from the Databricks UI does not impact endpoints that are currently running with that profile.^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Additional Resources

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — Overview of creating and managing serving endpoints.
- [AWS Instance Profile Configuration](/concepts/serving-endpoint-rest-api-instance-profile-configuration.md) — Guide for setting up instance profiles in Databricks.
- Serving Endpoint Security — Best practices for securing model serving endpoints.
- [Serverless Compute Trust Policy](/concepts/serverless-compute-trust-relationship-databricks.md) — Required trust relationship setup for serverless compute.

### Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
