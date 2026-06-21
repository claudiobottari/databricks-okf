---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e47930a94f0aadd0968cf1a67523a66fa7b7e1a23cea8bc9fd127a15a227671f
  pageDirectory: concepts
  sources:
    - explore-features-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-lineage-in-unity-catalog
    - FLIUC
  citations:
    - file: explore-features-in-unity-catalog-databricks-on-aws.md
title: Feature Lineage in Unity Catalog
description: Tracking of data sources used to create feature tables and tracking of downstream consumers including models, notebooks, jobs, and endpoints that use each feature.
tags:
  - lineage
  - governance
  - unity-catalog
timestamp: "2026-06-18T12:16:04.791Z"
---

# Feature Lineage in Unity Catalog

**Feature Lineage** in Unity Catalog tracks the relationships between [Feature Tables](/concepts/feature-tables.md), the data sources used to create them, and the downstream consumers that use those features — including MLflow models, notebooks, jobs, and endpoints. Lineage is one of the core governance capabilities provided by [Unity Catalog](/concepts/unity-catalog.md) for all feature tables, alongside feature discovery, cross-workspace access, and permission inheritance.^[explore-features-in-unity-catalog-databricks-on-aws.md]

## What Lineage Tracks

When you create a feature table in Databricks, Unity Catalog automatically records:
- The data sources ([Delta tables](/concepts/delta-lake-table.md), external data sources, or view definitions) that were used to build the feature table.
- For each individual feature within a feature table, the MLflow models, notebooks, jobs, and [endpoints](/concepts/serving-endpoint-acls.md) that consume that feature.

This bidirectional lineage allows data practitioners to answer both "where did this feature come from?" and "what uses this feature?" questions.^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Lineage in Catalog Explorer

You can explore and manage lineage for any feature table through [Catalog Explorer](/concepts/catalog-explorer.md). Click on a feature table name in the Features UI to open it in Catalog Explorer, where the **Lineage** tab displays:
- Upstream sources: the original datasets, pipelines, and transformations that fed into the feature table.
- Downstream consumers: the models, notebooks, jobs, and endpoints that reference individual features from the table.^[explore-features-in-unity-catalog-databricks-on-aws.md, explore-features-in-unity-catalog-databricks-on-aws.md]

## How Lineage Benefits Governance

Lineage supports several governance and operational workflows:

### Impact Analysis

When a source dataset changes schema or is removed, lineage shows which feature tables depend on it and which models or jobs would be affected — enabling proactive communication before breaking downstream consumers.^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Model Certification

Because MLflow models inherit permissions from the data they were trained on, lineage provides an audit trail that links a model back to the specific features and feature versions it used. This supports compliance requirements and model governance.^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Reproducibility

Lineage helps data scientists and ML engineers reconstruct the exact feature set used in a given model run or notebook — even if the feature table has been updated since that run.^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Viewing Lineage by Feature

For each individual feature in a feature table, you can see:
- The feature name and type.
- The models that reference that feature.
- The notebooks or jobs that read or write that feature.
- The endpoints serving that feature for online inference.

Lineage is updated automatically as consumers register their usage.^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Lineage in the Features UI

The [Features UI](/concepts/feature-store.md) in the Databricks sidebar also surfaces lineage metadata at the feature-table level:
- **Owner**: who manages the feature table.
- **Online stores**: where the feature has been published for low-latency serving.
- **Last write time**: the most recent notebook or job that wrote to the table.
- **Tags**: key-value annotations attached to the table.
- **Comments**: descriptive text for the table.

You can search for feature tables by name, feature name, comment, or tag to locate tables with relevant lineage.^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Feature Tables](/concepts/feature-tables.md) — Delta tables with primary key constraints, managed by Unity Catalog.
- MLflow Models — Models that inherit permissions from training data and reference features in lineage.
- [Catalog Explorer](/concepts/catalog-explorer.md) — UI tool for browsing and managing Unity Catalog assets, including lineage.
- [Unity Catalog](/concepts/unity-catalog.md) — The overarching governance layer that provides lineage tracking.
- [Data Lineage](/concepts/data-lineage.md) — The broader concept of tracking data movement across systems.
- [Model Governance](/concepts/ai-governance.md) — Applying lineage to model certification and audit trails.

## Sources

- explore-features-in-unity-catalog-databricks-on-aws.md

# Citations

1. [explore-features-in-unity-catalog-databricks-on-aws.md](/references/explore-features-in-unity-catalog-databricks-on-aws-b44ec93d.md)
