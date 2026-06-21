---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1f7048bea2e9728393c5c0a55964526a47421f77b94b06cc6c7e1cb58a3e0ca4
  pageDirectory: concepts
  sources:
    - opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-inbound-ip-allowlisting
    - DIIA
    - Databricks inbound IP addresses
  citations:
    - file: opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md
title: Databricks Inbound IP Allowlisting
description: The practice of adding Databricks-managed IP addresses to a firewall allowlist for the provider's cloud and region to enable SecureConnect access
tags:
  - databricks
  - networking
  - security
  - firewall
timestamp: "2026-06-19T19:50:50.391Z"
---

# Databricks Inbound IP Allowlisting

**Databricks Inbound IP Allowlisting** is a network configuration requirement for [Delta Sharing](/concepts/delta-sharing.md) recipients who need to access shares from a provider that has enabled [OpenSharing SecureConnect](/concepts/opensharing-secureconnect.md). When a recipient has an egress firewall, they must allowlist specific Databricks inbound IP addresses to establish connectivity with SecureConnect-enabled shares. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

## Overview

SecureConnect allows data providers to share data behind their firewall. For recipients to access these shares, their egress firewall must permit traffic from Databricks inbound IP addresses. The IP addresses to allowlist are determined by the **provider's cloud and region**, regardless of the recipient's own cloud platform. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

## Who Needs to Configure Allowlisting

The allowlisting requirement applies to specific recipient types:

- **Databricks recipients on classic compute** — Must allowlist Databricks inbound IP addresses. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]
- **Open recipients** — Must allowlist Databricks inbound IP addresses. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]
- **Databricks recipients on serverless compute** — Do **not** need to configure their egress firewall. Databricks routes serverless traffic to SecureConnect internally. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

## Configuration Steps

To configure allowlisting:

1. Identify the cloud platform your provider is on (AWS, Azure, or GCP).
2. Determine the provider's region.
3. Allowlist the Databricks inbound IP addresses for that specific cloud and region in your egress firewall.

The IP addresses to allowlist are published by Databricks and vary by cloud provider and region. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

## Limitations

The following limitations apply to Databricks recipients accessing SecureConnect-enabled shares:

- Mutual TLS (mTLS) is not enabled for recipients using classic compute. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]
- mTLS is not enabled for OIDC recipients. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]
- Serverless Databricks recipients using a Databricks-to-Open credential in the same region as the provider are not supported. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for sharing data across platforms
- [OpenSharing SecureConnect](/concepts/opensharing-secureconnect.md) — Provider-side feature for sharing data behind a firewall
- [Egress Firewall Configuration](/concepts/secureconnect-recipient-firewall-configuration.md) — Network security for outbound traffic
- Classic Compute vs Serverless Compute — Compute types with different networking requirements
- Databricks Inbound IP Ranges — The specific IP addresses to allowlist

## Sources

- opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md

# Citations

1. [opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md](/references/opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws-029f12f3.md)
