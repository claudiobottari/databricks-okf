---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 34c6cc9304c6c97ddc7161be2cf9fe37099c3511d4cbd44dc026f94c8e51a997
  pageDirectory: concepts
  sources:
    - manage-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serving-endpoint-acls
    - SEA
    - GPU Serving Endpoints
    - LLM Serving Endpoints
    - LLM serving endpoints
    - Serving Endpoint
    - Serving Endpoint API
    - Serving Endpoints
    - Serving Endpoints API
    - Serving endpoint
    - Serving endpoints
    - serving endpoint
    - Endpoint ACLs
    - Serving Endpoint Access Control
    - Serving Endpoint Permissions
    - Serving endpoint permissions
    - endpoints
  citations:
    - file: manage-model-serving-endpoints-databricks-on-aws.md
title: Serving Endpoint ACLs
description: Access control management for model serving endpoints, requiring CAN MANAGE permission to modify permissions on an endpoint.
tags:
  - model-serving
  - security
  - access-control
  - databricks
timestamp: "2026-06-19T19:26:26.573Z"
---

# Serving Endpoint ACLs

**Serving Endpoint ACLs** (Access Control Lists) define the permission levels that control access to model serving endpoints on Databricks. These ACLs determine what actions users and service principals can perform on serving endpoints, including querying, managing, and modifying endpoint configurations.

## Permission Levels

The following permission levels are available for model serving endpoints:

| Permission | Capabilities |
|------------|--------------|
| **CAN QUERY** | Allows querying the serving endpoint to get predictions from the deployed model |
| **CAN MANAGE** | Full administrative control, including the ability to modify permissions and manage the endpoint |

^[manage-model-serving-endpoints-databricks-on-aws.md]

## Required Permissions for Operations

Different operations on serving endpoints require specific permission levels:

- **Modifying permissions**: You must have at least the **CAN MANAGE** permission on a serving endpoint to modify its permissions. ^[manage-model-serving-endpoints-databricks-on-aws.md]
- **Viewing permissions**: Users can view the list of permissions on a serving endpoint through the **Serving** UI or using the Permissions API. ^[manage-model-serving-endpoints-databricks-on-aws.md]
- **Adding serverless usage policies**: Only users with **MANAGE** permissions can edit and add a [serverless usage policy](/concepts/serverless-budget-policy.md) to an existing endpoint. ^[manage-model-serving-endpoints-databricks-on-aws.md]

## Managing ACLs

### Using the UI

To view or modify permissions on a serving endpoint:

1. Navigate to the endpoint in the **Serving** UI.
2. Click the **Permissions** button at the top right of the page.
3. Modify permissions as needed.

^[manage-model-serving-endpoints-databricks-on-aws.md]

### Using the API

You can also modify serving endpoint permissions programmatically using the Permissions API. ^[manage-model-serving-endpoints-databricks-on-aws.md]

## Identity and Access Validation

When you update an endpoint, Databricks re-validates the recorded creator's workspace membership and served entity grants. This ensures that any permission changes are properly validated against current workspace state. ^[manage-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model serving endpoints](/concepts/model-serving-endpoint.md) – The core resources controlled by these ACLs
- [Serving endpoint state](/concepts/model-serving-endpoint-status.md) – Endpoint readiness and status indicators
- Serverless usage policies – Budget attribution for serverless endpoints
- Permissions API – Programmatic interface for managing permissions
- [Model server logs](/concepts/model-server-debugging-logs.md) – Debugging resources for endpoint issues
- [Serving endpoint schema](/concepts/serving-endpoint-openapi-schema.md) – OpenAPI specification for endpoint querying

## Sources

- manage-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [manage-model-serving-endpoints-databricks-on-aws.md](/references/manage-model-serving-endpoints-databricks-on-aws-7247257b.md)
