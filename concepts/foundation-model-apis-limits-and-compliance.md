---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ad4e92ba502a868de8163f04cf2c9688784e75901c8aa8db2044b92595f8f353
  pageDirectory: concepts
  sources:
    - model-serving-limits-and-regions-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foundation-model-apis-limits-and-compliance
    - Compliance and Foundation Model APIs Limits
    - FMALAC
    - Compliance Standards for Foundation Model APIs
  citations:
    - file: model-serving-limits-and-regions-databricks-on-aws.md
title: Foundation Model APIs Limits and Compliance
description: Rate limits, quotas, and compliance standards specific to Foundation Model APIs workloads including provisioned throughput, pay-per-token, and batch inference.
tags:
  - model-serving
  - foundation-model-apis
  - limits
  - databricks
timestamp: "2026-06-19T19:44:04.392Z"
---

#Foundation Model APIs Limits and Compliance

**Foundation Model APIs Limits and Compliance** refers to the resource, payload, and security compliance restrictions governing Databricks-hosted foundation model endpoints, including provisioned throughput, pay-per-token, and batch inference workloads. This page summarizes the compliance standards, region availability, and general limitations applicable to Foundation Model APIs. For detailed rate limits and quotas, see the dedicated article on [Foundation Model APIs rate limits and quotas](/concepts/foundation-model-apis-rate-limits.md). ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Compliance Security Profile Standards

Foundation Model APIs workloads—provisioned throughput, pay-per-token, and batch inference using AI Functions and Databricks-hosted models—must meet the supported compliance security profile standards listed in the compliance tables. These standards require that served containers be built within the most recent 30 days. Databricks automatically rebuilds outdated containers on your behalf. If the automated rebuild job fails, an event log message appears with guidance on how to ensure endpoints stay within compliance requirements. ^[model-serving-limits-and-regions-databricks-on-aws.md]

**Note:** Some models require cross-geography routing for provisioned throughput, and therefore are not UK Cyber Essentials Plus compliant. Contact your Databricks account team for more information. ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Region Availability

If your workspace is deployed in a region that supports model serving but is served by a control plane in an unsupported region, the workspace does not support model serving. Attempting to use model serving in such a workspace results in an error message stating that the workspace is not supported. For Databricks-hosted foundation model region availability, see [Foundation models hosted on Databricks](/concepts/foundation-models-apis-on-databricks.md). ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Resource and Payload Limits

Resource and payload limits for custom model and AI agent endpoints are documented in the Model Serving limits and regions page. For Foundation Model APIs and external model resource and payload limits, refer to the dedicated [Foundation Model APIs rate limits and quotas](/concepts/foundation-model-apis-rate-limits.md) article. ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Networking and Security Limitations

Foundation Model APIs endpoints are protected by access control and respect networking-related ingress rules configured on the workspace, such as IP allowlists and PrivateLink. By default, Model Serving does not support PrivateLink to external endpoints; support is evaluated on a per-region basis. Outbound network access can be restricted by configuring network policies. ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs rate limits and quotas](/concepts/foundation-model-apis-rate-limits.md)
- Model Serving limits and regions
- [Compliance security profile](/concepts/compliance-security-profile-databricks-on-aws.md)
- [Provisioned Throughput](/concepts/provisioned-throughput.md)
- [Pay-per-token](/concepts/pay-per-token-serving-mode.md)
- [Batch inference](/concepts/batch-inference-pipelines.md)
- [AI Functions](/concepts/ai-functions.md)
- Databricks Geos

## Sources

- model-serving-limits-and-regions-databricks-on-aws.md

# Citations

1. [model-serving-limits-and-regions-databricks-on-aws.md](/references/model-serving-limits-and-regions-databricks-on-aws-f386cb0e.md)
