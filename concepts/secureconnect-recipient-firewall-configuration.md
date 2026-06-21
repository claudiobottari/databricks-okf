---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dd474cd80bea71c4d1d6b87e284f6648d442c9c242c1afcec12a19c13e366c88
  pageDirectory: concepts
  sources:
    - opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - secureconnect-recipient-firewall-configuration
    - SRFC
    - SecureConnect recipient configuration
    - Egress Firewall Configuration
  citations:
    - file: opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md
title: SecureConnect Recipient Firewall Configuration
description: The network configuration steps a Databricks recipient must take to access shares from a provider using SecureConnect, including allowlisting inbound IPs
tags:
  - databricks
  - delta-sharing
  - networking
  - firewall
timestamp: "2026-06-19T19:50:49.277Z"
---

# SecureConnect Recipient Firewall Configuration

**SecureConnect Recipient Firewall Configuration** refers to the network setup required for [Delta Sharing](/concepts/delta-sharing.md) recipients to access shares from a provider that has enabled [OpenSharing SecureConnect](/concepts/opensharing-secureconnect.md). This configuration primarily involves allowlisting [Databricks inbound IP addresses](/concepts/databricks-inbound-ip-allowlisting.md) in the recipient's egress firewall. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

## Overview

When a provider enables SecureConnect to share data behind a firewall, recipients must configure their network to allow outbound traffic to Databricks. The specific firewall configuration required depends on the type of compute the recipient uses. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

### Classic Compute and Open Recipients

Databricks recipients using classic compute and open recipients **must** allowlist Databricks inbound IP addresses in their egress firewall to access SecureConnect. The IP addresses to allowlist correspond to the provider's cloud and region, regardless of the recipient's own cloud platform. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

### Serverless Compute

Databricks recipients on serverless compute **do not** need to configure their egress firewall to access SecureConnect. Databricks routes serverless traffic to SecureConnect internally, eliminating the need for manual network configuration. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

## Allowlisting Databricks Inbound IPs

To configure the firewall:

1. Identify the cloud platform your provider is on (AWS, Azure, or GCP).
2. Determine the provider's region.
3. Allowlist the Databricks inbound IP addresses for that specific cloud and region in your egress firewall.

> **Important**: The IP addresses to allowlist are based on the **provider's** cloud and region, not the recipient's cloud.

## Limitations

The following limitations apply to Databricks recipients accessing SecureConnect-enabled shares:

- **mTLS not enabled for classic compute**: Mutual TLS (mTLS) is not available for recipients using classic compute. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]
- **mTLS not enabled for OIDC recipients**: Recipients using OIDC (OpenID Connect) authentication do not have mTLS enabled. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]
- **Serverless same-region limitation**: Serverless Databricks recipients using a Databricks-to-Open credential in the same region as the provider are not supported. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for sharing data across platforms
- [SecureConnect](/concepts/secureconnect.md) — The provider-side feature for sharing data behind a firewall
- [Databricks inbound IP addresses](/concepts/databricks-inbound-ip-allowlisting.md) — The IP ranges that need to be allowlisted
- [Classic Compute](/concepts/classic-compute-forecasting.md) — Traditional Databricks compute that requires manual firewall configuration
- Serverless Compute — Databricks compute that routes traffic internally for SecureConnect
- mTLS — Mutual TLS authentication for secure connections
- [Open Recipients](/concepts/opensharing-recipient.md) — Non-Databricks recipients accessing Delta Sharing

## Sources

- opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md

# Citations

1. [opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md](/references/opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws-029f12f3.md)
