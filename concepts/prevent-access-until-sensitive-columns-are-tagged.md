---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6bf96b7a899b3fe24f8fadf0908b3738ed185da1150af861c7432fff64f3befc
  pageDirectory: concepts
  sources:
    - common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prevent-access-until-sensitive-columns-are-tagged
    - PAUSCAT
  citations:
    - file: common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
title: Prevent access until sensitive columns are tagged
description: A governance pattern that uses a default 'unverified' tag to block access to unclassified data, then automatically switches to column masking once a data steward updates the classification tag.
tags:
  - abac
  - data-classification
  - row-filter
  - column-masking
  - governance
timestamp: "2026-06-19T09:18:00.995Z"
---

# Prevent access until sensitive columns are tagged

**Prevent access until sensitive columns are tagged** is a common governance pattern that controls access to data based on whether it has been classified. The pattern uses a default restrictive tag, a [row filter policy](/concepts/row-filter-policies.md) that blocks access for unverified tables, and a [column mask policy](/concepts/column-mask-policies.md) that protects sensitive columns once classification is complete. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## How the pattern works

The pattern follows four steps:

1. **Apply a default restrictive tag** – Apply a tag like `classification : unverified` to all new objects by default, through automation or through tag inheritance by applying the tag at the catalog or schema level. Any new tables added to the catalog or schema automatically inherit the tag.
2. **Create a row filter that blocks unverified tables** – Create a row filter policy that blocks access to tables tagged `classification : unverified` for all non-admin users.
3. **Create a column mask for reviewed data** – Create a column mask policy that masks sensitive columns on tables where the `classification : unverified` tag is no longer present.
4. **Update the tag when classification is done** – When a data steward completes classification, they update the tag. The blocking policy no longer matches, and the masking policy takes effect.

^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Example: Block access to unverified tables

The following policy uses a row filter function that always returns `FALSE`. It applies to all tables in the catalog `my_catalog` that carry the tag `classification : unverified`. All principals in `account users` are blocked except for the `data_admins` group, which can still access and classify the data.

```sql
-- Block access to unverified tables for all non-admin users
CREATE FUNCTION catalog.schema.block_all() RETURNS BOOLEAN
  RETURN FALSE;

CREATE POLICY block_unverified
ON CATALOG my_catalog
ROW FILTER catalog.schema.block_all
TO `account users` EXCEPT `data_admins`
FOR TABLES
WHEN has_tag_value('classification', 'unverified');
```

^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Example: Mask sensitive columns after classification

Once a table has been classified and its tag updated from `classification : unverified` to something else (e.g. `classification : confidential`), the blocking policy no longer applies. To protect sensitive data, define a column mask policy that takes effect when the `classification : unverified` tag is **not** present.

```sql
CREATE FUNCTION catalog.schema.mask_pii(val STRING)
RETURNS STRING
RETURN '***';

CREATE POLICY mask_reviewed_pii
ON CATALOG my_catalog
COLUMN MASK catalog.schema.mask_pii
TO `account users`
EXCEPT `data_admins`
FOR TABLES
WHEN NOT has_tag_value('classification', 'unverified')
MATCH COLUMNS (has_tag_value('pii', 'name') OR has_tag_value('pii', 'address')) AS m
ON COLUMN m;
```

^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Tag inheritance for safe defaults

To ensure new objects start with the `classification : unverified` tag automatically, apply the tag at the catalog or schema level. All descendants inherit the tag by default. A data steward can later override the inherited tag on individual tables or columns when classification is complete. This approach reduces the need for separate policies per object. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Usage considerations

- The pattern uses row filter and column mask policies only. [ABAC GRANT Policies](/concepts/abac-grant-policy.md) (Beta) currently support only `EXECUTE` on models and cannot be used for this table-based pattern.
- The `EXCEPT` clause in the policy allows data stewards (`data_admins`) to see unverified tables so they can classify them. Adjust the group names to match your governance structure.
- After classification, the blocking policy condition (`has_tag_value('classification', 'unverified')`) is no longer `TRUE`, so the row filter does not apply. The column mask condition (`NOT has_tag_value('classification', 'unverified')`) becomes `TRUE`, and the mask function replaces sensitive column values.

## Related concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – The governance model that enables tag-driven policies
- [Row Filter Policies](/concepts/row-filter-policies.md) – Policies that restrict which rows a user can see
- [Column Mask Policies](/concepts/column-mask-policies.md) – Policies that mask sensitive column values
- [Governed Tags](/concepts/governed-tags.md) – The tags used to trigger policy conditions
- [Tag Inheritance](/concepts/tag-inheritance.md) – Applying tags at a catalog or schema so descendants inherit them
- [ABAC Tagging Taxonomy and Governance](/concepts/abac-tagging-taxonomy-and-governance.md) – Best practices for naming and managing tags
- [ABAC Policy Scoping and Sprawl Prevention](/concepts/abac-policy-scoping-and-sprawl-prevention.md) – How to keep policy counts manageable

## Sources

- common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md

# Citations

1. [common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md](/references/common-patterns-for-row-filtering-and-column-masking-databricks-on-aws-f18db1c1.md)
