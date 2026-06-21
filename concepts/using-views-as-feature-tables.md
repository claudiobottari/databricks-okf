---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ce69244777dcb8ec1fda789d8789e13d4de09dad6b9684f455849380a3dc1522
  pageDirectory: concepts
  sources:
    - feature-tables-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - using-views-as-feature-tables
    - UVAFT
  citations:
    - file: feature-tables-in-unity-catalog-databricks-on-aws.md
title: Using Views as Feature Tables
description: Simple SELECT views over Delta tables in Unity Catalog can serve as feature tables for offline training, but cannot be published to online stores or used for model serving.
tags:
  - feature-store
  - views
  - unity-catalog
timestamp: "2026-06-19T18:48:56.222Z"
---

## Using Views as Feature Tables

In Unity Catalog, a simple SELECT view can serve as a feature table when the underlying Delta table has a primary key and the view definition selects from that table without transformations that remove or aggregate the key. This approach allows you to create lightweight, query-based feature tables that expose a subset of rows or columns from an existing Delta table without duplicating data.

### Requirements

- `databricks-feature-engineering` version 0.7.0 or above. This client is pre-installed in Databricks Runtime 16.0 ML and later.^[feature-tables-in-unity-catalog-databricks-on-aws.md]
- A **simple SELECT view**, defined as a view created from a single Delta table in Unity Catalog that can serve as a feature table. The view’s primary keys must be selected **without** `JOIN`, `GROUP BY`, or `DISTINCT` clauses. Acceptable keywords in the SQL statement are: `SELECT`, `FROM`, `WHERE`, `ORDER BY`, `LIMIT`, and `OFFSET`.^[feature-tables-in-unity-catalog-databricks-on-aws.md]
- The underlying Delta table must have a [Primary Key Constraint](/concepts/primary-key-constraint-for-feature-tables.md) defined. If the table does not, you must add one using `ALTER TABLE ... ADD CONSTRAINT` before creating the view.^[feature-tables-in-unity-catalog-databricks-on-aws.md]
- Supported data types must match those allowed by Feature Engineering in Unity Catalog (see Supported Data Types for Feature Tables).^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Limitations

- Feature tables backed by views **do not appear** in the Features UI. They can only be accessed programmatically through the `FeatureEngineeringClient` API.^[feature-tables-in-unity-catalog-databricks-on-aws.md]
- If columns are renamed in the source Delta table, the column names in the view’s `SELECT` statement must be updated to match.^[feature-tables-in-unity-catalog-databricks-on-aws.md]
- Views as feature tables can be used for **offline model training and evaluation only**. They **cannot** be published to online stores. Features derived from these tables, and models based on those features, cannot be served via [Model Serving](/concepts/model-serving.md) or online endpoints.^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Example

The following SQL creates a view that selects a filtered subset of columns and rows from a feature table called `content_recommendations_features`. The view retains the primary keys `user_id` and `content_id` from the underlying table and applies `WHERE` and `ORDER BY` clauses, which are permitted in a simple SELECT view.^[feature-tables-in-unity-catalog-databricks-on-aws.md]

```sql
CREATE OR REPLACE VIEW ml.recommender_system.content_recommendation_subset AS
SELECT
    user_id,
    content_id,
    user_age,
    user_gender,
    content_genre,
    content_release_year,
    user_content_watch_duration,
    user_content_like_dislike_ratio
FROM
    ml.recommender_system.content_recommendations_features
WHERE
    user_age BETWEEN 18 AND 35
    AND content_genre IN ('Drama', 'Comedy', 'Action')
    AND content_release_year >= 2010
    AND user_content_watch_duration > 60;
```

After the view is created, you can use the `FeatureEngineeringClient` API to read from it (e.g., `fe.read_table(name='ml.recommender_system.content_recommendation_subset')`) and use it as a feature table in Training Sets for offline training.

### When to Use Views as Feature Tables

Use a view when you need to:

- Expose a filtered or projected subset of an existing Delta table as features without copying data.
- Apply row-level or column-level security through the view definition.
- Avoid maintaining a separate feature table for subsets that are derived from one authoritative source.

Do **not** use a view when:

- You need to serve features to online models (e.g., real-time inference). For online serving, use a standard feature table backed by a Delta table with a primary key.
- The view requires joins, aggregations, or `DISTINCT` — those operations are not allowed for simple SELECT views.
- You want the feature table to appear in the Features UI for discovery via Catalog Explorer.

### Related Concepts

- [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md)
- [Primary Key Constraints](/concepts/primary-key-constraints-for-feature-tables.md)
- Training Sets
- [Model Serving](/concepts/model-serving.md)
- [Feature Engineering Client API](/concepts/featureengineeringclient-api.md)
- Online Stores for Feature Tables

### Sources

- feature-tables-in-unity-catalog-databricks-on-aws.md

# Citations

1. [feature-tables-in-unity-catalog-databricks-on-aws.md](/references/feature-tables-in-unity-catalog-databricks-on-aws-f1336f1e.md)
