---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ce9a678c6206c4b89ff9c28e14dbcfefd5369749aa635cb6b63bda8667407eb5
  pageDirectory: concepts
  sources:
    - opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-vs-classic-compute-for-secureconnect
    - SVCCFS
  citations:
    - file: opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md
title: Serverless vs Classic Compute for SecureConnect
description: Serverless compute recipients do not need egress firewall configuration for SecureConnect, while classic compute and open recipients must allowlist inbound IPs
tags:
  - databricks
  - compute
  - networking
  - delta-sharing
timestamp: "2026-06-19T19:50:45.643Z"
---

## Serverless vs Classic Compute for SecureConnect

When accessing shares through **OpenSharing SecureConnect**, the compute type used by the recipient determines the firewall configuration required. The key difference between serverless and classic compute lies in whether the recipient must manually allowlist Databricks inbound IP addresses in their egress firewall. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

### Classic Compute Recipients

Recipients using classic compute (and open recipients) **must** configure their egress firewall to allowlist the Databricks inbound IP addresses for the provider’s cloud and region. This allowlisting is required regardless of the cloud the recipient is on — the IP addresses to allowlist are based on the provider’s deployment, not the recipient’s. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

Classic compute recipients also face a limitation regarding mutual TLS (mTLS): mTLS is **not enabled** for these recipients when accessing SecureConnect-enabled shares. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

### Serverless Compute Recipients

Recipients on serverless compute **do not need** to configure their egress firewall to access SecureConnect. Databricks routes serverless traffic to SecureConnect internally, bypassing the need for manual IP allowlisting. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

However, serverless recipients face their own limitation: serverless Databricks recipients using a Databricks-to-Open credential in the same region as the provider are **not supported**. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

### Summary Comparison

| Aspect | Classic Compute | Serverless Compute |
|--------|----------------|-------------------|
| Egress firewall configuration | Must allowlist Databricks inbound IPs for the provider’s region | No firewall configuration needed |
| mTLS support | Not enabled | Not explicitly mentioned; see limitations |
| Supported credentials | No region restriction noted | Databricks-to-Open credential in same region as provider not supported |
| Open recipients | Must also allowlist IPs | N/A (open recipients are classic compute) |

### Related Concepts

- [SecureConnect](/concepts/secureconnect.md) – The overall feature for sharing data behind a firewall.
- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol that SecureConnect builds on.
- mTLS (mutual TLS) – A security mechanism that is not enabled for classic compute recipients.
- [Egress Firewall Configuration](/concepts/secureconnect-recipient-firewall-configuration.md) – The network setup required for SecureConnect access.
- Databricks-to-Open Credential – A credential type with a region restriction for serverless recipients.

### Sources

- opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md

# Citations

1. [opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md](/references/opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws-029f12f3.md)
