---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bb1b1611d7c161cc344e18d743b04bc0d93f55c577de1f2d8a27bbe18a2d5d8a
  pageDirectory: concepts
  sources:
    - model-serving-limits-and-regions-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-resource-and-payload-limits
    - Payload Limits and Model Serving Resource
    - MSRAPL
    - Resource and Payload Limits
    - Resource and Payload Limits|rate limit
    - Resource and payload limits
    - resource and payload limits
  citations:
    - file: model-serving-limits-and-regions-databricks-on-aws.md
title: Model Serving Resource and Payload Limits
description: Default limits that Databricks Model Serving imposes on custom model and AI agent endpoints to ensure reliable performance.
tags:
  - model-serving
  - limits
  - databricks
timestamp: "2026-06-19T19:43:38.608Z"
---

# Model Serving Resource and Payload Limits

**Model Serving Resource and Payload Limits** are default constraints that Databricks imposes on custom model and AI Agent endpoints to ensure reliable performance. These limits apply only to custom models and AI agents and do not apply to [Foundation Model APIs](/concepts/foundation-model-apis.md) or [External Models](/concepts/external-models.md), which have their own separate rate limits and quotas. ^[model-serving-limits-and-regions-databricks-on-aws.md]

If you have feedback on these limits, you can reach out to your Databricks account team for discussion. ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Scope of Limits

The resource and payload limits documented in this article apply specifically to:

- Custom model endpoints
- AI agent endpoints

For Foundation Model APIs and external model resource and payload limits, refer to Foundation Model APIs Rate Limits and Quotas. ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Security and Networking Limitations

Model Serving endpoints are protected by Access Control for Serving Endpoints and respect networking-related ingress rules configured on the workspace, such as IP allowlists and PrivateLink. ^[model-serving-limits-and-regions-databricks-on-aws.md]

By default, Model Serving does not support PrivateLink to external endpoints. Support for this functionality is evaluated and implemented on a per-region basis. Reach out to your Databricks account team for more information. ^[model-serving-limits-and-regions-databricks-on-aws.md]

Model Serving does not provide security patches to existing model images because of the risk of destabilization to production deployments. A new model image created from a new model version will contain the latest patches. ^[model-serving-limits-and-regions-databricks-on-aws.md]

You can restrict outbound network access from Model Serving endpoints by configuring network policies. See Manage Network Policies for Serverless Egress Control. ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Compliance Security Profile Standards: CPU and GPU Workloads

The following table lists the region availability and supported compliance security profile compliance standards for model serving on CPU and GPU workloads, including external models. ^[model-serving-limits-and-regions-databricks-on-aws.md]

These compliance standards require served containers to be built in the most recent 30 days. Databricks automatically rebuilds outdated containers on your behalf. However, if this automated job fails, an event log message like the following appears:

```
"Databricks couldn't complete a scheduled compliance check for model $servedModelName. This can happen if the system can't apply a required update. To resolve, try relogging your model. If the issue persists, contact support@databricks.com."
```

^[model-serving-limits-and-regions-databricks-on-aws.md]

## Compliance Security Profile Standards: Foundation Model APIs Workloads

The table lists the supported compliance security profile compliance standards for the following Foundation Model APIs workloads:

- Provisioned throughput
- Pay-per-token
- Batch inference using AI Functions and Databricks-hosted models

^[model-serving-limits-and-regions-databricks-on-aws.md]

These compliance standards also require served containers to be built in the most recent 30 days, with the same automatic rebuild mechanism and event log message. ^[model-serving-limits-and-regions-databricks-on-aws.md]

Some models require [Cross Geography Routing](/concepts/cross-geography-routing-for-global-endpoints.md) for provisioned throughput and therefore are not UK Cyber Essentials Plus compliant. Reach out to your Databricks account team for more information. ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Foundation Model APIs Limits

For detailed information about Foundation Model APIs, including resource and payload limits for foundation and external models, see Foundation Model APIs Rate Limits and Quotas. ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Region Availability

If you require an endpoint in an unsupported region, reach out to your Databricks account team. ^[model-serving-limits-and-regions-databricks-on-aws.md]

If your workspace is deployed in a region that supports model serving but is served by a Control Plane in an unsupported region, the workspace does not support model serving. If you attempt to use model serving in such a workspace, you will see an error message stating that your workspace is not supported. ^[model-serving-limits-and-regions-databricks-on-aws.md]

See Model Serving Features Availability for more information on regional availability of each Model Serving feature. For Databricks-hosted foundation model region availability, see [Foundation Models Hosted on Databricks](/concepts/foundation-models-apis-on-databricks.md). ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md)
- AI Agent Framework
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [External Models](/concepts/external-models.md)
- [Provisioned Throughput](/concepts/provisioned-throughput.md)
- [Pay-per-Token](/concepts/pay-per-token-serving-mode.md)
- Batch Inference
- [Serving Endpoint Access Control](/concepts/serving-endpoint-acls.md)
- PrivateLink
- Serverless Egress Control
- Compliance Security Profiles

## Sources

- model-serving-limits-and-regions-databricks-on-aws.md

# Citations

1. [model-serving-limits-and-regions-databricks-on-aws.md](/references/model-serving-limits-and-regions-databricks-on-aws-f386cb0e.md)
