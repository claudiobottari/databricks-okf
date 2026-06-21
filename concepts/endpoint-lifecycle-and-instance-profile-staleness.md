---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d59bbcd8e324e0938a8dc3b237715e5de2d39b4067d2f919090a1a136dd3521e
  pageDirectory: concepts
  sources:
    - add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - endpoint-lifecycle-and-instance-profile-staleness
    - Instance Profile Staleness and Endpoint Lifecycle
    - ELAIPS
  citations:
    - file: add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md
title: Endpoint Lifecycle and Instance Profile Staleness
description: Changes to an instance profile IAM role or deletion of the profile from Databricks settings do not affect running endpoints until the endpoint is updated or restarted.
tags:
  - model-serving
  - operations
  - iam
timestamp: "2026-06-19T08:51:56.012Z"
---

# Endpoint Lifecycle and Instance Profile Staleness

**Endpoint Lifecycle and Instance Profile Staleness** refers to the behavior where a model serving endpoint continues to use an outdated IAM role after its associated instance profile has been modified or deleted in Databricks, persisting the original access configuration until the endpoint is explicitly updated or recreated.

## Overview

When a model serving endpoint is configured with an instance profile, the IAM role associated with that profile is used to authenticate data access to AWS resources. However, changes to the instance profile configuration in Databricks do not automatically propagate to running endpoints. The endpoint retains the original IAM role until it undergoes a lifecycle event such as an update or redeployment. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

For endpoints running on serverless compute, STS temporary security credentials are used to authenticate data access. These credentials cannot bypass any network restrictions, and the staleness behavior described here applies regardless of the compute type. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Staleness Scenarios

### Editing the IAM Role

If a customer edits the instance profile's IAM role from the **Settings** of the Databricks UI, endpoints already running with that instance profile continue to use the old IAM role until the endpoint is updated. Changes to the role are not applied retroactively to active endpoints. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

### Deleting the Instance Profile

If a customer deletes an instance profile from the **Settings** of the Databricks UI and that profile is in use by running endpoints, the running endpoints are not impacted. The endpoints continue to function using the previously assigned IAM role, even though the profile record has been removed from Databricks. ^[add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md]

## Implications

- **Security drift**: Modified or deleted instance profiles may create a gap between the intended access policy and the actual permissions used by running endpoints. Security teams should be aware that changes to instance profiles are not immediately enforced.
- **Operational planning**: Updates to instance profiles require explicit endpoint lifecycle actions (update or recreate the serving endpoint) to take effect.
- **Audit considerations**: The stale role may continue to access AWS resources after the administrator believes access has been revoked, potentially complicating compliance audits.

## Best Practices

1. **Update endpoints after role changes**: After modifying an instance profile's IAM role, update all serving endpoints that use the profile to ensure they adopt the new role.
2. **Coordinate deletions**: Before deleting an instance profile from Databricks, verify that no endpoints are actively using it, or update those endpoints to use a different profile first.
3. **Monitor endpoint configurations**: Regularly review the instance profiles attached to serving endpoints to ensure they reflect the current intended access policies.

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) – The endpoints that consume instance profiles for AWS resource access.
- Instance Profile – The IAM role configuration that provides permissions for AWS resource access.
- STS Temporary Credentials – The credential mechanism used for authentication on serverless compute.
- Model Serving Limits – General limitations applying to model serving endpoints.
- Serving Endpoint API – The REST API used to create and update endpoint configurations, including the `instance_profile_arn` field.

## Sources

- add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md

# Citations

1. [add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws.md](/references/add-an-instance-profile-to-a-model-serving-endpoint-databricks-on-aws-6124b720.md)
