---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 47fcd0d90e1fc2120aecd0dcefa8790640e6b7aad194662bcc134217628b9b5b
  pageDirectory: concepts
  sources:
    - foundation-model-apis-compliance-and-security-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provisioned-throughput-deployment-mode
    - PTDM
  citations:
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
title: Provisioned throughput deployment mode
description: A reserved-capacity pricing model for Foundation Model APIs supporting the full range of compliance standards including HIPAA, PCI-DSS, FedRAMP, IRAP, CCCS, and UK Cyber Essentials Plus.
tags:
  - databricks
  - pricing
  - compliance
timestamp: "2026-06-18T12:24:26.363Z"
---

## Provisioned Throughput Deployment Mode

**Provisioned throughput** is a deployment mode for [Foundation Model APIs](/concepts/foundation-model-apis.md) that reserves dedicated compute capacity for serving models. Unlike the [Pay-per-token deployment mode](/concepts/pay-per-token-deployment-mode.md), where costs scale with each request, provisioned throughput provides predictable latency and throughput by allocating fixed infrastructure. This mode is recommended for production workloads that require guaranteed performance and compliance certifications.

### Compliance Standards Support

Provisioned throughput workloads support the full range of compliance standards available for Model Serving:

- **HIPAA** compliance across all regions.
- Additional compliance standards (**PCI-DSS**, **FedRAMP**, **IRAP**, **CCCS**, **UK Cyber Essentials Plus**) in supported regions.
- Recommended for all workloads that require compliance certifications beyond HIPAA. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

These compliance standards require served containers to be built in the most recent 30 days. Databricks automatically rebuilds outdated containers on your behalf. If the automated job fails, an event log message appears, and the remedy is to try relogging your model or contact support. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Data Processing and Residency

The region and corresponding geography where provisioned throughput requests are processed depend on your workspace region and the specific model being used.

- As part of providing the Foundation Model APIs, Databricks might process your data outside of the region and cloud provider where your data originated.
- If your workspace is in a Model Serving region but not a US or EU region, your workspace must be enabled for **cross-Geo data processing**.
- See [Designated Services](https://docs.databricks.com/aws/en/resources/designated-services) for geographic areas that process provisioned throughput workloads. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Regional Model Availability

Certain models have regional restrictions based on compliance and infrastructure requirements. For provisioned throughput, the same model availability tables apply as for pay-per-token, but with the additional compliance coverage noted above.

For detailed model lists by region, refer to the model availability tables in Foundation Model APIs regional availability. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Security Best Practices

Provisioned throughput endpoints inherit the same security controls as other Foundation Model API endpoints:

- **Access control**: Endpoints are protected by workspace-level access controls. Only workspace admins can modify governance settings. Endpoints respect networking-related ingress rules configured on the workspace.
- **Network security**: Endpoints respect IP allowlists and PrivateLink configurations. Outbound network access from Model Serving endpoints can be restricted by configuring network policies.
- **Container security**: Model Serving does not provide security patches to existing model images to avoid destabilizing production deployments. New model images created from new model versions contain the latest patches. Containers are automatically rebuilt every 30 days for compliance requirements. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Related Concepts

- [Pay-per-token deployment mode](/concepts/pay-per-token-deployment-mode.md) — The alternative consumption-based deployment mode.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The API layer that supports both deployment modes.
- [Compliance Security Profile](/concepts/compliance-security-profile-databricks-on-aws.md) — The framework enabling HIPAA and other standards.
- [Model Serving](/concepts/model-serving.md) — The underlying infrastructure for serving models.
- PrivateLink — Network security feature for endpoint isolation.

### Sources

- foundation-model-apis-compliance-and-security-databricks-on-aws.md

# Citations

1. [foundation-model-apis-compliance-and-security-databricks-on-aws.md](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
