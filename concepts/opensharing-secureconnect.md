---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d80ac814e321a1ea974c58deb8dc749a85cf95a570f2116bd7f50951a2cf3200
  pageDirectory: concepts
  sources:
    - share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-secureconnect
    - Data transfer billing for SecureConnect
    - Share data behind a firewall with SecureConnect
  citations:
    - file: share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md
title: OpenSharing SecureConnect
description: A Databricks feature that allows providers to share data from cloud storage behind firewalls or private endpoints without needing to allowlist each recipient's network individually.
tags:
  - delta-sharing
  - networking
  - security
timestamp: "2026-06-19T23:04:48.742Z"
---

# [OpenSharing](/concepts/opensharing.md) [SecureConnect](/concepts/secureconnect.md)

**OpenSharing SecureConnect** is a feature that enables [Delta Sharing](/concepts/delta-sharing.md) providers to share data from cloud storage that is behind a firewall or private endpoint without needing to allowlist each recipient's network individually. It routes recipient requests through a managed proxy, simplifying provider-side network configuration. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## How [SecureConnect](/concepts/secureconnect.md) Works

Before enabling [SecureConnect](/concepts/secureconnect.md) on a Databricks account, a provider makes a one-time configuration that allows Databricks recipients to access the provider's storage behind a firewall or private endpoint. Databricks then routes recipient requests through a managed proxy, meaning the provider does not need to update their storage firewall when adding a new recipient. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

Recipients access shared data using their existing [OpenSharing](/concepts/opensharing.md) setup. Databricks recipients on serverless compute can access shares with no per-provider firewall changes. Databricks recipients on classic compute and open recipients need to allowlist a single set of Databricks control plane IPs for the provider's region. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

Without [SecureConnect](/concepts/secureconnect.md), a provider must add each recipient's network identifier to their storage firewall, coordinating with the recipient and a cloud platform administrator for every new recipient. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Requirements

To use [SecureConnect](/concepts/secureconnect.md), the **OpenSharing SecureConnect** preview must be enabled in the **Account Console**. See Manage Databricks previews in the Databricks documentation. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Provider Setup

Setting up [SecureConnect](/concepts/secureconnect.md) involves configuring your storage firewall to allow access and enabling [SecureConnect](/concepts/secureconnect.md) for your metastores and recipients. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

### Step 1: Configure Your Storage Firewall

[SecureConnect](/concepts/secureconnect.md) accesses your storage through the serverless data plane. For the lowest networking costs, keep the region of your shared assets the same as your provider [Metastore](/concepts/metastore.md) region. Configure your S3 bucket policies to include the VPCE OrgPath. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

#### Private Connectivity with a Network Connectivity Configuration (NCC)

If your shared storage is behind a private endpoint and is not reachable from the public network, an account admin must configure a Network Connectivity Configuration (NCC) and attach it to the [Metastore](/concepts/metastore.md) that hosts your shared data. An NCC attached to a workspace cannot be attached to a [Metastore](/concepts/metastore.md). An NCC applied to a [Metastore](/concepts/metastore.md) for [OpenSharing](/concepts/opensharing.md) applies to all shares attached to that [Metastore](/concepts/metastore.md). ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

Note that AWS PrivateLink to S3 is not compatible with FIPS endpoints, which Databricks uses by default in all US regions. If your provider [Metastore](/concepts/metastore.md) is in a US region, contact your Databricks account team. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

### Step 2: Enable [SecureConnect](/concepts/secureconnect.md) on a [Metastore](/concepts/metastore.md)

A [Metastore](/concepts/metastore.md) administrator can configure the [Metastore](/concepts/metastore.md) so new recipients automatically use [SecureConnect](/concepts/secureconnect.md). By default, new and existing recipients are not enrolled in [SecureConnect](/concepts/secureconnect.md). To enable [SecureConnect](/concepts/secureconnect.md) on a [Metastore](/concepts/metastore.md):

