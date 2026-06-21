---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b8d3e4b6874d57a3173eaf44b117c5506ec9ff9a96e9a169e12291d46fd7cff3
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-lineage-and-online-workflows
    - Online Workflows and Feature Lineage
    - FLAOW
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Feature Lineage and Online Workflows
description: Models trained using Databricks features automatically track lineage to those features; when deployed as serving endpoints, they use Unity Catalog to resolve and look up the correct features in online stores for real-time inference.
tags:
  - model-serving
  - lineage
  - unity-catalog
timestamp: "2026-06-19T09:53:10.395Z"
---

## Feature Lineage and Online Workflows

**Feature Lineage and Online Workflows** refers to the automatic tracking of which features a machine learning model was trained on, and the subsequent use of that lineage information to serve the correct features during real-time inference. In Databricks, this capability is built into the [Feature Engineering in Databricks|Feature Store](/concepts/feature-store-and-feature-engineering.md) and [Unity Catalog](/concepts/unity-catalog.md), enabling seamless transitions from offline training to online serving. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Automatic Lineage Tracking

When a model is trained using features published in the Databricks Feature Store, the training process automatically captures lineage — a record of exactly which feature table and columns were used. This lineage is stored in [Unity Catalog](/concepts/unity-catalog.md) alongside the model. No manual annotation or separate bookkeeping is required. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Online Workflows

Once a model with tracked feature lineage is deployed as a [Model Serving Endpoint](/concepts/model-serving-endpoint.md), it automatically discovers the features it needs by querying Unity Catalog. The endpoint then looks up the latest values for those features from an [Online Feature Store](/concepts/online-feature-store.md). This allows the model to compute predictions on fresh input data without the application needing to explicitly fetch or manage feature tables. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Dependencies and Infrastructure

The online workflow depends on:

- An [Online Feature Store](/concepts/online-feature-store.md) that has been created and has feature tables published to it via the `publish_table` API.
- A [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) (or Model Serving Endpoint) that is configured to use the features discovered through lineage.
- Unity Catalog serving as the central metadata store for both the offline feature table and the model’s lineage.

For detailed guidance on setting up and using online workflows, see the dedicated documentation on [Use features in online workflows](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-workflows). ^[databricks-online-feature-stores-databricks-on-aws.md]

## Benefits

- **Consistency**: The same features used during training are automatically retrieved during inference, reducing the risk of training-serving skew.
- **Simplicity**: Application code does not need to know the details of feature tables; the model endpoint handles lookup via Unity Catalog.
- **Governance**: Lineage is stored in Unity Catalog, providing auditability and enabling impact analysis when features change.

## Related Concepts

- [Online Feature Stores](/concepts/online-feature-store.md)
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Feature Engineering in Databricks](/concepts/feature-engineering-on-databricks.md)
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md)
- [Publish a feature table to an online store](/concepts/publishing-feature-tables-to-online-stores.md)

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
