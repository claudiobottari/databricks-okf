---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5bca51f0e70e3cb066fd53994ab672b20aaf478b64fd63d299e271278935f3f7
  pageDirectory: concepts
  sources:
    - feature-governance-and-lineage-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-feature-table-access-control
    - UCFTAC
  citations:
    - file: feature-governance-and-lineage-databricks-on-aws.md
title: Unity Catalog Feature Table Access Control
description: Access control for Databricks Feature Store feature tables is managed through Unity Catalog privileges
tags:
  - governance
  - unity-catalog
  - access-control
timestamp: "2026-06-19T10:29:42.900Z"
---

# Unity Catalog Feature Table Access Control

**Unity Catalog Feature Table Access Control** governs who can read, write, and manage feature tables stored in Unity Catalog. Access control is managed entirely through Unity Catalog's privilege system, and lineage between feature tables, functions, and models is automatically tracked when models are logged using the Feature Engineering client. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Overview

Feature tables in Unity Catalog are governed by the same [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md) model used for other securable objects. This means administrators can grant or revoke permissions on feature tables using standard SQL or the Catalog Explorer interface, without needing separate feature-store-specific access controls. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Managing Access

To control access to a feature table, use Unity Catalog's privilege management tools. Users and service principals require appropriate privileges — such as `SELECT`, `MODIFY`, or `OWNERSHIP` — to read from or write to feature tables. For the full list of available privileges and how to grant them, see the [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md) documentation. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Automatic Lineage Tracking

When you log a model using `FeatureEngineeringClient.log_model`, Databricks automatically captures lineage information linking the model to the feature tables and Python UDFs used during training. This lineage is visible in the **Lineage** tab of Catalog Explorer for the feature table, model version, or function. ^[feature-governance-and-lineage-databricks-on-aws.md]

### What Gets Tracked

- **Feature tables** referenced via `FeatureLookup` in the training set are linked to the logged model. ^[feature-governance-and-lineage-databricks-on-aws.md]
- **Python UDFs** used for on-demand feature computation (via `FeatureFunction`) are also tracked. ^[feature-governance-and-lineage-databricks-on-aws.md]

### Viewing Lineage

1. Navigate to the feature table, model version, or function page in Catalog Explorer.
2. Select the **Lineage** tab. The left sidebar shows Unity Catalog components logged with that object.
3. Click **See lineage graph** to view the full lineage visualization. ^[feature-governance-and-lineage-databricks-on-aws.md]

The lineage graph shows how feature tables, functions, and models are connected, enabling impact analysis and data provenance tracking. For more details on exploring the lineage graph, see [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md). ^[feature-governance-and-lineage-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md) — The permission model governing all Unity Catalog objects
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) — The API used to log models and capture lineage
- [Feature Lookup](/concepts/feature-lookup.md) — How features are referenced from feature tables during training
- [Feature Function](/concepts/feature-function.md) — On-demand feature computation using Python UDFs
- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) — Broader lineage capabilities across Unity Catalog
- [Data Profiling](/concepts/data-profiling.md) — Monitoring feature table data changes and model performance

## Sources

- feature-governance-and-lineage-databricks-on-aws.md

# Citations

1. [feature-governance-and-lineage-databricks-on-aws.md](/references/feature-governance-and-lineage-databricks-on-aws-4bd9813b.md)
