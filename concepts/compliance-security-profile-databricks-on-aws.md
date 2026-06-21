---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 587ce924b47f292d906a41a9bb566f081e6f77d935b30119feb014469fb18240
  pageDirectory: concepts
  sources:
    - foundation-model-apis-compliance-and-security-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - compliance-security-profile-databricks-on-aws
    - CSP(OA
    - Compliance Security Profile
    - Compliance security profile
    - compliance security profile
  citations:
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
title: Compliance Security Profile (Databricks on AWS)
description: A compliance framework for Databricks Model Serving that enforces standards like HIPAA, PCI-DSS, FedRAMP, IRAP, CCCS, and UK Cyber Essentials Plus, requiring container rebuilds within the last 30 days.
tags:
  - databricks
  - security
  - compliance
timestamp: "2026-06-18T12:24:43.087Z"
---

# Compliance Security Profile (Databricks on AWS)

The **Compliance Security Profile (CSP)** is a Databricks feature that enables workspaces to meet enterprise security and regulatory compliance standards. On AWS, CSP support varies by workload type, particularly for [Foundation Model APIs] and [Model Serving]. The profile governs which compliance standards—such as HIPAA, PCI-DSS, or FedRAMP—are available for a given deployment mode and region. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Compliance Standards Support: Pay-per-token

Pay-per-token Foundation Model API workloads are HIPAA compliant. For customers with the Compliance Security Profile enabled, pay-per-token workloads are available provided that the compliance standard selected for the workspace is **HIPAA** or **None**. Other compliance standards (PCI-DSS, FedRAMP, IRAP, CCCS, UK Cyber Essentials Plus) are not currently supported for pay-per-token workloads. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Compliance Standards Support: Provisioned Throughput

Provisioned throughput Foundation Model API workloads support the full range of compliance standards available for Model Serving:

- HIPAA compliance across all regions.
- Additional compliance standards (PCI-DSS, FedRAMP, IRAP, CCCS, UK Cyber Essentials Plus) in supported regions.

Provisioned throughput is recommended for all workloads that require compliance certifications beyond HIPAA. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Container Compliance Requirements

Compliance standards require served containers to be built within the most recent 30 days. Databricks automatically rebuilds outdated containers on your behalf. If this automated job fails, an event log message appears, such as:

> "Databricks couldn't complete a scheduled compliance check for model `$servedModelName`. This can happen if the system can't apply a required update. To resolve, try relogging your model. If the issue persists, contact support@databricks.com." ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Data Processing and Residency

The region and geography where Foundation Model API requests are processed depends on your workspace region and the specific model being used. As part of providing the Foundation Model APIs, Databricks might process data outside the region and cloud provider where your data originated. If your workspace is in a Model Serving region that is not a US or EU region, cross-Geo data processing must be enabled. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Regional Model Availability

Certain models have regional restrictions based on compliance and infrastructure requirements.

- **US-only models** (e.g., Anthropic Claude Opus 4.1, Meta Llama 3.1 405B Instruct, BGE Large (En)) are supported only in pay-per-token supported US regions. Note that Meta-Llama-3.1-405B-Instruct is retired as of February 15, 2026.
- **EU and US models** (e.g., OpenAI GPT-5.5 Pro, Anthropic Claude Sonnet 4, and many others) are available in pay-per-token EU and US supported regions. Workspaces outside these regions can enable cross-Geo data processing to access these models. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Security Best Practices

Several security controls apply to Foundation Model API endpoints regardless of the compliance standard:

- **Access control**: Endpoints are protected by workspace-level access controls. Only workspace admins can modify governance settings. Endpoints respect networking-related ingress rules configured on the workspace.
- **Network security**: Endpoints respect IP allowlists and [PrivateLink] configurations. Outbound network access from Model Serving endpoints can be restricted by configuring network policies.
- **Container security**: Model Serving does not provide security patches to existing model images to avoid destabilizing production deployments. New model images created from new model versions contain the latest patches. Containers are automatically rebuilt every 30 days for compliance requirements. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

To restrict which Databricks-hosted foundation models your organization can invoke, see [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md). ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Model Serving](/concepts/model-serving.md)
- HIPAA
- PCI-DSS
- FedRAMP
- PrivateLink
- [Unity Catalog](/concepts/unity-catalog.md)
- Serverless Network Security
- [Cross-Geo Data Processing](/concepts/cross-geo-data-processing.md)

## Sources

- foundation-model-apis-compliance-and-security-databricks-on-aws.md

# Citations

1. [foundation-model-apis-compliance-and-security-databricks-on-aws.md](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
