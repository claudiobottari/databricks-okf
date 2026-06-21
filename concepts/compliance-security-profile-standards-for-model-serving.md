---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3ad58fc80b5d930f0dc25c4019864d5be6966bd981f9f9069d4f0c0f87e993b1
  pageDirectory: concepts
  sources:
    - model-serving-limits-and-regions-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - compliance-security-profile-standards-for-model-serving
    - CSPSFMS
  citations:
    - file: model-serving-limits-and-regions-databricks-on-aws.md
title: Compliance Security Profile Standards for Model Serving
description: Compliance standards (e.g., UK Cyber Essentials Plus) that apply to served model containers, requiring containers to be rebuilt within the most recent 30 days.
tags:
  - model-serving
  - compliance
  - security
  - databricks
timestamp: "2026-06-19T19:43:58.744Z"
---

# Compliance Security Profile Standards for Model Serving

**Compliance Security Profile Standards for Model Serving** define the regulatory and security compliance certifications that Databricks Model Serving endpoints support across different workload types, including CPU, GPU, external models, and Foundation Model APIs. These standards ensure that model serving infrastructure meets specific security and compliance requirements for regulated industries. ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Overview

Databricks Model Serving supports compliance security profile standards for both CPU and GPU workloads, as well as for Foundation Model APIs workloads. The available compliance standards vary by region and workload type. Workspaces must be deployed in supported regions to utilize compliant model serving endpoints. If a workspace is in an unsupported region, model serving will not function and an error message is displayed. ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Container Compliance Requirements

Compliance security profile standards require served containers to be built within the most recent 30 days. Databricks automatically rebuilds outdated containers on behalf of users to maintain compliance. However, if this automated rebuild job fails, an event log message appears providing guidance to resolve the issue. The message advises users to try relogging their model and, if the problem persists, to contact Databricks support. ^[model-serving-limits-and-regions-databricks-on-aws.md]

### Automatic Container Updates

The automated compliance maintenance process ensures that containers remain within the 30-day build window without manual intervention. If the automated job encounters a failure, the following event log message is generated: ^[model-serving-limits-and-regions-databricks-on-aws.md]

`"Databricks couldn't complete a scheduled compliance check for model $servedModelName. This can happen if the system can't apply a required update. To resolve, try relogging your model. If the issue persists, contact support@databricks.com."`

## Supported Workload Types

### CPU and GPU Workloads (including External Models)

Compliance security profile standards are available for custom model endpoints, AI agent endpoints, and external model endpoints running on CPU or GPU infrastructure. The specific compliance standards supported depend on the region where the workspace is deployed. ^[model-serving-limits-and-regions-databricks-on-aws.md]

### Foundation Model APIs Workloads

Compliance security profile standards also apply to Foundation Model APIs workloads, including:
- [Provisioned Throughput](/concepts/provisioned-throughput.md) endpoints
- Pay-per-token endpoints
- Batch inference using [AI Functions](/concepts/ai-functions.md) and Databricks-hosted models

Some models require [cross geography routing](/concepts/cross-geography-routing-for-global-endpoints.md) for provisioned throughput and therefore are not compliant with certain standards (such as UK Cyber Essentials Plus) in specific regions. Users should contact their Databricks account team for more information on regional compliance variations. ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Networking and Security Limitations

Model Serving endpoints are protected by access control mechanisms and respect networking-related ingress rules configured on the workspace, including IP allowlists and PrivateLink. By default, Model Serving does not support PrivateLink to external endpoints, with support evaluated and implemented on a per-region basis. Additionally, Model Serving does not provide security patches to existing model images due to the risk of destabilizing production deployments — new model versions must be created to receive the latest patches. ^[model-serving-limits-and-regions-databricks-on-aws.md]

Outbound network access from Model Serving endpoints can be restricted by configuring network policies for serverless egress control. ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Region Availability

Compliance security profile standards are available only in regions where Databricks Model Serving is deployed. If a workspace is served by a control plane in an unsupported region, model serving is not supported even if the workspace itself is in a supported region. Users can refer to Model Serving features availability documentation for detailed regional availability information. ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The core service for deploying and serving models on Databricks
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — API-based access to Databricks-hosted foundation models
- Serverless Egress Control — Network policies for restricting outbound traffic
- [Serving Endpoints](/concepts/serving-endpoint-acls.md) — The endpoints through which models are served
- Access Control for Serving Endpoints — Authorization mechanisms for endpoint access

## Sources

- model-serving-limits-and-regions-databricks-on-aws.md

# Citations

1. [model-serving-limits-and-regions-databricks-on-aws.md](/references/model-serving-limits-and-regions-databricks-on-aws-f386cb0e.md)
