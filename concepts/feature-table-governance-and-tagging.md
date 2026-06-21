---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c0706202e96c91c84f4cf2b98925f71d7bcf847510e3573d821cd13203c7e0a3
  pageDirectory: concepts
  sources:
    - feature-tables-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-table-governance-and-tagging
    - Tagging and Feature Table Governance
    - FTGAT
  citations:
    - file: feature-tables-in-unity-catalog-databricks-on-aws.md
title: Feature Table Governance and Tagging
description: Feature tables in Unity Catalog can be browsed, searched, and managed via the Features UI and Catalog Explorer, with support for tags (key-value pairs) for categorization.
tags:
  - governance
  - unity-catalog
  - catalog-explorer
timestamp: "2026-06-19T18:49:01.415Z"
---

# Feature Table Governance and Tagging

**Feature Table Governance and Tagging** refers to the set of capabilities in Databricks Unity Catalog that enable organizations to manage, categorize, and control access to feature tables used in machine learning workflows. These capabilities include primary key constraints, metadata management, tagging, search, and access control.

## Overview

In Unity Catalog, any Delta table with a primary key constraint can serve as a feature table. Feature tables are accessed using a three-level namespace: `<catalog-name>.<schema-name>.<table-name>`. This integration with Unity Catalog provides centralized governance, allowing feature tables to be managed alongside other data assets using the same security and metadata frameworks. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

Feature tables in Unity Catalog are accessible to all workspaces assigned to the table's Unity Catalog [Metastore](/concepts/metastore.md). To share feature tables with workspaces not assigned to the same [Metastore](/concepts/metastore.md), organizations can use [OpenSharing](/concepts/opensharing.md) via [Delta Sharing](/concepts/delta-sharing.md). ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Primary Key Constraints

A primary key constraint is required for any table to function as a feature table. Only the table owner can declare primary key constraints. The owner's name is displayed on the table detail page of [Catalog Explorer](/concepts/catalog-explorer.md). ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

To add a primary key to an existing Delta table, first set the primary key columns to `NOT NULL`, then add the constraint:

```sql
ALTER TABLE <full_table_name> ALTER COLUMN <pk_col_name> SET NOT NULL;
ALTER TABLE <full_table_name> ADD CONSTRAINT <pk_name> PRIMARY KEY(pk_col1, pk_col2, ...);
```

By convention, the primary key constraint name uses the table name (without schema and catalog) with a `_pk` suffix. For example, a table named `ml.recommender_system.customer_features` would have `customer_features_pk` as its primary key constraint name. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

For [Time Series Feature Tables](/concepts/time-series-feature-tables.md), specify the `TIMESERIES` keyword on one of the primary key columns. This requires Databricks Runtime 13.3 LTS or above. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Feature Table Tags

Tags are simple key-value pairs used to categorize and manage feature tables and features. Tags enable search and discovery of feature tables through the Features UI. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Managing Tags

For feature tables, tags can be created, edited, and deleted using:
- [Catalog Explorer](/concepts/catalog-explorer.md)
- SQL statements in a notebook or SQL query editor
- The [Feature Engineering Python API](/concepts/featureengineeringclient-python-client.md)

For individual features within a table, tags can be created, edited, and deleted using Catalog Explorer or SQL statements. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Tag Operations with the Python API

The `FeatureEngineeringClient` provides methods for managing feature table tags:

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()

# Create feature table with tags
customer_feature_table = fe.create_table(
  # ...
  tags={"tag_key_1": "tag_value_1", "tag_key_2": "tag_value_2", ...},
  # ...
)

# Upsert a tag
fe.set_feature_table_tag(name="customer_feature_table", key="tag_key_1", value="new_key_value")

# Delete a tag
fe.delete_feature_table_tag(name="customer_feature_table", key="tag_key_2")
```

^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Search and Discovery

The Features UI provides search and browsing capabilities for feature tables in Unity Catalog. Users can search by:
- All or part of a feature table name
- Feature names
- Comments
- Tag keys or values

Search text is case-insensitive. The catalog selector allows users to view all available feature tables within a specific catalog. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Metadata Management

The `get_table` method retrieves feature table metadata, including the list of features:

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()
ft = fe.get_table(name="ml.recommender_system.user_feature_table")
print(ft.features)
```

^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Feature Table Deletion

Deleting a feature table can be done through Catalog Explorer or the Feature Engineering Python API. Important considerations include:
- Deleting a feature table can cause unexpected failures in upstream producers and downstream consumers (models, endpoints, and scheduled jobs).
- Published online stores must be deleted separately with the cloud provider.
- When a feature table is deleted in Unity Catalog, the underlying Delta table is also dropped.
- The `drop_table` method is not supported in Databricks Runtime 13.1 ML or below; use the SQL `DROP TABLE` command instead.

^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for managing data assets including feature tables.
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — The framework for creating and managing feature tables.
- [Catalog Explorer](/concepts/catalog-explorer.md) — The UI for browsing and managing Unity Catalog assets.
- [Delta Sharing](/concepts/delta-sharing.md) — Mechanism for sharing feature tables across metastores.
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md) — Feature tables with time-based primary keys for point-in-time lookups.
- [Feature Engineering Python API](/concepts/featureengineeringclient-python-client.md) — Programmatic interface for feature table operations.
- [Primary Key Constraints](/concepts/primary-key-constraints-for-feature-tables.md) — Required constraint for feature tables in Unity Catalog.

## Sources

- feature-tables-in-unity-catalog-databricks-on-aws.md

# Citations

1. [feature-tables-in-unity-catalog-databricks-on-aws.md](/references/feature-tables-in-unity-catalog-databricks-on-aws-f1336f1e.md)
