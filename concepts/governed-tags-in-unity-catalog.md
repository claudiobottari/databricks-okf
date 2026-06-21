---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b8da11f17fa865806caccb12dddfc207e69b860ed7a43e65e8add61b9166934
  pageDirectory: concepts
  sources:
    - attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
    - data-discovery-in-unity-catalog-databricks-on-aws.md
    - tutorial-configure-abac-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - governed-tags-in-unity-catalog
    - GTIUC
  citations:
    - file: attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
    - file: data-discovery-in-unity-catalog-databricks-on-aws.md
    - file: tutorial-configure-abac-databricks-on-aws.md
title: Governed Tags in Unity Catalog
description: Attributes/ tags associated with securable objects that are used in ABAC policy conditions to identify which data a policy should protect.
tags:
  - unity-catalog
  - tagging
  - data-governance
timestamp: "2026-06-19T17:36:00.455Z"
---

# Governed Tags in Unity Catalog

**Governed tags** are key-value metadata labels that serve as the foundation for [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) in [Unity Catalog](/concepts/unity-catalog.md). They provide the attributes that ABAC policies reference to determine which data to protect and how.^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md] Governed tags also enable data discovery: administrators can create controlled tag vocabularies that users apply to catalog objects to organize and categorize data by topic, team, or domain, making data browseable and filterable across the catalog.^[data-discovery-in-unity-catalog-databricks-on-aws.md]

A governed tag consists of a **key** (required) and an optional **value**, along with optional **allowed values** that restrict which values can be assigned to the key. Tag keys and values are chosen arbitrarily by administrators and typically represent business concepts such as sensitivity level, data domain, or ownership group.^[tutorial-configure-abac-databricks-on-aws.md]

## Creating governed tags

To create a governed tag, you must have the `CREATE` permission on governed tags at the account level. Account admins and workspace admins have this permission by default.^[tutorial-configure-abac-databricks-on-aws.md]

In **Catalog Explorer**, navigate to **Catalog** > **Govern** > **Governed Tags**, click **Create governed tag**, enter the key (e.g., `pii`), a description, and optionally define allowed values (e.g., `ssn`, `address`). Only those allowed values can be assigned to the tag key. Click **Create** to finish.^[tutorial-configure-abac-databricks-on-aws.md]

## Applying governed tags

Tags are applied to columns (and other securable objects) using the `ALTER TABLE … ALTER COLUMN … SET TAGS` statement. Multiple tags can be applied to the same column. Example from the ABAC tutorial:^[tutorial-configure-abac-databricks-on-aws.md]

```sql
ALTER TABLE abac.customers.profiles
ALTER COLUMN SSN
SET TAGS ('pii' = 'ssn');

ALTER TABLE abac.customers.profiles
ALTER COLUMN Address
SET TAGS ('pii' = 'address');
```

## Using tags in ABAC policies

ABAC policies use two built-in functions to match tagged columns: `has_tag(tag_key)` and `has_tag_value(tag_key, tag_value)`. These functions appear in the `MATCH COLUMNS` clause of [ABAC Row Filter Policies](/concepts/abac-row-filter-policies.md) and [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md). The `MATCH COLUMNS` clause can combine multiple tag conditions with `AND` and `OR` operators.^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md, tutorial-configure-abac-databricks-on-aws.md]

For example, a column mask policy can target columns that have a specific tag value:^[tutorial-configure-abac-databricks-on-aws.md]

```sql
-- In Catalog Explorer UI, the policy is configured to:
-- Purpose: Mask column data
-- Condition: Mask column if it has specific tag (pii : ssn)
-- Function: mask_ssn (a UDF that returns '***-**-****')
```

Row filter policies use tags in `MATCH COLUMNS` to identify the column(s) that contain the filter criterion (e.g., a column tagged with `pii : address`), then use the column’s value as input to a UDF that determines whether to hide the row.^[tutorial-configure-abac-databricks-on-aws.md]

## Security considerations

Tag data (key names, values, and descriptions) is stored as plain text and may be replicated globally. Do not use tag names, values, or descriptors that could compromise the security of your resources — for example, avoid including personal or sensitive information.^[tutorial-configure-abac-databricks-on-aws.md]

## Related concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md)
- [ABAC Row Filter Policies](/concepts/abac-row-filter-policies.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Governed tag policy (tag allowed values)

## Sources

- attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
- tutorial-configure-abac-databricks-on-aws.md
- data-discovery-in-unity-catalog-databricks-on-aws.md

# Citations

1. [attribute-based-access-control-in-unity-catalog-databricks-on-aws.md](/references/attribute-based-access-control-in-unity-catalog-databricks-on-aws-23c11bc2.md)
2. [data-discovery-in-unity-catalog-databricks-on-aws.md](/references/data-discovery-in-unity-catalog-databricks-on-aws-a33f291f.md)
3. [tutorial-configure-abac-databricks-on-aws.md](/references/tutorial-configure-abac-databricks-on-aws-cbba5828.md)
