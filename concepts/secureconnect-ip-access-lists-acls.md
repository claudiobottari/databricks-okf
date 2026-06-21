---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 711770ea8a885b3ad0c71a21dd642ada8815f1574584f5048b65a0c278277ac3
  pageDirectory: concepts
  sources:
    - share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - secureconnect-ip-access-lists-acls
    - SIAL(
  citations:
    - file: share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md
title: SecureConnect IP access lists (ACLs)
description: For open recipients, IP ACLs can restrict which client IP addresses are allowed to reach SecureConnect, covering both OpenSharing endpoint access and storage access.
tags:
  - security
  - networking
  - delta-sharing
timestamp: "2026-06-19T23:04:50.076Z"
---

# [SecureConnect](/concepts/secureconnect.md) IP access lists (ACLs)

**SecureConnect IP access lists (ACLs)** allow a provider to restrict which client IP addresses are permitted to reach [SecureConnect](/concepts/secureconnect.md) for open recipients. They are an optional security layer that a provider can configure after enabling [SecureConnect](/concepts/secureconnect.md) on a recipient. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Scope and Applicability

IP ACLs apply only to open recipients—Databricks recipients on serverless compute are not subject to these IP restrictions. With [SecureConnect](/concepts/secureconnect.md) enabled, the IP ACL governs both (1) access to the [OpenSharing](/concepts/opensharing.md) endpoint and (2) access to the underlying storage. Without [SecureConnect](/concepts/secureconnect.md), IP ACLs restrict only [OpenSharing](/concepts/opensharing.md) endpoint access, and storage URLs remain reachable from any client IP. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Propagation Time

Changes to IP ACLs for SecureConnect‑enabled open recipients can take up to 10 minutes to take effect. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Setting Up IP ACLs

For setup instructions, see Restrict OpenSharing recipient access using IP access lists (Databricks-to-Open sharing). ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Related Concepts

- [SecureConnect](/concepts/secureconnect.md) – General mechanism for sharing data behind firewalls.
- [OpenSharing](/concepts/opensharing.md) – The sharing protocol that [SecureConnect](/concepts/secureconnect.md) extends.
- IP access lists – The broader concept of network‑level access controls on Databricks.
- [Open recipient](/concepts/opensharing-recipient.md) – A recipient type that can be restricted with IP ACLs.
- Provider configuration for SecureConnect – Steps to enable [SecureConnect](/concepts/secureconnect.md) on a [Metastore](/concepts/metastore.md) and per recipient.

## Sources

- share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md

# Citations

1. [share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md](/references/share-data-behind-a-firewall-with-secureconnect-databricks-on-aws-7f7f967f.md)