1. In your Databricks workspace, open **Catalog** to launch [Catalog Explorer](/concepts/catalog-explorer.md).
2. Click the gear icon and select **OpenSharing**.
3. Click **Settings** in the upper-right corner.
4. Turn on **Enable [SecureConnect](/concepts/secureconnect.md) for new recipients**.
5. Click **Save**.

^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

### Step 3: Enable [SecureConnect](/concepts/secureconnect.md) for Individual Recipients

Recipient owners and users with the `USE_RECIPIENT` privilege can toggle [SecureConnect](/concepts/secureconnect.md) on or off for each recipient. [SecureConnect](/concepts/secureconnect.md) is disabled on a recipient by default unless the [Metastore](/concepts/metastore.md) was set to enable it for all new recipients when the recipient was created. To configure [SecureConnect](/concepts/secureconnect.md) on a recipient:

1. Open **Catalog** and click the gear icon to select **OpenSharing**.
2. Click the **Shared by me** tab, then the **Recipients** tab.
3. Turn on **SecureConnect** for each desired recipient.

^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

### Step 4: Restrict Open Recipient Access with IP ACLs

For open recipients, you can restrict which client IP addresses are allowed to reach [SecureConnect](/concepts/secureconnect.md) using IP access lists. IP ACLs apply only to open recipients. With [SecureConnect](/concepts/secureconnect.md), IP ACLs apply to both [OpenSharing](/concepts/opensharing.md) endpoint access and storage access. Without [SecureConnect](/concepts/secureconnect.md), IP ACLs restrict only [OpenSharing](/concepts/opensharing.md) endpoint access; storage URLs remain reachable from any client IP. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

IP ACL changes for SecureConnect-enabled open recipients can take up to 10 minutes to take effect. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Supported Sharing Scenarios

[SecureConnect](/concepts/secureconnect.md) supports sharing to AWS, Azure, and GCP. mTLS to [SecureConnect](/concepts/secureconnect.md) is supported for only serverless recipient clusters. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

### Feature Support

- OIDC sharing does not currently work when the recipient is also on Databricks.
- Cloud token optimization is not available for [SecureConnect](/concepts/secureconnect.md).

^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Limitations

- Your assets cannot be backed by Cloudflare R2 storage.
- [SecureConnect](/concepts/secureconnect.md) is not available on AWS GovCloud.
- AWS PrivateLink to S3 is not compatible with FIPS endpoints, which Databricks uses by default in all US regions.

^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Billing

Providers are billed for data transfer through [SecureConnect](/concepts/secureconnect.md). Per-recipient usage is attributed through the `recipient_id` field in the billing system table, allowing providers to break down billable [SecureConnect](/concepts/secureconnect.md) usage by recipient. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

The following query returns the list cost of [SecureConnect](/concepts/secureconnect.md) data egress for each recipient over the last 7 days:

```sql
SELECT
  usage_records.usage_metadata.recipient_id,
  SUM(usage_records.usage_quantity * list_prices.pricing.default) AS list_cost
FROM system.billing.usage usage_records
INNER JOIN system.billing.list_prices ON
  usage_records.cloud = list_prices.cloud AND
  usage_records.sku_name = list_prices.sku_name AND
  usage_records.usage_start_time >= list_prices.price_start_time AND
  (usage_records.usage_end_time <= list_prices.price_end_time OR list_prices.price_end_time IS NULL)
WHERE
  usage_records.billing_origin_product = 'NETWORKING'
  AND usage_records.usage_metadata.recipient_id IS NOT NULL
  AND usage_records.usage_date >= CURRENT_DATE() - INTERVAL 7 DAYS
GROUP BY
  usage_records.usage_metadata.recipient_id
ORDER BY
  list_cost DESC
```

^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md)
- [OpenSharing](/concepts/opensharing.md)
- Network Connectivity Configuration (NCC)
- [Data Sharing Provider Setup](/concepts/opensharing-provider-object.md)
- Data Sharing Recipient Configuration
- [IP Access Lists for OpenSharing](/concepts/ip-access-lists-for-opensharing-recipients.md)

## Sources

- share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md

# Citations

1. [share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md](/references/share-data-behind-a-firewall-with-secureconnect-databricks-on-aws-7f7f967f.md)
