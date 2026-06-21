---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 92b69eed68cca4e617dcc096ec104344e92a5906a0d4c2c1fbb1891519adf0d0
  pageDirectory: concepts
  sources:
    - create-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - endpoint-configuration-lifecycle
    - ECL
  citations:
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
title: Endpoint Configuration Lifecycle
description: The process of creating, modifying, and updating Databricks model serving endpoints, including immutable properties, in-progress update cancellation, and safe rollback to previous configuration on failure.
tags:
  - model-serving
  - operations
timestamp: "2026-06-19T09:36:18.747Z"
---

# Endpoint Configuration Lifecycle

**Endpoint Configuration Lifecycle** refers to the sequence of states and operations that a [Model Serving](/concepts/model-serving.md) endpoint for [custom models](/concepts/custom-mlflow-pythonmodel.md) goes through from creation through modification, update cancellation, and eventual decommissioning. Understanding this lifecycle helps ensure reliable serving and avoid disruptions during configuration changes.

## Overview

A custom model serving endpoint is created with an initial configuration that specifies compute type, served entities, traffic routing, and optional governance features. After creation, the endpoint enters a **Not Ready** state while infrastructure is provisioned. Once ready, the endpoint’s configuration can be updated to adjust compute resources, GPU workload types, scale-out settings, or served entities. Updates are applied without interrupting the currently serving configuration until the new one is fully ready. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Creation

Endpoints can be created using the **Serving UI**, the **REST API**, or the **MLflow Deployments SDK**. During creation, the caller must provide:

- A unique endpoint name (the `databricks-` prefix is reserved).
- One or more served entities (models from Unity Catalog or the Workspace Model Registry), each with a traffic share percentage.
- A compute type (CPU or GPU) and a [GPU workload types|GPU workload type](/concepts/gpu-workload-types-for-model-serving.md) if applicable.
- A **Compute Scale-out** size — **Small** (0–4 concurrent requests), **Medium** (8–16), or **Large** (16–64) — that determines how many requests the served model can process simultaneously.
- Whether the endpoint should scale to zero when idle (not recommended for production due to cold starts).
- Optional: route optimization, [AI Gateway](/concepts/ai-gateway.md) governance features, and [Inference Tables](/concepts/inference-tables.md) for capturing requests and responses.

After submission, the endpoint’s state displays as **Not Ready** until provisioning completes. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Modification

After an endpoint is active, its configuration can be modified. Most aspects can be changed except the endpoint name and certain immutable properties. Modifications are performed through the same interfaces (UI, API, SDK) and include:

- Changing compute type or GPU workload.
- Adjusting scale-out size or concurrency (for GPU endpoints, concurrency determines replica count: number of replicas = concurrency ÷ 4).
- Adding, removing, or updating served entities and traffic splits.
- Enabling or disabling route optimization and governance features.

While an update is in progress, the previous configuration continues to serve prediction traffic. Another update cannot be started until the current one completes or is cancelled. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Update Failures

Configuration updates can fail. When a failure occurs, the existing active configuration remains effective as though the update never happened. The endpoint’s status should be reviewed to confirm whether the new configuration was successfully applied. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Cancelling an Update

A configuration update that is in progress can be cancelled from the Serving UI by selecting **Cancel update** on the endpoint’s details page. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Identity and Access Considerations

The identity used to create the endpoint (typically a service principal) is recorded as the endpoint’s **creator** and is used to access Unity Catalog resources. **Configuration and served-entity updates re-validate the recorded creator’s workspace membership and grants.** If the creator is no longer a workspace member, updates fail with `PERMISSION_DENIED` even if the caller has valid permissions. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Best Practices

- Use a long-lived service principal owned by your team as the endpoint creator.
- Do not use a personal user account that might be deactivated or removed from the workspace later.
- The recorded creator must remain a workspace member for the lifetime of the endpoint.

To change the creator, the endpoint must be deleted and recreated under a service principal with the required permissions. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Status Monitoring

The endpoint’s current state and configuration version can be reviewed via the Serving UI or APIs. Successful updates transition the endpoint to a **Ready** state serving the new configuration. Failed updates leave the previous configuration active. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Create custom model serving endpoints](/concepts/custom-model-serving-endpoint-support.md) — Detailed workflow for endpoint creation.
- Manage model serving endpoints — Tasks such as viewing status, enabling inference tables, and deleting endpoints.
- [Served entities](/concepts/served-entity-grants.md) — Models and version registered to an endpoint.
- Route optimization — Feature for high-throughput endpoints.
- [GPU workload types](/concepts/gpu-workload-types-for-model-serving.md) — Available GPU compute options per cloud provider.
- [Inference Tables](/concepts/inference-tables.md) — Automatic capture of request and response data.
- Custom models — Models that are not foundation models or feature-serving endpoints.

## Sources

- create-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-custom-model-serving-endpoints-databricks-on-aws.md](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
