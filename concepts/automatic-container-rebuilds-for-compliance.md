---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ba8ac6700332af4de6816efd28a828155b3ad514e31061da4e18da67b95ffccc
  pageDirectory: concepts
  sources:
    - foundation-model-apis-compliance-and-security-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-container-rebuilds-for-compliance
    - ACRFC
  citations:
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
title: Automatic Container Rebuilds for Compliance
description: Compliant Model Serving requires containers built within the last 30 days; Databricks automatically rebuilds outdated containers, with event log notifications if the automated rebuild fails.
tags:
  - compliance
  - container-security
  - model-serving
timestamp: "2026-06-19T10:38:01.111Z"
---

# Automatic Container Rebuilds for Compliance

**Automatic Container Rebuilds for Compliance** is a security mechanism in Databricks Model Serving that periodically rebuilds served model containers to ensure they include the latest security patches and remain compliant with applicable regulatory standards.

## Overview

Model Serving environments host containers that serve machine learning models for inference. To maintain compliance with standards such as HIPAA, PCI-DSS, FedRAMP, IRAP, CCCS, and UK Cyber Essentials Plus, these containers must be built within the most recent 30 days. Databricks automates this process by rebuilding outdated containers on behalf of users. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## How It Works

Databricks automatically rebuilds served containers every 30 days to meet compliance requirements. This ensures that containers contain the latest security patches without requiring manual intervention from users. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Pay-per-Token vs. Provisioned Throughput

Automatic container rebuilds apply to both pay-per-token and provisioned throughput workloads, though the compliance standards supported differ:

| Deployment Mode | Compliance Standards Supported | Container Rebuild Requirement |
|----------------|-------------------------------|-------------------------------|
| Pay-per-token | HIPAA only | 30-day rebuild required for HIPAA compliance |
| Provisioned throughput | HIPAA, PCI-DSS, FedRAMP, IRAP, CCCS, UK Cyber Essentials Plus | 30-day rebuild required for all compliance standards |

^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

For provisioned throughput workloads, Databricks recommends them for all workloads requiring compliance certifications beyond HIPAA. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Container Security Policy

Model Serving does not provide security patches to existing model images to avoid destabilizing production deployments. Instead, new model images created from new model versions contain the latest patches. This design choice means that automatic rebuilds serve as the primary mechanism for keeping production containers up to date with security fixes. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Troubleshooting

If the automated container rebuild job fails, an event log message appears similar to the following:

> Databricks couldn't complete a scheduled compliance check for model $servedModelName. This can happen if the system can't apply a required update. To resolve, try relogging your model. If the issue persists, contact support@databricks.com.

^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

To resolve this issue, users should attempt to relog their model. If the problem persists, they should contact Databricks support. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Best Practices

- **For provisioned throughput workloads**: These support the full range of compliance standards and are recommended when certifications beyond HIPAA are required. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]
- **Monitor for rebuild failures**: Check event logs periodically for messages indicating failed compliance checks, and take corrective action promptly to avoid compliance gaps. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]
- **Use new model versions**: When deploying updated models, containers built from new model versions automatically include the latest patches. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Related Concepts

- Foundation Model APIs Compliance and Security — Broader compliance standards for model serving
- Model Serving Limits and Regions — Regional availability and limits for model serving
- [Container Security](/concepts/model-serving-container-security-databricks.md) — Security practices for model containers
- [Compliance Security Profile](/concepts/compliance-security-profile-databricks-on-aws.md) — Configuration for enabling compliance standards
- [Model Serving](/concepts/model-serving.md) — The underlying serving infrastructure

## Sources

- foundation-model-apis-compliance-and-security-databricks-on-aws.md

# Citations

1. [foundation-model-apis-compliance-and-security-databricks-on-aws.md](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
