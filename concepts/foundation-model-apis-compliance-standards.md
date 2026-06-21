---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fb2827dbbc335777a235f61f1efa783f62a78f7b7b4c5155cd24572bdb376e0e
  pageDirectory: concepts
  sources:
    - foundation-model-apis-compliance-and-security-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foundation-model-apis-compliance-standards
    - FMACS
    - Foundation Model APIs Compliance and Security
    - Foundation Model APIs compliance and security
  citations:
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
      start: 7
      end: 9
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
      start: 13
      end: 13
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
      start: 15
      end: 15
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
      start: 16
      end: 16
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
      start: 18
      end: 18
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
      start: 22
      end: 22
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
      start: 23
      end: 23
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
      start: 24
      end: 24
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
      start: 25
      end: 25
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
      start: 30
      end: 32
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
      start: 36
      end: 36
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
      start: 38
      end: 38
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
      start: 40
      end: 40
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
      start: 42
      end: 42
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
      start: 46
      end: 46
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
      start: 50
      end: 50
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
      start: 60
      end: 60
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
      start: 77
      end: 77
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
      start: 84
      end: 97
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
      start: 84
      end: 84
title: Foundation Model APIs Compliance Standards
description: Enterprise compliance certifications (HIPAA, PCI-DSS, FedRAMP, IRAP, CCCS, UK Cyber Essentials Plus) supported by Databricks Foundation Model APIs, with availability depending on deployment mode (pay-per-token vs provisioned throughput).
tags:
  - compliance
  - security
  - foundation-model-apis
timestamp: "2026-06-19T10:38:06.696Z"
---

# Foundation Model APIs Compliance Standards

**Foundation Model APIs Compliance Standards** describes the regulatory and security certifications supported by Databricks Foundation Model APIs, which vary by deployment mode — pay-per-token or provisioned throughput. These standards help enterprises meet compliance requirements such as HIPAA, PCI-DSS, FedRAMP, IRAP, CCCS, and UK Cyber Essentials Plus. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md:7-9]

## Compliance Standards Support: Pay-per-token

Pay-per-token workloads are HIPAA compliant. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md:13]

- For customers with the [Compliance Security Profile](/concepts/compliance-security-profile-databricks-on-aws.md) enabled, pay-per-token workloads are available provided that compliance standard **HIPAA** or **None** is selected. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md:15]
- Other compliance standards (PCI-DSS, FedRAMP, IRAP, CCCS, UK Cyber Essentials Plus) are **not** currently supported for pay-per-token workloads. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md:16]

See the Model Serving Limits and Regions page for more details on compliance security profile standards for Foundation Model APIs. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md:18]

## Compliance Standards Support: Provisioned Throughput

Provisioned throughput workloads support the full range of compliance standards available for [Model Serving](/concepts/model-serving.md): ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md:22]

- HIPAA compliance across all regions. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md:23]
- Additional compliance standards (PCI-DSS, FedRAMP, IRAP, CCCS, UK Cyber Essentials Plus) in supported regions. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md:24]
- Recommended for all workloads that require compliance certifications beyond HIPAA. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md:25]

These compliance standards require served containers to be built within the most recent 30 days. Databricks automatically rebuilds outdated containers on your behalf. If that automated job fails, an event log message appears prompting you to relog your model or contact support. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md:30-32]

## Data Processing and Residency

The region and geography where your Foundation Model API requests are processed depends on your workspace region and the specific model being used: ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md:36]

- As part of providing the Foundation Model APIs, Databricks might process your data outside of the region and cloud provider where your data originated. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md:38]
- If your workspace is in a Model Serving region but not a US or EU region, your workspace must be enabled for cross‑Geo data processing. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md:40]
- See [Designated Services](/concepts/databricks-designated-service-with-geos.md) for geographic areas that process pay-per-token and provisioned throughput workloads. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md:42]

## Regional Model Availability

Certain models have regional restrictions based on compliance and infrastructure requirements. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md:46]

### US‑Only Models (Pay-per-token)

The following models are supported only in Foundation Model APIs pay-per-token supported US regions: ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md:50]
- Anthropic Claude Opus 4.1
- Meta Llama 3.1 405B Instruct (retiring February 15, 2026; see Retired Models for migration guidance)
- BGE Large (En)

