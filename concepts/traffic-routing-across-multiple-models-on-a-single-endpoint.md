---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a8f51350053b7c3cc5d1b8925e5f823e533128b9cf5da69e015160d702de43e7
  pageDirectory: concepts
  sources:
    - create-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - traffic-routing-across-multiple-models-on-a-single-endpoint
    - TRAMMOASE
  citations:
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
title: Traffic Routing Across Multiple Models on a Single Endpoint
description: The ability to serve multiple custom models or model versions from a single serving endpoint, with configurable traffic-split percentages between served entities.
tags:
  - model-serving
  - traffic-routing
  - multi-model
timestamp: "2026-06-19T14:37:26.536Z"
---

# Traffic Routing Across Multiple Models on a Single Endpoint

**Traffic Routing Across Multiple Models on a Single Endpoint** refers to the capability to serve multiple models or model versions from a single model serving endpoint while controlling how incoming prediction requests are distributed among them. This approach allows teams to serve different configurations, perform A/B testing, or gradually roll out new model versions without managing separate endpoints.

## Overview

When creating a [custom model serving endpoint](/concepts/custom-model-serving-endpoint-support.md) on Databricks, you can add multiple **served entities** to a single endpoint. Each served entity represents a specific model and version — either from [Unity Catalog](/concepts/unity-catalog.md) or the [Workspace Model Registry](/concepts/workspace-model-registry.md). You configure the percentage of traffic to route to each served entity. The endpoint then distributes incoming prediction requests according to those configured traffic splits.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

This pattern is commonly used for:

- **A/B testing** — Serve two versions of a model simultaneously to compare performance.
- **Canary deployments** — Route a small percentage of traffic to a new model version before full rollout.
- **Multi-model serving** — Offer different models (e.g., for different use cases) from a single endpoint.
- **Incremental upgrades** — Gradually shift traffic from an old version to a new version.

## Configuring Traffic Routing

### Adding Multiple Served Entities

When creating or editing a serving endpoint in the [Serving UI](/concepts/serving-ui.md):

1. After configuring the first served entity (selecting model, version, and compute), click **Add served entity**.
2. Configure the additional served entity with its own model, version, and compute settings.
3. For each served entity, set the **traffic percentage** that the endpoint should route to that model. The percentages across all served entities must sum to 100.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Traffic Splitting

The traffic percentage controls what proportion of incoming requests are sent to each served entity. For example, a 80/20 split sends 80% of requests to one model version and 20% to another. This split is probabilistic, meaning that over many requests the distribution approximates the configured percentages.

### Compute Considerations

Each served entity can have its own compute configuration, including CPU or GPU types and scale-out sizes. This allows you to allocate different resources to different models on the same endpoint.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Advanced Configuration

### Renaming Served Entities

In the advanced configuration section, you can rename each served entity to customize how it appears in the endpoint. This is useful for distinguishing between model versions or configurations when reviewing logs and metrics.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

### Route Optimization

For endpoints with high queries per second (QPS) and throughput requirements, Databricks recommends enabling **route optimization**. Route optimization improves request distribution efficiency across the served entities.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Identity and Access Requirements

When adding multiple served entities to an endpoint, the endpoint's recorded **creator** identity must hold the required grants on **each** served entity. This identity is validated at endpoint creation and update time:

- Grants validated at **creation/update** will cause the request to fail with `PERMISSION_DENIED` if missing.
- Grants required at **query time** are not validated upfront — missing grants cause runtime errors when the endpoint serves traffic.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

The recorded creator must remain a workspace member for the lifetime of the endpoint. Databricks recommends using a long-lived service principal rather than a personal user account that might be deactivated or removed.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Updating Traffic Routing

After an endpoint is created, you can modify the traffic routing by editing the endpoint configuration:

1. From the Serving UI, select **Edit endpoint**.
2. Adjust the traffic percentages for each served entity.
3. Add or remove served entities as needed.

Updates to the endpoint configuration are applied without downtime — the old configuration continues serving traffic until the new configuration is ready. While an update is in progress, another update cannot be made. You can cancel an in-progress update from the Serving UI.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

Configuration and served-entity updates re-validate the recorded creator's workspace membership and per-served-entity grants. Updates fail with `PERMISSION_DENIED` if the recorded creator is no longer a workspace member, even when the caller has valid permissions.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Best Practices

- **Use service principals** as endpoint creators to avoid disruptions from deactivated user accounts.
- **Start with a small traffic percentage** for new model versions (e.g., 5-10%) and gradually increase as confidence grows.
- **Enable inference tables** to capture incoming requests and outgoing responses for monitoring and analysis.
- **Monitor performance metrics** per served entity to compare latency, error rates, and prediction quality across model versions.
- **Keep the endpoint name immutable** — endpoint names cannot be changed after creation and cannot use the `databricks-` prefix (reserved for Databricks preconfigured endpoints).^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) — The core serving infrastructure that supports multi-model endpoints.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — A related technique for comparing model or agent behaviors.
- Model Serving Limits — Constraints on concurrency and compute for serving endpoints.
- [Inference Tables](/concepts/inference-tables.md) — Automatic capture of request/response data for model monitoring.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Continuous quality monitoring for deployed models.

## Sources

- create-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-custom-model-serving-endpoints-databricks-on-aws.md](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
