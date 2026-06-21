---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 25fe98b83699446a117595cfe2605cc19cfa159f7640fd2ce3f554bf1e5dfbbe
  pageDirectory: concepts
  sources:
    - explore-features-and-lineage-legacy-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-store-publishing
    - OSP
  citations:
    - file: explore-features-and-lineage-legacy-databricks-on-aws.md
title: Online Store Publishing
description: Tracking which online stores a feature table has been published to, visible in the Workspace Feature Store UI.
tags:
  - feature-store
  - online-store
  - serving
timestamp: "2026-06-19T18:45:38.281Z"
---

# Online Store Publishing

**Online Store Publishing** refers to the capability of publishing a [Feature Table](/concepts/feature-table.md) to an [Online Store](/concepts/online-feature-store.md) within the Databricks Workspace Feature Store. When a feature table is published to an online store, the metadata tracked in the Feature Store UI includes which online stores the feature table has been published to, enabling users to monitor and manage the deployment of features for low-latency serving. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Tracking in the Feature Store UI

The Workspace Feature Store UI displays a table of all available feature tables. For each feature table, the metadata shown includes the online stores where the feature table has been published. This information appears alongside other lineage data such as data sources, scheduled jobs, and the last write time. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Related Concepts

- [Feature Table](/concepts/feature-table.md) – A collection of features stored in the feature store.
- [Online Store](/concepts/online-feature-store.md) – A low-latency storage for serving features in production.
- Feature Freshness – Monitoring how recently features have been updated.
- [Feature Lineage](/concepts/feature-lineage-tracking.md) – Tracking the origin and usage of features across the ML lifecycle.

## Sources

- explore-features-and-lineage-legacy-databricks-on-aws.md

# Citations

1. [explore-features-and-lineage-legacy-databricks-on-aws.md](/references/explore-features-and-lineage-legacy-databricks-on-aws-6e819774.md)
