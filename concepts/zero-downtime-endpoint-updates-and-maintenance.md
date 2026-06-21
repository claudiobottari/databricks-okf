---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5d31c6c8f853852dbbd05c16cb47060982bb4c5a6dc8746b5970d1efa1039351
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - zero-downtime-endpoint-updates-and-maintenance
    - maintenance and Zero-downtime endpoint updates
    - ZEUAM
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: Zero-downtime endpoint updates and maintenance
description: Databricks keeps existing endpoints serving while new configurations deploy, then performs zero-downtime transitions; during maintenance models are reloaded, and failures cause rollback ensuring no service interruption.
tags:
  - model-serving
  - reliability
  - deployment
timestamp: "2026-06-19T18:03:45.602Z"
---

# Zero-downtime endpoint updates and maintenance

**Zero-downtime endpoint updates and maintenance** is a feature of Databricks Model Serving for Custom Models that allows endpoints to be updated or undergo system maintenance without interrupting service. During an update or maintenance event, the existing endpoint configuration continues to serve requests until the new configuration is fully ready. ^[custom-models-overview-databricks-on-aws.md]

## How it works

When a custom model serving endpoint is updated – for example, to deploy a new model version – Databricks keeps the existing endpoint configuration running and continues to handle incoming requests. The update process builds and provisions the new endpoint configuration in the background. Once the new configuration is ready, traffic is transitioned seamlessly to it. This approach reduces the risk of interruption for endpoints that are in active use. ^[custom-models-overview-databricks-on-aws.md]

While both the old and new configurations are active during the transition, you are billed for both until the old configuration is fully decommissioned. ^[custom-models-overview-databricks-on-aws.md]

## System updates and maintenance

In addition to user-initiated updates, Databricks performs occasional zero-downtime system updates and maintenance on existing Model Serving endpoints. During maintenance, Databricks reloads the model from its registered MLflow artifact. ^[custom-models-overview-databricks-on-aws.md]

If a model fails to reload during maintenance, the endpoint update is marked as failed. The existing endpoint configuration remains in place and continues to serve requests. To avoid service disruption, you should make sure that your custom models are robust and are able to reload successfully at any time. ^[custom-models-overview-databricks-on-aws.md]

## Applicability

Zero-downtime endpoint updates and maintenance apply only to Custom Models served through Model Serving. They do not apply to endpoints that serve [Foundation Model APIs](/concepts/foundation-model-apis.md) or [External Models](/concepts/external-models.md). ^[custom-models-overview-databricks-on-aws.md]

## Implications for model robustness

Because models can be reloaded at any time during maintenance, custom models must be self-contained and reliably loadable. This includes ensuring that all dependencies (Python packages, system libraries, code dependencies) are correctly specified in the MLflow model artifact and that the model can be deserialized and initialised without errors. ^[custom-models-overview-databricks-on-aws.md]

For guidance on packaging dependencies, see [Deployment Container and Dependencies](/concepts/deployment-container-and-dependencies.md) and the [Pre-deployment Validation for Model Serving](/concepts/pre-deployment-validation-for-model-serving.md) documentation. ^[custom-models-overview-databricks-on-aws.md]

## Related concepts

- Custom Models – The type of models that support zero-downtime updates.
- [Model Serving](/concepts/model-serving.md) – The service that provides endpoint hosting.
- [Endpoint creation and update expectations](/concepts/endpoint-creation-update-and-maintenance-expectations.md) – Broader timeline and scaling expectations for endpoints.
- [Endpoint scaling expectations](/concepts/model-serving-endpoint-scaling.md) – How endpoints scale to handle traffic.
- [GPU workload limitations](/concepts/gpu-workload-limitations-in-model-serving.md) – Additional considerations for GPU-backed endpoints.

## Sources

- custom-models-overview-databricks-on-aws.md

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
