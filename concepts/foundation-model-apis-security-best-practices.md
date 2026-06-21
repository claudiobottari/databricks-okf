---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 99e3320dad3a0692da37a95242171e2293ceb306eb8f7667e3c8520ea4bca25d
  pageDirectory: concepts
  sources:
    - foundation-model-apis-compliance-and-security-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foundation-model-apis-security-best-practices
    - FMASBP
  citations:
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
title: Foundation Model APIs Security Best Practices
description: Security measures for Foundation Model APIs including workspace-level access controls, IP allowlists, PrivateLink configurations, network policy restrictions, and endpoint governance by workspace admins.
tags:
  - security
  - access-control
  - networking
  - foundation-model-apis
timestamp: "2026-06-19T10:38:09.411Z"
---

# Foundation Model APIs Security Best Practices

**Foundation Model APIs Security Best Practices** encompass the compliance standards, data residency controls, network security configurations, and access governance mechanisms that protect Databricks-hosted foundation model endpoints. These practices help organizations meet enterprise security and regulatory requirements when using pay-per-token or provisioned throughput deployments. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Compliance Standards

### Pay-per-token workloads

Pay-per-token workloads are HIPAA compliant. Customers with the Compliance Security Profile enabled can select **HIPAA** or **None** as the compliance standard; other standards (PCI-DSS, FedRAMP, IRAP, CCCS, UK Cyber Essentials Plus) are not currently supported for pay-per-token workloads. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Provisioned throughput workloads

Provisioned throughput workloads support the full range of compliance standards available for [Model Serving](/concepts/model-serving.md): HIPAA compliance across all regions, plus PCI-DSS, FedRAMP, IRAP, CCCS, and UK Cyber Essentials Plus in supported regions. Provisioned throughput is recommended for any workload requiring compliance certifications beyond HIPAA. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

These compliance standards require served containers to have been built within the most recent 30 days. Databricks automatically rebuilds outdated containers on your behalf. If the automated job fails, an event log message appears prompting you to redeploy the model or contact support. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Data Processing and Residency

The region and geography where Foundation Model API requests are processed depends on the workspace region and the specific model used. Databricks may process your data outside of the region and cloud provider where the data originated. If the workspace is in a Model Serving region that is not a US or EU region, the workspace must be enabled for cross-Geo data processing. See Databricks Geos and [Designated Services](/concepts/databricks-designated-service-with-geos.md) for geographic areas that process pay-per-token and provisioned throughput workloads. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Regional Model Availability

Certain models have regional restrictions. For example, Anthropic Claude Opus 4.1, Meta Llama 3.1 405B Instruct, and BGE Large (En) are supported only in US regions for pay-per-token. Many models (e.g., OpenAI GPT-5 series, Anthropic Claude Sonnet 4) are available in EU and US pay-per-token regions. Workspaces outside EU/US regions can enable cross-Geo data processing to access those models. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Security Best Practices

### Access Control

Foundation Model API endpoints are protected by workspace-level access controls. Only workspace admins can modify governance settings for these endpoints. Endpoints respect networking-related ingress rules configured on the workspace. To restrict which Databricks-hosted foundation models your organization can invoke, use foundation model [Unity Catalog permissions](/concepts/unity-catalog-permissions-model.md). ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Network Security

Endpoints respect IP allowlists and PrivateLink configurations. You can restrict outbound network access from Model Serving endpoints by configuring network policies via Manage network policies. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Container Security

Model Serving does not provide security patches to existing model images because that could destabilize production deployments. Instead, new model images created from new model versions contain the latest patches. Containers are automatically rebuilt every 30 days to satisfy compliance requirements. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Related Concepts

- Model Serving limits and regions
- [Foundation Model APIs rate limits and quotas](/concepts/foundation-model-apis-rate-limits.md)
- [Compliance Security Profile](/concepts/compliance-security-profile-databricks-on-aws.md)
- Serverless network security

## Sources

- foundation-model-apis-compliance-and-security-databricks-on-aws.md

# Citations

1. [foundation-model-apis-compliance-and-security-databricks-on-aws.md](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
