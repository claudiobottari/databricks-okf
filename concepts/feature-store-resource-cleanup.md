---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d02b0b03f42295fefbc9fa3061539d3ad19be1bc05e0cfdcd9fddc3b99470b0e
  pageDirectory: concepts
  sources:
    - materialize-declarative-features-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-store-resource-cleanup
    - FSRC
  citations:
    - file: materialize-declarative-features-databricks-on-aws.md
title: Feature Store Resource Cleanup
description: Background asynchronous cleanup process that removes tables, pipelines, and jobs when the last materialized feature referencing those resources is deleted, using a Databricks-managed system service principal.
tags:
  - feature-store
  - resource-management
  - cleanup
timestamp: "2026-06-19T19:31:17.722Z"
---

## Feature Store Resource Cleanup

**Feature Store Resource Cleanup** refers to the automatic, asynchronous removal of infrastructure — such as Delta tables, online tables, materialization pipelines, and orchestration jobs — that is triggered when materialized features are deleted in Databricks Feature Store. This cleanup is managed by a background process to ensure that resources are only freed after all associated features have been removed. ^[materialize-declarative-features-databricks-on-aws.md]

### How Deletion Works

Before deleting a materialized feature, you must first remove or update any models or feature specs that reference that feature. ^[materialize-declarative-features-databricks-on-aws.md]

The specific object to pass to `delete_materialized_feature()` depends on the feature type:

- **Aggregation features**: Pass the offline materialized feature. Deleting the offline feature also deletes its paired online materialized feature. ^[materialize-declarative-features-databricks-on-aws.md]
- **ColumnSelection features**: Pass the online materialized feature only. ColumnSelection features are materialized solely to the online store, so there is no paired offline feature to delete. ^[materialize-declarative-features-databricks-on-aws.md]

When a materialized feature is deleted, Databricks removes the feature metadata immediately. However, because multiple materialized features can share the same underlying tables and pipelines, those shared resources are not removed until **every** materialized feature that references them has been deleted. ^[materialize-declarative-features-databricks-on-aws.md]

### Background Resource Cleanup

After the last materialized feature in a group is deleted, a background process automatically removes the following resources:

- The offline Delta tables containing the materialized feature data
- The online tables, if the features were materialized to an online store
- The materialization pipeline
- The orchestration job

This cleanup is performed by a Databricks-managed system service principal. No action is required from the user. The cleanup is fully managed by the feature store. There may be a short delay between deleting the last materialized feature and the actual removal of the associated tables and other resources. ^[materialize-declarative-features-databricks-on-aws.md]

### Limitations

- Materialized features can only be deleted in the workspace where they were created. ^[materialize-declarative-features-databricks-on-aws.md]
- For materialized aggregation features, the online materialized feature cannot be deleted directly. You must delete the paired offline materialized feature; the change propagates to both. ^[materialize-declarative-features-databricks-on-aws.md]
- For materialized aggregation features created before April 20, 2026, the materialization pipeline continues producing new feature values until **all** materialized features in the pipeline have been deleted, which then triggers resource cleanup. To create an updated pipeline that supports per-feature delete, delete and re-materialize the feature. ^[materialize-declarative-features-databricks-on-aws.md]
- For materialized ColumnSelection features, the materialization pipeline likewise continues producing new feature values until all materialized features in the pipeline have been deleted. ^[materialize-declarative-features-databricks-on-aws.md]

### Related Concepts

- materialize_features() API|Materialized Feature – A precomputed representation of a declarative feature in Unity Catalog.
- [Declarative Features](/concepts/declarative-feature-engineering-api.md) – Feature definitions that specify how to compute feature values from source tables.
- [Feature Store](/concepts/feature-store.md) – Centralized repository for managing ML features.
- [Online Feature Store](/concepts/online-feature-store.md) – Low-latency store used for model serving.
- [Delta Tables](/concepts/delta-lake-table.md) – Storage format for offline materialized feature data.
- Materialization Pipeline – The pipeline that populates feature tables on a schedule or trigger.

### Sources

- materialize-declarative-features-databricks-on-aws.md

# Citations

1. [materialize-declarative-features-databricks-on-aws.md](/references/materialize-declarative-features-databricks-on-aws-fe7c4a29.md)
