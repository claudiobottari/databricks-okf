---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 44062723652d817f8b4fbabf9fa3f7af7c55c5067b18e5adafe7ce9056f5a8a1
  pageDirectory: concepts
  sources:
    - create-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serving-endpoint-update-semantics
    - SEUS
  citations:
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
title: Serving Endpoint Update Semantics
description: "How configuration updates to custom model endpoints work: old config keeps serving until new one is ready, concurrent updates are blocked, and updates can be cancelled from the UI."
tags:
  - model-serving
  - endpoint-lifecycle
  - update-strategy
timestamp: "2026-06-19T14:36:32.416Z"
---

# Serving Endpoint Update Semantics

**Serving Endpoint Update Semantics** refers to the behavior and constraints that govern how custom model serving endpoints are modified after their initial creation on Databricks Model Serving. Understanding these semantics is critical for maintaining reliable production deployments and avoiding update failures.

## Overview

After enabling a custom model endpoint, you can update the compute configuration as desired. This is particularly helpful when you need additional resources for your model. Workload size and compute configuration play a key role in what resources are allocated for serving your model. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Update Behavior

### Graceful Transition

When an update is submitted, the existing active configuration continues serving prediction traffic until the new configuration is ready. This ensures zero-downtime updates for production workloads. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Update Locking

While an update is in progress, another update cannot be made. However, you can cancel an in-progress update from the Serving UI. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Failure Handling

Updates to the endpoint configuration can fail. When failures occur, the existing active configuration stays effective as if the update didn't happen. You should verify that the update was successfully applied by reviewing the status of your endpoint. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Modifiable Properties

You can change most aspects of the endpoint configuration, except for the endpoint name and certain immutable properties. Modifiable properties include compute type, scale-out size, traffic routing percentages, and served entity configurations. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Identity and Grant Re-validation

Configuration and served-entity updates re-evaluate the endpoint's recorded creator workspace membership and per-served-entity grants. This is a critical semantic that can cause updates to fail. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Creator Identity Validation

The recorded creator must remain a workspace member for the lifetime of the endpoint. Updates fail with `PERMISSION_DENIED` if the recorded creator is no longer a workspace member, even when the caller has valid permissions. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Grant Validation

The recorded creator must hold the required grants on each served entity. Grants are validated at endpoint creation or update — missing grants cause the request to fail with `PERMISSION_DENIED`. Grants required at query time are not validated upfront; missing grants cause runtime errors when the endpoint serves traffic. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Best Practices

To avoid update failures, follow these recommendations:

- **Use a long-lived service principal** owned by your team as the endpoint creator. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]
- **Do not use a personal user account** that might be deactivated or removed from the workspace later. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]
- **Confirm both membership and grants** still hold before submitting an update. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]
- **Verify the update was applied** by reviewing the endpoint status after submission. ^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The core serving infrastructure for custom models
- Serving Endpoint Identity and Access — Creator identity and grant requirements
- [Serving Endpoint Status](/concepts/model-serving-endpoint-status.md) — How to monitor endpoint health and update progress
- [Serve Multiple Models to Serving Endpoint](/concepts/multi-model-serving-endpoint.md) — Traffic splitting across multiple served entities
- [Route Optimization on Serving Endpoints](/concepts/route-optimization-for-serving-endpoints.md) — Performance optimization for high-throughput endpoints

## Sources

- create-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-custom-model-serving-endpoints-databricks-on-aws.md](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
