---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: db12dd749abf1b480e8f099ca631b9640161b74272030dba31c8ebafde5f7563
  pageDirectory: concepts
  sources:
    - opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md
    - set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - secureconnect
  citations:
    - file: opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md
    - file: set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md
title: SecureConnect
description: Databricks feature enabling data sharing through firewalls by routing traffic through Databricks-internal IP addresses
tags:
  - databricks
  - delta-sharing
  - networking
  - security
timestamp: "2026-06-19T19:51:16.243Z"
---

# SecureConnect

**SecureConnect** is a managed proxy service that brokers data access between data providers and recipients through a secure intermediary, eliminating the need for recipients to manually configure their own egress firewalls and network access controls. When a provider enables SecureConnect, Databricks routes all shared data traffic through a dedicated proxy, and recipients access the data via Databricks inbound IP addresses rather than directly reaching the provider's cloud storage. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md, set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md]

## Overview

SecureConnect functions as a network intermediary between data providers and recipients. The provider configures their Databricks account to use SecureConnect, and recipients access shared data through Databricks-managed connections. This architecture prevents recipients from needing to configure their own storage network access or manage complex firewall rules for each provider they connect to. ^[set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md]

## Recipient Firewall Configuration

When a provider has enabled SecureConnect, recipients with egress firewalls must allowlist specific Databricks inbound IP addresses to access shared data. The IP addresses to allowlist are determined by the provider's cloud and region, regardless of the recipient's own cloud environment. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

### Allowlist Requirements by Recipient Type

- **Databricks recipients on classic compute** — Must allowlist Databricks inbound IP addresses. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]
- **Databricks recipients on serverless compute** — Do not need to configure their egress firewall. Databricks routes serverless traffic to SecureConnect internally. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]
- **Open recipients (non-Databricks)** — Must allowlist Databricks inbound IP addresses. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

### Provider Cloud Selection

The allowlist process depends on the provider's cloud. Select the provider's cloud (AWS, Azure, or GCP), then allowlist the listed Databricks inbound IP addresses for the provider's region. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

## Limitations

The following limitations apply to recipients accessing SecureConnect-enabled shares:

- **mTLS** — Mutual TLS (mTLS) is not enabled for recipients using classic compute. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]
- **mTLS** — mTLS is not enabled for OpenID Connect (OIDC) recipients. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]
- **Serverless Databricks recipients** — Serverless Databricks recipients using a Databricks-to-Open credential in the same region as the provider are not supported. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

## Provider Setup

Providers set up SecureConnect by enabling OpenSharing on a Unity Catalog [Metastore](/concepts/metastore.md), configuring the recipient token lifetime, and optionally specifying an organization name. Providers can also use SecureConnect as an alternative to manually configuring storage network access and firewall rules for each recipient. ^[set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md]

For detailed provider setup instructions, see [Share data behind a firewall with SecureConnect](/concepts/opensharing-secureconnect.md). ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The data sharing framework that SecureConnect operates within.
- [Unity Catalog](/concepts/unity-catalog.md) — Required for providers using SecureConnect.
- [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) — A sharing protocol that can use SecureConnect.
- [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) — An open sharing protocol that can use SecureConnect.
- [Serverless compute](/concepts/serverless-gpu-compute.md) — A compute model that does not require egress firewall configuration for SecureConnect.
- Classic compute — A compute model that requires egress firewall configuration for SecureConnect.
- mTLS — Mutual TLS, a security protocol not enabled for certain recipient types in SecureConnect.
- [Recipient Token Lifetime](/concepts/recipient-token-lifetime.md) — A configurable setting for SecureConnect recipient tokens.

## Sources

- opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md
- set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md

# Citations

1. [opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md](/references/opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws-029f12f3.md)
2. [set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md](/references/set-up-opensharing-for-your-account-for-providers-databricks-on-aws-4b18295d.md)
