---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d5275a4e50f97c3543cbfb90da8092fbe435e0e599140df6c02ad0ffa867a8b
  pageDirectory: concepts
  sources:
    - foundation-model-apis-compliance-and-security-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-container-rebuilding-for-compliance
    - ACRFC
  citations:
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
title: Automatic Container Rebuilding for Compliance
description: Compliance standards require served containers to be rebuilt within the last 30 days; Databricks automatically rebuilds outdated containers, with failure notifications via event logs.
tags:
  - compliance
  - containers
  - automation
timestamp: "2026-06-19T18:54:13.484Z"
---

## Automatic Container Rebuilding for Compliance

**Automatic Container Rebuilding for Compliance** is a process in Databricks [Model Serving](/concepts/model-serving.md) that ensures the container images used for provisioned throughput endpoints are automatically rebuilt every 30 days. This rebuilding is required to satisfy compliance standards that mandate model containers be built within the most recent 30 days. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Compliance Requirement

Several compliance standards—including **HIPAA**, **PCI-DSS**, **FedRAMP**, **IRAP**, **CCCS**, and **UK Cyber Essentials Plus**—require that served containers be built in the most recent 30 days. Databricks automatically rebuilds outdated containers on your behalf to meet this requirement. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Failure Handling

If the automated container rebuild job fails, an event log message like the following is generated:

> "Databricks couldn't complete a scheduled compliance check for model $servedModelName. This can happen if the system can't apply a required update. To resolve, try relogging your model. If the issue persists, contact support@databricks.com."

^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Security Context

Beyond compliance, the 30‑day rebuild cycle also serves a security function. Model Serving does **not** apply security patches to existing model images to avoid destabilizing production deployments. Instead, new model images created from new model versions contain the latest patches. The automatic rebuild every 30 days helps ensure that containers are periodically refreshed with these updated images. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Applicability

Automatic container rebuilding for compliance applies specifically to **provisioned throughput** workloads, which support the full range of compliance standards (HIPAA, PCI-DSS, FedRAMP, etc.). Pay-per-token workloads are HIPAA compliant but currently do not support the other compliance standards; the 30‑day container rebuild requirement applies only to provisioned throughput deployments. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Related Concepts

- [Model Serving](/concepts/model-serving.md)
- [Provisioned Throughput](/concepts/provisioned-throughput.md)
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Compliance Security Profile](/concepts/compliance-security-profile-databricks-on-aws.md)
- HIPAA and other compliance standards (PCI-DSS, FedRAMP, IRAP, CCCS, UK Cyber Essentials Plus)
- Model Deployment and Versioning

### Sources

- foundation-model-apis-compliance-and-security-databricks-on-aws.md

# Citations

1. [foundation-model-apis-compliance-and-security-databricks-on-aws.md](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
