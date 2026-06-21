---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5bbe676b7b6181dc7869005fb836dead41fda4236403ecb67030d263a3e35dff
  pageDirectory: concepts
  sources:
    - monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - change-data-feed-cdf-for-recipient-side-replication
    - CDF(FRR
  citations:
    - file: monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md
title: Change Data Feed (CDF) for Recipient-Side Replication
description: Enabling CDF on shared tables allows recipients to access changes and merge them into a local copy, limiting egress to the incremental refresh rather than full query access across regions.
tags:
  - delta-sharing
  - data-replication
  - change-data-feed
timestamp: "2026-06-19T19:46:01.462Z"
---

# Change Data Feed (CDF) for Recipient-Side Replication

**Change Data Feed (CDF) for Recipient-Side Replication** is a strategy for minimizing cross-region data egress costs in [OpenSharing](/concepts/opensharing.md) by enabling recipients to maintain a local replica of a shared table. When the provider enables CDF on a shared table with history, the recipient can access only the incremental changes and merge them into a local copy, avoiding full-table downloads across region boundaries. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Overview

In [OpenSharing](/concepts/opensharing.md) scenarios where a provider shares data across clouds or regions, cloud vendors may charge egress fees for data transfer. One approach to avoiding these costs is for recipients to clone the shared data to local regions for active querying, setting up syncs between the shared table and the local clone. CDF supports this pattern by limiting egress to only the changes needed to refresh a local replica, rather than transferring the entire table each time. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Enabling CDF on Shared Tables

To share a table with its change data feed, the provider must both **enable CDF on the table** and **share it `WITH HISTORY`**. This dual requirement ensures that the recipient can access the historical change records and merge them into a local copy. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

### Provider Actions

1. Enable CDF on the source table using standard [Change Data Feed on Databricks](/concepts/change-data-feed-column-conflict.md) configuration.
2. When adding the table to a share, include the history option.

For detailed instructions, see [Use change data feed on Databricks](https://docs.databricks.com/aws/en/tables/features/change-data-feed) and [Add tables to a share](https://docs.databricks.com/aws/en/delta-sharing/create-share#add-tables). ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Recipient Workflow

When a table is shared with CDF, the recipient can:

1. **Create a local replica** of the shared table in their own region or cloud.
2. **Run incremental syncs** using the CDF to apply only the changes since the last sync.
3. **Serve queries** from the local replica, avoiding cross-region data transfers during query execution.

If the recipient is on Databricks, they can use a [Lakeflow Jobs](/concepts/lakeflow-jobs.md) workflow to propagate changes to the local replica on a scheduled basis. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Benefits

- **Reduced egress costs**: Only the incremental changes (not the full table) cross region boundaries during sync operations.
- **Low latency queries**: Users query a local copy of the data, avoiding the network latency of cross-region reads.
- **Consistency**: The local replica can be kept up-to-date with a regular sync schedule.

## Comparison with Provider-Side Replication

CDF for recipient-side replication is an alternative to provider-side replication using [Delta Deep Clone](/concepts/deep-clone.md). In the provider-side approach, the provider creates and syncs local replicas in each recipient's region. In the recipient-side approach, the recipient manages their own local copy and uses CDF to update it. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

| Approach | Who manages replication | Egress cost borne by |
|---|---|---|
| Provider-side (Deep Clone) | Provider | Provider during sync between replicas |
| Recipient-side (CDF) | Recipient | Recipient during CDF sync |

## Related Concepts

- OpenSharing Egress Costs — Overall strategies for monitoring and minimizing egress charges.
- [Delta Deep Clone](/concepts/deep-clone.md) — An alternative replication method for providers.
- [Change Data Feed on Databricks](/concepts/change-data-feed-column-conflict.md) — The underlying CDF mechanism on the Databricks platform.
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) — The scheduling tool for automating incremental syncs.
- Cloudflare R2 Storage — An egress-free storage option for avoiding these costs entirely.

## Sources

- monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md

# Citations

1. [monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md](/references/monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws-13b884c0.md)
