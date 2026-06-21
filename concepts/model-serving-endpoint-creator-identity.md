---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 82e290af3058b6a8d4ca5cdda5ecf8880d2ebfb3b832d37b17ba4f70fb8878a3
  pageDirectory: concepts
  sources:
    - create-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-creator-identity
    - MSECI
    - Endpoint Creator Identity
  citations:
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
title: Model Serving Endpoint Creator Identity
description: The calling identity recorded as the endpoint's creator, used for Unity Catalog access, immutable after creation, and continuously validated for workspace membership and grants.
tags:
  - model-serving
  - identity-and-access
  - Unity-Catalog
timestamp: "2026-06-19T14:36:28.752Z"
---

---
title: Model Serving Endpoint Creator Identity
summary: Databricks records the calling identity as the endpoint's permanent creator, which is used to access Unity Catalog resources and cannot be changed after creation.
sources:
  - create-custom-model-serving-endpoints-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:22:23.928Z"
updatedAt: "2026-06-18T11:22:23.928Z"
tags:
  - model-serving
  - security
  - identity
aliases:
  - model-serving-endpoint-creator-identity
  - MSECI
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Model Serving Endpoint Creator Identity

**Model Serving Endpoint Creator Identity** refers to the Databricks user or service principal recorded as the creator of a [Model Serving](/concepts/model-serving.md) endpoint. This identity is used to access [Unity Catalog](/concepts/unity-catalog.md) resources on behalf of the endpoint and has significant implications for endpoint management, updates, and long-term maintainability.

## Recording of Creator Identity

When you create a model serving endpoint, Databricks records the calling identity as the endpoint's **creator**. This identity — typically a service principal — is used to access Unity Catalog resources on behalf of the endpoint. Crucially, this identity cannot be changed after the endpoint is created. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Requirements for Endpoint Creation

To create or update a model serving endpoint, both the caller and the endpoint's recorded creator must:

- Be a member of the workspace.
- Hold the `workspace-access` entitlement. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Impact on Endpoint Operations

### Resource Access

The recorded creator identity is used to access Unity Catalog resources — specifically, the registered model versions served by the endpoint — on behalf of the endpoint. The creator must hold the following grants on each served entity: ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

| Grant Type | Validation Timing |
|------------|-------------------|
| Grants validated at creation or update | Checked upfront; missing grants cause `PERMISSION_DENIED` |
| Grants required at query time | Not validated upfront; missing grants cause runtime errors when the endpoint serves traffic |

If a Unity Catalog model declares transitive function dependencies, the recorded creator also needs `EXECUTE` on those upstream functions. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Update Failures Due to Creator Status

Configuration and served-entity updates re-evaluate the recorded creator's workspace membership and per-served-entity grants. Updates fail with `PERMISSION_DENIED` if the recorded creator is no longer a workspace member, even when the caller has valid permissions. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

If the recorded creator lacks the required Unity Catalog grants or has been removed from the workspace, you cannot simply change the creator — you must delete the endpoint and recreate it under a service principal that has the required permissions and is a current workspace member. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Best Practices

To avoid update failures due to creator identity issues, follow these recommendations: ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

- **Use a long-lived service principal owned by your team** as the endpoint creator rather than a personal user account.
- **Do not use a personal user account** that might be deactivated or removed from the workspace later.
- **Ensure the recorded creator remains a workspace member** for the lifetime of the endpoint.

These practices are critical because the creator identity cannot be changed after endpoint creation — the only remedy for an invalid creator is to delete and recreate the endpoint. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The Databricks service for deploying and querying models
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer used by endpoints for resource access
- Service Principal — The recommended identity type for endpoint creators
- Managed permissions on serving endpoints — Access control for who can query or manage endpoints
- [Foundation Model Serving Endpoints](/concepts/foundation-model-serving-endpoints.md) — A separate endpoint type for generative AI models

## Sources

- create-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-custom-model-serving-endpoints-databricks-on-aws.md](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
