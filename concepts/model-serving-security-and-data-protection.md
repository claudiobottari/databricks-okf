---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 38356b8da0002b08a8517b921298add32167baf9be55968ba8dee4b171bf071a
  pageDirectory: concepts
  sources:
    - deploy-models-using-model-serving-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-security-and-data-protection
    - Data Protection and Model Serving Security
    - MSSADP
  citations:
    - file: deploy-models-using-model-serving-databricks-on-aws.md
title: Model Serving Security and Data Protection
description: Security controls for Model Serving including logical isolation, AES-256 encryption at rest, TLS 1.2+ in transit, no training on customer data, container build log retention (30 days), metrics retention (14 days), and abuse monitoring for Foundation Model APIs.
tags:
  - security
  - data-protection
  - databricks
timestamp: "2026-06-18T15:26:56.281Z"
---

# Model Serving Security and Data Protection

**Model Serving Security and Data Protection** encompasses the controls, policies, and practices that Databricks employs to protect data and models deployed via [Model Serving](/concepts/model-serving.md). Model Serving is designed for high-availability, low-latency production use and is protected by multiple layers of security to ensure a secure environment for sensitive workloads.^[deploy-models-using-model-serving-databricks-on-aws.md]

## Security Controls

Databricks implements the following security controls for all Model Serving workloads:

- **Logical isolation**: Every customer request to Model Serving is logically isolated, authenticated, and authorized.^[deploy-models-using-model-serving-databricks-on-aws.md]
- **Encryption**: All data at rest is encrypted using AES-256, and all data in transit is encrypted using TLS 1.2+.^[deploy-models-using-model-serving-databricks-on-aws.md]
- **No training on customer data**: For all paid accounts, Model Serving does **not** use user inputs submitted to the service or outputs from the service to train any models or improve any Databricks services.^[deploy-models-using-model-serving-databricks-on-aws.md]

## Data Protection

### Data Retention

Databricks retains the following data for operational purposes:

- Container build logs are retained for up to thirty (30) days.
- Metrics data are retained for up to fourteen (14) days.

^[deploy-models-using-model-serving-databricks-on-aws.md]

### Abuse Detection for Foundation Model APIs

For [Foundation Model APIs](/concepts/foundation-model-apis.md) as part of providing the service, Databricks may temporarily process and store inputs and outputs for the purposes of preventing, detecting, and mitigating abuse or harmful uses. These inputs and outputs are:

- Isolated from those of other customers.
- Stored in the same region as the workspace for up to thirty (30) days.
- Only accessible for detecting and responding to security or abuse concerns.

^[deploy-models-using-model-serving-databricks-on-aws.md]

### Partner Model Provider Data Retention

Some partner model providers of foundation models may retain data for safety purposes. This retention relies on automated scanning prior to any limited human review. Models with safety retention requirements are noted on the page [Databricks-hosted foundation models available in Foundation Model APIs](/concepts/databricks-model-serving-foundation-model-apis-fmapi.md).^[deploy-models-using-model-serving-databricks-on-aws.md]

Foundation Model APIs is a [Databricks Designated Service](/concepts/databricks-designated-service-with-geos.md) and adheres to data residency boundaries as implemented by Databricks Geos.^[deploy-models-using-model-serving-databricks-on-aws.md]

## Network Security

You can control network access to Model Serving endpoints by configuring network policies. See Manage network policies for serverless egress control.^[deploy-models-using-model-serving-databricks-on-aws.md]

## Security Patches

Model Serving does **not** provide security patches to existing model images because of the risk of destabilization to production deployments. A new model image created from a new model version will contain the latest patches. If you need security updates for a deployed model, you should create and deploy a new model version. Contact your Databricks account team for more information.^[deploy-models-using-model-serving-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – The overall service for deploying AI/ML models.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The API layer for querying Databricks-hosted foundation models.
- [AI Gateway](/concepts/ai-gateway.md) – Centralized governance, usage limits, and quality monitoring for model endpoints.
- [Serverless compute](/concepts/serverless-gpu-compute.md) – The underlying compute model for Model Serving.
- Manage network policies for serverless egress control – How to restrict network access to endpoints.
- [Serving Endpoint ACLs](/concepts/serving-endpoint-acls.md) – Permissions required to access serving endpoints.
- Model Serving limits and regions – Default limits and supported regions.

## Sources

- deploy-models-using-model-serving-databricks-on-aws.md

# Citations

1. [deploy-models-using-model-serving-databricks-on-aws.md](/references/deploy-models-using-model-serving-databricks-on-aws-7a559b74.md)
