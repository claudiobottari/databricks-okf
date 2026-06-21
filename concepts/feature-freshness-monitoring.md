---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ade35a6e1bfcef8c69a2a685337c366c0790832cfaddc87833c7203b65fc0ef7
  pageDirectory: concepts
  sources:
    - explore-features-and-lineage-legacy-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-freshness-monitoring
    - FFM
  citations:
    - file: explore-features-and-lineage-legacy-databricks-on-aws.md
title: Feature Freshness Monitoring
description: Tracking the last write time and scheduled job status for feature tables to verify data recency.
tags:
  - feature-store
  - data-quality
  - monitoring
timestamp: "2026-06-19T18:45:33.310Z"
---

```yaml
---
title: Feature Freshness Monitoring
summary: A capability in the Databricks Workspace Feature Store UI that lets you verify when feature data was last written to a feature table, helping you confirm that scheduled pipelines are running and features are up to date.
sources:
  - explore-features-and-lineage-legacy-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:15:44.070Z"
updatedAt: "2026-06-19T10:26:33.666Z"
tags:
  - feature-store
  - monitoring
  - data-quality
aliases:
  - feature-freshness-monitoring
  - FFM
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Feature Freshness Monitoring

**Feature Freshness Monitoring** is a capability of the [[Workspace Feature Store UI|Workspace Feature Store]] (legacy) that lets you verify when feature data was last written to a feature table. It helps you confirm that scheduled data pipelines are running as expected and that the features used by downstream models are up to date. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Check freshness in the UI

1. In the Databricks sidebar, under **AI/ML**, click **Features** to open the feature store UI. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]
2. The feature table list shows metadata for each table, including **the last time a notebook or job wrote to the feature table**. This allows you to quickly assess overall freshness at a glance. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]
3. Click a feature table name to view its dedicated page. The **Producers** table lists all notebooks and jobs that write to that table. The **Last updated** column displays the most recent write timestamp for each producer, enabling you to confirm that scheduled jobs are running and the feature table is fresh. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

![Feature store page showing last updated column](https://docs.databricks.com/aws/en/assets/images/feature-store-ui-14cd6020583d17242ddb0c0275b86222.png)

## Importance

Monitoring freshness provides visibility into the health of your feature engineering pipelines. By checking the last write time, you can detect when a scheduled job has stopped running or is delayed, and take corrective action before stale data affects model predictions. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Related concepts

- [[Feature Store]] – Central repository for storing and serving features.
- [[Feature Lineage Tracking|Feature Lineage]] – Tracks the data sources and jobs that create features, complementing freshness monitoring.
- [[Delta table versioning|Feature Table Versioning]] – Manages different versions of feature tables.
- MLOps – Practices for operationalizing machine learning, including data pipeline monitoring.

## Sources

- explore-features-and-lineage-legacy-databricks-on-aws.md
```

# Citations

1. [explore-features-and-lineage-legacy-databricks-on-aws.md](/references/explore-features-and-lineage-legacy-databricks-on-aws-6e819774.md)
