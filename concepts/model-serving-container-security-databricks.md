---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 121d17fc238588188ff42cdcf48700c58d4d20df1e9b652b8b11cc9b92d8d34e
  pageDirectory: concepts
  sources:
    - foundation-model-apis-compliance-and-security-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-container-security-databricks
    - MSCS(
    - Container Security
  citations:
    - file: foundation-model-apis-compliance-and-security-databricks-on-aws.md
title: Model Serving Container Security (Databricks)
description: Security practices for model serving containers including automatic 30-day rebuilds for compliance, no backporting of security patches to existing images, and patching via new model versions.
tags:
  - databricks
  - security
  - containers
timestamp: "2026-06-18T12:24:30.272Z"
---

Here is the wiki page written in the requested format.

---

**Model Serving Container Security** refers to the security posture, patching strategy, and compliance requirements for the containers that host models on [Databricks Model Serving](/concepts/databricks-model-serving.md). The security model differs depending on whether the endpoint uses a pay-per-token [Foundation Model API](/concepts/foundation-model-apis.md) or a provisioned throughput deployment. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Security Patch Policy

Databricks Model Serving does **not** apply security patches to existing model images in order to avoid destabilizing running production deployments. New model images, created when a new model version is deployed, contain the latest available patches. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Compliance-Driven Container Refresh

For endpoints that require compliance certifications beyond basic security—such as HIPAA, PCI-DSS, FedRAMP, IRAP, CCCS, or UK Cyber Essentials Plus—served containers must have been built within the most recent 30 days. Databricks automatically rebuilds outdated containers on your behalf to meet this requirement. If the automated rebuild job fails, an event log is generated with a message like: ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

> "Databricks couldn't complete a scheduled compliance check for model $servedModelName. This can happen if the system can't apply a required update. To resolve, try relogging your model. If the issue persists, contact support@databricks.com."

## Security Best Practices

### Access Control

Foundation Model API endpoints are protected by workspace-level access controls. Only workspace admins can modify governance settings for these endpoints. The endpoints also respect networking-related ingress rules configured on the workspace. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

### Network Security

Model Serving endpoints respect IP allowlists and PrivateLink configurations. Administrators can further restrict outbound network access from endpoints by configuring network policies. ^[foundation-model-apis-compliance-and-security-databricks-on-aws.md]

## Related Concepts

- Model Serving limits and regions
- [Foundation Model APIs overview](/concepts/foundation-model-apis.md)
- [Unity Catalog](/concepts/unity-catalog.md) — for governing which foundation models users can invoke
- [Compliance security profile](/concepts/compliance-security-profile-databricks-on-aws.md)

## Sources

- foundation-model-apis-compliance-and-security-databricks-on-aws.md

# Citations

1. [foundation-model-apis-compliance-and-security-databricks-on-aws.md](/references/foundation-model-apis-compliance-and-security-databricks-on-aws-837cc200.md)
