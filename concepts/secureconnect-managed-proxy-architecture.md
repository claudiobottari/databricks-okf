---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6862b3652e8a5113e83bd8ae4916ad1c94f4912577c88d202fd0139b0dcab900
  pageDirectory: concepts
  sources:
    - share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - secureconnect-managed-proxy-architecture
    - SMPA
  citations:
    - file: share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md
title: SecureConnect managed proxy architecture
description: Databricks routes recipient data requests through a managed proxy, eliminating the need for providers to update storage firewalls when adding new recipients.
tags:
  - architecture
  - networking
  - delta-sharing
timestamp: "2026-06-19T23:04:40.401Z"
---

# [SecureConnect](/concepts/secureconnect.md) Managed Proxy Architecture

**SecureConnect managed proxy architecture** is the infrastructure that enables Databricks providers to share data from cloud storage behind a firewall or private endpoint without requiring per-recipient network allowlisting. The architecture routes recipient requests through a managed proxy, eliminating the need for providers to update their storage firewall when adding new recipients. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## How the Architecture Works

Before enabling [SecureConnect](/concepts/secureconnect.md), a provider makes a one-time configuration that allows Databricks recipients to access the provider's storage behind a firewall or private endpoint. Databricks then routes all recipient requests through a managed proxy. This proxy handles the network connectivity, so the provider does not need to coordinate with recipients or cloud platform administrators for every new sharing relationship. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

Without [SecureConnect](/concepts/secureconnect.md), a provider must add each recipient's network identifier to their storage firewall, requiring coordination with the recipient and a cloud platform administrator for every new recipient. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Access Methods for Recipients

The managed proxy architecture supports different access methods depending on the recipient's compute type:

- **Databricks recipients on serverless compute** access shares with no per-provider firewall changes required.
- **Databricks recipients on classic compute and open recipients** allowlist a single set of Databricks control plane IPs for the provider's region.

^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Storage Access via Serverless Data Plane

[SecureConnect](/concepts/secureconnect.md) accesses provider storage through the serverless data plane. Providers configure their S3 bucket policies to include the VPCE OrgPath, which grants access to the managed proxy infrastructure. For lowest networking costs, providers should keep the region of their shared assets the same as their provider [Metastore](/concepts/metastore.md) region. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

### Private Connectivity with NCC

If shared storage is behind a private endpoint and not reachable from the public network, an account admin must configure a Network Connectivity Configuration (NCC) and attach it to the [Metastore](/concepts/metastore.md) hosting the shared data. An NCC attached to a workspace cannot be attached to a [Metastore](/concepts/metastore.md), and an NCC applied to a [Metastore](/concepts/metastore.md) for [OpenSharing](/concepts/opensharing.md) applies to all shares attached to that [Metastore](/concepts/metastore.md). ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## IP Access Control for Open Recipients

For open recipients, providers can restrict which client IP addresses are allowed to reach [SecureConnect](/concepts/secureconnect.md) using IP access lists. With [SecureConnect](/concepts/secureconnect.md), IP ACLs apply to both [OpenSharing](/concepts/opensharing.md) endpoint access and storage access. Without [SecureConnect](/concepts/secureconnect.md), IP ACLs restrict only [OpenSharing](/concepts/opensharing.md) endpoint access, leaving storage URLs reachable from any client IP. IP ACL changes for SecureConnect-enabled open recipients can take up to 10 minutes to take effect. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Billing and Attribution

Providers are billed for data transfer through [SecureConnect](/concepts/secureconnect.md). Per-recipient usage is attributed through the `recipient_id` field in the billing system table, enabling providers to break down billable [SecureConnect](/concepts/secureconnect.md) usage by recipient. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Supported Sharing Scenarios

[SecureConnect](/concepts/secureconnect.md) supports sharing to AWS, Azure, and GCP recipients. mTLS to [SecureConnect](/concepts/secureconnect.md) is supported only for serverless recipient clusters. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Limitations

- Assets cannot be backed by Cloudflare R2 storage.
- [SecureConnect](/concepts/secureconnect.md) is not available on AWS GovCloud.
- AWS PrivateLink to S3 is not compatible with FIPS endpoints, which Databricks uses by default in all US regions.

^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The data sharing framework that [SecureConnect](/concepts/secureconnect.md) operates within
- Network Connectivity Configuration (NCC) — Required for private endpoint connectivity
- [Delta Sharing](/concepts/delta-sharing.md) — The underlying protocol for sharing data across platforms
- Serverless Data Plane — The compute infrastructure through which [SecureConnect](/concepts/secureconnect.md) accesses storage
- IP Access Lists — Used to restrict open recipient access to [SecureConnect](/concepts/secureconnect.md)

## Sources

- share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md

# Citations

1. [share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md](/references/share-data-behind-a-firewall-with-secureconnect-databricks-on-aws-7f7f967f.md)
