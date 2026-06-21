---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a4b5ea06f9abb5448b53c56364f387346eaa74bf2e0e7b82e6d82565ca48eb0b
  pageDirectory: concepts
  sources:
    - share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - secureconnect-billing-and-usage-attribution
    - usage attribution and SecureConnect billing
    - SBAUA
  citations:
    - file: share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md
title: SecureConnect billing and usage attribution
description: Providers are billed for data transfer through SecureConnect, with per-recipient usage attributed via the recipient_id field in the billing system table for cost breakdown.
tags:
  - billing
  - administration
  - delta-sharing
timestamp: "2026-06-19T23:05:03.360Z"
---

# [SecureConnect](/concepts/secureconnect.md) billing and usage attribution

**SecureConnect billing and usage attribution** describes how providers using [OpenSharing SecureConnect](/concepts/opensharing-secureconnect.md) on Databricks are charged for data transfer and how they can attribute those costs to individual recipients. Understanding billing and attribution is essential for providers who share data from behind a firewall or private endpoint, as [SecureConnect](/concepts/secureconnect.md) routes recipient requests through a managed proxy that incurs data transfer costs. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Billing model

Providers are billed for data transfer that flows through [SecureConnect](/concepts/secureconnect.md). The pricing is determined by the standard Databricks data transfer and connectivity pricing model. Providers do not pay per-recipient setup fees — instead, they pay only for the volume of data egressed through the [SecureConnect](/concepts/secureconnect.md) proxy. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

Data transfer charges appear in the provider's bill under the `NETWORKING` billing origin product. The relevant SKU is defined in the [system.billing.list_prices](/concepts/systembillingusage-system-table.md) system table. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Usage attribution per recipient

Providers can break down their [SecureConnect](/concepts/secureconnect.md) costs by individual recipient using the **recipient_id** field in the billing system table. Each [SecureConnect](/concepts/secureconnect.md) data transfer is tagged with the identifier of the recipient that received the data, enabling per-recipient cost tracking. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

The `recipient_id` is stored in the `usage_metadata` column of the [system.billing.usage](/concepts/systembillingusage-system-table.md) system table. When this field is not null, the associated usage record corresponds to a [SecureConnect](/concepts/secureconnect.md) data egress event for that specific recipient. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

### Query example

The following SQL query returns the list cost of [SecureConnect](/concepts/secureconnect.md) data egress for each recipient over the last 7 days:

```sql
SELECT
  usage_records.usage_metadata.recipient_id,
  SUM(usage_records.usage_quantity * list_prices.pricing.default) AS list_cost
FROM system.billing.usage usage_records
INNER JOIN system.billing.list_prices
  ON
    usage_records.cloud = list_prices.cloud
    AND usage_records.sku_name = list_prices.sku_name
    AND usage_records.usage_start_time >= list_prices.price_start_time
    AND (
      usage_records.usage_end_time <= list_prices.price_end_time
      OR list_prices.price_end_time IS NULL
    )
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

This query joins the `usage` table with the `list_prices` table to calculate the estimated list cost for each recipient. The `recipient_id` field in the `WHERE` clause filters out non-SecureConnect usage. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Key considerations

- The `recipient_id` attribution is available only for [SecureConnect](/concepts/secureconnect.md) data egress. Other networking charges (such as standard [OpenSharing](/concepts/opensharing.md) endpoint access) are not tagged with a recipient identifier. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]
- Billing records appear under the `NETWORKING` billing origin product and are subject to the provider's contracted pricing terms. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]
- Per-recipient attribution enables providers to perform chargebacks or showbacks, allowing them to allocate [SecureConnect](/concepts/secureconnect.md) costs to specific business units or external sharing partners. ^[share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md]

## Related concepts

- [OpenSharing SecureConnect](/concepts/opensharing-secureconnect.md) – The technology that enables data sharing through a managed proxy.
- [system.billing.usage](/concepts/systembillingusage-system-table.md) – System table containing billable usage records with recipient attribution.
- [system.billing.list_prices](/concepts/systembillingusage-system-table.md) – System table containing pricing information for billable SKUs.
- Data transfer pricing – The pricing model for network egress on Databricks.
- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol that underlies [OpenSharing](/concepts/opensharing.md).

## Sources

- share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md

# Citations

1. [share-data-behind-a-firewall-with-secureconnect-databricks-on-aws.md](/references/share-data-behind-a-firewall-with-secureconnect-databricks-on-aws-7f7f967f.md)
