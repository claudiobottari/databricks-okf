---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 094b1c07c8a86129520b04af11b6befdb7e89746514c9376705ced1b4f5f1278
  pageDirectory: concepts
  sources:
    - databricks-feature-store-databricks-on-aws.md
    - explore-features-and-lineage-legacy-databricks-on-aws.md
    - explore-features-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - feature-lineage-tracking
    - FLT
    - Feature Lineage
    - Feature lineage
    - Feature tracing
    - feature lineage
    - lineage tracking
  citations:
    - file: explore-features-and-lineage-legacy-databricks-on-aws.md
    - file: databricks-feature-store-databricks-on-aws.md
    - file: explore-features-in-unity-catalog-databricks-on-aws.md
title: Feature Lineage Tracking
description: Automatic tracking of which features from the Feature Store were used to train a model, enabling governance and reproducibility.
tags:
  - machine-learning
  - governance
  - lineage
timestamp: "2026-06-19T18:11:54.743Z"
---

---  
title: Feature Lineage Tracking  
summary: Automatic lineage tracking from models to the features used during training, enabling governance, reproducibility, and automated feature lookup at inference time.  
sources:  
  - databricks-feature-store-databricks-on-aws.md  
  - explore-features-and-lineage-legacy-databricks-on-aws.md  
  - explore-features-in-unity-catalog-databricks-on-aws.md  
kind: concept  
createdAt: "2026-06-18T12:15:35.833Z"  
updatedAt: "2026-06-19T09:50:46.976Z"  
tags:  
  - lineage  
  - governance  
  - ml-ops  
aliases:  
  - feature-lineage-tracking  
  - FLT  
confidence: 0.9  
provenanceState: merged  
inferredParagraphs: 1  
---

# Feature Lineage Tracking

**Feature Lineage Tracking** is the ability to trace the complete lifecycle of a feature — from its raw data sources and computation pipelines through to the models that consume it in training and inference. In the Databricks environment, lineage is captured by both the legacy Workspace Feature Store and the Unity Catalog‑backed Feature Engineering system. ^[explore-features-and-lineage-legacy-databricks-on-aws.md, databricks-feature-store-databricks-on-aws.md]

## Overview

Feature lineage enables data scientists and ML engineers to understand where features come from, how they are computed, and which models depend on them. This visibility is critical for debugging, compliance, model retraining, and impact analysis when source data changes. ^[explore-features-and-lineage-legacy-databricks-on-aws.md, databricks-feature-store-databricks-on-aws.md]

## Lineage in the Workspace Feature Store UI (Legacy)

In the legacy Workspace Feature Store, lineage is tracked through the feature table UI and covers both producers and consumers of features. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

### Producers (How Features Were Created)

The **Producers** table on a feature table page provides information about all notebooks and jobs that write to that feature table. This allows you to confirm the status of scheduled jobs and assess the freshness of the feature table. Tracked producer metadata includes: ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

- The raw data sources used to compute the feature table.
- Notebooks and jobs that compute the features.
- The last time a notebook or job wrote to the feature table.

### Consumers (Where Features Are Used)

The **Features** table lists every feature in the table and provides links to: ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

- Models trained using the feature.
- Serving endpoints that access the feature.
- Jobs and notebooks that read the feature.
- Online stores where the feature has been published.

### Search by Lineage

Users can search for feature tables by entering all or part of a feature name, data source, or tag key/value (case‑insensitive). This enables discovery of feature tables based on their lineage relationships. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Lineage with Unity Catalog Feature Engineering

When feature tables are managed in [Unity Catalog](/concepts/unity-catalog.md), lineage is automatically captured and augmented with full Unity Catalog governance. For each feature in a feature table, users can access the models, notebooks, jobs, and endpoints that use that feature. ^[explore-features-in-unity-catalog-databricks-on-aws.md, databricks-feature-store-databricks-on-aws.md]

### Training Set Lineage

When a feature table is used to train a model, the model automatically tracks lineage to the features that were used in training. At inference time, the model automatically looks up the latest feature values from the online store, and all feature computation is handled by the Feature Store. This eliminates training/serving skew and simplifies client‑side code. ^[databricks-feature-store-databricks-on-aws.md]

### Cross‑Workspace Lineage

Because feature tables, functions, and models are governed by Unity Catalog, they are automatically available in any workspace that has access to the catalog. Cross‑workspace lineage is preserved, so a model trained in one workspace can reference features registered in another, and the lineage still appears in both environments. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Feature Freshness

Lineage tracking includes freshness information. The Workspace Feature Store UI displays the last time a notebook or job wrote to a feature table, allowing users to confirm whether scheduled feature computation jobs are running on time. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Use Cases

### Impact Analysis

When a source data table changes or a feature computation pipeline fails, lineage tracking helps identify all downstream models that depend on the affected features, enabling targeted retraining or alerting. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

### Debugging and Auditing

Lineage allows teams to trace prediction quality issues back to their root cause — whether it originated in raw data quality, feature computation logic, or model training. It also supports compliance requirements by documenting the provenance of features used in production models. ^[explore-features-and-lineage-legacy-databricks-on-aws.md, databricks-feature-store-databricks-on-aws.md]

### Model Reproducibility

By recording which features (and which versions of feature computation logic) were used during training, lineage enables exact reproduction of training datasets for debugging or model re‑evaluation. ^[databricks-feature-store-databricks-on-aws.md]

## Related Concepts

- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) — The legacy feature store that provides the UI for lineage exploration.
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — The Unity Catalog‑backed system for feature management with automatic lineage.
- [Point-in-time correctness](/concepts/point-in-time-correctness.md) — Ensures feature values are computed using only data available before each row's timestamp.
- [Model Serving](/concepts/model-serving.md) — The serving infrastructure that uses stored feature metadata for inference.
- [Online Feature Store](/concepts/online-feature-store.md) — Where features are published for low‑latency serving.

## Sources

- databricks-feature-store-databricks-on-aws.md
- explore-features-and-lineage-legacy-databricks-on-aws.md
- explore-features-in-unity-catalog-databricks-on-aws.md

# Citations

1. [explore-features-and-lineage-legacy-databricks-on-aws.md](/references/explore-features-and-lineage-legacy-databricks-on-aws-6e819774.md)
2. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
3. [explore-features-in-unity-catalog-databricks-on-aws.md](/references/explore-features-in-unity-catalog-databricks-on-aws-b44ec93d.md)
