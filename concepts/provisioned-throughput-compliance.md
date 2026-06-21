---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2842a36f6867de683f4eb48da63d2d23546a948c4a08d7eb42657de1209d5dd3
  pageDirectory: concepts
  sources:
    - foundation-model-apis-compliance-and-security-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provisioned-throughput-compliance
    - PTC
  citations:
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
title: Provisioned Throughput Compliance
description: Provisioned throughput workloads support the full range of compliance standards (HIPAA, PCI-DSS, FedRAMP, IRAP, CCCS, UK Cyber Essentials Plus) in supported regions.
tags:
  - compliance
  - foundation-model-apis
  - provisioned-throughput
timestamp: "2026-06-19T18:53:57.424Z"
---

# Provisioned Throughput Compliance

**Provisioned Throughput Compliance** refers to the set of compliance standards, security controls, and data residency capabilities that are available when using Databricks Foundation Model APIs in provisioned throughput mode. This mode supports a broader range of regulatory certifications than pay-per-token workloads, making it suitable for enterprise workloads that require strict compliance adherence. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Compliance Standards Support

Provisioned throughput workloads support the full range of compliance standards available for [Model Serving](/concepts/model-serving.md) on Databricks. The following certifications are available:

- **HIPAA** – supported across all regions.
- **PCI-DSS, FedRAMP, IRAP, CCCS, UK Cyber Essentials Plus** – supported in regions where those standards are enabled for Model Serving.

For workloads that require compliance certifications beyond HIPAA, provisioned throughput is the recommended deployment mode. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

In contrast, [Pay-per-token](/concepts/pay-per-token-serving-mode.md) workloads are only HIPAA-compliant (when the Compliance Security Profile is enabled with HIPAA or None selected) and do not support the additional standards. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Container Compliance Requirements

To maintain compliance, served containers must be built within the most recent 30 days. Databricks automatically rebuilds containers that are outdated to meet this requirement. If the automated rebuild job fails, an event log message appears:

> "Databricks couldn't complete a scheduled compliance check for model $servedModelName. This can happen if the system can't apply a required update. To resolve, try relogging your model. If the issue persists, contact support@databricks.com."

^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Data Processing and Residency

For provisioned throughput workloads, the region where your requests are processed depends on the workspace region and the specific model. Databricks may process data outside of the region and cloud provider where the data originated. Workspaces in supported Model Serving regions outside the US or EU must enable [Cross-Geo Data Processing](/concepts/cross-geo-data-processing.md) to use the APIs. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

See the [Designated Services](/concepts/databricks-designated-service-with-geos.md) documentation for geographic areas that process provisioned throughput workloads. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Regional Model Availability

Certain models have regional restrictions tied to compliance and infrastructure requirements. For provisioned throughput, the available models and their regional support are listed in the Foundation Model APIs documentation. Notably, models such as Meta Llama 3.1 405B Instruct and BGE Large (En) are limited to US regions when accessed via pay-per-token; provisioned throughput may have different constraints. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Security Best Practices

Provisioned throughput endpoints inherit the security controls of Model Serving:

- **Access control** – endpoints are protected by workspace-level access controls; only workspace admins can modify governance settings; endpoints respect networking ingress rules.
- **Network security** – endpoints respect IP allowlists and PrivateLink configurations. Outbound network access can be restricted via network policies.
- **Container security** – existing model images do not receive security patches to avoid destabilizing production deployments. New model versions include the latest patches. Containers are automatically rebuilt every 30 days for compliance. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Pay-per-token](/concepts/pay-per-token-serving-mode.md)
- [Model Serving](/concepts/model-serving.md)
- HIPAA
- PCI-DSS
- FedRAMP
- [Compliance Security Profile](/concepts/compliance-security-profile-databricks-on-aws.md)
- [Cross-Geo Data Processing](/concepts/cross-geo-data-processing.md)
- PrivateLink

## Sources

- foundation-model-apis-compliance-and-security-databricks-on-aws.md

# Citations

1. [foundation-model-apis-compliance-and-security-databricks-on-aws.md](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
