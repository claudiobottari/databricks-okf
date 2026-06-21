---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 086ecc35018a279b06775ded5bf333d0b1b67acc227cc48116c9dce87db2ba77
  pageDirectory: concepts
  sources:
    - share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - secureconnect-privatelink-and-ncc-configuration
    - NCC configuration and SecureConnect PrivateLink
    - SPANC
    - Span
    - span
  citations:
    - file: share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md
title: SecureConnect PrivateLink and NCC configuration
description: For shared storage behind private endpoints not reachable from the public network, account admins can configure a Network Connectivity Configuration (NCC) and attach it to the OpenSharing metastore, with a note that AWS PrivateLink to S3 is incompatible with FIPS endpoints in US regions.
tags:
  - networking
  - security
  - aws
  - private-link
timestamp: "2026-06-19T23:05:01.944Z"
---

# [SecureConnect](/concepts/secureconnect.md) PrivateLink and NCC configuration

**SecureConnect PrivateLink and NCC configuration** refers to the optional network setup that allows a data provider using [OpenSharing SecureConnect](/concepts/opensharing-secureconnect.md) to share data from cloud storage that is behind a private endpoint and is not reachable from the public network. This configuration requires a Network Connectivity Configuration (NCC) and AWS PrivateLink to S3. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Overview

When a provider's shared storage is behind a private endpoint, an account administrator must configure an NCC and attach it to the OpenSharing metastore that hosts the shared data. The NCC enables Databricks to route recipient requests through a managed proxy to the private storage, so the provider does not need to update their storage firewall when adding new recipients. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

An NCC attached to a workspace cannot be attached to a [Metastore](/concepts/metastore.md). An NCC applied to a [Metastore](/concepts/metastore.md) for [OpenSharing](/concepts/opensharing.md) applies to all shares attached to that [Metastore](/concepts/metastore.md). ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Prerequisites

- The **OpenSharing SecureConnect** preview must be enabled in the Account Console. See Manage Databricks previews.
- The provider's shared assets and provider [Metastore](/concepts/metastore.md) should be in the same region for the lowest networking costs.

## Important limitation: AWS PrivateLink to S3 and FIPS endpoints

AWS PrivateLink to S3 is not compatible with FIPS endpoints, which Databricks uses by default in all US regions. If your provider [Metastore](/concepts/metastore.md) is in a US region and you use [SecureConnect](/concepts/secureconnect.md) with PrivateLink, contact your Databricks account team. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Step-by-step configuration

### Step 1: Create an NCC and private endpoint rule

Create an [NCC](/concepts/percent-null.md) and a private endpoint rule for your S3 bucket, but do not attach the NCC to a workspace. See Configure private connectivity to AWS-managed resources for NCC and PrivateLink setup instructions. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

### Step 2: Attach the NCC to the [OpenSharing](/concepts/opensharing.md) [Metastore](/concepts/metastore.md)

1. As a Databricks account administrator, go to the Account Console.
2. In the sidebar, click **Catalog**.
3. Click the name of the [OpenSharing](/concepts/opensharing.md) [Metastore](/concepts/metastore.md) to open its details.
4. Under **OpenSharing Network connectivity configuration (NCC)**, click **Edit**.
5. Search for and select the NCC you created for [OpenSharing](/concepts/opensharing.md).
6. Click **Save**.

> **Important:** If you are unable to attach an NCC to a [Metastore](/concepts/metastore.md), contact your Databricks account team to enable private connectivity for [OpenSharing SecureConnect](/concepts/opensharing-secureconnect.md) using an NCC.

### Step 3: Configure storage firewall for [SecureConnect](/concepts/secureconnect.md)

[SecureConnect](/concepts/secureconnect.md) accesses your storage through the serverless data plane. Configure your S3 bucket policies to include the VPCE OrgPath. See S3 bucket access using VPCE OrgPath. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Related concepts

- [SecureConnect](/concepts/secureconnect.md) — The overall mechanism for sharing data behind firewalls
- Network Connectivity Configuration (NCC) — The configuration that enables private connectivity
- AWS PrivateLink to S3 — The AWS service used for private S3 access
- OpenSharing metastore — The [Metastore](/concepts/metastore.md) that hosts shared data
- Serverless data plane — The compute infrastructure that routes recipient requests
- VPCE OrgPath — The identifier used in S3 bucket policies for [SecureConnect](/concepts/secureconnect.md) access
- FIPS endpoints — A compatibility consideration for US regions

## Sources

- share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md

# Citations

1. [share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md](/references/share-data-behind-a-firewall-with-secureconnect-databricks-on-aws-7f7f967f.md)
