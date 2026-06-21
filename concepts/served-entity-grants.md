---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 40af3c426d80a5bf1b99ea0a11d29b8efb32f92bfa18f7739d9a3018f18e6301
  pageDirectory: concepts
  sources:
    - create-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - served-entity-grants
    - SEG
    - Served entities
  citations:
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
title: Served Entity Grants
description: Unity Catalog grants (READ, EXECUTE) that the endpoint creator must hold on each served model and its transitive function dependencies, validated at endpoint creation and update time.
tags:
  - unity-catalog
  - model-serving
  - authorization
timestamp: "2026-06-19T18:01:06.794Z"
---

# Served Entity Grants

**Served Entity Grants** are the [Unity Catalog](/concepts/unity-catalog.md) permissions that a [Model Serving Endpoint](/concepts/model-serving-endpoint.md)’s recorded creator must hold on each model or other entity served by the endpoint. These grants are validated at endpoint creation and update time, and missing grants cause the request to fail with a `PERMISSION_DENIED` error. Grants required at query time are not validated upfront — missing grants cause runtime errors when the endpoint attempts to serve traffic. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Identity and Creator

When you create an endpoint, Databricks records the calling identity as the endpoint’s **creator**. This identity — typically a service principal — is used to access Unity Catalog resources on behalf of the endpoint and cannot be changed after creation. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

If the recorded creator lacks the required Unity Catalog grants or has been removed from the workspace, you must delete the endpoint and recreate it under a service principal that has the required permissions and is a current workspace member. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Grant Validation Timing

Grants are validated at different points in the endpoint lifecycle: ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

- **At endpoint creation or update**: Missing grants cause the request to fail immediately with `PERMISSION_DENIED`.
- **At query time**: Grants required for serving traffic are not validated upfront. Missing grants cause runtime errors when the endpoint attempts to serve requests.

Configuration and served-entity updates re-evaluate the recorded creator’s workspace membership and grants. Updates fail with `PERMISSION_DENIED` if the recorded creator is no longer a workspace member, even when the caller has valid permissions. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Required Grants

The recorded creator must hold the necessary Unity Catalog permissions on each served entity. If a Unity Catalog model declares transitive function dependencies (such as calls to other models or functions), the recorded creator also needs `EXECUTE` on those upstream functions. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

> **Note:** The source material does not enumerate an exhaustive list of all required grants. The `EXECUTE` permission is explicitly mentioned in the context of transitive function dependencies. Additional grants may be required depending on the served entity type and configuration.

## Best Practices

To avoid update failures related to served entity grants: ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

- Use a long-lived service principal owned by your team as the endpoint creator.
- Do not use a personal user account that might be deactivated or removed from the workspace later.
- The recorded creator must remain a workspace member for the lifetime of the endpoint.

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The endpoints that serve custom models
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that manages model permissions
- Service Principals — Recommended identity type for endpoint creators
- Model Serving Permissions — Access control for managing endpoints

## Sources

- create-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-custom-model-serving-endpoints-databricks-on-aws.md](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
