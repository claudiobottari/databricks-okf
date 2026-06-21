---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2da17f550e0f975675539facc578ae87171249f2cf399dd79e8f917126d95135
  pageDirectory: concepts
  sources:
    - create-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - creator-identity-for-model-serving
    - CIFMS
  citations:
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
title: Creator Identity for Model Serving
description: The recorded identity (typically a service principal) that created an endpoint, used to access Unity Catalog resources; cannot be changed after creation and must remain a workspace member.
tags:
  - model-serving
  - security
  - identity
timestamp: "2026-06-19T18:00:53.979Z"
---

# Creator Identity for Model Serving

**Creator Identity for Model Serving** refers to the identity recorded as the creator of a [Model Serving](/concepts/model-serving.md) endpoint on Databricks. This identity — typically a Service Principal — is used to access [Unity Catalog](/concepts/unity-catalog.md) resources on behalf of the endpoint and cannot be changed after creation. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Recording and Immutability

When you create a model serving endpoint, Databricks records the calling identity as the endpoint's **creator**. This identity is used to access Unity Catalog resources on behalf of the endpoint and cannot be changed after creation. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

If the recorded creator lacks the required Unity Catalog grants or has been removed from the workspace, you must delete the endpoint and recreate it under a service principal that has the required permissions and is a current workspace member. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Validation During Updates

Configuration and served-entity updates re-evaluate the recorded creator's workspace membership and grants. Updates fail with `PERMISSION_DENIED` if the recorded creator is no longer a workspace member, even when the caller has valid permissions. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Requirements for Endpoint Creation and Updates

To create or update a model serving endpoint, both the caller and the endpoint's recorded creator must:

- Be a member of the workspace.
- Hold the `workspace-access` entitlement.

^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Served Entity Grants

The recorded creator must hold the following grants on each served entity:

- Grants validated at endpoint creation or update cause the request to fail with `PERMISSION_DENIED` if missing.
- Grants required at query time are not validated upfront — missing grants cause runtime errors when the endpoint serves traffic.

If a Unity Catalog model declares transitive function dependencies, the recorded creator also needs `EXECUTE` on those upstream functions. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Best Practices

To avoid update failures:

- Use a long-lived service principal owned by your team as the endpoint creator.
- Do not use a personal user account that might be deactivated or removed from the workspace later.
- The recorded creator must remain a workspace member for the lifetime of the endpoint.

^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The Databricks service for deploying and serving models.
- Service Principal — Recommended identity type for endpoint creation.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that the creator identity accesses.
- [Serving Endpoint Permissions](/concepts/serving-endpoint-acls.md) — Access control for model serving endpoints.
- [Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) — Endpoints that serve custom models.

## Sources

- create-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-custom-model-serving-endpoints-databricks-on-aws.md](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
