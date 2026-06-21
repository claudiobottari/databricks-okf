---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 611929c5cf3508808cf43e338eec27bfaf464600127be9ec75f6f06b39ea344d
  pageDirectory: concepts
  sources:
    - common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tag-based-access-gating-unverified-classification-pattern
    - TAG(CP
  citations:
    - file: common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
title: Tag-based access gating (unverified classification pattern)
description: A governance pattern that blocks access to untagged or unclassified data using a default restrictive tag, then applies column masking after classification is complete, using has_tag_value conditions in policies.
tags:
  - abac
  - data-classification
  - tag-based-access
  - row-filter
timestamp: "2026-06-19T14:19:10.714Z"
---

# Tag-based access gating (unverified classification pattern)

**Tag-based access gating (unverified classification pattern)** is a governance pattern that blocks access to unclassified or unverified data until a data steward has reviewed and tagged it with an appropriate classification. It uses a two-stage approach: first preventing access to untagged objects, then applying column-level masking once classification is complete. This pattern is implemented using [ABAC row filter and column mask policies](/concepts/row-filter-and-column-mask-policies.md) in [Unity Catalog](/concepts/unity-catalog.md).

## Overview

The pattern relies on a default restrictive tag — such as `classification : unverified` — applied to all new objects. By default, a row filter policy blocks access to tables that carry this tag. Once a data steward reviews and updates the tag (for example, changing it to `classification : pii`), the blocking policy no longer matches, and a separate column mask policy takes effect to protect sensitive columns. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

This approach ensures that data is never accessible without appropriate protection. Unverified data is completely blocked; verified data has sensitive columns masked. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Implementation

### Apply the default tag

Apply the `classification : unverified` tag to all new objects, either through automation or through tag inheritance by applying the tag at the catalog or schema level. Any new tables added to the tagged catalog or schema automatically inherit the tag. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

### Create the blocking row filter

Define a row filter policy that blocks access to tables tagged `classification : unverified` for all non-admin users.

```sql
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

### Create the protection column mask

Define a column mask policy that masks sensitive columns once the `classification : unverified` tag is no longer present. The `MATCH COLUMNS` clause targets columns carrying specific PII tags.

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
MATCH COLUMNS (
    has_tag_value('pii', 'name') OR
    has_tag_value('pii', 'address')
) AS m
ON COLUMN m;
```

^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Workflow

1. A new table is created in the catalog or schema and automatically inherits the `classification : unverified` tag.
2. Non-admin users who query the table receive an empty result set because the `block_unverified` row filter blocks all rows.
3. A data steward reviews the table and determines it contains personally identifiable information (PII).
4. The steward updates the tag from `classification : unverified` to `classification : pii` and applies appropriate PII tags (for example, `pii : name`, `pii : address`) to sensitive columns.
5. The blocking policy no longer matches, so rows become visible.
6. The column mask policy now applies, replacing sensitive column values with `***`.

## Considerations

- This pattern requires a two-policy setup: one for blocking unverified data and one for masking verified data. The policies must be carefully ordered so that the blocking policy and masking policy do not conflict. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Related concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Row Filter Policies](/concepts/row-filter-policies.md)
- [Column Mask Policies](/concepts/column-mask-policies.md)
- Tag-based governance
- PII classification
- Data stewardship workflows

## Sources

- common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md

# Citations

1. [common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md](/references/common-patterns-for-row-filtering-and-column-masking-databricks-on-aws-f18db1c1.md)
