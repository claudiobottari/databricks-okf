---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1758d36efff573b65587d172c6fed9807e0bf484fafd37faa535e7847d3b8b5a
  pageDirectory: concepts
  sources:
    - share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - secureconnect-limitations-and-supported-scenarios
    - supported scenarios and SecureConnect limitations
    - SLASS
  citations:
    - file: share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md
title: SecureConnect limitations and supported scenarios
description: SecureConnect supports sharing to AWS, Azure, and GCP recipients but has limitations including incompatibility with Cloudflare R2 storage, unavailability on AWS GovCloud, and AWS PrivateLink-to-S3 incompatibility with FIPS endpoints in US regions.
tags:
  - compatibility
  - limitations
  - delta-sharing
timestamp: "2026-06-19T23:05:01.541Z"
---

# [SecureConnect Limitations](/concepts/secureconnect-limitations.md) and Supported Scenarios

**SecureConnect** is a Databricks feature that allows providers to share data from cloud storage behind a firewall or private endpoint without requiring per-recipient network allowlisting. This page documents the supported sharing configurations and known limitations of [SecureConnect](/concepts/secureconnect.md).

## Supported Sharing Scenarios

[SecureConnect](/concepts/secureconnect.md) supports sharing to AWS, Azure, and GCP recipients. The feature works with both [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) and [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md). ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

### mTLS Support

Mutual TLS (mTLS) to [SecureConnect](/concepts/secureconnect.md) is supported only for serverless recipient clusters. Classic compute recipients cannot use mTLS with [SecureConnect](/concepts/secureconnect.md). ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

### OIDC Sharing

OpenID Connect (OIDC) sharing does not currently work when the recipient is also on Databricks. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

### Cloud Token Optimization

Cloud token optimization is not available for [SecureConnect](/concepts/secureconnect.md). ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

### IP Access Lists for Open Recipients

For open recipients ([Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md)), providers can restrict client IP addresses using IP access lists. With [SecureConnect](/concepts/secureconnect.md), IP ACLs apply to both [OpenSharing](/concepts/opensharing.md) endpoint access and storage access. Without [SecureConnect](/concepts/secureconnect.md), IP ACLs restrict only endpoint access. IP ACL changes for SecureConnect-enabled open recipients can take up to 10 minutes to take effect. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Limitations

The following limitations apply to [SecureConnect](/concepts/secureconnect.md) as a provider:

- Assets cannot be backed by Cloudflare R2 storage. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]
- [SecureConnect](/concepts/secureconnect.md) is not available on AWS GovCloud. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]
- AWS PrivateLink to S3 is not compatible with FIPS endpoints. Databricks uses FIPS endpoints by default in all US regions. If you use [SecureConnect](/concepts/secureconnect.md) with PrivateLink in a US region, contact your Databricks account team. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

For recipient-side limitations (such as mTLS support and [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) restrictions), see the SecureConnect recipient configuration page. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md)
- [OpenSharing](/concepts/opensharing.md)
- Serverless Compute
- PrivateLink
- IP ACLs in Delta Sharing
- Network connectivity configuration (NCC)

## Sources

- share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md

# Citations

1. [share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md](/references/share-data-behind-a-firewall-with-secureconnect-databricks-on-aws-7f7f967f.md)
