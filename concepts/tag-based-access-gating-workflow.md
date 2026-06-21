---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 69122ff74c20470452fe5e8f375178c12059acbb9657ce549a6d9cb080f0ec9e
  pageDirectory: concepts
  sources:
    - common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tag-based-access-gating-workflow
    - TAGW
  citations:
    - file: common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
title: Tag-based access gating workflow
description: "A governance pattern that uses a default restrictive tag (e.g. 'classification : unverified') to block access to unclassified data, then transitions to column masking once a data steward completes classification and updates the tag."
tags:
  - data-governance
  - abac
  - tag-based
  - classification
timestamp: "2026-06-19T17:47:00.145Z"
---

# Tag-based access gating workflow

**Tag-based access gating workflow** is a common [ABAC (Attribute-Based Access Control)](/concepts/abac-attribute-based-access-control.md) pattern on Databricks that uses Unity Catalog tags to progressively control access to data based on its classification status. The workflow enforces a default restrictive policy for unclassified data and then applies finer-grained protections—typically [row filter](/concepts/row-filter-policies.md) and column mask policies—once a data steward assigns a classification tag. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## How it works

The workflow consists of four steps:

1. **Apply a default restrictive tag** to all new objects. A tag like `classification : unverified` can be applied automatically through automation or through [Tag Inheritance](/concepts/tag-inheritance.md) by setting the tag at the catalog or schema level. Any new table added to the catalog or schema inherits the tag. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

2. **Create a row filter policy** that blocks access to tables tagged `classification : unverified`. For example:
   ```sql
   CREATE FUNCTION block_all() RETURNS BOOLEAN RETURN FALSE;
   CREATE POLICY block_unverified
     ON CATALOG my_catalog
     ROW FILTER block_all
     TO `account users` EXCEPT `data_admins`
     FOR TABLES
     WHEN has_tag_value('classification', 'unverified');
   ```
   This ensures non-admin users see no rows from unclassified tables. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

3. **Create a column mask policy** that masks sensitive columns on tables where the `classification : unverified` tag is no longer present. For example:
   ```sql
   CREATE FUNCTION mask_pii(val STRING) RETURNS STRING RETURN '***';
   CREATE POLICY mask_reviewed_pii
     ON CATALOG my_catalog
     COLUMN MASK mask_pii
     TO `account users`
     EXCEPT `data_admins`
     FOR TABLES
     WHEN NOT has_tag_value('classification', 'unverified')
     MATCH COLUMNS (has_tag_value('pii', 'name') OR has_tag_value('pii', 'address')) AS m
     ON COLUMN m;
   ```
   This masks columns with PII tags (e.g., `pii : name`, `pii : address`) for all tables that are no longer marked as `unverified`. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

4. **A data steward reclassifies the data** by updating the tag (e.g., changing `classification : unverified` to `classification : reviewed`). The blocking policy stops matching, and the masking policy takes effect. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Use cases

- **Data discovery & governance**: Prevent access to tables that have not yet been reviewed by a data steward, ensuring that sensitive data is never exposed before classification.
- **Gradual protection**: Once classification is complete, automatically switch from blocking rows to masking sensitive columns, allowing users to see non-sensitive data while protecting PII.
- **Audit & automation**: The workflow can be automated via tag inheritance and periodic reclassification jobs, reducing manual policy maintenance. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Related concepts

- [Row filter policy](/concepts/row-filter-policies.md)
- [Column mask policy](/concepts/column-mask-policies.md)
- [ABAC (Attribute-Based Access Control)](/concepts/abac-attribute-based-access-control.md)
- [Tag Inheritance](/concepts/tag-inheritance.md)
- Unity Catalog tags
- [Data Classification](/concepts/data-classification.md)

## Sources

- common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md

# Citations

1. [common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md](/references/common-patterns-for-row-filtering-and-column-masking-databricks-on-aws-f18db1c1.md)
