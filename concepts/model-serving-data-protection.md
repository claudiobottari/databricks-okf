---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 55903b648355bddc7ae85b6e21a718db55d697c36ed2ba5d9c77464d8f9b80ec
  pageDirectory: concepts
  sources:
    - deploy-models-using-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-data-protection
    - MSDP
  citations:
    - file: deploy-models-using-model-serving-databricks-on-aws.md
title: Model Serving Data Protection
description: Security controls including logical isolation, AES-256 encryption at rest, TLS 1.2+ in transit, and policies against using customer data for model training
tags:
  - security
  - compliance
  - privacy
timestamp: "2026-06-19T10:11:48.501Z"
---

# Model Serving Data Protection

**Model Serving Data Protection** refers to the security controls and data handling policies that safeguard customer data when using [Model Serving](/concepts/model-serving.md) on Databricks. Model Serving is the unified platform for deploying AI and ML models for real-time and batch inference, and it implements multiple layers of security to protect user inputs, outputs, and associated telemetry. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Security Controls

Every customer request to Model Serving is logically isolated, authenticated, and authorized. All data at rest is encrypted using AES-256, and all data in transit is encrypted using TLS 1.2 or higher. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Data Usage and Retention

For all paid accounts, Model Serving does **not** use user inputs submitted to the service or outputs from the service to train any models or improve any Databricks services. ^[deploy-models-using-model-serving-databricks-on-aws.md]

Model Serving retains the following operational data for limited durations:

- **Container build logs**: up to thirty (30) days.
- **Metrics data**: up to fourteen (14) days.

^[deploy-models-using-model-serving-databricks-on-aws.md]

## Foundation Model APIs Data Handling

For Databricks [Foundation Model APIs](/concepts/foundation-model-apis.md), Databricks may temporarily process and store inputs and outputs for the purposes of preventing, detecting, and mitigating abuse or harmful uses. These inputs and outputs are:

- Isolated from those of other customers.
- Stored in the same region as the customer’s workspace for up to thirty (30) days.
- Only accessible for detecting and responding to security or abuse concerns.

^[deploy-models-using-model-serving-databricks-on-aws.md]

Partner model providers that host models accessible through Foundation Model APIs may retain data for safety purposes. This retention relies on automated scanning prior to any limited human review. Models with safety retention requirements are documented on the [supported models page](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models). ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Data Residency

Foundation Model APIs are a [Databricks Designated Service](https://docs.databricks.com/aws/en/resources/designated-services), meaning they adhere to data residency boundaries as implemented by [Databricks Geos](https://docs.databricks.com/aws/en/resources/databricks-geos). ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Related Concepts

- Encryption at Rest — AES-256 encryption for stored data.
- Encryption in Transit — TLS 1.2+ for data in motion.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The interface for querying hosted foundation models.
- [AI Gateway](/concepts/ai-gateway.md) — Centralized governance, usage limits, and monitoring for endpoints.
- Data Residency — Geographic boundaries for data storage and processing.
- [Model Serving](/concepts/model-serving.md) — The overarching serving platform.

## Sources

- deploy-models-using-model-serving-databricks-on-aws.md

# Citations

1. [deploy-models-using-model-serving-databricks-on-aws.md](/references/deploy-models-using-model-serving-databricks-on-aws-7a559b74.md)
