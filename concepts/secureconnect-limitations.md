---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e2a77bbaa8794378c524f1c263d7476ad9812c3d73bc88430fbb829eb401b35d
  pageDirectory: concepts
  sources:
    - opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - secureconnect-limitations
  citations:
    - file: opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md
title: SecureConnect Limitations
description: Known constraints of SecureConnect including lack of mTLS support for classic compute and OIDC recipients, and unsupported serverless-to-Open credential scenarios
tags:
  - databricks
  - delta-sharing
  - security
  - limitations
timestamp: "2026-06-19T19:50:55.867Z"
---

# SecureConnect Limitations

**SecureConnect Limitations** describes the functional constraints and unsupported configurations that apply when recipients access shares from a provider who has enabled [OpenSharing SecureConnect](/concepts/opensharing-secureconnect.md) on Databricks. These limitations affect how recipients connect and what security features are available depending on their compute type and authentication method. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

## mTLS Not Enabled for Classic Compute Recipients

Mutual TLS (mTLS) is not enabled for recipients using [Classic Compute](/concepts/classic-compute-forecasting.md) to access SecureConnect-enabled shares. This means that while SecureConnect provides a secure tunnel for data sharing, the additional mutual authentication layer provided by mTLS is unavailable for recipients running on classic compute. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

## mTLS Not Enabled for OIDC Recipients

Similarly, mTLS is not enabled for OIDC (OpenID Connect) recipients accessing SecureConnect shares. Organizations that rely on OIDC-based authentication for their recipients cannot also use mTLS for transport-level mutual authentication when connecting through SecureConnect. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

## Serverless Recipients with Cross-Region Databricks-to-Open Credentials Not Supported

Serverless Databricks recipients using a Databricks-to-Open credential in the **same region** as the provider are not supported. This means that if both the recipient's serverless compute and the provider's SecureConnect endpoint are in the same AWS region, the connection is not available. Recipients in this scenario must use an alternative compute type or choose a different credential configuration. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

## Firewall Configuration Requirements Vary by Compute Type

While not a strict limitation, it is important to note that firewall configuration requirements differ between compute types:

- **Databricks recipients on classic compute** and **open recipients** must allowlist Databricks inbound IP addresses in their egress firewall to access SecureConnect. The allowlist must be configured for the provider's cloud and region, regardless of the recipient's cloud. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]
- **Databricks recipients on serverless compute** do not need to configure their egress firewall. Databricks routes serverless traffic to SecureConnect internally. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

## Summary of Limitations

| Limitation | Applies To |
|---|---|
| mTLS not enabled | Classic compute recipients and OIDC recipients |
| Databricks-to-Open credential in same region not supported | Serverless recipients in the same region as the provider |
| Egress firewall allowlisting required | Classic compute and open recipients |

## Related Concepts

- [SecureConnect](/concepts/secureconnect.md) — Overview of the SecureConnect feature for sharing data behind firewalls
- [Delta Sharing](/concepts/delta-sharing.md) — The underlying data sharing protocol
- [Classic Compute](/concepts/classic-compute-forecasting.md) — Traditional Databricks compute that requires firewall configuration
- Serverless Compute — Databricks compute that handles routing internally
- OIDC Authentication — OpenID Connect-based authentication for recipients
- [OpenSharing](/concepts/opensharing.md) — The open standard for Delta Sharing

## Sources

- opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md

# Citations

1. [opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md](/references/opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws-029f12f3.md)
