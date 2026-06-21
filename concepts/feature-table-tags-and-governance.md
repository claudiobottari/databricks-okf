---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3701d6cbd2afbb12ed1dd43ad84be9c34f01bde08da5d9a01cf3c9be3e7fe1d5
  pageDirectory: concepts
  sources:
    - feature-tables-in-unity-catalog-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-table-tags-and-governance
    - Governance and Feature Table Tags
    - FTTAG
    - feature-table-tagging-and-governance
    - governance and Feature table tagging
  citations:
    - file: feature-tables-in-unity-catalog-databricks-on-aws.md
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
    - file: best-practices-for-abac-policies-databricks-on-aws.md
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: Feature Table Tags and Governance
description: Tags (key-value pairs) can be applied to feature tables and individual features via Catalog Explorer, SQL, or Python API for categorization and governance.
tags:
  - governance
  - tagging
  - unity-catalog
  - feature-store
timestamp: "2026-06-18T12:19:44.662Z"
---

# Feature Table Tags and Governance

**Feature Table Tags and Governance** refers to the use of metadata tags — simple key-value pairs — on feature tables and individual features within [Unity Catalog](/concepts/unity-catalog.md) to organize, categorize, and govern feature assets across the machine learning lifecycle. Tags enable search, classification, and attribute-based access control for feature tables managed by [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md).

## Overview

In Unity Catalog, any Delta table with a primary key constraint can serve as a feature table. These feature tables, like other data assets in Unity Catalog, support tagging as a governance mechanism. Tags are key-value pairs that can be applied to both feature tables and individual features within those tables, enabling teams to manage and discover feature assets at scale. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Tag Management

### Feature Table Tags

You can create, edit, and delete tags on feature tables using three methods: Catalog Explorer, SQL statements in a notebook or SQL query editor, or the Feature Engineering Python API. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Feature-Level Tags

For individual features within a feature table, you can create, edit, and delete tags using Catalog Explorer or SQL statements. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

### Feature Engineering Python API

The [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) provides methods for managing feature table tags programmatically. The following example demonstrates creating a feature table with initial tags, updating a tag value, and deleting a tag: ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

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
fe.set_feature_table_tag(
    name="customer_feature_table",
    key="tag_key_1",
    value="new_key_value"
)

# Delete a tag
fe.delete_feature_table_tag(
    name="customer_feature_table",
    key="tag_key_2"
)
```

## Searching Feature Tables by Tags

The Features UI supports searching for feature tables by entering all or part of the key or value of a tag. Search text is case-insensitive. This enables users to quickly locate feature tables based on governance classifications, project associations, or other metadata categories. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

To search by tags:

1. Click **Features** in the sidebar to display the Features UI.
2. Select a catalog using the catalog selector.
3. In the search box, enter all or part of a tag key or value, along with other search criteria such as feature table name, feature name, or comment. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Integration with Unity Catalog Governance

Feature table tags integrate with the broader [Unity Catalog](/concepts/unity-catalog.md) governance model. Tags can be used in conjunction with [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies to control access to feature tables based on tag values. For example, tags such as `classification` or `data_sensitivity` can drive [ABAC GRANT Policy](/concepts/abac-grant-policy.md) or [Column Mask Policies](/concepts/column-mask-policies.md) that restrict or mask feature data for specific users or groups. ^[feature-tables-in-unity-catalog-databricks-on-aws.md, abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Best Practices

- **Establish a tagging taxonomy** before applying tags at scale. Define consistent tag keys (e.g., `project`, `domain`, `data_classification`, `owner`) and allowed values to ensure discoverability and governance effectiveness. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Use governed tags for ABAC policies.** When using tags to drive access control, apply [Governed Tags](/concepts/governed-tags.md) that are controlled and auditable, rather than free-form tags that users can arbitrarily modify. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Document the tagging taxonomy** and governance model so teams can understand expected tag usage patterns and identify anomalous changes in the audit log. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Audit tag changes regularly** to detect unauthorized modifications. Restrict tag creation and modification to authorized data stewards or governance admins. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Audit Logging for Tag Operations

Changes to governed tags are logged in the [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) (`system.access.audit`). The following tag-related actions are recorded under the `service_name = 'unityCatalog'`: ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

| Action Name | Description |
|-------------|-------------|
| `createEntityTagAssignment` | A tag is assigned to a securable object |
| `deleteEntityTagAssignment` | A tag is removed from a securable object |

## Related Concepts

- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — The framework for managing feature tables
- [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) — Python client for feature table operations
- Unity Catalog Tags — Tagging system for all Unity Catalog securable objects
- [Governed Tags](/concepts/governed-tags.md) — Controlled tags suitable for ABAC policy conditions
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Access control model that can use tags for policy evaluation
- [Data Classification](/concepts/data-classification.md) — Automatic detection and tagging of sensitive columns
- [ABAC Policy Audit Logging](/concepts/abac-policy-audit-logging.md) — Auditing of tag and policy operations

## Sources

- feature-tables-in-unity-catalog-databricks-on-aws.md
- abac-grant-policies-for-models-beta-databricks-on-aws.md
- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [feature-tables-in-unity-catalog-databricks-on-aws.md](/references/feature-tables-in-unity-catalog-databricks-on-aws-f1336f1e.md)
2. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
3. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
4. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)
