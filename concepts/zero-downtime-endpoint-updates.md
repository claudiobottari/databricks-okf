---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 849cc2777f68640edd2f4af4e706bd43af9db3328f6887556a6640cc8aef3514
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - zero-downtime-endpoint-updates
    - ZEU
    - zero-downtime-endpoint-updates-and-maintenance
    - maintenance and Zero-downtime endpoint updates
    - ZEUAM
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: Zero-Downtime Endpoint Updates
description: Databricks performs zero-downtime updates by keeping the existing endpoint configuration active until the new one is ready, with billing for both configurations during transition.
tags:
  - model-serving
  - deployment
  - reliability
timestamp: "2026-06-18T14:57:47.490Z"
---

# Zero-Downtime Endpoint Updates

**Zero-downtime endpoint updates** refer to the deployment strategy used by Databricks [Model Serving](/concepts/model-serving.md) to update a serving endpoint without interrupting ongoing requests. When a new model version or configuration is deployed, Databricks keeps the existing endpoint configuration active until the new one is fully ready, then seamlessly transitions traffic.

## How It Works

Databricks performs a zero-downtime update of endpoints by keeping the existing endpoint configuration active until the new one becomes ready. This approach reduces risk of interruption for endpoints that are in use. During this update process, you are billed for both the old and new endpoint configurations until the transition is complete.^[custom-models-overview-databricks-on-aws.md]

The update applies to any change that triggers a redeployment, such as promoting a new model version, modifying environment dependencies, or updating scaling parameters. The transition is handled transparently; clients do not experience a connectivity drop.

## Billing Considerations

Because both the old and new endpoint configurations run concurrently during the update, you incur costs for both during that overlapping period. Once the new configuration is confirmed healthy and traffic is cut over, the old resources are released and billing for them stops.^[custom-models-overview-databricks-on-aws.md]

## System Maintenance

Databricks occasionally performs zero-downtime system updates and maintenance on existing [Model Serving](/concepts/model-serving.md) endpoints. During maintenance, Databricks reloads models. If a model fails to reload during such maintenance, the endpoint update is marked as failed and the existing endpoint configuration continues to serve requests. Custom models should be robust enough to reload at any time.^[custom-models-overview-databricks-on-aws.md]

## Limitations

- **Deployment duration**: The total time to complete a deployment depends on model size, dependency installation, and provisioning of compute resources. While typical deployments take approximately 10 minutes, complex models may take longer.^[custom-models-overview-databricks-on-aws.md]
- **GPU workloads**: Container image creation for GPU serving takes longer than CPU serving. Very large models may cause deployment timeouts if the container build and model deployment exceed a 60-minute duration.^[custom-models-overview-databricks-on-aws.md]

## Best Practices

- Design custom models to be stateless and able to reload without external dependencies that may fail.
- Validate model dependencies and signatures before deployment to avoid reload failures during updates.
- Monitor endpoint health during and after updates using Serving Endpoint Health Checks.

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – The platform that provides zero-downtime updates for custom and foundation model endpoints.
- [Endpoint Scaling](/concepts/model-serving-endpoint-scaling.md) – How endpoints automatically scale traffic and concurrency.
- [Express Deployments](/concepts/express-deployments-databricks.md) – A faster deployment option for model serving endpoints.
- Route Optimization – Improves performance for high-QPS use cases.

## Sources

- custom-models-overview-databricks-on-aws.md

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
