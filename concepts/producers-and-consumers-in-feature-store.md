---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a553ffb80373dce17efa9197147400f113e4e682164efd32673a02870d354bdb
  pageDirectory: concepts
  sources:
    - explore-features-and-lineage-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - producers-and-consumers-in-feature-store
    - Consumers in Feature Store and Producers
    - PACIFS
  citations:
    - file: explore-features-and-lineage-legacy-databricks-on-aws.md
title: Producers and Consumers in Feature Store
description: A lineage concept distinguishing notebooks and jobs that write to a feature table (producers) from models, endpoints, notebooks, and jobs that read from it (consumers).
tags:
  - feature-store
  - lineage
  - governance
timestamp: "2026-06-19T10:26:36.107Z"
---

# Producers and Consumers in Feature Store

**Producers and Consumers in Feature Store** refers to the two main roles that notebooks and jobs play in the lifecycle of feature tables within Databricks Workspace Feature Store. Producers write data to feature tables, while consumers read from feature tables for training, inference, or other downstream tasks.

## Producers

Producers are the notebooks and jobs that compute and write features to a feature table. The **Producers** table in the Workspace Feature Store UI[^] provides information about all notebooks and jobs that write to a given feature table. This view allows users to confirm the status of scheduled jobs and the freshness of the feature table. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

Key information tracked for producers includes:
- Notebooks and jobs that write to the feature table
- The status of scheduled jobs
- Feature freshness indicators
- The last time a notebook or job wrote to the feature table ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Consumers

Consumers are the models, endpoints, jobs, and notebooks that read or use features from a feature table. The **Features** table in the UI provides links to all consumers that use a particular feature, enabling full [feature lineage](/concepts/feature-lineage-tracking.md) tracking. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

Consumers tracked in the Feature Store include:
- Models trained using the feature
- Serving endpoints that access the feature
- Jobs and notebooks that read the feature
- Online stores where the feature has been published ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Lineage Tracking

The interaction between producers and consumers creates a complete lineage graph for each feature. You can track both how a feature was created and where it is used, including: ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

- Raw data sources used to compute the features
- Notebooks and jobs that performed the computation
- Online stores where the feature is published
- Models trained with the feature
- Serving endpoints that access the feature
- Notebooks and jobs that read the feature

This lineage information helps with data governance, debugging, impact analysis, and ensuring feature freshness for production deployments.

## Related Concepts

- [Feature Store](/concepts/feature-store.md)
- [Feature Lineage](/concepts/feature-lineage-tracking.md)
- [Feature Tables](/concepts/feature-tables.md)
- [Model Serving](/concepts/model-serving.md)
- Feature Freshness

## Sources

- explore-features-and-lineage-legacy-databricks-on-aws.md

# Citations

1. [explore-features-and-lineage-legacy-databricks-on-aws.md](/references/explore-features-and-lineage-legacy-databricks-on-aws-6e819774.md)
