---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3e7d8b8afdd77b939f85faedba42e13724b90e20c871040ccb8bed29d7c87deb
  pageDirectory: concepts
  sources:
    - create-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - creator-identity-for-serving-endpoints
    - CIFSE
  citations:
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
title: Creator Identity for Serving Endpoints
description: The recorded caller identity (typically a service principal) that owns a model serving endpoint, used for Unity Catalog access; it is immutable after creation and must remain a workspace member for the endpoint lifetime.
tags:
  - identity
  - access-control
  - unity-catalog
  - model-serving
timestamp: "2026-06-19T09:36:13.147Z"
---

#Creator Identity for Serving Endpoints

**Creator Identity for Serving Endpoints** refers to the identity — typically a service principal — that is recorded as the creator of a [Model Serving](/concepts/model-serving.md) endpoint when it is provisioned. This identity governs the endpoint's access to [Unity Catalog](/concepts/unity-catalog.md) resources and determines whether configuration updates are allowed. The creator identity is immutable after endpoint creation. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## How Creator Identity Is Recorded

When a custom model serving endpoint is created via the Serving UI, REST API, or MLflow Deployments SDK, Databricks records the calling identity as the endpoint's *creator*. Databricks recommends using a long-lived service principal owned by your team rather than a personal user account, because a personal account might be deactivated or removed from the workspace later, which would prevent updates to the endpoint. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Permissions Required at Creation and Update

To create or update a model serving endpoint, both the caller and the endpoint's recorded creator must:

- Be a member of the workspace.
- Hold the `workspace-access` entitlement.

The recorded creator must also hold specific grants on each served entity (model version or function):

| Grant type | Validated at |
|------------|--------------|
| `EXECUTE` on served model | Endpoint creation or update |
| `EXECUTE` on transitive function dependencies (if any) | Endpoint creation or update |
| Grants required at query time (e.g., read on underlying data) | Not validated upfront; missing grants cause runtime errors |

If any required grant is missing at creation or update time, Databricks rejects the request with `PERMISSION_DENIED`. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Immutability

The recorded creator identity **cannot be changed after endpoint creation**. If the recorded creator is later removed from the workspace or loses required Unity Catalog grants, the only remedy is to delete the endpoint and recreate it under a service principal that has the correct permissions and is a current workspace member. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Impact on Endpoint Updates

Configuration updates and served-entity updates **re-evaluate** the recorded creator's workspace membership and per-served-entity grants. If the recorded creator is no longer a workspace member at the time of an update, the update fails with `PERMISSION_DENIED` — even if the caller initiating the update has valid permissions. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

To avoid update failures:
- Use a long-lived service principal owned by your team as the endpoint creator.
- Do not use a personal user account that might be deactivated or removed from the workspace later.
- The recorded creator must remain a workspace member for the lifetime of the endpoint.

^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Best Practices

- **Choose a durable identity.** A service principal is less likely to be deactivated than a human user.
- **Verify permissions before updates.** Confirm that the recorded creator still holds workspace membership and the required `EXECUTE` grants on served entities before submitting a configuration change.
- **Plan for the future.** If you need to change the creator identity, you must delete and recreate the endpoint, which causes a service interruption.

## Related Concepts

- Service Principal
- [Unity Catalog Permissions](/concepts/unity-catalog-permissions-model.md)
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md)
- [Served Entity Grants](/concepts/served-entity-grants.md)
- Workspace Access Entitlement

## Sources

- create-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-custom-model-serving-endpoints-databricks-on-aws.md](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
