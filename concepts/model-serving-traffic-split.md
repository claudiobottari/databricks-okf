---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4f1047d8fbc6cedb4aa77442ad282465201ea95da35e01d0be51e6121f69deef
  pageDirectory: concepts
  sources:
    - upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-traffic-split
    - MSTS
  citations:
    - file: upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md
title: Model Serving Traffic Split
description: Ability to route a fraction of inference traffic to models in Unity Catalog while gradually increasing the proportion for controlled rollouts
tags:
  - model-serving
  - deployment
  - unity-catalog
  - traffic-management
timestamp: "2026-06-19T23:19:24.312Z"
---

# [Model Serving](/concepts/model-serving.md) Traffic Split

**Model Serving Traffic Split** is a feature of [Model Serving](/concepts/model-serving.md) on Databricks that allows you to route a configurable fraction of inference traffic to different model versions or models registered in different catalogs. This capability enables incremental migration, A/B testing, and safe rollout of new models without disrupting existing serving endpoints. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

## Overview

Traffic splitting is particularly useful when migrating from workspace-level models to models in [Unity Catalog](/concepts/unity-catalog.md). Rather than creating a new serving endpoint and switching all consumers at once, you can use traffic split to gradually shift traffic from the existing model to the new [Unity Catalog](/concepts/unity-catalog.md) model. This approach allows you to validate the new model's performance in production before fully committing to it. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

## Use Cases

### Incremental Migration to [Unity Catalog](/concepts/unity-catalog.md)

When upgrading model training and inference workflows to [Unity Catalog](/concepts/unity-catalog.md), Databricks recommends an incremental approach. You create a parallel training, deployment, and inference pipeline that leverages [Models in Unity Catalog](/concepts/models-in-unity-catalog.md). For [Model Serving](/concepts/model-serving.md) specifically, you use the traffic split feature to start routing a small fraction of traffic to [Models in Unity Catalog](/concepts/models-in-unity-catalog.md). As you review the results, you increase the amount of traffic until all traffic is rerouted. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

### A/B Testing and Canary Deployments

Traffic splitting enables you to test new model versions against a subset of production traffic before full rollout. By directing a small percentage of requests to a candidate model, you can monitor performance metrics, latency, and output quality without risking the entire production workload. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

## How It Works

The traffic split feature is configured on an existing serving endpoint. You specify which model versions receive traffic and what percentage of requests each version should handle. The endpoint distributes incoming inference requests according to the configured split ratios. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

## Migration Workflow

1. **Create a parallel pipeline**: Set up a new training and deployment workflow that registers models to [Unity Catalog](/concepts/unity-catalog.md), while keeping the existing workflow running. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]
2. **Configure traffic split**: On your existing serving endpoint, use the traffic split feature to route a small fraction of traffic (e.g., 5-10%) to the [Unity Catalog](/concepts/unity-catalog.md) model version. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]
3. **Monitor and validate**: Review the results from the [Unity Catalog](/concepts/unity-catalog.md) model, comparing performance, accuracy, and latency against the existing model. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]
4. **Gradually increase traffic**: As confidence grows, increase the traffic percentage routed to the [Unity Catalog](/concepts/unity-catalog.md) model. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]
5. **Complete migration**: When all traffic is rerouted to the [Unity Catalog](/concepts/unity-catalog.md) model, downstream consumers can be updated to read from the new endpoint configuration. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

## Requirements

To use traffic splitting with [Models in Unity Catalog](/concepts/models-in-unity-catalog.md), the principal running the workflow must have:
- `USE CATALOG` and `USE SCHEMA` privileges on the [Catalog and Schema](/concepts/catalog-and-schema.md) holding the model
- `EXECUTE` privilege on the registered model to load or deploy it
- Appropriate permissions to create model versions and set aliases

The compute resource specified for the workflow must also have access to [Unity Catalog](/concepts/unity-catalog.md). ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The serving infrastructure that hosts models for real-time inference
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance catalog for managing models and other assets
- [Model Aliases](/concepts/model-aliases.md) — Used to manage production model rollouts (e.g., "Champion" alias)
- Model Deployment Workflow — The process of deploying model versions to serving endpoints
- Batch Inference — Alternative to real-time serving for processing large volumes of data
- Model Versioning — Managing different versions of registered models

## Sources

- upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md](/references/upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws-c3150366.md)