### EU and US Models (Pay-per-token)

The following models are available in pay-per-token EU and US supported regions: ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md:60]
- OpenAI GPT-5.5 Pro, GPT-5.5, GPT-5.4, GPT-5.4 mini, GPT-5.4 nano, GPT-5.3 Codex, GPT-5.2 Codex, GPT-5.2, GPT-5.1, GPT-5.1 Codex Max, GPT-5.1 Codex Mini, GPT-5, GPT-5 mini, GPT-5 nano
- Anthropic Claude Fable 5, Opus 4.8, Opus 4.7, Opus 4.6, Opus 4.5, Sonnet 4.6, Sonnet 4.5, Haiku 4.5, Sonnet 4

If your workspace is not in an EU or US region but is in a supported Model Serving region, you can enable cross‑Geo data processing to access these models. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md:77]

## Security Best Practices

| Topic | Details |
|-------|---------|
| Access control | Foundation Model API endpoints are protected by workspace‑level access controls. Only workspace admins can modify governance settings. Endpoints respect networking‑related ingress rules configured on the workspace. |
| Network security | Endpoints respect IP allowlists and PrivateLink configurations. You can restrict outbound network access from Model Serving endpoints by configuring network policies. |
| Container security | Model Serving does not provide security patches to existing model images to avoid destabilization of production deployments. New model images created from new model versions contain the latest patches. Containers are automatically rebuilt every 30 days for compliance requirements. |

^[foundation-model-apis-compliance-and-security-databricks-on-aws.md:84-97]

To restrict which Databricks‑hosted foundation models your organization can invoke, see [Foundation Model Unity Catalog Permissions](/concepts/foundation-model-unity-catalog-permissions.md). ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md:84]

## Related Concepts

- [Compliance Security Profile](/concepts/compliance-security-profile-databricks-on-aws.md)
- [Model Serving](/concepts/model-serving.md)
- [Pay-per-token Foundation Model APIs](/concepts/pay-per-token-foundation-model-apis.md)
- [Provisioned Throughput Foundation Model APIs](/concepts/provisioned-throughput-foundation-model-apis.md)
- HIPAA
- Data Residency
- [Regional Model Availability](/concepts/regional-model-availability-us-vs-eu.md)
- Foundation Model APIs Overview
- Foundation Model APIs Rate Limits and Quotas
- Databricks Geos

## Sources

- foundation-model-apis-compliance-and-security-databricks-on-aws.md

# Citations

1. [foundation-model-apis-compliance-and-security-databricks-on-aws.md:7-9](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
2. [foundation-model-apis-compliance-and-security-databricks-on-aws.md:13-13](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
3. [foundation-model-apis-compliance-and-security-databricks-on-aws.md:15-15](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
4. [foundation-model-apis-compliance-and-security-databricks-on-aws.md:16-16](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
5. [foundation-model-apis-compliance-and-security-databricks-on-aws.md:18-18](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
6. [foundation-model-apis-compliance-and-security-databricks-on-aws.md:22-22](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
7. [foundation-model-apis-compliance-and-security-databricks-on-aws.md:23-23](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
8. [foundation-model-apis-compliance-and-security-databricks-on-aws.md:24-24](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
9. [foundation-model-apis-compliance-and-security-databricks-on-aws.md:25-25](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
10. [foundation-model-apis-compliance-and-security-databricks-on-aws.md:30-32](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
11. [foundation-model-apis-compliance-and-security-databricks-on-aws.md:36-36](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
12. [foundation-model-apis-compliance-and-security-databricks-on-aws.md:38-38](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
13. [foundation-model-apis-compliance-and-security-databricks-on-aws.md:40-40](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
14. [foundation-model-apis-compliance-and-security-databricks-on-aws.md:42-42](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
15. [foundation-model-apis-compliance-and-security-databricks-on-aws.md:46-46](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
16. [foundation-model-apis-compliance-and-security-databricks-on-aws.md:50-50](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
17. [foundation-model-apis-compliance-and-security-databricks-on-aws.md:60-60](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
18. [foundation-model-apis-compliance-and-security-databricks-on-aws.md:77-77](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
19. [foundation-model-apis-compliance-and-security-databricks-on-aws.md:84-97](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
20. [foundation-model-apis-compliance-and-security-databricks-on-aws.md:84-84](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
