---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d3f61cb13c593ce1efc47ea821a42380f907b79dfe221f3721d95a82e3beef92
  pageDirectory: concepts
  sources:
    - foundation-model-apis-compliance-and-security-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pay-per-token-deployment-mode
    - PDM
  citations:
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
title: Pay-per-token deployment mode
description: A consumption-based pricing model for Foundation Model APIs that supports HIPAA compliance but not other standards like PCI-DSS, FedRAMP, IRAP, CCCS, or UK Cyber Essentials Plus.
tags:
  - databricks
  - pricing
  - compliance
timestamp: "2026-06-18T12:24:44.798Z"
---

# Pay-per-token deployment mode

**Pay-per-token deployment mode** is a usage-based pricing model for [Foundation Model APIs](/concepts/foundation-model-apis.md) on Databricks. In this mode, you are billed per token consumed by the model, and the endpoint automatically scales to handle request volume without requiring you to provision dedicated capacity. It is one of two deployment options, the other being [Provisioned throughput deployment mode](/concepts/provisioned-throughput-deployment-mode.md).

## Compliance standards support

Pay-per-token workloads are HIPAA compliant.^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

- For customers with the [Compliance Security Profile](/concepts/compliance-security-profile-databricks-on-aws.md) enabled, pay-per-token workloads are available provided that the compliance standard **HIPAA** or **None** is selected.^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]
- Other compliance standards (PCI-DSS, FedRAMP, IRAP, CCCS, UK Cyber Essentials Plus) are **not** currently supported for pay-per-token workloads.^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

If your workload requires compliance certifications beyond HIPAA, Databricks recommends using [Provisioned throughput deployment mode](/concepts/provisioned-throughput-deployment-mode.md), which supports the full range of compliance standards available for [Model Serving](/concepts/model-serving.md).^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Data processing and residency

The region and geography where your Foundation Model API requests are processed depends on your workspace region and the specific model being used.^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

- Databricks might process your data outside of the region and cloud provider where your data originated.^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]
- If your workspace is in a Model Serving region but not a US or EU region, your workspace must be enabled for cross-Geo data processing.^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]
- See [Designated Services](/concepts/databricks-designated-service-with-geos.md) for geographic areas that process pay-per-token workloads.^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Regional model availability

The set of models available via pay-per-token depends on your workspace region.

| Region | Models | Details |
|--------|--------|---------|
| US-only | Anthropic Claude Opus 4.1, Meta Llama 3.1 405B Instruct, BGE Large (En) | Available only in Foundation Model APIs pay-per-token supported US regions. Note: Meta Llama 3.1 405B Instruct is scheduled for retirement on February 15, 2026. |
| EU and US | OpenAI GPT‑5.5 Pro, GPT‑5.5, GPT‑5.4, GPT‑5.4 mini, GPT‑5.4 nano, GPT‑5.3 Codex, GPT‑5.2 Codex, GPT‑5.2, GPT‑5.1, GPT‑5.1 Codex Max, GPT‑5.1 Codex Mini, GPT‑5, GPT‑5 mini, GPT‑5 nano; Anthropic Claude Fable 5, Claude Opus 4.8, 4.7, 4.6, 4.5, Claude Sonnet 4.6, 4.5, Claude Haiku 4.5, Claude Sonnet 4 | Available in pay-per-token EU and US supported regions. If your workspace is not in an EU or US region but is in a supported Model Serving region, you can enable cross-Geo data processing to access these models. |

^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Security best practices

- **Access control**: Foundation Model API endpoints are protected by workspace-level access controls. Only workspace admins can modify governance settings for these endpoints. Endpoints respect networking-related ingress rules configured on the workspace.^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]
- **Network security**: Endpoints respect IP allowlists and PrivateLink configurations. You can restrict outbound network access from Model Serving endpoints by configuring network policies.^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]
- **Container security**: Model Serving does not provide security patches to existing model images to avoid destabilizing production deployments. New model images created from new model versions contain the latest patches. Containers are automatically rebuilt every 30 days for compliance requirements.^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Related concepts

- [Provisioned throughput deployment mode](/concepts/provisioned-throughput-deployment-mode.md) – Dedicated capacity model with broader compliance certification support.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The service that provides access to Databricks-hosted foundation models.
- [Model Serving](/concepts/model-serving.md) – The underlying serving infrastructure.
- [Compliance Security Profile](/concepts/compliance-security-profile-databricks-on-aws.md) – Security controls and compliance standards for Databricks workspaces.
- HIPAA compliance – Health Insurance Portability and Accountability Act certification.
- [Designated Services](/concepts/databricks-designated-service-with-geos.md) – Geographic areas for data processing.

## Sources

- foundation-model-apis-compliance-and-security-databricks-on-aws.md

# Citations

1. [foundation-model-apis-compliance-and-security-databricks-on-aws.md](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
