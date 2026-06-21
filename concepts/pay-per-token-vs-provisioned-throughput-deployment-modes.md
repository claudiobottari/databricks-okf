---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f11cd0b5bff2943dbc9ada12124fdf11d9e52a40764dd094aaff66e212178e59
  pageDirectory: concepts
  sources:
    - foundation-model-apis-compliance-and-security-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pay-per-token-vs-provisioned-throughput-deployment-modes
    - PVPTDM
  citations:
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
title: Pay-per-token vs Provisioned Throughput Deployment Modes
description: "Two distinct deployment modes for Foundation Model APIs with different compliance support: pay-per-token supports only HIPAA, while provisioned throughput supports the full range of compliance standards."
tags:
  - compliance
  - deployment
  - foundation-model-apis
timestamp: "2026-06-19T10:37:52.355Z"
---

# Pay-per-token vs Provisioned Throughput Deployment Modes

**Pay-per-token** and **Provisioned Throughput** are two deployment modes for [Foundation Model APIs](/concepts/foundation-model-apis.md) on Databricks. The choice between them affects compliance certifications supported, regional model availability, and the handling of data processing. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Compliance Standards

The compliance standards available for a Foundation Model API workload depend on the deployment mode selected. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Pay-per-token
Pay-per-token workloads are **HIPAA compliant**. For customers with the Compliance Security Profile enabled, pay-per-token workloads are available provided that the compliance standard **HIPAA** or **None** is selected. Other compliance standards (PCI-DSS, FedRAMP, IRAP, CCCS, UK Cyber Essentials Plus) are **not** currently supported for pay-per-token workloads. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Provisioned Throughput
Provisioned throughput workloads support the **full range** of compliance standards available for [Model Serving](/concepts/model-serving.md):
- HIPAA compliance across all regions.
- Additional compliance standards (PCI-DSS, FedRAMP, IRAP, CCCS, UK Cyber Essentials Plus) in supported regions.

Provisioned throughput is **recommended** for all workloads that require compliance certifications beyond HIPAA. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

Containers used for provisioned throughput must be rebuilt every 30 days to maintain compliance. Databricks automatically rebuilds outdated containers on your behalf. If the automated job fails, an event log message appears and manual re-logging of the model may be required. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Regional Model Availability

Model availability can vary by region and deployment mode. For pay-per-token workloads, certain models are restricted to specific geographies:

- **US-only models** (pay-per-token): Anthropic Claude Opus 4.1, Meta Llama 3.1 405B Instruct, BGE Large (En). Note: Meta-Llama-3.1-405B-Instruct will be retired starting February 15, 2026. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]
- **EU and US models** (pay-per-token): A range of OpenAI and Anthropic models are available in pay-per-token EU and US supported regions. If a workspace is not in an EU or US region but is in a supported Model Serving region, cross-Geo data processing can be enabled to access these models. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

The source material does not provide an equivalent regional model list for provisioned throughput, but notes that provisioned throughput workloads support the full compliance range across supported regions.

## Data Processing and Residency

For both deployment modes, the region and geography where requests are processed depends on the workspace region and the specific model used. As part of providing Foundation Model APIs, Databricks might process data outside the region and cloud provider where the data originated. If the workspace is in a Model Serving region but not a US or EU region, it must be enabled for cross-Geo data processing. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Choosing Between Modes

- Use **Pay-per-token** when HIPAA compliance is sufficient and you prefer a consumption-based pricing model.
- Use **Provisioned Throughput** when you need compliance certifications beyond HIPAA (e.g., PCI-DSS, FedRAMP) or when you require guaranteed throughput and capacity.

Both modes share the same network security and access control protections: endpoints respect IP allowlists, PrivateLink configurations, and workspace-level access controls. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Model Serving](/concepts/model-serving.md)
- [Compliance Security Profile](/concepts/compliance-security-profile-databricks-on-aws.md)
- [Cross-Geo Data Processing](/concepts/cross-geo-data-processing.md)
- Foundation Model APIs Rate Limits and Quotas

## Sources

- foundation-model-apis-compliance-and-security-databricks-on-aws.md

# Citations

1. [foundation-model-apis-compliance-and-security-databricks-on-aws.md](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
