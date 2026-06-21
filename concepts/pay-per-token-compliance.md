---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b5eff945fdcf5a422f49fe746e6b3fba101738528f04ab6e70513ef23b9d8fa9
  pageDirectory: concepts
  sources:
    - foundation-model-apis-compliance-and-security-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pay-per-token-compliance
  citations:
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
title: Pay-per-token Compliance
description: HIPAA compliance only for pay-per-token Foundation Model API workloads; other standards (PCI-DSS, FedRAMP, IRAP, CCCS, UK Cyber Essentials Plus) not supported.
tags:
  - compliance
  - foundation-model-apis
  - pay-per-token
timestamp: "2026-06-19T18:54:07.171Z"
---

# Pay-per-token Compliance

**Pay-per-token Compliance** refers to the security and regulatory compliance standards supported for [Foundation Model APIs](/concepts/foundation-model-apis.md) workloads that are billed on a per-token basis. These workloads operate differently from provisioned throughput deployments and have a more limited set of supported compliance standards.

## Compliance Standards Support

Pay-per-token workloads are **HIPAA compliant** for organizations with the appropriate security profile enabled. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

For customers using the [Compliance Security Profile](/concepts/compliance-security-profile-databricks-on-aws.md), pay-per-token workloads are available only when the compliance standard **HIPAA** or **None** is selected. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

Other compliance standards — including PCI-DSS, FedRAMP, IRAP, CCCS, and UK Cyber Essentials Plus — are **not currently supported** for pay-per-token workloads. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Comparison with Provisioned Throughput

Organizations that require compliance certifications beyond HIPAA should use [Provisioned Throughput](/concepts/provisioned-throughput.md) workloads instead. Provisioned throughput supports the full range of compliance standards available for [Model Serving](/concepts/model-serving.md), including all certifications not available in pay-per-token mode. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Regional Model Availability

Some models are restricted to specific geographic regions based on compliance and infrastructure requirements:

- **US-only models** (e.g., Anthropic Claude Opus 4.1, Meta Llama 3.1 405B Instruct) are supported only in pay-per-token US regions. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]
- **EU and US models** (e.g., OpenAI GPT-5.5 Pro, Anthropic Claude Sonnet 4) are available in pay-per-token EU and US supported regions. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

Workspaces located outside EU or US regions but in a supported Model Serving region can access these models by enabling [Cross-Geo Data Processing](/concepts/cross-geo-data-processing.md). ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Data Processing and Residency

As part of providing the Foundation Model APIs, Databricks may process data outside of the region and cloud provider where the data originated. Workspaces outside US or EU regions must enable cross-Geo data processing to use pay-per-token models. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Provisioned Throughput](/concepts/provisioned-throughput.md)
- [Compliance Security Profile](/concepts/compliance-security-profile-databricks-on-aws.md)
- HIPAA Compliance
- [Model Serving](/concepts/model-serving.md)
- [Cross-Geo Data Processing](/concepts/cross-geo-data-processing.md)
- Foundation Model APIs Rate Limits and Quotas

## Sources

- foundation-model-apis-compliance-and-security-databricks-on-aws.md

# Citations

1. [foundation-model-apis-compliance-and-security-databricks-on-aws.md](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
