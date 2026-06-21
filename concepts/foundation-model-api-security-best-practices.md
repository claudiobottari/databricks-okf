---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5a9e0676d2340cdd1f26883e1ec3c79f405c490237bd68a281209923827f0ded
  pageDirectory: concepts
  sources:
    - foundation-model-apis-compliance-and-security-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foundation-model-api-security-best-practices
    - FMASBP
  citations:
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
title: Foundation Model API Security Best Practices
description: Security measures include workspace-level access controls, IP allowlists, PrivateLink, network policies, and automatic container rebuilding every 30 days for compliance.
tags:
  - security
  - networking
  - foundation-model-apis
timestamp: "2026-06-19T18:54:12.020Z"
---

# Foundation Model API Security Best Practices

**Foundation Model API Security Best Practices** encompasses the governance, access control, network security, and compliance configurations that organizations should implement when using [Foundation Model APIs](/concepts/foundation-model-apis.md) on Databricks. These practices help protect sensitive data, restrict model access, and meet enterprise regulatory requirements.

## Access Control

Foundation Model API endpoints are protected by workspace-level access controls. Only workspace admins can modify governance settings for Foundation Model API endpoints. Endpoints respect networking-related ingress rules configured on the workspace. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

To restrict which Databricks-hosted foundation models your organization can invoke, configure [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md). This allows you to control model access at the catalog level. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Network Security

Endpoints respect IP allowlists and PrivateLink configurations, enabling organizations to restrict access to trusted networks only. You can also restrict outbound network access from [Model Serving](/concepts/model-serving.md) endpoints by configuring network policies. See Manage Network Policies for detailed configuration guidance. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Compliance Standards Support

Both deployment models—pay-per-token and provisioned throughput—support compliance standards, but with different coverage:

- **Pay-per-token workloads** are HIPAA compliant. For customers with the Compliance Security Profile enabled, pay-per-token workloads are available provided that compliance standard **HIPAA** or **None** is selected. Other compliance standards (PCI-DSS, FedRAMP, IRAP, CCCS, UK Cyber Essentials Plus) are not currently supported for pay-per-token workloads. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]
- **Provisioned throughput workloads** support the full range of compliance standards available for Model Serving, including HIPAA compliance across all regions and additional standards (PCI-DSS, FedRAMP, IRAP, CCCS, UK Cyber Essentials Plus) in supported regions. Provisioned throughput is recommended for all workloads that require compliance certifications beyond HIPAA. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Compliance Container Rebuilding

Compliance standards require served containers to be built in the most recent 30 days. Databricks automatically rebuilds outdated containers on your behalf. However, if this automated job fails, an event log message appears: `"Databricks couldn't complete a scheduled compliance check for model $servedModelName. This can happen if the system can't apply a required update. To resolve, try relogging your model. If the issue persists, contact support@databricks.com."` ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Container Security

Model Serving does not provide security patches to existing model images to avoid destabilizing production deployments. New model images created from new model versions will contain the latest patches. Containers are automatically rebuilt every 30 days for compliance requirements. Organize your deployment lifecycle to regularly serve new model versions to benefit from the latest security patches. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Data Processing and Residency

As part of providing the Foundation Model APIs, Databricks might process your data outside of the region and cloud provider where your data originated. The region and corresponding geography where your Foundation Model API requests are processed depends on your workspace region and the specific model being used. If your workspace is in a Model Serving region but not a US or EU region, your workspace must be enabled for [Cross-Geo Data Processing](/concepts/cross-geo-data-processing.md). ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

Certain models have regional restrictions. For example, models like Anthropic Claude Opus 4.1 and Meta Llama 3.1 405B Instruct are supported only in US regions for pay-per-token workloads. Verify [Regional Model Availability](/concepts/regional-model-availability-us-vs-eu.md) before deploying. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Model Serving](/concepts/model-serving.md)
- PrivateLink
- IP Allowlists
- [Compliance Security Profile](/concepts/compliance-security-profile-databricks-on-aws.md)
- [Cross-Geo Data Processing](/concepts/cross-geo-data-processing.md)
- [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md)
- Manage Network Policies

## Sources

- foundation-model-apis-compliance-and-security-databricks-on-aws.md

# Citations

1. [foundation-model-apis-compliance-and-security-databricks-on-aws.md](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
