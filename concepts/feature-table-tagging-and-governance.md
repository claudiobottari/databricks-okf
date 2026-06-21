---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fe5f6ad6545b5b8f74108c78c51e1bb0aade2fda19b9cf0267ca87c88eae8555
  pageDirectory: concepts
  sources:
    - feature-tables-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-table-tagging-and-governance
    - governance and Feature table tagging
    - FTTAG
  citations:
    - file: feature-tables-in-unity-catalog-databricks-on-aws.md
title: Feature table tagging and governance
description: Using key-value tags to categorize, search, and manage feature tables and individual features in Unity Catalog, supported via Catalog Explorer, SQL, and the Feature Engineering Python API.
tags:
  - governance
  - unity-catalog
  - metadata
timestamp: "2026-06-19T10:30:59.953Z"
---

# Feature table tagging and governance

**Feature table tagging** is a mechanism in [Unity Catalog](/concepts/unity-catalog.md) that enables users to attach key-value metadata to feature tables and their individual columns (features). Tags are used for categorization, discovery, and governance of feature assets across the data and AI lifecycle. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Overview

Feature tables in Unity Catalog are [Delta tables](/concepts/delta-lake-table.md) with a primary key constraint. They can be tagged to simplify organization, search, and management. Tags are simple key-value pairs (e.g., `"team": "recommender"`, `"pii": "false"`) that can be applied to feature tables and to individual features within a table. Tags help data teams enforce governance practices by labeling assets with ownership, sensitivity, domain, or lifecycle stage. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Tagging feature tables

Tags can be created, edited, and deleted on feature tables using:

- [Catalog Explorer](/concepts/catalog-explorer.md) (the Unity Catalog UI) ^[feature-tables-in-unity-catalog-databricks-on-aws.md]
- SQL statements in a notebook or query editor ^[feature-tables-in-unity-catalog-databricks-on-aws.md]
- The [Feature Engineering Python API](/concepts/featureengineeringclient-python-client.md) (`FeatureEngineeringClient`) ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

The following Python example shows how to create a feature table with initial tags and then upsert or delete a tag:

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()

# Create feature table with tags
customer_feature_table = fe.create_table(
  # ... other parameters ...
  tags={"tag_key_1": "tag_value_1", "tag_key_2": "tag_value_2", ...},
)

# Upsert a tag
fe.set_feature_table_tag(name="customer_feature_table",
                         key="tag_key_1",
                         value="new_key_value")

# Delete a tag
fe.delete_feature_table_tag(name="customer_feature_table",
                            key="tag_key_2")
```

^[feature-tables-in-unity-catalog-databricks-on-aws.md]

The `set_feature_table_tag` method updates an existing tag’s value or creates it if the key does not yet exist; `delete_feature_table_tag` removes a tag entirely. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Tagging individual features

Tags can also be applied to individual columns (features) within a feature table. This is useful for marking specific features as sensitive, deprecated, or experimental. For features, tags can be managed using Catalog Explorer or SQL statements; the Feature Engineering Python API does not currently provide feature-level tag methods. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Searching and browsing by tags

The Features UI supports searching feature tables by tag key or value. When a tag key or value is entered in the search box, the UI returns all matching feature tables. This capability makes tags a practical tool for governance use cases such as auditing, compliance reporting, and impact analysis. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Governance implications

While the source material does not describe explicit governance policies tied to tags, tagging is a foundational practice for [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) and other Unity Catalog governance features. Tags can later be consumed by [row filters](/concepts/row-filter-policies.md) or [column masks](/concepts/delta-lake-column-masks.md) to enforce dynamic access rules based on tag values. Tagging also supports:

- **Discovery**: Teams can quickly find feature tables relevant to their domain.
- **Ownership tracking**: A `team` or `owner` tag clarifies responsibility.
- **Lifecycle management**: Tags like `status: deprecated` or `stage: production` help manage feature lifecycle.

For general guidance on tagging Unity Catalog securable objects, see Apply tags to Unity Catalog securable objects. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Related concepts

- Unity Catalog tagging
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Feature Store in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md)
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)

## Sources

- feature-tables-in-unity-catalog-databricks-on-aws.md

# Citations

1. [feature-tables-in-unity-catalog-databricks-on-aws.md](/references/feature-tables-in-unity-catalog-databricks-on-aws-f1336f1e.md)
